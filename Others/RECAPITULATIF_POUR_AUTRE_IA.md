# Récapitulatif de passation — Workspace « Battle Shōnen × Collin de Plancy »

**Destinataire :** autre IA (assistant avec exécution de code Python et lecture de fichiers).
**Émetteur :** agent Arena.ai ayant réalisé les quatre chantiers décrits ci-dessous.
**Date d'état :** 4 octobre 2026.
**Périmètre :** le contenu des deux archives ZIP livrées avec ce document.

> ⚠️ **Règle absolue imposée par l'utilisateur : « N'invente rien. »**
> Chaque chiffre, chaque titre et chaque citation doit sortir d'un comptage exécuté sur les fichiers du workspace. Aucune donnée ne doit être extrapolée, estimée « à vue de nez » ou complétée de mémoire. Si une information manque, écrire qu'elle manque.
> **Langue de travail : le français.** L'utilisateur écrit et attend ses livrables en français.

> ⚠️ **Ce document est volontairement hors des ZIP.** Il ne doit pas être fusionné avec eux ni recopié tel quel dans un livrable : c'est une note de passation technique.

---

## 0. Comment reprendre le travail en 5 minutes

1. Décompresser les deux ZIP (ils se complètent, aucun contenu redondant).
2. Pour la partie **critique de réception / Battle Shōnen** : ouvrir en priorité
   - `benchmark_4_piliers/codage_critiques_FMA_HxH_hors_anime_anterieur.csv` (table de codage, 1 ligne = 1 critique),
   - `benchmark_4_piliers/Analyse_critiques_recurrentes_FMA_hors_2003.md`,
   - `benchmark_4_piliers/Analyse_critiques_recurrentes_HxH_hors_1999.md`,
   - `benchmark_4_piliers/Synthese_comparative_4_piliers_vs_Red_Hood.md`.
3. Pour la partie **corpus historiques** : ouvrir `dictionnaire_infernal_1825/dictionnaire_infernal_1825.db` et `dictionnaire_feodal_1820/dictionnaire_feodal_1820.db` (SQLite + FTS5) — **ne pas** charger les gros JSON en texte brut, interroger les bases ou les JSON par script.
4. Pour la partie **catalogue MAL** : ouvrir `uploads/catalogue_mal_shonen.json` (`2 951` œuvres, collecte du 30/09/2026) — **c'est la seule source de scores/notoriété à utiliser pour cette partie**.
5. Lire la § 8 **avant** de refaire une collecte web : plusieurs API et URL sont déjà connues comme cassées.

---

## 1. Les deux archives ZIP

| Archive | Contenu | Fichiers | Taille compressée | SHA-256 |
| :--- | :--- | :---: | :---: | :--- |
| **`workspace_1_benchmark_battle_shonen_et_corpus.zip`** | `benchmark_4_piliers/` + `uploads/` : corpus de critiques, codages, rapports d'analyse, catalogue MAL | 22 | **3,25 Mo** | `21fd035ee747a2d6692261d8859cb3b3436f377b356c3602054363e57b56d98b` |
| **`workspace_2_dictionnaires_1820_1825.zip`** | `dictionnaire_feodal_1820/` + `dictionnaire_infernal_1825/` : JSON structurés, bases SQLite FTS5, rapports | 17 | **9,74 Mo** | `b53b89c9a9d478b0ae7d9bd4ffe281b60e8b79a945994391e1ab495a153a2b72` |

Volume total décompressé : **~44 Mo** pour **39 fichiers**. Contrôle d'intégrité effectué (`unzip -t`) : aucune erreur.

---

## 2. Chantier 1 — Benchmark « Battle Shōnen » et grille en 5 pôles

### 2.1. Origine de la demande

L'utilisateur a construit une grille personnelle à partir du cas *The Hunters Guild: Red Hood* (Yūto Suzuki, 2021, annulé au ch. 18) : il cherchait à savoir **ce qui attire** les lecteurs d'un battle shōnen et **pourquoi un bon lancement ne suffit pas à créer un attachement durable**. La grille a ensuite été testée sur des séries longues.

### 2.2. La grille en 5 pôles (à respecter telle quelle)

