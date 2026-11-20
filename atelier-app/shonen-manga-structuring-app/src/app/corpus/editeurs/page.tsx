import { db } from "@/db";
import { editeurs } from "@/db/schema";
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
import { FIABILITE, FIABILITES } from "@/lib/labels";
import { deleteEditeur, upsertEditeur } from "@/app/actions";

export const dynamic = "force-dynamic";

const optionsFiabilite = FIABILITES.map((f) => ({
  value: f,
  label: FIABILITE[f].label,
}));

function Formulaire({
  e,
}: {
  e?: typeof editeurs.$inferSelect;
}) {
  return (
    <form action={upsertEditeur} className="grid gap-3 sm:grid-cols-2">
      {e ? <input type="hidden" name="id" value={e.id} /> : null}
      <Field label="Nom" name="nom" defaultValue={e?.nom ?? ""} required />
      <Field label="Groupe / maison mère" name="groupe" defaultValue={e?.groupe ?? ""} />
      <Field
        label="Collections concernées"
        name="collections"
        defaultValue={e?.collections ?? ""}
        wide
      />
      <Area
        label="Ligne éditoriale"
        name="ligneEditoriale"
        defaultValue={e?.ligneEditoriale ?? ""}
        placeholder="À reprendre de votre rapport. Ne rien écrire ici de mémoire."
        rows={4}
      />
      <Field label="Formats acceptés" name="formats" defaultValue={e?.formats ?? ""} />
      <Field
        label="Canal de soumission"
        name="canalSoumission"
        defaultValue={e?.canalSoumission ?? ""}
      />
      <Area label="Notes" name="notes" defaultValue={e?.notes ?? ""} />
      <Field
        label="Source"
        name="source"
        defaultValue={e?.source ?? ""}
        placeholder="Nom du rapport, page, date de consultation…"
        aide="Sans source, la fiche reste « à vérifier »."
      />
      <Select
        label="Niveau de renseignement"
        name="fiabilite"
        options={optionsFiabilite}
        defaultValue={e?.fiabilite ?? "squelette"}
      />
      <div className="sm:col-span-2">
        <Button>{e ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(editeurs).orderBy(editeurs.nom);

  return (
    <>
      <PageHeader
        titre="Maisons d'édition"
        chapo="Réceptacle de votre analyse des éditeurs français. Une fiche renseignée devient confrontable à vos décisions éditoriales."
        precision="Les fiches livrées sont vides et marquées « Squelette ». Je n'ai pas pré-rempli de lignes éditoriales : je n'ai pas vos rapports, et une approximation plausible serait plus nuisible qu'une case vide."
      />

      {liste.length === 0 ? (
        <EmptyState titre="Aucune fiche">
          Ajoutez les maisons de votre analyse. Le champ « Source » sert à garder la
          trace du document d&apos;origine.
        </EmptyState>
      ) : (
        <div className="space-y-3">
          {liste.map((e) => (
            <Card key={e.id}>
              <div className="flex flex-wrap items-center gap-3">
                <h2 className="text-base font-medium text-zinc-100">{e.nom}</h2>
                <Badge classe={FIABILITE[e.fiabilite].classe} title={FIABILITE[e.fiabilite].aide}>
                  {FIABILITE[e.fiabilite].label}
                </Badge>
                {e.groupe ? (
                  <span className="text-xs text-zinc-500">{e.groupe}</span>
                ) : null}
              </div>

              <dl className="mt-2 grid gap-x-8 sm:grid-cols-2">
                <Prop label="Collections" value={e.collections} />
                <Prop label="Formats" value={e.formats} />
                <Prop label="Ligne éditoriale" value={e.ligneEditoriale} />
                <Prop label="Canal de soumission" value={e.canalSoumission} />
                <Prop label="Notes" value={e.notes} />
                <Prop label="Source" value={e.source} />
              </dl>

              <div className="mt-4">
                <Disclosure summary="Modifier">
                  <Formulaire e={e} />
                  <form action={deleteEditeur} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={e.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-4">
        <Disclosure summary="+ Nouvelle maison d'édition" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
