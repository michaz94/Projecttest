import Link from "next/link";

import { Chips, Segmented } from "@/components/chips";
import { PageHeader } from "@/components/ui";
import { analyser, construireDico, versTexte } from "@/lib/query";
import { PALIERS, palierScore, styleScore } from "@/lib/score";
import { SEUIL_EXACT } from "@/lib/recherche";
import {
  chercher,
  compter,
  etatImport,
  rechercherNoms,
  statistiques,
  tousLesTags,
  type Filtres,
  type Groupe,
  type Stat,
} from "@/lib/catalogue";

export const dynamic = "force-dynamic";

type SP = Record<string, string | string[] | undefined>;

const arr = (v: string | string[] | undefined): string[] =>
  v === undefined ? [] : Array.isArray(v) ? v.filter(Boolean) : v ? [v] : [];
const one = (v: string | string[] | undefined): string =>
  Array.isArray(v) ? (v[0] ?? "") : (v ?? "");
const numOr = (v: string | string[] | undefined): number | undefined => {
  const n = Number.parseFloat(one(v));
  return Number.isFinite(n) ? n : undefined;
};

/** Trois groupes par famille : suffisant pour toute requête réaliste. */
const RANGS = [1, 2, 3] as const;

function lireGroupes(sp: SP, prefixe: "g" | "t"): Groupe[] {
  return RANGS.map((r) => ({
    noms: arr(sp[`${prefixe}${r}`]),
    mode: one(sp[`${prefixe}${r}m`]) === "and" ? "and" : "or",
  })) as Groupe[];
}

function lireFiltres(sp: SP, viaRequete?: ReturnType<typeof analyser>): Filtres {
  return {
    scoreMin: numOr(sp.scoreMin),
    scoreMax: numOr(sp.scoreMax),
    volMin: numOr(sp.volMin),
    volMax: numOr(sp.volMax),
    anneeMin: numOr(sp.anneeMin),
    anneeMax: numOr(sp.anneeMax),
    membresMin: numOr(sp.membresMin),
    membresMax: numOr(sp.membresMax),
    statut: one(sp.statut),
    volInconnu: one(sp.volInconnu) === "1",
    genreGroupes: viaRequete ? viaRequete.genreGroupes : lireGroupes(sp, "g"),
    genresExcl: viaRequete ? viaRequete.genresExcl : arr(sp.gx),
    themeGroupes: viaRequete ? viaRequete.themeGroupes : lireGroupes(sp, "t"),
    themesExcl: viaRequete ? viaRequete.themesExcl : arr(sp.tx),
    magazines: viaRequete ? viaRequete.magazines : arr(sp.m),
    magazinesExcl: viaRequete ? viaRequete.magazinesExcl : arr(sp.mx),
    tri: one(sp.tri) || "score",
    sens: one(sp.sens) === "asc" ? "asc" : "desc",
    page: Math.max(0, Number.parseInt(one(sp.page) || "0", 10) || 0),
    parPage: numOr(sp.parPage) ?? 50,
  };
}

function lienPage(sp: SP, page: number): string {
  const p = new URLSearchParams();
  for (const [k, v] of Object.entries(sp)) {
    if (k === "page") continue;
    for (const x of arr(v)) p.append(k, x);
  }
  if (page > 0) p.set("page", String(page));
  const q = p.toString();
  return q ? `/catalogue?${q}` : "/catalogue";
}

function nbFiltresActifs(f: Filtres): number {
  let n = 0;
  for (const k of [
    f.scoreMin, f.scoreMax, f.volMin, f.volMax,
    f.anneeMin, f.anneeMax, f.membresMin, f.membresMax,
  ]) if (k !== undefined) n++;
  if (f.statut) n++;
  for (const g of [...f.genreGroupes, ...f.themeGroupes]) n += g.noms.length;
  return n + f.genresExcl.length + f.themesExcl.length +
    f.magazines.length + f.magazinesExcl.length;
}

/** Traduit les filtres en une expression booléenne lisible. */
function expression(f: Filtres): string | null {
  const morceaux: string[] = [];
  const bloc = (groupes: Groupe[]) =>
    groupes
      .filter((g) => g.noms.length > 0)
      .map((g) =>
        g.noms.length === 1
          ? g.noms[0]
          : `(${g.noms.join(g.mode === "and" ? " ET " : " OU ")})`,
      );
  morceaux.push(...bloc(f.genreGroupes), ...bloc(f.themeGroupes));
  if (f.magazines.length) morceaux.push(`(${f.magazines.join(" OU ")})`);
  const positif = morceaux.join(" ET ");
  const exclus = [...f.genresExcl, ...f.themesExcl, ...f.magazinesExcl];
  const negatif = exclus.length ? `SAUF ${exclus.join(", ")}` : "";
  const total = [positif, negatif].filter(Boolean).join(" · ");
  return total || null;
}

