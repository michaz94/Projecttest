import {
  doublePrecision,
  index,
  integer,
  primaryKey,
  uniqueIndex,
  pgEnum,
  pgTable,
  serial,
  text,
  timestamp,
} from "drizzle-orm/pg-core";

/**
 * Statut épistémique d'un élément de projet.
 * C'est le coeur du modèle : l'outil refuse de confondre ces trois registres.
 */
export const statutDecisionEnum = pgEnum("statut_decision", [
  "choisi", // l'auteur a tranché
  "indetermine", // ouvert, assumé comme tel
  "proposition", // suggéré (par l'outil, un tiers, une lecture) et NON adopté
  "ecarte", // explicitement rejeté, conservé pour mémoire
]);

export const origineEnum = pgEnum("origine", [
  "auteur",
  "outil",
  "corpus",
  "tiers",
]);

/**
 * Niveau de renseignement d'une fiche de corpus.
 * "squelette" = structure créée par l'outil, contenu à importer depuis vos rapports.
 */
export const fiabiliteEnum = pgEnum("fiabilite", [
  "squelette",
  "a_verifier",
  "source",
]);

export const resultatEnum = pgEnum("resultat", [
  "reussite",
  "echec",
  "mitige",
  "non_classe",
]);

export const relationEnum = pgEnum("relation", [
  "appui",
  "tension",
  "neutre",
  "non_evalue",
]);

export const statutAmbiguiteEnum = pgEnum("statut_ambiguite", [
  "ouverte",
  "arbitree",
  "ecartee",
]);

/**
 * Statut d'une inspiration. Distinct du statut d'une décision :
 * aimer une référence n'est pas l'avoir retenue pour l'œuvre.
 */
export const statutInspirationEnum = pgEnum("statut_inspiration", [
  "reference", // vous appréciez / cela vous intéresse
  "retenue", // effectivement adopté pour l'œuvre
  "indetermine", // rôle dans l'œuvre non défini
  "ecartee",
]);

/** Nature d'une affirmation soumise au fact-check. */
export const natureAffirmationEnum = pgEnum("nature_affirmation", [
  "source", // source historique ou légendaire
  "interpretation",
  "adaptation", // adaptation artistique existante
  "invention", // invention nouvelle
  "marche", // affirmation sur le marché / les éditeurs / les lecteurs
]);

export const statutVerifEnum = pgEnum("statut_verif", [
  "a_verifier",
  "verifie",
  "nuance",
  "refute",
]);

