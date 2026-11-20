import { Card, PageHeader } from "@/components/ui";

export const metadata = { title: "API mobile — Atelier éditorial" };

const ROUTES = [
  {
    methode: "GET",
    chemin: "/api/projets",
    desc: "Liste des projets.",
  },
  {
    methode: "POST",
    chemin: "/api/projets",
    desc: "Crée un projet. Corps : { titre, pitch?, notePerimetre? }.",
  },
  {
    methode: "GET",
    chemin: "/api/decisions?projet=1&statut=choisi",
    desc: "Décisions filtrables, avec leurs confrontations et la répartition par statut.",
  },
  {
    methode: "POST",
    chemin: "/api/decisions",
    desc: "Crée une décision. Corps : { projetId, intitule, axe?, contenu?, statut?, justification? }. L'origine est forcée à « outil ».",
  },
  {
    methode: "GET",
    chemin: "/api/corpus",
    desc: "Éditeurs, cas d'œuvres et segments de public, avec le compte de fiches encore vides.",
  },
  {
    methode: "GET",
    chemin: "/api/ambiguites?projet=1",
    desc: "Registre des ambiguïtés, avec le nombre d'ouvertes.",
  },
  {
    methode: "GET",
    chemin: "/api/health",
    desc: "Vérification de disponibilité.",
  },
] as const;

const NON_TRANCHE = [
  "Aucune authentification n'est posée. En l'état l'API est ouverte : utilisable en local, pas exposable telle quelle.",
  "Aucune stratégie de synchronisation. Si l'app mobile écrit aussi de son côté, la question du gagnant en cas de conflit n'est pas traitée.",
  "Le sens de la dépendance n'est pas fixé : ce service peut être la source de vérité de la couche éditoriale, ou un simple miroir consultable.",
  "Aucun versionnage d'URL. À ajouter avant tout usage réel par un client déployé.",
];

export default function Page() {
  return (
    <>
      <PageHeader
        titre="API mobile"
        chapo="Surface REST permettant à votre application mobile de lire — et écrire partiellement — la couche éditoriale tenue ici."
        precision="Cette API est une proposition de ma part. Vous n'avez pas demandé d'intégration entre les deux applications ; rien n'oblige à s'en servir, et la supprimer ne casse rien du reste de l'outil."
      />

      <Card className="mb-8">
        <h2 className="mb-4 text-sm font-semibold text-zinc-300">Points d&apos;entrée</h2>
        <div className="space-y-2">
          {ROUTES.map((r) => (
            <div
              key={`${r.methode} ${r.chemin}`}
              className="rounded-lg border border-zinc-800 px-3 py-2"
            >
              <div className="flex flex-wrap items-center gap-2">
                <span
                  className={`rounded px-1.5 py-0.5 font-mono text-[10px] font-semibold ${
                    r.methode === "GET"
                      ? "bg-sky-500/15 text-sky-300"
                      : "bg-emerald-500/15 text-emerald-300"
                  }`}
                >
                  {r.methode}
                </span>
                <code className="font-mono text-xs text-zinc-200">{r.chemin}</code>
              </div>
              <p className="mt-1 text-xs text-zinc-500">{r.desc}</p>
            </div>
          ))}
        </div>
      </Card>

      <Card className="border-amber-900/50 bg-amber-950/10">
        <h2 className="text-sm font-semibold text-zinc-100">
          Ce que cette API ne tranche pas
        </h2>
        <ul className="mt-3 space-y-2">
          {NON_TRANCHE.map((item) => (
            <li key={item} className="flex gap-2 text-xs leading-relaxed text-zinc-400">
              <span className="text-amber-300">—</span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </Card>
    </>
  );
}