const nf = new Intl.NumberFormat("fr-FR");
const compact = (n: number | null) =>
  n === null
    ? "—"
    : n >= 1000
      ? `${Math.round(n / 1000)} k`
      : String(n);

function Pagination({
  sp, page, pages, total, debut, fin,
}: {
  sp: SP; page: number; pages: number; total: number; debut: number; fin: number;
}) {
  if (total === 0) return null;
  const fenetre: number[] = [];
  const from = Math.max(0, Math.min(page - 2, pages - 5));
  for (let i = from; i < Math.min(pages, from + 5); i++) fenetre.push(i);

  const btn =
    "inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg border border-zinc-700 px-3 text-sm text-zinc-300 active:bg-zinc-800";
  const actif =
    "inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg bg-zinc-100 px-3 text-sm font-medium text-zinc-900";

  return (
    <nav className="mt-4">
      <p className="mb-2 text-xs text-zinc-500">
        {nf.format(debut)}–{nf.format(fin)} sur {nf.format(total)}
      </p>
      <div className="flex flex-wrap items-center gap-1.5">
        {page > 0 ? (
          <Link href={lienPage(sp, page - 1)} className={btn} rel="prev">‹ Préc.</Link>
        ) : null}
        {fenetre.map((i) => (
          <Link key={i} href={lienPage(sp, i)} className={i === page ? actif : btn}
            aria-current={i === page ? "page" : undefined}>
            {i + 1}
          </Link>
        ))}
        {page < pages - 1 ? (
          <Link href={lienPage(sp, page + 1)} className={btn} rel="next">Suiv. ›</Link>
        ) : null}
      </div>
    </nav>
  );
}

function Barre({ stats, total }: { stats: Stat[]; total: number }) {
  const max = stats[0]?.n ?? 1;
  return (
    <ul className="space-y-1.5">
      {stats.slice(0, 12).map((s) => (
        <li key={s.nom} className="text-xs">
          <div className="flex items-baseline justify-between gap-2">
            <span className="truncate text-zinc-400" title={s.nom}>{s.nom}</span>
            <span className="shrink-0 tabular-nums text-zinc-500">
              {total ? ((100 * s.n) / total).toFixed(0) : 0}%
              <span className="ml-1 text-zinc-600">({s.n})</span>
            </span>
          </div>
          <span className="mt-0.5 block h-1.5 overflow-hidden rounded-sm bg-zinc-800">
            <span className="block h-full bg-sky-500/60"
              style={{ width: `${Math.max(2, (100 * s.n) / max)}%` }} />
          </span>
        </li>
      ))}
    </ul>
  );
}

const champ =
  "w-full min-h-11 rounded-lg border border-zinc-700 bg-field px-3 text-base sm:text-sm text-zinc-100 focus:border-zinc-100 focus:outline-none";

function Duo({
  label, a, b, sp, step, placeholders = ["min", "max"],
}: {
  label: string; a: string; b: string; sp: SP; step?: string;
  placeholders?: [string, string];
}) {
  return (
    <div>
      <span className="mb-1.5 block text-xs font-medium text-zinc-400">{label}</span>
      <div className="flex items-center gap-2">
        <input name={a} type="number" step={step} inputMode="decimal"
          placeholder={placeholders[0]} defaultValue={one(sp[a])} className={champ} />
        <span className="text-zinc-600">–</span>
        <input name={b} type="number" step={step} inputMode="decimal"
          placeholder={placeholders[1]} defaultValue={one(sp[b])} className={champ} />
      </div>
    </div>
  );
}

/**
 * Un groupe de tags, replié ou déplié.
 * Le résumé reste lisible fermé : mode ET/OU et tags déjà choisis.
 * Ouvert d'office si le groupe contient une sélection.
 */
function GroupeTags({
  titre, prefixe, rang, options, groupe, limite,
}: {
  titre: string; prefixe: "g" | "t"; rang: number;
  options: { nom: string; n: number }[]; groupe: Groupe;
  limite?: number;
}) {
  const choisis = groupe.noms.length;
  return (
    <details open={choisis > 0}
      className="group/g rounded-lg border border-zinc-800 bg-zinc-950/40">
      <summary className="flex min-h-12 cursor-pointer list-none items-center gap-2 px-3 select-none">
        <span className="inline-block text-vermilion transition-transform group-open/g:rotate-90">›</span>
        <span className="text-[13px] font-semibold text-zinc-200">{titre}</span>
        {choisis > 0 ? (
          <>
            <span className="rounded-[3px] bg-zinc-100 px-1.5 py-0.5 font-mono text-[10px] font-semibold text-zinc-900">
              {groupe.mode === "and" ? "ET" : "OU"}
            </span>
            <span className="min-w-0 flex-1 truncate text-xs text-zinc-500">
              {groupe.noms.join(", ")}
            </span>
            <span className="shrink-0 font-mono text-[10px] font-semibold text-zinc-500">
              {choisis}
            </span>
          </>
        ) : (
          <span className="text-xs text-zinc-600">vide</span>
        )}
      </summary>
      <div className="border-t border-zinc-800 p-3">
        <div className="mb-2.5 flex items-center justify-between gap-2">
          <span className="text-[11px] text-zinc-500">Combiner les tags du groupe en</span>
          <Segmented name={`${prefixe}${rang}m`} value={groupe.mode}
            options={[{ v: "or", label: "OU" }, { v: "and", label: "ET" }]} />
        </div>
        <Chips name={`${prefixe}${rang}`} options={options} selected={groupe.noms} limite={limite} />
      </div>
    </details>
  );
}

