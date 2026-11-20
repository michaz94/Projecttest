import Link from "next/link";
import { eq } from "drizzle-orm";

import { db } from "@/db";
import { decisions, projets } from "@/db/schema";
import {
  Area,
  Badge,
  Button,
  Card,
  Disclosure,
  EmptyState,
  Field,
  PageHeader,
  Select,
} from "@/components/ui";
import {
  ORIGINE,
  ORIGINES,
  STATUT_DECISION,
  STATUTS_DECISION,
  type StatutDecision,
} from "@/lib/labels";
import { createDecision, setDecisionStatut } from "@/app/actions";

export const dynamic = "force-dynamic";

const AXES_SUGGERES = [
  "Prémisse",
  "Protagoniste",
  "Système de pouvoir",
  "Antagonisme",
  "Structure d'arc",
  "Ton",
  "Format & pagination",
  "Positionnement marché",
  "Cible éditeur",
];

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ projet?: string; statut?: string }>;
}) {
  const sp = await searchParams;
  const listeProjets = await db.select().from(projets).orderBy(projets.id);

  if (listeProjets.length === 0) {
    return (
      <>
        <PageHeader
          kicker="Projet"
        titre="Décisions éditoriales"
          chapo="Chaque décision porte un statut explicite. L'outil refuse d'afficher une proposition comme si c'était un choix."
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
  const filtre = (sp.statut ?? "") as StatutDecision | "";

  const toutes = await db
    .select()
    .from(decisions)
    .where(eq(decisions.projetId, projetActif.id))
    .orderBy(decisions.axe, decisions.id);

  const visibles = filtre ? toutes.filter((d) => d.statut === filtre) : toutes;
  const axes = [...new Set(visibles.map((d) => d.axe))];

  return (
    <>
      <PageHeader
        titre="Décisions éditoriales"
        chapo="Un choix, une hypothèse et une suggestion extérieure ne se valent pas. Ici le statut est une donnée, pas une nuance de rédaction : une proposition reste une proposition tant que vous ne l'avez pas adoptée."
        precision="Les axes proposés dans le formulaire sont des suggestions de classement, pas une méthodologie. Vous pouvez saisir n'importe quel axe."
      />

      <div className="mb-6 flex flex-wrap items-center gap-2">
        {listeProjets.map((p) => (
          <Link
            key={p.id}
            href={`/decisions?projet=${p.id}${filtre ? `&statut=${filtre}` : ""}`}
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

      <div className="mb-6 flex flex-wrap items-center gap-2 border-y border-zinc-800 py-3">
        <span className="mr-1 text-[11px] uppercase tracking-wide text-zinc-600">
          Filtre
        </span>
        <Link
          href={`/decisions?projet=${projetActif.id}`}
          className={`rounded-full px-2.5 py-1 text-[11px] ${
            !filtre ? "bg-zinc-800 text-zinc-100" : "text-zinc-500 hover:text-zinc-200"
          }`}
        >
          Tout ({toutes.length})
        </Link>
        {STATUTS_DECISION.map((s) => (
          <Link
            key={s}
            href={`/decisions?projet=${projetActif.id}&statut=${s}`}
            className={`rounded-full px-2.5 py-1 text-[11px] ${
              filtre === s ? "bg-zinc-800 text-zinc-100" : "text-zinc-500 hover:text-zinc-200"
            }`}
          >
            {STATUT_DECISION[s].label} ({toutes.filter((d) => d.statut === s).length})
          </Link>
        ))}
      </div>

      {visibles.length === 0 ? (
        <EmptyState titre="Rien à afficher">
          Aucune décision ne correspond à ce filtre pour ce projet.
        </EmptyState>
      ) : (
        <div className="space-y-8">
          {axes.map((axe) => (
            <section key={axe}>
              <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-zinc-500">
                {axe}
              </h2>
              <div className="space-y-2">
                {visibles
                  .filter((d) => d.axe === axe)
                  .map((d) => (
                    <Card key={d.id} className="!p-4">
                      <div className="flex flex-wrap items-start justify-between gap-3">
                        <div className="min-w-0 flex-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <Badge
                              classe={STATUT_DECISION[d.statut].classe}
                              title={STATUT_DECISION[d.statut].aide}
                            >
                              {STATUT_DECISION[d.statut].label}
                            </Badge>
                            <span className="text-[11px] text-zinc-600">
                              origine : {ORIGINE[d.origine]}
                            </span>
                          </div>
                          <Link
                            href={`/decisions/${d.id}`}
                            className="mt-2 block text-sm font-medium text-zinc-100 hover:underline"
                          >
                            {d.intitule}
                          </Link>
                          {d.contenu ? (
                            <p className="mt-1 line-clamp-2 text-xs text-zinc-500">
                              {d.contenu}
                            </p>
                          ) : null}
                        </div>

                        <form action={setDecisionStatut} className="flex items-center gap-2">
                          <input type="hidden" name="id" value={d.id} />
                          <select
                            name="statut"
                            defaultValue={d.statut}
                            className="rounded-lg border border-zinc-700 bg-zinc-950 px-2 py-1 text-xs text-zinc-200"
                          >
                            {STATUTS_DECISION.map((s) => (
                              <option key={s} value={s}>
                                {STATUT_DECISION[s].label}
                              </option>
                            ))}
                          </select>
                          <Button variant="ghost">Requalifier</Button>
                        </form>
                      </div>
                    </Card>
                  ))}
              </div>
            </section>
          ))}
        </div>
      )}

      <div className="mt-6">
        <Disclosure summary="+ Nouvelle décision" tone="accent">
          <form action={createDecision} className="grid gap-3 sm:grid-cols-2">
            <input type="hidden" name="projetId" value={projetActif.id} />
            <Field
              label="Intitulé"
              name="intitule"
              required
              placeholder="Ex. : le protagoniste ne gagne jamais seul"
            />
            <Field
              label="Axe"
              name="axe"
              placeholder={AXES_SUGGERES.join(" · ")}
              aide="Champ libre."
            />
            <Select
              label="Statut"
              name="statut"
              defaultValue="indetermine"
              options={STATUTS_DECISION.map((s) => ({
                value: s,
                label: STATUT_DECISION[s].label,
              }))}
              aide="Par défaut : indéterminé. Rien n'est réputé choisi tant que vous ne l'avez pas dit."
            />
            <Select
              label="Origine"
              name="origine"
              defaultValue="auteur"
              options={ORIGINES.map((o) => ({ value: o, label: ORIGINE[o] }))}
            />
            <Area label="Contenu" name="contenu" rows={3} />
            <Area
              label="Justification"
              name="justification"
              rows={3}
              placeholder="Pourquoi ce statut. Utile surtout pour les « indéterminé » assumés."
            />
            <div className="sm:col-span-2">
              <Button>Créer</Button>
            </div>
          </form>
        </Disclosure>
      </div>
    </>
  );
}