| Pôle | Libellé | Sous-codes |
| :--- | :--- | :--- |
| **D** | **Narration / Scénario / Histoire** | `D1` Intrigue & cohésion · `D2` Rythme, arcs, narrateur · `D3` Dramaturgie, ton, émotion · `D4` Climax, fin, résolution |
| **C** | **Personnages / Cast choral** | (pôle simple ; antagonistes inclus chez HxH) |
| **A** | **Visuel strict** | `A1` Trait / animation / style · `A2` Esthétique propre à la série (alchimie ; auras & gore) · `A3` Chara-design |
| **B** | **Monde / Système** | `B1` Philosophie & morale · `B2` Worldbuilding & système de pouvoir (alchimie ; *Nen*) |
| **E** | **Action / Chorégraphie / Tactique** | `E1` Combats & chorégraphie · `E2` Tactique & stratégie |

**Contrainte utilisateur explicite :** le **pôle D doit toujours figurer en entier** dans les tableaux comparatifs, à côté de Monde, Personnages et Visuel. Ne jamais le fusionner ni l'omettre.

### 2.3. Résultats mesurés — *Fullmetal Alchemist* (hors anime 2003)

Corpus : `uploads/corpus_critiques_MAL_FMA.json` — **`N = 1 097`** critiques (**Manga `60`** + ***Brotherhood* `1 037`**) ; `91,0 %` *Recommended* global, `92,6 %` hors critiques « seulement comparatives », note moyenne `9,02/10`.

| Pôle | Taux | Détail | Écart Manga / Anime |
| :--- | ---: | :--- | :--- |
| **D** Narration | **`96,1 %`** (`1 054`) | `D1` 90,7 % · `D2` 42,5 % · `D3` 50,9 % · `D4` 36,2 % | 95,0 % M / 96,1 % B |
| **C** Personnages | **`61,4 %`** (`674`) | — | 66,7 % M / 61,1 % B |
| **A** Visuel strict | **`59,6 %`** (`654`) | `A1` 57,5 % · `A2` 3,5 % · `A3` 9,9 % | 58,3 % M / 59,7 % B |
| **B** Monde & philosophie | **`56,2 %`** (`617`) | `B1` 38,6 % · `B2` 44,0 % | 63,3 % M / 55,8 % B |
| **E** Action & tactique | **`41,0 %`** (`450`) | `E1` 38,8 % · **`E2` 5,6 %** | 45,0 % M / 40,8 % B |

Ratios : `D/A = 1,61×` (`1,63×` en manga) ; `A/B = 0,92×` (manga) / `1,06×` (total).

### 2.4. Résultats mesurés — *Hunter × Hunter* (hors anime 1999)

Corpus : `uploads/corpus_critiques_MAL_HxH.json` — **`N = 897`** critiques (**Manga `40`** + ***HxH 2011* `857`**) ; `88,4 %` *Recommended* global, `89,2 %` hors comparatives, note moyenne `8,83/10`.

| Pôle | Taux | Détail | Écart Manga / Anime |
| :--- | ---: | :--- | :--- |
| **D** Narration | **`97,9 %`** (`878`) | `D1` 88,3 % · **`D2` 81,4 %** · `D3` 53,3 % · `D4` 36,5 % | 97,5 % M / 97,9 % A |
| **C** Personnages | **`77,7 %`** (`697`) | — | 60,0 % M / 78,5 % A |
| **B** Monde, morale & *Nen* | **`67,7 %`** (`607`) | `B1` 23,4 % · **`B2` 62,0 %** | 70,0 % M / 67,6 % A |
| **A** Visuel strict | **`56,4 %`** (`506`) | `A1` 54,5 % · `A2` 2,7 % · `A3` 10,8 % | 50,0 % M / 56,7 % A |
| **E** Action & tactique | **`55,4 %`** (`497`) | `E1` 53,7 % · **`E2` 17,2 %** | 50,0 % M / 55,7 % A |

Ratios : `D/A = 1,74×` (`1,95×` en manga) ; `A/B = 0,71×` (manga) / `0,83×` (total).
**À retenir :** la tactique (`E2`) pèse **3× plus** chez *HxH* que chez *FMA* (17,2 % vs 5,6 %), et le rythme/narrateur (`D2`) est un pôle *négatif* massif (81,4 % de mentions, dont beaucoup critiques).

