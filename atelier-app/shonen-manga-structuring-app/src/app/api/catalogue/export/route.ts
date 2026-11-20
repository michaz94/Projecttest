import { sql } from "drizzle-orm";

import { db } from "@/db";

export const dynamic = "force-dynamic";

type Row = {
  mal_id: number;
  titre: string;
  score: number | null;
  volumes: number | null;
  chapitres: number | null;
  annee_debut: number | null;
  annee_fin: number | null;
  statut: string;
  members: number | null;
  scored_by: number | null;
  genres: string | null;
  themes: string | null;
  magazines: string | null;
  auteurs: string | null;
};

function csv(v: unknown): string {
  const s = v === null || v === undefined ? "" : String(v);
  return /[",;\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

export async function GET() {
  const r = await db.execute<Row>(sql`
    select o.mal_id, o.titre, o.score, o.volumes, o.chapitres,
           o.annee_debut, o.annee_fin, o.statut, o.members, o.scored_by,
           (select string_agg(t.nom, '|' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type='genre') as genres,
           (select string_agg(t.nom, '|' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type='theme') as themes,
           (select string_agg(t.nom, '|' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type='magazine') as magazines,
           (select string_agg(t.nom, '|' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type='auteur') as auteurs
      from oeuvres o order by o.score desc nulls last
  `);

  const cols = [
    "mal_id", "titre", "score", "volumes", "chapitres",
    "annee_debut", "annee_fin", "statut", "members", "scored_by",
    "genres", "themes", "magazines", "auteurs",
  ] as const;

  const lignes = [
    cols.join(","),
    ...r.rows.map((row) => cols.map((c) => csv(row[c])).join(",")),
  ];

  return new Response("\ufeff" + lignes.join("\n"), {
    headers: {
      "content-type": "text/csv; charset=utf-8",
      "content-disposition": 'attachment; filename="corpus-shonen-mal.csv"',
    },
  });
}
