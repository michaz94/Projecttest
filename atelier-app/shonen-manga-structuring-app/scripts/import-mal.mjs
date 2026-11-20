/**
 * Importe un corpus MAL dans Postgres.
 *
 * Deux étapes :
 *   1. `list`   — parcourt les pages de recherche MAL (50 œuvres/page) et
 *                 enregistre les identifiants + colonnes de la liste.
 *   2. `detail` — visite la fiche de chaque œuvre pas encore détaillée pour
 *                 récupérer genres, thèmes, démographie, magazine, auteurs.
 *
 * Reprenable : relancer `detail` continue là où l'import s'était arrêté.
 *
 * Usage :
 *   node scripts/import-mal.mjs list   [pages]
 *   node scripts/import-mal.mjs detail [limite]
 *
 * Source : pages publiques MyAnimeList. Un délai est respecté entre les
 * requêtes. Ce script ne contourne aucune protection.
 */
import pg from "pg";

const UA =
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36";
const DB =
  process.env.DATABASE_URL ??
  "postgresql://postgres:postgres@127.0.0.1:5432/app_db";

const pool = new pg.Pool({ connectionString: DB });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function get(url, tries = 3) {
  for (let i = 0; i < tries; i++) {
    try {
      const res = await fetch(url, { headers: { "User-Agent": UA } });
      if (res.ok) return await res.text();
      if (res.status === 404) return null;
    } catch {
      /* réessai */
    }
    await sleep(2000 * (i + 1));
  }
  return null;
}

const strip = (s) => s.replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
const intOrNull = (s) => {
  const n = Number.parseInt(String(s).replace(/[^\d]/g, ""), 10);
  return Number.isFinite(n) ? n : null;
};

/* ------------------------------------------------------------------ étape 1 */

async function importList(pages) {
  // c[]=a,b,g,c,d,f => colonnes Type, Vol., Chap., Score, Start Date, Members
  const base =
    "https://myanimelist.net/manga.php?type=1&score=1&sy=1980" +
    "&c%5B0%5D=a&c%5B1%5D=b&c%5B2%5D=g&c%5B3%5D=c&c%5B4%5D=d&c%5B5%5D=f" +
    "&genre%5B0%5D=27&o=3&w=1&show=";
  let total = 0;
  for (let p = 0; p < pages; p++) {
    const html = await get(base + p * 50);
    if (!html) {
      console.log(`page ${p}: échec`);
      continue;
    }
    const rows = [...html.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)];
    let found = 0;
    for (const [, row] of rows) {
      const idm = row.match(/myanimelist\.net\/manga\/(\d+)\//);
      if (!idm) continue;
      const malId = Number(idm[1]);
      const tm = row.match(
        /<a[^>]*class="hoverinfo_trigger fw-b"[^>]*>\s*<strong>([\s\S]*?)<\/strong>/,
      );
      const titre = tm ? strip(tm[1]) : null;
      if (!titre) continue;
      // cellules centrées = colonnes de données (hors vignette et titre)
      const tds = [...row.matchAll(/<td class="borderClass ac[^"]*"[^>]*>([\s\S]*?)<\/td>/g)].map(
        (m) => strip(m[1]),
      );
      // [type] [vol] [chap] [score] [date] [membres]
      const vol = intOrNull(tds[1]);
      const chap = intOrNull(tds[2]);
      const score = Number.parseFloat(tds[3]);
      const dm = (tds[4] || "").match(/(\d{2})-(\d{2})-(\d{2})/);
      let annee = null;
      if (dm) {
        const yy = Number(dm[3]);
        annee = yy > 30 ? 1900 + yy : 2000 + yy;
      }
      const members = intOrNull(tds[5]);
      await pool.query(
        `insert into oeuvres (mal_id, titre, volumes, chapitres, score, annee_debut, members, url)
         values ($1,$2,$3,$4,$5,$6,$7,$8)
         on conflict (mal_id) do update set
           titre=excluded.titre, volumes=excluded.volumes, chapitres=excluded.chapitres,
           score=excluded.score, annee_debut=excluded.annee_debut, members=excluded.members`,
        [
          malId,
          titre,
          vol,
          chap,
          Number.isFinite(score) ? score : null,
          annee,
          members,
          `https://myanimelist.net/manga/${malId}`,
        ],
      );
      found++;
      total++;
    }
    console.log(`page ${p} → ${found} œuvres (cumul ${total})`);
    if (found === 0) break;
    await sleep(1200);
  }
  console.log(`liste terminée : ${total} lignes traitées`);
}