### 2.5. Les 6 critiques récurrentes intrinsèques (hors phrases de nostalgie comparative)

Table de codage : `benchmark_4_piliers/codage_critiques_FMA_HxH_hors_anime_anterieur.csv` (colonnes : `work, subcorpus, user, date, year, tag, score, reactions, word_count_clean, is_prior_comparison_driven, matched_criticisms`) + son résumé `…json`.
Fichiers totalement exclus : *FMA 2003* (`252` critiques) et *HxH 1999* (`59`) — y compris les phrases de comparaison nostalgique à l'intérieur des corpus *Brotherhood* / *2011*, marquées `is_prior_comparison_driven = True`.
Base intrinsèque : **FMA `N = 982`** (dont `73` Mix/NotRec) ; **HxH `N = 869`** (dont `94` Mix/NotRec).

**FMA :** ① Rythme/lenteurs (*Briggs*, *Liore*) — 30,7 % (37,0 % chez Mix-NotRec) · ② Humour *chibi* — 10,2 % (31,5 %) · ③ Tropes shōnen / *Father* / fin — 7,8 % (34,2 %) · ④ « Surcoté, n°1 MAL » — 8,8 % (34,2 %) · ⑤ Exposition et facilités scénaristiques — 3,5 % (11,0 %) · ⑥ Combats d'alchimie peu tactiques, dessin « simple », *plot armor* — 1,3 % (12,3 %).

**HxH :** ① Lenteur + narrateur dans *Chimera Ant* et *Succession* — 27,0 % (58,5 %) · ② Début enfantin/lent (*Hunter Exam*) — 26,7 % (28,7 %) · ③ Arcs disjoints / *Greed Island* / *Genthru* / Kurapika-Leorio disparus — 24,3 % (44,7 %) · ④ Hiatus, inachèvement, dessin manga brut — 13,9 % (11,7 %) · ⑤ *Alluka/Nanika* en *deus ex machina*, anticlimax, *Nen* contorsionné — 10,1 % (25,5 %) · ⑥ « Surcoté » — 6,1 % (27,7 %).

### 2.6. Les 6 contre-voix majoritaires (déjà listées pour les deux séries)

Elles ont été extraites et comparées pour *FMA* (`92,6 %` favorable) et *HxH* (`89,2 %` favorable) dans les deux rapports `Analyse_critiques_recurrentes_*.md` : chaque critique récurrente y est appariée à la réponse majoritaire qui la neutralise dans le discours des recommandants. **Si l'utilisateur redemande cette liste, elle se reconstruit à partir de ces deux fichiers** (section « contre-voix »), pas d'une nouvelle collecte.

### 2.7. Le cas *Red Hood* et les 5 séries de référence

- Fichiers : `benchmark_4_piliers/synthese_red_hood.md` (analyse Reddit : `4 432` commentaires, `1 382` comptes), `Analyse_critiques_recurrentes_Red_Hood_et_comparaison_series_longues_2026-09-29.md`, `Addendum_MAL_Japon_MangaPlus_ToC_et_grille_de_lecture_2026-09-29.md`, `Synthese_comparative_4_piliers_vs_Red_Hood.md`.
- Données : `mal_reviews_5_series.json` (`300` critiques MAL réparties sur 6 séries : 60+40+60+60+20+60) et `goodreads_tomes_1_2_5_series.json` (`371` critiques réparties sur `13` fiches = 5 séries × Tomes 1-2 + Red Hood Tomes 1-3), plus `reddit_jjk_2018_ch1_18.json`. ⚠️ Les rapports travaillent sur des sous-ensembles analysés (`N = 311` en couche Goodreads, `N = 240` en couche MAL) : ne pas confondre le total du fichier et l'effectif analysé.
- **Mesure clé (Chapitre 1 Reddit, `N = 185` commentaires vérifiés)** : Pôle A Visuel **48,1 %** vs Pôle B Monde/Conte de fées **32,4 %** → ratio **1,48×** en faveur du visuel (au sein du pôle A : `A1` 28,6 % > `A3` 22,7 % > `A2` 10,8 % ; au sein du pôle B : `B2` dark fantasy 24,3 % > `B1` conte 13,5 %).
- **Sur la série entière (ch. 1–18, `N = 4 432`)** : A **16,2 %** vs B **10,7 %** → ratio **1,51×** (`30,5 %` vs `20,7 %` en comptes uniques).
- **En relié (Goodreads T1, `N = 30`)** : A **56,7 %** vs B **63,3 %** → ratio **0,90×** : l'avantage visuel **disparaît** en lecture volume.
- Comparaison inter-séries (Goodreads T1, `30` critiques/série) — mentions du Visuel : *Red Hood* **56,7 %** > *FMA* 30,0 % > *One Piece* 26,7 % > *Naruto* 26,7 % > *HxH* 23,3 % > *JJK* 16,7 %. Sur MAL, `90,0 %` des critiques de *Red Hood* parlent du dessin contre 35–37 % d'éloge pur pour *JJK*/*HxH*.
- Piège documenté : le prénom « Grimm » apparaît dans `868` commentaires sur `4 432`, mais massivement pour parler de ses répliques — **ne jamais s'en servir comme proxy du « conte de fées »**.

