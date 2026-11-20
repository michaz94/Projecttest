import {
  lireOeuvres,
  lireVersion,
  NOTES_EFFECTIFS,
  origine,
} from "@/lib/catalogue-export";

export const dynamic = "force-dynamic";

/**
 * Export JSON complet du catalogue.
 *
 *   GET /api/catalogue/json              → affichage direct
 *   GET /api/catalogue/json?download=1   → téléchargement du fichier
 *
 * Pour une lecture par lots, voir /api/catalogue/oeuvres (limit, offset, next).
 */
export async function GET(request: Request) {
  const telecharger = new URL(request.url).searchParams.get("download") === "1";

  const [{ version, collecte }, oeuvres] = await Promise.all([
    lireVersion(),
    lireOeuvres(),
  ]);

  const manque = (f: (o: (typeof oeuvres)[number]) => boolean) =>
    oeuvres.filter(f).length;

  const meta = {
    version,
    description:
      "Catalogue de mangas issu de MyAnimeList : type manga, démographie shōnen, début à partir de 1980, score minimum 1.",
    genere_le: new Date().toISOString(),
    collecte,
    source: "Pages publiques de myanimelist.net, collectées par scripts/import-mal.mjs",
    ordre: "mal_id croissant",
    nombre_oeuvres: oeuvres.length,
    identifiants_uniques: new Set(oeuvres.map((o) => o.mal_id)).size,
    lecture_paginee: `${origine(request)}/api/catalogue/oeuvres`,
    champs: {
      ...NOTES_EFFECTIFS,
      score: "Moyenne MAL sur 10, pondérée par MAL.",
      volumes: "Vide pour la plupart des séries en cours.",
      annee_debut:
        "Lue sur la liste de recherche, complétée depuis la ligne Published de la fiche quand la liste n'affichait que l'année.",
      genres: "Tags MAL de type genre.",
      themes: "Tags MAL de type thème.",
      demographies:
        "Dans ce catalogue, toujours « Shounen » (c'est le filtre de collecte), parfois avec une seconde démographie.",
      magazines: "Magazines de prépublication listés sur la fiche (champ Serialization).",
      collecte:
        "Date d'import de la ligne. Score, notateurs et membres évoluent chaque jour : ils sont figés à cette date.",
    },
    valeurs_manquantes: {
      sans_genre: manque((o) => o.genres.length === 0),
      sans_theme: manque((o) => o.themes.length === 0),
      sans_magazine: manque((o) => o.magazines.length === 0),
      sans_volumes: manque((o) => o.volumes === null),
      sans_chapitres: manque((o) => o.chapitres === null),
      sans_annee_debut: manque((o) => o.annee_debut === null),
      sans_annee_fin: manque((o) => o.annee_fin === null),
      sans_titre_en: manque((o) => o.titre_en === null),
      sans_score: manque((o) => o.score === null),
      sans_notateurs: manque((o) => o.notateurs === null),
      sans_membres: manque((o) => o.membres === null),
    },
    limites: [
      "Le filtre « Shounen » de MAL désigne un créneau de magazine, pas un registre narratif : le catalogue contient des comédies et des tranches de vie.",
      "Les manfras et autres séries non classées « manga » par MAL en sont absents (exemple : Radiant).",
      "Les magazines seinen d'un même éditeur (Big Gangan, Young Gangan) sont absents : ils ne sont pas classés shōnen.",
      "Un nombre de membres ou de notateurs mesure la notoriété sur une plateforme anglophone, pas les ventes.",
    ],
  };

  const corps =
    `{"meta":${JSON.stringify(meta)},\n"oeuvres":[\n` +
    oeuvres.map((o) => JSON.stringify(o)).join(",\n") +
    `\n]}\n`;

  return new Response(corps, {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      ...(telecharger
        ? {
            "content-disposition":
              'attachment; filename="catalogue_mal_shonen.json"',
          }
        : {}),
    },
  });
}
