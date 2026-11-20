import { db } from "@/db";
import { projets } from "@/db/schema";

export const dynamic = "force-dynamic";

export async function GET() {
  const rows = await db.select().from(projets).orderBy(projets.id);
  return Response.json({ data: rows });
}

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return Response.json({ error: "JSON invalide" }, { status: 400 });
  }

  const payload = body as { titre?: string; pitch?: string; notePerimetre?: string };
  if (!payload.titre || typeof payload.titre !== "string") {
    return Response.json({ error: "Champ « titre » requis" }, { status: 400 });
  }

  const [row] = await db
    .insert(projets)
    .values({
      titre: payload.titre,
      pitch: typeof payload.pitch === "string" ? payload.pitch : "",
      notePerimetre:
        typeof payload.notePerimetre === "string" ? payload.notePerimetre : "",
    })
    .returning();

  return Response.json({ data: row }, { status: 201 });
}