> **Consigne utilisateur :** ne pas relancer les analyses *Red Hood* de sa propre initiative (il l'a dit explicitement : « Je te demande pas de les faire, juste je te pose la question »).

---

## 3. Chantier 2 — *Dictionnaire infernal* (2ᵉ éd., 1825-1826, 4 tomes)

### 3.1. Ce que c'est

Numérisation structurée et intégralement fichée de la 2ᵉ édition (Paris, P. Mongie aîné, 1825-1826, 4 vol. + Atlas) de Jacques Collin de Plancy — l'édition **libérale, sceptique et anticléricale**, antérieure de 12 ans à sa conversion de 1837 et à l'édition illustrée de 1863.

### 3.2. Fichiers et usage

| Fichier | Rôle | Taille |
| :--- | :--- | ---: |
| `dictionnaire_infernal_1825.db` | **Source de vérité** : SQLite, table `articles` + index **FTS5** (`articles_fts`) | 11,2 Mo |
| `dictionnaire_infernal_1825_4_tomes_complets.json` | JSON intégral : `metadata`, `paratexte_1825_tome_1`, `explication_des_planches_et_pacte_grandier_tome_4`, `articles` | 5,4 Mo |
| `dictionnaire_infernal_1825_tomes_1_2.json` / `…_tomes_3_4.json` | Mêmes données scindées (pour IA à fenêtre limitée) | 2,5 / 2,8 Mo |
| `dictionnaire_infernal_1825_index_leger_4_tomes.json` | Index allégé + `extrait_debut` (220 car.) | 1,2 Mo |
| `cour_infernale_et_demons_1825_4_tomes.json` | Sous-corpus démonologie / Goétie (entrées démons avec fiches) | 0,5 Mo |
| `cour_infernale_et_demons_1825_t1_t2.json` | Idem, Tomes 1-2 | 0,3 Mo |
| `ANALYSE_COMPLETE_DICTIONNAIRE_INFERNAL_1825_4_TOMES.md` | Rapport d'analyse (à ne pas montrer en premier si l'on veut un regard indépendant) | 57 Ko |
| `ANALYSE_DICTIONNAIRE_INFERNAL_1825_TOMES_1_2.md` | Premier rapport (Tomes 1-2) | 33 Ko |
| `GUIDE_ET_PROMPTS_POUR_AUTRE_IA.md` | Guide + prompts prêts à copier-coller | 8 Ko |

### 3.3. Statistiques réelles (source : `metadata.statistiques_globales` du JSON complet et `count(*)` de la base)

