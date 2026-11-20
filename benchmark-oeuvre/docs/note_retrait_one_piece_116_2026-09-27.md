# Retrait de « ONE PIECE 116 » du corpus principal — note de mise à jour

**27 septembre 2026**

## 1. Décision

Le diagnostic du 22/09/2026 sur les fichiers de percentiles avait repéré **4 tomes présents uniquement côté Goodreads** (absents de la distribution SensCritique) : Black Clover 37 et 38, Hunter × Hunter 39 et One Piece 116.

Après vérification :

- les trois premiers sont de **vrais tomes** : leurs fiches SensCritique existent, mais elles ont trop peu de notes pour afficher une moyenne ;
- **One Piece 116 n'est pas un tome relié** : c'est un chapitre de l'édition originale (Glénat, 15/06/2022), sans fiche SensCritique — la série s'arrête au tome 115 (« Ce qu'il y a de plus fort au monde »).

Décision : **retrait de l'entrée One Piece 116** du corpus, avec recalcul complet des percentiles, rangs et scores ajustés Goodreads. Les trois autres tomes sont **conservés** (aucune modification).

## 2. Entrée retirée

| Champ | Valeur |
|---|---|
| Plateforme | Goodreads |
| Série / position | One Piece, 116 |
| Titre | `ONE PIECE 116` |
| Note | **4,68 / 5** |
| Notations | 59 |
| Percentile brut (avant retrait) | 96,93 (bande P95–99) |
| Rang brut (avant retrait) | 18–20 / 603 |
| Motif | chapitre de l'édition originale, pas un tome relié ; aucune fiche SensCritique |

## 3. Fichiers mis à jour

| Fichier | Avant | Après |
|---|---:|---:|
| `percentiles_tous_corpus_principaux_2026-09-22.csv` / `.json` / `.xlsx` | 1 202 lignes (603 GR + 599 SC) | **1 201** (602 GR + 599 SC) |
| `percentiles_tous_corpus_principaux_2026-09-20.csv` / `.json` / `.xlsx` | 1 196 lignes (600 GR + 596 SC) | **1 195** (599 GR + 596 SC) |
| `percentiles_avec_nombre_votes_2026-09-22.csv` / `.json` / `.xlsx` | 1 202 lignes | **1 201** |
| `percentiles_avec_nombre_votes_2026-09-20.csv` / `.xlsx` | 1 196 lignes | **1 195** (+ feuille « Cycles » recalculée) |

Côté SensCritique : **aucun changement** (599 œuvres au 22/09, 596 au 20/09).

Notes également corrigées : `Percentiles_tous_corpus_principaux_2026-09-22.md`, `Percentiles_tous_corpus_principaux_2026-09-20.md`, `Percentiles_avec_nombre_de_votes_2026-09-22.md`, `Percentiles_avec_nombre_de_votes_2026-09-20.md` et la section 5 du rapport `Analyse_complete_Seigneur_des_anneaux_Goodreads_SensCritique_2026-09-22.md` (rangs désormais exprimés sur 602).

Chaque classeur porte désormais une ligne « **Correction 27/09/2026** » dans l'onglet Synthèse, et chaque note un encadré de correction — la traçabilité est donc lisible directement dans les livrables.

## 4. Effet chiffré du retrait

### Percentiles bruts

- Population Goodreads : 603 → **602** (fichiers du 22/09) ; 600 → **599** (fichiers du 20/09).
- 585 des 602 œuvres retenues **gagnent une place** au classement brut (toutes celles notées sous 4,68, puisque l'entrée retirée leur était supérieure) ; les deux ex æquo à 4,68 (One Piece 107 et 115) gagnent une demi-place ; les 17 œuvres notées au-dessus de 4,68 gardent exactement le même rang.
- Écart maximal de percentile : **0,16 point** (0,1596).

### Score ajusté (classement robuste)

Le score ajusté dépend de deux paramètres estimés sur le corpus : `C` (moyenne des notes) et `m` (médiane du nombre de votes). Le retrait les déplace légèrement, donc **tous les scores ajustés sont réestimés** :

| Corpus | C avant → après | m avant → après | \|Δ score\| max | Rangs ajustés modifiés |
|---|---|---|---|---:|
| 2026-09-22 | 4,40197 → **4,40151** | 5 839,0 → **5 892,5** | 0,0017 | **138 / 602 (23 %)**, \|Δ rang\| ≤ 3 |
| 2026-09-20 | 4,40147 → **4,40100** | 5 810,5 → **5 814,0** | 0,0005 | **117 / 599 (20 %)**, \|Δ rang\| ≤ 6 |

**Lecture** : le retrait déplace surtout la **médiane** du nombre de votes, et très peu la moyenne des notes. Dans un classement ajusté aussi dense que ce corpus (des milliers de notes très proches), ces micro-écarts suffisent à intervertir des voisins immédiats. C'est une propriété connue du classement robuste, pas une erreur de calcul.

Repères de contrôle : One Piece 103 reste **n°1 brut** et passe au rang ajusté **41** (fichiers 22/09) / **39** (fichiers 20/09, inchangé) ; One Piece 59 garde son rang ajusté **16** ; le Worm Goodreads passe de P89,65 à P90,57 ajusté (20/09).

### Répartition Goodreads (fichiers 22/09)

560 mangas + 29 œuvres de cycles fantasy + 12 textes arthuriens fondateurs + 1 web-serial = **602**.

## 5. Les trois autres tomes : état et décision

| Série | Tome | Fiche SensCritique | Notes SC | Notes Goodreads | Statut | Décision |
|---|---:|---|---|---|---|---|
| Black Clover | 37 | [`…/123918345`](https://www.senscritique.com/bd/black_clover_tome_37/123918345) | 4 notes (pas de moyenne affichée) | 4,24 / 295 | sorti le 25/02/2026 (France) | **conservé** |
| Black Clover | 38 | [`…/139000484`](https://www.senscritique.com/bd/black_clover_tome_38/139000484) | 1 note | 4,05 / 44 | sortie japonaise 04/08/2026, VF à venir | **conservé** |
| Hunter × Hunter | 39 | [`…/139228306`](https://www.senscritique.com/bd/hunter_x_hunter_tome_39/139228306) | 2 notes, 1 envie | 4,27 / 153 | sortie VF prévue le 04/12/2026 | **conservé** |

Chacune de ces fiches SensCritique existe donc bien, mais compte **moins de 5 notes** : aucune moyenne n'y est publiée. Ces trois tomes restent présents uniquement dans la partie Goodreads de la distribution, selon la même règle que les trois tomes manga sans moyenne SensCritique déjà absents du corpus.

## 6. Effets en cascade

- Le relevé source `work/one_piece_goodreads_2026-09-19.csv` est **laissé intact** (traçabilité) : toute régénération ultérieure du corpus doit exclure la ligne `volume = 116` de One Piece. C'est la seule source où l'entrée subsiste volontairement.
- `Recapitulatif_discussion_et_suite.md` conserve la ligne « One Piece, **116** volumes principaux : 4,488/5 sur **1 110 638** notations » (analyse One Piece antérieure, calculée chapitre inclus). Ce document n'a pas été modifié. Si on exclut le chapitre : **115 volumes**, **1 110 579** notations, moyenne toujours arrondie à **4,488** — dis-le-moi si tu veux que je propage.
- Rappel de méthode : ces percentiles sont **internes au corpus local**, et non des percentiles de plateforme.

## 7. Reproductibilité et sauvegardes

- Une sauvegarde locale des 11 fichiers **avant** correction (4 CSV, 3 JSON, 4 XLSX) a été conservée dans `work/backup_avant_retrait_op116/` au moment de l'opération — elle n'est pas destinée au commit, l'historique Git remplissant ce rôle.
- Script de correction : `work/corriger_retrait_op116.py` (retrait, recalcul complet, réécriture des CSV/JSON/XLSX, remise en forme conditionnelle). Il est inclus dans le commit et rejouable depuis un état antérieur restauré par Git.
- Contrôles passés après correction : aucune trace résiduelle de l'entrée ; 602 / 599 lignes attendues par fichier ; percentile recalculé ligne à ligne conforme à la formule du rang moyen des ex æquo ; scores ajustés conformes ; classeurs Excel synchronisés avec les CSV ; partie SensCritique inchangée.
- Variante possible : si tu préfères **figer `C` et `m`** aux valeurs d'avant le retrait (pour éviter que le classement robuste se réordonne), c'est faisable en une passe — les percentiles bruts ne seraient pas affectés.
