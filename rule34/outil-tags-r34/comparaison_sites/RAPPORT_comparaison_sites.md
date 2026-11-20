# Comparaison des tags de personnages entre 5 sites (23 octobre 2026)

Relevé de l'IA. Personnages comparés : les **195 personnages individuels** retenus sur rule34.xxx (172 féminins + 23 masculins). Les espèces, catégories et doublons sont exclus.

## Sites et méthode

| Site | Contenu | Accès | Gestion des noms |
|---|---|---|---|
| rule34.xxx | Tout type, toutes origines | relevés du jour (pages 108 à 250) et autocomplétion pour les 24 tags du 27 sept. | tag rule34 |
| Danbooru | Surtout anime/manga, toutes classifications | API `tags.json` | alias officiels résolus (ex. `d.va` → `d.va_(overwatch)`) |
| Safebooru | Images tout public uniquement | API `dapi` | le plus grand des noms testés (rule34, Danbooru, e621) |
| Xbooru | Contenu adulte, petit site | API `dapi` | idem ; pas de fusion d'alias sur ce site |
| e621 | Surtout furry / anthropomorphe | API `tags.json` + alias | alias résolus, puis recherche par motif pour les cas restants |

Non utilisés : Gelbooru (API fermée sans clé), Realbooru (API hors ligne), rule34.paheal (noms sans qualificatif de série, trop ambigus), Konachan et yande.re (noms différents, compteurs à 0).

**Indice** = part du personnage sur le site ÷ sa part sur rule34. 1 = même poids ; 5 = cinq fois plus présent qu'attendu ; 0,1 = dix fois moins.

## Totaux des 195 personnages

| Site | Publications |
|---|---|
| rule34.xxx | 3 721 392 |
| Danbooru | 1 170 683 |
| Safebooru | 551 000 |
| Xbooru | 260 536 |
| e621 | 743 132 |

## Ressemblance des classements (corrélation de Spearman, 195 personnages)

| | Danbooru | Safebooru | Xbooru | e621 |
|---|---|---|---|---|
| **rule34** | 0,23 | 0,23 | 0,48 | 0,25 |
| **Danbooru** | | 0,90 | −0,10 | −0,15 |
| **Safebooru** | | | −0,05 | −0,05 |
| **Xbooru** | | | | 0,28 |

Lecture : 1 = même ordre, 0 = aucun lien. Danbooru et Safebooru ont presque le même classement ; rule34 ressemble le plus à Xbooru.

## Top 10 par site

- **rule34.xxx** : Nami 58 235 ; Tifa Lockhart 54 497 ; Princesse Peach 50 540 ; Rouge the Bat 45 404 ; Hinata Hyûga 44 131 ; 2B 43 042 ; Loona 43 037 ; Amy Rose 41 819 ; Hatsune Miku 41 502 ; Chun-Li 40 998
- **Danbooru** : Hatsune Miku 148 200 ; Reimu Hakurei 102 543 ; Artoria Pendragon 46 584 ; Lumine 22 523 ; Raiden Shogun 22 188 ; Link 21 401 ; Ganyu 20 296 ; Asuna 18 939 ; Asuka Langley 17 707 ; Tifa Lockhart 17 342
- **Safebooru** : Hatsune Miku 112 992 ; Reimu Hakurei 74 073 ; Link 14 259 ; Cloud Strife 10 074 ; Princesse Zelda 9 671 ; Asuka Langley 9 521 ; Frieren 8 572 ; Lumine 8 239 ; Ganyu 7 911 ; Furina 7 369
- **Xbooru** : Raven 11 453 ; Hinata Hyûga 7 590 ; Sakura Haruno 6 991 ; Amy Rose 6 663 ; Princesse Peach 6 152 ; Starfire 6 130 ; Kim Possible 6 056 ; Velma Dinkley 5 991 ; Rouge the Bat 5 982 ; Naruto Uzumaki 5 979
- **e621** : Twilight Sparkle 42 232 ; Judy Hopps 41 872 ; Rouge the Bat 34 625 ; Loona 32 882 ; Fluttershy 32 442 ; Nick Wilde 31 907 ; Rainbow Dash 31 071 ; Sonic 28 305 ; Rarity 27 460 ; Pinkie Pie 26 743

## Personnages les plus sur- et sous-représentés par rapport à rule34

