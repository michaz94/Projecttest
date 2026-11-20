import { db } from "@/db";
import { documents } from "@/db/schema";
import {
  Area,
  Button,
  Card,
  Disclosure,
  EmptyState,
  Field,
  PageHeader,
} from "@/components/ui";
import { deleteDocument, upsertDocument } from "@/app/actions";

export const dynamic = "force-dynamic";

function Formulaire({ d }: { d?: typeof documents.$inferSelect }) {
  return (
    <form action={upsertDocument} className="grid gap-3 sm:grid-cols-2">
      {d ? <input type="hidden" name="id" value={d.id} /> : null}
      <Field label="Titre" name="titre" defaultValue={d?.titre ?? ""} required />
      <Field label="Nature" name="nature" defaultValue={d?.nature ?? ""} placeholder="Étude de réception, relevé de notes, note de méthode…" />
      <Field label="URL" name="url" defaultValue={d?.url ?? ""} wide />
      <Area
        label="Ce que le document établit"
        name="etabli"
        defaultValue={d?.etabli ?? ""}
        rows={3}
      />
      <Area
        label="Ce qu'il n'établit pas"
        name="nonEtabli"
        defaultValue={d?.nonEtabli ?? ""}
        rows={3}
        aide="Champ le plus utile du registre. C'est lui qui empêche de surinterpréter le document six mois plus tard."
      />
      <div className="sm:col-span-2">
        <Button>{d ? "Enregistrer" : "Ajouter"}</Button>
      </div>
    </form>
  );
}

export default async function Page() {
  const liste = await db.select().from(documents).orderBy(documents.id);

  return (
    <>
      <PageHeader
        kicker="Méthode"
        titre="Vos rapports"
        chapo="Index de vos documents de recherche, avec pour chacun sa portée réelle. Cet index pointe vers vos fichiers, il n'en recopie pas le contenu."
        precision="Choix délibéré, conforme à votre section 8 : votre Markdown de contexte reste le document à maintenir. Dupliquer vos chiffres ici créerait une seconde copie qui divergerait de la première."
      />

      {liste.length === 0 ? (
        <EmptyState titre="Index vide">Ajoutez vos rapports et leur portée.</EmptyState>
      ) : (
        <div className="space-y-3">
          {liste.map((d) => (
            <Card key={d.id}>
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="text-sm font-medium text-zinc-100">{d.titre}</h2>
                {d.nature ? (
                  <span className="text-[11px] text-zinc-600">{d.nature}</span>
                ) : null}
              </div>
              {d.url ? (
                <a
                  href={d.url}
                  target="_blank"
                  rel="noreferrer"
                  className="mt-1 block text-[11px] break-all text-sky-400 hover:underline"
                >
                  {d.url}
                </a>
              ) : null}

              <div className="mt-3 grid gap-3 sm:grid-cols-2">
                {d.etabli ? (
                  <div className="rounded-lg border border-emerald-900/40 bg-emerald-950/15 px-3 py-2">
                    <span className="text-[11px] font-medium uppercase tracking-wide text-emerald-300">
                      Établit
                    </span>
                    <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">{d.etabli}</p>
                  </div>
                ) : null}
                {d.nonEtabli ? (
                  <div className="rounded-lg border border-rose-900/40 bg-rose-950/15 px-3 py-2">
                    <span className="text-[11px] font-medium uppercase tracking-wide text-rose-300">
                      N&apos;établit pas
                    </span>
                    <p className="mt-1 text-xs whitespace-pre-line text-zinc-300">
                      {d.nonEtabli}
                    </p>
                  </div>
                ) : null}
              </div>

              <div className="mt-3">
                <Disclosure summary="Modifier">
                  <Formulaire d={d} />
                  <form action={deleteDocument} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={d.id} />
                    <Button variant="danger">Supprimer</Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>
      )}

      <div className="mt-6">
        <Disclosure summary="+ Nouveau document" tone="accent">
          <Formulaire />
        </Disclosure>
      </div>
    </>
  );
}