/** Famille de groupes (Genres, Thèmes…), dépliable, avec le nombre de tags choisis. */
function Famille({
  titre, choisis, children, ouvert,
}: {
  titre: string; choisis: number; children: React.ReactNode; ouvert?: boolean;
}) {
  return (
    <details open={ouvert ?? choisis > 0}
      className="group/f rounded-lg border border-zinc-700 bg-zinc-900">
      <summary className="flex min-h-12 cursor-pointer list-none items-center gap-2 px-3.5 select-none">
        <span className="inline-block text-vermilion transition-transform group-open/f:rotate-90">›</span>
        <span className="font-display text-sm font-bold text-zinc-100">{titre}</span>
        {choisis > 0 ? (
          <span className="rounded-full bg-vermilion px-2 py-0.5 font-mono text-[10px] font-bold text-white">
            {choisis}
          </span>
        ) : null}
      </summary>
      <div className="space-y-2 border-t border-zinc-800 p-2.5">{children}</div>
    </details>
  );
}

/** Filtres numériques que les barres de recherche doivent conserver. */
const CLES_FILTRES = [
  "scoreMin", "scoreMax", "volMin", "volMax", "anneeMin", "anneeMax",
  "membresMin", "membresMax", "statut", "volInconnu", "tri", "sens", "parPage",
];

/**
 * Reporte des paramètres dans un formulaire GET. Un formulaire GET n'envoie que
 * ses propres champs : sans cela, soumettre une barre de recherche ferait
 * perdre tous les autres filtres.
 */
function Cache({ sp, garder }: { sp: SP; garder: string[] }) {
  return (
    <>
      {garder.flatMap((k) =>
        arr(sp[k]).map((v, i) => (
          <input key={`${k}-${i}`} type="hidden" name={k} value={v} />
        )),
      )}
    </>
  );
}

/** Signale une correspondance par nom qui n'est pas exacte. */
function Approx() {
  return (
    <span
      title="Correspondance approchée : le titre ressemble à votre saisie sans la contenir telle quelle."
      className="ml-1.5 inline-flex items-center rounded-[3px] bg-amber-500/15 px-1 py-0.5 align-middle font-mono text-[9px] leading-none font-semibold tracking-wider text-amber-300 uppercase ring-1 ring-amber-500/30 ring-inset"
    >
      approx.
    </span>
  );
}

/** Tuile de score colorée selon le palier. Le chiffre y figure toujours. */
function TuileScore({ score, taille = "md" }: { score: number | null; taille?: "md" | "sm" }) {
  const dim = taille === "md" ? "size-12 text-lg" : "h-7 min-w-11 px-1.5 text-[13px]";
  return (
    <span
      role="img"
      aria-label={score === null ? "Score inconnu" : `Score ${score.toFixed(2)}, ${palierScore(score).libelle}`}
      style={styleScore(score)}
      className={`inline-flex shrink-0 flex-col items-center justify-center rounded-md border font-display leading-none font-extrabold tabular-nums ${dim}`}
    >
      {score === null ? "—" : score.toFixed(taille === "md" ? 1 : 2)}
    </span>
  );
}

/** Légende repliable du code couleur. */
function LegendeScores() {
  return (
    <details className="group/l mb-3 rounded-lg border border-zinc-700 bg-zinc-900">
      <summary className="flex min-h-11 cursor-pointer list-none items-center gap-2 px-3 text-xs font-semibold text-zinc-300 select-none">
        <span className="inline-block text-vermilion transition-transform group-open/l:rotate-90">›</span>
        Code couleur des scores
        <span className="ml-auto flex gap-0.5" aria-hidden>
          {PALIERS.map((p) => (
            <span key={p.id} style={{ backgroundColor: p.fond }} className="size-2.5 rounded-sm" />
          ))}
        </span>
      </summary>
      <ul className="grid grid-cols-2 gap-x-3 gap-y-1.5 border-t border-zinc-800 p-3 sm:grid-cols-3">
        {PALIERS.map((p) => (
          <li key={p.id} className="flex items-center gap-2 text-xs text-zinc-400">
            <span style={{ backgroundColor: p.fond, borderColor: p.bord }}
              className="size-4 shrink-0 rounded border" />
            {p.libelle}
          </li>
        ))}
      </ul>
    </details>
  );
}

