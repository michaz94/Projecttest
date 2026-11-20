# Analyse des critiques récurrentes et des 5 pôles — *Radiant* (anime saisons 1 et 2, MyAnimeList)

**Date de l'étude** : 5 octobre 2026
**Méthode reprise de** : `Analyse_critiques_recurrentes_FMA_hors_2003.md` et `Analyse_critiques_recurrentes_HxH_hors_1999.md` (même plan : périmètre → verdicts → 5 pôles → table des critiques récurrentes → détail avec citations datées et contre-voix → comparaison).
**Corpus** : les 48 critiques écrites visibles sur MyAnimeList pour *Radiant* (saison 1 : 36, MAL 37202) et *Radiant 2nd Season* (saison 2 : 12, MAL 39355), issues de `radiant_anime_mal_saisons_1_2.json`.
**Filtre demandé** : les phrases qui parlent des épisodes filler du début de la saison 1 sont retirées (18 phrases, listées dans le JSON).

---

## 0. Ce qui est identique à FMA/HxH, ce qui est différent, et ce que je n'ai pas pu reproduire

**Identique** : les 5 pôles et leurs sous-pôles (D1–D4, C, B1–B2, A1–A3, E1–E2), le texte nettoyé des en-têtes de template MAL (`Story: 5/10`, `[characters]`, etc.), la table des critiques récurrentes (total, part dans les *Mixed / Not-Rec*, note moyenne, réactions), les citations datées avec réactions, la contre-voix, le tableau comparatif final.

**Différent** :
- **Pas d'anime antérieur à neutraliser.** Les règles FMA 2003 / HxH 1999 ne s'appliquent pas. Le filtre appliqué ici est celui que tu as demandé (filler du début de la saison 1).
- **Anime seulement.** Pas de critiques MAL du manga ni de Goodreads : le corpus se limite à ce que tu as demandé (anime saisons 1 et 2).
- **Corpus très petit** : 48 critiques, contre 1 097 pour FMA et 897 pour HxH. Voir § 5 pour les marges d'erreur.
- **8 critiques récurrentes au lieu de 6**, parce que l'échantillon est petit et que plusieurs catégories pèsent presque autant.

