"use server";

import { revalidatePath } from "next/cache";
import { eq } from "drizzle-orm";

import { db } from "@/db";
import {
  ambiguites,
  constats,
  casOeuvres,
  confrontations,
  decisions,
  documents,
  editeurs,
  inspirations,
  mecaniques,
  projets,
  segmentsPublics,
  verifications,
} from "@/db/schema";

function str(data: FormData, key: string, fallback = ""): string {
  const value = data.get(key);
  return typeof value === "string" && value.trim().length > 0
    ? value.trim()
    : fallback;
}

function num(data: FormData, key: string): number {
  return Number.parseInt(str(data, key, "0"), 10) || 0;
}

/* ------------------------------------------------------------------ projets */

export async function createProjet(data: FormData) {
  const titre = str(data, "titre");
  if (!titre) return;
  await db.insert(projets).values({
    titre,
    pitch: str(data, "pitch"),
    notePerimetre: str(data, "notePerimetre"),
  });
  revalidatePath("/");
}

export async function updateProjet(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db
    .update(projets)
    .set({
      titre: str(data, "titre", "Sans titre"),
      pitch: str(data, "pitch"),
      notePerimetre: str(data, "notePerimetre"),
    })
    .where(eq(projets.id, id));
  revalidatePath("/");
}

export async function deleteProjet(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(projets).where(eq(projets.id, id));
  revalidatePath("/");
}

/* ----------------------------------------------------------------- éditeurs */

type EditeurFields = typeof editeurs.$inferInsert;

function editeurFromForm(data: FormData): EditeurFields {
  return {
    nom: str(data, "nom", "Sans nom"),
    groupe: str(data, "groupe"),
    collections: str(data, "collections"),
    ligneEditoriale: str(data, "ligneEditoriale"),
    formats: str(data, "formats"),
    canalSoumission: str(data, "canalSoumission"),
    notes: str(data, "notes"),
    source: str(data, "source"),
    fiabilite: str(data, "fiabilite", "squelette") as EditeurFields["fiabilite"],
  };
}

export async function upsertEditeur(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(editeurs).set(editeurFromForm(data)).where(eq(editeurs.id, id));
  } else {
    await db.insert(editeurs).values(editeurFromForm(data));
  }
  revalidatePath("/corpus/editeurs");
  revalidatePath("/");
}

export async function deleteEditeur(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(editeurs).where(eq(editeurs.id, id));
  revalidatePath("/corpus/editeurs");
  revalidatePath("/");
}

/* --------------------------------------------------------------------- cas */

type CasFields = typeof casOeuvres.$inferInsert;

function casFromForm(data: FormData): CasFields {
  return {
    titre: str(data, "titre", "Sans titre"),
    marche: str(data, "marche"),
    periode: str(data, "periode"),
    resultat: str(data, "resultat", "non_classe") as CasFields["resultat"],
    facteurs: str(data, "facteurs"),
    analyse: str(data, "analyse"),
    source: str(data, "source"),
    fiabilite: str(data, "fiabilite", "squelette") as CasFields["fiabilite"],
  };
}

export async function upsertCas(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(casOeuvres).set(casFromForm(data)).where(eq(casOeuvres.id, id));
  } else {
    await db.insert(casOeuvres).values(casFromForm(data));
  }
  revalidatePath("/corpus/cas");
  revalidatePath("/");
}

export async function deleteCas(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(casOeuvres).where(eq(casOeuvres.id, id));
  revalidatePath("/corpus/cas");
  revalidatePath("/");
}

/* ---------------------------------------------------------------- segments */

type SegmentFields = typeof segmentsPublics.$inferInsert;

function segmentFromForm(data: FormData): SegmentFields {
  return {
    nom: str(data, "nom", "Sans nom"),
    description: str(data, "description"),
    attentes: str(data, "attentes"),
    frictions: str(data, "frictions"),
    source: str(data, "source"),
    fiabilite: str(data, "fiabilite", "squelette") as SegmentFields["fiabilite"],
  };
}

export async function upsertSegment(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db
      .update(segmentsPublics)
      .set(segmentFromForm(data))
      .where(eq(segmentsPublics.id, id));
  } else {
    await db.insert(segmentsPublics).values(segmentFromForm(data));
  }
  revalidatePath("/corpus/segments");
  revalidatePath("/");
}

export async function deleteSegment(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(segmentsPublics).where(eq(segmentsPublics.id, id));
  revalidatePath("/corpus/segments");
  revalidatePath("/");
}

/* --------------------------------------------------------------- décisions */

type DecisionFields = typeof decisions.$inferInsert;

