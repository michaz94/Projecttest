# Analyse des critiques récurrentes et des 5 pôles — *Radiant* (manga, tomes 1 à 3 : Goodreads + autres sites)

**Date de l'étude** : 5 octobre 2026
**Méthode reprise de** : `Analyse_critiques_recurrentes_FMA_hors_2003.md` et `Analyse_critiques_recurrentes_HxH_hors_1999.md`, et de l'analyse de l'anime *Radiant* faite au tour précédent (même plan : périmètre → verdicts → 5 pôles → table des critiques récurrentes → détail avec citations datées et contre-voix → comparaison).
**Corpus** : **303 avis du manga** (≈ 45 397 mots), après dédoublonnage (24 avis retirés sur 327 ; voir § 0).
- **Goodreads** : 184 avis (T1 : 119, T2 : 38, T3 : 27) : **tous les avis avec texte** des trois pages du site (120 + 40 + 29 = 189 avant dédoublonnage). Source : ton fichier `Radiant_tomes_1_3_corpus_avis.json`, dont j'ai complété les textes (coupés à environ 500 caractères) et les pseudos.
- **Autres sites** : 119 avis (Babelio 53, Manga-News 46, SensCritique 16, presse 4 : Otaku USA, TheOASG, Nerdbot, Askear).
**Exclusions et dédoublonnage** : voir § 0. Aucun filtre « filler » : il ne concernait que l'anime.

---

## 0. Ce qui est identique à FMA/HxH, ce qui est différent, et ce que je n'ai pas pu reproduire

**Identique** : les 5 pôles et leurs sous-pôles (D1–D4, C, B1–B2, A1–A3, E1–E2), la table des critiques récurrentes (total, part dans les avis mitigés/négatifs, note moyenne, réactions), les citations datées avec réactions, la contre-voix, le tableau comparatif final. Les citations de ce document ont été vérifiées par script contre les textes du corpus (75/75).

