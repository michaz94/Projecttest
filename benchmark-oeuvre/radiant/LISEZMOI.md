# Radiant (Tony Valente) : complément au dépôt

Cette archive complète `Benchmark Oeuvre/Radiant/radiant.zip` du dépôt. Elle ne contient **aucun fichier déjà présent** dans ce zip (comparaison par contenu). Pour reconstituer un dossier complet, fusionne les deux.

## rapports/
- `Analyse_critiques_recurrentes_Radiant_manga_Goodreads_et_autres_sites.md` : analyse des critiques récurrentes du manga (303 avis, Goodreads tomes 1-3 + autres sites).
- `Analyse_critiques_recurrentes_Radiant_anime_MAL.md` : idem pour l'anime S1-S2 (48 avis MAL ; phrases sur les fillers du début de S1 exclues).
- `Radiant_manga_avis_combats_et_systeme_de_pouvoir.md`, `Radiant_manga_avis_tactique_de_combat.md`, `Radiant_anime_avis_tactique_combats_et_systeme_de_pouvoir.md` : phrases d'avis sur les combats, le système de pouvoir et la tactique.

## donnees/
- `Radiant_tomes_1_3_corpus_avis_SOURCE_utilisateur.json` : ton fichier d'origine (Goodreads, Manga-News, rédaction, SensCritique, Babelio ; textes tronqués à ~500 caractères).
- `goodreads_radiant_tomes_1_3_complet.json` : 184 avis Goodreads après dédoublonnage, texte complet et pseudos.
- `critiques_manga_radiant_autres_sites_complet.json` : 119 avis hors Goodreads et hors MAL (SensCritique, Manga-News, magazines, Babelio).
- `radiant_anime_mal_saisons_1_2.json` : critiques MAL de l'anime, avec `texte_filtre` et `phrases_exclues`.

## comparaison/
Sorties de l'outil `comparer_defauts` pour Radiant contre 5 séries (Goodreads T1-T2).

## scripts/
Scripts qui ont produit les rapports (`manga_analyse/`, `anime_analyse/`) et collecté les pages (`collecte_manga/`). **Les chemins sont codés en dur (`/home/user/...`)** : à adapter avant de relancer. Les pages HTML brutes de la collecte (~11 Mo) ne sont pas incluses : elles sont reproductibles et déjà résumées par les JSON bruts du dépôt.

## Non inclus (volontairement)
- Les fichiers déjà dans le dépôt (avis bruts Goodreads, codage JSON du manga et de l'anime, extraits de fiches).
- Les CSV de codage (même contenu que les JSON du dépôt) et les versions partielles des JSON `*_complet`.
- Tout contenu au-delà du tome 6 (limite anti-spoil).
