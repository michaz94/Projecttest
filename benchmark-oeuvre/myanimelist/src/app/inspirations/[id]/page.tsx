import Link from "next/link";
import { notFound } from "next/navigation";
import { eq } from "drizzle-orm";

import { db } from "@/db";
import { inspirations } from "@/db/schema";
import { Segmented } from "@/components/chips";
import { Badge, Button, Disclosure } from "@/components/ui";
import { InspirationForm } from "@/components/inspiration-form";
import { STATUT_INSPIRATION, STATUTS_INSPIRATION } from "@/lib/labels";
import { deleteInspiration, setInspirationStatut } from "@/app/actions";

export const dynamic = "force-dynamic";

/** Bloc de lecture : titre d'étiquette, puis texte sur une largeur confortable. */
function Section({
  titre,
  children,
  ton = "neutre",
}: {
  titre: string;
  children: React.ReactNode;
  ton?: "neutre" | "alerte" | "ouvert";
}) {
  const styles = {
    neutre: "border-zinc-700 bg-zinc-900",
    alerte: "border-rose-400/60 bg-rose-500/5",
    ouvert: "border-amber-400/60 bg-amber-500/5",
  } as const;
  const etiquette = {
    neutre: "text-zinc-500",
    alerte: "text-rose-300",
    ouvert: "text-amber-300",
  } as const;
  return (
    <section className={`rounded-lg border px-5 py-4 sm:px-6 sm:py-5 ${styles[ton]}`}>
      <h2
        className={`mb-2 font-mono text-[11px] font-semibold tracking-[0.16em] uppercase ${etiquette[ton]}`}
      >
        {titre}
      </h2>
      <div className="space-y-3 text-[15px] leading-relaxed whitespace-pre-line text-zinc-300">
        {children}
      </div>
    </section>
  );
}

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const num = Number.parseInt(id, 10);
  if (!num) notFound();

  const [i] = await db.select().from(inspirations).where(eq(inspirations.id, num)).limit(1);
  if (!i) notFound();

  const statut = STATUT_INSPIRATION[i.statut];

  return (
    <div className="mx-auto max-w-2xl">
      <Link
        href="/inspirations"
        className="mb-5 inline-flex min-h-11 items-center gap-1.5 text-sm font-semibold text-zinc-500 hover:text-zinc-100"
      >
        <span aria-hidden>←</span> Toutes les inspirations
      </Link>

      <header className="mb-6">
        <p className="mb-2 flex items-center gap-2 font-mono text-[11px] font-semibold tracking-[0.18em] text-vermilion uppercase">
          <span className="h-px w-5 bg-vermilion" />
          {i.categorie}
        </p>
        <h1 className="text-[1.75rem] leading-[1.1] font-extrabold tracking-tight text-zinc-100 sm:text-4xl">
          {i.nom}
        </h1>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <Badge classe={statut.classe}>{statut.label}</Badge>
          {i.medium ? (
            <span className="text-sm text-zinc-500">{i.medium}</span>
          ) : null}
        </div>
        <p className="mt-2 text-sm leading-relaxed text-zinc-500">{statut.aide}</p>
      </header>

      {/* Changer le statut : choix visible, un seul geste */}
      <form
        action={setInspirationStatut}
        className="mb-6 rounded-lg border border-zinc-700 bg-zinc-900 p-4"
      >
        <input type="hidden" name="id" value={i.id} />
        <p className="mb-2 font-mono text-[10px] font-semibold tracking-wider text-zinc-500 uppercase">
          Requalifier
        </p>
        <div className="scroll-x">
          <Segmented
            name="statut"
            value={i.statut}
            options={STATUTS_INSPIRATION.map((s) => ({
              v: s,
              label: STATUT_INSPIRATION[s].label,
            }))}
          />
        </div>
        <div className="mt-3">
          <Button variant="ghost">Appliquer le statut</Button>
        </div>
      </form>

      <div className="space-y-3">
        {i.ceQueVousEnDites ? (
          <Section titre="Ce que vous en dites">{i.ceQueVousEnDites}</Section>
        ) : null}

        {i.piegesInterpretation ? (
          <Section titre="Ne pas en déduire" ton="alerte">
            {i.piegesInterpretation}
          </Section>
        ) : null}

        {i.resteOuvert ? (
          <Section titre="Ce qui reste ouvert" ton="ouvert">
            {i.resteOuvert}
          </Section>
        ) : null}

        {i.economie ? (
          <Section titre="Économie de publication">{i.economie}</Section>
        ) : null}

        {!i.ceQueVousEnDites &&
        !i.piegesInterpretation &&
        !i.resteOuvert &&
        !i.economie ? (
          <p className="rounded-lg border-2 border-dashed border-zinc-700 p-6 text-center text-sm text-zinc-500">
            Fiche encore vide. Ouvrez « Modifier » pour la renseigner.
          </p>
        ) : null}
      </div>

      <div className="mt-8 space-y-3">
        <Disclosure summary="Modifier cette fiche">
          <InspirationForm i={i} />
        </Disclosure>
        <Disclosure summary="Supprimer">
          <p className="mb-3 text-sm text-zinc-500">
            La fiche sera supprimée définitivement. Si vous hésitez, requalifiez-la
            plutôt en « Écartée » : le motif reste consultable.
          </p>
          <form action={deleteInspiration}>
            <input type="hidden" name="id" value={i.id} />
            <Button variant="danger">Supprimer définitivement</Button>
          </form>
        </Disclosure>
      </div>
    </div>
  );
}
