import { db } from "@/db";
import { constats } from "@/db/schema";
import {
  Area,
  Button,
  Card,
  Disclosure,
  EmptyState,
  Field,
  PageHeader,
} from "@/components/ui";
import { deleteConstat, upsertConstat } from "@/app/actions";

export const dynamic = "force-dynamic";

function Formulaire({ c }: { c?: typeof constats.$inferSelect }) {
  return (
    <form action={upsertConstat} className="grid gap-3 sm:grid-cols-2">
      {c ? <input type="hidden" name="id" value={c.id} /> : null}
      <Field label="Titre" name="titre" defaultValue={c?.titre ?? ""} required />
      <Field label="Corpus" name="corpus" defaultValue={c?.corpus ?? ""} />
      <Area label="Mesure" name="mesure" defaultValue={c?.mesure ?? ""} rows={5} />
      <Area label="Lecture proposée" name="lecture" defaultValue={c?.lecture ?? ""} rows={4} />
      <Area label="Limites" name="limites" defaultValue={c?.limites ?? ""} rows={3} />
      <Area
        label="Contre-épreuve à mener"
        name="contreEpreuve"
        defaultValue={c?.contreEpreuve ?? ""}
        rows={2}
      />
      <div className="sm:col-span-2">
        <Button>{c ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(constats).orderBy(constats.id);

  return (
    <>
      <PageHeader
        titre="Constats mesurés"
        chapo="Comptages effectués sur le corpus brut Reddit de votre dossier : 4 432 commentaires Red Hood, 18 chapitres, plus 4 925 commentaires de trois séries témoins."
        precision="Produits par l'outil, pas par vos rapports. Votre synthèse v2 précise n'avoir relu que 371 textes de premier niveau sur les chapitres 1, 5 et 15, et ne mesure aucune fréquence. Ces comptages portent sur l'intégralité du corpus, mais par appariement lexical : un commentaire contenant « slow » peut dire « ce n'est pas trop lent ». Le script est dans scripts/analyse_red_hood.py, rejouable."
      />

      {liste.length === 0 ? (
        <EmptyState titre="Aucun constat">Rien n&apos;a encore été mesuré.</EmptyState>
      ) : (
        <div className="space-y-4">
          {liste.map((c) => (
            <Card key={c.id}>
              <h2 className="text-sm font-semibold text-zinc-100">{c.titre}</h2>
              {c.corpus ? (
                <p className="mt-1 text-[11px] text-zinc-600">Corpus : {c.corpus}</p>
              ) : null}
              {c.mesure ? (
                <pre className="mt-3 overflow-x-auto rounded-lg border border-zinc-800 bg-zinc-950/70 p-3 font-mono text-[11px] leading-relaxed whitespace-pre text-zinc-300">
                  {c.mesure}
                </pre>
              ) : null}
              {c.lecture ? (
                <div className="mt-3 rounded-lg border border-sky-900/40 bg-sky-950/15 px-3 py-2">
                  <span className="text-[11px] font-medium uppercase tracking-wide text-sky-300">
                    Lecture proposée
                  </span>
                  <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">{c.lecture}</p>
                </div>
              ) : null}
              {c.limites ? (
                <div className="mt-2 rounded-lg border border-rose-900/40 bg-rose-950/15 px-3 py-2">
                  <span className="text-[11px] font-medium uppercase tracking-wide text-rose-300">
                    Limites
                  </span>
                  <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">{c.limites}</p>
                </div>
              ) : null}
              {c.contreEpreuve ? (
                <p className="mt-2 text-[11px] text-zinc-500">
                  Contre-épreuve : {c.contreEpreuve}
                </p>
              ) : null}
              <div className="mt-3">
                <Disclosure summary="Modifier">
                  <Formulaire c={c} />
                  <form action={deleteConstat} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={c.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-6">
        <Disclosure summary="+ Nouveau constat" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
