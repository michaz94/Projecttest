import Link from "next/link";

import { db } from "@/db";
import {
  ambiguites,
  casOeuvres,
  decisions,
  editeurs,
  inspirations,
  mecaniques,
  oeuvres,
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
  Fold,
  PageHeader,
  Stat,
} from "@/components/ui";
import { STATUT_DECISION, STATUTS_DECISION } from "@/lib/labels";
import { createProjet, deleteProjet, updateProjet } from "./actions";

export const dynamic = "force-dynamic";

const CADRAGE = [
  {
    cle: "pose",
    titre: "Ce que vous avez posé",
    pastille: "bg-emerald-500",
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
    pastille: "bg-amber-500",
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
    pastille: "bg-sky-500",
    items: [
      "Attacher à chaque référence son média et son économie de publication : c'est là que loge le risque de transposition silencieuse.",
      "Un registre « Mécaniques de genre » séparé des décisions, pour votre travail d'étude en cours — comprendre une mécanique n'est pas l'adopter.",
      "Observer la rétention là où elle est publiquement mesurable : les plateformes de web fiction affichent le décrochage par chapitre. Substitut imparfait, mais vous ne pouvez pas recruter de bêta-lecteurs.",
      "Ne pas redupliquer votre outil de structuration ; indexer vos rapports par leur portée plutôt que recopier leurs chiffres.",
      "Une API REST pour l'app mobile — proposition technique, non engagée.",
    ],
  },
] as const;

const nf = new Intl.NumberFormat("fr-FR");