export async function createDecision(data: FormData) {
  const projetId = num(data, "projetId");
  const intitule = str(data, "intitule");
  if (!projetId || !intitule) return;
  await db.insert(decisions).values({
    projetId,
    intitule,
    axe: str(data, "axe", "Non classé"),
    contenu: str(data, "contenu"),
    statut: str(data, "statut", "indetermine") as DecisionFields["statut"],
    origine: str(data, "origine", "auteur") as DecisionFields["origine"],
    justification: str(data, "justification"),
  });
  revalidatePath("/decisions");
  revalidatePath("/");
}

export async function updateDecision(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db
    .update(decisions)
    .set({
      intitule: str(data, "intitule", "Sans intitulé"),
      axe: str(data, "axe", "Non classé"),
      contenu: str(data, "contenu"),
      statut: str(data, "statut", "indetermine") as DecisionFields["statut"],
      origine: str(data, "origine", "auteur") as DecisionFields["origine"],
      justification: str(data, "justification"),
    })
    .where(eq(decisions.id, id));
  revalidatePath("/decisions");
  revalidatePath(`/decisions/${id}`);
  revalidatePath("/");
}

export async function setDecisionStatut(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db
    .update(decisions)
    .set({ statut: str(data, "statut", "indetermine") as DecisionFields["statut"] })
    .where(eq(decisions.id, id));
  revalidatePath("/decisions");
  revalidatePath(`/decisions/${id}`);
  revalidatePath("/");
}

export async function deleteDecision(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(decisions).where(eq(decisions.id, id));
  revalidatePath("/decisions");
  revalidatePath("/");
}

/* ----------------------------------------------------------- confrontations */

export async function createConfrontation(data: FormData) {
  const decisionId = num(data, "decisionId");
  // Le select unique encode "type:id" pour éviter un select en cascade côté client.
  const ref = str(data, "ref");
  const [refTypeBrut, refIdBrut] = ref.includes(":") ? ref.split(":") : ["", ""];
  const refType = refTypeBrut || str(data, "refType");
  const refId = Number.parseInt(refIdBrut, 10) || num(data, "refId");
  if (!decisionId || !refId || !refType) return;
  await db.insert(confrontations).values({
    decisionId,
    refType,
    refId,
    relation: str(
      data,
      "relation",
      "non_evalue",
    ) as typeof confrontations.$inferInsert.relation,
    note: str(data, "note"),
  });
  revalidatePath(`/decisions/${decisionId}`);
  revalidatePath("/");
}

export async function updateConfrontation(data: FormData) {
  const id = num(data, "id");
  const decisionId = num(data, "decisionId");
  if (!id) return;
  await db
    .update(confrontations)
    .set({
      relation: str(
        data,
        "relation",
        "non_evalue",
      ) as typeof confrontations.$inferInsert.relation,
      note: str(data, "note"),
    })
    .where(eq(confrontations.id, id));
  revalidatePath(`/decisions/${decisionId}`);
  revalidatePath("/");
}

export async function deleteConfrontation(data: FormData) {
  const id = num(data, "id");
  const decisionId = num(data, "decisionId");
  if (!id) return;
  await db.delete(confrontations).where(eq(confrontations.id, id));
  revalidatePath(`/decisions/${decisionId}`);
  revalidatePath("/");
}

/* -------------------------------------------------------------- ambiguïtés */

type AmbiguiteFields = typeof ambiguites.$inferInsert;

export async function createAmbiguite(data: FormData) {
  const projetId = num(data, "projetId");
  const question = str(data, "question");
  if (!projetId || !question) return;
  await db.insert(ambiguites).values({
    projetId,
    question,
    enjeu: str(data, "enjeu"),
    consequences: str(data, "consequences"),
    statut: str(data, "statut", "ouverte") as AmbiguiteFields["statut"],
    arbitrage: str(data, "arbitrage"),
  });
  revalidatePath("/ambiguites");
  revalidatePath("/");
}

export async function updateAmbiguite(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db
    .update(ambiguites)
    .set({
      question: str(data, "question", "Question non formulée"),
      enjeu: str(data, "enjeu"),
      consequences: str(data, "consequences"),
      statut: str(data, "statut", "ouverte") as AmbiguiteFields["statut"],
      arbitrage: str(data, "arbitrage"),
    })
    .where(eq(ambiguites.id, id));
  revalidatePath("/ambiguites");
  revalidatePath("/");
}

export async function deleteAmbiguite(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(ambiguites).where(eq(ambiguites.id, id));
  revalidatePath("/ambiguites");
  revalidatePath("/");
}

/* ------------------------------------------------------------- inspirations */

type InspirationFields = typeof inspirations.$inferInsert;

