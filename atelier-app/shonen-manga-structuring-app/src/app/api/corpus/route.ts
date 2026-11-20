import { db } from "@/db";
import { casOeuvres, editeurs, segmentsPublics } from "@/db/schema";

export const dynamic = "force-dynamic";

/**
 * Lecture seule du corpus de recherche.
 * Le champ `fiabilite` vaut "squelette" tant que la fiche n'a pas été remplie :
 * un client mobile ne doit pas présenter une fiche squelette comme une donnée.
 */
export async function GET() {
  const [eds, cas, segs] = await Promise.all([
    db.select().from(editeurs).orderBy(editeurs.nom),
    db.select().from(casOeuvres).orderBy(casOeuvres.titre),
    db.select().from(segmentsPublics).orderBy(segmentsPublics.nom),
  ]);

  return Response.json({
    data: { editeurs: eds, cas, segments: segs },
    meta: {
      aRemplir: {
        editeurs: eds.filter((e) => e.fiabilite === "squelette").length,
        cas: cas.filter((c) => c.fiabilite === "squelette").length,
        segments: segs.filter((s) => s.fiabilite === "squelette").length,
      },
    },
  });
}
