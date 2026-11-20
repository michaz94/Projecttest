# Favoris féminins MyAnimeList vs rule34, Danbooru et tier lists TierMaker (25 octobre 2026)

Base : les **33 personnages féminins** du top 100 des favoris MyAnimeList. MAL n'a pas de classement réservé aux filles ; la 33e, Rikka Takanashi, a 19 827 favoris.
Détail par personnage : `comparaison_feminines_mal_r34_danbooru_tiermaker_2026-10-25.csv` (script `comparer_feminins.py`).

## 1. Ce que mesure chaque source

| Source | Ce qui est compté | Qui « vote » | Ce que ça reflète surtout |
|---|---|---|---|
| **MAL – favoris** | membres qui ont ajouté le personnage à leurs favoris (cumul) | spectateurs d'anime inscrits sur MAL, filles et garçons mélangés | attachement au personnage : écriture, rôle dans l'histoire, œuvre culte |
| **rule34.xxx** | images explicites publiées avec le tag | dessinateurs, modeleurs 3D et publieurs, avec une forte part occidentale | attrait sexuel + volume de production des fans (3D, comics, jeux, anime récents très diffusés) |
| **Danbooru** | toutes les images (y compris tout public) avec le tag | illustrateurs, surtout dans le style japonais | présence dans le fan art japonais (gacha, Touhou, Madoka, Fate…) |
| **TierMaker** | moyenne des paliers S → D donnés par les votants | participants d'un vote, sur une liste d'images fixée par son créateur | jugement sur l'apparence (« waifu », « hottest ») |

## 2. Résultat chiffré

Corrélation de Spearman entre les favoris MAL et chaque mesure, sur les personnages qui l'ont :

| Mesure | ρ | n | Lecture |
|---|---:|---:|---|
| Publications rule34 | −0,08 | 31 | aucun lien (p = 0,67) |
| Images Danbooru | 0,20 | 33 | lien faible, non significatif (p = 0,26) |
| Rang dans « Best Anime Waifus 2025 » (99761754) | −0,30 | 19 | non significatif ; signe inverse (plus de favoris ≠ meilleur rang) |
| Rang dans « The Anime Waifu Tier List » (30081640) | −0,21 | 18 | non significatif |

Les autres votes contiennent trop peu de ces 33 personnages dans leur top 100 identifié (7, 5 et 4).

## 3. Exemples

- **Très aimées sur MAL, peu présentes ailleurs** : Kurisu Makise (1re fille MAL, 69 792 favoris ; 1 760 publications rule34 ; dans aucun top 100 de tier list), Hitagi Senjougahara (1 390), Taiga Aisaka (499), Violet Evergarden (890), Rikka Takanashi (608), Yukino Yukinoshita (1 679).
- **Énormes sur rule34, moyennes sur MAL** : Nico Robin (35 080 publications, 1re des 33 ; 25e fille MAL), Marin Kitagawa (29 857 ; 20e), Rias Gremory (17 248 ; 33e). Les filles d'anime les plus publiées sur rule34 (Nami 58 263, Hinata 44 141, Tsunade 40 786, Sakura 40 018, Ochako, Makima, Yor, Mirko, C-18) ne sont **pas** dans le top 100 MAL.
- **Danbooru ≠ rule34** : moyenne d'EdeniaList ≈ 39 images Danbooru pour 100 publications rule34. Homura Akemi : 30 350 contre 3 035 (1 000 pour 100) ; Taiga 703 ; Shinobu Oshino 470 ; Rikka 401 ; Saber 46 589 (227). À l'inverse : Rias 10, Marin 22, Robin 22.
- **Tier lists** : les têtes des votes anime sont Yor, Makima, 2B, Marin, Tsunade, Yoruichi, Mirko, Esdeath, Albedo. Parmi les tops 10, seules Marin, Mai Sakurajima, Robin et Rias sont dans le top 100 MAL. 11 des 33 favorites MAL ne sont dans le top 100 identifié d'aucun vote : Kurisu, Senjougahara, Shinobu, Taiga, Yuno, Holo, Homura, Kaori, Yukino, Revy, Rikka. Marin est la seule à être dans le top 10 de 4 votes.

## 4. Les tier lists anime ne mesurent pas toutes la même chose

| Vote | Images | Participants | Période | Particularité |
|---|---:|---:|---|---|
| 99761754 Best Anime Waifus 2025 | 311 | 19 274 | 20-27/08/2025 | 100 % anime ; le plus de participants, pour une liste courte |
| 30081640 The Anime Waifu Tier List | 2 050 | 3 530 | 24/09-01/10/2026 | anime/manga, avec quelques jeux (2B, Cynthia) ; très large liste, donc moins de votants par image : classement plus bruité |
| 87784832 Ultimate Fictional Animated Women | 1 310 | 9 150 | 16-23/10/2026 | tous dessins animés : l'anime y est en concurrence avec cartoons et jeux (2B, Mai Shiranui, Shego) |
| 80408816 Waifus Anime, Cartoon and Videogames | 381 | 11 877 | 17-24/08/2025 | tous médiums ; Raven, Hinata, Starfire, Chun-Li en tête |
| 436045 Cartoon Hotties | 295 | 7 894 | depuis le 21/10/2025 (pas de date de fin) | cartoons avant tout, environ un tiers d'anime |

Points communs : le créateur choisit les images (un personnage absent du modèle ne peut pas être classé), le titre oriente le critère (« hottest », « waifu »), et le vote porte sur une image, donc sur le design.

## 5. Limites

- MAL : une seule mesure (favoris), cumulée dans le temps, ce qui avantage les œuvres anciennes très vues (Code Geass, Steins;Gate, Monogatari, Toradora!).
- rule34 : 13 personnages relevés pour cette comparaison au tag seul (doublons non audités) ; pas de compteur pour les collégiennes de 14 ans (Yuno Gasai, Kaori Miyazono). Homura et Shinobu : compteurs déjà présents dans EdeniaList.
- TierMaker : seul le top 100 Average Vote est identifié ; « absente » veut dire « hors top 100 identifié ou absente du modèle », sans distinction ; images non identifiées exclues.
- Corrélations sur de petits effectifs (18 à 33) : elles montrent l'absence de lien fort, pas une valeur précise.
