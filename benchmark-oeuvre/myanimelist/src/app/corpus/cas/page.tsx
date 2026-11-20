import { db } from "@/db";
import { casOeuvres } from "@/db/schema";
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
import { FIABILITE, FIABILITES, RESULTAT, RESULTATS } from "@/lib/labels";
import { deleteCas, upsertCas } from "@/app/actions";

export const dynamic = "force-dynamic";

const optionsFiabilite = FIABILITES.map((f) => ({ value: f, label: FIABILITE[f].label }));
const optionsResultat = RESULTATS.map((r) => ({ value: r, label: RESULTAT[r].label }));

function Formulaire({ c }: { c?: typeof casOeuvres.$inferSelect }) {
  return (
    <form action={upsertCas} className="grid gap-3 sm:grid-cols-2">
      {c ? <input type="hidden" name="id" value={c.id} /> : null}
      <Field label="Titre de l'œuvre" name="titre" defaultValue={c?.titre ?? ""} required />
      <Select
        label="Issue observée"
        name="resultat"
        options={optionsResultat}
        defaultValue={c?.resultat ?? "non_classe"}
        aide="Votre qualification, pas un calcul de l'outil."
      />
      <Field label="Marché observé" name="marche" defaultValue={c?.marche ?? ""} placeholder="France, Japon, US…" />
      <Field label="Période" name="periode" defaultValue={c?.periode ?? ""} />
      <Area
        label="Facteurs retenus"
        name="facteurs"
        defaultValue={c?.facteurs ?? ""}
        placeholder="Un facteur par ligne. Ce sont eux que vous confronterez aux décisions."
        rows={4}
      />
      <Area label="Analyse" name="analyse" defaultValue={c?.analyse ?? ""} rows={4} />
      <Field label="Source" name="source" defaultValue={c?.source ?? ""} />
      <Select
        label="Niveau de renseignement"
        name="fiabilite"
        options={optionsFiabilite}
        defaultValue={c?.fiabilite ?? "squelette"}
      />
      <div className="sm:col-span-2">
        <Button>{c ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(casOeuvres).orderBy(casOeuvres.titre);

  return (
    <>
      <PageHeader
        kicker="Étude"
        titre="Cas d'œuvres"
        chapo="Les réussites et les échecs que vous avez étudiés. L'intérêt opérationnel tient aux « facteurs retenus » : ce sont eux qu'on met en regard d'une décision."
        precision="Attention à un biais que l'outil ne corrigera pas à votre place : un facteur extrait d'un succès n'est pas une cause démontrée. La colonne « Issue observée » enregistre une corrélation que vous avez constatée, rien de plus."
      />

      {liste.length === 0 ? (
        <EmptyState titre="Aucun cas enregistré">
          Versez ici les œuvres de votre analyse comparative, avec les facteurs que
          vous en avez tirés.
        </EmptyState>
      ) : (
        <div className="space-y-3">
          {liste.map((c) => (
            <Card key={c.id}>
              <div className="flex flex-wrap items-center gap-3">
                <h2 className="text-base font-medium text-zinc-100">{c.titre}</h2>
                <Badge classe={RESULTAT[c.resultat].classe}>{RESULTAT[c.resultat].label}</Badge>
                <Badge classe={FIABILITE[c.fiabilite].classe} title={FIABILITE[c.fiabilite].aide}>
                  {FIABILITE[c.fiabilite].label}
                </Badge>
                {c.marche || c.periode ? (
                  <span className="text-xs text-zinc-500">
                    {[c.marche, c.periode].filter(Boolean).join(" · ")}
                  </span>
                ) : null}
              </div>

              <dl className="mt-2 grid gap-x-8 sm:grid-cols-2">
                <Prop label="Facteurs retenus" value={c.facteurs} />
                <Prop label="Analyse" value={c.analyse} />
                <Prop label="Source" value={c.source} />
              </dl>

              <div className="mt-4">
                <Disclosure summary="Modifier">
                  <Formulaire c={c} />
                  <form action={deleteCas} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={c.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-4">
        <Disclosure summary="+ Nouveau cas" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
