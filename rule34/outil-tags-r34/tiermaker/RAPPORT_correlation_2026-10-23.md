# Tier list communautaire TierMaker et nombre de tags : y a-t-il une corrélation ? (23 oct. 2026)

**Source tier list :** modèle TierMaker « THE ULTIMATE FICTIONAL ANIMATED WOMEN TIER LIST [ONGOING] » (1 310 images), classement communautaire. L'API publique a renvoyé 20 listes (la page en annonce 34), dont 18 non vides ; 1 027 personnages au moins une fois classés. Fichiers bruts : `community_lists_4452917.json`, `template_images_test-run-3-125077.json`.

**Méthode :**
- Score « site » : même calcul que TierMaker (points par rangée, divisés par le nombre total de listes). Il reproduit le haut du classement affiché (2B, Tifa, Samus combinaison, D.Va en S).
- Score normalisé : position dans chaque liste ramenée entre 0 et 1, moyenne sur les seules listes où le personnage apparaît (rangées « Who? », « Don't know » et « furry » ignorées).
- 78 personnages identifiables par le nom de leur image, avec le nombre de posts Danbooru relevé le 23 oct. 2026 (`correspondance_danbooru.csv`).
- Corrélation de rang de Spearman.

**Résultats :**

| Comparaison | rho | p | n |
|---|---|---|---|
| Score normalisé / Danbooru | 0,41 | 0,0002 | 78 |
| Score site / Danbooru | 0,33 | 0,003 | 78 |
| Score normalisé / r34 (relevé du 27 sept.) | 0,63 | 0,04 | 11 |
| Danbooru / r34 | 0,71 | 0,015 | 11 |
| Accord entre deux listes individuelles (médiane) | 0,12 | — | 74 paires |

- Les 11 personnages du top r34 trouvés dans le modèle sont tous dans les 18 % du haut (sur 1 027) : 2B 1er, Tifa 2e, Samus 3e, D.Va 5e, Zelda 14e, Peach 29e, Chun-Li 36e, Makima 51e, Nami 104e, Widowmaker 115e, Lara Croft 183e.
- Les autres membres du top r34 (Hinata, Sakura, Miku, Rouge, etc.) n'ont pas été trouvés par nom de fichier : absents ou image au nom illisible. Purah non trouvée non plus.

**Limites :** peu de listes (18) ; échantillon de 78 non aléatoire (noms lisibles, surtout le haut du classement) ; le score site favorise les personnages ajoutés tôt au modèle ; tier list sur la « beauté » ; les compteurs Danbooru incluent toutes les classifications ; dates différentes. Corrélation ne veut pas dire causalité : la notoriété de la franchise peut expliquer les deux.

---

## Ajout : le vote en direct (live.tiermaker.com/87784832), 23 oct. 2026

**Accès :** API publique `server.tiermaker.com/v1/live-event/87784832`, qui donne la répartition S/A/B/C/D de chacune des 1 310 images. Fichier brut : `live_event_87784832_2026-10-23.json`. Le vote se terminait le 23 oct. à 10 h 23 UTC, avec 9 150 participants et 315 107 votes.

**Les deux vues recalculées :**
- « Average Vote » : moyenne avec S = 5, A = 4, B = 3, C = 2, D = 1.
- « Most Votes » : palier ayant reçu le plus de votes (le paramètre de l'événement est `voteCalculationBy: most_votes`). 1 049 images sur 1 310 ont D comme palier majoritaire ; ce critère est donc grossier.

**Biais majeur :** le nombre de votants par image chute avec sa position dans le défilement (de 3 450 pour la 1re image à 78 ; rho = -0,97). Les gens votent sur les premières images puis abandonnent. Le nombre de votes mesure donc surtout l'ordre de passage, pas la popularité.

| Comparaison (vote en direct) | rho | p | n |
|---|---|---|---|
| Average / Danbooru | 0,29 | 0,009 | 78 |
| Most Votes (palier majoritaire) / Danbooru | 0,29 | 0,011 | 78 |
| Average / r34 | 0,22 | 0,52 (non significatif) | 11 |
| Average du direct / score des 18 listes | 0,69 | — | 78 |

- Rang en Average (sur 1 310) des 11 personnages du top r34 : 2B 1re, Tifa 29e, Chun-Li 40e, Makima 43e, D.Va 50e, Samus 59e, Nami 60e, Lara Croft 124e, Widowmaker 182e, **Zelda 470e, Peach 517e** (palier majoritaire D pour ces deux-là).
- 9 sur 11 ont S comme palier majoritaire.
