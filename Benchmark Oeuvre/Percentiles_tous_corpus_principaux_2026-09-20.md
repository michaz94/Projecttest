# Percentiles de tous les corpus principaux — 2026-09-20

## Définition

Population choisie : **tous les corpus locaux**, mais uniquement les œuvres principales. Chaque plateforme forme sa propre distribution ; les échelles Goodreads /5 et SensCritique /10 ne sont pas mélangées.

Le percentile est calculé au **rang moyen des ex æquo** :

`P = 100 × (nombre d’œuvres moins bien notées + 0,5 × nombre d’ex æquo) / N`

Ainsi, **P90 = note supérieure à environ 90 % du corpus local**, soit approximativement le top 10 %. Le maximum n’atteint pas exactement P100 avec cette convention, puisque chaque œuvre occupe le milieu de son propre rang.

## Populations de référence

| Plateforme | N noté | Manga | Cycles fantasy | Arthur fondateur | Worm |
|---|---:|---:|---:|---:|---:|
| Goodreads | 599 | 560 | 26 | 12 | 1 |
| SensCritique | 596 | 557 | 26 | 12 | 1 |

**Correction du 27/09/2026** — retrait de l'entrée « ONE PIECE 116 » (Goodreads) : chapitre de l'édition originale, pas un tome relié, sans fiche SensCritique. La population Goodreads passe de 600 à 599 œuvres et la répartition passe de 561 à 560 mangas ; percentiles, rangs et bandes ont été recalculés. Détail : `Note_retrait_One_Piece_116_2026-09-27.md`.


## Seuils de note correspondant aux percentiles

| Plateforme | Minimum | Q1/P25 | Médiane/P50 | Q3/P75 | P90 | P95 | P99 | Maximum |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Goodreads | 3,540 | 4,320 | 4,410 | 4,510 | 4,600 | 4,660 | 4,730 | 4,770 |
| SensCritique | 5,400 | 6,500 | 7,200 | 7,700 | 8,000 | 8,100 | 8,402 | 9,700 |

## Extrêmes

### Goodreads — cinq premiers
- ONE PIECE 103 解放の戦士 (One Piece) — 4,77, P99,92, rang 1/599
- Words of Radiance (Stormlight Archive) — 4,76, P99,75, rang 2/599
- 鋼の錬金術師 27 [Hagane no Renkinjutsushi 27] (Fullmetal Alchemist) — 4,75, P99,50, rang 3–4/599
- ONE PIECE 104 ワノ国将軍 光月モモの助 (One Piece) — 4,75, P99,50, rang 3–4/599
- One Piece, Volume 59: The Death of Portgaz D. Ace (One Piece) — 4,74, P99,17, rang 5–6/599

### SensCritique — cinq premiers
- Worm (Parahumans) — 9,70, P99,92, rang 1/596
- La Mort de Portgas D. Ace - One Piece, tome 59 (One Piece) — 8,70, P99,75, rang 2/596
- L'Ère de Barbe Blanche - One Piece, tome 58 (One Piece) — 8,60, P99,58, rang 3/596
- Le Trône de fer — Intégrale 3 (A Song of Ice and Fire) — 8,50, P99,33, rang 4–5/596
- Guerre au sommet - One Piece, tome 57 (One Piece) — 8,50, P99,33, rang 4–5/596

## Précautions

- Ces percentiles sont **internes au corpus local**, pas à l’ensemble de Goodreads ou de SensCritique.
- Chaque œuvre pèse une unité, quel que soit son nombre de notations. Le nombre de votes sert à juger la robustesse, pas à calculer le percentile.
- Goodreads affiche généralement deux décimales et SensCritique une seule : les ex æquo sont donc particulièrement nombreux sur SensCritique.
- Un percentile très élevé sur peu de votes peut être instable : *Worm* atteint par exemple le sommet SensCritique avec seulement 11 notations.
- Les 3 tomes manga sans moyenne SensCritique sont absents de la distribution SensCritique, d’où 557 mangas notés au lieu de 560 fiches.

## Livrables

- `Percentiles_tous_corpus_principaux_2026-09-20.xlsx` : classeur filtrable avec feuilles Synthèse, Goodreads et SensCritique.
- `percentiles_tous_corpus_principaux_2026-09-20.csv` : les 1 195 lignes exploitables.
- `percentiles_tous_corpus_principaux_2026-09-20.json` : données, méthode et statistiques structurées.

Le classeur contient pour chaque tome/livre : note, nombre de notations, percentile, bande percentile, rang décroissant moyen, plage de rangs des ex æquo et proportion strictement mieux notée.