**Je n'ai pas pu reproduire** : les listes de mots-clés qui ont servi à coder les pôles dans FMA/HxH ne figurent pas dans les dossiers `Others` que j'ai parcourus (j'y ai trouvé les rapports `.md`, le CSV/JSON de codage des critiques et des scripts de collecte, pas les listes de pôles). J'ai donc écrit mes propres listes à partir des définitions des pôles (annexe A). **Les pourcentages de pôles de *Radiant* sont donc comparables à ceux de FMA/HxH en ordre de grandeur seulement.** Les 8 critiques récurrentes sont codées à la main après lecture des 48 textes (comme les catégories de FMA/HxH, qui sont construites à partir du corpus).

---

## 1. Périmètre et répartition globale

### 1.1. Structure du corpus *Radiant* (anime, `N = 48`)

| Sous-corpus | Critiques (`N`) | Mots (texte nettoyé) | *Recommended* | *Mixed Feelings* | *Not Recommended* | Note moyenne (`/10`) | Note médiane | Réactions cumulées | Réactions (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Saison 1 (2018–2019)** | **36** | 13 080 | **22 (61,1 %)** | **8 (22,2 %)** | **6 (16,7 %)** | **6,50** | 7,0 | 553 | 3,0 / 15,4 |
| **Saison 2 (2019–2020)** | **12** | 2 780 | **9 (75,0 %)** | **2 (16,7 %)** | **1 (8,3 %)** | **7,75** | 8,0 | 167 | 8,0 / 13,9 |
| **Total** | **48** | **15 860** | **31 (64,6 %)** | **10 (20,8 %)** | **7 (14,6 %)** | **6,81** | 7,0 | **720** | 4,0 / 15,0 |

Pour mémoire, scores MAL relevés le 5 oct. 2026 : saison 1 = **6,88** (87 105 votes, rang #5557) ; saison 2 = **7,55** (48 999 votes, rang #2009).

Notes de méthode : (a) 3 critiques sans compteur de réactions sont comptées à 0 ; (b) le doublon espagnol d'une critique (`TheDiv`) est retiré du comptage de mots ; (c) trois critiques postées sur la page de la saison 1 parlent aussi de la saison 2 (`maougha`, `MidniteAndBeyond`, `Elyshion`) ; je les ai laissées en saison 1, telles que MAL les classe.

### 1.2. Distribution par verdict et par période

| Verdict / Période | Critiques (`N`) | Part | Note moyenne | Note médiane | Réactions médianes | Réactions moyennes | Max réactions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ***Recommended*** | 31 | **64,6 %** | 8,03 | 8 | 3,0 | 16,6 | 195 (`Karhu`) |
| ***Mixed Feelings*** | 10 | **20,8 %** | 5,50 | 5,5 | 2,5 | 4,8 | 19 (`KingShnebs`) |
| ***Not Recommended*** | 7 | **14,6 %** | 3,29 | 3 | 5,0 | 22,4 | 90 (`Stark700`) |
| **2018–2020** *(diffusion et fin)* | 32 | 66,7 % | **62,5 % Rec** | 21,9 % Mix | 15,6 % NotRec | — | — |
| **2021–2026** *(recul)* | 16 | 33,3 % | **68,8 % Rec** | 18,8 % Mix | 12,5 % NotRec | — | — |

Contrairement à FMA et HxH (où la part de *Recommended* baisse avec le temps), je ne vois pas de recul net chez *Radiant*. Avec 16 critiques tardives, je ne conclus rien de cette différence.

---

## 2. Les 5 pôles et la table des critiques récurrentes

### 2.1. Les 5 pôles (texte nettoyé, part des critiques qui mentionnent le pôle)

| Pôle | *Radiant* S1 (`N = 36`) | *Radiant* S2 (`N = 12`) | ***Radiant* total (`N = 48`)** | Rappel FMA (`N = 1 097`) | Rappel HxH (`N = 897`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Pôle D — Narration, Scénario & Histoire** | 36 (100,0 %) | 12 (100,0 %) | **48 (100,0 %)** | 96,1 % | 97,9 % |
| ↳ `D1` Intrigue, écriture, twists | 35 (97,2 %) | 11 (91,7 %) | **46 (95,8 %)** | 90,7 % | 88,3 % |
| ↳ `D2` Rythme, arcs, exposition | 25 (69,4 %) | 7 (58,3 %) | **32 (66,7 %)** | 42,5 % | 81,4 % |
| ↳ `D3` Dramaturgie, enjeux, ton | 18 (50,0 %) | 6 (50,0 %) | **24 (50,0 %)** | 50,9 % | 53,3 % |
| ↳ `D4` Climax, fin d'arc, résolution | 9 (25,0 %) | 2 (16,7 %) | **11 (22,9 %)** | 36,2 % | 36,5 % |
| **Pôle C — Personnages & antagonistes** | 35 (97,2 %) | 11 (91,7 %) | **46 (95,8 %)** | 61,4 % | 77,7 % |
| **Pôle B — Monde, morale & système** | 21 (58,3 %) | 8 (66,7 %) | **29 (60,4 %)** | 56,2 % | 67,7 % |
| ↳ `B1` Philosophie, morale, discrimination | 17 (47,2 %) | 2 (16,7 %) | **19 (39,6 %)** | 38,6 % | 23,4 % |
| ↳ `B2` Worldbuilding, magie, Inquisition | 18 (50,0 %) | 7 (58,3 %) | **25 (52,1 %)** | 44,0 % | 62,0 % |
| **Pôle A — Visuel strict** | 24 (66,7 %) | 10 (83,3 %) | **34 (70,8 %)** | 59,6 % | 56,4 % |
| ↳ `A1` Style, animation, couleurs | 23 (63,9 %) | 9 (75,0 %) | **32 (66,7 %)** | 57,5 % | 54,5 % |
| ↳ `A2` Esthétique des sorts et créatures | 3 (8,3 %) | 1 (8,3 %) | **4 (8,3 %)** | 3,5 % | 2,7 % |
| ↳ `A3` Chara-design & physique | 11 (30,6 %) | 3 (25,0 %) | **14 (29,2 %)** | 9,9 % | 10,8 % |
| **Pôle E — Action, chorégraphie & tactique** | 18 (50,0 %) | 7 (58,3 %) | **25 (52,1 %)** | 41,0 % | 55,4 % |
| ↳ `E1` Intensité, combats | 18 (50,0 %) | 7 (58,3 %) | **25 (52,1 %)** | 38,8 % | 53,7 % |
| ↳ `E2` Tactique, stratégie, créativité | 2 (5,6 %) | 0 (0,0 %) | **2 (4,2 %)** | 5,6 % | 17,2 % |
| **Ratio Narration / Visuel (`D / A`)** | 1,50× | 1,20× | **1,41×** | 1,61× | 1,74× |
| **Ratio Visuel / Monde (`A / B`)** | 1,14× | 1,25× | **1,17×** | 1,06× | 0,83× |
| *Hors grille (ajout de ma part)* : Son & musique | 15 (41,7 %) | 5 (41,7 %) | 20 (41,7 %) | non mesuré | non mesuré |
| *Hors grille (ajout de ma part)* : Humour | 17 (47,2 %) | 5 (41,7 %) | 22 (45,8 %) | non mesuré | non mesuré |

**Ce que montre le tableau** (observations ; la comparaison avec FMA/HxH est indicative, voir § 0) :
1. **Narration et personnages sont mentionnés dans presque toutes les critiques** (`D = 100 %`, `C = 95,8 %`). Les deux pôles les plus cités sont les mêmes que dans FMA et HxH.
2. **Le visuel pèse plus lourd face au monde que dans FMA/HxH** (`A/B = 1,17×`, contre `1,06×` pour FMA et `0,83×` pour HxH). Pour *Radiant*, l'animation est un sujet de discussion presque aussi fréquent que le worldbuilding. Dans HxH, le monde et le système de Nen devancent le visuel.
3. **La tactique de combat est quasi absente** (`E2 = 4,2 %`), comme dans FMA (`5,6 %`) et loin de HxH (`17,2 %`). Les critiques parlent de combats (`E1 = 52,1 %`) mais presque jamais de leur logique.
4. **Le chara-design (`A3 = 29,2 %`) ressort nettement** (≈ 3× FMA et HxH). Attention : ma liste de mots-clés et celles de FMA/HxH diffèrent, donc l'écart est peut-être en partie artificiel. Dans le texte, les mentions sont partagées, avec plusieurs éloges nets (`Karhu` sur Mélie, `Praetori_Samurai` : *« pass the silhouette test »*, `FishMAL`, `Tenkay`) et quelques critiques (`Flexstyle`, `aoikimahri`).
5. **Le thème de la discrimination (`B1`) est beaucoup moins cité en saison 2** (2 critiques sur 12, contre 17 sur 36). Avec 12 critiques, c'est une observation, pas une tendance établie.

### 2.2. Table de codage des critiques récurrentes

*Couverture : ces 8 catégories couvrent 17 des 17 critiques mitigées ou négatives (*Mixed* + *Not-Rec*). C'est automatique, puisque les catégories sont construites à partir de ces mêmes 48 textes. Elles couvrent aussi des réserves exprimées dans 20 des 31 critiques *Recommended* (64,5 %).*

| Rang & catégorie | Total (`N = 48`) | S1 / S2 | Part dans les *Mixed / Not-Rec* (`N = 17`) | Note moyenne (tous) | Note moyenne (*Mix/NotRec*) | Réactions *Mix/NotRec* (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1. Démarrage lent / rythme inégal** (≈ 10 premiers épisodes ou 1re moitié de S1 ; lenteur de S2) | **24 (50,0 %)** | 22 / 2 | 8 / 17 (47,1 %) | 6,54 | 4,12 | 4,0 / 19,9 |
| **C2. Héros (Seth) et/ou casting jugés génériques, bêtes ou irritants** | **23 (47,9 %)** | 20 / 3 | **14 / 17 (82,4 %)** | 5,65 | 4,57 | 4,0 / 13,9 |
| **C3. Dérivatif / « shōnen standard »** (*Naruto*, *One Piece*, *Black Clover*, *Fairy Tail*) | **19 (39,6 %)** | 17 / 2 | 13 / 17 (76,5 %) | 5,37 | 4,46 | 4,0 / 13,5 |
| **C4. Ton enfantin et/ou humour qui casse la tension ou tombe à plat** | **9 (18,8 %)** | 8 / 1 | 6 / 17 (35,3 %) | 4,89 | 3,67 | 3,5 / 17,5 |
| **C5. Animation / visuel jugé moyen, plat ou paresseux** | **8 (16,7 %)** | 7 / 1 | 5 / 17 (29,4 %) | 5,38 | 3,80 | 4,0 / 28,2 |
| **C6. Surexplication, bavardage, objectif répété** | **7 (14,6 %)** | 6 / 1 | 4 / 17 (23,5 %) | 5,43 | 4,25 | 5,5 / 5,8 |
| **C7. Enjeux faibles, incohérences de la logique du monde** | **7 (14,6 %)** | 6 / 1 | 5 / 17 (29,4 %) | 4,57 | 3,60 | 4,0 / 6,2 |
| **C8. Adaptation jugée appauvrie par rapport au manga** | **5 (10,4 %)** | 4 / 1 | 2 / 17 (11,8 %) | 6,60 | 5,00 | 2,0 / 2,0 |

*Effet du filtre « filler du début de la saison 1 »* : trois critiques de la saison 1 (`TheDiv`, `demetri_123`, `gbrain`) n'avaient comme seule phrase sur la lenteur une phrase mentionnant le filler ; elles n'entrent donc plus dans **C1** (sans le filtre : 27 au lieu de 24). Plusieurs phrases proches (« 10 premiers épisodes pas terribles », « aventures sans rapport avec l'intrigue ») ne contiennent pas le mot *filler* et sont donc conservées ; elles ne changent aucune ligne du tableau.

---

## 3. Analyse détaillée des critiques récurrentes

*Les citations sont en anglais (texte original). Format : pseudo (saison, verdict, date, note, réactions).*

### 3.1. Critique n°1 — Démarrage lent (`50,0 %` du corpus ; `47,1 %` des *Mixed/Not-Rec*)

* **Ce qui est reproché** : la saison 1 est jugée lente à démarrer. Beaucoup situent le vrai départ vers l'épisode 10-11 (arc Rumble Town). Dans la saison 2, seules 2 critiques parlent de lenteur (`therealab`, `GosuDRM`).
* **Citations** :
  * `Flexstyle` (S1, *Not Recommended*, 28 févr. 2019, `3/10`, **45 réactions**) : *« Radiant only starts to get good during its first arc- Rumble Town at ep.11. »*
  * `Zonticore` (S1, *Recommended*, 4 oct. 2019, `8/10`, 2 réactions) : *« for the first 10 or so episodes the show is really not that great. But then the story picks up »*
  * `Jpk8` (S1, *Recommended*, 17 juin 2022, `8/10`, 2 réactions) : *« this anime does have a rather slow and boring start but just power through it »*
  * `therealab` (S2, *Recommended*, 5 mai 2024, `8/10`, 0 réaction) : *« Depth increased at the cost of pace. »*
* **Contre-voix** : **15 des 36 critiques de la saison 1** disent que la série « décolle » après environ 10 épisodes ou dans sa seconde moitié (ex. `Astagami` : *« The Rumble Town Arc is what makes Radiant good »*). Ce n'est pas un défaut qui fait fuir : la plupart de ces critiques sont *Recommended*. Ce n'est pas non plus un défaut mineur : c'est le premier défaut cité.

### 3.2. Critique n°2 — Héros et casting génériques ou irritants (`47,9 %` ; **`82,4 %` des *Mixed/Not-Rec***)

* **Ce qui est reproché** : Seth est décrit comme un héros de shōnen sans relief, bruyant ou « bête ». Doc est jugé répétitif. Le casting secondaire est jugé joli mais sans personnalité (`ZB_Blades`). C'est la catégorie qui pèse le plus parmi les critiques négatives.
* **Citations** :
  * `Stark700` (S1, *Not Recommended*, 23 févr. 2019, `4/10`, **90 réactions**) : *« Seth is about as one dimensional as he can get. »*
  * `maougha` (S1, *Mixed Feelings*, 5 janv. 2020, `6/10`, 2 réactions) : *« The main character is just too dumb. »*
  * `KyomaBritannia` (S2, *Mixed Feelings*, 7 juil. 2022, `6/10`, 1 réaction) : *« Seth is similar to Naruto in that he's dumb but wants to help his friends, only turned up to an almost unbearable level. »*
* **Contre-voix** : `FishMAL` (S1, *Recommended*) : *« The rest of the group is totally different and actually has interesting personalities. »* ; `CrumbleGarden` (S1, *Recommended*) : *« The characters are easily the best part of this show. »* Plusieurs critiques disent que Seth s'améliore dans la seconde moitié (`Stytch`, `CrumbleGarden`, `Praetori_Samurai`) ou en saison 2 (`lenompasbanal` : *« Seth loses some of his brattiness »*).

### 3.3. Critique n°3 — Dérivatif / « shōnen standard » (`39,6 %` ; `76,5 %` des *Mixed/Not-Rec*)

* **Ce qui est reproché** : ressemblance avec *Naruto*, *One Piece*, *Black Clover*, *Fairy Tail* ; trames, gags et ressorts jugés connus. La catégorie pèse bien plus que le « classicisme shōnen » de FMA (`7,9 %`) ou le « overrated » de HxH (`6,1 %`). Les définitions ne sont pas identiques (celle de FMA vise surtout le méchant final et l'épilogue), donc je compare l'ordre de grandeur, pas les chiffres.
* **Citations** :
  * `Flexstyle` (S1, *Not Recommended*, 28 févr. 2019, `3/10`, **45 réactions**) : *« Radiant is the spiritual successor to Black Clover. »*
  * `ZB_Blades` (S1, *Mixed Feelings*, 23 févr. 2019, `6/10`, 4 réactions) : *« Instead, I got just another cliche ridden shounen. »*
  * `MidniteAndBeyond` (S1, *Not Recommended*, 27 déc. 2024, `5/10`, 4 réactions) : *« This show wanted to be One Piece SO badly. »*
* **Contre-voix** : plusieurs critiques positives acceptent la formule (`lenompasbanal`, S2 : *« Radiant only picked the good ones »*, à propos des stéréotypes shōnen) ; d'autres soulignent des éléments qui s'écartent du moule : la discrimination des sorciers (voir § 3.9).

### 3.4. Critique n°4 — Ton enfantin, humour qui casse la tension (`18,8 %` ; `35,3 %` des *Mixed/Not-Rec*)

* **Ce qui est reproché** : l'humour est jugé enfantin ou mal placé ; le sérieux du héros n'est pas crédible dans un ton léger. À noter que l'humour est aussi cité positivement (`Karhu`).
* **Citations** :
  * `nokinoks` (S1, *Not Recommended*, 2 mars 2019, `3/10`, 5 réactions) : *« The show doesn't take itself seriously at all, but wants us to take the protagonist seriously. »*
  * `charliechuckle` (S1, *Not Recommended*, 31 déc. 2019, `3/10`, 2 réactions) : *« The comedy ruins the pacing of the show when used in serious situations, and they do it often. »*
* **Contre-voix** : `Karhu` (S1, *Recommended*, 24 févr. 2019, `7/10`, **195 réactions**, la critique la plus approuvée du corpus) : *« Its strong sides lie within the light comedy and world building. »* 22 critiques sur 48 mentionnent l'humour (liste de mots-clés) ; le même registre est loué par les uns et blâmé par les autres.
* **Rapprochement avec le corpus FMA** : c'est le défaut n°2 de FMA (humour *chibi*, `10,4 %` du corpus). Ici il pèse 18,8 %.

### 3.5. Critique n°5 — Animation moyenne ou paresseuse (`16,7 %` ; `29,4 %` des *Mixed/Not-Rec*)

* **Citations** :
  * `Flexstyle` (S1) : *« I despise how bland all the spells look like green sparkles. »*
  * `Zonticore` (S1, *Recommended*, 4 oct. 2019, `8/10`, 2 réactions) : *« it just end up looking lazy and bad »* (à propos d'une technique d'animation des scènes rapides).
  * `Astagami` (S1, *Recommended*, 2 mai 2020, `8/10`, 4 réactions) : *« Radiant does not have the best animation, it's average at best. »*
* **Contre-voix** : `Zerity` (S1, *Recommended*, 23 févr. 2019, `9/10`, **62 réactions**) : *« The animation is very strong from start to finish. »* ; le pôle visuel est cité par 70,8 % des critiques, souvent positivement. Un avis lie ce défaut au manga (voir § 3.8).

### 3.6. Critique n°6 — Surexplication, bavardage, objectif répété (`14,6 %` ; `23,5 %` des *Mixed/Not-Rec*)

* **Ce qui est reproché** : le héros annonce son but à chaque épisode, l'introduction réexplique la série, les personnages parlent beaucoup. C'est le même type de reproche que la critique n°5 de FMA (exposition *tell don't show*, `3,5 %` du corpus intrinsèque) et que la critique n°1 de HxH (narrateur omniprésent, `27,4 %` du corpus), à une échelle intermédiaire.
* **Citations** :
  * `Zryn` (S1, *Mixed Feelings*, 23 févr. 2019, `6/10`, 10 réactions) : *« an unneeded time waster of an opening explaining the show to us every episode LOL »*
  * `Hyouron` (S1, *Recommended*, 11 avr. 2020, `7/10`, 1 réaction) : *« every episode Seth would announce how determined he was to go to Radiant »*
  * `demetri_123` (S1, *Recommended*, 21 mars 2022, `7/10`, 0 réaction) : *« there is a lot of unnecessary dialogue with not enough action »*
* **Contre-voix** : `Elyshion` (S1, *Recommended*, 22 avr. 2026) apprécie au contraire les explications pendant les eyecatch ; la même fonction est donc lue de deux façons.

### 3.7. Critique n°7 — Enjeux faibles et logique du monde (`14,6 %` ; `29,4 %` des *Mixed/Not-Rec*)

* **Citations** :
  * `Disfemisef` (S1, *Recommended*, 21 juin 2020, `7/10`, 1 réaction) : *« sorcerers are hated for the powers they possess, however, the inquisitors (the team that hunts them) also have weird powers, but aren't feared by the people »*
  * `aoikimahri` (S1, *Not Recommended*, 14 mai 2020, `1/10`, 4 réactions) : *« There are no real consequences after all. »*
* **Contre-voix** : en saison 2, `Disfemisef` écrit : *« Radiant S2 had stakes. There were consequences for what they fought for. »* (S2, *Recommended*, 29 juin 2020, `8/10`, 9 réactions). La même personne (`Disfemisef`) relevait en saison 1 des incohérences de logique, et loue en saison 2 des enjeux réels.

### 3.8. Critique n°8 — Adaptation jugée appauvrie par rapport au manga (`10,4 %` ; `11,8 %` des *Mixed/Not-Rec*)

* **Ce qui est reproché** : ton plus enfantin, personnages simplifiés, couleurs moins vives, rythme plus lent que le manga. Ce sont des lecteurs du manga ; dans FMA et HxH, la comparaison avec l'ancien anime concernait 26,3 % et 9,6 % des critiques négatives, ici 2 critiques *Mixed/Not-Rec* sur 17 (11,8 %).
* **Citations** :
  * `Oriotiar` (S1, *Mixed Feelings*, 5 avr. 2019, `5/10`, 3 réactions) : *« the anime is mediocre and as an adaptation it's trash »*
  * `LizzieMallow` (S1, *Mixed Feelings*, 24 juin 2022, `5/10`, 1 réaction) : *« The anime is slow. Like, Naruto-level slow. »*
  * `Praetori_Samurai` (S1, *Recommended*, 20 févr. 2021, `8/10`, 1 réaction) : *« As a manga adaptation - 4/10 (manga always had really pretty and vibrant color pages whereas the anime art mostly feels flat) »*
* **Contre-voix** : `nnidorion` (S1, *Recommended*, 24 juin 2020, `9/10`) défend l'anime en soi et attribue la note MAL basse à des spectateurs déçus par l'adaptation. C'est son interprétation, que le corpus ne permet pas de vérifier.

### 3.9. Ce qui est loué le plus souvent (contre-voix d'ensemble)

* **« Ça décolle » après environ 10 épisodes** : 15 critiques de la saison 1 sur 36.
* **La saison 2 est jugée meilleure que la saison 1** : 8 des 12 critiques de la saison 2 le disent, plus 2 critiques de la page de la saison 1 (`Praetori_Samurai`, `Elyshion`). Une seule critique de la saison 2 (`therealab`) la juge plus lente. Exemple : `gumpngreen` (S2, *Recommended*, 29 janv. 2020, `8/10`, **45 réactions**) : *« The new story arc gives the characters much-needed emotional depth and develops the plot with some twists. »*
* **La discrimination des sorciers** : `Zerity` (S1, *Recommended*) : *« One thing I like about this anime is how they deal with the discrimination against sorcerers. »* ; `gbrain` (S1, *Recommended*, 10 déc. 2019, `8/10`, 2 réactions) : *« the content of its first season is surprisingly relevant to modern political problems »*.
* **L'opening** : cité par `Karhu`, `ZB_Blades` (*« The opening song alone is straight fire »*) et d'autres ; le pôle son/musique est mentionné par 41,7 % des critiques.

---

## 4. Tableau comparatif : FMA (hors 2003) vs HxH (hors 1999) vs *Radiant* (anime)

| Dimension | *Fullmetal Alchemist* (`N = 1 097`) | *Hunter × Hunter* (`N = 897`) | *Radiant* anime (`N = 48`) |
| :--- | :--- | :--- | :--- |
| **Verdicts favorables** | **91,0 %** — note moy. **9,02 / 10** | **88,4 %** — note moy. **8,83 / 10** | **64,6 %** — note moy. **6,81 / 10** (S1 6,50 ; S2 7,75) |
| **Pôle D — Narration** | **96,1 %** (D2 rythme `42,5 %`) | **97,9 %** (D2 rythme `81,4 %`) | **100 %** (D2 rythme `66,7 %`) |
| **Pôle C — Personnages** | **61,4 %** | **77,7 %** | **95,8 %** |
| **Pôle B — Monde / système** | **56,2 %** | **67,7 %** | **60,4 %** |
| **Pôle A — Visuel** | **59,6 %** | **56,4 %** | **70,8 %** |
| **Pôle E — Action** | **41,0 %** (E2 `5,6 %`) | **55,4 %** (E2 `17,2 %`) | **52,1 %** (E2 `4,2 %`) |
| **Ratios `D/A` et `A/B`** | `1,61×` ; `1,06×` | `1,74×` ; `0,83×` | `1,41×` ; `1,17×` |
| **Critique n°1** | Rythme début/Briggs (`31,0 %`) | Lenteur/narrateur de *Chimera Ant* (`27,4 %`) | Démarrage lent (`50,0 %`) |
| **Critique n°1 chez les mitigés/négatifs** | Rythme (`37,0 %`) | Lenteur/narrateur (`58,5 %`) | **Héros/casting générique (`82,4 %`)** |
| **Critique de « classicisme »** | `7,9 %` (méchant final, épilogue) | `6,1 %` (« overrated ») | **`39,6 %`** (dérivatif, shōnen standard) |

**Lecture (mienne, à ne pas prendre pour un fait)** :
- Dans FMA et HxH, les reproches portent surtout sur des choix précis (rythme d'un arc, narrateur, humour). Chez *Radiant*, les deux plus gros reproches chez les mitigés et négatifs (héros générique `82,4 %`, dérivatif `76,5 %`) visent l'identité même de la série. Ce n'est pas la même nature de défaut.
- Dans le corpus, le défaut le plus cité (démarrage lent, `50,0 %`) coexiste avec une contre-voix très répandue (« ça décolle après 10 épisodes », 15 critiques sur 36). Les verdicts restent majoritairement favorables (`64,6 %`).
- **Écarts à garder en tête** : taille du corpus (48 contre 897 et 1 097), anime seulement (FMA et HxH incluent des critiques du manga), listes de mots-clés différentes pour les pôles.

---

## 5. Limites et marges d'erreur

- **Taille** : avec `N = 48`, une part de 50 % a une marge d'environ ±14 points (intervalle de confiance à 95 %). Pour la saison 2 seule (`N = 12`), la marge est d'environ ±28 points : je n'interprète pas les écarts S1/S2 des pôles.
- **Échantillon non aléatoire** : ce sont les critiques visibles sur MAL (36 et 12 critiques écrites), alors que les scores MAL reposent sur 87 105 et 48 999 votes.
- **Pôles** : codés par mots-clés (annexe A) ; une mention n'indique ni un jugement positif ni négatif. Les 8 critiques C1–C8 sont codées à la main (fichier de codage joint).
- **Filtre filler** : appliqué comme défini dans le JSON (18 phrases) ; effet sur C1 mesuré au § 2.2.
- **Pas de lecture de l'œuvre** : ces chiffres décrivent les avis des spectateurs de l'anime (2018–2020), pas le manga.

---

## Annexe A — Listes de mots-clés des pôles (anglais, insensibles à la casse)

- `D1` : story, plot, writing/written, screenplay, twist, narrative, premise, script, dialogue, foreshadow, mystery
- `D2` : pace/pacing/paced, slow…, sluggish, drag, arc(s), exposition, explain…, first half/few/ten, ep N, stretch, rushed, runtime, beginning, intro, introduction
- `D3` : stakes, consequence(s), tragic, dark, serious…, emotion…, tone, mature, death(s), betray…, intens…, angst, drama…, heartfelt, moving, depth
- `D4` : climax, ending, finale, conclusion, resolution, cliffhanger, payoff, epilogue, final arc/episode, last episode, end of the season, (de)escalation
- `C` : character(s), protagonist, MC, villain, antagonist, Seth, Mélie, Doc, Grimm, Alma, Dragunov, Konrad, cast, hero, sidekick, supporting, personality
- `B1` : discriminat…, racis…, xenophob…, bigot…, persecut…, outcast, oppress…, minority, prejudice, stigma…, infected, moral…, grey, ostraci…, equality, acceptance, social commentary, political, injustice, immigrant, hated
- `B2` : world, worldbuilding, magic/power system, setting, lore, Inquisition, hierarchy, universe, mechanics, spell(s), curse(s), faction
- `A1` : art, artwork, art style, animation, visuals, color/colour, palette, Lerche, CGI, drawn, drawing, backgrounds, frames
- `A2` : spell effects, sparkles, particles, aura, gore, creature/monster design, blobs of color, lightsabers
- `A3` : (character) design(s), silhouette, costume, outfit, clothes, fashion, hair, appearance, horns, haired
- `E1` : fight(s), fighting, battle(s), combat, action, choreograph…, punch…, war, clash
- `E2` : tactic…, strateg…, bluff, outsmart…, clever…, creative…, inventive, ingenious
- Hors grille : Son (sound, music, OST, opening, ending song, voice, seiyuu, soundtrack) ; Humour (humor, comedy, joke, funny, gag, punchline)

Fichiers de travail : `radiant_analyse/codage_critiques_radiant_anime_MAL.csv` (codage ligne par ligne), `…json`, `radiant_analyse/codage.py` et `analyse.py` (listes et calculs).
