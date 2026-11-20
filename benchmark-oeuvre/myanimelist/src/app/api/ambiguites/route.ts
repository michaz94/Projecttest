import { eq } from "drizzle-orm";

import { db } from "@/db";
import { ambiguites } from "@/db/schema";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const projetParam = Number.parseInt(url.searchParams.get("projet") ?? "", 10);

  const base = db.select().from(ambiguites);
  const rows = projetParam
    ? await base.where(eq(ambiguites.projetId, projetParam)).orderBy(ambiguites.id)
    : await base.orderBy(ambiguites.id);

  return Response.json({
    data: rows,
    meta: {
      ouvertes: rows.filter((a) => a.statut === "ouverte").length,
      avertissement:
        "Une ambiguïté ouverte ne doit pas être présentée comme résolue dans un client.",
    },
  });
}
