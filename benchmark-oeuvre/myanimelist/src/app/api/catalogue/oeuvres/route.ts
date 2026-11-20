import {
  lireOeuvres,
  lireVersion,
  NOTES_EFFECTIFS,
  origine,
} from "@/lib/catalogue-export";

export const dynamic = "force-dynamic";

const LIMITE_DEFAUT = 5;
const LIMITE_MAX = 200;

function erreur(message: string) {
  return Response.json({ erreur: message }, { status: 400 });
}

/** Entier positif ou nul, écrit en chiffres uniquement. */
function entier(brut: string | null, defaut: number): number | null {
  if (brut === null || brut === "") return defaut;
  return /^\d+$/.test(brut) ? Number.parseInt(brut, 10) : null;
}

/**
 * Lecture paginée du catalogue.
 *
 *   GET /api/catalogue/oeuvres                      → 5 œuvres, à partir de 0
 *   GET /api/catalogue/oeuvres?limit=20&offset=40   → 20 œuvres, à partir de la 41e
 *
 * Ordre stable : identifiant MAL croissant. Le champ `next` donne l'adresse du
 * lot suivant, ou null à la fin : on parcourt tout le catalogue en le suivant.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;

  const limitDemande = entier(params.get("limit"), LIMITE_DEFAUT);
  const offset = entier(params.get("offset"), 0);
  if (limitDemande === null || offset === null) {
    return erreur(
      "limit et offset doivent être des entiers positifs ou nuls, écrits en chiffres.",
    );
  }
  if (limitDemande === 0) return erreur("limit doit valoir au moins 1.");
  const limit = Math.min(limitDemande, LIMITE_MAX);

  const [{ version, total, collecte }, oeuvres] = await Promise.all([
    lireVersion(),
    lireOeuvres({ limit, offset }),
  ]);

  const base = `${origine(request)}${new URL(request.url).pathname}`;
  const lot = (o: number) => `${base}?limit=${limit}&offset=${o}`;

  const retournes = oeuvres.length;
  const suivant = offset + retournes < total ? lot(offset + limit) : null;
  const precedent = offset > 0 ? lot(Math.max(0, offset - limit)) : null;

  const entete = {
    version,
    total,
    offset,
    limit,
    retournes,
    ordre: "mal_id croissant",
    next: suivant,
    previous: precedent,
    ...(limitDemande > LIMITE_MAX
      ? {
          avertissement: `limit demandé : ${limitDemande}. Plafonné à ${LIMITE_MAX}.`,
        }
      : {}),
    collecte,
    export_complet: `${origine(request)}/api/catalogue/json`,
    notes: NOTES_EFFECTIFS,
  };

  // Une œuvre par ligne : valide en JSON, lisible par les outils qui découpent.
  const tete = JSON.stringify(entete);
  const corps =
    `${tete.slice(0, -1)},"oeuvres":[\n` +
    oeuvres.map((o) => JSON.stringify(o)).join(",\n") +
    `\n]}\n`;

  return new Response(corps, {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}
