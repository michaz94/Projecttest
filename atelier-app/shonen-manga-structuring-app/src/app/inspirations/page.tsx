import { db } from "@/db";
import { inspirations } from "@/db/schema";
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
import { STATUT_INSPIRATION, STATUTS_INSPIRATION } from "@/lib/labels";
import {
  deleteInspiration,
  setInspirationStatut,
  upsertInspiration,
} from "@/app/actions";

export const dynamic = "force-dynamic";

const optionsStatut = STATUTS_INSPIRATION.map((s) => ({
  value: s,
  label: STATUT_INSPIRATION[s].label,
}));

function Formulaire({ i }: { i?: typeof inspirations.$inferSelect }) {
  return (
    <form action={upsertInspiration} className="grid gap-3 sm:grid-cols-2">
      {i ? <input type="hidden" name="id" value={i.id} /> : null}
      <Field label="Nom" name="nom" defaultValue={i?.nom ?? ""} required />
      <Field
        label="Catégorie"
        name="categorie"
        defaultValue={i?.categorie ?? ""}
        placeholder="Worldbuilding · Folklore · Esthétique · Zone envisagée…"
      />
      <Select
        label="Statut"
        name="statut"
        options={optionsStatut}
        defaultValue={i?.statut ?? "reference"}
        aide="« Référence » par défaut : aimer une source ne l'intègre pas à l'œuvre."
      />
      <Area
        label="Ce que vous en dites"
        name="ceQueVousEnDites"
        defaultValue={i?.ceQueVousEnDites ?? ""}
        rows={3}
      />
      <Area
        label="Pièges d'interprétation"
        name="piegesInterpretation"
        defaultValue={i?.piegesInterpretation ?? ""}
        rows={3}
        aide="Les glissements à ne pas commettre à partir de cette référence — par moi, par une autre IA, ou par vous dans six mois."
      />
      <Field
        label="Média d'origine"
        name="medium"
        defaultValue={i?.medium ?? ""}
        placeholder="Manga hebdomadaire · Roman · Web serial · Jeu vidéo…"
      />
      <Field
        label="Économie de publication"
        name="economie"
        defaultValue={i?.economie ?? ""}
        placeholder="Et son écart avec la vôtre"
      />
      <Area
        label="Ce qui reste ouvert"
        name="resteOuvert"
        defaultValue={i?.resteOuvert ?? ""}
        rows={2}
      />
      <div className="sm:col-span-2">
        <Button>{i ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db
    .select()
    .from(inspirations)
    .orderBy(inspirations.categorie, inspirations.nom);
  const categories = [...new Set(liste.map((i) => i.categorie))];
  const retenues = liste.filter((i) => i.statut === "retenue").length;

  return (
    <>
      <PageHeader
        titre="Inspirations"
        chapo="Vos références, conservées comme références. Chacune porte le champ « pièges d'interprétation » : les raccourcis qu'elle invite et qu'il ne faut pas prendre pour vos intentions."
        precision="Contenu transcrit de votre document de contexte du 29/09/2026, section 3. Je n'ai rien ajouté à votre liste et rien déduit de vos références."
      />

      <div className="mb-6 rounded-xl border border-zinc-800 bg-zinc-900/40 px-4 py-3 text-xs text-zinc-500">
        {liste.length} inspiration{liste.length > 1 ? "s" : ""} enregistrée
        {liste.length > 1 ? "s" : ""} · <span className="text-emerald-300">{retenues}</span>{" "}
        effectivement retenue{retenues > 1 ? "s" : ""} pour l&apos;œuvre. L&apos;écart
        entre les deux est normal et n&apos;est pas un retard.
      </div>

      {liste.length === 0 ? (
        <EmptyState titre="Registre vide">
          Ajoutez vos références avec, pour chacune, ce qu&apos;elle n&apos;implique pas.
        </EmptyState>
      ) : (
        <div className="space-y-8">
          {categories.map((cat) => (
            <section key={cat}>
              <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-zinc-500">
                {cat}
              </h2>
              <div className="space-y-2">
                {liste
                  .filter((i) => i.categorie === cat)
                  .map((i) => (
                    <Card key={i.id} className="!p-4">
                      <div className="flex flex-wrap items-start justify-between gap-3">
                        <div className="min-w-0 flex-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <h3 className="text-sm font-medium text-zinc-100">{i.nom}</h3>
                            <Badge
                              classe={STATUT_INSPIRATION[i.statut].classe}
                              title={STATUT_INSPIRATION[i.statut].aide}
                            >
                              {STATUT_INSPIRATION[i.statut].label}
                            </Badge>
                          </div>
                          {i.medium || i.economie ? (
                            <p className="mt-1 text-[11px] text-zinc-600">
                              {[i.medium, i.economie].filter(Boolean).join(" · ")}
                            </p>
                          ) : null}
                          <dl>
                            <Prop label="Ce que vous en dites" value={i.ceQueVousEnDites} />
                            <Prop label="Reste ouvert" value={i.resteOuvert} />
                          </dl>
                          {i.piegesInterpretation ? (
                            <div className="mt-3 rounded-lg border border-rose-900/40 bg-rose-950/20 px-3 py-2">
                              <span className="text-[11px] font-medium uppercase tracking-wide text-rose-300">
                                Ne pas en déduire
                              </span>
                              <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">
                                {i.piegesInterpretation}
                              </p>
                            </div>
                          ) : null}
                        </div>

                        <form action={setInspirationStatut} className="flex items-center gap-2">
                          <input type="hidden" name="id" value={i.id} />
                          <select
                            name="statut"
                            defaultValue={i.statut}
                            className="rounded-lg border border-zinc-700 bg-zinc-950 px-2 py-1 text-xs text-zinc-200"
                          >
                            {STATUTS_INSPIRATION.map((s) => (
                              <option key={s} value={s}>
                                {STATUT_INSPIRATION[s].label}
                              </option>
                            ))}
                          </select>
                          <Button variant="ghost">Requalifier</Button>
                        </form>
                      </div>

                      <div className="mt-3">
                        <Disclosure summary="Modifier">
                          <Formulaire i={i} />
                          <form
                            action={deleteInspiration}
                            className="mt-4 border-t border-zinc-800 pt-4"
                          >
                            <input type="hidden" name="id" value={i.id} />
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
        <Disclosure summary="+ Nouvelle inspiration" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