export const projets = pgTable("projets", {
  id: serial("id").primaryKey(),
  titre: text("titre").notNull(),
  pitch: text("pitch").notNull().default(""),
  notePerimetre: text("note_perimetre").notNull().default(""),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/** Corpus 1 — maisons d'édition. */
export const editeurs = pgTable("editeurs", {
  id: serial("id").primaryKey(),
  nom: text("nom").notNull(),
  groupe: text("groupe").notNull().default(""),
  collections: text("collections").notNull().default(""),
  ligneEditoriale: text("ligne_editoriale").notNull().default(""),
  formats: text("formats").notNull().default(""),
  canalSoumission: text("canal_soumission").notNull().default(""),
  notes: text("notes").notNull().default(""),
  source: text("source").notNull().default(""),
  fiabilite: fiabiliteEnum("fiabilite").notNull().default("squelette"),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/** Corpus 2 — oeuvres étudiées (réussites / échecs). */
export const casOeuvres = pgTable(
  "cas_oeuvres",
  {
    id: serial("id").primaryKey(),
    titre: text("titre").notNull(),
    marche: text("marche").notNull().default(""),
    periode: text("periode").notNull().default(""),
    resultat: resultatEnum("resultat").notNull().default("non_classe"),
    facteurs: text("facteurs").notNull().default(""),
    analyse: text("analyse").notNull().default(""),
    source: text("source").notNull().default(""),
    fiabilite: fiabiliteEnum("fiabilite").notNull().default("squelette"),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [index("cas_resultat_idx").on(table.resultat)],
);

/** Corpus 3 — segments de lectorat. */
export const segmentsPublics = pgTable("segments_publics", {
  id: serial("id").primaryKey(),
  nom: text("nom").notNull(),
  description: text("description").notNull().default(""),
  attentes: text("attentes").notNull().default(""),
  frictions: text("frictions").notNull().default(""),
  source: text("source").notNull().default(""),
  fiabilite: fiabiliteEnum("fiabilite").notNull().default("squelette"),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/** Décisions éditoriales du projet, avec statut épistémique explicite. */
export const decisions = pgTable(
  "decisions",
  {
    id: serial("id").primaryKey(),
    projetId: integer("projet_id")
      .notNull()
      .references(() => projets.id, { onDelete: "cascade" }),
    axe: text("axe").notNull().default("Non classé"),
    intitule: text("intitule").notNull(),
    contenu: text("contenu").notNull().default(""),
    statut: statutDecisionEnum("statut").notNull().default("indetermine"),
    origine: origineEnum("origine").notNull().default("auteur"),
    justification: text("justification").notNull().default(""),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [
    index("decisions_projet_idx").on(table.projetId),
    index("decisions_statut_idx").on(table.statut),
  ],
);

/**
 * Mise en regard d'une décision et d'un élément de corpus.
 * Le verdict est saisi par l'auteur : aucun score automatique.
 */
export const confrontations = pgTable(
  "confrontations",
  {
    id: serial("id").primaryKey(),
    decisionId: integer("decision_id")
      .notNull()
      .references(() => decisions.id, { onDelete: "cascade" }),
    refType: text("ref_type").notNull(), // "editeur" | "cas" | "segment"
    refId: integer("ref_id").notNull(),
    relation: relationEnum("relation").notNull().default("non_evalue"),
    note: text("note").notNull().default(""),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [index("confrontations_decision_idx").on(table.decisionId)],
);

/** Registre des ambiguïtés structurantes non résolues. */
export const ambiguites = pgTable(
  "ambiguites",
  {
    id: serial("id").primaryKey(),
    projetId: integer("projet_id")
      .notNull()
      .references(() => projets.id, { onDelete: "cascade" }),
    question: text("question").notNull(),
    enjeu: text("enjeu").notNull().default(""),
    consequences: text("consequences").notNull().default(""),
    statut: statutAmbiguiteEnum("statut").notNull().default("ouverte"),
    arbitrage: text("arbitrage").notNull().default(""),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [index("ambiguites_projet_idx").on(table.projetId)],
);

/**
 * Registre des inspirations. Pièce centrale de la méthode : une référence
 * y est conservée AVEC les glissements d'interprétation à éviter.
 */
export const inspirations = pgTable(
  "inspirations",
  {
    id: serial("id").primaryKey(),
    nom: text("nom").notNull(),
    categorie: text("categorie").notNull().default("Autre"),
    statut: statutInspirationEnum("statut").notNull().default("reference"),
    ceQueVousEnDites: text("ce_que_vous_en_dites").notNull().default(""),
    piegesInterpretation: text("pieges_interpretation").notNull().default(""),
    resteOuvert: text("reste_ouvert").notNull().default(""),
    /** Média d'origine : prose, manga hebdomadaire, web serial, jeu vidéo… */
    medium: text("medium").notNull().default(""),
    /** Économie de publication de la référence, et écart avec votre cible. */
    economie: text("economie").notNull().default(""),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [index("inspirations_statut_idx").on(table.statut)],
);

/**
 * Mécaniques de genre à comprendre. Registre du travail d'étude en cours,
 * distinct des décisions : comprendre une mécanique n'est pas l'adopter.
 */
export const mecaniques = pgTable("mecaniques", {
  id: serial("id").primaryKey(),
  nom: text("nom").notNull(),
  domaine: text("domaine").notNull().default(""),
  exemplifiePar: text("exemplifie_par").notNull().default(""),
  question: text("question").notNull().default(""),
  transposition: text("transposition").notNull().default(""),
  statut: statutVerifEnum("statut").notNull().default("a_verifier"),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/**
 * Constats mesurés sur un corpus. Distinct d'une vérification :
 * ici on a compté quelque chose, et la méthode doit voyager avec le chiffre.
 */
export const constats = pgTable("constats", {
  id: serial("id").primaryKey(),
  titre: text("titre").notNull(),
  corpus: text("corpus").notNull().default(""),
  mesure: text("mesure").notNull().default(""),
  lecture: text("lecture").notNull().default(""),
  limites: text("limites").notNull().default(""),
  contreEpreuve: text("contre_epreuve").notNull().default(""),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/** Fact-check : distingue source, interprétation, adaptation, invention. */
export const verifications = pgTable("verifications", {
  id: serial("id").primaryKey(),
  affirmation: text("affirmation").notNull(),
  nature: natureAffirmationEnum("nature").notNull().default("interpretation"),
  statut: statutVerifEnum("statut").notNull().default("a_verifier"),
  constat: text("constat").notNull().default(""),
  source: text("source").notNull().default(""),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/**
 * Pointeurs vers vos rapports existants.
 * On référence, on ne recopie pas : votre document de contexte reste la source.
 */
export const documents = pgTable("documents", {
  id: serial("id").primaryKey(),
  titre: text("titre").notNull(),
  url: text("url").notNull().default(""),
  nature: text("nature").notNull().default(""),
  etabli: text("etabli").notNull().default(""),
  nonEtabli: text("non_etabli").notNull().default(""),
  createdAt: timestamp("created_at", { withTimezone: true })
    .notNull()
    .defaultNow(),
});

/* ------------------------------------------------ catalogue MAL (étude) --- */

export const oeuvres = pgTable(
  "oeuvres",
  {
    malId: integer("mal_id").primaryKey(),
    titre: text("titre").notNull(),
    titreEn: text("titre_en").notNull().default(""),
    volumes: integer("volumes"),
    chapitres: integer("chapitres"),
    statut: text("statut").notNull().default(""),
    score: doublePrecision("score"),
    scoredBy: integer("scored_by"),
    members: integer("members"),
    anneeDebut: integer("annee_debut"),
    anneeFin: integer("annee_fin"),
    url: text("url").notNull().default(""),
    importeLe: timestamp("importe_le", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (table) => [
    index("oeuvres_score_idx").on(table.score),
    index("oeuvres_annee_idx").on(table.anneeDebut),
  ],
);

/** type : genre | theme | demographic | magazine | auteur */
export const tags = pgTable(
  "tags",
  {
    id: serial("id").primaryKey(),
    type: text("type").notNull(),
    nom: text("nom").notNull(),
  },
  (table) => [uniqueIndex("tags_type_nom_idx").on(table.type, table.nom)],
);

export const oeuvreTags = pgTable(
  "oeuvre_tags",
  {
    oeuvreId: integer("oeuvre_id")
      .notNull()
      .references(() => oeuvres.malId, { onDelete: "cascade" }),
    tagId: integer("tag_id")
      .notNull()
      .references(() => tags.id, { onDelete: "cascade" }),
  },
  (table) => [
    primaryKey({ columns: [table.oeuvreId, table.tagId] }),
    index("oeuvre_tags_tag_idx").on(table.tagId),
  ],
);

export type Oeuvre = typeof oeuvres.$inferSelect;
export type Tag = typeof tags.$inferSelect;

export type Projet = typeof projets.$inferSelect;
export type Inspiration = typeof inspirations.$inferSelect;
export type Mecanique = typeof mecaniques.$inferSelect;
export type Constat = typeof constats.$inferSelect;
export type Verification = typeof verifications.$inferSelect;
export type Document = typeof documents.$inferSelect;
export type Editeur = typeof editeurs.$inferSelect;
export type CasOeuvre = typeof casOeuvres.$inferSelect;
export type SegmentPublic = typeof segmentsPublics.$inferSelect;
export type Decision = typeof decisions.$inferSelect;
export type Confrontation = typeof confrontations.$inferSelect;
export type Ambiguite = typeof ambiguites.$inferSelect;