- **`2 517` articles** — Tomes : T1 (A-B) `501` · T2 (C-E) `603` · T3 (F-L) `576` · T4 (M-Z) `837`.
- Répartition par lettre : `C` **400**, `A` 273, `B` 228, `M` 169, `P` 164, `S` 142, `G` 147, `L` 127… jusqu'à `Q` 3, `W`/`X`/`Y` 5.
- **7 catégories principales** (avec % du total) : ① Hiérarchie & Cour infernale **`259`** (10,3 %) · ② Sorcellerie, sabbats, pactes, procès **`490`** (19,5 %) · ③ Divination & sciences occultes **`537`** (21,3 %) · ④ Folklore, spectres, revenants, vampires **`177`** (7,0 %) · ⑤ Mythologies & religions comparées **`188`** (7,5 %) · ⑥ Personnages historiques, savants, démonologues **`294`** (11,7 %) · ⑦ Superstitions populaires & prodiges **`572`** (≈22,7 %).
- Champs par article : `id` (`DI1825_T{1..4}_{num}`), `tome`, `lettre`, `page_estimee`, `titre`, `texte`, `notes_de_bas_de_page`, longueurs, `categorie_principale`, `categories_secondaires`, `est_demon_hierarchie` + `fiche_demonologique` (`rangs_et_titres`, `legions_mentionnees`), `marqueurs_ton_voltairien_1825`, `sources_et_auteurs_cites`.

> ⚠️ **Incohérence à connaître :** `dictionnaire_infernal_1825_index_leger_4_tomes.json` et `GUIDE_ET_PROMPTS_POUR_AUTRE_IA.md` annoncent **`2 490`** articles, chiffre issu du parseur **antérieur au correctif** (voir § 8, bug de filtre monotone). La base `.db` et le JSON `…_4_tomes_complets.json` portent le décompte corrigé de **`2 517`**. **Toujours citer `2 517` et signaler l'index léger comme plus ancien** (ou le régénérer) si l'utilisateur s'appuie dessus.

### 3.4. Requêtes utiles

```python
import sqlite3
c = sqlite3.connect('dictionnaire_infernal_1825/dictionnaire_infernal_1825.db')
# recherche plein texte
c.execute("SELECT id, titre FROM articles_fts WHERE articles_fts MATCH ? ORDER BY rank LIMIT 20", ('sabbat',)).fetchall()
# démons du Tome 4
c.execute("SELECT titre, rangs_et_titres, legions_mentionnees FROM articles WHERE est_demon_hierarchie=1 AND tome=4").fetchall()
# articles les plus longs
c.execute("SELECT titre, longueur_mots FROM articles ORDER BY longueur_mots DESC LIMIT 30").fetchall()
```
`articles_fts` indexe : `id, titre, categorie_principale, rangs_et_titres, sources_citees, texte`.

---

## 4. Chantier 3 — *Dictionnaire féodal* (2ᵉ éd., 1820) + répertoire croisé

### 4.1. Le corpus

`Dictionnaire féodal, ou Recherches et anecdotes sur les dîmes et les droits féodaux…`, 2ᵉ édition corrigée et augmentée (Paris, Brissot-Thivars, 1820, 2 tomes ; 1ʳᵉ éd. Foulon, 1819). Même auteur que le *Dictionnaire infernal* — l'idée directrice est de fournir le **matériau de « vieux monde » français** (droits seigneuriaux, justices, folklore, personnages historiques) réutilisable dans un battle shōnen.

### 4.2. Fichiers

