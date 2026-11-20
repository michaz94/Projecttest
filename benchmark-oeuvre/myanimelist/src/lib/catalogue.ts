import { sql } from "drizzle-orm";

import { db } from "@/db";
import { classer, type Resultat } from "@/lib/recherche";

/**
 * Un groupe de tags évalué ensemble. Les groupes d'une même famille sont
 * combinés entre eux par ET, ce qui permet d'exprimer par exemple
 * (Supernatural OU Fantasy) ET (Action).
 */
export type Groupe = { noms: string[]; mode: "and" | "or" };

export type Filtres = {
  scoreMin?: number;
  scoreMax?: number;
  volMin?: number;
  volMax?: number;
  anneeMin?: number;
  anneeMax?: number;
  membresMin?: number;
  membresMax?: number;
  statut?: string;
  volInconnu: boolean;
  genreGroupes: Groupe[];
  genresExcl: string[];
  themeGroupes: Groupe[];
  themesExcl: string[];
  magazines: string[];
  magazinesExcl: string[];
  tri: string;
  sens: "asc" | "desc";
  page: number;
  parPage: number;
  /**
   * Œuvres retenues par la recherche par nom, de la plus à la moins pertinente.
   * Absent = pas de recherche par nom. Présent mais vide = recherche sans résultat.
   */
  ids?: number[];
};

export type Ligne = {
  mal_id: number;
  titre: string;
  volumes: number | null;
  chapitres: number | null;
  score: number | null;
  scored_by: number | null;
  members: number | null;
  annee_debut: number | null;
  annee_fin: number | null;
  statut: string;
  url: string;
  genres: string | null;
  themes: string | null;
  magazines: string | null;
};

const TRIS: Record<string, string> = {
  score: "o.score",
  volumes: "o.volumes",
  members: "o.members",
  scored_by: "o.scored_by",
  annee: "o.annee_debut",
  titre: "o.titre",
};

function tagClause(
  type: string,
  noms: string[],
  mode: "and" | "or",
  negatif = false,
) {
  if (noms.length === 0) return null;
  if (negatif || mode === "or") {
    // Liste explicite : Drizzle ne sérialise pas un tableau JS en tableau Postgres.
    const liste = sql.join(
      noms.map((n) => sql`${n}`),
      sql`, `,
    );
    const inner = sql`select 1 from oeuvre_tags ot join tags t on t.id = ot.tag_id
      where ot.oeuvre_id = o.mal_id and t.type = ${type} and t.nom in (${liste})`;
    return negatif ? sql`not exists (${inner})` : sql`exists (${inner})`;
  }
  const parts = noms.map(
    (n) => sql`exists (select 1 from oeuvre_tags ot join tags t on t.id = ot.tag_id
      where ot.oeuvre_id = o.mal_id and t.type = ${type} and t.nom = ${n})`,
  );
  return sql.join(parts, sql` and `);
}

