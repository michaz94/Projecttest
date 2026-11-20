import { sql } from "drizzle-orm";

import { db } from "@/db";

type LigneBrute = {
  mal_id: number;
  url: string;
  titre: string;
  titre_en: string;
  score: number | null;
  scored_by: number | null;
  members: number | null;
  volumes: number | null;
  chapitres: number | null;
  statut: string;
  annee_debut: number | null;
  annee_fin: number | null;
  importe_le: Date | string;
  genres: string[];
  themes: string[];
  demographies: string[];
  magazines: string[];
  auteurs: string[];
};

/** Sous-requête : liste triée des noms d'un type de tag, ou [] s'il n'y en a aucun. */
const tags = (type: string) =>
  sql.raw(`
  coalesce((select json_agg(t.nom order by t.nom)
              from oeuvre_tags ot join tags t on t.id = ot.tag_id
             where ot.oeuvre_id = o.mal_id and t.type = '${type}'), '[]'::json)`);

const vide = <T,>(v: T | "" | null | undefined): T | null =>
  v === "" || v === undefined ? null : (v as T | null);

/** Forme publique d'une œuvre. « notateurs » et « membres » sont deux effectifs distincts. */
function formater(o: LigneBrute) {
  return {
    mal_id: o.mal_id,
    url: o.url,
    titre: o.titre,
    titre_en: vide(o.titre_en),
    notateurs: o.scored_by,
    membres: o.members,
    score: o.score,
    volumes: o.volumes,
    chapitres: o.chapitres,
    statut: vide(o.statut),
    annee_debut: o.annee_debut,
    annee_fin: o.annee_fin,
    genres: o.genres,
    themes: o.themes,
    demographies: o.demographies,
    magazines: o.magazines,
    auteurs: o.auteurs,
    collecte: new Date(o.importe_le).toISOString().slice(0, 10),
  };
}

export type OeuvreExport = ReturnType<typeof formater>;

/**
 * Lit les œuvres dans un ordre stable : identifiant MAL croissant.
 * Sans `fenetre`, renvoie tout le catalogue.
 */
export async function lireOeuvres(
  fenetre?: { limit: number; offset: number },
): Promise<OeuvreExport[]> {
  const borne = fenetre
    ? sql`limit ${fenetre.limit} offset ${fenetre.offset}`
    : sql``;

  const r = await db.execute<LigneBrute>(sql`
    select o.mal_id, o.url, o.titre, o.titre_en, o.score, o.scored_by, o.members,
           o.volumes, o.chapitres, o.statut, o.annee_debut, o.annee_fin, o.importe_le,
           ${tags("genre")}       as genres,
           ${tags("theme")}       as themes,
           ${tags("demographic")} as demographies,
           ${tags("magazine")}    as magazines,
           ${tags("auteur")}      as auteurs
      from oeuvres o
     order by o.mal_id asc
     ${borne}
  `);
  return r.rows.map(formater);
}

/**
 * Identité du jeu de données : « date de la dernière collecte . empreinte ».
 *
 * L'empreinte est calculée sur le CONTENU (champs des œuvres et relations de
 * tags). Elle change dès qu'une valeur change, même sans nouvelle collecte :
 * deux lectures portant la même version lisent exactement les mêmes données.
 */
export async function lireVersion(): Promise<{
  version: string;
  total: number;
  collecte: string;
}> {
  const r = await db.execute<{ jour: string; empreinte: string; total: number }>(sql`
    select to_char(max(o.importe_le), 'YYYY-MM-DD') as jour,
           left(md5(
             coalesce(string_agg(concat_ws('|', o.mal_id, o.titre, o.titre_en, o.score,
               o.scored_by, o.members, o.volumes, o.chapitres, o.statut,
               o.annee_debut, o.annee_fin), ';' order by o.mal_id), '')
             || '#' ||
             coalesce((select string_agg(ot.oeuvre_id || ':' || ot.tag_id, ','
                         order by ot.oeuvre_id, ot.tag_id) from oeuvre_tags ot), '')
           ), 8) as empreinte,
           count(*)::int as total
      from oeuvres o
  `);
  const l = r.rows[0];
  return {
    version: `${l?.jour ?? "inconnue"}.${l?.empreinte ?? "00000000"}`,
    total: l?.total ?? 0,
    collecte: l?.jour ?? "inconnue",
  };
}

const HOTES_LOCAUX = /^(localhost|127\.|0\.0\.0\.0|10\.|192\.168\.|169\.254\.|172\.(1[6-9]|2\d|3[01])\.|\[::1\])/;

/**
 * Adresse publique de la requête.
 *
 * Derrière le proxy de l'aperçu, le serveur reçoit la requête en http même si
 * le visiteur est arrivé en https, et l'en-tête x-forwarded-proto n'est pas
 * fiable : un lien « next » en http:// ne se suit pas depuis l'extérieur.
 * Règle : une adresse locale reste en http ; tout autre hôte est servi en https.
 * La variable PUBLIC_BASE_URL, si elle est définie, l'emporte sur tout.
 */
export function origine(request: Request): string {
  const fixe = process.env.PUBLIC_BASE_URL?.trim();
  if (fixe) return fixe.replace(/\/+$/, "");

  const h = request.headers;
  const host = (h.get("x-forwarded-host") ?? h.get("host") ?? "").split(",")[0].trim();
  if (HOTES_LOCAUX.test(host)) {
    const proto = (
      h.get("x-forwarded-proto") ?? new URL(request.url).protocol.replace(":", "")
    )
      .split(",")[0]
      .trim();
    return `${proto}://${host}`;
  }
  return `https://${host}`;
}

export const NOTES_EFFECTIFS = {
  notateurs:
    "Personnes ayant noté l'œuvre : l'effectif derrière le score. Ne pas confondre avec membres.",
  membres:
    "Personnes ayant l'œuvre dans leur liste MAL, tous statuts confondus. Indicateur de notoriété : ni vente, ni lecture, ni rétention.",
  statut:
    "Déduit de la ligne « Published » (date de fin présente : terminé ; sinon : en cours). Ce n'est pas le champ Status de MAL.",
};
