import Link from "next/link";

import { Chips, Segmented } from "@/components/chips";
import { PageHeader } from "@/components/ui";
import { analyser, construireDico, versTexte } from "@/lib/query";
import {
  chercher,
  compter,
  etatImport,
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
  "w-full min-h-11 rounded-lg border border-zinc-700 bg-zinc-950/70 px-3 text-base sm:text-sm text-zinc-100 focus:border-sky-500 focus:outline-none";

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

/** Un groupe de tags : sa propre liste et son propre mode ET/OU. */
function GroupeTags({
  titre, prefixe, rang, options, groupe, limite, obligatoire,
}: {
  titre: string; prefixe: "g" | "t"; rang: number;
  options: { nom: string; n: number }[]; groupe: Groupe;
  limite?: number; obligatoire?: boolean;
}) {
  const vide = groupe.noms.length === 0;
  if (vide && !obligatoire) {
    return (
      <details className="rounded-lg border border-dashed border-zinc-800 bg-zinc-950/30">
        <summary className="flex min-h-11 cursor-pointer list-none items-center px-3 text-xs text-zinc-500 select-none">
          + {titre}
        </summary>
        <div className="border-t border-zinc-800 p-3">
          <div className="mb-2 flex justify-end">
            <Segmented name={`${prefixe}${rang}m`} value={groupe.mode}
              options={[{ v: "or", label: "OU" }, { v: "and", label: "ET" }]} />
          </div>
          <Chips name={`${prefixe}${rang}`} options={options} selected={groupe.noms} limite={limite} />
        </div>
      </details>
    );
  }
  return (
    <div className="rounded-lg border border-zinc-800 bg-zinc-950/40 p-3">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <span className="text-xs font-medium text-zinc-300">{titre}</span>
        <Segmented name={`${prefixe}${rang}m`} value={groupe.mode}
          options={[{ v: "or", label: "OU" }, { v: "and", label: "ET" }]} />
      </div>
      <Chips name={`${prefixe}${rang}`} options={options} selected={groupe.noms} limite={limite} />
    </div>
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

  const f = lireFiltres(sp, resolu);
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
          <Link href="/api/catalogue/export" className="text-sky-400 active:opacity-70">
            export CSV
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
                <option value="score">Score</option>
                <option value="members">Membres</option>
                <option value="scored_by">Nombre de votes</option>
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
              Chaque groupe a son propre ET/OU. Les groupes se combinent ensuite par ET.
              Exemple : groupe 1 = Supernatural + Fantasy en <strong>OU</strong>, groupe 2
              = Action → <span className="text-zinc-300">(Supernatural OU Fantasy) ET Action</span>.
            </p>

            <div className="space-y-2">
              <p className="text-xs font-semibold tracking-wide text-zinc-400 uppercase">Genres</p>
              {RANGS.map((r) => (
                <GroupeTags key={r} titre={`Groupe ${r}`} prefixe="g" rang={r}
                  options={genresDispo} groupe={gAff[r - 1]} obligatoire={r === 1} />
              ))}
            </div>

            <div className="space-y-2">
              <p className="text-xs font-semibold tracking-wide text-zinc-400 uppercase">Thèmes</p>
              {RANGS.map((r) => (
                <GroupeTags key={r} titre={`Groupe ${r}`} prefixe="t" rang={r}
                  options={themesDispo} groupe={tAff[r - 1]}
                  limite={20} obligatoire={r === 1} />
              ))}
            </div>

            <div className="rounded-lg border border-zinc-800 bg-zinc-950/40 p-3">
              <p className="mb-2 text-xs font-medium text-zinc-300">Magazines — inclure (OU)</p>
              <Chips name="m" options={magsDispo} selected={f.magazines} limite={14} />
            </div>

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

      <ul className="space-y-2 md:hidden">
        {lignes.map((l) => (
          <li key={l.mal_id} className="rounded-xl border border-zinc-800 bg-zinc-900/60 p-3">
            <a href={l.url} target="_blank" rel="noreferrer"
              className="block text-sm leading-snug font-medium text-zinc-100 active:opacity-70">
              {l.titre}
            </a>
            <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-zinc-400">
              <span className="font-medium text-emerald-300">{l.score ?? "—"}</span>
              <span className="text-sky-300">{compact(l.members)} membres</span>
              <span>{l.volumes ?? "?"} tomes</span>
              {l.chapitres ? <span>{l.chapitres} ch.</span> : null}
              <span className="text-zinc-500">{l.annee_debut ?? "—"}</span>
              {l.statut ? <span className="text-[10px] text-zinc-600">{l.statut}</span> : null}
            </div>
            {l.genres ? (
              <p className="mt-1.5 text-[11px] leading-relaxed text-zinc-500">{l.genres}</p>
            ) : null}
            {l.magazines ? (
              <p className="mt-0.5 text-[11px] text-zinc-600">{l.magazines}</p>
            ) : null}
          </li>
        ))}
      </ul>

      <div className="hidden overflow-x-auto rounded-xl border border-zinc-800 md:block">
        <table className="w-full text-left text-xs">
          <thead className="bg-zinc-900 text-zinc-400">
            <tr>
              <th className="px-3 py-2 font-medium">Titre</th>
              <th className="px-3 py-2 text-right font-medium">Score</th>
              <th className="px-3 py-2 text-right font-medium">Votes</th>
              <th className="px-3 py-2 text-right font-medium">Membres</th>
              <th className="px-3 py-2 text-right font-medium">Tomes</th>
              <th className="px-3 py-2 text-right font-medium">Ch.</th>
              <th className="px-3 py-2 text-right font-medium">Début</th>
              <th className="px-3 py-2 font-medium">Genres</th>
              <th className="px-3 py-2 font-medium">Magazine</th>
            </tr>
          </thead>
          <tbody>
            {lignes.map((l) => (
              <tr key={l.mal_id} className="border-t border-zinc-800/70 hover:bg-zinc-900/40">
                <td className="px-3 py-2">
                  <a href={l.url} target="_blank" rel="noreferrer"
                    className="text-zinc-100 hover:underline">{l.titre}</a>
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-emerald-300">{l.score ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums text-zinc-500">
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