function whereSql(f: Filtres) {
  const c = [sql`1 = 1`];
  if (f.scoreMin !== undefined) c.push(sql`o.score >= ${f.scoreMin}`);
  if (f.scoreMax !== undefined) c.push(sql`o.score <= ${f.scoreMax}`);
  if (f.anneeMin !== undefined) c.push(sql`o.annee_debut >= ${f.anneeMin}`);
  if (f.anneeMax !== undefined) c.push(sql`o.annee_debut <= ${f.anneeMax}`);
  if (f.membresMin !== undefined) c.push(sql`o.members >= ${f.membresMin}`);
  if (f.membresMax !== undefined) c.push(sql`o.members <= ${f.membresMax}`);
  if (f.statut) c.push(sql`o.statut = ${f.statut}`);

  if (f.volMin !== undefined || f.volMax !== undefined) {
    const bornes = [sql`o.volumes is not null`];
    if (f.volMin !== undefined) bornes.push(sql`o.volumes >= ${f.volMin}`);
    if (f.volMax !== undefined) bornes.push(sql`o.volumes <= ${f.volMax}`);
    const dansBornes = sql.join(bornes, sql` and `);
    c.push(
      f.volInconnu
        ? sql`((${dansBornes}) or o.volumes is null)`
        : sql`(${dansBornes})`,
    );
  } else if (!f.volInconnu && !f.ids) {
    // Une recherche par nom ne doit pas masquer une série en cours (volumes vides).
    c.push(sql`o.volumes is not null`);
  }

  if (f.ids) {
    c.push(
      f.ids.length
        ? sql`o.mal_id in (${sql.join(f.ids.map((i) => sql`${i}`), sql`, `)})`
        : sql`false`,
    );
  }

  // Chaque groupe est une condition supplémentaire : les groupes se cumulent par ET.
  for (const g of f.genreGroupes) {
    const t = tagClause("genre", g.noms, g.mode);
    if (t) c.push(sql`(${t})`);
  }
  for (const g of f.themeGroupes) {
    const t = tagClause("theme", g.noms, g.mode);
    if (t) c.push(sql`(${t})`);
  }

  const autres = [
    tagClause("genre", f.genresExcl, "or", true),
    tagClause("theme", f.themesExcl, "or", true),
    tagClause("magazine", f.magazines, "or"),
    tagClause("magazine", f.magazinesExcl, "or", true),
  ].filter(Boolean);
  for (const t of autres) c.push(sql`(${t})`);

  return sql.join(c, sql` and `);
}

export async function compter(f: Filtres) {
  const w = whereSql(f);
  const r = await db.execute<{ n: number }>(
    sql`select count(*)::int as n from oeuvres o where ${w}`,
  );
  return r.rows[0]?.n ?? 0;
}

export async function chercher(f: Filtres) {
  const w = whereSql(f);
  const col = TRIS[f.tri] ?? "o.score";
  const dir = f.sens === "asc" ? "asc" : "desc";
  // Tri « pertinence » : l'ordre de la recherche par nom (les ids sont des entiers
  // produits par le classeur, jamais du texte saisi).
  const parPertinence = f.tri === "pertinence" && f.ids && f.ids.length > 0;
  const ordre = parPertinence
    ? sql.raw(
        `array_position(ARRAY[${f.ids!.map((i) => Math.trunc(i)).join(",")}]::int[], o.mal_id) asc`,
      )
    : sql.raw(`${col} ${dir} nulls last, o.mal_id asc`);
  const taille = Math.min(Math.max(f.parPage, 10), 500);
  const saut = Math.max(f.page, 0) * taille;

  const lignes = await db.execute<Ligne>(sql`
    select o.mal_id, o.titre, o.volumes, o.chapitres, o.score, o.scored_by,
           o.members, o.annee_debut, o.annee_fin, o.statut, o.url,
           (select string_agg(t.nom, ', ' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type = 'genre') as genres,
           (select string_agg(t.nom, ', ' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type = 'theme') as themes,
           (select string_agg(t.nom, ', ' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type = 'magazine') as magazines
      from oeuvres o
     where ${w}
     order by ${ordre}
     limit ${taille} offset ${saut}
  `);
  return lignes.rows;
}

export type Stat = { nom: string; n: number };

