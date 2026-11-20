/**
 * Recherche d'œuvres par nom, tolérante.
 *
 * Module volontairement PUR (aucun import) : il se teste seul et ne dépend
 * ni de la base, ni d'une extension Postgres.
 *
 * Ce qui est toléré :
 *   - majuscules, accents, ponctuation (« Frieren: Beyond… » = « frieren beyond »)
 *   - espaces manquants ou en trop (« dragonball » = « Dragon Ball »)
 *   - début de mot (« nar » trouve « Naruto »)
 *   - fautes de frappe, proportionnelles à la longueur du mot
 *   - variantes de romanisation du japonais : voyelles longues (« shonen » =
 *     « Shounen », « yuki » = « Yuuki »). C'est une heuristique : elle rapproche
 *     aussi deux mots qui n'ont rien à voir, d'où le tri par pertinence.
 *   - les petites particules (no, wa, ga, to…) ne comptent pas quand la
 *     requête contient d'autres mots.
 */

const sansAccent = (s: string) => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

/** Minuscules, sans accents, lettres et chiffres séparés par un seul espace. */
export function normaliser(s: string): string {
  return sansAccent(s)
    .toLowerCase()
    .replace(/&/g, " and ")
    .replace(/[^a-z0-9]+/g, " ")
    .trim()
    .replace(/\s+/g, " ");
}

/** Rapproche les romanisations : « ou » devient « o », les voyelles doublées se réduisent. */
export function phonetique(normalise: string): string {
  return normalise.replace(/ou/g, "o").replace(/([aeiou])\1+/g, "$1");
}

const PARTICULES = new Set(["no", "wa", "ga", "to", "ni", "de", "na", "wo", "o", "the", "of", "a", "and"]);

function trigrammes(s: string): Set<string> {
  const p = `  ${s} `;
  const out = new Set<string>();
  for (let i = 0; i < p.length - 2; i++) out.add(p.slice(i, i + 3));
  return out;
}

/** Coefficient de Dice entre deux ensembles de trigrammes, de 0 à 1. */
function dice(a: Set<string>, b: Set<string>): number {
  if (a.size === 0 || b.size === 0) return 0;
  let commun = 0;
  for (const x of a) if (b.has(x)) commun++;
  return (2 * commun) / (a.size + b.size);
}

/** Distance de Levenshtein, abandonnée dès qu'elle dépasse `max`. */
function levenshtein(a: string, b: string, max: number): number {
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prec = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) {
    const cour = [i];
    let mini = i;
    for (let j = 1; j <= b.length; j++) {
      const cout = a[i - 1] === b[j - 1] ? 0 : 1;
      const v = Math.min(prec[j] + 1, cour[j - 1] + 1, prec[j - 1] + cout);
      cour.push(v);
      if (v < mini) mini = v;
    }
    if (mini > max) return max + 1;
    prec = cour;
  }
  return prec[b.length];
}

/** Nombre de fautes admises pour un mot de cette longueur. */
/**
 * Pas de faute admise sous 6 lettres : « saiki » et « shiki » sont deux mots.
 * Réglage mesuré : à 2 fautes sur 6 lettres, « bleach » rapprochait « black ».
 */
const tolerance = (n: number) => (n <= 5 ? 0 : n <= 8 ? 1 : n <= 11 ? 2 : 3);

export type Requete = {
  brute: string;
  phrase: string;
  condensee: string;
  mots: string[];
  tri: Set<string>;
};

/** Prépare une requête. Renvoie null si elle est trop courte pour chercher. */
export function preparer(brute: string): Requete | null {
  const phrase = phonetique(normaliser(brute));
  if (phrase.length < 2) return null;
  const tous = phrase.split(" ");
  const utiles = tous.filter((m) => !PARTICULES.has(m));
  return {
    brute,
    phrase,
    condensee: phrase.replace(/ /g, ""),
    mots: utiles.length > 0 ? utiles : tous,
    tri: trigrammes(phrase),
  };
}

/** Score de 0 à 1 d'un titre pour une requête. 0 = aucune correspondance. */
export function scoreTitre(q: Requete, titre: string): number {
  const t = phonetique(normaliser(titre));
  if (!t) return 0;
  const condense = t.replace(/ /g, "");

  // 1. Correspondances de la phrase entière
  if (t === q.phrase) return 1;
  if (condense === q.condensee) return 0.97;
  if (t.startsWith(`${q.phrase} `)) return 0.95; // commence par la requête, mot entier
  if (` ${t} `.includes(` ${q.phrase} `)) return 0.92; // la contient, mots entiers
  // Début de mot seulement (« ippo » dans « ippon ») : après les mots entiers.
  if (q.phrase.length >= 3 && t.startsWith(q.phrase)) return 0.88;
  if (q.phrase.length >= 3 && t.includes(q.phrase)) return 0.85;
  // Mots recollés (« dragonball » dans « dragon ball z »). Score bas : « naruto »
  // se retrouve aussi dans « Naru to », qui est un autre titre.
  if (q.condensee.length >= 5 && condense.includes(q.condensee)) return 0.6;

  // 2. Mot par mot, avec tolérance aux fautes.
  //    Un mot du titre ne peut servir qu'une fois : « hunter hunter » ne doit
  //    pas trouver un titre qui ne contient qu'un seul « hunter ».
  const motsTitre = t.split(" ");
  const pris = new Array<boolean>(motsTitre.length).fill(false);
  let somme = 0;
  for (const m of q.mots) {
    let meilleur = 0;
    let indice = -1;
    for (let k = 0; k < motsTitre.length; k++) {
      if (pris[k]) continue;
      const w = motsTitre[k];
      let s = 0;
      if (w === m) s = 1;
      else if (m.length >= 2 && w.startsWith(m)) s = 0.9;
      else {
        const tol = tolerance(m.length);
        if (tol > 0 && Math.abs(w.length - m.length) <= tol) {
          const d = levenshtein(m, w, tol);
          if (d <= tol) s = 0.85 - 0.12 * d;
        }
      }
      if (s > meilleur) {
        meilleur = s;
        indice = k;
      }
    }
    if (indice >= 0) pris[indice] = true;
    somme += meilleur;
  }
  const couverture = somme / q.mots.length;
  const parMots = couverture * 0.9;

  // 3. Ressemblance globale des lettres (espaces mal placés, fautes multiples)
  const parLettres = dice(q.tri, trigrammes(t)) * 0.8;

  return Math.max(parMots, parLettres);
}

export type Candidat = {
  id: number;
  titres: string[];
  /** Sert à départager deux œuvres de même score : la plus connue d'abord. */
  poids: number;
};

export type Resultat = { id: number; score: number };

const SEUIL = 0.42;

/** Classe les candidats pour une requête, du plus pertinent au moins pertinent. */
export function classer(brute: string, candidats: Candidat[], limite = 500): Resultat[] | null {
  const q = preparer(brute);
  if (!q) return null;
  const sortie: (Resultat & { poids: number })[] = [];
  for (const c of candidats) {
    let meilleur = 0;
    for (const titre of c.titres) {
      if (!titre) continue;
      const s = scoreTitre(q, titre);
      if (s > meilleur) meilleur = s;
    }
    if (meilleur >= SEUIL) sortie.push({ id: c.id, score: meilleur, poids: c.poids });
  }
  sortie.sort((a, b) => b.score - a.score || b.poids - a.poids || a.id - b.id);
  return sortie.slice(0, limite).map(({ id, score }) => ({ id, score }));
}

/** En dessous de ce score, on signale que la correspondance est approchée. */
export const SEUIL_EXACT = 0.85;
