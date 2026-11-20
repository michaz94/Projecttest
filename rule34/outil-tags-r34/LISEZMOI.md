# Outil de classement des tags Character (Rule34.xxx) — dossier récupéré

Récupéré le 23 oct. 2026 à partir de tes fichiers. Aucune nouvelle collecte n'a été faite sur Rule34.

- `notebooks/` : ton notebook Colab (`Outil_tags_reprise_107_Colab.ipynb`), la variante `Classement_import_ZIP_reprise.ipynb`, le script `collecteur_tags.py`, ton LIRE_MOI d'origine et les CSV du 27 sept. 2026 (42 tags, 21 personnages féminins).
- `donnees/` : **dossier perdu (constaté le 24/10/2026)**. Il contenait les 5 exports ZIP du 27 sept. 2026 décompressés (pages 1 à 107) et les fichiers par bloc des relevés 108 à 250. Rien d'utile n'est perdu : le dernier export, cumulatif (42 tags Character des pages 1 à 107), reste dans `notebooks/dernier_export_2026-09-27.zip` avec `notebooks/classement_42_tags_2026-09-27.csv`, et tous les tags relevés sur les pages 108 à 250 sont dans `selection_172_personnages_feminins_2026-10-23.csv` et `autres_tags_personnages_124_hors_feminins_2026-10-23.csv` (colonne `source` = bloc de pages). Les chemins `donnees/releve_pages_…` cités plus bas n'existent donc plus.
- `comparaison_r34_danbooru_2026-10-23.csv` : tes 21 personnages féminins, avec le nombre de posts sur Danbooru (relevé de l'IA le 23 oct. 2026 via l'API publique `tags.json` ; alias résolus : 2B = `2b_(nier:automata)`, Ochako = `uraraka_ochaco`, etc.) et le ratio r34/Danbooru.

Limites :
- Les deux relevés n'ont pas la même date (27 sept. et 23 oct.).
- Danbooru vise surtout le style anime : les personnages occidentaux y sont sous-représentés. Le ratio mesure donc à la fois l'attrait sexuel et l'origine (Japon ou Occident).
- Les compteurs Danbooru incluent toutes les classifications (pas seulement les images tout public).

- `tiermaker/` : test de corrélation entre le classement communautaire TierMaker (« Ultimate Fictional Animated Women ») et les nombres de tags (23 oct. 2026). Voir `tiermaker/RAPPORT_correlation_2026-10-23.md`.

## Relevé des pages 108 à 118 (23 octobre 2026)
Fait par l'IA avec un outil de lecture de pages web, sur les mêmes tableaux triés que le notebook (`pid` 2140 à 2340). Les pages 106 et 107 ont aussi été vérifiées : elles ne contiennent aucun nouveau tag Character, donc la suite de l'ancienne collecte est continue. Résultat : **13 tags Character**, dont 3 catégories Pokémon. Fichiers dans `donnees/releve_pages_108-118_2026-10-23/` :
- `tags_personnages_pages_108-118.csv` ;
- `classement_55_tags_fusion.csv`, qui fusionne les 42 anciens tags (27 sept.) et les 13 nouveaux (23 oct.). Les compteurs n'ont pas tous la même date.

## Relevé des pages 119 à 128 (23 octobre 2026)
Même méthode (`pid` 2360 à 2540). Résultat : **8 tags Character**. Parmi eux, `rumi_usagiyama` est le vrai nom de Miruko, donc un doublon non fusionné, et `draenei` est une espèce de Warcraft. Fichiers dans `donnees/releve_pages_119-128_2026-10-23/` : `tags_personnages_pages_119-128.csv` et `classement_63_tags_fusion.csv` (42 + 13 + 8 tags, dates mélangées).

## Relevé des pages 129 à 138 (23 octobre 2026)
Même méthode (`pid` 2560 à 2740). Résultat : **16 tags Character** : 9 personnages féminins, 2 doublons (`yor_forger` pour Yor, `rachel_roth` pour Raven) et 5 espèces (Noctali, Lockpin, elfe de la nuit, yordle, inkling). Fichiers dans `donnees/releve_pages_129-138_2026-10-23/` : `tags_personnages_pages_129-138.csv` et `classement_79_tags_fusion.csv` (dates mélangées).

## Relevé des pages 139 à 150 (23 octobre 2026)
Même méthode (`pid` 2760 à 2980). Résultat : **21 tags Character** : 12 personnages féminins, 2 masculins (Bowser, Spider-Man), 1 doublon (`uzumaki_hinata`) et 6 catégories ou espèces. On y voit aussi que `kim_possible` est classé **Copyright** (la série) : le tag du personnage est `kimberly_ann_possible`. Fichiers dans `donnees/releve_pages_139-150_2026-10-23/` : `tags_personnages_pages_139-150.csv` et `classement_100_tags_fusion.csv` (dates mélangées).

