import Link from "next/link";

import { db } from "@/db";
import {
  ambiguites,
  casOeuvres,
  decisions,
  editeurs,
  projets,
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
} from "@/components/ui";
import { STATUT_DECISION, STATUTS_DECISION } from "@/lib/labels";
import { createProjet, deleteProjet, updateProjet } from "./actions";

export const dynamic = "force-dynamic";

const CADRAGE = [
  {
    cle: "pose",
    titre: "Ce que vous avez posé",
    ton: "border-emerald-900/50 bg-emerald-950/20",
    puce: "text-emerald-300",
    items: [
      "Objectif : un battle shōnen commercialement stable, visant d'abord le lectorat occidental, tenant sur plusieurs dizaines de tomes.",
      "Voie visée : l'édition traditionnelle (Ankama, Kana, Glénat). Vous êtes débutant et ne pouvez pas recruter de bêta-lecteurs.",
      "Vous confirmez la section 7 : le diagnostic de marché et le benchmark éditeurs restent à faire.",
      "Vous êtes entré en phase de worldbuilding, et vous observez qu'elle touche déjà à la narration, la structure, le plot, les archétypes et la fonctionnalité des personnages.",
      "Références restant à comprendre, que vous nommez : Hunter x Hunter, Stormlight Archive, Worm, la progression fantasy et la web fiction.",
    ],
  },
  {
    cle: "indetermine",
    titre: "Ce qui reste indéterminé",
    ton: "border-amber-900/50 bg-amber-950/20",
    puce: "text-amber-300",
    items: [
      "La phase « comprendre le public occidental » : vous la déclarez suffisante, puis vous la rouvrez dans la même phrase. Je ne tranche pas, mais la suite en dépend.",
      "Red Hood : référence esthétique, ou cas d'étude d'un échec ? Vos données le documentent comme un échec commercial et mal reçu en Occident. Les deux usages sont légitimes ; leur fusion ne l'est pas.",
      "Vos références de système (Worm, Stormlight, HxH) viennent de médias à forte capacité d'exposition. Votre cible n'en a pas autant par page.",
      "Si les signaux ToC du Weekly Shōnen Jump valent pour une publication en volumes chez un éditeur français, qui n'a pas ce dispositif.",
      "Ce que ce module web doit être vis-à-vis de l'app mobile, et où vit la source de vérité.",
    ],
  },
  {
    cle: "propose",
    titre: "Ce que je propose",
    ton: "border-sky-900/50 bg-sky-950/20",
    puce: "text-sky-300",
    items: [
      "Attacher à chaque référence son média et son économie de publication : c'est là que loge le risque de transposition silencieuse.",
      "Un registre « Mécaniques de genre » séparé des décisions, pour votre travail d'étude en cours — comprendre une mécanique n'est pas l'adopter.",
      "Observer la rétention là où elle est publiquement mesurable : les plateformes de web fiction affichent le décrochage par chapitre. Substitut imparfait, mais vous ne pouvez pas recruter de bêta-lecteurs.",
      "Ne pas redupliquer votre outil de structuration ; indexer vos rapports par leur portée plutôt que recopier leurs chiffres.",
      "Une API REST pour l'app mobile — proposition technique, non engagée.",
    ],
  },
] as const;