**Différent** :
- **Pas d'étiquette *Recommended / Mixed / Not Recommended*.** Goodreads et les autres sites donnent seulement une note, sur des échelles différentes (`/5`, `/10`, `/20`). J'ai donc **dérivé un verdict de la note** (annexe B) : *Positif* si la note vaut au moins 75 % de l'échelle, *Mitigé* entre 41 % et 74 %, *Négatif* à 40 % ou moins, *Non noté* sans note. **Ces seuils sont mon choix**, pas une donnée du site. Deux avis de presse sans note exploitable ont reçu un verdict lu à la main (`TheOASG` : négatif ; `Otaku USA` : positif), signalés « (lu) ».
- **Goodreads : tous les avis texte, pas un échantillon de 30.** FMA/HxH étaient plafonnés à 30 avis par tome ; ici le corpus est complet pour Goodreads (T1 120 avis, T2 40, T3 29 avant dédoublonnage). **Le fichier fourni coupait 62 avis à environ 500 caractères et n'avait pas de pseudos** : j'ai rechargé chaque avis (mêmes identifiants Goodreads, tous retrouvés) pour récupérer le texte complet et l'auteur.
- **Corpus multilingue.** Goodreads mélange les langues : anglais 71, français 32, espagnol 24, ukrainien 13, indonésien 6, allemand 5, bulgare 5, 12 avis dans 10 autres langues (croate, danois, suédois, grec, etc.), et 16 avis de moins de 4 mots (une note comme « 3.5 », un emoji, « Excellent tome »). Les autres sites sont en français, sauf trois avis de presse en anglais (Otaku USA, TheOASG, Nerdbot).
- **Pôles : seulement 222 avis sur 303.** Mes listes de mots-clés couvrent l'anglais et le français ; les 81 autres avis (65 dans une autre langue, 16 de moins de 4 mots) sont **exclus des pourcentages de pôles** mais **inclus dans les verdicts et dans C1–C8**, que j'ai codés à la main après lecture (les avis de moins de 25 mots dans d'autres langues ont été lus en aperçu seulement).
- **Dédoublonnage (24 avis retirés sur 327)** : le même avis est souvent publié sur plusieurs sites ou plusieurs tomes ; je garde une seule copie (la plus longue). Retirés : 6 copies de `Sunread26` (extraits de blog repris sur SensCritique et Babelio ; la copie Goodreads est gardée), 3 copies Goodreads de `Drine Psylook` (copies Babelio, plus longues, gardées), 2 copies Babelio de `Tachan`, 1 de `Zutto`, 2 avis identiques de `Ivan Jovanovic` publiés sur les tomes 2 et 3 (gardé au T1), 2 doublons de `eques` sur Manga-News, **7 commentaires Manga-News d'annonce** (date de sortie, nombre de tomes) sans avis sur l'œuvre, et 1 avis SensCritique (`Shigeo`) qui parle de « cet anime ». Les pseudos identiques sur plusieurs sites peuvent être des homonymes ; je ne les ai pas fusionnés au-delà de ces copies exactes.
- **Anime mentionné** dans 15 avis : conservés (ils parlent du manga).

**Je n'ai pas pu reproduire / pas pu collecter** :
- Les listes de mots-clés de FMA/HxH n'ont pas été retrouvées : mes listes sont à moi (annexe A). **Les pourcentages de pôles ne sont comparables à ceux de FMA/HxH qu'en ordre de grandeur.** FMA/HxH reposaient sur des critiques MAL longues ; ici beaucoup d'avis sont des phrases isolées (voir la colonne « avis de 50 mots ou plus »).
- **Babelio est incomplet** : 59 critiques collectées sur 81 annoncées (T1 30/47, pages 4 et 5 manquantes ; T2 19/19 ; T3 10/15, page 2 manquante). Les notes globales Babelio viennent de la page (T1 3,97 sur 41 notes ; T2 4,11 sur 18 ; T3 4,25 sur 14).
- **Manga-News** : avis lecteurs collectés pour les trois tomes ; **il n'existe pas de critique de la rédaction pour le tome 3** (la page répond sans bloc de critique).
- **SensCritique** : première page de chaque liste seulement.
- **Booknode** (écarté, sur ta demande) et **Reddit r/manga** (accès refusé) : non collectés.

---

## 1. Périmètre et répartition globale

### 1.1. Structure du corpus *Radiant* (manga, `N = 303`)

| Sous-corpus | Avis (`N`) | Mots | *Positif* | *Mitigé* | *Négatif* | Non noté | Note moyenne (% de l'échelle) | Réactions cumulées | Réactions (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Goodreads T1 | 119 | 11 192 | 47 (39,5 %) | 49 (41,2 %) | 18 (15,1 %) | 5 | 66,5 % (sur 114) | 115 | 0 / 1,0 |
| Goodreads T2 | 38 | 3 933 | 23 (60,5 %) | 11 (28,9 %) | 4 (10,5 %) | 0 | 76,3 % (sur 38) | 25 | 0 / 0,7 |
| Goodreads T3 | 27 | 2 672 | 20 (74,1 %) | 6 (22,2 %) | 0 (0,0 %) | 1 | 80,8 % (sur 26) | 29 | 0 / 1,1 |
| **Goodreads (total)** | 184 | 17 797 | 90 (48,9 %) | 66 (35,9 %) | 22 (12,0 %) | 6 | 70,7 % (sur 178) | 169 | 0 / 0,9 |
| Babelio T1 | 29 | 10 535 | 20 (69,0 %) | 6 (20,7 %) | 1 (3,4 %) | 2 | 82,2 % (sur 27) | — | — |
| Babelio T2 | 16 | 2 969 | 11 (68,8 %) | 4 (25,0 %) | 0 (0,0 %) | 1 | 83,3 % (sur 15) | — | — |
| Babelio T3 | 8 | 1 663 | 5 (62,5 %) | 2 (25,0 %) | 0 (0,0 %) | 1 | 82,9 % (sur 7) | — | — |
| SensCritique T1 | 8 | 1 607 | 4 (50,0 %) | 4 (50,0 %) | 0 (0,0 %) | 0 | 76,2 % (sur 8) | 18 | 1,5 / 2,2 |
| SensCritique T2 | 1 | 315 | 0 (0,0 %) | 1 (100,0 %) | 0 (0,0 %) | 0 | 70,0 % (sur 1) | 2 | 2 / 2,0 |
| SensCritique T3 | 2 | 968 | 1 (50,0 %) | 1 (50,0 %) | 0 (0,0 %) | 0 | 80,0 % (sur 2) | 5 | 2,5 / 2,5 |
| SensCritique série (tous tomes) | 5 | 3 902 | 1 (20,0 %) | 2 (40,0 %) | 2 (40,0 %) | 0 | 54,0 % (sur 5) | 25 | 1 / 5,0 |
| Manga-News — rédaction (T1, T2) | 2 | 1 526 | 2 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | 0 | 77,5 % (sur 2) | — | — |
| Manga-News — lecteurs T1 | 27 | 1 109 | 18 (66,7 %) | 0 (0,0 %) | 0 (0,0 %) | 9 | 94,4 % (sur 18) | — | — |
| Manga-News — lecteurs T2 | 7 | 214 | 6 (85,7 %) | 0 (0,0 %) | 0 (0,0 %) | 1 | 95,0 % (sur 6) | — | — |
| Manga-News — lecteurs T3 | 10 | 343 | 5 (50,0 %) | 2 (20,0 %) | 0 (0,0 %) | 3 | 85,0 % (sur 7) | — | — |
| Presse / blogs (Otaku USA, TheOASG, Nerdbot, Askear) | 4 | 2 449 | 2 (50,0 %) | 1 (25,0 %) | 1 (25,0 %) | 0 | 73,0 % (sur 2) | — | — |
| **Autres sites (total)** | 119 | 27 600 | 75 (63,0 %) | 23 (19,3 %) | 4 (3,4 %) | 17 | 83,3 % (sur 100) | 50 | 1,5 / 3,1 |
| **TOTAL manga** | 303 | 45 397 | 165 (54,5 %) | 89 (29,4 %) | 26 (8,6 %) | 23 | 75,2 % (sur 278) | 219 | 0 / 1,1 |

Notes agrégées affichées par les sites (relevé du 5 oct. 2026) : **Goodreads** T1 **3,80** (1 058 notes), T2 **4,00** (557), T3 **4,19** (434) ; **Babelio** T1 3,97 (41 notes), T2 4,11 (18), T3 4,25 (14) ; **SensCritique** T1 7,0 / T2 7,2 / T3 7,4 / série 7,0 (sur 10) ; **Manga-News** rédaction T1 15 / T2 16 (sur 20), lecteurs T1 19 / T2 19 / T3 17 ; **Askear** 3,8/5 ; **Nerdbot** 3,5/5 ; **TheOASG** « 2 » (échelle non précisée).

**Sur Goodreads, les lecteurs qui écrivent notent moins bien que l'ensemble des lecteurs** : T1 3,34 sur 115 avis notés contre 3,80 sur 1058 notes ; T2 3,85 (40) contre 4,00 (557) ; T3 4,07 (28) contre 4,19 (434). L'écart est le plus grand au tome 1. Le corpus d'avis texte est donc un peu plus sévère que l'opinion globale (à lire avec le § 5).

Notes de méthode : (a) les « réactions » sont les *likes* Goodreads et SensCritique ; Manga-News, Babelio et la presse n'en ont pas dans mon relevé ; (b) dans Goodreads, **16 avis annoncent une note décimale** dans le texte (ex. « 3.5 ★ ») alors que le site n'accepte que des entiers : **11 des 66 avis *Mitigé* de Goodreads** (16,7 %) sont des « 3,5/5 » arrondis à 3. Le verdict ne change pas (3,5/5 = 70 % = *Mitigé* dans ma règle), mais la note Goodreads moyenne de ces avis est un peu sous-estimée ; sur Babelio, les demi-notes existent ; (c) l'avis de `Sunread26` conservé est un extrait de blog ; (d) 19 avis datent de 2013, dont 16 de Manga-News, souvent écrits **avant la sortie du tome 1** (juin 2013) ; (e) 13 commentaires Manga-News sont sans note.

### 1.2. Distribution par verdict et par période

| Verdict | Avis (`N`) | Part | Note moyenne (% échelle) | Réactions médianes | Réactions moyennes | Max réactions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| ***Positif*** | 165 | **54,5 %** | 89,1 % | 0 | 0,9 | 15 (`Roman Zarichnyi`) |
| ***Mitigé*** | 89 | **29,4 %** | 61,6 % | 0 | 1,4 | 42 (`Celestina1210`) |
| ***Négatif*** | 26 | **8,6 %** | 32,4 % | 0 | 1,0 | 20 (`Josselin-B`) |
| ***Non noté*** | 23 | **7,6 %** | — % | 0 | 0,7 | 3 (`tamazawareads`) |

| Période | Avis (`N`) | *Positif* (sur notés) | *Mitigé* | *Négatif* | dont Goodreads | Goodreads *Positif* | Goodreads *Mitigé+Négatif* |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2013–2017** | 71 | 50 (83,3 %) | 10 (16,7 %) | 0 (0,0 %) | 7 | 7 (100,0 %) | 0 (0,0 %) |
| **2018–2020** | 99 | 45 (48,4 %) | 35 (37,6 %) | 13 (14,0 %) | 67 | 27 (42,2 %) | 37 (57,8 %) |
| **2021–2026** | 132 | 69 (54,8 %) | 44 (34,9 %) | 13 (10,3 %) | 110 | 56 (52,3 %) | 51 (47,7 %) |

La baisse apparente entre 2013–2017 et 2018+ vient surtout de la **composition** : en 2013–2017, l'essentiel des avis vient de Manga-News (lecteurs enthousiastes, certains avant la sortie) ; Goodreads n'y compte que 7 avis, tous positifs. **À l'intérieur de Goodreads**, la part de positifs passe de 42,2 % en 2018–2020 (`N = 64`, marge ± 12 points) à 52,3 % en 2021–2026 (`N = 107`, ± 9) : un écart de 10 points, **dans la marge d'erreur**. Je n'en tire pas de tendance.

---

## 2. Les 5 pôles et la table des critiques récurrentes

### 2.1. Les 5 pôles (texte nettoyé, part des avis qui mentionnent le pôle ; avis en anglais et français seulement)

| Pôle | Goodreads (`N = 103`) | Autres sites (`N = 119`) | ***Radiant* manga (`N = 222`)** | dont avis de 50 mots ou plus (`N = 132`) | Rappel FMA (`N = 1 097`) | Rappel HxH (`N = 897`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Pôle D — Narration, Scénario & Histoire** | 54 (52,4 %) | 83 (69,7 %) | **137 (61,7 %)** | 106 (80,3 %) | 96,1 % | 97,9 % |
| ↳ `D1` Intrigue, écriture, twists | 42 (40,8 %) | 67 (56,3 %) | **109 (49,1 %)** | 85 (64,4 %) | 90,7 % | 88,3 % |
| ↳ `D2` Rythme, arcs, exposition | 25 (24,3 %) | 36 (30,3 %) | **61 (27,5 %)** | 53 (40,2 %) | 42,5 % | 81,4 % |
| ↳ `D3` Dramaturgie, enjeux, ton | 7 (6,8 %) | 24 (20,2 %) | **31 (14,0 %)** | 31 (23,5 %) | 50,9 % | 53,3 % |
| ↳ `D4` Climax, fin d'arc, résolution | 10 (9,7 %) | 25 (21,0 %) | **35 (15,8 %)** | 31 (23,5 %) | 36,2 % | 36,5 % |
| **Pôle C — Personnages & antagonistes** | 52 (50,5 %) | 78 (65,5 %) | **130 (58,6 %)** | 111 (84,1 %) | 61,4 % | 77,7 % |
| **Pôle B — Monde, morale & système** | 42 (40,8 %) | 70 (58,8 %) | **112 (50,5 %)** | 98 (74,2 %) | 56,2 % | 67,7 % |
| ↳ `B1` Philosophie, morale, discrimination | 13 (12,6 %) | 33 (27,7 %) | **46 (20,7 %)** | 46 (34,8 %) | 38,6 % | 23,4 % |
| ↳ `B2` Worldbuilding, magie, Inquisition | 40 (38,8 %) | 63 (52,9 %) | **103 (46,4 %)** | 89 (67,4 %) | 44,0 % | 62,0 % |
| **Pôle A — Visuel strict** | 41 (39,8 %) | 66 (55,5 %) | **107 (48,2 %)** | 84 (63,6 %) | 59,6 % | 56,4 % |
| ↳ `A1` Dessin, trait, planches, couleurs | 37 (35,9 %) | 66 (55,5 %) | **103 (46,4 %)** | 80 (60,6 %) | 57,5 % | 54,5 % |
| ↳ `A2` Effets de sorts et créatures | 2 (1,9 %) | 0 (0,0 %) | **2 (0,9 %)** | 2 (1,5 %) | 3,5 % | 2,7 % |
| ↳ `A3` Chara-design & physique | 15 (14,6 %) | 15 (12,6 %) | **30 (13,5 %)** | 28 (21,2 %) | 9,9 % | 10,8 % |
| **Pôle E — Action, chorégraphie & tactique** | 23 (22,3 %) | 44 (37,0 %) | **67 (30,2 %)** | 59 (44,7 %) | 41,0 % | 55,4 % |
| ↳ `E1` Intensité, combats | 22 (21,4 %) | 41 (34,5 %) | **63 (28,4 %)** | 55 (41,7 %) | 38,8 % | 53,7 % |
| ↳ `E2` Tactique, stratégie, créativité | 1 (1,0 %) | 4 (3,4 %) | **5 (2,3 %)** | 5 (3,8 %) | 5,6 % | 17,2 % |
| **Ratio Narration / Visuel (`D / A`)** | 1,32× | 1,26× | **1,28×** | 1,26× | 1,61× | 1,74× |
| **Ratio Visuel / Monde (`A / B`)** | 0,98× | 0,94× | **0,96×** | 0,86× | 1,06× | 0,83× |
| *Hors grille (ajout de ma part)* : Humour | 32 (31,1 %) | 66 (55,5 %) | 98 (44,1 %) | 82 (62,1 %) | non mesuré | non mesuré |

**Ce que montre le tableau** (observations ; la comparaison avec FMA/HxH est indicative, voir § 0) :
1. **La narration (`D = 61,7 %`) et les personnages (`C = 58,6 %`) sont les pôles les plus cités**, comme dans FMA et HxH. Dans le détail, l'intrigue (`D1 = 49,1 %`) est le premier sous-pôle. Les parts sont plus basses que pour FMA/HxH parce que 51 des 222 avis ont moins de 25 mots. Sur les avis de 50 mots ou plus, `D = 80,3 %` et `C = 84,1 %`.
2. **Le visuel pèse plus que dans FMA/HxH par rapport à la narration** : `D / A = 1,28×` (contre 1,61× pour FMA et 1,74× pour HxH) et `A / B = 0,96×`. Les deux sous-corpus sont proches sur ce ratio (Goodreads `1,32×`, autres sites `1,26×`), mais le dessin est plus souvent cité sur les autres sites (`A1 = 55,5 %`) que sur Goodreads (`A1 = 35,9 %`). L'art est surtout loué (voir § 3.7 et 3.9).
3. **La tactique de combat est quasi absente** (`E2 = 2,3 %`), comme dans FMA (`5,6 %`), loin de HxH (`17,2 %`). Les combats sont cités (`E1 = 28,4 %`) sans que leur logique soit discutée. **Lecture des 5 avis repérés en `E2` : 4 sont des faux positifs** (« bluffé » ×2, « cleverly » à propos d'un titre de chapitre, « pas très intelligent » à propos du héros) ; **un seul avis parle de stratégie de combat** (`Tmor`, Babelio T3). Liste détaillée : `Radiant_manga_avis_tactique_de_combat.md`.
4. **Rythme et dramaturgie sont peu cités** (`D2 = 27,5 %`, `D3 = 14,0 %`), très en dessous de HxH pour `D2` (`81,4 %`). Avec des avis courts, je ne conclus pas que le rythme ne pose pas question : voir C5.
5. **Le chara-design (`A3 = 13,5 %`)** est un peu plus cité que dans FMA (`9,9 %`) et HxH (`10,8 %`), mais bien moins que dans l'anime (`29,2 %`). Mes listes ne sont pas celles de FMA/HxH : l'écart est faible et peut être en partie artificiel.
6. **La discrimination (`B1 = 20,7 %`, 34,8 % sur les avis de 50 mots ou plus)** est du même ordre que HxH (`23,4 %`) et sous FMA (`38,6 %`).
7. **L'humour est mentionné par 44,1 % des avis** (62,1 % sur les avis de 50 mots ou plus), nettement plus sur les autres sites (55,5 %) que sur Goodreads (31,1 %). Ce pôle n'existe pas dans la grille FMA/HxH.

### 2.2. Table de codage des critiques récurrentes

*Couverture : ces 8 catégories couvrent **72 des 115** avis mitigés ou négatifs (62,6 %). Les 43 autres ne relèvent d'aucune de ces catégories : avis sans motif précis (ex. `Isak+Even` : *« That was fun! »*, `Lindsay` : *« DNF. Not interesting enough to keep my attention. »*, `Anna Wallman` : *« Too weird for me. »*, plusieurs notes seules comme « 3.5 ») ou avis surtout favorables notés 3 (ex. `Tachan` T3). Elles couvrent aussi des réserves dans **24 des 165** avis *Positif* (14,5 %). **Méthode** : j'ai lu tous les avis *Mitigé* et *Négatif* ; pour les avis *Positif*, j'ai repéré les phrases à réserve par mots-clés (« mais », « but », « however », « un peu trop », etc.) : **des réserves discrètes dans des avis positifs ont pu m'échapper**, donc ces catégories sont plutôt sous-estimées chez les *Positif*. Les catégories sont construites à partir de ces 303 textes : la couverture est en partie circulaire.*

| Rang & catégorie | Total (`N = 303`) | Goodreads / Autres | Part dans les *Mitigé / Négatif* (`N = 115`) | Note moyenne (tous, % échelle) | Note moyenne (*Mit/Nég*) | Réactions *Mit/Nég* (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1. Dérivatif / déjà-vu (Fairy Tail, Naruto, One Piece…)** | **37 (12,2 %)** | 22 / 15 | 28 / 115 (24,3 %) | 59,1 % | 52,2 % | 0 / 1,8 |
| **C2. Seth et/ou casting jugés irritants ou archétypaux** | **26 (8,6 %)** | 21 / 5 | 22 / 115 (19,1 %) | 53,8 % | 50,0 % | 0 / 1,6 |
| **C3. Surcharge de texte, exposition, planches denses ou illisibles** | **25 (8,3 %)** | 20 / 5 | 19 / 115 (16,5 %) | 62,4 % | 57,9 % | 0 / 1,5 |
| **C4. Humour lourd, répétitif, mal dosé ; ton ou public jugé jeune** | **24 (7,9 %)** | 15 / 9 | 18 / 115 (15,7 %) | 63,8 % | 57,8 % | 0 / 3,4 |
| **C5. Rythme : démarrage lent, flashbacks ou combats étirés, action qui se fait attendre** | **20 (6,6 %)** | 14 / 6 | 15 / 115 (13,0 %) | 61,1 % | 54,3 % | 0 / 1,5 |
| **C6. Logique du monde, explications absentes ou confuses ; récit brouillon** | **16 (5,3 %)** | 11 / 5 | 15 / 115 (13,0 %) | 56,0 % | 54,3 % | 0 / 2,9 |
| **C7. Dessin jugé moyen, impersonnel ou trop jeune** | **7 (2,3 %)** | 3 / 4 | 6 / 115 (5,2 %) | 46,4 % | 41,7 % | 1 / 12,8 |
| **C8. Propos sur la discrimination jugé appuyé, maladroit ou problématique** | **7 (2,3 %)** | 2 / 5 | 6 / 115 (5,2 %) | 50,0 % | 50,0 % | 2 / 7,3 |

**Répartition par tome** (nombre d'avis qui portent la réserve) :

| Tome | Avis | Positif / Mitigé / Négatif / Non noté | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| T1 | 188 | 92 / 60 / 20 / 16 | 30 | 24 | 18 | 12 | 12 | 12 | 4 | 1 |
| T2 | 63 | 41 / 16 / 4 / 2 | 3 | 1 | 6 | 8 | 3 | 1 | 1 | 2 |
| T3 | 47 | 31 / 11 / 0 / 5 | 0 | 0 | 1 | 3 | 5 | 1 | 0 | 3 |
| Série | 5 | 1 / 2 / 2 / 0 | 4 | 1 | 0 | 1 | 0 | 2 | 2 | 1 |

Lecture (observation) : **le déjà-vu (C1), Seth (C2), le texte (C3) et la logique du monde (C6) se concentrent sur le tome 1** (C1 : 30 avis sur 188 ; T2 : 3 sur 63 ; T3 : 0 sur 47 ; C2 : 24 / 1 / 0 ; C3 : 18 / 6 / 1 ; C6 : 12 / 1 / 1). **L'humour (C4) est la seule catégorie plus fréquente au tome 2 qu'au tome 1** (8 sur 63 contre 12 sur 188). **Au tome 3, il reste surtout le rythme (C5 : 5 avis), l'humour (C4 : 3) et la discrimination appuyée (C8 : 3)**, soit des réserves plus rares mais d'un autre type. Cela va avec la hausse des notes des sites (Goodreads 3,80 → 4,00 → 4,19). **Attention au biais** : le tome 1 compte 188 avis, le tome 3 47 ; les lecteurs du tome 3 ont déjà aimé les deux premiers ; ce ne sont pas les mêmes personnes qui jugent chaque tome. Les avis « série » (5) portent surtout C1 (4 sur 5).

---

## 3. Analyse détaillée des critiques récurrentes

*Citations en langue originale (français ou anglais). Format : pseudo (source et tome, verdict, date, note, réactions). Les avis dans d'autres langues sont comptés mais non cités.*

### 3.1. Critique n°1 — Dérivatif, déjà-vu (`37 (12,2 %)` du corpus ; `28 / 115 (24,3 %)` des *Mitigé/Négatif*)

* **Ce qui est reproché** : *Radiant* serait un assemblage d'ingrédients de shōnen déjà vus. Œuvres citées dans l'ensemble du corpus (réserves et éloges confondus) : *Naruto* (23 avis), *One Piece* (21), *Fairy Tail* (18), *Dragon Ball* / Toriyama (17), puis *Blue Exorcist* (5), *Bleach* (4), *Black Clover* (3), *Evangelion* (3). **Mentionner une influence n'est pas toujours un reproche** (voir contre-voix). C'est sur SensCritique que la réserve est la plus fréquente (10 avis sur 16). Répartition : T1 : 30, T2 : 3, série : 4 ; langues : français 19, anglais 11, espagnol 3, ukrainien 2, croate 1, catalan 1.
* **Citations** :
  * `Josselin-B` (SensCritique série, Négatif, 27 déc. 2020, `2/10`, 20 likes) : *« Radiant est le calque d'un calque d'un calque de Nekketsu »*
  * `alanparish` (SensCritique T1, Mitigé, 19 mai 2017, `7/10`) : *« un pot pourri de tous les nekketsu les plus populaires »*
  * `Cornerofmadness` (Goodreads T1, Mitigé, 17 janv. 2019, `3/5`, 1 like) : *« honestly I'm at my limit with screamy shonen boys »*
  * `Nick` (Goodreads T1, Mitigé, 13 janv. 2020, `3/5`, 1 like) : *« If other fantasy manga didn't already exist, this one might have felt fresh and new. »*
  * `Zutto` (Goodreads T1, Mitigé, 19 oct. 2019, `3/5`, 2 likes) : *« Seth est un peu un mix de tous les héros de shonens phares »*
  * `Ashe Catlin` (Goodreads T1, Négatif, 2 sept. 2020, `1/5`) : *« The story is completely unoriginal »*
  * `Mitchell George` (Goodreads T1, Négatif, 23 avr. 2022, `2/5`) : *« Radiant feels like a poor man's Black Clover »*
* **Contre-voix** : plusieurs avis reconnaissent la parenté et la jugent assumée ou dépassée.
  * `Kiraa7` (Manga-News T1, Positif, 30 août 2013, `15/20`) : *« il faut avouer qu'après seulement quelques pages Tony Valente nous montre clairement que son univers est unique »*
  * `Ilona` (Goodreads T1, Positif, 1 sept. 2023, `4/5`, 2 likes) : *« sans toutefois donner l'impression de les copier »*
  * `David Estrella` (Otaku USA Magazine T1, Positif (lu), 2 nov. 2018, `sans note`) : *« it never feels like Valente leans too heavily on his predecessors »*
  * `Cryver` (SensCritique T1, Positif, 14 juil. 2014, `9/10`, 3 likes) : *« tout ça sent un petit peu le réchauffé, mais c'est fait avec tellement d'amour, de talent et d'humour »*

### 3.2. Critique n°2 — Seth et/ou casting irritants ou archétypaux (`26 (8,6 %)` ; `22 / 115 (19,1 %)`)

* **Ce qui est reproché** : héros bruyant, impulsif, « bête », typique du shōnen ; casting jugé archétypal. C'est la catégorie dont les avis sont répartis sur le plus grand nombre de langues (9). Répartition : T1 : 24, T2 : 1, série : 1 ; langues : anglais 10, français 7, ukrainien 2, espagnol 2, suédois 1, croate 1, italien 1, tchèque 1, bulgare 1. Dans deux avis (croate, ukrainien), le héros agace au départ puis le jugement s'adoucit ; dans l'avis suédois, il reste agaçant.
* **Citations** :
  * `Helen` (TheOASG T1, Négatif (lu), 8 nov. 2018, `2`) : *« Main character Seth was also a major turn off for me in this first volume. »*
  * `Cornerofmadness` (Goodreads T1, Mitigé, 17 janv. 2019, `3/5`, 1 like) : *« I didn't really like Seth because of the screaming silliness »*
  * `Nick` (Goodreads T1, Mitigé, 13 janv. 2020, `3/5`, 1 like) : *« the main character is just the traditional "tough, spunky and a bit stupid" kid »*
  * `alanparish` (SensCritique T1, Mitigé, 19 mai 2017, `7/10`) : *« j'avoue avoir eu du mal à accrocher aux personnages et en particulier au duo héros/maître »*
  * `Sesana` (Goodreads T1, Négatif, 11 nov. 2019, `2/5`) : *« one of the most obnoxiously stupid protagonists I've ever seen »*
* **Contre-voix** : les avis qui commentent les personnages en bien sont plus nombreux : 81 avis *Positif* sur 120 mentionnent les personnages (mention, pas forcément louange).
  * `Kiraa7` (Manga-News T1, Positif, 30 août 2013, `15/20`) : *« ceux-ci ayant une personnalité réellement propre (on n'a pas vraiment de copier/coller avec un personnage d'un autre manga) »*
  * `Kalie (Half of Pristine Prose)` (Goodreads T2, Positif, 6 mai 2020, `5/5`) : *« The characters are so well rounded that it's only the second book and I feel like I know them and am invested in them. »*

### 3.3. Critique n°3 — Surcharge de texte, exposition, planches denses (`25 (8,3 %)` ; `19 / 115 (16,5 %)`)

* **Ce qui est reproché** : trop de texte dans les bulles, explications en dialogues (« info dump »), cases très chargées, parfois difficiles à lire (combats compris). **C'est la critique la plus partagée entre langues** : anglais 7, français 7, ukrainien 4, indonésien 3, bulgare 2, danois 1, espagnol 1 ; 11 des 25 avis ne sont ni en anglais ni en français, la part la plus élevée des huit catégories. Elle apparaît surtout aux tomes 1 et 2 (T1 : 18, T2 : 6, T3 : 1). Deux avis du tome 3 (`Tachan` et un avis ukrainien) trouvent la narration plus épurée ou plus dynamique.
* **Citations** :
  * `Selena Pigoni` (Goodreads T1, Mitigé, 23 juin 2019, `3/5`, 11 likes) : *« there were walls of word bubbles to explain a situation rather than just running with it »*
  * `Cocopanzer` (Askear T1, Positif, date non indiquée, `3,8/5`) : *« Des cases minuscules, engorgées de texte »*
  * `anonyme` (Nerdbot T1, Mitigé, 30 août 2018, `3,5/5`) : *« the laundry list and the info dump »*
  * `Tachan` (Goodreads T2, Mitigé, 4 janv. 2024, `3/5`) : *« L’auteur a une narration trop lourde pour un shonen qui a besoin de moins de texte et plus d’action pour être percutant. »*
  * `Ronron` (Manga-News T3, Non noté, 14 févr. 2018, `sans note`) : *« Indigeste, trop de blabla explicatif »*
  * `Ashley Beer` (Goodreads T1, Mitigé, 24 avr. 2026, `3/5`) : *« For a manga there were just walls of it. »*
* **Contre-voix** : d'autres jugent la lecture fluide et les combats clairs.
  * `Kiraa7` (Manga-News T1, Positif, 30 août 2013, `15/20`) : *« Le découpage se veut même très fluide, les scènes d'action se lisent facilement et jamais le lecteur se retrouve perdu dans les dessins »*
  * `Drine Psylook (Babelio : LeManegeDePsy…)` (Babelio T2, Positif, 19 sept. 2022, `5,0/5`) : *« des combats très clairs, des actions explicites »*

### 3.4. Critique n°4 — Humour lourd, répétitif, mal dosé ; ton ou public jugé jeune (`24 (7,9 %)` ; `18 / 115 (15,7 %)`)

* **Ce qui est reproché** : blagues scatologiques (« pee, poop », « pipi-caca-prout », « en dessous de la ceinture »), répétition des gags, humour « enfantin », sentiment que l'œuvre vise un public plus jeune. Plusieurs avis (espagnol, français, anglais) relèvent aussi des gags ou des remarques jugés sexistes ou ecchi. Répartition : T1 : 12, T2 : 8, T3 : 3, série : 1 ; langues : français 14, ukrainien 3, anglais 3, espagnol 2, croate 1, bulgare 1. **Cette catégorie apparaît à tous les tomes, y compris le tome 3.**
* **Citations** :
  * `Zutto` (Goodreads T2, Négatif, 17 nov. 2019, `2/5`, 2 likes) : *« The writing and the dialogue are very childish »*
  * `Tachan` (Goodreads T2, Mitigé, 4 janv. 2024, `3/5`) : *« son humour, lourd, répétitif, en-dessous de la ceinture et rare inspiré »*
  * `D.T. Henderson` (Goodreads T3, Mitigé, 8 févr. 2020, `3/5`) : *« Radiant is getting increasingly slapstick/juvenile with its humor »*
  * `Ryan Russell` (Goodreads T1, Mitigé, 10 juil. 2024, `3/5`, 1 like) : *« the story and art are a bit juvenile for my taste »*
  * `GeorgesBouche` (SensCritique série, Mitigé, 8 janv. 2019, `7/10`, 3 likes) : *« se perdent parfois en surenchère de punchlines ou de running gags, qui finissent par tomber à plat »*
  * `Alfaric` (Babelio T2, Mitigé, 29 févr. 2020, `3,5/5`) : *« les blagues pipi-caca-prout et les gags ecchi »*
  * `Kiatoulu` (Goodreads T1, Négatif, 27 oct. 2023, `1/5`) : *« l'humour du texte et les dessins et remarques sexistes font que je ne lirais pas la suite »*
  * `francois1123` (Manga-News T3, Mitigé, 9 sept. 2018, `12,0/20`) : *« la lourdeur des jeux de mots et des joutes verbales »*
* **Contre-voix** : l'humour est aussi l'un des points forts les plus cités par les avis *Positif* (60 sur 120) ; plusieurs lecteurs francophones l'associent au fait que l'œuvre est française.
  * `Bakakappa` (SensCritique T1, Mitigé, 28 févr. 2016, `7/10`, 2 likes) : *« c'est un manga français et cela se ressent plus particulièrement dans l'humour »*
  * `FinalMangaka` (Manga-News T1, Positif, 16 juil. 2013, `19/20`) : *« un humour ravageur et super efficace »*
  * `arnonaud` (SensCritique T2, Mitigé, 2 oct. 2016, `7/10`, 2 likes) : *« toujours un bon paquet de blagues dont pas mal qui m'ont bien fait marrer »*

### 3.5. Critique n°5 — Rythme : démarrage lent, flashbacks ou combats étirés (`20 (6,6 %)` ; `15 / 115 (13,0 %)`)

* **Ce qui est reproché** : trois formes différentes. (1) **Démarrage** : le tome 1 / les premières pages jugés lents ou trop longs. (2) **Tome 3 plus long ou plus lent** : cinq avis (anglais, espagnol ×2, ukrainien, français) trouvent le flashback de Hameline ou le combat contre Konrad trop long, ou le tome « longuet ». (3) **Action qui se fait attendre** au tome 2 (SensCritique). Répartition : T1 : 12, T2 : 3, T3 : 5 ; langues : anglais 8, français 6, ukrainien 2, espagnol 2, portugais 1, indonésien 1. **Contrairement à l'anime** (démarrage lent n°1 avec 50 % des avis), le manga n'a pas de plainte dominante sur le début.
* **Citations** :
  * `Zutto` (Goodreads T2, Négatif, 17 nov. 2019, `2/5`, 2 likes) : *« especially the first 50 pages or so I was so sure I would just dump the series »*
  * `Will Brown` (Goodreads T3, Mitigé, 1 févr. 2020, `3/5`) : *« the fight felt really drawn out already, and continually cutting away without any significant development during the fight really pumped the brakes »*
  * `arnonaud` (SensCritique T2, Mitigé, 2 oct. 2016, `7/10`, 2 likes) : *« Les soucis de ce tome, c'est que l'action se fait attendre. »*
  * `Helen` (TheOASG T1, Négatif (lu), 8 nov. 2018, `2`) : *« Radiant’s 100 page opener feels excessively long, messy »*
  * `reveusedusud` (Babelio T3, Positif, 21 déc. 2016, `4,0/5`) : *« il n'aurait rien perdu à être grandement raccourci pour gagner en dynamisme »*
  * `Devin Panda` (Goodreads T1, Mitigé, 27 nov. 2024, `3/5`) : *« I was actually a little bored in the beginning »*
* **Contre-voix** : le tome 1 est jugé introductif mais « prometteur » par plusieurs avis, et au moins trois lecteurs disent que la série s'améliore au fil des tomes.
  * `Valentin` (Goodreads T2, Positif, 11 mars 2021, `5/5`) : *« Certain•es reprocheront peut-être que tout s'accélère très vite mais finalement, c'est pas un mal »*
  * `Tachan` (Goodreads T3, Mitigé, 4 janv. 2024, `3/5`) : *« A chaque tome, il semble éliminer des défauts pour ne garder que ce qui fait le succès de la série. »*

### 3.6. Critique n°6 — Logique du monde, explications absentes ou confuses ; récit brouillon (`16 (5,3 %)` ; `15 / 115 (13,0 %)`)

* **Ce qui est reproché** : l'Inquisition « mal expliquée », la logique des infections et des Némésis, la profondeur de la magie, des éléments « introduits de façon brouillonne ». **Une incohérence revient dans plusieurs avis du tome 1** : si les sorciers sont les seuls à pouvoir tuer les Némésis, pourquoi sont-ils craints et sans soutien de l'État (`Albs` en espagnol, `Andre` en anglais ; `The Book Dragon` relève une logique voisine : des villageois qui lancent des pierres à des sorciers puissants). Répartition : T1 : 12, T2 : 1, T3 : 1, série : 2. Petit effectif (16 avis).
* **Citations** :
  * `Nick` (Goodreads T1, Mitigé, 13 janv. 2020, `3/5`, 1 like) : *« Sadly, the author didn't do arithmetic very well, or a LOT of people are stupid enough to get touched by one of these Nemeses »*
  * `Selena Pigoni` (Goodreads T1, Mitigé, 23 juin 2019, `3/5`, 11 likes) : *« an institution that isn't really well explained despite the lengthy explanations of everything else »*
  * `The Book Dragon` (Goodreads T3, Positif, 18 janv. 2019, `4/5`, 1 like) : *« Tony Valente may not be good at writing believable worldviews and logic, but he does know how to end on cliffhangers. »*
  * `Josselin-B` (SensCritique série, Négatif, 27 déc. 2020, `2/10`, 20 likes) : *« Aucun approfondissement de la magie ne sera à noter dans l'œuvre. »*
  * `GeorgesBouche` (SensCritique série, Mitigé, 8 janv. 2019, `7/10`, 3 likes) : *« introduits de manière un peu brouillonne »*
  * `Andre` (Goodreads T1, Mitigé, 2 avr. 2022, `3/5`) : *« if wizards are the only ones who can destroy the Nemesis, why are they so feared and without government help? »*
* **Contre-voix** : le worldbuilding est l'un des points les plus cités en positif (`B2` mentionné par 58 avis *Positif* sur 120) ; plusieurs lecteurs aiment justement l'ampleur de l'univers.

### 3.7. Critique n°7 — Dessin jugé moyen, impersonnel ou trop jeune (`7 (2,3 %)` ; `6 / 115 (5,2 %)`)

* **Ce qui est reproché** : dessin « sans personnalité » (comparé à d'autres shōnen), « bon sans être excellent », orienté public jeune, absence de décors dans certaines cases. Répartition : T1 : 4, T2 : 1, série : 2. **Elle est presque absente des avis *Positif* (1 seul)**, et l'art est très loué ailleurs ; c'est la catégorie dont la note moyenne est la plus basse (46,4 % de l'échelle), sur 7 avis seulement.
* **Citations** :
  * `Josselin-B` (SensCritique série, Négatif, 27 déc. 2020, `2/10`, 20 likes) : *« Les dessins sont aussi impersonnels que le script »*
  * `Broyor` (SensCritique série, Négatif, 21 mai 2026, `1/10`, 1 like) : *« le dessin est exécrable de bout en bout »*
  * `Celestina1210` (Goodreads T1, Mitigé, 26 sept. 2024, `3/5`, 42 likes) : *« le graphisme qui est bon sans être excellent »*
  * `Kiraa7` (Manga-News T1, Positif, 30 août 2013, `15/20`) : *« il s'apparente tout de même pas mal à un jeune public »*
  * `julienhoel3` (Babelio T1, Négatif, 9 avr. 2025, `2,0/5`) : *« J'aime bien le style de dessin mais sans plus »*
* **Contre-voix** :
  * `David Estrella` (Otaku USA Magazine T1, Positif (lu), 2 nov. 2018, `sans note`) : *« the clean, dynamic art demonstrates Valente’s profound understanding of what makes manga pop »*
  * `Zirckhor` (Manga-News T1, Non noté, 7 oct. 2013, `sans note`) : *« je suis autant surpris de la qualité des dessins »*
  * `Selena Pigoni` (Goodreads T1, Mitigé, 23 juin 2019, `3/5`, 11 likes) : *« the art is expressive, character designs are neat with a touch of weird that makes it fun »*

### 3.8. Critique n°8 — Propos sur la discrimination jugé appuyé, maladroit ou problématique (`7 (2,3 %)` ; `6 / 115 (5,2 %)`)

* **Ce qui est reproché** : la métaphore du racisme jugée peu convaincante ou « preachy » ; un avis (T2) trouve que le traitement de l'islamophobie pose problème ; un autre (série) juge le manichéisme « patent » ; trois avis du tome 3 (dont un commentaire Manga-News sans note : « Beaucoup trop manichéen ») jugent le thème de l'exclusion appuyé, gratuit ou trop manichéen. **Effectif très petit (7 avis)** : T1 : 1, T2 : 2, T3 : 3, série : 1. Cinq des 7 avis portent sur les tomes 2 et 3, ceux de l'arc de Rumble Town, où le thème est le plus visible.
* **Citations** :
  * `Zutto` (Goodreads T2, Négatif, 17 nov. 2019, `2/5`, 2 likes) : *« Now, let's address the main thing that bothered me reading this volume and it's the islamophobia. »*
  * `The Book Dragon` (Goodreads T2, Mitigé, 19 nov. 2018, `3/5`) : *« it did seem to get a little preachy when it added the bit about chasing immigrants out of Rumble Town »*
  * `Helen` (TheOASG T1, Négatif (lu), 8 nov. 2018, `2`) : *« parts of this story seem like a barely-veiled metaphor for racism that doesn’t work well »*
  * `Josselin-B` (SensCritique série, Négatif, 27 déc. 2020, `2/10`, 20 likes) : *« le manichéisme patent et pâteux »*
  * `francois1123` (Manga-News T3, Mitigé, 9 sept. 2018, `12,0/20`) : *« la discrimination, qui ici fait écho à la fictive islamophobie et est gratuite de surcroît »*
  * `Catilina38` (Babelio T3, Mitigé, 27 avr. 2018, `3,5/5`) : *« le thème de l'exclusion des gens différent est appuyé »*
* **Contre-voix** : **16 avis (14 auteurs) louent explicitement ce propos** (Goodreads 8, Babelio 7, SensCritique 1 ; langues : fr 12, es 3, bg 1). C'est un sujet qui **polarise** : aucun des 7 auteurs de réserves n'en fait partie. Les éloges portent presque tous sur le tome 2 (11 sur 16), celui où le thème s'installe.
  * `Tachan` (Goodreads T2, Mitigé, 4 janv. 2024, `3/5`) : *« cela fait tellement écho à ce qui se joue en France depuis quelques temps »*
  * `arnonaud` (SensCritique T2, Mitigé, 2 oct. 2016, `7/10`, 2 likes) : *« une thématique sur l'immigration qu'on aurait pas eu sur un shônen japonais »*
  * `reveusedusud` (Babelio T2, Positif, 16 déc. 2016, `5,0/5`) : *« s'engage également dans la défense des droits humains »*
  * `DocBird` (Babelio T2, Positif, 1 mai 2019, `4,5/5`) : *« Le manga prend alors l'allure d'un plaidoyer pour accepter l'autre dans sa différence et son intégrité »*

### 3.9. Ce qui est loué le plus souvent (contre-voix d'ensemble)

*Comptage par mots-clés dans les 120 avis *Positif* en anglais ou français ; une mention n'est pas toujours une louange.*

* **Les personnages** : mentionnés par 81 avis sur 120. **L'humour** : 60. **Le dessin** : 58. **L'intrigue** : 57. **L'univers / la magie** : 58. **Les combats** : 36. **La discrimination** : 23 seulement par mots-clés, mais 16 avis la louent explicitement (§ 3.8).
* **Le fait que ce soit un manga français** : 56 avis sur 303 mentionnent la France, le français ou le « manfra ». Plusieurs y voient un plus (humour qui ne sent pas la traduction, dessin à hauteur des mangas japonais).
  * `jackpapy` (Manga-News T1, Positif, 17 févr. 2018, `18/20`) : *« Moi qui suis allergique au manga fr pour leur dialogue j’ai tous simplement adoré ce premier tome »*
  * `Tachan` (Babelio T1, Mitigé, 22 juil. 2020, `3,5/5`) : *« une copie parfaite du genre, au point que je n'aurais jamais pu deviner que ça n'avait pas été fait par un japonais »*
  * `Catilina38` (Babelio T1, Positif, 23 mars 2018, `4,5/5`) : *« les codes manga sont là et c'est vraiment très drôle et très maîtrisé »*
* **La série s'améliore avec les tomes** (trois lecteurs ; voir aussi le tableau par tome, § 2.2) :
  * `The Book Dragon` (Goodreads T2, Mitigé, 19 nov. 2018, `3/5`) : *« the second volume has saved the series for me »*
  * `Zian B.` (Goodreads T3, Positif, 13 janv. 2019, `4/5`) : *« It took 3 volumes but now i’m very invested in this »*
  * `Tachan` (Goodreads T3, Mitigé, 4 janv. 2024, `3/5`) : *« LE tome à partir duquel la série s’envole et trouve ses marques »*

---

## 4. Tableau comparatif : FMA (hors 2003) vs HxH (hors 1999) vs *Radiant* (anime) vs *Radiant* (manga)

| Dimension | *Fullmetal Alchemist* (`N = 1 097`) | *Hunter × Hunter* (`N = 897`) | *Radiant* anime (`N = 48`) | *Radiant* manga (`N = 303`) |
| :--- | :--- | :--- | :--- | :--- |
| **Verdicts favorables** | **91,0 %** — note moy. **9,02 / 10** | **88,4 %** — note moy. **8,83 / 10** | **64,6 %** — note moy. **6,81 / 10** | **54,5 %** *Positif* (58,9 % des avis notés ; seuil à 75 % de l'échelle) — note moy. **75,2 %** de l'échelle |
| **Pôle D — Narration** | **96,1 %** (D2 `42,5 %`) | **97,9 %** (D2 `81,4 %`) | **100 %** (D2 `66,7 %`) | **61,7 %** (D2 `27,5 %`) ; 80,3 % (≥ 50 mots) |
| **Pôle C — Personnages** | **61,4 %** | **77,7 %** | **95,8 %** | **58,6 %** ; 84,1 % (≥ 50 mots) |
| **Pôle B — Monde / système** | **56,2 %** | **67,7 %** | **60,4 %** | **50,5 %** ; 74,2 % (≥ 50 mots) |
| **Pôle A — Visuel** | **59,6 %** | **56,4 %** | **70,8 %** | **48,2 %** ; 63,6 % (≥ 50 mots) |
| **Pôle E — Action** | **41,0 %** (E2 `5,6 %`) | **55,4 %** (E2 `17,2 %`) | **52,1 %** (E2 `4,2 %`) | **30,2 %** (E2 `2,3 %`) ; 44,7 % (≥ 50 mots) |
| **Ratios `D/A` et `A/B`** | `1,61×` ; `1,06×` | `1,74×` ; `0,83×` | `1,41×` ; `1,17×` | `1,28×` ; `0,96×` |
| **Critique n°1 (tous avis)** | Rythme début/Briggs (`31,0 %`) | Lenteur/narrateur de *Chimera Ant* (`27,4 %`) | Démarrage lent (`50,0 %`) | **Dérivatif / déjà-vu (`12,2 %`)** |
| **Critique n°1 chez les mitigés/négatifs** | Rythme (`37,0 %`) | Lenteur/narrateur (`58,5 %`) | **Héros/casting générique (`82,4 %`)** | **Dérivatif / déjà-vu (`24,3 %`)** |
| **Critique de « classicisme »** | `7,9 %` | `6,1 %` | **`39,6 %`** | **`12,2 %`** |

**Lecture (mienne, à ne pas prendre pour un fait)** :
- **Le reproche de déjà-vu (C1) est le plus fréquent dans le manga comme dans l'anime** (`C3` de l'anime : 39,6 % ; ici `12,2 %`), très au-dessus des reproches de « classicisme » de FMA et HxH (`7,9 %` et `6,1 %`). Il pèse moins dans le manga, mais les bases diffèrent (anime : 48 avis MAL longs ; manga : 303 avis dont beaucoup sont très courts).
- **Les plaintes sur le héros générique sont bien plus rares dans le manga** : `C2 = 8,6 %` du corpus, `19,1 %` des mitigés/négatifs, contre `47,9 %` et `82,4 %` pour l'anime. **Le démarrage lent**, premier défaut de l'anime (`50,0 %`), n'est pas dominant chez les lecteurs du manga (`C5 = 6,6 %`). Je ne tire pas de cause de ces écarts.
- **Un défaut propre au manga : le texte à la page** (C3, 8,3 %), absent de l'anime. Il est proche, par le thème, de la « surexplication » de l'anime (14,6 %), sans être la même mesure.
- **Écarts à garder en tête** : taille et nature des corpus (303 avis multilingues, beaucoup d'avis courts, contre 897 et 1 097 critiques MAL), verdicts dérivés de la note et non étiquetés par les sites, listes de mots-clés différentes pour les pôles.

---

## 5. Limites et marges d'erreur

- **Taille** : avec `N = 303`, une part de 50 % a une marge d'environ ±6 points (IC à 95 %) ; avec `N = 222` (pôles), ±7 points ; avec `N = 115` (mitigés/négatifs), ±9 points. Les écarts entre tomes ou entre catégories rares (C7, C8 : 7 avis chacune ; C6 : 16) ne sont pas interprétables.
- **Corpus complet pour Goodreads, mais pas représentatif des lecteurs** : seuls les lecteurs qui écrivent un texte sont dans le corpus (115 avis notés pour 1058 notes au tome 1), et ils notent moins bien que l'ensemble (§ 1.1). Pas de conclusion sur « ce que pensent les lecteurs » en général.
- **Autres sites incomplets** : Babelio 59 critiques sur 81 annoncées ; SensCritique limité à la première page ; Booknode et Reddit absents ; pas de critique de rédaction Manga-News pour le tome 3 (elle n'existe pas). Les commentaires Manga-News datent en partie d'avant la sortie. Le corpus francophone est donc plus fragmentaire que le corpus anglophone.
- **Échelles hétérogènes** : un 4/5 Goodreads, un 8/10 SensCritique et un 15/20 Manga-News ne signifient pas la même chose ; les seuils de verdict sont les miens (annexe B). Avec un seuil à 70 % au lieu de 75 %, les `7/10` de SensCritique et les « 3,5/5 » passeraient en *Positif*.
- **Biais de survie par tome** : les lecteurs du tome 3 sont ceux qui ont continué ; le tome 1 compte 188 avis, le tome 3 47.
- **Notes entières sur Goodreads** : 16 avis annoncent une note décimale ; 11 avis *Mitigé* sont des 3,5/5 arrondis à 3 (sans effet sur le verdict).
- **Auteurs répétés** : 49 pseudos apparaissent plus d'une fois ; trois avis ou plus pour 28 d'entre eux, dont `Daniel` (4), `Flozer` (3), `lag123` (3), `soroxas` (3), `Roman Zarichnyi` (3), `Jessica` (3). Ces pseudos peuvent être des homonymes (« Daniel », « Jessica »). Les auteurs à plusieurs avis pèsent plusieurs fois dans les comptages.
- **Pôles** : codés par mots-clés (annexe A) sur 222 avis seulement ; une mention n'indique ni un jugement positif ni négatif. Les comptages d'œuvres citées (§ 3.1) et de mentions de la France (§ 3.9) sont aussi faits par mots-clés.
- **C1–C8** : codées à la main (fichier de codage joint). Tous les avis *Mitigé* et *Négatif* ont été lus ; les réserves dans les avis *Positif* ont été repérées par mots-clés et ont pu m'échapper (§ 2.2). Ces catégories sont tirées du corpus lui-même : elles décrivent ces avis, pas un lexique indépendant comme celui de FMA/HxH.
- **Langues** : les avis ukrainiens, espagnols, bulgares, allemands, indonésiens, croates, danois et autres sont codés sur C1–C8 par ma lecture ; je ne suis pas locuteur natif de ces langues, la lecture est donc moins fine que pour l'anglais et le français.
- **Pas de lecture de l'œuvre** : ces chiffres décrivent des avis, pas la qualité du manga.

---

## Annexe A — Listes de mots-clés des pôles (anglais et français, insensibles à la casse)

Voir `/home/user/radiant_manga_analyse/analyse.py` (dictionnaire `POLES`) : une expression régulière par sous-pôle, avec les termes anglais de l'analyse de l'anime et leurs équivalents français (ex. `D2` : *rythme, lent, longuet, traîne, démarr…, explications, flash-back, chapitre*, `A1` : *dessin, graphi…, trait, planches, décors, couleurs, mise en page, découpage*, `B1` : *racisme, discrimin…, xénophob…, préjugés, immigr…, morale, thématiques, bouc émissaire*, `HUM` : *humour, drôle, blagues, gags…*). Retirés par rapport à l'anime : les termes liés à l'animation (*Lerche, CGI, animation*) et à la musique.

## Annexe B — Règle de verdict (note normalisée)

| Échelle | *Positif* (≥ 75 %) | *Mitigé* (41–74 %) | *Négatif* (≤ 40 %) |
| :--- | :--- | :--- | :--- |
| Goodreads `/5` | 4–5 | 3 | 1–2 |
| SensCritique `/10` | 8–10 | 5–7 | 1–4 |
| Manga-News `/20` | 15–20 | 9–14 | 1–8 |
| Askear `/5` ; Nerdbot `/5` | 3,8 → *Positif* | 3,5 → *Mitigé* | — |

Sans note : *Non noté* ; exceptions lues à la main : `TheOASG` (négatif), `Otaku USA` (positif).

Numérotation des catégories C1–C8 : par rang de fréquence dans ce corpus (elle ne correspond donc pas à celle du MD de l'anime).

## Annexe C — Fichiers

- `Radiant_tomes_1_3_corpus_avis.json` (ton fichier) : source des avis Goodreads (textes coupés à environ 500 caractères, sans pseudo), Babelio, Manga-News et SensCritique. `radiant_manga/goodreads_full_parsed.json` : textes complets et pseudos Goodreads que j'ai récupérés.
- `radiant_manga_analyse/codage_critiques_radiant_manga.csv` et `.json` : une ligne par avis (303), avec verdict, catégories C1–C8, pôles (anglais/français) et langue détectée.
- `goodreads_radiant_tomes_1_3_complet.json` et `critiques_manga_radiant_autres_sites_complet.json` : le corpus de 303 avis après dédoublonnage (textes complets, pseudos, notes). Les deux anciens JSON (version partielle) sont conservés tels quels.
- Scripts : `radiant_manga_analyse/corpus2.py` (fusion des sources), `prep.py` (dédoublonnage, langues), `analyse.py` (pôles), `codes_v2.py` (codage C1–C8), `stats.py`, `build_md.py` / `write_md.py` (tableaux et citations vérifiées).
