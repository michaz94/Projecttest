import { db } from "@/db";
import { verifications } from "@/db/schema";
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
import {
  NATURE_AFFIRMATION,
  NATURES_AFFIRMATION,
  STATUT_VERIF,
  STATUTS_VERIF,
} from "@/lib/labels";
import { deleteVerification, upsertVerification } from "@/app/actions";

export const dynamic = "force-dynamic";

function Formulaire({ v }: { v?: typeof verifications.$inferSelect }) {
  return (
    <form action={upsertVerification} className="grid gap-3 sm:grid-cols-2">
      {v ? <input type="hidden" name="id" value={v.id} /> : null}
      <Area
        label="Affirmation"
        name="affirmation"
        defaultValue={v?.affirmation ?? ""}
        rows={2}
        placeholder="L'énoncé tel qu'il a été formulé, sans l'adoucir."
      />
      <Select
        label="Nature"
        name="nature"
        defaultValue={v?.nature ?? "interpretation"}
        options={NATURES_AFFIRMATION.map((n) => ({
          value: n,
          label: NATURE_AFFIRMATION[n].label,
        }))}
        aide="Source historique, interprétation, adaptation artistique, invention nouvelle, ou affirmation de marché."
      />
      <Select
        label="Statut"
        name="statut"
        defaultValue={v?.statut ?? "a_verifier"}
        options={STATUTS_VERIF.map((s) => ({ value: s, label: STATUT_VERIF[s].label }))}
      />
      <Area label="Constat" name="constat" defaultValue={v?.constat ?? ""} rows={3} />
      <Field label="Source" name="source" defaultValue={v?.source ?? ""} wide />
      <div className="sm:col-span-2">
        <Button>{v ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(verifications).orderBy(verifications.id);
  const aVerifier = liste.filter((v) => v.statut === "a_verifier").length;

  return (
    <>
      <PageHeader
        kicker="Méthode"
        titre="Vérifications"
        chapo="Registre de fact-check. Chaque énoncé y est classé par nature — source, interprétation, adaptation, invention, affirmation de marché — parce que ces quatre registres se confondent vite quand on travaille à partir de folklore."
        precision="Les quatre premières entrées sont reprises de votre document de contexte, section 4. Une variante de folklore n'est pas un canon universel, et une fonction narrative possible n'est pas « la vraie fonction » du mythe."
      />

      <div className="mb-6 rounded-xl border border-zinc-800 bg-zinc-900/40 px-4 py-3 text-xs text-zinc-500">
        {liste.length} entrée{liste.length > 1 ? "s" : ""} ·{" "}
        <span className="text-amber-300">{aVerifier}</span> en attente de vérification.
      </div>

      {liste.length === 0 ? (
        <EmptyState titre="Registre vide">
          Consignez ici toute affirmation dont la fausseté coûterait cher.
        </EmptyState>
      ) : (
        <div className="space-y-2">
          {liste.map((v) => (
            <Card key={v.id} className="!p-4">
              <div className="flex flex-wrap items-center gap-2">
                <Badge classe={STATUT_VERIF[v.statut].classe}>
                  {STATUT_VERIF[v.statut].label}
                </Badge>
                <Badge classe={NATURE_AFFIRMATION[v.nature].classe}>
                  {NATURE_AFFIRMATION[v.nature].label}
                </Badge>
              </div>
              <p className="mt-2 text-sm text-zinc-100">{v.affirmation}</p>
              <dl>
                <Prop label="Constat" value={v.constat} />
              </dl>
              {v.source ? (
                <p className="mt-2 text-[11px] break-all text-zinc-600">{v.source}</p>
              ) : null}
              <div className="mt-3">
                <Disclosure summary="Modifier">
                  <Formulaire v={v} />
                  <form
                    action={deleteVerification}
                    className="mt-4 border-t border-zinc-800 pt-4"
                  >
                    <input type="hidden" name="id" value={v.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-6">
        <Disclosure summary="+ Nouvelle vérification" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
