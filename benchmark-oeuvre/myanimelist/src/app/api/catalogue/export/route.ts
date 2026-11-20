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
  titre_en: string;
  url: string;
  importe_le: Date | string;
  demographies: string | null;
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
    select o.mal_id, o.url, o.titre, o.titre_en, o.score, o.volumes, o.chapitres,
           o.annee_debut, o.annee_fin, o.statut, o.members, o.scored_by, o.importe_le,
           (select string_agg(t.nom, '|' order by t.nom) from oeuvre_tags ot
              join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type='demographic') as demographies,
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

  // Mêmes noms que l'export JSON : « notateurs » et « membres » sont deux effectifs distincts.
  const cols = [
    "mal_id", "url", "titre", "titre_en", "score", "notateurs", "membres",
    "volumes", "chapitres", "statut", "annee_debut", "annee_fin",
    "genres", "themes", "demographies", "magazines", "auteurs", "collecte",
  ] as const;

  const valeur = (row: Row, c: (typeof cols)[number]): unknown => {
    if (c === "notateurs") return row.scored_by;
    if (c === "membres") return row.members;
    if (c === "collecte") return new Date(row.importe_le).toISOString().slice(0, 10);
    return row[c as keyof Row];
  };

  const lignes = [
    cols.join(","),
    ...r.rows.map((row) => cols.map((c) => csv(valeur(row, c))).join(",")),
  ];

  return new Response("\ufeff" + lignes.join("\n"), {
    headers: {
      "content-type": "text/csv; charset=utf-8",
      "content-disposition": 'attachment; filename="corpus-shonen-mal.csv"',
    },
  });
}
