import { db } from "@/db";
import { mecaniques } from "@/db/schema";
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
import { STATUT_VERIF, STATUTS_VERIF } from "@/lib/labels";
import { deleteMecanique, upsertMecanique } from "@/app/actions";

export const dynamic = "force-dynamic";

function Formulaire({ m }: { m?: typeof mecaniques.$inferSelect }) {
  return (
    <form action={upsertMecanique} className="grid gap-3 sm:grid-cols-2">
      {m ? <input type="hidden" name="id" value={m.id} /> : null}
      <Field label="Mécanique" name="nom" defaultValue={m?.nom ?? ""} required />
      <Field
        label="Domaine"
        name="domaine"
        defaultValue={m?.domaine ?? ""}
        placeholder="Système de pouvoir · Rythme · Archétype · Structure d'arc…"
      />
      <Field
        label="Exemplifiée par"
        name="exemplifiePar"
        defaultValue={m?.exemplifiePar ?? ""}
        wide
      />
      <Area
        label="Question que vous vous posez"
        name="question"
        defaultValue={m?.question ?? ""}
        rows={3}
      />
      <Area
        label="Transposition vers votre cible"
        name="transposition"
        defaultValue={m?.transposition ?? ""}
        rows={3}
        aide="Votre cible : manga en volumes, éditeur français. La mécanique vient souvent d'un autre média et d'une autre économie. C'est ici que la transposition se discute."
      />
      <Select
        label="État de l'étude"
        name="statut"
        defaultValue={m?.statut ?? "a_verifier"}
        options={STATUTS_VERIF.map((s) => ({ value: s, label: STATUT_VERIF[s].label }))}
      />
      <div className="sm:col-span-2">
        <Button>{m ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(mecaniques).orderBy(mecaniques.domaine, mecaniques.id);
  const domaines = [...new Set(liste.map((m) => m.domaine))];
  const aFaire = liste.filter((m) => m.statut === "a_verifier").length;

  return (
    <>
      <PageHeader
        kicker="Étude"
        titre="Mécaniques de genre"
        chapo="Registre du travail d'étude que vous décrivez comme restant : comprendre les mécaniques du genre et vos références. Comprendre une mécanique n'est pas l'adopter — c'est pourquoi ce registre est séparé des décisions."
        precision="Les entrées viennent de votre message. Le champ « transposition » existe parce que la plupart de vos nouvelles références (Worm, progression fantasy, web fiction, Stormlight) ne sont ni du manga ni publiées en volumes chez un éditeur. Ce champ est vide par défaut : je ne préjuge pas de ce qui transpose."
      />

      <div className="mb-6 rounded-xl border border-zinc-800 bg-zinc-900/40 px-4 py-3 text-xs text-zinc-500">
        {liste.length} mécanique{liste.length > 1 ? "s" : ""} ·{" "}
        <span className="text-amber-300">{aFaire}</span> encore à étudier.
      </div>

      {liste.length === 0 ? (
        <EmptyState titre="Registre vide">
          Ajoutez les mécaniques que vous voulez comprendre avant de décider.
        </EmptyState>
      ) : (
        <div className="space-y-8">
          {domaines.map((dom) => (
            <section key={dom}>
              <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-zinc-500">
                {dom || "Non classé"}
              </h2>
              <div className="space-y-2">
                {liste
                  .filter((m) => m.domaine === dom)
                  .map((m) => (
                    <Card key={m.id} className="!p-4">
                      <div className="flex flex-wrap items-center gap-2">
                        <h3 className="text-sm font-medium text-zinc-100">{m.nom}</h3>
                        <Badge classe={STATUT_VERIF[m.statut].classe}>
                          {STATUT_VERIF[m.statut].label}
                        </Badge>
                      </div>
                      {m.exemplifiePar ? (
                        <p className="mt-1 text-[11px] text-zinc-600">
                          Exemplifiée par : {m.exemplifiePar}
                        </p>
                      ) : null}
                      <dl>
                        <Prop label="Question" value={m.question} />
                      </dl>
                      {m.transposition ? (
                        <div className="mt-3 rounded-lg border border-amber-900/40 bg-amber-950/15 px-3 py-2">
                          <span className="text-[11px] font-medium uppercase tracking-wide text-amber-300">
                            Transposition
                          </span>
                          <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">
                            {m.transposition}
                          </p>
                        </div>
                      ) : null}
                      <div className="mt-3">
                        <Disclosure summary="Modifier">
                          <Formulaire m={m} />
                          <form
                            action={deleteMecanique}
                            className="mt-4 border-t border-zinc-800 pt-4"
                          >
                            <input type="hidden" name="id" value={m.id} />
                            <Button variant="danger">Supprimer</Button>
                          </form>
                        </Disclosure>
                      </div>
                    </Card>
                  ))}
              </div>
            </section>
          ))}
        </div>
      )}

      <div className="mt-6">
        <Disclosure summary="+ Nouvelle mécanique" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