| Fichier | Contenu | Taille |
| :--- | :--- | ---: |
| `dictionnaire_feodal_1820.db` | SQLite + FTS5 (table `articles` / `articles_fts`) | 2,5 Mo |
| `dictionnaire_feodal_1820_complet.json` | JSON intégral : `metadata`, `paratexte_tome_1` (Discours préliminaire 1819, Avertissement 1820, *Tableau de l'Ancien Régime*), `articles`, `paratexte_fin_tome_2` (Conclusion, Table des auteurs consultés, **Table générale des matières**) | 2,0 Mo |
| `repertoire_personnages_et_folklore_francais_shonen.json` | **Répertoire croisé** (voir 4.4) | 3,2 Mo |
| `ANALYSE_COMPLETE_DICTIONNAIRE_FEODAL_1820.md` | Rapport d'analyse | 63 Ko |
| `REPERTOIRE_PERSONNAGES_HISTORIQUES_ET_FOLKLORE_FRANCAIS_SHONEN.md` | Rapport du répertoire | 31 Ko |

### 4.3. Statistiques réelles

- **`266` articles** : T1 (A-I) `162` · T2 (J-Z) `104` ; `126 588` mots / `802 410` caractères.
- **`679` anecdotes et cas** découpés dans les articles.
- Lettres les plus fournies : `D` 35, `C` 31, `F` 21, `A` 19, `P` 18, `E` 17, `M` 15.
- Catégories : ① Hiérarchie nobiliaire & fiefs `51` (19,2 %) · ② Droits féodaux, redevances, corvées, péages `79` (29,7 %) · ③ Foi & hommage, vassalité `19` (7,1 %) · ④ Justices seigneuriales, duels judiciaires, ordalies `27` (10,2 %) · ⑤ Clergé féodal, dîmes, bénéfices, Inquisition `49` (18,4 %) · ⑥ Servitude, glèbe, mainmorte, affranchissements `19`.
- Champs SQLite : `id, tome, lettre, page_imprimee, titre, categorie_principale, longueur_caracteres, longueur_mots, nb_anecdotes, dates_mentionnees, regions_mentionnees, sources_citees, texte`.

### 4.4. Le répertoire croisé (fichier `repertoire_personnages_et_folklore_francais_shonen.json`)

- **`421` personnages historiques et savants** extraits.
- **`613` articles de folklore / histoire de France** issus du *Dictionnaire infernal* 1825, **rangés par 11 régions françaises** : Paris & Île-de-France `201`, Poitou-Touraine-Anjou `131`, Bretagne & Finistère `117`, Lorraine-Alsace-Champagne `101`, Provence-Dauphiné-Lyonnais `90`, Languedoc-Roussillon-Pyrénées `74`, Bourgogne-Franche-Comté-Jura `47`, Picardie-Artois-Flandre `43`, Pays basque-Béarn-Gascogne `34`, Normandie `34`, Auvergne-Limousin-Berry `23`.
- **`266` articles de coutumes féodales** (issus du *Dictionnaire féodal*) rattachés au même dispositif.
- Clés du JSON : `metadata`, `personnages_historiques_et_savants` (liste), `folklore_et_affaires_par_region_francaise` (dict région → articles), `articles_francais_texte_complet` (liste).

Ce fichier est le **livrable de croisement** entre les deux dictionnaires : il sert à un projet de série mêlant folklore régional français, histoire et codes du shōnen. Les fichiers `Etude_complete_Dictionnaire_Infernal_1825.md`, `Utilisation_references_folklore_religion_Battle_Shonen.md` et `Esthetique_vestimentaire_anachronique_Battle_Shonen (1).md` (dans `uploads/`) documentent l'exploitation de ce matériau et les problèmes d'anachronisme repérés.

---

## 5. Chantier 4 — Catalogue MAL des shōnen et sélection de la décennie

### 5.1. Le catalogue

`uploads/catalogue_mal_shonen.json` — **`2 951` œuvres**, type *manga*, démographie *Shounen*, début ≥ 1980, collecte **figée au 30/09/2026**. Champs par œuvre : `mal_id, url, titre, titre_en, notateurs, membres, score, volumes, chapitres, statut, annee_debut, annee_fin, genres, themes, demographies, magazines, auteurs, collecte`.
**L'URL fournie par l'utilisateur (`…/api/catalogue/json`) sert exactement le même contenu** que ce fichier (vérifié) : inutile de re-collecter, sauf besoin d'un rafraîchissement.
Pièges documentés par le catalogue lui-même : `notateurs` ≠ `membres` (le second n'est **ni** une vente **ni** une lecture) ; `statut` est déduit de la ligne « Published » ; les manfras et les séries non classées « manga » par MAL sont absents (ex. *Radiant*) ; les magazines seinen d'un même éditeur sont absents.

### 5.2. Sélection livrée : shōnen lancés ≥ 2020 avec score **> 7,80**

**`28` titres** (sur `608` shōnen lancés depuis 2020, soit `4,6 %` ; moyenne du pool `6,75`). Livrables : `benchmark_4_piliers/Shonen_2020s_superieurs_a_7.80_MAL_2026-09-30.md` + `.csv`.

Top 10 par note : **Sousou no Frieren** 8,87 (2020) · **Sayonara Eri** 8,63 (2022, one-shot) · **Mayonaka Heart Tune** 8,48 (2023) · **Sensou Kyoushitsu** 8,46 (2022) · **Look Back** 8,44 (2021, one-shot) · **Bungou Stray Dogs: Dazai, Chuuya, Juugosai** 8,41 (2022, terminé) · **Mairimashita! Iruma-kun: If Episode of Mafia** 8,39 (2023) · **Dandadan** 8,38 (2021) · **Ao no Hako** 8,32 (2021, terminé) · **Shangri-La Frontier** 8,28 (2020).
Puis : Phantom Busters 8,25 · Gachiakuta 8,18 · Kesa mo Yuraretemasu 8,16 · Akane-banashi 8,15 · Kagurabachi 8,08 · Tower Dungeon 8,08 · Sakamoto Days 8,05 · One Piece: Episode A 8,03 · Seihantai na Kimi to Boku 8,00 · Futari Bus 7,95 · Nigoru Hitomi… Highserk Senki 7,94 · Madan no Ichi 7,91 · Exorcist wo Otosenai 7,89 · Tsue to Tsurugi no Wistoria 7,88 · Takopii no Genzai 7,87 · Mikadono Sanshimai… 7,83 · Boruto: Two Blue Vortex 7,81 · Blue Lock: Episode Nagi 7,81.

Stats d'ensemble : moyenne `8,16`, médiane `8,12` ; `22` en cours / `6` terminés ; par année : 2020 → 5, 2021 → 7, 2022 → 7, 2023 → 6, 2024 → 2, 2025 → 1, **2026 → 0** ; magazines dominants : **Shounen Jump+ 6**, **Shounen Jump 5**, Sunday 3, Magazine 3 ; genres dominants **Fantasy 13 / Action 13**, Comedy 8, Romance 7.
Cas limites signalés : *Ogami Tsumiki to Kinichijou.* à **7,80 pile** est exclu (strictement supérieur) ; *Kaijuu 8-gou* et *Mashle* très notoires mais à **7,60** ; one-shots et spin-offs inclus et signalés comme tels ; Tatsuki Fujimoto seul auteur présent deux fois.

---

## 6. Contraintes permanentes posées par l'utilisateur

1. **« N'invente rien »** — aucune donnée non vérifiable ; toute affirmation chiffrée doit être reproductible par script.
2. **Français** pour tous les livrables.
3. **Une série à la fois** pour les gros traitements de corpus (il a demandé *FMA* puis *HxH* en deux temps distincts pour éviter les blocages d'interface).
4. **Exclusions strictes** : anime *FMA 2003* et anime *HxH 1999* exclus des analyses (sous-corpus dédiés **et** phrases de comparaison nostalgique à l'intérieur de *Brotherhood* / *2011*).
5. **Pôle D (Narration / Scénario) toujours présent** dans les tableaux, jamais absorbé dans un autre pôle.
6. **Ne pas relancer les analyses *Red Hood*** sans demande explicite.
7. Les livrables longs sont écrits en fichiers Markdown/CSV/JSON dans le workspace, puis présentés à l'utilisateur — pas seulement en réponse de chat.

---

## 7. Chiffres « signature » à ne pas confondre

| | *FMA* (hors 2003) | *HxH* (hors 1999) | *Red Hood* |
| :--- | :---: | :---: | :---: |
| Effectif codé | `1 097` (M 60 / B 1 037) | `897` (M 40 / 2011 857) | `185` comm. ch.1 (vérifiés) |
| % *Recommended* | `91,0 %` / `92,6 %` intrinsèque | `88,4 %` / `89,2 %` intrinsèque | `45,0 %` (MAL) |
| Note moyenne | `9,02/10` | `8,83/10` | — |
| Pôle D | `96,1 %` | `97,9 %` | — |
| Pôle A | `59,6 %` | `56,4 %` | `48,1 %` (ch.1) |
| Pôle B | `56,2 %` | `67,7 %` | `32,4 %` (ch.1) |
| Pôle E | `41,0 %` — `E2` 5,6 % | `55,4 %` — `E2` 17,2 % | — |
| Ratio A/B | `1,06×` | `0,83×` | **`1,48×`** (ch.1) / `0,90×` (relié) |

Lecture : *HxH* est la série **la plus portée par son système et sa tactique**, *FMA* par sa narration et sa philosophie, *Red Hood* est le seul cas où **le visuel attire plus que le monde** — et c'est précisément l'anomalie que l'utilisateur cherche à exploiter ou à corriger.

---

## 8. Pièges techniques déjà rencontrés (ne pas les refaire)

| Problème | Solution retenue |
| :--- | :--- |
| `api.jikan.moe/v4/manga/{id}/reviews` → **HTTP 504** | Scraper directement `https://myanimelist.net/manga/{id}/{slug}/reviews` (HTTP 200 stable) |
| `arctic-shift…/posts/search` avec `before=` seul → **HTTP 422** | Toujours passer `after=` **et** `before=` (fenêtre étroite) |
| Goodreads : le slug textuel est ignoré, seul l'`id` compte (id erronés → livres sans rapport) | IDs vérifiés : *FMA* `870`/`873` · *HxH* `18249913`/`29931268` · *JJK* `44451887`/`51169203` · *One Piece* `1237398`/`364956` · *Red Hood* `60433200`/`61273638`/`61273651` |
| MAL : `data-id="1"` est le tag de recommandation, pas l'ID de critique ; balises `<i>` polluent le verdict | Extraire `review_id` via `reviews\.php\?id=(\d+)` ; nettoyer les `<i …></i>` du verdict |
| Pagination MAL non authentifiée : `manga/26/…/reviews?p=3` → **HTTP 404** (plafond 40 critiques) | Se limiter à `p=1,2` pour le manga *HxH* |
| **Parse des Tomes 3-4 (Dictionnaire infernal)** : un mot capitalisé isolé (*LA —*, *LIV. —*) faisait avancer le filtre de lettre (`F→L`, `M→S`) et sautait des lettres entières | Corrigé par `parse_vol_windowed` : n'accepter le changement de lettre qu'avec confirmation (`≥ 2` des 5 candidats suivants). **C'est ce correctif qui fait passer le total de `2 490` à `2 517` articles** |
| Gros JSON non lisibles « en texte brut » par une autre IA | Toujours passer par script Python (`json`), par la base SQLite FTS5, ou par les fichiers scindés / allégés prévus à cet effet |

---

## 9. Points de vigilance ouverts

1. **Index léger du *Dictionnaire infernal*** : `2 490` articles contre `2 517` réel — à régénérer si l'utilisateur doit s'en servir, et `GUIDE_ET_PROMPTS_POUR_AUTRE_IA.md` doit être corrigé (§ 3.3).
2. **Scores et notoriété** du catalogue MAL sont **figés au 30/09/2026** : pour toute mise à jour, re-collecter (l'URL de l'utilisateur sert le même jeu).
3. **Sélection 2020+** mêle séries longues, one-shots et spin-offs : si l'utilisateur veut une liste « purement séries d'action », il faut refiltrer et l'annoncer.
4. **Aucune donnée de ventes** n'existe dans ce workspace : `membres` MAL et nombre de `notateurs` ne doivent **jamais** être présentés comme des ventes ou de la rétention.
5. Les analyses de réception (*FMA*, *HxH*, *Red Hood*) reposent sur des **corpus anglophones MAL/Goodreads/Reddit** : les biais de plateforme (et le biais de date, cf. *JJK* 2024) sont documentés dans `Synthese_comparative_4_piliers_vs_Red_Hood.md` — à rappeler avant toute conclusion généralisante.

---

## 10. Pistes de reprise possibles (à proposer, non engagées)

- Étendre la grille D/C/A/B/E aux **titres de la sélection 2020+** (Kagurabachi, Gachiakuta, Sakamoto Days, Dandadan, Frieren…) en réutilisant le pipeline de codage de `codage_critiques_FMA_HxH_hors_anime_anterieur.csv` — l'utilisateur n'a jamais demandé d'aller au-delà des six séries actuelles.
- Croiser le **répertoire de folklore français** (`repertoire_personnages_et_folklore_francais_shonen.json`) avec les pôles B (monde) et C (personnages) pour évaluer la « charge culturelle » d'un projet original.
- Régénérer `dictionnaire_infernal_1825_index_leger_4_tomes.json` sur le parse corrigé (`2 517`).
- Mettre à jour le catalogue MAL et recalculer la sélection > 7,80 sur un millésime plus récent.

---

*Fin du récapitulatif. Toute affirmation de ce document est adossée à un fichier du workspace listé ci-dessus ; en cas de doute, recalculer par script plutôt que citer de mémoire.*
