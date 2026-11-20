import { and, eq, type SQL } from "drizzle-orm";

import { db } from "@/db";
import { confrontations, decisions } from "@/db/schema";
import { STATUTS_DECISION, type StatutDecision } from "@/lib/labels";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const projetParam = Number.parseInt(url.searchParams.get("projet") ?? "", 10);
  const statutParam = url.searchParams.get("statut");

  const filtres: SQL[] = [];
  if (projetParam) filtres.push(eq(decisions.projetId, projetParam));
  if (statutParam && STATUTS_DECISION.includes(statutParam as StatutDecision)) {
    filtres.push(eq(decisions.statut, statutParam as StatutDecision));
  }

  const base = db.select().from(decisions);
  const rows = filtres.length
    ? await base.where(and(...filtres)).orderBy(decisions.id)
    : await base.orderBy(decisions.id);

  const liens = await db.select().from(confrontations);

  return Response.json({
    data: rows.map((d) => ({
      ...d,
      confrontations: liens.filter((l) => l.decisionId === d.id),
    })),
    meta: {
      avertissement:
        "Le statut fait foi. Une décision « proposition » n'a pas été adoptée par l'auteur.",
      repartition: Object.fromEntries(
        STATUTS_DECISION.map((s) => [s, rows.filter((d) => d.statut === s).length]),
      ),
    },
  });
}

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return Response.json({ error: "JSON invalide" }, { status: 400 });
  }

  const p = body as {
    projetId?: number;
    intitule?: string;
    axe?: string;
    contenu?: string;
    statut?: string;
    justification?: string;
  };

  if (!p.projetId || !p.intitule) {
    return Response.json(
      { error: "Champs « projetId » et « intitule » requis" },
      { status: 400 },
    );
  }

  const statut: StatutDecision = STATUTS_DECISION.includes(p.statut as StatutDecision)
    ? (p.statut as StatutDecision)
    : "indetermine";

  const [row] = await db
    .insert(decisions)
    .values({
      projetId: p.projetId,
      intitule: p.intitule,
      axe: p.axe ?? "Non classé",
      contenu: p.contenu ?? "",
      statut,
      // Une écriture via l'API ne peut pas se déclarer « choisie par l'auteur ».
      origine: "outil",
      justification: p.justification ?? "",
    })
    .returning();

  return Response.json({ data: row }, { status: 201 });
}