/* ------------------------------------------------------------------ étape 2 */

function extractBlock(html, label) {
  const re = new RegExp(
    `<span class="dark_text">${label}s?:?</span>([\\s\\S]*?)</div>`,
  );
  const m = html.match(re);
  return m ? m[1] : null;
}

function extractLinks(block) {
  if (!block) return [];
  return [...block.matchAll(/<a [^>]*>([^<]+)<\/a>/g)]
    .map((m) => strip(m[1]))
    .filter(Boolean);
}

async function tagId(type, nom) {
  const r = await pool.query(
    `insert into tags (type, nom) values ($1,$2)
     on conflict (type, nom) do update set nom=excluded.nom returning id`,
    [type, nom],
  );
  return r.rows[0].id;
}

async function importDetail(limit) {
  const { rows } = await pool.query(
    `select o.mal_id from oeuvres o
     where not exists (select 1 from oeuvre_tags ot where ot.oeuvre_id = o.mal_id)
     order by o.score desc nulls last limit $1`,
    [limit],
  );
  console.log(`${rows.length} fiches a detailler`);

  // 3 requetes simultanees, ~900 ms par requete et par worker :
  // environ 3 requetes/seconde, soit la limite de l'API Jikan officielle.
  const PARALLELE = 3;
  const PAUSE = 900;
  let curseur = 0;
  let ok = 0;
  let echecs = 0;

  async function traiter(id) {
    const html = await get(`https://myanimelist.net/manga/${id}`);
    if (!html) {
      echecs++;
      return;
    }
    const sets = [
      ["genre", extractLinks(extractBlock(html, "Genre"))],
      ["theme", extractLinks(extractBlock(html, "Theme"))],
      ["demographic", extractLinks(extractBlock(html, "Demographic"))],
      ["magazine", extractLinks(extractBlock(html, "Serialization"))],
      ["auteur", extractLinks(extractBlock(html, "Author"))],
    ];
    for (const [type, noms] of sets) {
      for (const nom of [...new Set(noms)]) {
        if (!nom || nom.toLowerCase() === "none found") continue;
        const tid = await tagId(type, nom);
        await pool.query(
          `insert into oeuvre_tags (oeuvre_id, tag_id) values ($1,$2)
           on conflict do nothing`,
          [id, tid],
        );
      }
    }
    const pub = extractBlock(html, "Published");
    let fin = null;
    let statut = "";
    if (pub) {
      const t = strip(pub);
      const yrs = [...t.matchAll(/(\d{4})/g)].map((m) => Number(m[1]));
      if (/\?/.test(t)) statut = "en cours";
      else if (yrs.length >= 2) {
        fin = yrs[yrs.length - 1];
        statut = "termine";
      } else if (yrs.length === 1) statut = "en cours";
    }
    const sb = html.match(/<span itemprop="ratingCount"[^>]*>(\d+)<\/span>/);
    const en = html.match(/<span class="dark_text">English:<\/span>([^<]+)</);
    await pool.query(
      `update oeuvres set annee_fin=coalesce($2, annee_fin),
         statut=case when $3='' then statut else $3 end,
         scored_by=coalesce($4, scored_by),
         titre_en=case when $5='' then titre_en else $5 end
       where mal_id=$1`,
      [id, fin, statut === "termine" ? "terminé" : statut, sb ? Number(sb[1]) : null, en ? strip(en[1]) : ""],
    );
    ok++;
    if (ok % 100 === 0) console.log(`  ${ok}/${rows.length}`);
  }

  async function worker() {
    while (curseur < rows.length) {
      const i = curseur++;
      await traiter(rows[i].mal_id);
      await sleep(PAUSE);
    }
  }

  await Promise.all(Array.from({ length: PARALLELE }, () => worker()));
  console.log(`details : ${ok} reussites, ${echecs} echecs`);
}

const [, , cmd, argRaw] = process.argv;
const arg = Number.parseInt(argRaw ?? "", 10);
if (cmd === "list") await importList(Number.isFinite(arg) ? arg : 10);
else if (cmd === "detail") await importDetail(Number.isFinite(arg) ? arg : 100);
else console.log("usage: node scripts/import-mal.mjs list|detail [n]");
await pool.end();
