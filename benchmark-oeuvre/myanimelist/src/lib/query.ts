/**
 * Analyseur de requête par tags, inspiré de Danbooru.
 *
 * Syntaxe acceptée :
 *   fantasy action          → fantasy ET action
 *   fantasy|supernatural    → fantasy OU supernatural
 *   (fantasy ou magie) action → groupe OU, puis ET
 *   -comedy                 → exclusion
 *   "school life"           → tag contenant un espace
 *   school_life             → idem, souligné = espace
 *
 * Séparateurs OU reconnus : `|`, `ou`, `or`, `,`
 * Insensible à la casse et aux accents.
 */

export type Dico = Map<string, { type: string; nom: string }>;

export type Resolution = {
  genreGroupes: { noms: string[]; mode: "and" | "or" }[];
  themeGroupes: { noms: string[]; mode: "and" | "or" }[];
  magazines: string[];
  genresExcl: string[];
  themesExcl: string[];
  magazinesExcl: string[];
  inconnus: string[];
};

const sansAccent = (s: string) =>
  s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();

export function construireDico(
  familles: { type: string; tags: { nom: string }[] }[],
): Dico {
  const d: Dico = new Map();
  for (const { type, tags } of familles) {
    for (const t of tags) {
      d.set(sansAccent(t.nom), { type, nom: t.nom });
      // Variante avec soulignés, comme sur Danbooru
      d.set(sansAccent(t.nom).replace(/\s+/g, "_"), { type, nom: t.nom });
    }
  }
  return d;
}

/** Découpe en jetons de premier niveau, en respectant parenthèses et guillemets. */
function jetons(q: string): string[] {
  const out: string[] = [];
  let buf = "";
  let prof = 0;
  let guillemet = false;
  for (const ch of q) {
    if (ch === '"') {
      guillemet = !guillemet;
      buf += ch;
      continue;
    }
    if (!guillemet && ch === "(") {
      prof++;
      buf += ch;
      continue;
    }
    if (!guillemet && ch === ")") {
      prof = Math.max(0, prof - 1);
      buf += ch;
      continue;
    }
    if (!guillemet && prof === 0 && /\s/.test(ch)) {
      if (buf.trim()) out.push(buf.trim());
      buf = "";
      continue;
    }
    buf += ch;
  }
  if (buf.trim()) out.push(buf.trim());

  // Fusionne « a ou b » en « a|b » : un OU écrit en toutes lettres relie
  // les deux jetons qui l'encadrent.
  const fusionne: string[] = [];
  for (const jeton of out) {
    if (/^(?:ou|or)$/i.test(jeton) && fusionne.length > 0) {
      fusionne[fusionne.length - 1] += "|";
      continue;
    }
    const dernier = fusionne[fusionne.length - 1];
    if (dernier !== undefined && dernier.endsWith("|")) {
      fusionne[fusionne.length - 1] = dernier + jeton;
      continue;
    }
    fusionne.push(jeton);
  }
  return fusionne.map((j) => j.replace(/\|$/, "")).filter(Boolean);
}

/** Sépare un jeton en alternatives (OU). */
function alternatives(jeton: string): string[] {
  const nu = jeton.replace(/^\(|\)$/g, "");
  return nu
    .split(/\s*(?:\||,)\s*|\s+(?:ou|or)\s+/i)
    .map((s) => s.trim())
    .filter(Boolean);
}

const nettoie = (s: string) => s.replace(/^["']|["']$/g, "").trim();

export function analyser(requete: string, dico: Dico): Resolution {
  const r: Resolution = {
    genreGroupes: [],
    themeGroupes: [],
    magazines: [],
    genresExcl: [],
    themesExcl: [],
    magazinesExcl: [],
    inconnus: [],
  };
  if (!requete.trim()) return r;

  for (const jeton of jetons(requete)) {
    const negatif = jeton.startsWith("-");
    const corps = negatif ? jeton.slice(1) : jeton;
    const parts = alternatives(corps);

    // Regroupe les tags résolus par famille
    const parType = new Map<string, string[]>();
    for (const p of parts) {
      const clef = sansAccent(nettoie(p));
      const trouve = dico.get(clef) ?? dico.get(clef.replace(/_/g, " "));
      if (!trouve) {
        if (nettoie(p)) r.inconnus.push(nettoie(p));
        continue;
      }
      const liste = parType.get(trouve.type) ?? [];
      if (!liste.includes(trouve.nom)) liste.push(trouve.nom);
      parType.set(trouve.type, liste);
    }

    for (const [type, noms] of parType) {
      if (noms.length === 0) continue;
      if (negatif) {
        if (type === "genre") r.genresExcl.push(...noms);
        else if (type === "theme") r.themesExcl.push(...noms);
        else if (type === "magazine") r.magazinesExcl.push(...noms);
        continue;
      }
      // Un jeton = un groupe. Plusieurs alternatives = mode OU.
      const groupe = { noms, mode: "or" as const };
      if (type === "genre") r.genreGroupes.push(groupe);
      else if (type === "theme") r.themeGroupes.push(groupe);
      else if (type === "magazine") r.magazines.push(...noms);
    }
  }
  return r;
}

/** Reconstitue une requête texte à partir de filtres déjà posés. */
export function versTexte(res: {
  genreGroupes: { noms: string[]; mode: string }[];
  themeGroupes: { noms: string[]; mode: string }[];
  magazines: string[];
  genresExcl: string[];
  themesExcl: string[];
  magazinesExcl: string[];
}): string {
  const bloc = (g: { noms: string[]; mode: string }) => {
    if (g.noms.length === 0) return "";
    const items = g.noms.map((n) => (n.includes(" ") ? `"${n}"` : n));
    if (items.length === 1) return items[0];
    return g.mode === "and" ? items.join(" ") : `(${items.join("|")})`;
  };
  const morceaux = [
    ...res.genreGroupes.map(bloc),
    ...res.themeGroupes.map(bloc),
    ...res.magazines.map((m) => (m.includes(" ") ? `"${m}"` : m)),
    ...[...res.genresExcl, ...res.themesExcl, ...res.magazinesExcl].map((n) =>
      n.includes(" ") ? `-"${n}"` : `-${n}`,
    ),
  ].filter(Boolean);
  return morceaux.join(" ");
}