export async function statistiques(f: Filtres) {
  const w = whereSql(f);

  const repartition = await db.execute<{ type: string; nom: string; n: number }>(sql`
    with s as (select o.mal_id from oeuvres o where ${w})
    select t.type, t.nom, count(*)::int as n
      from s join oeuvre_tags ot on ot.oeuvre_id = s.mal_id
             join tags t on t.id = ot.tag_id
     where t.type in ('genre','theme','magazine','demographic')
     group by t.type, t.nom
     order by n desc
  `);

  const agg = await db.execute<{
    total: number;
    avec_vol: number;
    vol_moy: number | null;
    vol_med: number | null;
    vol_max: number | null;
    score_moy: number | null;
    membres_moy: number | null;
    membres_med: number | null;
    termines: number;
  }>(sql`
    with s as (select o.* from oeuvres o where ${w})
    select count(*)::int as total,
           count(volumes)::int as avec_vol,
           round(avg(volumes)::numeric, 1)::float8 as vol_moy,
           percentile_cont(0.5) within group (order by volumes)::float8 as vol_med,
           max(volumes)::int as vol_max,
           round(avg(score)::numeric, 2)::float8 as score_moy,
           round(avg(members)::numeric, 0)::float8 as membres_moy,
           percentile_cont(0.5) within group (order by members)::float8 as membres_med,
           count(*) filter (where statut = 'terminé')::int as termines
      from s
  `);

  const tranches = await db.execute<{ tranche: string; n: number }>(sql`
    with s as (select o.volumes from oeuvres o where ${w})
    select case
             when volumes is null then 'inconnu'
             when volumes <= 3  then '1-3'
             when volumes <= 7  then '4-7'
             when volumes <= 14 then '8-14'
             when volumes <= 29 then '15-29'
             when volumes <= 59 then '30-59'
             else '60+'
           end as tranche, count(*)::int as n
      from s group by 1
  `);

  const decennies = await db.execute<{ dec: number; n: number }>(sql`
    with s as (select o.annee_debut from oeuvres o where ${w})
    select (annee_debut / 10 * 10)::int as dec, count(*)::int as n
      from s where annee_debut is not null group by 1 order by 1
  `);

  const par = (type: string): Stat[] =>
    repartition.rows
      .filter((r) => r.type === type)
      .map((r) => ({ nom: r.nom, n: r.n }));

  const a = agg.rows[0];
  return {
    total: a?.total ?? 0,
    avecVol: a?.avec_vol ?? 0,
    volMoy: a?.vol_moy ?? null,
    volMed: a?.vol_med ?? null,
    volMax: a?.vol_max ?? null,
    scoreMoy: a?.score_moy ?? null,
    membresMoy: a?.membres_moy ?? null,
    membresMed: a?.membres_med ?? null,
    termines: a?.termines ?? 0,
    genres: par("genre"),
    themes: par("theme"),
    magazines: par("magazine"),
    demographies: par("demographic"),
    tranches: tranches.rows,
    decennies: decennies.rows,
  };
}

export async function tousLesTags(type: string) {
  const r = await db.execute<{ nom: string; n: number }>(sql`
    select t.nom, count(ot.oeuvre_id)::int as n
      from tags t left join oeuvre_tags ot on ot.tag_id = t.id
     where t.type = ${type}
     group by t.nom having count(ot.oeuvre_id) > 0
     order by count(ot.oeuvre_id) desc, t.nom asc
  `);
  return r.rows;
}

/**
 * Recherche par nom, tolérante, sur le titre et le titre anglais.
 * Renvoie null si la requête est trop courte (moins de 2 caractères utiles).
 * Les 2 951 titres sont lus à chaque recherche : c'est quelques millisecondes.
 */
export async function rechercherNoms(requete: string): Promise<Resultat[] | null> {
  const r = await db.execute<{ id: number; titre: string; titre_en: string; poids: number }>(
    sql`select mal_id as id, titre, titre_en, coalesce(members, 0) as poids from oeuvres`,
  );
  return classer(
    requete,
    r.rows.map((o) => ({ id: o.id, titres: [o.titre, o.titre_en], poids: o.poids })),
  );
}

export async function etatImport() {
  const r = await db.execute<{ total: number; detaillees: number }>(sql`
    select (select count(*) from oeuvres)::int as total,
           (select count(distinct oeuvre_id) from oeuvre_tags)::int as detaillees
  `);
  return r.rows[0] ?? { total: 0, detaillees: 0 };
}
