/**
 * Code couleur des scores MAL, tel que demandé :
 *
 *   9 et plus     bleu foncé
 *   8 à 8,99      bleu clair
 *   7 à 7,99      vert
 *   6,50 à 6,99   jaune
 *   6,00 à 6,49   orange
 *   0 à 5,99      rouge
 *
 * Les couleurs sont FIXES (identiques en thème clair et sombre) et le chiffre
 * est toujours affiché dans la tuile : la couleur ne porte jamais seule
 * l'information (daltonisme).
 *
 * Contrastes mesurés du chiffre sur sa tuile : de 5,1:1 à 12,1:1.
 */
export type Palier = {
  id: string;
  libelle: string;
  fond: string;
  texte: string;
  /** Liseré : rend visible une tuile proche du fond de la carte. */
  bord: string;
};

export const PALIERS: Palier[] = [
  { id: "bleu-fonce", libelle: "9 et plus", fond: "#1f43a8", texte: "#ffffff", bord: "#6f8fe0" },
  { id: "bleu-clair", libelle: "8 – 8,99", fond: "#8fcbf5", texte: "#14110e", bord: "#8fcbf5" },
  { id: "vert", libelle: "7 – 7,99", fond: "#52b97d", texte: "#14110e", bord: "#52b97d" },
  { id: "jaune", libelle: "6,50 – 6,99", fond: "#f1cd45", texte: "#14110e", bord: "#f1cd45" },
  { id: "orange", libelle: "6 – 6,49", fond: "#f08a35", texte: "#14110e", bord: "#f08a35" },
  { id: "rouge", libelle: "moins de 6", fond: "#c9382e", texte: "#ffffff", bord: "#e0766d" },
];

const NEUTRE: Palier = {
  id: "inconnu",
  libelle: "sans score",
  fond: "transparent",
  texte: "inherit",
  bord: "currentColor",
};

/** Paliers évalués du plus haut au plus bas. Les scores MAL ont deux décimales. */
export function palierScore(score: number | null | undefined): Palier {
  if (score === null || score === undefined || Number.isNaN(score)) return NEUTRE;
  if (score >= 9) return PALIERS[0];
  if (score >= 8) return PALIERS[1];
  if (score >= 7) return PALIERS[2];
  if (score >= 6.5) return PALIERS[3];
  if (score >= 6) return PALIERS[4];
  return PALIERS[5];
}

export function styleScore(score: number | null | undefined) {
  const p = palierScore(score);
  return { backgroundColor: p.fond, color: p.texte, borderColor: p.bord };
}