- **Danbooru, plus présents** : Reimu Hakurei ×32,66 ; Hatsune Miku ×11,35 ; Artoria Pendragon ×7,7 ; Asuna ×5,19 ; Lumine ×4,68 ; Furina ×4,34 ; Cloud Strife ×4,31 ; Ganyu ×3,92 ; Rei Ayanami ×3,41 ; Rem ×3,4
- **Danbooru, moins présents** : Roxanne Wolf ×0,02 ; Toy Chica ×0,02 ; Spike ×0,04 ; Foxy ×0,04 ; Helen Parr (Elastigirl) ×0,04 ; Loona ×0,04 ; Liara T'Soni ×0,05 ; Princesse Luna ×0,05 ; Princesse Celestia ×0,05 ; Ellie ×0,06
- **Safebooru, plus présents** : Reimu Hakurei ×50,12 ; Hatsune Miku ×18,39 ; Cloud Strife ×5,67 ; Furina ×4,78 ; Rei Ayanami ×4,52 ; Rem ×3,75 ; Lumine ×3,63 ; Hu Tao ×3,38 ; Asuka Langley ×3,36 ; Ganyu ×3,25
- **Safebooru, moins présents** : Shadowheart (Cœur-Ombre) ×0,0 ; Helen Parr (Elastigirl) ×0,0 ; Girlfriend ×0,0 ; Liara T'Soni ×0,01 ; Chel ×0,01 ; Roxanne Wolf ×0,01 ; Toy Chica ×0,01 ; Jessica Rabbit ×0,02 ; Princesse Celestia ×0,02 ; Gwen Tennyson ×0,02
- **Xbooru, plus présents** : Kim Possible ×6,96 ; Velma Dinkley ×5,73 ; Cream the Rabbit ×4,36 ; Raven ×4,12 ; Starfire ×4,02 ; Jessica Rabbit ×3,55 ; Helen Parr (Elastigirl) ×2,58 ; Vanilla ×2,55 ; Gwen Tennyson ×2,53 ; Sakura Haruno ×2,5
- **Xbooru, moins présents** : Venom ×0,05 ; Wise ×0,08 ; Liara T'Soni ×0,09 ; Yae Miko ×0,09 ; Asuka Langley ×0,09 ; Aether ×0,1 ; Furina ×0,11 ; Hornet ×0,12 ; Lumine ×0,14 ; Jane Doe ×0,15
- **e621, plus présents** : Nick Wilde ×12,22 ; Judy Hopps ×8,02 ; Pinkie Pie ×6,87 ; Spike ×6,87 ; Twilight Sparkle ×6,85 ; Princesse Celestia ×6,69 ; Rainbow Dash ×6,5 ; Fox McCloud ×6,5 ; Princesse Luna ×6,46 ; Applejack ×6,27
- **e621, moins présents** : Ellie ×0,0 ; Asuna ×0,0 ; Sarada Uchiha ×0,0 ; Shinobu Kocho ×0,0 ; Marin Kitagawa ×0,0 ; Kushina Uzumaki ×0,01 ; Furina ×0,01 ; Eula ×0,01 ; Femme invisible (Sue Storm) ×0,01 ; Akeno Himejima ×0,01

## Personnages forts partout (rang moyen sur les 5 sites)

1. Princesse Zelda (15,8) ; 2. Tifa Lockhart (20,4) ; 3. Princesse Peach (21,4) ; 4. Sonic (22,4) ; 5. Link (23,0) ; 6. Hatsune Miku (23,4) ; 7. Samus Aran (30,4) ; 8. Amy Rose (31,2) ; 9. Nami (32,8) ; 10. Chun-Li (36,0) ; 11. Naruto Uzumaki (39,8) ; 12. Frieren (44,2) ; 13. May (Flora en VF) (45,0) ; 14. Nico Robin (46,8) ; 15. Rouge the Bat (48,8)

## Limites

- Les compteurs incluent toutes les classifications, sauf Safebooru (tout public seulement).
- Sur Safebooru et Xbooru, un même personnage peut être éclaté entre plusieurs noms. On garde le plus grand ; on ne peut pas additionner (une image peut porter les deux).
- Liste de départ = les personnages les plus tagués sur rule34. Les grands noms propres aux autres sites (ex. personnages de Touhou ou de Kantai Collection sur Danbooru) ne sont pas dans la liste, sauf s'ils sont aussi forts sur rule34.
- Les tags dérivés, comme `nami_(one_piece)_(cosplay)`, ne sont pas comptés.

Fichiers : `comparaison_sites_195_personnages_2026-10-23.csv` (tableau complet : tag et compteur sur chaque site, rangs, indices) ; données brutes et scripts dans `comparaison_sites/`.