function PanneauStat({
  titre, children, ouvertMobile = false,
}: {
  titre: string; children: React.ReactNode; ouvertMobile?: boolean;
}) {
  const entete = "text-xs font-semibold tracking-wide text-zinc-400 uppercase";
  return (
    <>
      <details open={ouvertMobile}
        className="rounded-xl border border-zinc-800 bg-zinc-900/60 lg:hidden">
        <summary className={`flex min-h-12 cursor-pointer list-none items-center justify-between px-4 select-none ${entete}`}>
          {titre}
          <span className="text-zinc-600">▾</span>
        </summary>
        <div className="px-4 pb-4">{children}</div>
      </details>
      <div className="hidden rounded-xl border border-zinc-800 bg-zinc-900/60 p-4 lg:block">
        <h2 className={`mb-3 ${entete}`}>{titre}</h2>
        {children}
      </div>
    </>
  );
}

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<SP>;
}) {
  const sp = await searchParams;

  const [genresDispo, themesDispo, magsDispo, etat] = await Promise.all([
    tousLesTags("genre"),
    tousLesTags("theme"),
    tousLesTags("magazine"),
    etatImport(),
  ]);

  const requete = one(sp.q).trim();
  const dico = construireDico([
    { type: "genre", tags: genresDispo },
    { type: "theme", tags: themesDispo },
    { type: "magazine", tags: magsDispo },
  ]);
  const resolu = requete ? analyser(requete, dico) : undefined;

  // Recherche par nom : classe les œuvres, puis restreint le catalogue à ce classement.
  const nom = one(sp.n).trim();
  const trouves = nom ? await rechercherNoms(nom) : null; // null = absente ou trop courte
  const scoresNom = new Map((trouves ?? []).map((t) => [t.id, t.score]));

  const f = lireFiltres(sp, resolu);
  if (trouves) {
    f.ids = trouves.map((t) => t.id);
    if (!one(sp.tri)) f.tri = "pertinence"; // sans choix explicite : le plus pertinent d'abord
  }
  if (f.tri === "pertinence" && !f.ids) f.tri = "score"; // « pertinence » n'a de sens qu'avec un nom
  const approx = (id: number) => {
    const sc = scoresNom.get(id);
    return sc !== undefined && sc < SEUIL_EXACT ? <Approx /> : null;
  };
  const actifs = nbFiltresActifs(f);
  const expr = expression(f);
  // Pré-remplit la barre à partir des puces quand aucune requête n'est saisie
  const texteBarre = requete || versTexte(f);
  // Les puces attendent toujours 3 groupes ; une requête texte peut en produire moins.
  const vide: Groupe = { noms: [], mode: "or" };
  const gAff = RANGS.map((r) => f.genreGroupes[r - 1] ?? vide);
  const tAff = RANGS.map((r) => f.themeGroupes[r - 1] ?? vide);

  const [lignes, stats, totalFiltre] = await Promise.all([
    chercher(f), statistiques(f), compter(f),
  ]);
  const pages = Math.max(1, Math.ceil(totalFiltre / f.parPage));
  const debut = totalFiltre === 0 ? 0 : f.page * f.parPage + 1;
  const fin = Math.min(totalFiltre, f.page * f.parPage + lignes.length);
  const enCours = etat.detaillees < etat.total;

  return (
    <>
      <PageHeader
        kicker="Étude"
        titre="Catalogue"
        chapo="Corpus MyAnimeList : manga, démographie shōnen, débuts à partir de 1980. Les filtres de genres et de thèmes sont organisés en groupes : chaque groupe a son propre ET/OU, et les groupes se combinent par ET."
        precision="MAL classe « Shounen » comme démographie de magazine, pas comme genre narratif : le corpus contient donc des comédies et des tranches de vie. Membres = personnes ayant l'œuvre dans leur liste, quel que soit le statut ; ce n'est ni une vente ni une lecture."
      />

      <div className={`mb-4 rounded-xl border px-3 py-2.5 text-xs leading-relaxed ${
        enCours ? "border-amber-900/50 bg-amber-950/20 text-zinc-300"
                : "border-zinc-800 bg-zinc-900/40 text-zinc-500"}`}>
        <div>
          {nf.format(etat.total)} œuvres · {nf.format(etat.detaillees)} avec genres et magazine
          {" · "}
          <a href="/api/catalogue/oeuvres" target="_blank" rel="noreferrer"
            className="text-sky-400 active:opacity-70">
            voir JSON
          </a>
          {" · "}
          <Link href="/api/catalogue/json?download=1" className="text-sky-400 active:opacity-70">
            télécharger JSON
          </Link>
          {" · "}
          <Link href="/api/catalogue/export" className="text-sky-400 active:opacity-70">
            CSV
          </Link>
        </div>
        {enCours ? (
          <p className="mt-1.5 text-[11px] leading-relaxed text-amber-200/90">
            <strong>Corpus incomplet : {etat.total - etat.detaillees} fiches sans genre.</strong>{" "}
            Les fiches sont récupérées par score décroissant : toute statistique de genre
            calculée maintenant sur-représente le haut du classement.
          </p>
        ) : null}
      </div>

      <form method="get" className="mb-3">
        <Cache sp={sp} garder={Object.keys(sp).filter((k) => k !== "n" && k !== "page")} />
        <label htmlFor="champ-nom" className="mb-1.5 block text-xs font-medium text-zinc-400">
          Rechercher par nom
        </label>
        <div className="flex gap-2">
          <input
            id="champ-nom"
            name="n"
            type="search"
            defaultValue={nom}
            placeholder="ex. fulmetal alchmist, shonen, ippo…"
            autoComplete="off"
            autoCapitalize="none"
            spellCheck={false}
            className={champ}
          />
          <button className="inline-flex min-h-11 shrink-0 items-center rounded-md bg-zinc-100 px-4 text-sm font-semibold text-zinc-900 shadow-[2px_2px_0_0_var(--color-vermilion)] active:translate-x-px active:translate-y-px">
            Chercher
          </button>
          {nom ? (
            <Link
              href={lienPage(Object.fromEntries(Object.entries(sp).filter(([k]) => k !== "n" && k !== "page")), 0)}
              aria-label="Effacer la recherche par nom"
              className="inline-flex min-h-11 shrink-0 items-center rounded-md border border-zinc-700 px-3 text-sm text-zinc-300 active:bg-zinc-800"
            >
              ✕
            </Link>
          ) : null}
        </div>
        <p className="mt-1.5 text-[11px] leading-relaxed text-zinc-600">
          Tolère les fautes de frappe, les accents, les espaces oubliés et les variantes
          de romanisation (« shonen » = « shounen »). Cherche dans le titre japonais et le
          titre anglais.
        </p>
      </form>

      <form method="get" className="mb-3">
        <Cache sp={sp} garder={[...CLES_FILTRES, "n"]} />
        <label className="mb-1.5 block text-xs font-medium text-zinc-400">
          Recherche par tags
        </label>
        <div className="flex gap-2">
          <input
            name="q"
            defaultValue={texteBarre}
            list="tags-dispo"
            placeholder="(fantasy|supernatural) action -comedy"
            autoComplete="off"
            autoCapitalize="none"
            spellCheck={false}
            className={`${champ} font-mono`}
          />
          <button className="inline-flex min-h-11 shrink-0 items-center rounded-lg bg-zinc-100 px-4 text-sm font-medium text-zinc-900 active:scale-[0.98]">
            OK
          </button>
        </div>
        <datalist id="tags-dispo">
          {[...genresDispo, ...themesDispo, ...magsDispo].map((t) => (
            <option key={t.nom} value={t.nom.includes(" ") ? `"${t.nom}"` : t.nom} />
          ))}
        </datalist>
        <p className="mt-1.5 text-[11px] leading-relaxed text-zinc-600">
          Espace = <span className="text-zinc-400">ET</span> · <code>|</code> ou{" "}
          <code>ou</code> = <span className="text-zinc-400">OU</span> ·{" "}
          <code>-tag</code> = <span className="text-zinc-400">exclure</span> ·{" "}
          <code>&quot;deux mots&quot;</code> ou <code>deux_mots</code> pour un tag composé.
          Une requête ici remplace les puces de genres, thèmes et magazines ; les filtres
          numériques restent actifs.
        </p>
        {resolu && resolu.inconnus.length > 0 ? (
          <p className="mt-2 rounded-lg border border-amber-900/50 bg-amber-950/20 px-3 py-2 text-[11px] text-amber-200">
            Tags non reconnus, ignorés : {resolu.inconnus.join(", ")}
          </p>
        ) : null}
      </form>

      <details open={actifs > 0 && !requete}
        className="group mb-6 rounded-xl border border-zinc-800 bg-zinc-900/40">
        <summary className="flex min-h-13 cursor-pointer list-none items-center justify-between gap-2 px-4 py-3 select-none">
          <span className="flex items-center gap-2 text-sm font-medium text-zinc-200">
            <span className="inline-block transition group-open:rotate-90">›</span>
            Filtres
            {actifs > 0 ? (
              <span className="rounded-full bg-sky-500/20 px-2 py-0.5 text-[11px] font-medium text-sky-300">
                {actifs}
              </span>
            ) : null}
          </span>
          <span className="text-xs text-zinc-500">
            {nf.format(totalFiltre)} résultat{totalFiltre > 1 ? "s" : ""}
          </span>
        </summary>

        <form method="get" className="border-t border-zinc-800 p-3 sm:p-4">
          {/* Soumettre les puces annule la requête texte */}
          <input type="hidden" name="q" value="" />
          <Cache sp={sp} garder={["n"]} />
          <div className="grid gap-4 sm:grid-cols-2">
            <Duo label="Score" a="scoreMin" b="scoreMax" sp={sp} step="0.01" />
            <Duo label="Tomes" a="volMin" b="volMax" sp={sp} />
            <Duo label="Année de début" a="anneeMin" b="anneeMax" sp={sp} />
            <Duo label="Membres" a="membresMin" b="membresMax" sp={sp}
              placeholders={["ex. 10000", "max"]} />
          </div>

          <div className="mt-4 grid gap-4 sm:grid-cols-3">
            <div>
              <span className="mb-1.5 block text-xs font-medium text-zinc-400">Statut</span>
              <Segmented name="statut" value={f.statut ?? ""}
                options={[
                  { v: "", label: "Tous" },
                  { v: "terminé", label: "Terminé" },
                  { v: "en cours", label: "En cours" },
                ]} />
            </div>
            <div>
              <span className="mb-1.5 block text-xs font-medium text-zinc-400">Trier par</span>
              <select name="tri" defaultValue={f.tri} className={champ}>
                <option value="pertinence">Pertinence (recherche par nom)</option>
                <option value="score">Score</option>
                <option value="members">Membres</option>
                <option value="scored_by">Nombre de notateurs</option>
                <option value="volumes">Tomes</option>
                <option value="annee">Année</option>
                <option value="titre">Titre</option>
              </select>
            </div>
            <div>
              <span className="mb-1.5 block text-xs font-medium text-zinc-400">Sens</span>
              <Segmented name="sens" value={f.sens}
                options={[
                  { v: "desc", label: "↓ Décroissant" },
                  { v: "asc", label: "↑ Croissant" },
                ]} />
            </div>
          </div>

          <label className="mt-3 flex min-h-11 items-center gap-2.5 rounded-lg border border-zinc-800 bg-zinc-950/40 px-3">
            <input type="checkbox" name="volInconnu" value="1"
              defaultChecked={f.volInconnu} className="size-5 accent-sky-500" />
            <span className="text-xs text-zinc-400">
              Inclure les œuvres sans nombre de tomes connu
            </span>
          </label>

          <div className="mt-4 space-y-3">
            <p className="rounded-lg border border-zinc-800 bg-zinc-950/30 px-3 py-2 text-[11px] leading-relaxed text-zinc-500">
              Chaque groupe a son propre ET/OU et se déplie d'un geste. Les groupes se combinent ensuite par ET.
              Exemple : groupe 1 = Supernatural + Fantasy en <strong>OU</strong>, groupe 2
              = Action → <span className="text-zinc-300">(Supernatural OU Fantasy) ET Action</span>.
            </p>

            <Famille titre="Genres"
              choisis={gAff.reduce((t, g) => t + g.noms.length, 0)}>
              {RANGS.map((r) => (
                <GroupeTags key={r} titre={`Groupe ${r}`} prefixe="g" rang={r}
                  options={genresDispo} groupe={gAff[r - 1]} />
              ))}
            </Famille>

            <Famille titre="Thèmes"
              choisis={tAff.reduce((t, g) => t + g.noms.length, 0)}>
              {RANGS.map((r) => (
                <GroupeTags key={r} titre={`Groupe ${r}`} prefixe="t" rang={r}
                  options={themesDispo} groupe={tAff[r - 1]} limite={20} />
              ))}
            </Famille>

            <Famille titre="Magazines (inclure, en OU)" choisis={f.magazines.length}>
              <div className="p-1">
                <Chips name="m" options={magsDispo} selected={f.magazines} limite={14} />
              </div>
            </Famille>

            <details open={f.genresExcl.length + f.themesExcl.length + f.magazinesExcl.length > 0}>
              <summary className="flex min-h-11 cursor-pointer list-none items-center text-xs font-medium text-zinc-400 select-none">
                <span className="mr-1.5">−</span> Exclusions
              </summary>
              <div className="mt-2 space-y-3">
                <div className="rounded-lg border border-zinc-800 bg-zinc-950/40 p-3">
                  <p className="mb-2 text-xs font-medium text-zinc-300">Genres — exclure</p>
                  <Chips name="gx" options={genresDispo} selected={f.genresExcl} ton="exclusion" />
                </div>
                <div className="rounded-lg border border-zinc-800 bg-zinc-950/40 p-3">
                  <p className="mb-2 text-xs font-medium text-zinc-300">Thèmes — exclure</p>
                  <Chips name="tx" options={themesDispo} selected={f.themesExcl} ton="exclusion" limite={16} />
                </div>
                <div className="rounded-lg border border-zinc-800 bg-zinc-950/40 p-3">
                  <p className="mb-2 text-xs font-medium text-zinc-300">Magazines — exclure</p>
                  <Chips name="mx" options={magsDispo} selected={f.magazinesExcl} ton="exclusion" limite={12} />
                </div>
              </div>
            </details>
          </div>

          <div className="mt-4 flex items-center gap-2">
            <label className="shrink-0">
              <span className="sr-only">Résultats par page</span>
              <select name="parPage" defaultValue={String(f.parPage)} className={champ}>
                <option value="25">25 / page</option>
                <option value="50">50 / page</option>
                <option value="100">100 / page</option>
                <option value="200">200 / page</option>
              </select>
            </label>
            <Link href="/catalogue"
              className="inline-flex min-h-11 shrink-0 items-center rounded-lg border border-zinc-700 px-4 text-sm text-zinc-300 active:bg-zinc-800">
              Réinit.
            </Link>
            <button className="inline-flex min-h-11 flex-1 items-center justify-center rounded-lg bg-zinc-100 px-4 text-sm font-medium text-zinc-900 active:scale-[0.98]">
              Appliquer
            </button>
          </div>
        </form>
      </details>

      {nom ? (
        <p className="mb-3 rounded-lg border border-vermilion/40 bg-vermilion-soft/20 px-3 py-2 text-xs leading-relaxed text-zinc-300">
          <span className="font-semibold text-vermilion">Nom :</span> « {nom} »
          {trouves === null
            ? " — la recherche par nom est ignorée : il faut au moins 2 lettres ou chiffres de l'alphabet latin (les titres sont en romaji, les caractères japonais ne sont pas lus)."
            : ` — ${trouves.length} œuvre${trouves.length > 1 ? "s" : ""} proche${trouves.length > 1 ? "s" : ""} avant les autres filtres.${
                f.volMin === undefined && f.volMax === undefined
                  ? " Les œuvres sans nombre de tomes connu sont incluses."
                  : ""
              }`}
        </p>
      ) : null}

      {expr ? (
        <p className="mb-4 rounded-lg border border-sky-900/40 bg-sky-950/15 px-3 py-2 text-xs leading-relaxed text-sky-200">
          <span className="text-sky-400">Requête :</span> {expr}
        </p>
      ) : null}

      <section className="mb-6 space-y-3">
        <div className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-6">
          {[
            { v: nf.format(stats.total), l: "œuvres" },
            { v: stats.scoreMoy ?? "—", l: "score moyen" },
            { v: stats.volMed ?? "—", l: "tomes (médiane)" },
            { v: stats.volMoy ?? "—", l: "tomes (moyenne)" },
            { v: compact(stats.membresMed), l: "membres (médiane)" },
            { v: compact(stats.membresMoy), l: "membres (moyenne)" },
          ].map((s) => (
            <div key={s.l} className="rounded-xl border border-zinc-800 bg-zinc-900/60 px-3 py-3">
              <div className="text-lg font-semibold text-zinc-100 sm:text-xl">{s.v}</div>
              <div className="text-[11px] leading-tight text-zinc-500">{s.l}</div>
            </div>
          ))}
        </div>

        <div className="grid gap-3 lg:grid-cols-3">
          <PanneauStat titre="Genres dominants" ouvertMobile>
            <Barre stats={stats.genres} total={stats.total} />
          </PanneauStat>
          <PanneauStat titre="Thèmes dominants">
            <Barre stats={stats.themes} total={stats.total} />
          </PanneauStat>
          <PanneauStat titre="Magazines · tomes · décennies">
            <div className="space-y-4">
              <Barre stats={stats.magazines} total={stats.total} />
              <div className="border-t border-zinc-800 pt-3">
                <p className="mb-2 text-[11px] text-zinc-500">Par nombre de tomes</p>
                <Barre stats={stats.tranches.map((t) => ({ nom: t.tranche, n: t.n }))
                  .sort((a, b) => b.n - a.n)} total={stats.total} />
              </div>
              <div className="border-t border-zinc-800 pt-3">
                <p className="mb-2 text-[11px] text-zinc-500">Par décennie</p>
                <Barre stats={stats.decennies.map((d) => ({ nom: `${d.dec}s`, n: d.n }))}
                  total={stats.total} />
              </div>
            </div>
          </PanneauStat>
        </div>

        <p className="text-[11px] leading-relaxed text-zinc-600">
          Page {f.page + 1} sur {pages}. Les statistiques portent sur la sélection entière
          ({nf.format(stats.total)} œuvres), pas sur la page affichée. Une œuvre porte
          plusieurs genres : le total dépasse 100 %.
        </p>
      </section>

      <LegendeScores />
      <p className="mb-2 text-[11px] leading-relaxed text-zinc-600">
        Le numéro à gauche est la position dans la liste actuelle, selon le tri choisi
        (rang {nf.format(debut)} à {nf.format(fin)} sur {nf.format(totalFiltre)}).
      </p>

      <ul className="space-y-2 md:hidden">
        {lignes.map((l, idx) => (
          <li key={l.mal_id}>
            <a
              href={l.url}
              target="_blank"
              rel="noreferrer"
              className="flex items-start gap-2.5 rounded-lg border border-zinc-700 bg-zinc-900 p-3 active:bg-zinc-800"
            >
              <span
                aria-label={`Rang ${debut + idx}`}
                className="w-8 shrink-0 pt-1 text-right font-mono text-[13px] leading-none font-bold text-zinc-500 tabular-nums"
              >
                {debut + idx}
              </span>
              <TuileScore score={l.score} />
              <span className="min-w-0 flex-1">
                <span className="block text-[15px] leading-snug font-semibold text-zinc-100">
                  {l.titre}
                  {approx(l.mal_id)}
                </span>
                <span className="mt-1 flex flex-wrap items-center gap-x-2.5 gap-y-0.5 font-mono text-[11px] text-zinc-500">
                  <span className="font-semibold text-zinc-300">
                    {l.scored_by === null ? "—" : nf.format(l.scored_by)} notateurs
                  </span>
                  <span className="text-sky-300">{compact(l.members)} membres</span>
                  <span>{l.volumes ?? "?"} t.</span>
                  {l.chapitres ? <span>{l.chapitres} ch.</span> : null}
                  <span>{l.annee_debut ?? "—"}</span>
                  {l.statut ? <span className="text-zinc-600">{l.statut}</span> : null}
                </span>
                {l.genres ? (
                  <span className="mt-1.5 block text-xs leading-relaxed text-zinc-500">
                    {l.genres}
                  </span>
                ) : null}
                {l.magazines ? (
                  <span className="mt-0.5 block text-[11px] text-zinc-600">{l.magazines}</span>
                ) : null}
              </span>
            </a>
          </li>
        ))}
      </ul>

      <div className="hidden overflow-x-auto rounded-lg border border-zinc-700 bg-zinc-900 md:block">
        <table className="w-full text-left text-xs">
          <thead className="bg-zinc-100 text-zinc-900">
            <tr>
              <th className="w-12 px-3 py-2.5 text-right font-semibold">#</th>
              <th className="px-3 py-2.5 font-semibold">Titre</th>
              <th className="px-3 py-2 text-right font-medium">Score</th>
              <th className="px-3 py-2 text-right font-medium">Notateurs</th>
              <th className="px-3 py-2 text-right font-medium">Membres</th>
              <th className="px-3 py-2 text-right font-medium">Tomes</th>
              <th className="px-3 py-2 text-right font-medium">Ch.</th>
              <th className="px-3 py-2 text-right font-medium">Début</th>
              <th className="px-3 py-2 font-medium">Genres</th>
              <th className="px-3 py-2 font-medium">Magazine</th>
            </tr>
          </thead>
          <tbody>
            {lignes.map((l, idx) => (
              <tr key={l.mal_id} className="border-t border-zinc-800/70 hover:bg-zinc-900/40">
                <td className="px-3 py-2 text-right font-mono font-bold text-zinc-500 tabular-nums">{debut + idx}</td>
                <td className="px-3 py-2">
                  <a href={l.url} target="_blank" rel="noreferrer"
                    className="text-zinc-100 hover:underline">{l.titre}</a>{approx(l.mal_id)}
                </td>
                <td className="px-3 py-2 text-right"><TuileScore score={l.score} taille="sm" /></td>
                <td className="px-3 py-2 text-right tabular-nums text-zinc-300">
                  {l.scored_by === null ? "—" : nf.format(l.scored_by)}
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-sky-300">
                  {l.members === null ? "—" : nf.format(l.members)}
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-zinc-300">{l.volumes ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums text-zinc-500">{l.chapitres ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums text-zinc-500">{l.annee_debut ?? "—"}</td>
                <td className="max-w-48 px-3 py-2 text-zinc-400">{l.genres ?? "—"}</td>
                <td className="max-w-40 px-3 py-2 text-zinc-500">{l.magazines ?? "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {lignes.length === 0 ? (
        <p className="rounded-xl border border-dashed border-zinc-800 p-8 text-center text-sm text-zinc-500">
          Aucune œuvre ne correspond à ces filtres.
        </p>
      ) : null}

      <Pagination sp={sp} page={f.page} pages={pages} total={totalFiltre}
        debut={debut} fin={fin} />
    </>
  );
}