export default async function Page() {
  const [
    listeProjets,
    listeDecisions,
    listeAmbiguites,
    eds,
    cas,
    segs,
    insp,
    meca,
    oeuvresN,
  ] = await Promise.all([
    db.select().from(projets).orderBy(projets.id),
    db.select().from(decisions),
    db.select().from(ambiguites),
    db.select().from(editeurs),
    db.select().from(casOeuvres),
    db.select().from(segmentsPublics),
    db.select().from(inspirations),
    db.select().from(mecaniques),
    db.$count(oeuvres),
  ]);

  const parStatut = STATUTS_DECISION.map((s) => ({
    statut: s,
    n: listeDecisions.filter((d) => d.statut === s).length,
  }));
  const ouvertes = listeAmbiguites.filter((a) => a.statut === "ouverte").length;
  const retenues = insp.filter((i) => i.statut === "retenue").length;
  const aRemplir =
    eds.filter((e) => e.fiabilite === "squelette").length +
    cas.filter((c) => c.fiabilite === "squelette").length +
    segs.filter((s) => s.fiabilite === "squelette").length;

  const acces = [
    {
      href: "/catalogue",
      titre: "Catalogue",
      sous: `${nf.format(oeuvresN)} œuvres`,
      desc: "Filtrer le corpus MAL par genres, thèmes, magazines, tomes et membres.",
      accent: true,
    },
    {
      href: "/inspirations",
      titre: "Inspirations",
      sous: `${insp.length} références · ${retenues} retenue${retenues > 1 ? "s" : ""}`,
      desc: "Chaque référence garde ses pièges d'interprétation.",
    },
    {
      href: "/mecaniques",
      titre: "Mécaniques",
      sous: `${meca.length} à comprendre`,
      desc: "Comprendre une mécanique n'est pas l'adopter.",
    },
    {
      href: "/corpus/cas",
      titre: "Cas d'œuvres",
      sous: `${cas.length} fiches`,
      desc: "Réussites et échecs, avec chiffres sourcés.",
    },
  ];

  return (
    <>
      <PageHeader
        kicker="Atelier éditorial"
        titre="Où en est le projet"
        chapo="Registre des décisions, de leur statut et du corpus sur lequel elles s'appuient ou se heurtent. Il ne stocke pas le worldbuilding."
        precision="Les cas d'œuvres portent vos chiffres, repris tels quels. Les fiches d'éditeurs restent vides : vous confirmez que ce travail reste à faire."
      />

      {/* Résumé chiffré */}
      <section aria-label="Résumé" className="mb-8">
        <div className="grid grid-cols-2 gap-2.5 sm:grid-cols-4">
          <Stat valeur={nf.format(oeuvresN)} label="œuvres au catalogue" accent />
          <Stat valeur={ouvertes} label={`ambiguïté${ouvertes > 1 ? "s" : ""} ouverte${ouvertes > 1 ? "s" : ""}`} />
          <Stat valeur={parStatut.find((p) => p.statut === "choisi")?.n ?? 0} label="décisions choisies" />
          <Stat valeur={aRemplir} label="fiches à renseigner" />
        </div>
      </section>

      {/* Accès rapides */}
      <section aria-label="Accès rapides" className="mb-9">
        <div className="grid gap-2.5 sm:grid-cols-2">
          {acces.map((a) => (
            <Link
              key={a.href}
              href={a.href}
              className={`group relative block rounded-lg border bg-zinc-900 p-4 transition-all active:translate-x-px active:translate-y-px ${
                a.accent
                  ? "panel-hard border-zinc-100 hover:-translate-x-px hover:-translate-y-px"
                  : "border-zinc-700 hover:border-zinc-100"
              }`}
            >
              <div className="flex items-baseline justify-between gap-3">
                <h2 className="font-display text-lg font-extrabold tracking-tight text-zinc-100">
                  {a.titre}
                </h2>
                <span className="text-lg text-vermilion transition-transform group-hover:translate-x-0.5">
                  →
                </span>
              </div>
              <p className="mt-0.5 font-mono text-[11px] font-semibold text-vermilion">
                {a.sous}
              </p>
              <p className="mt-1.5 text-[13px] leading-snug text-zinc-500">{a.desc}</p>
            </Link>
          ))}
        </div>
      </section>

      {/* Cadrage : trois registres qu'on ne mélange pas */}
      <section aria-label="Cadrage" className="mb-9">
        <div className="mb-3 flex items-end justify-between gap-3">
          <h2 className="font-display text-xl font-extrabold tracking-tight text-zinc-100">
            Le cadrage
          </h2>
          <p className="max-w-[16rem] text-right text-[11px] leading-tight text-zinc-600">
            Trois registres distincts : jamais mélangés.
          </p>
        </div>
        <div className="grid gap-2.5 lg:grid-cols-3">
          {CADRAGE.map((bloc, i) => (
            <Fold
              key={bloc.cle}
              ouvert={i === 1}
              titre={
                <span className="flex items-center gap-2">
                  <span className={`size-2.5 rounded-sm ${bloc.pastille}`} />
                  {bloc.titre}
                  <span className="font-mono text-[10px] font-semibold text-zinc-600">
                    {bloc.items.length}
                  </span>
                </span>
              }
            >
              <ul className="space-y-2.5">
                {bloc.items.map((item) => (
                  <li key={item} className="flex gap-2.5 text-[13px] leading-relaxed text-zinc-400">
                    <span className={`mt-[7px] size-1.5 shrink-0 rounded-full ${bloc.pastille}`} />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </Fold>
          ))}
        </div>
      </section>

      {/* Décisions par statut */}
      <section aria-label="Décisions" className="mb-9">
        <h2 className="mb-3 font-display text-xl font-extrabold tracking-tight text-zinc-100">
          Statut des décisions
        </h2>
        <div className="grid grid-cols-2 gap-2.5 sm:grid-cols-4">
          {parStatut.map(({ statut, n }) => (
            <Link
              key={statut}
              href={`/decisions?statut=${statut}`}
              className="rounded-lg border border-zinc-700 bg-zinc-900 p-3.5 transition-colors hover:border-zinc-100"
            >
              <div className="flex items-center justify-between">
                <span className="font-display text-3xl leading-none font-extrabold text-zinc-100 tabular-nums">
                  {n}
                </span>
                <Badge classe={STATUT_DECISION[statut].classe}>
                  {STATUT_DECISION[statut].label}
                </Badge>
              </div>
              <p className="mt-2.5 text-[11px] leading-snug text-zinc-500">
                {STATUT_DECISION[statut].aide}
              </p>
            </Link>
          ))}
        </div>
      </section>

      {/* Projets */}
      <section aria-label="Projets">
        <h2 className="font-display text-xl font-extrabold tracking-tight text-zinc-100">
          Projets
        </h2>
        <p className="mt-1 mb-4 max-w-2xl text-xs leading-relaxed text-zinc-500">
          Le multi-projet est une initiative de l&apos;outil : vous n&apos;avez évoqué
          qu&apos;un seul projet. Si un seul suffit, n&apos;en créez qu&apos;un.
        </p>

        <div className="space-y-3">
          {listeProjets.map((p) => (
            <Card key={p.id}>
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div className="min-w-0">
                  <h3 className="font-display text-lg font-bold text-zinc-100">{p.titre}</h3>
                  {p.pitch ? (
                    <p className="mt-1 max-w-2xl text-sm text-zinc-400">{p.pitch}</p>
                  ) : null}
                  {p.notePerimetre ? (
                    <p className="mt-2 max-w-2xl text-xs leading-relaxed text-zinc-500">
                      <span className="font-mono text-[10px] font-semibold tracking-wider text-zinc-600 uppercase">
                        Périmètre
                      </span>{" "}
                      {p.notePerimetre}
                    </p>
                  ) : null}
                </div>
                <div className="flex gap-2">
                  <Link
                    href={`/decisions?projet=${p.id}`}
                    className="inline-flex min-h-10 items-center rounded-md border border-zinc-700 bg-zinc-900 px-3 text-xs font-semibold text-zinc-200 hover:border-zinc-100"
                  >
                    Décisions
                  </Link>
                  <Link
                    href={`/ambiguites?projet=${p.id}`}
                    className="inline-flex min-h-10 items-center rounded-md border border-zinc-700 bg-zinc-900 px-3 text-xs font-semibold text-zinc-200 hover:border-zinc-100"
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

        <div className="mt-3">
          <Disclosure summary="Nouveau projet" tone="accent">
            <form action={createProjet} className="grid gap-3 sm:grid-cols-2">
              <Field label="Titre" name="titre" required placeholder="Titre de travail" />
              <Field label="Note de périmètre" name="notePerimetre" placeholder="Optionnel" />
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
