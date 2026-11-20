import Link from "next/link";
import { notFound } from "next/navigation";
import { eq } from "drizzle-orm";

import { db } from "@/db";
import {
  casOeuvres,
  confrontations,
  decisions,
  editeurs,
  segmentsPublics,
} from "@/db/schema";
import {
  Area,
  Badge,
  Button,
  Card,
  Disclosure,
  Field,
  PageHeader,
  Prop,
  Select,
} from "@/components/ui";
import {
  ORIGINE,
  ORIGINES,
  REF_TYPE,
  RELATION,
  RELATIONS,
  STATUT_DECISION,
  STATUTS_DECISION,
  type RefType,
} from "@/lib/labels";
import {
  createConfrontation,
  deleteConfrontation,
  deleteDecision,
  updateConfrontation,
  updateDecision,
} from "@/app/actions";

export const dynamic = "force-dynamic";

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const decisionId = Number.parseInt(id, 10);
  if (!decisionId) notFound();

  const [decision] = await db
    .select()
    .from(decisions)
    .where(eq(decisions.id, decisionId))
    .limit(1);
  if (!decision) notFound();

  const [liens, eds, cas, segs] = await Promise.all([
    db.select().from(confrontations).where(eq(confrontations.decisionId, decisionId)),
    db.select().from(editeurs).orderBy(editeurs.nom),
    db.select().from(casOeuvres).orderBy(casOeuvres.titre),
    db.select().from(segmentsPublics).orderBy(segmentsPublics.nom),
  ]);

  const nomDe = (type: string, refId: number): string => {
    if (type === "editeur") return eds.find((e) => e.id === refId)?.nom ?? "fiche supprimée";
    if (type === "cas") return cas.find((c) => c.id === refId)?.titre ?? "fiche supprimée";
    return segs.find((s) => s.id === refId)?.nom ?? "fiche supprimée";
  };

  const optionsRef = [
    ...eds.map((e) => ({ value: `editeur:${e.id}`, label: `Éditeur — ${e.nom}` })),
    ...cas.map((c) => ({ value: `cas:${c.id}`, label: `Cas — ${c.titre}` })),
    ...segs.map((s) => ({ value: `segment:${s.id}`, label: `Public — ${s.nom}` })),
  ];

  const appuis = liens.filter((l) => l.relation === "appui").length;
  const tensions = liens.filter((l) => l.relation === "tension").length;

  return (
    <>
      <Link
        href={`/decisions?projet=${decision.projetId}`}
        className="mb-4 inline-block text-xs text-zinc-500 hover:text-zinc-200"
      >
        ← Retour aux décisions
      </Link>

      <PageHeader
        titre={decision.intitule}
        chapo={`Axe : ${decision.axe} · Origine : ${ORIGINE[decision.origine]}`}
      />

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <Badge classe={STATUT_DECISION[decision.statut].classe}>
          {STATUT_DECISION[decision.statut].label}
        </Badge>
        <span className="text-xs text-zinc-500">
          {STATUT_DECISION[decision.statut].aide}
        </span>
      </div>

      <Card className="mb-8">
        <dl>
          <Prop label="Contenu" value={decision.contenu} />
          <Prop label="Justification" value={decision.justification} />
        </dl>
        {!decision.contenu && !decision.justification ? (
          <p className="text-sm text-zinc-600">Aucun contenu saisi.</p>
        ) : null}
        <div className="mt-4">
          <Disclosure summary="Modifier la décision">
            <form action={updateDecision} className="grid gap-3 sm:grid-cols-2">
              <input type="hidden" name="id" value={decision.id} />
              <Field label="Intitulé" name="intitule" defaultValue={decision.intitule} required />
              <Field label="Axe" name="axe" defaultValue={decision.axe} />
              <Select
                label="Statut"
                name="statut"
                defaultValue={decision.statut}
                options={STATUTS_DECISION.map((s) => ({
                  value: s,
                  label: STATUT_DECISION[s].label,
                }))}
              />
              <Select
                label="Origine"
                name="origine"
                defaultValue={decision.origine}
                options={ORIGINES.map((o) => ({ value: o, label: ORIGINE[o] }))}
              />
              <Area label="Contenu" name="contenu" defaultValue={decision.contenu} rows={4} />
              <Area
                label="Justification"
                name="justification"
                defaultValue={decision.justification}
                rows={4}
              />
              <div className="sm:col-span-2">
                <Button>Enregistrer</Button>
              </div>
            </form>
            <form action={deleteDecision} className="mt-4 border-t border-zinc-800 pt-4">
              <input type="hidden" name="id" value={decision.id} />
              <Button variant="danger">Supprimer cette décision</Button>
            </form>
          </Disclosure>
        </div>
      </Card>

      <section>
        <div className="mb-3 flex flex-wrap items-baseline justify-between gap-2">
          <h2 className="text-sm font-semibold text-zinc-300">
            Mise en regard du corpus
          </h2>
          <span className="text-xs text-zinc-600">
            {appuis} appui{appuis > 1 ? "s" : ""} · {tensions} tension
            {tensions > 1 ? "s" : ""} · {liens.length} lien{liens.length > 1 ? "s" : ""}
          </span>
        </div>
        <p className="mb-4 max-w-3xl text-xs leading-relaxed text-zinc-600">
          Un décompte n&apos;est pas un verdict. Trois appuis contre une tension ne
          rendent pas une décision bonne : c&apos;est à vous de peser. L&apos;outil
          n&apos;additionne rien de plus que ce que vous avez coché.
        </p>

        {optionsRef.length === 0 ? (
          <div className="rounded-xl border border-dashed border-zinc-800 p-6 text-xs text-zinc-500">
            Le corpus est vide. Renseignez au moins une fiche (éditeur, cas ou public)
            pour pouvoir confronter cette décision.
          </div>
        ) : (
          <>
            <div className="space-y-2">
              {liens.map((l) => (
                <Card key={l.id} className="!p-4">
                  <div className="flex flex-wrap items-center gap-3">
                    <Badge classe={RELATION[l.relation].classe}>
                      {RELATION[l.relation].label}
                    </Badge>
                    <span className="text-sm text-zinc-200">
                      {nomDe(l.refType, l.refId)}
                    </span>
                    <span className="text-[11px] text-zinc-600">
                      {REF_TYPE[l.refType as RefType] ?? l.refType}
                    </span>
                  </div>
                  {l.note ? (
                    <p className="mt-2 text-xs whitespace-pre-line text-zinc-400">{l.note}</p>
                  ) : null}
                  <div className="mt-3">
                    <Disclosure summary="Modifier le lien">
                      <form action={updateConfrontation} className="grid gap-3 sm:grid-cols-2">
                        <input type="hidden" name="id" value={l.id} />
                        <input type="hidden" name="decisionId" value={decision.id} />
                        <Select
                          label="Relation"
                          name="relation"
                          defaultValue={l.relation}
                          options={RELATIONS.map((r) => ({
                            value: r,
                            label: RELATION[r].label,
                          }))}
                        />
                        <Area label="Note" name="note" defaultValue={l.note} rows={3} />
                        <div className="sm:col-span-2 flex gap-2">
                          <Button>Enregistrer</Button>
                        </div>
                      </form>
                      <form action={deleteConfrontation} className="mt-4 border-t border-zinc-800 pt-4">
                        <input type="hidden" name="id" value={l.id} />
                        <input type="hidden" name="decisionId" value={decision.id} />
                        <Button variant="danger">Retirer</Button>
                      </form>
                    </Disclosure>
                  </div>
                </Card>
              ))}
            </div>

            <div className="mt-4">
              <Disclosure summary="+ Confronter à un élément du corpus" tone="accent">
                <form action={createConfrontation} className="grid gap-3 sm:grid-cols-2">
                  <input type="hidden" name="decisionId" value={decision.id} />
                  <Select label="Élément du corpus" name="ref" options={optionsRef} />
                  <Select
                    label="Relation"
                    name="relation"
                    defaultValue="non_evalue"
                    options={RELATIONS.map((r) => ({ value: r, label: RELATION[r].label }))}
                    aide="« Non évalué » est un choix légitime : le lien existe, le verdict attend."
                  />
                  <Area
                    label="Note"
                    name="note"
                    rows={3}
                    placeholder="En quoi cet élément appuie ou contrarie la décision."
                  />
                  <div className="sm:col-span-2">
                    <Button>Ajouter le lien</Button>
                  </div>
                </form>
              </Disclosure>
            </div>
          </>
        )}
      </section>
    </>
  );
}
