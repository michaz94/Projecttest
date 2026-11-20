export const STATUT_DECISION = {
  choisi: {
    label: "Choisi",
    aide: "Tranché par vous. Fait autorité dans le projet.",
    classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30",
  },
  indetermine: {
    label: "Indéterminé",
    aide: "Ouvert. Assumé comme non tranché, pas comme un oubli.",
    classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30",
  },
  proposition: {
    label: "Proposition",
    aide: "Suggéré par un tiers ou l'outil. Non adopté tant que vous ne l'avez pas requalifié.",
    classe: "bg-sky-500/15 text-sky-300 ring-sky-500/30",
  },
  ecarte: {
    label: "Écarté",
    aide: "Rejeté explicitement. Conservé pour mémoire.",
    classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30",
  },
} as const;

export type StatutDecision = keyof typeof STATUT_DECISION;
export const STATUTS_DECISION = Object.keys(STATUT_DECISION) as StatutDecision[];

export const ORIGINE = {
  auteur: "Vous",
  outil: "Outil",
  corpus: "Corpus",
  tiers: "Tiers",
} as const;
export type Origine = keyof typeof ORIGINE;
export const ORIGINES = Object.keys(ORIGINE) as Origine[];

export const FIABILITE = {
  squelette: {
    label: "Squelette",
    aide: "Fiche créée vide par l'outil. Contenu à importer depuis vos rapports.",
    classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30",
  },
  a_verifier: {
    label: "À vérifier",
    aide: "Renseigné mais sans source consolidée.",
    classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30",
  },
  source: {
    label: "Sourcé",
    aide: "Adossé à un document identifié.",
    classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30",
  },
} as const;
export type Fiabilite = keyof typeof FIABILITE;
export const FIABILITES = Object.keys(FIABILITE) as Fiabilite[];

export const RESULTAT = {
  reussite: { label: "Réussite", classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30" },
  echec: { label: "Échec", classe: "bg-rose-500/15 text-rose-300 ring-rose-500/30" },
  mitige: { label: "Mitigé", classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30" },
  non_classe: { label: "Non classé", classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30" },
} as const;
export type Resultat = keyof typeof RESULTAT;
export const RESULTATS = Object.keys(RESULTAT) as Resultat[];

export const RELATION = {
  appui: { label: "Appui", classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30" },
  tension: { label: "Tension", classe: "bg-rose-500/15 text-rose-300 ring-rose-500/30" },
  neutre: { label: "Neutre", classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30" },
  non_evalue: { label: "Non évalué", classe: "bg-sky-500/15 text-sky-300 ring-sky-500/30" },
} as const;
export type Relation = keyof typeof RELATION;
export const RELATIONS = Object.keys(RELATION) as Relation[];

export const STATUT_AMBIGUITE = {
  ouverte: { label: "Ouverte", classe: "bg-rose-500/15 text-rose-300 ring-rose-500/30" },
  arbitree: { label: "Arbitrée", classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30" },
  ecartee: { label: "Écartée", classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30" },
} as const;
export type StatutAmbiguite = keyof typeof STATUT_AMBIGUITE;
export const STATUTS_AMBIGUITE = Object.keys(STATUT_AMBIGUITE) as StatutAmbiguite[];

export const STATUT_INSPIRATION = {
  reference: {
    label: "Référence",
    aide: "Vous appréciez cette source. Cela n'en fait pas un élément de l'œuvre.",
    classe: "bg-violet-500/15 text-violet-300 ring-violet-500/30",
  },
  retenue: {
    label: "Retenue",
    aide: "Effectivement adoptée pour l'œuvre, par vous.",
    classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30",
  },
  indetermine: {
    label: "Rôle indéterminé",
    aide: "Présente dans vos inspirations, sans fonction définie dans l'œuvre.",
    classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30",
  },
  ecartee: {
    label: "Écartée",
    aide: "Retirée des inspirations actives.",
    classe: "bg-zinc-500/15 text-zinc-400 ring-zinc-500/30",
  },
} as const;
export type StatutInspiration = keyof typeof STATUT_INSPIRATION;
export const STATUTS_INSPIRATION = Object.keys(
  STATUT_INSPIRATION,
) as StatutInspiration[];

export const NATURE_AFFIRMATION = {
  source: { label: "Source", classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30" },
  interpretation: { label: "Interprétation", classe: "bg-sky-500/15 text-sky-300 ring-sky-500/30" },
  adaptation: { label: "Adaptation", classe: "bg-violet-500/15 text-violet-300 ring-violet-500/30" },
  invention: { label: "Invention", classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30" },
  marche: { label: "Marché", classe: "bg-rose-500/15 text-rose-300 ring-rose-500/30" },
} as const;
export type NatureAffirmation = keyof typeof NATURE_AFFIRMATION;
export const NATURES_AFFIRMATION = Object.keys(
  NATURE_AFFIRMATION,
) as NatureAffirmation[];

export const STATUT_VERIF = {
  a_verifier: { label: "À vérifier", classe: "bg-amber-500/15 text-amber-300 ring-amber-500/30" },
  verifie: { label: "Vérifié", classe: "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30" },
  nuance: { label: "Nuancé", classe: "bg-sky-500/15 text-sky-300 ring-sky-500/30" },
  refute: { label: "Réfuté", classe: "bg-rose-500/15 text-rose-300 ring-rose-500/30" },
} as const;
export type StatutVerif = keyof typeof STATUT_VERIF;
export const STATUTS_VERIF = Object.keys(STATUT_VERIF) as StatutVerif[];

export const REF_TYPE = {
  editeur: "Éditeur",
  cas: "Cas d'œuvre",
  segment: "Segment de public",
} as const;
export type RefType = keyof typeof REF_TYPE;
export const REF_TYPES = Object.keys(REF_TYPE) as RefType[];