function inspirationFromForm(data: FormData): InspirationFields {
  return {
    nom: str(data, "nom", "Sans nom"),
    categorie: str(data, "categorie", "Autre"),
    statut: str(data, "statut", "reference") as InspirationFields["statut"],
    ceQueVousEnDites: str(data, "ceQueVousEnDites"),
    piegesInterpretation: str(data, "piegesInterpretation"),
    resteOuvert: str(data, "resteOuvert"),
    medium: str(data, "medium"),
    economie: str(data, "economie"),
  };
}

export async function upsertInspiration(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db
      .update(inspirations)
      .set(inspirationFromForm(data))
      .where(eq(inspirations.id, id));
  } else {
    await db.insert(inspirations).values(inspirationFromForm(data));
  }
  revalidatePath("/inspirations");
  revalidatePath("/");
}

export async function setInspirationStatut(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db
    .update(inspirations)
    .set({
      statut: str(data, "statut", "reference") as InspirationFields["statut"],
    })
    .where(eq(inspirations.id, id));
  revalidatePath("/inspirations");
  revalidatePath("/");
}

export async function deleteInspiration(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(inspirations).where(eq(inspirations.id, id));
  revalidatePath("/inspirations");
  revalidatePath("/");
}

/* ------------------------------------------------------------ vérifications */

type VerifFields = typeof verifications.$inferInsert;

function verifFromForm(data: FormData): VerifFields {
  return {
    affirmation: str(data, "affirmation", "Affirmation non formulée"),
    nature: str(data, "nature", "interpretation") as VerifFields["nature"],
    statut: str(data, "statut", "a_verifier") as VerifFields["statut"],
    constat: str(data, "constat"),
    source: str(data, "source"),
  };
}

export async function upsertVerification(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(verifications).set(verifFromForm(data)).where(eq(verifications.id, id));
  } else {
    await db.insert(verifications).values(verifFromForm(data));
  }
  revalidatePath("/verifications");
  revalidatePath("/");
}

export async function deleteVerification(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(verifications).where(eq(verifications.id, id));
  revalidatePath("/verifications");
  revalidatePath("/");
}

/* ---------------------------------------------------------------- documents */

type DocumentFields = typeof documents.$inferInsert;

function documentFromForm(data: FormData): DocumentFields {
  return {
    titre: str(data, "titre", "Sans titre"),
    url: str(data, "url"),
    nature: str(data, "nature"),
    etabli: str(data, "etabli"),
    nonEtabli: str(data, "nonEtabli"),
  };
}

export async function upsertDocument(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(documents).set(documentFromForm(data)).where(eq(documents.id, id));
  } else {
    await db.insert(documents).values(documentFromForm(data));
  }
  revalidatePath("/documents");
  revalidatePath("/");
}

export async function deleteDocument(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(documents).where(eq(documents.id, id));
  revalidatePath("/documents");
  revalidatePath("/");
}

/* --------------------------------------------------------------- mécaniques */

type MecaniqueFields = typeof mecaniques.$inferInsert;

function mecaniqueFromForm(data: FormData): MecaniqueFields {
  return {
    nom: str(data, "nom", "Sans nom"),
    domaine: str(data, "domaine"),
    exemplifiePar: str(data, "exemplifiePar"),
    question: str(data, "question"),
    transposition: str(data, "transposition"),
    statut: str(data, "statut", "a_verifier") as MecaniqueFields["statut"],
  };
}

export async function upsertMecanique(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(mecaniques).set(mecaniqueFromForm(data)).where(eq(mecaniques.id, id));
  } else {
    await db.insert(mecaniques).values(mecaniqueFromForm(data));
  }
  revalidatePath("/mecaniques");
  revalidatePath("/");
}

export async function deleteMecanique(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(mecaniques).where(eq(mecaniques.id, id));
  revalidatePath("/mecaniques");
  revalidatePath("/");
}

/* ----------------------------------------------------------------- constats */

type ConstatFields = typeof constats.$inferInsert;

function constatFromForm(data: FormData): ConstatFields {
  return {
    titre: str(data, "titre", "Sans titre"),
    corpus: str(data, "corpus"),
    mesure: str(data, "mesure"),
    lecture: str(data, "lecture"),
    limites: str(data, "limites"),
    contreEpreuve: str(data, "contreEpreuve"),
  };
}

export async function upsertConstat(data: FormData) {
  const id = num(data, "id");
  if (id) {
    await db.update(constats).set(constatFromForm(data)).where(eq(constats.id, id));
  } else {
    await db.insert(constats).values(constatFromForm(data));
  }
  revalidatePath("/constats");
}

export async function deleteConstat(data: FormData) {
  const id = num(data, "id");
  if (!id) return;
  await db.delete(constats).where(eq(constats.id, id));
  revalidatePath("/constats");
}
