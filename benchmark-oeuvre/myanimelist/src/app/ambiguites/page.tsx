import Link from "next/link";
import { eq } from "drizzle-orm";

import { db } from "@/db";
import { ambiguites, projets } from "@/db/schema";
import {
  Area,
  Badge,
  Button,
  Card,
  Disclosure,
  EmptyState,
  Field,
  PageHeader,
  Prop,
  Select,
} from "@/components/ui";
import { STATUT_AMBIGUITE, STATUTS_AMBIGUITE } from "@/lib/labels";
import { createAmbiguite, deleteAmbiguite, updateAmbiguite } from "@/app/actions";

export const dynamic = "force-dynamic";

const optionsStatut = STATUTS_AMBIGUITE.map((s) => ({
  value: s,
  label: STATUT_AMBIGUITE[s].label,
}));

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ projet?: string }>;
}) {
  const sp = await searchParams;
  const listeProjets = await db.select().from(projets).orderBy(projets.id);

  if (listeProjets.length === 0) {
    return (
      <>
        <PageHeader
          kicker="Projet"
        titre="Ambiguïtés structurantes"
          chapo="Les questions ouvertes qui conditionnent d'autres décisions."
        />
        <EmptyState titre="Aucun projet">
          Créez d&apos;abord un projet depuis le{" "}
          <Link href="/" className="underline underline-offset-4">
            tableau de bord
          </Link>
          .
        </EmptyState>
      </>
    );
  }

  const projetId = Number.parseInt(sp.projet ?? "", 10) || listeProjets[0].id;
  const projetActif = listeProjets.find((p) => p.id === projetId) ?? listeProjets[0];

  const liste = await db
    .select()
    .from(ambiguites)
    .where(eq(ambiguites.projetId, projetActif.id))
    .orderBy(ambiguites.statut, ambiguites.id);

  return (
    <>
      <PageHeader
        titre="Ambiguïtés structurantes"
        chapo="Une ambiguïté structurante est une question dont la réponse en engage plusieurs autres. La laisser ouverte est légitime ; la refermer sans le dire ne l'est pas."
        precision="Ce registre existe pour rendre visible ce qui, sinon, se règle par défaut : un choix pris par fatigue, par habitude d'écriture ou par imitation d'un modèle, puis rétroactivement pris pour une intention."
      />

      <div className="mb-6 flex flex-wrap items-center gap-2">
        {listeProjets.map((p) => (
          <Link
            key={p.id}
            href={`/ambiguites?projet=${p.id}`}
            className={`rounded-lg px-3 py-1.5 text-xs transition ${
              p.id === projetActif.id
                ? "bg-zinc-100 text-zinc-900"
                : "border border-zinc-800 text-zinc-400 hover:bg-zinc-900"
            }`}
          >
            {p.titre}
          </Link>
        ))}
      </div>

      {liste.length === 0 ? (
        <EmptyState titre="Registre vide">
          Rien n&apos;est pré-rempli : je ne connais pas les tensions internes de votre
          projet. Trois candidates fréquentes, à retenir ou à ignorer — la part de
          codes shonen japonais assumée face à un lectorat occidental, le format visé
          (série longue ou récit borné), et la personne qui décide en dernier ressort
          entre vous et un éditeur.
        </EmptyState>
      ) : (
        <div className="space-y-3">
          {liste.map((a) => (
            <Card key={a.id}>
              <div className="flex flex-wrap items-start gap-3">
                <Badge classe={STATUT_AMBIGUITE[a.statut].classe}>
                  {STATUT_AMBIGUITE[a.statut].label}
                </Badge>
                <h2 className="flex-1 text-base font-medium text-zinc-100">
                  {a.question}
                </h2>
              </div>

              <dl className="mt-2">
                <Prop label="Enjeu" value={a.enjeu} />
                <Prop label="Ce que cela conditionne" value={a.consequences} />
                <Prop label="Arbitrage rendu" value={a.arbitrage} />
              </dl>

              {a.statut === "arbitree" && !a.arbitrage ? (
                <p className="mt-3 rounded-lg border border-amber-900/50 bg-amber-950/20 px-3 py-2 text-xs text-amber-300">
                  Marquée arbitrée, mais aucun arbitrage n&apos;est consigné. La trace
                  de la décision manque.
                </p>
              ) : null}

              <div className="mt-4">
                <Disclosure summary="Modifier">
                  <form action={updateAmbiguite} className="grid gap-3 sm:grid-cols-2">
                    <input type="hidden" name="id" value={a.id} />
                    <Field label="Question" name="question" defaultValue={a.question} required wide />
                    <Select
                      label="Statut"
                      name="statut"
                      defaultValue={a.statut}
                      options={optionsStatut}
                    />
                    <Field label="Enjeu" name="enjeu" defaultValue={a.enjeu} />
                    <Area
                      label="Ce que cela conditionne"
                      name="consequences"
                      defaultValue={a.consequences}
                      rows={3}
                    />
                    <Area
                      label="Arbitrage rendu"
                      name="arbitrage"
                      defaultValue={a.arbitrage}
                      rows={3}
                      aide="À remplir seulement si vous avez effectivement tranché."
                    />
                    <div className="sm:col-span-2">
                      <Button>Enregistrer</Button>
                    </div>
                  </form>
                  <form action={deleteAmbiguite} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={a.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-4">
        <Disclosure summary="+ Signaler une ambiguïté" tone="accent">
          <form action={createAmbiguite} className="grid gap-3 sm:grid-cols-2">
            <input type="hidden" name="projetId" value={projetActif.id} />
            <Field
              label="Question"
              name="question"
              required
              wide
              placeholder="Formulez-la comme une question, pas comme un manque."
            />
            <Select
              label="Statut"
              name="statut"
              defaultValue="ouverte"
              options={optionsStatut}
            />
            <Field label="Enjeu" name="enjeu" placeholder="Pourquoi c'est structurant" />
            <Area
              label="Ce que cela conditionne"
              name="consequences"
              rows={3}
              placeholder="Les décisions qui dépendent de cette réponse."
            />
            <div className="sm:col-span-2">
              <Button>Enregistrer</Button>
            </div>
          </form>
        </Disclosure>
      </div>
    </>
  );
}
