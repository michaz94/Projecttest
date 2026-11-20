import { db } from "@/db";
import { segmentsPublics } from "@/db/schema";
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
import { deleteSegment, upsertSegment } from "@/app/actions";

export const dynamic = "force-dynamic";

const optionsFiabilite = FIABILITES.map((f) => ({ value: f, label: FIABILITE[f].label }));

function Formulaire({ s }: { s?: typeof segmentsPublics.$inferSelect }) {
  return (
    <form action={upsertSegment} className="grid gap-3 sm:grid-cols-2">
      {s ? <input type="hidden" name="id" value={s.id} /> : null}
      <Field label="Nom du segment" name="nom" defaultValue={s?.nom ?? ""} required />
      <Field label="Source" name="source" defaultValue={s?.source ?? ""} />
      <Area label="Description" name="description" defaultValue={s?.description ?? ""} rows={3} />
      <Area
        label="Attentes"
        name="attentes"
        defaultValue={s?.attentes ?? ""}
        placeholder="Une attente par ligne."
        rows={4}
      />
      <Area
        label="Points de friction"
        name="frictions"
        defaultValue={s?.frictions ?? ""}
        placeholder="Ce qui fait décrocher ce segment."
        rows={4}
      />
      <Select
        label="Niveau de renseignement"
        name="fiabilite"
        options={optionsFiabilite}
        defaultValue={s?.fiabilite ?? "squelette"}
      />
      <div className="sm:col-span-2">
        <Button>{s ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(segmentsPublics).orderBy(segmentsPublics.nom);

  return (
    <>
      <PageHeader
        titre="Segments de public"
        chapo="Votre découpage du lectorat occidental. Un segment sert de contrepoint à une décision : à qui elle parle, à qui elle coûte."
        precision="« Public occidental » est une catégorie que vous avez posée, pas que j'ai déduite. Reste indéterminé, et je ne le tranche pas : s'il faut la subdiviser (marché francophone, anglophone, tranches d'âge, lecteurs de manga vs lecteurs de BD), et si ce découpage engage le récit ou seulement la stratégie de placement."
      />

      {liste.length === 0 ? (
        <EmptyState titre="Aucun segment">
          Reprenez les segments de votre étude de public plutôt que d&apos;en créer de
          nouveaux ici.
        </EmptyState>
      ) : (
        <div className="space-y-3">
          {liste.map((s) => (
            <Card key={s.id}>
              <div className="flex flex-wrap items-center gap-3">
                <h2 className="text-base font-medium text-zinc-100">{s.nom}</h2>
                <Badge classe={FIABILITE[s.fiabilite].classe} title={FIABILITE[s.fiabilite].aide}>
                  {FIABILITE[s.fiabilite].label}
                </Badge>
              </div>

              <dl className="mt-2 grid gap-x-8 sm:grid-cols-2">
                <Prop label="Description" value={s.description} />
                <Prop label="Attentes" value={s.attentes} />
                <Prop label="Points de friction" value={s.frictions} />
                <Prop label="Source" value={s.source} />
              </dl>

              <div className="mt-4">
                <Disclosure summary="Modifier">
                  <Formulaire s={s} />
                  <form action={deleteSegment} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={s.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-4">
        <Disclosure summary="+ Nouveau segment" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