export default async function Page() {
  const [listeProjets, listeDecisions, listeAmbiguites, eds, cas, segs] =
    await Promise.all([
      db.select().from(projets).orderBy(projets.id),
      db.select().from(decisions),
      db.select().from(ambiguites),
      db.select().from(editeurs),
      db.select().from(casOeuvres),
      db.select().from(segmentsPublics),
    ]);

  const parStatut = STATUTS_DECISION.map((s) => ({
    statut: s,
    n: listeDecisions.filter((d) => d.statut === s).length,
  }));

  const corpus = [
    { label: "Éditeurs", href: "/corpus/editeurs", rows: eds.length, vides: eds.filter((e) => e.fiabilite === "squelette").length },
    { label: "Cas d'œuvres", href: "/corpus/cas", rows: cas.length, vides: cas.filter((c) => c.fiabilite === "squelette").length },
    { label: "Segments de public", href: "/corpus/segments", rows: segs.length, vides: segs.filter((s) => s.fiabilite === "squelette").length },
  ];

  const ouvertes = listeAmbiguites.filter((a) => a.statut === "ouverte").length;

  return (
    <>
      <PageHeader
        titre="Atelier éditorial"
        chapo="Module web complémentaire d'un outil de structuration de projet shonen. Il ne stocke pas le worldbuilding : il tient le registre des décisions éditoriales, de leur statut, et du corpus de recherche sur lequel elles s'appuient ou se heurtent."
        precision="Mis à jour après lecture de la matrice d'arguments Red Hood, de l'analyse ToC Jajanken, du benchmark fantasy et de la série historique Stormlight. Les six cas d'œuvres portent vos chiffres, repris tels quels. Les fiches d'éditeurs restent vides : vous confirmez que ce travail reste à faire."
      />

      <section className="mb-10 grid gap-4 lg:grid-cols-3">
        {CADRAGE.map((bloc) => (
          <div key={bloc.cle} className={`rounded-xl border p-5 ${bloc.ton}`}>
            <h2 className="text-sm font-semibold text-zinc-100">{bloc.titre}</h2>
            <ul className="mt-3 space-y-2">
              {bloc.items.map((item) => (
                <li key={item} className="flex gap-2 text-xs leading-relaxed text-zinc-400">
                  <span className={bloc.puce}>—</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </section>

      <section className="mb-10">
        <h2 className="mb-3 text-sm font-semibold text-zinc-300">
          État des décisions
        </h2>
        <div className="grid gap-3 sm:grid-cols-4">
          {parStatut.map(({ statut, n }) => (
            <Link
              key={statut}
              href={`/decisions?statut=${statut}`}
              className="rounded-xl border border-zinc-800 bg-zinc-900/60 p-4 transition hover:border-zinc-700"
            >
              <div className="text-2xl font-semibold text-zinc-100">{n}</div>
              <div className="mt-1">
                <Badge classe={STATUT_DECISION[statut].classe}>
                  {STATUT_DECISION[statut].label}
                </Badge>
              </div>
              <p className="mt-2 text-[11px] leading-relaxed text-zinc-600">
                {STATUT_DECISION[statut].aide}
              </p>
            </Link>
          ))}
        </div>
      </section>

      <section className="mb-10 grid gap-4 lg:grid-cols-2">
        <Card>
          <h2 className="text-sm font-semibold text-zinc-300">Corpus de recherche</h2>
          <p className="mt-1 text-xs text-zinc-600">
            Fiches confrontables aux décisions. L&apos;index de vos rapports existants
            est sur la page{" "}
            <Link href="/documents" className="underline underline-offset-2">
              Rapports
            </Link>
            .
          </p>
          <ul className="mt-4 space-y-2">
            {corpus.map((c) => (
              <li key={c.href}>
                <Link
                  href={c.href}
                  className="flex items-center justify-between rounded-lg border border-zinc-800 px-3 py-2 text-sm transition hover:border-zinc-700"
                >
                  <span className="text-zinc-300">{c.label}</span>
                  <span className="text-xs text-zinc-500">
                    {c.rows} fiche{c.rows > 1 ? "s" : ""}
                    {c.vides > 0 ? ` · ${c.vides} à remplir` : ""}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </Card>

        <Card>
          <h2 className="text-sm font-semibold text-zinc-300">
            Ambiguïtés structurantes
          </h2>
          <p className="mt-1 text-xs text-zinc-600">
            Les questions qui conditionnent d&apos;autres décisions et qui ne doivent
            pas être tranchées en silence.
          </p>
          <div className="mt-4 flex items-baseline gap-3">
            <span className="text-3xl font-semibold text-zinc-100">{ouvertes}</span>
            <span className="text-xs text-zinc-500">
              ouverte{ouvertes > 1 ? "s" : ""} sur {listeAmbiguites.length} recensée
              {listeAmbiguites.length > 1 ? "s" : ""}
            </span>
          </div>
          <div className="mt-4">
            <Link
              href="/ambiguites"
              className="text-xs text-zinc-400 underline underline-offset-4 hover:text-zinc-100"
            >
              Ouvrir le registre →
            </Link>
          </div>
        </Card>
      </section>

      <section>
        <h2 className="mb-3 text-sm font-semibold text-zinc-300">Projets</h2>
        <p className="mb-4 max-w-3xl text-xs leading-relaxed text-zinc-600">
          Le multi-projet est une initiative de ma part : vous n&apos;avez évoqué
          qu&apos;un seul projet. Si un seul suffit, n&apos;en créez qu&apos;un.
        </p>

        <div className="space-y-3">
          {listeProjets.map((p) => (
            <Card key={p.id}>
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <h3 className="text-base font-medium text-zinc-100">{p.titre}</h3>
                  {p.pitch ? (
                    <p className="mt-1 max-w-2xl text-sm text-zinc-400">{p.pitch}</p>
                  ) : null}
                  {p.notePerimetre ? (
                    <p className="mt-2 max-w-2xl text-xs text-zinc-600">
                      Périmètre : {p.notePerimetre}
                    </p>
                  ) : null}
                </div>
                <div className="flex gap-2">
                  <Link
                    href={`/decisions?projet=${p.id}`}
                    className="rounded-lg border border-zinc-700 px-3 py-1.5 text-xs text-zinc-300 hover:bg-zinc-800"
                  >
                    Décisions
                  </Link>
                  <Link
                    href={`/ambiguites?projet=${p.id}`}
                    className="rounded-lg border border-zinc-700 px-3 py-1.5 text-xs text-zinc-300 hover:bg-zinc-800"
                  >
                    Ambiguïtés
                  </Link>
                </div>
              </div>

              <div className="mt-4">
                <Disclosure summary="Modifier ce projet">
                  <form action={updateProjet} className="grid gap-3 sm:grid-cols-2">
                    <input type="hidden" name="id" value={p.id} />
                    <Field label="Titre" name="titre" defaultValue={p.titre} required />
                    <Field
                      label="Note de périmètre"
                      name="notePerimetre"
                      defaultValue={p.notePerimetre}
                      placeholder="Ce que ce projet couvre ici, et ce qui reste dans l'app mobile"
                    />
                    <Area label="Pitch" name="pitch" defaultValue={p.pitch} />
                    <div className="sm:col-span-2">
                      <Button>Enregistrer</Button>
                    </div>
                  </form>
                  <form action={deleteProjet} className="mt-4 border-t border-zinc-800 pt-4">
                    <input type="hidden" name="id" value={p.id} />
                    <Button variant="danger">
                      Supprimer le projet et tout ce qui y est rattaché
                    </Button>
                  </form>
                </Disclosure>
              </div>
            </Card>
          ))}
        </div>

        <div className="mt-4">
          <Disclosure summary="+ Nouveau projet" tone="accent">
            <form action={createProjet} className="grid gap-3 sm:grid-cols-2">
              <Field label="Titre" name="titre" required placeholder="Titre de travail" />
              <Field
                label="Note de périmètre"
                name="notePerimetre"
                placeholder="Optionnel"
              />
              <Area label="Pitch" name="pitch" placeholder="Optionnel" />
              <div className="sm:col-span-2">
                <Button>Créer</Button>
              </div>
            </form>
          </Disclosure>
        </div>
      </section>
    </>
  );
}