## Relevé des pages 151 à 160 (23 octobre 2026)
Même méthode (`pid` 3000 à 3180). Résultat : **20 tags Character** : 13 personnages féminins et 7 catégories ou espèces (anonymous_male, elfe de sang, Nymphali, champions d'arène, gemme, koopa, Mystimaniac). Fichiers dans `donnees/releve_pages_151-160_2026-10-23/` : `tags_personnages_pages_151-160.csv` et `classement_120_tags_fusion.csv` (dates mélangées).

## Relevé des pages 161 à 170 (23 octobre 2026)
Même méthode (`pid` 3200 à 3380). Résultat : **15 tags Character** : 11 personnages féminins, 1 masculin (Astolfo), 1 doublon (`lara_croft_(survivor)`, la version reboot 2013 de Lara Croft, qui a déjà son tag `lara_croft`) et 2 espèces (Aquali, Octaling). La page 164 ne contient aucun tag Character. Fichiers dans `donnees/releve_pages_161-170_2026-10-23/` : `tags_personnages_pages_161-170.csv` et `classement_135_tags_fusion.csv` (dates mélangées).

## Relevé des pages 171 à 180 (23 octobre 2026)
Même méthode (`pid` 3400 à 3580). Résultat : **17 tags Character** : 11 personnages féminins, 1 personnage qui existe en version homme et femme (Byleth, non compté), 2 doublons (`misty_(pokemon)`, 2e tag de Misty après `kasumi_(pokemon)` ; `spider-gwen`, variante de Gwen Stacy) et 3 espèces ou catégories (Givrali, Pokémon de 8e génération, Zoroark). La page 173 ne contient aucun tag Character. À noter : `hinata_hyuuga` (15 686, page 177) est classé General, pas Character, et `arcane` (15 329, page 180) est classé Copyright. Fichiers dans `donnees/releve_pages_171-180_2026-10-23/` : `tags_personnages_pages_171-180.csv` et `classement_152_tags_fusion.csv` (dates mélangées).

## Relevé des pages 181 à 190 (23 octobre 2026)
Même méthode (`pid` 3600 à 3780). Résultat : **21 tags Character** : 16 personnages féminins, 1 masculin (Son Goku), 1 doublon (`felicia_hardy`, nom civil de Black Cat) et 3 espèces ou catégories (Dracaufeu, avatar Roblox, Roussil). Toutes les pages contiennent au moins un tag Character. Fichiers dans `donnees/releve_pages_181-190_2026-10-23/` : `tags_personnages_pages_181-190.csv` et `classement_173_tags_fusion.csv` (dates mélangées).

## Relevé des pages 191 à 200 (23 octobre 2026)
Même méthode (`pid` 3800 à 3980). Résultat : **14 tags Character** : 10 personnages féminins (dont Dawn et Sarada Uchiha, d'abord écartées comme enfants puis ajoutées à la demande de l'utilisateur), 1 masculin (Shadow), 1 doublon (`peter_parker`, nom civil de Spider-Man), 1 catégorie (Pokémon de 9e génération) et 1 espèce (Au Ra). Les pages 192 et 198 ne contiennent aucun tag Character. Fichiers dans `donnees/releve_pages_191-200_2026-10-23/` : `tags_personnages_pages_191-200.csv` et `classement_187_tags_fusion.csv` (dates mélangées).

## Relevé des pages 201 à 210 (23 octobre 2026)
Même méthode (`pid` 4000 à 4180). Résultat : **22 tags Character** : 9 personnages féminins, 4 masculins (Venom, Nick Wilde, Foxy, Luffy), 5 doublons ou variantes (`emma_frost_(marvel_rivals)`, `zero_suit_samus`, `zelda_(tears_of_the_kingdom)`, `haruno_sakura`, `mirko`) et 4 espèces ou catégories (asari, Brutocollinus, inkling fille, togruta). La page 202 ne contient aucun tag Character. Fichiers dans `donnees/releve_pages_201-210_2026-10-23/` : `tags_personnages_pages_201-210.csv` et `classement_209_tags_fusion.csv` (dates mélangées).

## Relevé des pages 211 à 220 (23 octobre 2026)
Même méthode (`pid` 4200 à 4380). Résultat : **18 tags Character** : 10 personnages féminins (dont Yamato, comptée comme fille à la demande de l'utilisateur), 1 masculin (Cloud Strife), 4 doublons (`uraraka_ochako`, `diana_prince`, `zelda_(breath_of_the_wild)`, `kara_zor-el`) et 3 espèces (protogen, Arcanin, Pyrobut). La page 216 ne contient aucun tag Character. Fichiers dans `donnees/releve_pages_211-220_2026-10-23/` : `tags_personnages_pages_211-220.csv` et `classement_227_tags_fusion.csv` (dates mélangées).

## Relevé des pages 221 à 230 (23 octobre 2026)
Même méthode (`pid` 4400 à 4580). Résultat : **22 tags Character** : 10 personnages féminins (dont `byleth_(fire_emblem)_(female)`, la version féminine de Byleth), 3 masculins (Mario, Wise, Fox McCloud), 3 doublons (`ankha_(animal_crossing)`, `imp_midna`, `jill_valentine_(sasha_zotova)`), 3 tags pour la même créature SCP-1471 / MalO (genre non défini, non comptée) et 3 espèces ou catégories (dresseur Pokémon, humain de Warcraft, vastaya). Les pages 227 et 229 ne contiennent aucun tag Character. Fichiers dans `donnees/releve_pages_221-230_2026-10-23/` : `tags_personnages_pages_221-230.csv` et `classement_249_tags_fusion.csv` (dates mélangées).

## Relevé des pages 231 à 240 (23 octobre 2026)
Même méthode (`pid` 4600 à 4780). Résultat : **26 tags Character** : 15 personnages féminins (dont Cream the Rabbit, d'abord écartée comme enfant puis ajoutée à la demande de l'utilisateur), 2 masculins (Katsuki Bakugo, Jotaro Kujo), 1 personnage au genre non défini dans son œuvre (Kris, Deltarune), 1 tag de plus pour la créature SCP-1471 / MalO (`malo`, non comptée), 3 doublons (`ellie_williams`, `elastigirl` pour Helen Parr, `sue_storm` pour la Femme invisible), 3 espèces (Mentali, Worgen, Absol) et 1 tag ambigu (`the_avatar`, sans précision sur le personnage visé). Toutes les pages contiennent au moins un tag Character. Fichiers dans `donnees/releve_pages_231-240_2026-10-23/` : `tags_personnages_pages_231-240.csv` et `classement_275_tags_fusion.csv` (dates mélangées).

## Relevé des pages 241 à 250 (23 octobre 2026)
Même méthode (`pid` 4800 à 4980). Résultat : **21 tags Character** : 12 personnages féminins (dont Mythra, autre forme de Pyra, comptée à part, et Toph Beifong, ajoutée à la demande de l'utilisateur), 1 personnage homme ou femme au choix du joueur (Commandant Shepard, non compté), 2 masculins (Ralsei, Spike), 1 doublon (`midoriya_izuku`, déjà `izuku_midoriya`) et 5 espèces ou catégories (Lougaroc, Miascarade, changelin, méga-évolution, Braségali). Toutes les pages contiennent au moins un tag Character. Fichiers dans `donnees/releve_pages_241-250_2026-10-23/` : `tags_personnages_pages_241-250.csv` et `classement_296_tags_fusion.csv` (dates mélangées).


## Relevé des pages 251 à 260 (24 octobre 2026) — dossier `releves/releve_pages_251-260_2026-10-24/`
Même méthode (`pid` 5000 à 5180), relevé fait le 24/10 (les blocs précédents datent du 23/10 ; contrôle de continuité sur la page 250 : mêmes tags qu'au relevé précédent). Résultat : **27 tags Character** : 15 personnages féminins, 4 masculins (Batman, Ritsuka Fujimaru version masculine, Boyfriend, Asriel), 1 duo de genre mixte (Kindred, non compté), 4 doublons (`karen_starr` = Power Girl, `yoruichi_shihouin` = Yoruichi, `miles_prower` = Tails, `link_(breath_of_the_wild)` = Link) et 3 espèces ou catégories (forme régionale Pokémon, Phyllali, Viera). Toutes les pages contiennent au moins un tag Character.
- `tags_personnages_pages_251-260.csv` : les 27 tags (avec le numéro de page) ; `unions_pages_251-260.csv` : 7 recherches OU (même méthode que `doublons/`) ; `construire.py` : reproduit tous les fichiers ci-dessous.
- `selection_187_personnages_feminins_2026-10-24.csv` (racine) : la sélection 172 + les 15 nouvelles, tag seul, sans déduplication (rangs 173 à 187).
- `autres_tags_personnages_136_hors_feminins_2026-10-24.csv` (racine) : les 124 autres tags + les 12 du bloc.
- `doublons/selection_188_dedupliquee_2026-10-24.csv` : la sélection dédupliquée 173 + 15 ; Yoruichi passe à l'union avec `yoruichi_shihouin` (21 936 → ≈ 25 389, +15,7 %, rang 47 → 35) et Power Girl à l'union avec `karen_starr` (+1,5 %) ; Asuna (+9,4 %), Sadako (+4,5 %) et Ilulu (+2,7 %) sont comptées par union ; Rebecca et Kasane Teto restent au tag seul (écart dans le bruit).
- Limite : `yoruichi_shihouin` (9 281) était sous le seuil des pages 1-250, d'où sa découverte tardive ; d'autres doublons de cette taille peuvent encore apparaître dans les pages suivantes.

## Relevé des pages 261 à 270 (24 octobre 2026) — dossier `releves/releve_pages_261-270_2026-10-24/`
Même méthode (`pid` 5200 à 5380), même jour que le bloc 251-260 (continuité vérifiée : la page 261 commence à 9 124, juste sous Viera à 9 125). Résultat : **22 tags Character** : 17 personnages féminins, aucun masculin, 2 doublons (`selina_kyle` = Catwoman, `invisible_woman_(marvel_rivals)` = Femme invisible) et 3 espèces ou catégories (Voltali, mutant Marvel, Team Rocket). La page 266 ne contient aucun tag Character.
- `tags_personnages_pages_261-270.csv`, `unions_pages_261-270.csv` (8 recherches OU), `construire.py`.
- `selection_204_personnages_feminins_2026-10-24.csv` (racine) : 187 + 17, tag seul (rangs 188 à 204).
- `autres_tags_personnages_141_hors_feminins_2026-10-24.csv` (racine) : 136 + 5.
- `doublons/selection_205_dedupliquee_2026-10-24.csv` : 188 + 17 ; Akali (+11,4 %), Nezuko (+9,2 %), Kobeni (+4,0 %) et Sona (+4,0 %) comptées par union. Catwoman ∪ `selina_kyle` (+144), Femme invisible ∪ version Marvel Rivals (+41), Serena et Makoto : écarts dans le bruit, donc inchangées. La version Marvel Rivals de la Femme invisible est presque toujours étiquetée aussi `invisible_woman`.
- L'Agneau (`lamb_(league_of_legends)`) est comptée comme personnage féminin ; le tag `kindred` (duo Agneau + Loup) reste non compté.

## Classement par médium v3 (24 octobre 2026) — dossier `classement_par_medium/`
`classer_v3.py` → `classement_r34_par_medium_2026-10-24.csv` / `.md` : base = `doublons/selection_205_dedupliquee_2026-10-24.csv` (pages 1-270, compteurs du 24/10, doublons comptés par union). Même règles que la v2 ; nouvelles Furry : Sally Acorn, Nicole Watterson, Susie, Coco Bandicoot, Millie (à confirmer, diablotine) et l'Agneau (indice estimé via `kindred_(lol)`). La v2 du 23/10 est conservée.

**Mise à jour du 24/10 (demande de l'utilisateur) :** Raven et Starfire, créées dans les comics (1980), sont déplacées en Cartoons / films d'animation occidentaux, car leur popularité sur rule34 vient surtout de la série Teen Titans (2003). Indice pour Raven : `purple_hair` sur 52 % de ses publications, contre 2,5 % pour `black_hair` sans `purple_hair`. Comics : 10 personnages / 149 654 publications ; Cartoons : 22 / 344 465.

## Effet d'une adaptation (24 octobre 2026) — dossier `effet_adaptation/`
`danbooru_avant_apres.py` → `danbooru_avant_apres_2026-10-24.json` : publications Danbooru 12 mois avant / 12 mois après la sortie d'une adaptation (date d'envoi), par million de publications du site sur la même période. rule34 n'a pas de filtre par date, d'où Danbooru. Résultats (multiplicateur) : Marin ×229, Nezuko ×150, Frieren ×115, Yor ×96, Power ×4,4, Makima ×2,9 ; Black Widow ×13 (petits nombres : 2 → 27), Spider-Gwen ×10, Wonder Woman ×2,5.

Spider-Gwen et les films Spider-Verse : `danbooru_spider_gwen.py` → `danbooru_spider_gwen_2026-10-24.json` (fenêtres annuelles alignées sur le 14/12/2018 + 6 mois avant/après le 02/06/2023) ; rule34 par bornes d'ID : `r34_spider_gwen_2026-10-24.csv` et `r34_spider_gwen_notes_2026-10-24.md` (nouvelles ancres 2,6M / 3M / 3,5M).

## Top des tags Copyright (24 octobre 2026) — dossier `copyright/`
- rule34 : la liste des tags ne se filtre pas par type → balayage des pages 1 à 31 de la liste triée par nombre (tous les tags ≥ 152 332 publications), relevé brut dans `r34_copyright_releve.txt`, tableau `top_copyright_rule34_2026-10-24.csv` (24 tags). `video_games`, `virtual_youtuber`, `anime` sont de type Metadata sur rule34, donc exclus.
- Danbooru : API `tags.json?search[category]=3&search[order]=count` → `top_copyright_danbooru_2026-10-24.csv` (30 tags).
- Tags bruts : ils mélangent franchises, éditeurs (nintendo, sega, disney), doublons (dc / dc_comics, naruto / naruto_(series)) et tags parents/enfants (fate_(series) ⊃ fate/grand_order) ; ne jamais additionner.

### Top 20 franchises seulement (24 octobre 2026)
- Fichiers : `copyright/top20_franchises_rule34_2026-10-24.csv`, `copyright/top20_franchises_danbooru_2026-10-24.csv`, `copyright/r34_unions_franchises_2026-10-24.txt` (requêtes OR + résultats).
- Retirés : tags non-franchise (original, patreon, mythology ; Danbooru : original, indie_virtual_youtuber) et éditeurs/diffuseurs qui regroupent des franchises indépendantes (nintendo, sega, disney, capcom, blizzard_entertainment, hasbro, riot_games, cartoon_network, mihoyo).
- Gardés avec mention : marvel et dc (univers partagés) ; hololive, nijisanji, vocaloid (marques).
- Doublons rule34 : union OR `( a ~ b )` sur la liste de posts, total = pid de la dernière page (+1 à 42). Les tags simples gardent le compte de la liste des tags (écart de méthode ±0,3 %).
- Danbooru : les tags enfants impliquent le parent (vérifié via tag_implications), donc le compte du parent suffit ; les enfants sont retirés.
- Balayage rule34 de la liste des tags : pages 1 à 43 (jusqu'à 101 657 publications).

## Comparaison entre sites (23 octobre 2026)
Les 195 personnages individuels (172 féminins + 23 masculins) comparés sur rule34.xxx, Danbooru, Safebooru, Xbooru et e621. Tableau : `comparaison_sites_195_personnages_2026-10-23.csv` ; rapport : `comparaison_sites/RAPPORT_comparaison_sites.md`. Les compteurs rule34 des 24 tags du 27 septembre ont été rafraîchis le 23 octobre par l'autocomplétion de rule34.

## Doublons dédupliqués par recherche OU (24/10/2026) — dossier `doublons/`

- Méthode : recherche `( tag_a ~ tag_b )` dans la liste des posts ; effectif = dernier pid + 21 (±21, la dernière page contient 1 à 42 posts). Le tag principal seul est relevé le même jour par l'autocomplete. Les écarts inférieurs à ~±60 sont du bruit de mesure (pagination et décalage autocomplete/recherche), pas des doublons.
- `pids_unions_2026-10-24.txt` : pids bruts ; `autocomplete_2026-10-24.tsv` : tags principaux et secondaires ; `autocomplete_172_2026-10-24.tsv` : les 172 tags principaux au 24/10.
- `doublons_unions_2026-10-24.csv` : 22 personnages (tag seul, tags secondaires, somme brute, union, gain, recouvrement).
- `selection_173_dedupliquee_2026-10-24.csv` : la sélection re-classée, toute au 24/10 (union pour les doublons, autocomplete du jour pour les autres) ; `effet_dedup` isole l'effet de la déduplication de la croissance depuis le relevé ; Psylocke ajoutée (aucun de ses tags n'atteint seul le seuil, l'union oui).
- Limite : Supergirl ∪ `kara_zor-el` inclut des posts de Power Girl étiquetés `kara_zor-el` (vu dans les résultats) ; le gain de Supergirl est donc un maximum. Seuls les doublons ≥ ~9 600 repérés dans les pages 1-250 sont traités ; un alias plus petit peut manquer.
- Reproduire : `python3 unions.py` depuis `doublons/`.
- Compléments du 24/10 (lignes commentées en fin de `pids_unions_2026-10-24.txt`) :
  - Magik : union de 4 tags ≈ 5 691 contre 5 609 pour `magik_(illyana_rasputin)` seul (+1,5 %), donc toujours sous le seuil de la sélection.
  - Gwen : `spider-gwen` sans `gwen_stacy` ≈ 315 ; `gwen_stacy` sans `spider-gwen` ≈ 4 221, dont ≈ 1 323 `gwen_stacy_(spider-verse)` et au plus 694 `gwen_stacy_(classic)` ; intersection ≈ 15 100.

## Audit complet des doublons (24/10/2026) — dossier `audit_doublons/`

- **But :** vérifier, pour les 205 personnages de la sélection, s'il existe un autre tag du même personnage (nom inversé, suffixe `_(série)`, version de jeu ou de costume ≥ ~500) et en mesurer le gain réel.
- **Étapes :** `autocomplete_audit.py` (autocomplétion des 205 tags et de leurs variantes, 574 requêtes → `autocomplete_audit_2026-10-24.json`) ; `candidats.py` → `candidats_bruts_2026-10-24.tsv` (463 tags candidats, triés à la main : tags génériques, autres personnages, artistes, séries et versions `_(eg)` exclus) ; mesures par recherche → `pids_audit_2026-10-24.txt` (toutes les requêtes et les pids).
- **Découverte :** le compteur de la liste des tags et de l'autocomplétion (celui du relevé) peut être **périmé** par rapport à la recherche directe : Hinata 44 141 contre ≈ 50 100, Misty (`kasumi_(pokemon)`) 18 082 contre ≈ 23 160, Yoruichi 21 936 contre ≈ 25 370, Orihime 19 208 contre ≈ 21 190, Rangiku, Sakura, Rukia (+1 300 à +1 700). Il est parfois plus haut (Amy, Malfoid : posts supprimés). Les anciennes unions comparaient une union (recherche) à un tag seul (liste des tags) : une partie du « gain » venait de ce décalage.
- **Nouvelle règle :** base = compteur du tag principal dans la liste des tags (le même pour les 205, comme le relevé) + **gain réel d'union** = posts qui portent un alias ou une version **sans** le tag principal, mesurés par recherche négative (`( alias1 ~ alias2 ) -tag_principal`, gain ≈ dernier pid + 21) ou par union − tag principal, tous deux mesurés par recherche. Gain retenu seulement s'il dépasse 150.
- **Résultat :** `doublons/selection_205_dedupliquee_audit_2026-10-24.csv` (colonnes `gain_dedup` et `mesure_gain` ajoutées ; le fichier `selection_205_dedupliquee_2026-10-24.csv` est conservé). 37 personnages avec gain : 16 anciennes unions confirmées (dont Psylocke) et 21 nouvelles (Artoria +1 323, Mythra +945, Marin +924, Mitsuri +903, Pyra +735, Harley +588, Reimu +588, Chel +525, etc.). 15 anciennes unions abandonnées (gain ≤ 150 ou nul : Hinata, Sakura, Yoruichi, Misty, Raven, Samus, Lara, Jill, Wonder Woman, Ankha, Helen, Black Cat, Midna, Femme invisible, Ellie). Catwoman et Starfire restent au tag seul (≈ +147).
- **Ajouts :** aucun. Rogue = 8 410 + 231 = 8 641 (sous le seuil de 8 651) ; Barbara Gordon = 7 287.
- **Propagation :** `classement_par_medium/classer_v4.py` → `classement_r34_par_medium_audit_2026-10-24.csv/.md` ; `audit_doublons/corriger_tops.py` → `copyright/top5_*_audit_2026-10-24.csv` et `copyright/top8_personnages_marvel_dc_nintendo_audit_2026-10-24.csv` (personnages masculins mesurés de la même façon : Luffy +357, Izuku +651, Tanjiro +189, Spider-Man +735 ; Naruto, Gojo, Itadori, Giyu, Maki, Lux : tag seul). Changements : Tsunade passe 2e de Naruto, Misty sort du top 8 Nintendo (remplacée par Marie/Isabelle).
- **Limites :** (1) le bruit de la méthode est d'environ ±21 par mesure ; (2) le gain de Supergirl (`kara_zor-el` sans `supergirl`) inclut des posts de Power Girl, c'est donc un maximum ; (3) les versions Lancer/Alter d'Artoria (autres Servants) ne sont pas comptées ; (4) **le classement reste sur la base du compteur de la liste des tags** ; pour les personnages dont ce compteur est périmé (voir ci-dessus), le vrai total est plus élevé. Seule une nouvelle mesure des 205 par recherche directe corrigerait ce biais.
- Reproduire : `python3 audit_doublons/construire_selection.py`, puis `python3 classement_par_medium/classer_v4.py` (depuis `classement_par_medium/`) et `python3 audit_doublons/corriger_tops.py`.

## Application de tri Rule34 / Danbooru (24/10/2026) — dossier `app_tri/`

- `classement_rule34_danbooru.html` : application autonome (aucune ressource externe), style « Top Characters » de MyAnimeList. Onglets par médium, classement par Rule34, Danbooru ou écart (Danbooru pour 100 Rule34), filtres (recherche, sexe, œuvre, minimums, doublons), tri par colonne, fiche détaillée, pagination par 50, export CSV de la vue.
- Données : `donnees_app_2026-10-24.json` = 205 personnages féminins de la sélection auditée + 23 masculins de la comparaison entre sites. Rule34 : base liste des tags + gain d'union audité ; masculins rafraîchis par autocomplétion le 24/10 (`r34_masculins_2026-10-24.json`). Danbooru : API `tags.json` le 24/10 (`danbooru_2026-10-24.json`) ; tags des 33 personnages absents de la comparaison résolus à la main ; `akali`, `sona_(league_of_legends)` et `lamb_(league_of_legends)` sont des alias vers `*_(league)`.
- Régénérer : `python3 donnees.py` puis `python3 build.py` (depuis `app_tri/`).

## Relevé des pages 271 à 280 (24 octobre 2026) — dossier `releves/releve_pages_271-280_2026-10-24/`

- Liste des tags rule34.xxx triée par nombre de publications, pid 5400 à 5580 ; la page 280 descend à 8 199 publications.
- `tags_personnages_pages_271-280.csv` : 27 tags de personnage, dont 12 féminins, 8 masculins, 2 doublons (lara_croft_(classic), bruce_wayne), 4 espèces (goodra, xenomorph, twi'lek, mewtwo) et 1 catégorie (unknown_character).
- Nouvelles féminines : Hana Uzaki, Rin Tohsaka, Lola Bunny, Yuri (DDLC), Stocking, Mavis Dracula, Malicia/Rogue, Palutena, Marceline, Minamoto no Raikou, Eve (Stellar Blade), C-21.
- Doublons vérifiés selon la méthode A de l'audit (autocomplétion des variantes, puis recherche négative ; ajout seulement si gain > 150). Mesures consignées à la fin de `audit_doublons/pids_audit_2026-10-24.txt`. Deux gains retenus : Raikou +693 (alias minamoto_no_raikou_(fate)), donc 8 975 ; Rogue +231 (mesure de l'audit), donc 8 641. Écartés car le gain reste ≤ 150 : Rin (0), Stocking (≈ 63), Marceline (≈ 21) et C-21 (≈ 21).
- Fichiers mis à jour :
  - `selection_216_personnages_feminins_2026-10-24.csv` ;
  - `doublons/selection_217_dedupliquee_audit_2026-10-24.csv` ;
  - `autres_tags_personnages_156_hors_feminins_2026-10-24.csv`.
- Classement par médium v5 : `classement_par_medium/classer_v5.py` produit `classement_r34_par_medium_v5_2026-10-24.csv/.md`. Rin et Raikou vont en jeux vidéo (Fate). C-21 va aussi en jeux vidéo, puisqu'elle a été créée pour Dragon Ball FighterZ. Lola Bunny est rangée en Furry (indice e621 3,44).
- Application `app_tri/` régénérée avec 240 personnages. Les nombres Danbooru des 12 nouvelles ont été relevés via l'API le 24/10 ; pour Stocking et Marceline, les tags Danbooru sont stocking_(psg) et marceline_abadeer.

## Franchises les plus représentées (24/10/2026) — dossier `franchises/`
- `classer_franchises.py` produit `classement_franchises_217_2026-10-24.csv/.md` à partir de la sélection des 217 filles (classement par médium v5).
- Deux classements : par nombre de personnages (départage par publications) et par publications cumulées. Résultat : 94 franchises, dont 53 avec un seul personnage. Le .md précise quels libellés ont été regroupés.
- **Version Danbooru :** `franchises/danbooru/classer_franchises_danbooru.py` produit `franchises/classement_franchises_danbooru_217_2026-10-24.csv/.md`.
  - Sélection propre à Danbooru : les 217 personnages féminins les plus fréquents, soit au moins 7 997 images, pris dans le top 600 des tags de personnage.
  - Genre déterminé par le ratio 1girl/1boy plus une vérification manuelle. Les avatars, espèces et objets sont exclus ; les versions aussi, car leur tag implique le parent.
  - Collecte brute (API, 24/10) : `danbooru/collecte_2026-10-24.json`, `danbooru/implications_2026-10-24.json` et `danbooru/top2000_personnages_danbooru_2026-10-24.json`.
- **Application, liste « Top Danbooru » (24/10/2026) :** dans la barre du haut, on passe de « Sélection Rule34 » (240 personnages) à « Top Danbooru » (217 filles) et inversement.
  - Données : `app_tri/donnees_danbooru.py` produit `app_tri/donnees_app_top_danbooru_2026-10-24.json`, qui est injecté par `build.py`.
  - Compteurs rule34 relevés par autocomplétion le 24/10 (`r34_top_danbooru_autocomplete_2026-10-24.json` et `r34_top_danbooru_variantes_2026-10-24.json`).
  - Tag retenu : le plus utilisé entre le nom Danbooru, le nom inversé et la variante de qualificatif de la même œuvre.
  - Ces compteurs ne sont pas audités pour les doublons, sauf pour les 42 personnages communs aux deux listes.

## Top 50 Xbooru (24 octobre 2026)

Relevé de l'IA dans `xbooru/`. `collecte_liste.py` parcourt la liste des tags de Xbooru triée par nombre (jusqu'à 997 publications) ; `variantes.py` cherche les autres noms de chaque personnage ; `groupes.py` les regroupe ; `union.py` compte en direct chaque groupe sans double compte (tag principal, puis chaque autre nom privé des précédents) ; `top50.py` produit `top50_personnages_xbooru_2026-10-24.csv/.md`. Tous sexes confondus (46 F, 4 M). Les compteurs de la liste des tags de Xbooru sont parfois périmés : seuls les compteurs en direct sont utilisés. Total du site : 883 920 publications.

## Top 100 TierMaker 87784832 vs top 100 féminin rule34 (24 octobre 2026)

Dossier `tiermaker_87784832/` : `comparaison_top100_tiermaker_r34_2026-10-24.md` (synthèse + 2 tableaux), CSV `top100_tiermaker_vs_r34_…` et `top100_r34_vs_tiermaker_…`, `especes_part_feminine_r34_2026-10-24.csv`, `ocr_etiquettes.json` (étiquettes des 1 310 images), scripts `tm_top100.py`, `r34_top.py`, `comparer.py`. Résultat : 31 personnages communs ; Spearman 0,27 et 0,20.

## Votes TierMaker « dessins animés » vs rule34, périmètre Comics + Cartoons occidentaux + Furry (24 octobre 2026)

Dossier `tiermaker_cartoons_vs_r34/` : votes 5058287, 8447367, 88691896, 91860172. La première version (tous médiums) a été remplacée à ta demande par une comparaison limitée aux Comics, Cartoons / films d'animation occidentaux et Furry : liste rule34 du périmètre = 69 personnages (64 de la sélection 217 selon la v5 + 5 espèces), top 100 TierMaker après retrait des personnages de jeux vidéo. `comparaison_perimetre_comics_cartoons_furry_2026-10-24.md`, CSV `top100_perimetre_<id>_vs_r34_2026-10-24.csv`, `identifications.py`, `comparer_perimetre.py`. Spearman : 0,41 ; 0,43 ; 0,38 ; 0,46 (après correction June/Azula et ajout de Ty Lee).

## App « Top 100 TierMaker × Rule34 » (24 octobre 2026)

`app_tiermaker/top100_tiermaker_rule34.html` (1,3 Mo, autonome, vignettes intégrées) : un onglet par vote (87784832, 5058287, 8447367, 88691896, 91860172), top 100 Average Vote avec vignette, médium, moyenne, votants, publications Rule34 (sélection 217 ou autocomplétion) et rang r34. Option « Périmètre Comics + Cartoons + Furry » (retire les personnages hors périmètre et complète avec les images suivantes pour les votes dessins animés), tri, filtre par médium, recherche ; Spearman et médiane recalculés sur les lignes affichées. Reconstruire : `python3 app_tiermaker/build.py` (nécessite les images dans /tmp/tmall et /tmp/tm4).

## 3 votes TierMaker ajoutés le 24 oct. (81614596, 30083716, 20899730)

| Vote | Titre (modèle) | Images | Participants | Votes | Dates | Paliers |
|---|---|---:|---:|---:|---|---|
| 81614596 | Disney/PIXAR Waifus (« Some of Disney/Pixar's hottest women ») | 150 | 14 094 | 498 430 | 13 → 20/06/2025 | S, A, B, C, D, Hard Pass |
| 30083716 | Hottest Cartoon Characters (« Female Cartoon Characters ») | 1 087 | 6 692 | 353 466 | 09 → 16/05/2026 | S à D |
| 20899730 | Hottest animated girls (« Penultimate Female Cartoon Character Tierlist ») | 324 | 7 827 | 472 180 | 24/02 → 03/03/2026 | S, A, B, C, D, Ewwwwww, Who? |

- Données : `tiermaker_<id>/live_event_<id>.json.gz` (téléchargées avec curl + en-têtes Referer/Origin live.tiermaker.com), classements `classement_average_avec_incertitude.csv/.json`.
- Script : `notebooks/analyse_live_tiermaker_v2.py`. Ton choix : Hard Pass et Ewwwwww = note la plus basse (échelle 6 → 1) ; votes « Who? » retirés. Colonne `moyenne_sur_5` = même ordre, ramené sur 5.
- Identifications : bloc « Ajout 24 oct. (suite) » de `tiermaker_cartoons_vs_r34/identifications.py` (noms de fichiers vérifiés sur planches pour 81614596 et 20899730 ; 30083716 surtout visuel). Nouveau : `ANIME` (hors périmètre) et `SANS_TAG` (identifiée mais sans tag rule34 dédié, exclue des calculs).
- Résultats (périmètre Comics + Cartoons + Furry) dans `comparaison_perimetre_comics_cartoons_furry_2026-10-24.md` et `top100_perimetre_<id>_vs_r34_2026-10-24.csv` : 81614596 Spearman 0,47 (n = 98, 5 personnages de la liste r34) ; 30083716 0,30 (n = 74 ; 16 images animanga/jeux retirées ; 27 de la liste) ; 20899730 0,48 (n = 97 ; Peach du film retirée ; 17 de la liste).
- 30083716 contient beaucoup d'images en double ; les doublons n'ont souvent que 30 à 80 votants et remontent haut par hasard (signalés « 2e image »). Recherche de la liste r34 dans ce modèle : planches jusqu'au rang 400 + noms de fichiers au-delà.
- App : 8 onglets ; `app_tiermaker/telecharger_vignettes.py id:N …` re-télécharge les vignettes dans /tmp avant `build.py`.

## Page « Analyse : les plus appréciés » (app TierMaker × Rule34, 24 oct. 2026)

- Nouvel onglet ouvert par défaut dans `app_tiermaker/top100_tiermaker_rule34.html`. Il synthétise les 8 votes (vue Average) : indice de consensus (moyenne sur les votes cochés de 101 − rang de la meilleure image dans le top 100, 0 si le personnage est absent), présence, nombre de top 10, rang médian, écart à la moyenne du vote (z), publications Rule34, et Danbooru / e621 quand le personnage figure dans le relevé des 195.
- Réglages : mode périmètre (Comics + Cartoons + Furry), votes à cocher, tri, médium, présence minimale, recherche. On y trouve un nuage indice × publications (échelle log), les écarts votes/publications, le top 5 de chaque vote et une section « Méthode et limites ».
- `build.py` ajoute `stats` à chaque vote (moyenne et écart-type sur toutes les images du classement CSV) et `D.sites`, construit à partir de `comparaison_sites_195_personnages_2026-10-23.csv`.
- Résultats par défaut : Shego 94,9 et Hélène Parr 92,5 sont les seules présentes dans les 8 top 100. Viennent ensuite Chel 85,3, Jessica Rabbit 80,6, Kim Possible 79,9, Starfire 79,4 et Raven 78,5. Spearman indice / publications : 0,27 (0,45 en mode périmètre, où Hélène Parr passe n° 1 avec 97,4).

## Vote 80408816 ajouté le 24 oct. 2026 (« Waifu anime and cartoon »)

- Modèle « Waifus Anime, Cartoon and Videogames », tous médiums : 381 images, paliers S à D, 11 877 participants, 486 531 votes, du 17/08/2025 au 24/08/2025. Fichiers : `tiermaker_80408816/live_event_80408816.json.gz` et le classement CSV/JSON (`notebooks/analyse_live_tiermaker_v2.py`).
- Identification : les noms sont écrits sur les images ; ils ont été lus par OCR puis vérifiés sur planches. Les rangs 1 à 130 sont tous identifiés. Au-delà, seules les images du périmètre Comics + Cartoons + Furry sont rattachées, jusqu'au rang 274, plus la liste r34 du périmètre jusqu'au rang 381. Cinq étiquettes n'ont pas été rattachées avec certitude : Ruby, Kaisa, Maya, Cleopatra, Johanna. Bloc « Ajout 24 oct. (suite 2) » dans `identifications.py`. Comptes hors sélection relevés par autocomplétion rule34 le 24 oct. ; `desiree` et `princess_fiona` sont des tags génériques.
- Résultats : top 5 = Raven, Hinata, Starfire, Chun-Li, Marin Kitagawa. Spearman rang TM / publications r34 : 0,55 sur le top 100 tous médiums (100 personnages) ; 0,43 dans le périmètre (89 images retirées, 33 personnages de la liste r34 du périmètre).
- App : 10e onglet. Le texte « Ce qu'il faut retenir » de la page Analyse a été réécrit pour 9 votes : Shego 91,7 et Hélène Parr 90,7 ; Hélène Parr est n° 1 en mode périmètre (97,2).

## Vote 30081640 ajouté le 24 oct. 2026 (« Biggest Waifu List », anime)

- Modèle « The Anime Waifu Tier List » : 2 050 images, paliers S à D, 3 530 participants, 119 540 votes, du 24/09/2026 au 01/10/2026. **Peu de votants par image** : médiane 26 sur l'ensemble du modèle, 18 à 1 094 dans le top 100, et moins de 100 votants pour 46 images du top 100.
- Le modèle est présenté comme anime/manga, mais il contient aussi des personnages de jeux vidéo (2B, A2, Tifa, Aerith, Bayonetta, Mitsuru, Cynthia, Ishtar, Ereshkigal). Leur médium suit les règles habituelles (classement v5, sinon médium de création).
- Identification : nom de fichier, plus l'étiquette « personnage / série » écrite sur l'image, vérifiés sur planches. Pièges : « Miku » = Miku Nakano (5-toubun), pas Hatsune Miku ; « Lucy » = Lucy d'Edgerunners ; « Haruka » = Flora (Pokémon) ; « Rumi » = Mirko.
- Le n° 92, Rin Kokonoe (Kodomo no Jikan), est un personnage enfant : aucun compte Rule34 n'a été relevé ni affiché.
- Comptes hors sélection : autocomplétion du 24 oct. Les variantes non fusionnées sont signalées (`VARIANTES_EV`). Bloc « Ajout 24 oct. (suite 3) » dans `identifications.py`.
- Le vote est marqué `ANIME_SEUL` : il est exclu de la comparaison périmètre et du mode périmètre de l'App (case désactivée sur son onglet, vote ignoré dans l'Analyse en mode périmètre).
- Top 5 : Yoruichi, Mirko (53 votants), Yor Forger, 2B, Esdeath. Spearman rang / publications : 0,45 (99 personnages).
- Analyse : boutons de sélection rapide « Tous les votes », « Votes dessins animés (7) » et « Votes ouverts à l'anime (3) ». Texte « Ce qu'il faut retenir » réécrit pour 10 votes. Sur les 3 votes ouverts à l'anime : 2B 97,3, Marin 95,3, Yoruichi 94,7, Yor 94,3.

## Vote 436045 ajouté le 24 oct. 2026

- Source : `https://live.tiermaker.com/436045`, « Cartoon Hotties » (modèle `ranking-baddies-20-17506926`, 295 images, paliers S à D, vue Average Vote).
- **Vote encore ouvert** : l'événement a été créé le 21/10/2025 et n'a pas de date de fin. Chiffres du relevé du 24/10/2026 : 7 894 participants, 441 695 votes, 957 à 3 565 votants par image. Ils changeront.
- Malgré le titre, le modèle mêle cartoons, comics et anime : 36 images du top 100 sont des anime.
  - Le vote est classé parmi les « votes ouverts à l'anime » (bouton à 4 votes). Le bouton « dessins animés » reste à 7 votes.
- Identification par nom de fichier, vérifiée sur planches.
  - Rangs 1 à 100 : toutes les images.
  - Rangs 101 à 175 : périmètre Comics + Cartoons + Furry seulement.
  - Cas à confirmer : n° 74 Ellen Yin, n° 107 Wilhamena, n° 116 Cleopatra (Clone High, sans tag dédié).
  - L'image n° 18 (Makio, Suma et Hinatsuru) n'a pas de tag unique et est retirée en périmètre.
- Les nouveaux tags ont des comptes d'autocomplétion rule34, approximatifs. Exemple : `duplikate` n'a que 3 publications.
- Résultats :
  - top 100 périmètre atteint au rang TierMaker 145 (58 Cartoons, 39 Comics, 3 Furry) ;
  - Spearman rang / publications : 0,42 en périmètre (n = 99), 0,36 sur le top 100 tous médiums.
- Fichiers :
  - `tiermaker_436045/` (JSON gzip et classement CSV) ;
  - `tiermaker_cartoons_vs_r34/top100_perimetre_436045_vs_r34_2026-10-24.csv` ;
  - 11e onglet de l'application.
- Correctifs du code :
  - `build.py` et `template.html` acceptent un vote sans date de début ni de fin (date de création affichée, mention « toujours en cours ») ;
  - `SANS_TAG_MEDIUM` permet de ranger une image sans tag dans l'animanga.
- Synthèse à 11 votes : Shego 83,6, Hélène Parr 83,2, Chel 76,5. En périmètre, Hélène Parr est n° 1 (97,4).

## Vote 73568440 ajouté le 24 oct. 2026

- **Source.** `https://live.tiermaker.com/73568440`, « Ranking Female Video Game Charecters » (modèle `most-popular-female-video-game-characters-902887`).
  - 617 images, vote du 11 au 18/09/2025, 4 126 participants, 166 146 votes.
  - 7 paliers notés de 7 à 1 : I love you, Ma gurl, AMAZING, Good, Mid, Ew, GET OUT.
  - Le notebook v2 accepte maintenant 7 paliers (colonne `palier_bas2`).
- **Votants.** De 113 à 1 624 par image (médiane 204). Le nombre de votants baisse avec la position de l'image dans le modèle (Spearman -0,94).
- **Identification.** Nom et jeu écrits sur les images. Rangs 1 à 100 : tout. Au-delà : toutes les images du périmètre repérées sur les 617, soit 24 images en tout.
- **Médium** (règles du classement par médium) :
  - Comics : Black Cat, Femme invisible, Psylocke, Catwoman, Emma Frost, Magik, Poison Ivy, Batgirl, Gamora, Squirrel Girl, Kamala Khan, Blanche-Neige (Fables, sans tag) ;
  - Cartoons : Harley Quinn ;
  - Furry : Ankha, Hornet, Felicia, Amy Rose, Blaze, Toriel, Isabelle, Rabbid Peach, Amaterasu, Rivet, Kindred (agneau) ;
  - Jeux vidéo : Luna Snow (créée pour un jeu) ;
  - Felicia, Rabbid Peach, Amaterasu et Rivet sont rangées en Furry d'après e621 (respectivement 2 781, 877, 2 138 et 5 326 publications).
- **Résultats.**
  - Top 5 : 2B, Tifa, Samus, Chun-Li, Zelda.
  - Spearman top 100 tous médiums : 0,53. En périmètre : 0,32 (n = 23, p = 0,14, non significatif).
- **Application.**
  - Nouveau bouton « Votes ouverts au jeu vidéo (3) » : 87784832, 80408816, 73568440.
  - Le bouton « dessins animés » a désormais une liste explicite de 7 votes.
- **Espace.** Pour garder de la marge, les JSON de classement de 5058287, 8447367, 88691896, 91860172, 81614596, 30083716 et 20899730 ont été gzippés. Les CSV restent en clair. Celui de 87784832 n'est pas gzippé, car `comparer.py` le lit.

## Nouvel indice de consensus et vote 99761754 (24 oct. 2026)

**Indice (page Analyse).**
- Calcul : moyenne de (101 − rang dans le top 100), calculée seulement sur les votes où le personnage pouvait figurer.
- Un vote compte s'il couvre le médium du personnage (`VCOV` dans `template.html`), ou si le personnage est dans son top 100.
- Couverture par vote :
  - 87784832 et 80408816 : tous les médiums ;
  - 436045 : Cartoons, Comics, Furry et Animanga ;
  - 30081640 et 99761754 : Animanga ;
  - 73568440 : Jeux vidéo, Comics et Furry ;
  - votes dessins animés : Cartoons, Comics et Furry ;
  - Disney 81614596 : seulement les personnages présents dans son top 100.
- Garde-fou : on divise par au moins min(3, nombre de votes cochés).
- L'ancien indice (absence = 0 partout, divisé par le nombre de votes cochés) reste en tri « ancien indice ».
- Effet sur le top 50 à 13 votes : avant, 34 Cartoons ; maintenant, 18 Cartoons, 15 Jeux vidéo, 13 Animanga, 3 Comics, 1 Furry.
- Nouveau classement : n° 1 2B (98,0) ; puis Chel, Shego, Starfire, Raven et Hélène Parr, entre 91,5 et 93,6.
- Spearman indice / publications Rule34 : 0,52 (contre 0,36 avec l'ancien indice).

**Vote 99761754.**
- « Top Tier Waifu », modèle `best-anime-waifus-2025-17820038` : 311 images, paliers S à D, du 20 au 27/08/2025.
- 19 274 participants, 693 261 votes.
- L'événement était réglé en « most votes » ; il est relu en Average Vote, comme les autres.
- Modèle 100 % anime, ajouté à `ANIME_SEUL` : le mode périmètre est sans objet.
- Identification visuelle (images sans nom) : 67 images du top 100 identifiées, 33 non identifiées. À confirmer : n° 47 Yunyun, n° 57 Maki Oze. Correction utilisateur : le n° 9 est Nico Robin, pas Boa Hancock.
- Top 5 : Yor, Makima, 2B, Marin, Tsunade. Spearman : 0,48.

**Espace disque.** Fichiers gzippés (non lus par les scripts) :
- `tiermaker/live_scores.json`, `tiermaker/scores.json`, `tiermaker/template_images_test-run-3-125077.json` ;
- `xbooru/liste_brute.json` ;
- `comparaison_sites/resultats.json`.

## Thèse « production par unité de temps » (24 oct. 2026)

- **Dossier :** `production_temps/`.
- **`danbooru_annuel.py`** : publications Danbooru par année d'upload (2006 à 2026), relevées avec le metatag `date:AAAA-01-01..AAAA-12-31`, pour 37 personnages et pour le total du site.
  - Résultats bruts : `danbooru_annuel_2026-10-24.json`.
  - Total 2026 : 3 requêtes (1er janvier → 24 octobre), soit 1 887 460 uploads.
  - Le tag Ai Hoshino est faux : il renvoie 0.
- **`analyse_production.py`** produit `production_danbooru_par_an_2026-10-24.csv`, avec trois mesures :
  - publications par an brutes ;
  - publications pour 10 000 uploads du site ;
  - même mesure sur la seule fenêtre 2023–2025.
  - Le début est estimé comme la première année atteignant 10 % du maximum du personnage. Si cette année est 2006, le personnage est marqué « censure gauche ».
- **`ia_rule34_2026-10-24.csv`** : part des publications Rule34 taguées `ai_generated`, mesurée avec l'astuce pid.
- **Point de méthode :** Danbooru interdit l'IA, ce qui en fait la mesure propre.

## Relevé des pages 281 à 290 (24 octobre 2026) — dossier `releves/releve_pages_281-290_2026-10-24/`

- **Source :** liste des tags rule34.xxx triée par nombre de publications, pid 5600 à 5780. La page 290 descend à 7 812 publications.
- **Continuité :** la page 280 a été relue ; ce sont les mêmes tags, à quelques publications près.
- **`tags_personnages_pages_281-290.csv`** contient 23 tags de personnage :
  - 12 féminins ;
  - 5 doublons : ada_wong_(adriana), natasha_romanoff, ahri_(league_of_legends), harley_quinn_(classic), et white_queen (surnom d'Emma Frost, vérifié sur les publications ; le wiki rule34 parle de la Reine blanche d'Alice, mais le tag sert en pratique pour Emma Frost) ;
  - 4 espèces : flareon, typhlosion, lugia, yoshi ;
  - 2 personnages au genre non défini, non comptés : Frisk et Chara (Undertale).
- **Nouvelles féminines :** Batgirl, Mash Kyrielight, Marie Rose, Marge Simpson, Magicienne des Ténèbres, Ouro Kronii (VTubeuse hololive, rangée dans « Hors des 4 médiums »), Camilla, Loba, Marie (Splatoon), Squirrel Girl, Shego, Panam Palmer.
- **Doublons (méthode A, mesures à la fin de `audit_doublons/pids_audit_2026-10-24.txt`).** Trois gains retenus :
  - Squirrel Girl +2 205, donc 10 093 ;
  - Batgirl +987 (barbara_gordon et versions), donc 9 182 ;
  - Mash +441 (shielder et versions), donc 8 624.
- **Contrôles sans effet :**
  - Black Widow + natasha_romanoff donne un gain d'environ 147, sous 150 : inchangée.
  - Emma Frost + white_queen donne environ 189, identique à l'audit : inchangée.
- **Fichiers mis à jour :**
  - `selection_228_personnages_feminins_2026-10-24.csv` ;
  - `doublons/selection_229_dedupliquee_audit_2026-10-24.csv` ;
  - `autres_tags_personnages_167_hors_feminins_2026-10-24.csv`.
- **Classement par médium v6 :** `classement_par_medium/classer_v6.py` produit `classement_r34_par_medium_v6_2026-10-24.csv/.md` (63 animanga, 94 jeux vidéo, 13 comics, 26 cartoons, 29 furry, 4 hors médiums).
- **Application `app_tri/` régénérée avec 252 personnages :** les nombres Danbooru des 12 nouvelles ont été relevés via l'API le 24/10.
- **Pas encore mis à jour** (ils lisent encore la sélection 217) :
  - l'application TierMaker ;
  - les classements de franchises.

## Relevé des pages 291 à 300 (24 octobre 2026) — dossier `releves/releve_pages_291-300_2026-10-24/`

- **Source :** liste des tags rule34.xxx triée par nombre de publications, pid 5800 à 5980. La page 300 descend à 7 458 publications ; le dernier tag de personnage, Kefla, en a 7 491.
- **`tags_personnages_pages_291-300.csv`** contient 22 tags de personnage :
  - 14 féminins ;
  - 5 doublons : koriand'r (Starfire), batman_(bruce_wayne), kara_zor-l (Power Girl), psylocke (déjà dans la sélection par union), gwen_tennyson_(classic) (version enfant de Gwen : gain ni mesuré ni ajouté) ;
  - 1 espèce : pal_(species) ;
  - 1 catégorie : octoling_girl ;
  - 1 personnage au genre au choix, non compté : Corrin.
- **Nouvelles féminines :**
  - Lucoa ;
  - Keqing, Noelle Silva, Femshep (version féminine du Commandant Shepard), Sonia ;
  - She-Hulk, Lux, Violette Parr, Miranda Lawson, Mary Jane Watson ;
  - Soraka, Brigitte, Kyoka Jiro, Kefla.
- **Gain retenu :** Lucoa +1 155 (lucoa, lucoa_(maidragon)…), donc 8 672.
- **Contrôles sans effet :**
  - She-Hulk : gain d'environ 105.
  - Power Girl avec kara_zor-l : environ 231, identique à l'audit.
- **Fichiers mis à jour :**
  - `selection_242_personnages_feminins_2026-10-24.csv` ;
  - `doublons/selection_243_dedupliquee_audit_2026-10-24.csv` ;
  - `autres_tags_personnages_175_hors_feminins_2026-10-24.csv`.
- **Classement par médium v7 :** `classement_par_medium/classer_v7.py` donne 67 animanga, 101 jeux vidéo, 15 comics, 27 cartoons, 29 furry et 4 hors médiums.
- **Application `app_tri/` :** 266 personnages.
- **Danbooru (API, 24/10) :** Femshep = commander_shepard_(female), Lux = lux_(league), Soraka = soraka_(league), Lucoa = lucoa_(maidragon), Kyoka Jiro = jiro_kyoka.

## Mise à jour des produits dérivés sur la sélection 243 (24 oct. 2026)

Tout ce qui lisait encore la sélection 217 (seuil 8 209, médium v5) lit maintenant la sélection 243 (`doublons/selection_243_dedupliquee_audit_2026-10-24.csv`, seuil 7 491, pages 1 à 300) et le classement par médium v7.

- **Application TierMaker** (`app_tiermaker/top100_tiermaker_rule34.html`) : `tiermaker_87784832/r34_top.py` → sélection 243 ; `build.py` → v7, seuil 7 491. Les vignettes viennent de l'application précédente (repli sur `/tmp/vcache.json` si `/tmp/tmall` et `/tmp/tm4` sont vides). 1 559 vignettes, toutes présentes.
- **Identifications** (`tiermaker_cartoons_vs_r34/identifications.py`, bloc final `REMAP_243`) : `barbara_gordon` → `batgirl` (la sélection additionne les deux tags) et `jirou_kyouka` → `kyoka_jiro` (tag principal rule34).
- **Comparaison de périmètre** (`tiermaker_cartoons_vs_r34/comparer_perimetre.py`) : la liste rule34 du périmètre passe de 69 à 76 personnages (Comics 15, Cartoons 27, Furry 29, plus 5 espèces).
- **Franchises rule34** : `franchises/classement_franchises_243_2026-10-24.csv/.md` (100 franchises, dont 53 à un seul personnage).
- **Franchises Danbooru** : la sélection propre à Danbooru passe aussi à 243 pour garder le même effectif (seuil 7 609 images). Fichiers : `franchises/danbooru/selection_243_…csv` et `franchises/classement_franchises_danbooru_243_2026-10-24.csv/.md`. Les phrases chiffrées du rapport sont maintenant calculées.
- **Top Danbooru de l'app de tri** : 243 personnages. Compteurs rule34 des 24 nouveaux relevés par autocomplétion le 24/10 ; 6 tags principaux diffèrent du nom Danbooru (`kasen_ibaraki`, `iku_nagae`, `ritsu_tainaka_(k-on!)`, `toujou_nozomi`, `murakumo_(kantai_collection)`, `amatsukaze_(kantai_collection)`). Ces compteurs ne sont pas audités.
- Les anciens fichiers 217 sont conservés.

## Relevé des pages 301 à 310 (24 oct. 2026)

- Source : liste des tags triée par nombre de publications, pages 301 à 310 (pid 6000 à 6180) ; la page 310 se termine à 7 152 publications. Script : `releves/releve_pages_301-310_2026-10-24/construire.py`. Détail : `tags_personnages_pages_301-310.csv` (27 tags de personnage).
- **13 personnages féminins ajoutés** : Poison Ivy, Zero Two, Karin (Blue Archive), Reine Chrysalis, Nino Nakano, Maki Zen'in, Colette (Brawl Stars), Jasmine, Noelle Holiday, Zhu Yuan, Usagi Tsukino, Hitori Gotō, Luz Noceda.
- Gains d'union retenus (> 150) : Usagi +651 (tag de personnage `sailor_moon`), Jasmine +231. Les autres mesures sont dans `audit_doublons/pids_audit_2026-10-24.txt`.
- Autres tags : 5 doublons (Gwen Stacy Spider-Verse, Amélie Lacroix, Himiko Toga, K/DA Ahri, Artoria Lancer), 6 masculins, 2 espèces (Hypno, Delphox), 1 catégorie (npc_trainer).
- Nouveaux fichiers : `selection_255_personnages_feminins_2026-10-24.csv`, `doublons/selection_256_dedupliquee_audit_2026-10-24.csv`, `autres_tags_personnages_189_hors_feminins_2026-10-24.csv`, `classement_par_medium/classement_r34_par_medium_v8_2026-10-24.csv/.md` (Animanga 72, Jeux vidéo 104, Comics 16, Cartoons 29, Furry 31, Hors 4). Reine Chrysalis (indice e621 6,5) et Noelle Holiday (4,87) sont rangées en Furry.
- Seuil : 7 228 publications (Luz Noceda, dernière fille relevée).
- Produits mis à jour dans la foulée : application de tri (279 personnages, Top Danbooru étendu à 256), application TierMaker et comparaison de périmètre (81 personnages dans le périmètre), franchises rule34 (`franchises/classement_franchises_256_…`) et Danbooru (`classement_franchises_danbooru_256_…`, seuil Danbooru 7 428). Alias de franchise ajouté : Hololive (VTubers) = Hololive.

## Application de tri : 18 personnages masculins ajoutés (24 oct. 2026)

- `app_tri/donnees.py` (liste `EXTRA_M`) : les 18 tags masculins notés dans les relevés de pages qui manquaient (Batman, Ritsuka Fujimaru, Boyfriend, Asriel, Moxxie, Sasuke, Freddy, Beast Boy, Leon Kennedy, Bonnie, Venti, Knuckles, Legoshi, Denji, Big Macintosh, Finn, Raikage, 9S). L'application compte maintenant 297 personnages (256 F, 41 M).
- Gains d'union mesurés pour 14 d'entre eux (journal `audit_doublons/pids_audit_2026-10-24.txt`) ; seul Sasuke dépasse 150 (+189, total 8 773). Moxxie, Bonnie, Legoshi, Finn et Raikage : non mesurés, marqués « non audité ».
- Médium : règle de création ; Furry pour Asriel, Moxxie, Freddy, Bonnie, Knuckles, Legoshi et Big Macintosh. Beast Boy reste en Comics (création 1965).
- Tags Danbooru : relevés le 24/10 (API tags.json) ; Raikage = `a_(naruto)`, Boyfriend = `boyfriend_(friday_night_funkin')`, 9S = `9s_(nier:automata)`.

## Décisions de l'utilisateur du 24 oct. 2026 (après le relevé 301-310)

- **Âge :** Violette Parr, Noelle Silva, Kyoka Jiro, Usagi Tsukino, Luz Noceda et Hitori Gotō restent dans la sélection (l'âge est seulement indiqué en Note).
- **Femshep :** gardée (Jeux vidéo, Mass Effect).
- **Kronii :** reste dans « Hors des 4 médiums ».
- **Beast Boy :** déplacé en Cartoons dans l'application de tri, comme Raven et Starfire.
- **Batgirl = Barbara Gordon seule.** Script `doublons/batgirl_barbara_seule_2026-10-24.py` (modifie `selection_256_dedupliquee_audit_2026-10-24.csv` sur place, idempotent). Barbara ≈ 7 875 (union de `batgirl`, `barbara_gordon` et de ses versions, moins les publications taguées Cassandra Cain ou Stephanie Brown), au lieu de 9 182 ; rang 229 au lieu de 197. Limite : les publications `batgirl` sans nom de personnage restent comptées (surtout Barbara, non vérifiable). Danbooru : `barbara_gordon` (313) au lieu de `batgirl` (532). Classement par médium v8, application de tri, application TierMaker, comparaison de périmètre et franchises régénérés.
- Cas similaires encore traités « par nom de héros » : Psylocke (Betsy Braddock + Kwannon, union `psylocke` ∪ `psylocke_(kwannon)`) et Supergirl (tag `supergirl`, qui peut inclure d'autres Supergirl, + `kara_zor-el`, qui inclut des posts de Power Girl).

## Franchises, tous personnages (24 oct. 2026)

- Script `franchises/classer_franchises_tous.py` → `franchises/classement_franchises_tous_personnages_2026-10-24.csv/.md`.
- Base : 302 personnages des pages 1 à 310 : 256 féminins (sélection auditée, médium v8), 41 masculins (application de tri) et 5 au genre non défini ou au choix (Kris, Frisk, Chara, Corrin, MalO avec son plus gros tag `scp-1471-a`). Byleth, le Commandant Shepard et Kindred ne sont pas ajoutés une 2e fois, car leur version féminine est déjà comptée. Espèces, catégories et doublons exclus.
- 110 franchises. Par nombre : Genshin Impact 14, Pokémon 13, Marvel 12, My Little Pony 11, DC 11, Sonic 10. Par publications : Sonic 220 467, Naruto 217 506, My Little Pony 200 026.

## EdeniaList : page « Franchises » (24 oct. 2026)

- Nouvel onglet **Franchises** dans `app_tri/classement_rule34_danbooru.html` (EdeniaList).
  - Sous-onglets : Top 20 Rule34 × Danbooru (deux tableaux côte à côte, base Rule34 au choix : tous les personnages ou filles seules, et la liste des franchises communes) ; Rule34 tous les personnages (110) ; Rule34 filles seules (107) ; Danbooru filles (50).
  - Tri par nombre de personnages ou par publications cumulées, recherche, et liste des personnages en touchant une ligne.
- Données : `app_tri/donnees_franchises.py` → `app_tri/donnees_franchises_2026-10-24.json`. Ce fichier lit les 3 CSV de `franchises/` et `franchises/tous_personnages_liste_2026-10-24.json` (écrit par `classer_franchises_tous.py`). `build.py` injecte `/*DATA_F*/`.
- Ordre de régénération : `classer_franchises.py`, `danbooru/classer_franchises_danbooru.py`, `classer_franchises_tous.py`, puis `app_tri/donnees_franchises.py` et `app_tri/build.py`.

## EdeniaList Franchises : tri par en-têtes et colonne « Tag franchise » (24 oct. 2026)

- Les boutons « Classer par » sont supprimés. On trie en cliquant sur les en-têtes (#, Franchise, Pers., Publications, Tag franchise, Rang sur l'autre site) ; un 2e clic inverse l'ordre.
  - Le # affiche le rang selon la colonne choisie.
  - Dans le Top 20, chaque tableau se trie séparément et garde les 25 premières franchises (top 25 depuis le 24/10) selon Pers., Publications ou Tag franchise.
- Nouvelle colonne **Tag franchise** : publications totales du tag de la franchise sur le site.
  - Script : `franchises/tags_franchise/choisir_tags.py` → `tags_franchise_2026-10-24.csv` (site, franchise, tag, publications, méthode, autres tags).
  - rule34 : compteur de l'autocomplétion du tag principal (sonde : `sonder_r34.py` → `sonde_autocomplete_r34_2026-10-24.json`).
  - Quand une franchise a des tags concurrents, ils sont notés (marvel 227 519 / marvel_comics 180 701 ; sonic_(series) / sonic_the_hedgehog_(series) ; naruto_(series) / naruto…).
  - Unions mesurées (recherche OR, dernière page + 21) : Avatar `avatar_the_last_airbender ~ the_legend_of_korra ~ avatar_legends` ≈ 61 089 ; Fatal Fury / KOF `king_of_fighters ~ fatal_fury` ≈ 53 991.
  - Danbooru : post_count du tag de franchise des personnages (`danbooru_tags_franchise_2026-10-24.json`).
- Limite : seules les franchises qui ont au moins un personnage dans la liste sont classées.

## Squirrel Girl et Magik avant/après Marvel Rivals (24 oct. 2026)

- `squirrel_girl_rivals/` et `magik_rivals/` : résultats (`resultats_*.md`), relevé Danbooru mensuel (`danbooru_mensuel.py` → json) et totaux.
- rule34 : unions de tags du personnage, comptes par la méthode dernière page + 21, coupure avant/après par numéro de post `id:<11884000`. La date exacte n'est pas lisible ; cette coupure correspond à la révélation de Squirrel Girl, le 30/11/2024.
- Squirrel Girl : ≈ 1 491 publications avant, ≈ 8 600 après (10 093). Magik : ≈ 651 avant, ≈ 5 080 après (5 733), plus ≈ 315 posts Marvel Tōkon (sorti le 06/08/2026).

## Fréquence de publication de Magik vs Jinx, Gwen, Nami, Frieren, Psylocke (24 oct. 2026)
Voir `frequence_magik/resultats_frequence_2026-10-24.md` (r34 par fenêtres d'ID normalisées par le volume du site ; Danbooru 12 derniers mois).

## Relevé des pages 311 à 330 (24 oct. 2026) — dossier `releves/releve_pages_311-330_2026-10-24/`

- Source : liste des tags triée par nombre de publications, pages 311 à 330 (pid 6200 à 6580) ; la page 330 se termine à 6 548 publications. Script : `construire.py` ; brut : `brut.txt` ; détail : `tags_personnages_pages_311-330.csv` (60 tags de personnage) ; mesures d'union : `requetes_gains.json`, `pids.txt`.
- **37 personnages féminins ajoutés** : Kamisato Ayaka, Mileena, Caulifla, Mori Calliope, Houshou Marine, Rio, Diane Foxington, Péridot, Temari, Nejire Hado, Chica, Evelyn Chevalier, Daphné Blake, Hermione Granger, Princesse Cadance, Poppy, Caitlyn Kiramman, Mère de Lana (Néphie en VF), Ashley, Bea (Faïza en VF), Sakuya Izayoi, Tsuki Uzaki, Jenny Wakeman, Yoko Littner, Burnice White, Callie, Bayonetta, Miss Fortune, Sanae Kochiya, Judy Alvarez, Frankie Foster, Lisa, Meow Skulls, Evelynn, Jean Gunnhildr, Nemona, Skyla (Carolina en VF).
- Gains d'union retenus (> 150) : Sanae +441, Meow Skulls +399, Sakuya +273, Caitlyn +189. Non additionnés (≤ 150 ou autre nature) : Rio, Nejire, Jean (≤ 147), Miss Fortune 105, Skyla ≤ 100, Cadance 25, Kara Danvers ≈ 105 ; `bayonetta` est le tag du jeu (≈ +651 hors tag du personnage, non additionné) ; `brazilian_miku` ≈ 315 posts sans `hatsune_miku` (variante de fans, non additionnée).
- Autres tags : 7 doublons (Barbara Gordon, Bulma, Squirrel Girl version Rivals, Kara Danvers, Miku brésilienne, Hana Song, Angela Ziegler), 8 espèces (Argonien, Sangheili, Goupix, Tauren, Félinferno, Gerudo, Vipélierre, Raichu), 5 masculins (Dick Grayson, Jax, Shining Armor, Ichigo Kurosaki, Sacha), 2 catégories (background_character, Scarlett Johansson = personne réelle), 1 genre au choix (Sensei de Blue Archive).
- Nouveaux fichiers : `selection_292_personnages_feminins_2026-10-24.csv`, `doublons/selection_293_dedupliquee_audit_2026-10-24.csv`, `autres_tags_personnages_212_hors_feminins_2026-10-24.csv`, `classement_par_medium/classement_r34_par_medium_v9_2026-10-24.csv/.md` (Animanga 77, Jeux vidéo 125, Comics 16, Cartoons 33, Furry 35, Hors 7). Furry par l'indice e621 : Cadance 5,85, Diane 5,69, Meow Skulls 4,35, Chica 3,08 ; Poppy (2,60), Jenny (1,60) et Callie (1,11) restent hors Furry. Hors des 4 médiums : Hermione (roman), Mori Calliope et Houshou Marine (VTubeuses).
- Seuil : 6 588 publications (Skyla, rang 293).
- Produits mis à jour : application de tri (334 personnages = 293 F + 41 M ; Top Danbooru étendu à 293, seuil Danbooru 6 892, 58 personnages communs ; tags rule34 Danbooru → rule34 corrigés pour Atago, Akebono, Shoukaku, Kyouko Kasodani, Ichirin Kumoi, Yamame Kurodani, Ishmael), franchises rule34 (`classement_franchises_293_…`, 117 franchises), Danbooru (`classement_franchises_danbooru_293_…`, 54) et tous personnages (345 = 293 F + 46 M + 6 genre au choix, 120 franchises), tags de franchise des 14 nouvelles franchises (`franchises/tags_franchise/ajout_releve_311-330.py`), application TierMaker et comparaison de périmètre (89 personnages dans le périmètre ; vignettes reprises du cache).
- Les 5 masculins de ce relevé ne sont pas dans l'application de tri ; ils comptent seulement dans le classement des franchises « tous personnages ».
- Place : fichiers remplacés compressés en `.gz` (sélections 175/217/229/242/243/255, autres tags 175/189, franchises et sélection Danbooru 217/243/256, médium v8) ; `doublons/selection_256_dedupliquee_audit` reste en clair (lu par d'anciens scripts).

## Filtre Copyright et pages numérotées dans EdeniaList (25/10/2026)

- `app_tri/donnees_copyright.py` → `app_tri/donnees_copyright_2026-10-25.json` : 47 tags rule34 de type Copyright (type vérifié un par un), associés par franchise. Les règles et les taux de co-tag mesurés sont en tête du script.
- `app_tri/build.py` injecte ce JSON à la place de `/*DATA_C*/`.
- `modele.html` : panneau « Filtre Copyright » (1 clic = inclure ✓, 2 clics = exclure ✗, 3 clics = retirer ; mode « au moins un » ou « tous » ; « Tout effacer »), ligne Copyright dans la fiche, colonne `copyright_rule34` dans l'export CSV, pagination numérotée.
- Couverture : 291 des 334 personnages de la sélection Rule34 et 88 des 293 du Top Danbooru ont au moins un tag.

## Tags Médium et type, option Espèces, barre des tags choisis (25/10/2026)

- `app_tri/donnees_especes.py` → `donnees_especes_2026-10-25.json` : 55 espèces (design défini, œuvre précise) sur les 62 du groupe « espèce » du fichier autres_212 ; 7 écartées (raisons dans le script). Compteurs Danbooru et e621 : `especes_api_2026-10-25.json` (API, 25/10). Furry : mêmes critères que classer_v9 (38 sur 55).
- `donnees_copyright.py` : groupe « Médium et type » (Animanga, Jeux vidéo, Comics, Cartoons, Autres = médium d'origine ; Furry ; Film ; Espèce), tags bethesda_softworks et bungie, franchises des espèces ; clé `e` dans le JSON.
- `modele.html` : option Espèces (Non par défaut, liste Rule34), barre « Tags choisis » cliquable (clic = exclure puis retirer, × = retirer), puces cliquables dans la fiche, filtre OU/ET appliqué séparément aux tags Copyright et aux tags Médium et type (ET entre les deux).

## Relevé des pages 331 à 340 et 5 garçons ajoutés (25 oct. 2026) — dossier `releves/releve_pages_331-340_2026-10-25/`

- Source : liste des tags triée par nombre de publications, pages 331 à 340 (pid 6600 à 6780) ; la page 340 se termine à 6 234 publications. Script : `construire.py` ; brut : `brut.txt` ; recherches négatives : `requetes_gains.json` et `pids.txt` ; Danbooru : `danbooru_nouveaux.py` (journal `danbooru_nouveaux.json`).
- **14 personnages féminins ajoutés** : Ayane et Honoka (Dead or Alive), Ashe (Overwatch), Tristana (League of Legends), Marinette Dupain-Cheng (Miraculous), Amity Blight (The Owl House), Anna (La Reine des neiges), Lois Griffin (Les Griffin), Bridget (Guilty Gear ; présentée comme femme trans depuis Strive, 2022), Hanabi Hyūga (Naruto), Futaba Sakura (Persona 5), Ragatha (The Amazing Digital Circus), Reine Marika (Elden Ring), Miyabi Hoshimi (Zenless Zone Zero).
- Aucun gain d'union au-dessus de 150 (Hanabi ≈ 147, les autres ≤ 21 ou variantes ≤ 102 en autocomplétion).
- Autres tags (11) : 4 masculins (Ren Amamiya, Superman, Wolf O'Donnell, Ganondorf), 1 genre au choix (Robin de Fire Emblem), 3 espèces (Mangriff, Deathclaw, Guilmon), 3 doublons (marin_kitagawa et yaoyorozu_momo, déjà dans les unions de Marin et Momo ; saber, tag de classe de Fate non additionné).
- Nouveaux fichiers : `selection_306_personnages_feminins_2026-10-25.csv`, `doublons/selection_307_dedupliquee_audit_2026-10-25.csv`, `autres_tags_personnages_223_hors_feminins_2026-10-25.csv`, `classement_par_medium/classer_v10.py` → `classement_r34_par_medium_v10_2026-10-25.csv/.md`.
- Seuil : 6 264 publications (Miyabi Hoshimi, rang 307). Médium v10 : Animanga 78, Jeux vidéo 133, Comics 16, Cartoons 38, Furry 35, Hors 7.
- **5 garçons des pages 311-330 ajoutés à l'application** (`EXTRA_M` de `app_tri/donnees.py`) : Dick Grayson (+189), Jax (+231, Furry : indice e621 3,39), Shining Armor (Furry : 5,79 ; non audité), Ichigo Kurosaki (+189), Sacha / Ash Ketchum (gain 0).
- Application de tri : 353 personnages (307 F + 46 M), 58 espèces en option (Furry 41) ; Top Danbooru étendu à 307 (seuil 6 780 images, données Danbooru du 24/10, 61 personnages communs) ; franchises : `franchises/classement_franchises_307_2026-10-25.*`, `classement_franchises_danbooru_307_2026-10-25.*`, `classement_franchises_tous_personnages_2026-10-25.*` (364 personnages : 307 F, 50 M, 7 au choix) ; tags de franchise des 6 nouvelles franchises : `franchises/tags_franchise/ajout_releve_331-340.py`.
- Copyright : arc_system_works (Guilty Gear), fromsoftware (Elden Ring), 20th_century_fox (Les Griffin), kodansha (Monogatari), bethesda_softworks pour Fallout (franchise rachetée : fallout ∧ bethesda_softworks ≈ 5 145 / 18 913 = 27 %). Miraculous : aucun tag de studio trouvé.
- TierMaker : périmètre Comics + Cartoons + Furry = 94 personnages (Marinette, Amity, Anna, Lois et Ragatha entrent) ; `comparer_perimetre.py` et `app_tiermaker/build.py` relancés.
- Place : fichiers remplacés compressés en `.gz` (sélections 292/293, autres 212, médium v9, franchises 293, Danbooru 293 et tri top 600 du 24/10, tous personnages du 24/10). À décompresser avant de relancer les anciens scripts (`releve_pages_311-330/construire.py`, `classer_v9.py`, `choisir_tags.py`). Le dossier `uploads/` n'est jamais supprimé.

## Catégorie de filtre « Espèce » dans EdeniaList (25/10/2026)

- Correction de la demande précédente : l'option Espèces (désactivée par défaut) reste telle quelle (ajout des fiches d'espèce rule34 au classement). En plus, le panneau de filtres a maintenant un groupe **Espèce**, comme « Médium et type » : cliquer sur « Inkling » garde les personnages Inkling (Callie, Marie, et la fiche Inkling si l'option est activée).
- Périmètre (ton choix, option 1) : espèce ou race définie par son œuvre ; pas de tag Humain (ni l'humain de WoW), pas d'animaux réels, pas de créatures génériques du folklore (démon, vampire, elfe, ange, fée, dragon, oni, kitsune…) ni de robots. Les yôkai de Touhou ne sont pas inclus, sauf Lunarien, Lapin lunaire et Demi-fantôme.
- Fichier : `app_tri/especes_filtre.py` (ESP = espèces avec note, PERSO = personnage → espèces, FRANCHISE = KanColle et Uma Musume en entier, FICHE = fiches de l'option qui partagent le tag, DOUTE = cas laissés sans espèce). Importé par `donnees_copyright.py` (tags `s:…`, famille k = 's').
- Résultat : 98 tags (49 espèces d'œuvres + 49 fiches de l'option sans équivalent) ; 65 des 353 personnages Rule34 et 55 des 307 du Top Danbooru ont au moins une espèce.
- `modele.html` : ligne « Espèce » dans la fiche (puces cliquables), colonne `espece` dans l'export CSV, logique ET entre les trois familles (Médium et type, Espèce, Copyright). Le tag de Médium « Espèce » est renommé « Fiche espèce (option) ».

## Relevé des pages 341 à 360 (25 oct. 2026) — dossier `releves/releve_pages_341-360_2026-10-25/`

- Source : liste des tags triée par nombre de publications, pages 341 à 360 (pid 6800 à 7180), de 6 234 à 5 693 publications. Brut : `brut.txt` (47 tags de personnage + 28 tags Copyright ; numéro de page exact de chaque tag non noté, colonne page = « 341-360 »). Script : `construire.py` ; recherches négatives : `pids.txt` ; Danbooru : `danbooru_nouveaux.py/.json`. Outil d'autocomplétion : `outils/ac.py`.
- **29 personnages féminins ajoutés** : Vi, Ivy Valentine, Gawr Gura, Misato Katsuragi, Trixie, Tenten, Felicia, Kit (Gameoverse), Hestia, Max Caulfield, Sayori, Vaggie, Mitsuki Bakugo, Kallen Stadtfeld, Melony, Raven Team Leader, Lapis Lazuli, Chara (version féminine, `female_chara`), Lucy (Edgerunners), Katarina, Shuuko Komi, Firefly, Taihou, Edelgard, Mavuika, Patchouli Knowledge, Ghislaine Dedoldia, Star Butterfly, Tharja.
- Gain d'union au-dessus de 150 : Vi seulement (`vi_(league_of_legends) -vi` ≈ 189 → 6 411). Les autres ≤ 147 (Misato), 105 (Trixie, Mitsuki), 63 (Felicia, Katarina) ou ≈ 21 / 0.
- Autres tags (18) : 7 masculins (Luigi, Robin (DC), Beerus, Boruto, Zoro, Gohan, Gojo ; pas ajoutés à l'application, comptés dans les franchises « tous »), 2 genre ambigu / au choix (Ranma Saotome, Villageois·e d'Animal Crossing), 8 doublons (orihime_inoue 0, rangiku_matsumoto 0, ashley_graham_(ella_freya) ≈ 21, jill_valentine_(julia_voth) ≈ 21, sailor_moon et chel_(…) déjà dans leur union, clark_kent = Superman, midnight_lycanroc = forme de Lycanroc), 1 exclu (`jaiden` : avatar d'une personne réelle, la YouTubeuse·eur Jaiden Animations ; groupe « exclu »).
- Chara : la version féminine entre dans la sélection ; le tag `chara` (genre au choix, 7 814) est retiré du classement des franchises « tous » pour ne pas compter Chara deux fois (même règle que Byleth, Shepard, Kindred).
- Nouveaux fichiers : `selection_335_personnages_feminins_2026-10-25.csv`, `doublons/selection_336_dedupliquee_audit_2026-10-25.csv`, `autres_tags_personnages_241_hors_feminins_2026-10-25.csv`, `classement_par_medium/classer_v11.py` → `classement_r34_par_medium_v11_2026-10-25.csv/.md`, `franchises/classement_franchises_336_2026-10-25.csv/.md`, `franchises/danbooru/selection_336_…` et `classement_franchises_danbooru_336_…`.
- Seuil : 5 693 publications (Tharja, rang 336). Médium v11 : Animanga 86, Jeux vidéo 147, Comics 16, Cartoons 41, Furry 38 (Kit : indice e621 3,48 ; Raven Team Leader 2,72 ; Trixie 6,57), Hors 8 (Gawr Gura). Felicia (2,28) reste en jeux vidéo (femme-chat humanoïde, comme Midna).
- Application : 382 personnages (336 F + 46 M). Top Danbooru étendu à 336 (seuil 6 336 images, 71 personnages communs) ; Northern Ocean Princess (apparence enfantine) : pas de compteur rule34 demandé, affiché 0. Nouveaux tags rule34 des autres noms Danbooru : `konata_izumi`, `kagami_hiiragi`, `yamada_ryou`, `minoriko_aki`, `kitakami_(kantai_collection)`, `don_quixote_(limbus_company)`, `kal'tsit_(arknights)`.
- Franchises : tous = 401 personnages (336 F, 57 M, 8 autres), 133 franchises ; filles 129 ; Danbooru 61. `tags_franchise/ajout_releve_341-360.py` : 14 lignes (rule34 : Azur Lane, Code Geass, DanMachi, Gameoverse, Life is Strange, Mushoku Tensei, Ranma ½, Soulcalibur, Star vs. les forces du mal ; Danbooru : Azur Lane, Lucky Star, My Dress-Up Darling, My Hero Academia, Omori).
- Copyright : Soulcalibur → bandai_namco, Life is Strange → square_enix, Star vs. → disney, Gameoverse → glitch_productions ; pas de tag retenu pour Code Geass, DanMachi, Mushoku Tensei, Azur Lane, Lucky Star, Omori.
- Espèce : nouvelles espèces Mewmain (Star), Homme-bête de Mushoku Tensei (Ghislaine), KAN-SEN (Azur Lane, toute la franchise), Abyssal (Northern Ocean Princess, exception à « Kanmusu ») ; Trixie → Licorne, Lapis → Gemme. Sans espèce (DOUTE) : Kit, Felicia, Raven Team Leader, Vaggie, Firefly. 102 tags ; 70 / 382 Rule34, 60 / 336 Danbooru.
- TierMaker : périmètre Comics + Cartoons + Furry = 100 (Vaggie, Lapis, Star, Kit, Raven Team Leader, Trixie entrent) ; `comparer_perimetre.py` et `app_tiermaker/build.py` relancés. Test Playwright de l'application : OK, aucune erreur JS.
- Place : fichiers remplacés compressés en `.gz` (sélections 306/307, autres 223, médium v10, franchises 307, Danbooru 307).

## Relevé des pages 361 à 390 (25 oct. 2026) — dossier `releves/releve_pages_361-390_2026-10-25/`

- Source : liste des tags triée par nombre de publications, pages 361 à 390 (pid 7200 à 7780), de 5 692 à 5 003 publications. Brut : `brut.txt`, notes et tags Copyright des 30 pages : `notes_pages.txt`, recherches d'union : `pids.txt`. Script : `construire.py`.
- **52 personnages féminins ajoutés** (rangs 294 à 388 de la liste dédupliquée), dont Ariel, Raiponce, Esdeath, Marisa Kirisame, Suguha (Leafa), Yukari Yakumo, Muffet, Undyne, Surge, Maître Tigresse, Tawna, Magik, Luna Snow, Ranma-chan, Corrin (version féminine), Valerie (V de Cyberpunk 2077), Kaguya Shinomiya, Chika Fujiwara, Jolyne, Poison, Rey, April O'Neil, la mère de Dexter, Haydee (dernière, 5 011).
- Gains d'union au-dessus de 150 : Ariel +1 491, Raiponce +903, Suguha +399 (`leafa`), Esdeath +315, Marisa +315, Yukari +189. Variantes ignorées (≤ 150) : détail dans `pids.txt`. Le tag `rapunzel` peut inclure `rapunzel_(nikke)` (347).
- Autres tags : 8 masculins (Falco, Gintoki, Ben Tennyson, protagoniste de Summertime Saga, Scout de TF2, Caelus, Vegeta, Naoto Hachiōji ; pas ajoutés à l'application, comptés dans les franchises « tous »), 9 doublons, 9 espèces, 2 catégories, 1 genre au choix (`v_(cyberpunk_2077)`).
- Nouveaux fichiers : `selection_387_personnages_feminins_2026-10-25.csv`, `doublons/selection_388_dedupliquee_audit_2026-10-25.csv`, `autres_tags_personnages_270_hors_feminins_2026-10-25.csv`, `classement_par_medium/classer_v12.py` → `classement_r34_par_medium_v12_2026-10-25.csv/.md`, `franchises/classement_franchises_388_*`, `franchises/classement_franchises_danbooru_388_*`, `franchises/danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv`, `franchises/tags_franchise/ajout_releve_361-390.py`.
- Médium v12 : Animanga 99, Jeux vidéo 169, Comics 18 (Magik, April O'Neil), Cartoons 50, Furry 43 (Muffet, Surge, Maître Tigresse, Tawna, Undyne), Hors 9 (Rey).
- Danbooru : tags des 52 relevés par `danbooru_nouveaux.py`, puis corrections à la main (magik_(x-men) 1 113 ; haydee_(haydee) 49 ; pas de tag pour Valerie, `v_(cyberpunk)` couvrant les deux V ; dexter's_mom 0).
- Application : 434 personnages (388 F + 46 M). Top Danbooru étendu à 388 (seuil 5 614 images, 81 personnages communs) ; tags rule34 de 13 nouveaux noms Danbooru (KanColle en `_(kantai_collection)`, `tsumugi_kotobuki_(k-on!)`, `mamizou_futatsuiwa`, `shizuha_aki`, `nikki_(infinity_nikki)`, `female_admiral_(kantai_collection)`).
- **Marvel Rivals → Jeux vidéo** (demande du 25/10) : les personnages jouables (Emma Frost, Femme invisible, Squirrel Girl, Psylocke, Malicia, Black Cat, Black Widow, Magik, Luna Snow, Spider-Man, Venom) reçoivent le tag de médium `m:jv` (`ROSTER` de `donnees_copyright.py`), en plus de Comics. Onglets de médium inchangés. Co-tag `marvel_rivals` : Magik 4 137 / 5 651 = 73 %, Luna Snow 5 313 / 5 510 = 96 %.
- Franchises : tous = 459 personnages (388 F, 65 M, 6 autres), 150 franchises ; filles 145 ; Danbooru 68. Corrin, Ranma et V retirés des « genre au choix » (déjà comptés par leur version féminine). `ajout_releve_361-390.py` : 24 lignes (17 rule34, 7 Danbooru).
- Copyright : Ranma ½ → shogakukan, Akame ga Kill! et Trials of Mana → square_enix, Kaguya-sama → shueisha, Final Fight → capcom, La Petite Sirène, Raiponce et Gravity Falls → disney, Dexter → cartoon_network, Dragons et Kung Fu Panda → dreamworks (ces 4 films ajoutés au tag Film). Les Tortues Ninja ∧ nickelodeon = 1 071 / 11 810 = 9,1 % → non. Pas de tag pour SAO, Roshidere, Dragon Maid, Haydee. Couverture : rule34 372 / 434, Danbooru 125 / 388.
- Espèce : nouvelles espèces Sheikah (Purah), Sankta (Exusiai), Halovien (Robin de Star Rail) ; Xayah → Vastaya, Vex → Yordle, Perle → Gemme, Muffet et Undyne → Monstre, Surge → Mobien, Magik → Mutant, Angelina → Vulpo ; Amiral (version féminine) exclue de « Kanmusu ». Sans espèce : Tohru, Ariel, Luna Snow, Marcille. Option Espèces : +9 (Orc de Warcraft, Luxray, Feunard, Malamandre, Tournesol de PvZ, Quarien, Riolu, Zeraora, Kirlia) → 67, dont 47 Furry. Groupe Espèce : 114 tags.
- TierMaker : périmètre Comics + Cartoons + Furry = 116 (111 + 5 espèces) ; `comparer_perimetre.py` et `app_tiermaker/build.py` relancés. Test Playwright : OK, aucune erreur JS.
- Place : fichiers remplacés compressés en `.gz` (sélections 335/336, autres 241, médium v11, franchises 336, Danbooru 336).

## Page « MyAnimeList » dans EdeniaList (25 oct. 2026)

- Nouvel onglet **MyAnimeList** : top 100 des personnages favoris de MAL (page « Most Favorited », `character.php` et `?limit=50`, relevé du 25/10/2026 ; pages brutes et extraction dans `myanimelist/brut/`).
- Données : `app_tri/donnees_mal.py` → `app_tri/donnees_mal_2026-10-25.json` (+ CSV `myanimelist/top100_personnages_favoris_mal_2026-10-25.csv`) ; nom affiché, œuvre et sexe ajoutés à la main (Hange Zoë et Rimuru Tempest : « non défini »). `build.py` injecte `/*DATA_M*/`.
- Résultat : 33 filles, 65 garçons, 2 non définis ; 4 230 891 favoris cumulés ; n° 1 Lelouch (181 648), n° 100 Rikka Takanashi (19 827).
- Lien avec EdeniaList : 33 personnages déjà présents (26 de la sélection Rule34, 3 du Top Danbooru : Shinobu Oshino, C.C., Homura ; 4 masculins des franchises au compteur du tag seul : Zoro, Gintoki, Gojo, Vegeta). Aucun nouveau compteur relevé.
- Interface : filtres Sexe et « Dans EdeniaList », recherche, tri par en-tête, ligne ▸ = ouvre la fiche, lien MAL. Test Playwright (bureau et mobile) : OK, aucune erreur JS.
- 25/10 : filtre Copyright `team_shanghai_alice` (cercle de ZUN, type Copyright, 1 421 publications) ajouté pour toute la franchise Touhou Project (`donnees_copyright.py`).

## Temporalité rule34 (25/10/2026) — `temporalite/`
- `releve_bornes_id.txt` : effectifs cumulés aux bornes d'ID (2M = 29/03/2016, 7M = 18/11/2022, 11 927 000 = 06/12/2024) et effectifs sans IA depuis déc. 2024, pour le top 20 général TierMaker.
- `parts_par_periode.py` → `top20_general_parts_par_periode_2026-10-25.csv` : posts par million d'ID attribués, par période, rangs, part IA récente.

## TierMaker par groupe de titres (25/10/2026) — `tiermaker_titres/`
- `classer_par_titre.py` (Playwright, réutilise `agreg()` de l'app) → `classement_par_groupe_de_titres_2026-10-25.csv` + JSON brut. Groupes : attirance (8 votes « Hottest/Hotties »), waifu (4), neutre (1, jeux vidéo).
