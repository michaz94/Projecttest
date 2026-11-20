import Link from "next/link";

import { db } from "@/db";
import { inspirations } from "@/db/schema";
import {
  Badge,
  Disclosure,
  EmptyState,
  PageHeader,
  Stat,
} from "@/components/ui";
import { InspirationForm } from "@/components/inspiration-form";
import { STATUT_INSPIRATION, STATUTS_INSPIRATION } from "@/lib/labels";

export const dynamic = "force-dynamic";

type SP = Record<string, string | string[] | undefined>;
const one = (v: string | string[] | undefined) =>
  Array.isArray(v) ? (v[0] ?? "") : (v ?? "");

const norm = (s: string) =>
  s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

function lien(sp: { statut?: string; cat?: string; q?: string }) {
  const p = new URLSearchParams();
  if (sp.statut) p.set("statut", sp.statut);
  if (sp.cat) p.set("cat", sp.cat);
  if (sp.q) p.set("q", sp.q);
  const q = p.toString();
  return q ? `/inspirations?${q}` : "/inspirations";
}

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<SP>;
}) {
  const sp = await searchParams;
  const statut = one(sp.statut);
  const cat = one(sp.cat);
  const q = one(sp.q).trim();

  const toutes = await db
    .select()
    .from(inspirations)
    .orderBy(inspirations.categorie, inspirations.nom);

  const categories = [...new Set(toutes.map((i) => i.categorie))];
  const nParStatut = (s: string) => toutes.filter((i) => i.statut === s).length;

  const visibles = toutes.filter((i) => {
    if (statut && i.statut !== statut) return false;
    if (cat && i.categorie !== cat) return false;
    if (q) {
      const cible = norm(
        [i.nom, i.categorie, i.ceQueVousEnDites, i.piegesInterpretation, i.medium]
          .join(" "),
      );
      if (!cible.includes(norm(q))) return false;
    }
    return true;
  });

  const groupes = [...new Set(visibles.map((i) => i.categorie))];
  const filtreActif = Boolean(statut || cat || q);

  const puce =
    "inline-flex min-h-10 items-center gap-1.5 rounded-md border px-3 text-[13px] whitespace-nowrap transition-colors";
  const puceOff = "border-zinc-700 bg-field text-zinc-400 hover:border-zinc-100";
  const puceOn = "border-zinc-100 bg-zinc-100 font-semibold text-zinc-900";

  return (
    <>
      <PageHeader
        kicker="Projet"
        titre="Inspirations"
        chapo="Vos références, gardées comme des références. Aimer une source ne l'intègre pas à l'œuvre : chaque fiche porte ce qu'il ne faut pas en déduire."
        precision="Contenu transcrit de votre document de contexte, section 3, puis complété au fil de nos échanges. Aucune référence n'a été déduite à votre place."
      />

      <section aria-label="Résumé" className="mb-6 grid grid-cols-2 gap-2.5 sm:grid-cols-4">
        <Stat valeur={toutes.length} label="inspirations" accent />
        <Stat valeur={nParStatut("retenue")} label="effectivement retenues" />
        <Stat valeur={nParStatut("indetermine")} label="au rôle indéterminé" />
        <Stat valeur={nParStatut("ecartee")} label="écartées" />
      </section>

      {/* Recherche */}
      <form method="get" className="mb-3 flex gap-2">
        {statut ? <input type="hidden" name="statut" value={statut} /> : null}
        {cat ? <input type="hidden" name="cat" value={cat} /> : null}
        <input
          name="q"
          defaultValue={q}
          placeholder="Rechercher une référence, un piège, un média…"
          autoComplete="off"
          className="min-h-11 w-full rounded-md border border-zinc-700 bg-field px-3 text-base text-zinc-100 placeholder:text-zinc-600 focus:border-zinc-100 focus:outline-none sm:text-sm"
        />
        <button className="inline-flex min-h-11 shrink-0 items-center rounded-md bg-zinc-100 px-4 text-sm font-semibold text-zinc-900 shadow-[2px_2px_0_0_var(--color-vermilion)] active:translate-x-px active:translate-y-px">
          Chercher
        </button>
      </form>

      {/* Filtres */}
      <div className="mb-1 space-y-2">
        <div className="scroll-x -mx-4 px-4 sm:mx-0 sm:px-0">
          <div className="flex w-max gap-1.5 sm:w-auto sm:flex-wrap">
            <Link
              href={lien({ cat, q })}
              className={`${puce} ${!statut ? puceOn : puceOff}`}
            >
              Tous
              <span className="font-mono text-[10px] opacity-60">{toutes.length}</span>
            </Link>
            {STATUTS_INSPIRATION.map((s) => (
              <Link
                key={s}
                href={lien({ statut: statut === s ? "" : s, cat, q })}
                className={`${puce} ${statut === s ? puceOn : puceOff}`}
              >
                {STATUT_INSPIRATION[s].label}
                <span className="font-mono text-[10px] opacity-60">{nParStatut(s)}</span>
              </Link>
            ))}
          </div>
        </div>
        <div className="scroll-x -mx-4 px-4 sm:mx-0 sm:px-0">
          <div className="flex w-max gap-1.5 sm:w-auto sm:flex-wrap">
            {categories.map((c) => (
              <Link
                key={c}
                href={lien({ statut, cat: cat === c ? "" : c, q })}
                className={`${puce} ${cat === c ? puceOn : puceOff}`}
              >
                {c}
              </Link>
            ))}
          </div>
        </div>
      </div>

      <p className="mt-3 mb-5 flex items-center justify-between text-xs text-zinc-500">
        <span>
          {visibles.length} sur {toutes.length}
          {filtreActif ? " après filtre" : ""}
        </span>
        {filtreActif ? (
          <Link href="/inspirations" className="font-semibold text-vermilion">
            Réinitialiser
          </Link>
        ) : null}
      </p>

      {/* Liste */}
      {visibles.length === 0 ? (
        <EmptyState titre={toutes.length === 0 ? "Registre vide" : "Aucun résultat"}>
          {toutes.length === 0
            ? "Ajoutez vos références avec, pour chacune, ce qu'elle n'implique pas."
            : "Aucune inspiration ne correspond à ces filtres."}
        </EmptyState>
      ) : (
        <div className="space-y-8">
          {groupes.map((g) => (
            <section key={g}>
              <h2 className="mb-2 flex items-center gap-2 font-mono text-[11px] font-semibold tracking-[0.16em] text-zinc-500 uppercase">
                <span className="h-px w-4 bg-zinc-700" />
                {g}
              </h2>
              <ul className="overflow-hidden rounded-lg border border-zinc-700 bg-zinc-900">
                {visibles
                  .filter((i) => i.categorie === g)
                  .map((i, k) => (
                    <li key={i.id} className={k > 0 ? "border-t border-zinc-800" : ""}>
                      <Link
                        href={`/inspirations/${i.id}`}
                        className="flex items-center gap-3 px-4 py-3.5 transition-colors hover:bg-zinc-950 active:bg-zinc-800"
                      >
                        <span className="min-w-0 flex-1">
                          <span className="flex flex-wrap items-center gap-x-2.5 gap-y-1.5">
                            <span className="text-[15px] leading-snug font-semibold text-zinc-100">
                              {i.nom}
                            </span>
                            <Badge classe={STATUT_INSPIRATION[i.statut].classe}>
                              {STATUT_INSPIRATION[i.statut].label}
                            </Badge>
                          </span>
                          {i.medium || i.economie ? (
                            <span className="mt-1 block text-xs leading-snug text-zinc-500">
                              {[i.medium, i.economie].filter(Boolean).join(" · ")}
                            </span>
                          ) : null}
                          <span className="mt-1.5 flex flex-wrap gap-x-3 gap-y-0.5 font-mono text-[10px] tracking-wide text-zinc-600 uppercase">
                            {i.piegesInterpretation ? (
                              <span className="text-rose-300">Pièges notés</span>
                            ) : null}
                            {i.resteOuvert ? (
                              <span className="text-amber-300">Reste ouvert</span>
                            ) : null}
                          </span>
                        </span>
                        <span aria-hidden className="shrink-0 text-lg text-vermilion">
                          →
                        </span>
                      </Link>
                    </li>
                  ))}
              </ul>
            </section>
          ))}
        </div>
      )}

      <div className="mt-8">
        <Disclosure summary="Nouvelle inspiration" tone="accent">
          <InspirationForm />
        </Disclosure>
      </div>
    </>
  );
}
