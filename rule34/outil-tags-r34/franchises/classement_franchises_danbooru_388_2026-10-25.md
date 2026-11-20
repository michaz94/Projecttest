# Franchises les plus représentées sur Danbooru (personnages féminins)

*Relevé du 24 octobre 2026 (API Danbooru). Base : sélection propre à Danbooru, c'est-à-dire les **388 personnages féminins les plus fréquents** (même effectif que la sélection rule34), soit tous les tags de personnage féminin à au moins **5 614 images**. Danbooru compte toutes les images, pas seulement les explicites.*

**Méthode :**
- Top 600 des tags de personnage Danbooru (catégorie 4) triés par nombre d'images.
- Genre : part des images du personnage taguées `1girl` parmi `1girl` + `1boy` (seuil 0,55), vérifiée à la main ; Anya (Spy×Family) est comptée fille malgré un ratio de 0,52 (souvent avec Loid ou Damian).
- Exclus : personnages masculins ; avatars du joueur au genre au choix (Sensei de Blue Archive, Amiral de KanColle, Dresseur d'Uma Musume, Producteur d'Idolmaster, Docteur d'Arknights, Rover, Trailblazer, Guerrier de la Lumière FF14, Inkling/Octoling joueur, Commandant d'Azur Lane) ; Kris (Deltarune) et Paimon (genre non précisé) ; espèces et créatures (Gardevoir, Pikachu, Évoli, Motisma, Kyubey, Manjuu, Kirby, Boo Tao) ; objets animés (poupée Shanghai, Rensouhou-chan, Senketsu).
- **Pas de doublons à additionner** : sur Danbooru, un tag de version (Saber, Madoka en magical girl, Shigure Kai Ni, costumes…) ajoute automatiquement le tag parent (implication), donc le parent compte déjà ces images. Les versions sont retirées pour ne pas compter deux fois. Exception : Stelle et Rover (féminin) sont gardées, car leur parent est un avatar sans genre.
- Franchise : tag Copyright le plus associé au personnage (`related_tag`). Danbooru regroupe les sous-séries sous un tag parent (Fate, The Idolmaster, Love Live!, BanG Dream!, Gundam, Final Fantasy) ; seul Honkai est séparé entre Star Rail et Impact 3rd, comme pour rule34.
- **À trancher :** Mahiro Oyama (Onimai, garçon transformé en fille, 8 008 images) est classé ambigu et non compté ; s'il est compté fille, il entre à la place de Yumemi Riamu (The Idolmaster, 5 614). Les VTubers Hololive/Nijisanji sont comptées : Danbooru les classe comme personnages.

**68 franchises**, dont 27 avec un seul personnage. Fichiers de détail : `danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv`, `danbooru/tri_top600_personnages_danbooru_2026-10-25.csv` (chaque exclusion avec son motif).

## 1. Par nombre de personnages

Départage à égalité : images cumulées. Colonne rule34 = nombre de personnages de la franchise dans la sélection rule34 des 388.

| # | Franchise | Personnages | Images cumulées | Moyenne | rule34 | Personnages (images) |
|---|---|---|---|---|---|---|
| 1 | Touhou Project | 75 | 1 564 758 | 20 863 | 7 | Hakurei Reimu (102 567), Kirisame Marisa (88 697), Flandre Scarlet (64 114), Remilia Scarlet (63 424), Izayoi Sakuya (53 945), Komeiji Koishi (46 052), Kochiya Sanae (41 529), Konpaku Youmu (41 307), Cirno (41 297), Alice Margatroid (40 243), Patchouli Knowledge (39 339), Yakumo Yukari (39 002), Shameimaru Aya (34 655), Reisen Udongein Inaba (31 584), Komeiji Satori (31 407), Fujiwara No Mokou (30 991), Hong Meiling (28 523), Saigyouji Yuyuko (28 322), Inubashiri Momiji (26 361), Yakumo Ran (23 136), Kaenbyou Rin (23 007), Rumia (22 669), Moriya Suwako (22 258), Reiuji Utsuho (20 847), Chen (20 815), Kazami Yuuka (20 461), Tatara Kogasa (18 855), Kawashiro Nitori (18 831), Houraisan Kaguya (18 244), Hinanawi Tenshi (18 102), Kamishirasawa Keine (17 991), Koakuma (16 386), Mystia Lorelei (16 327), Nazrin (16 292), Ibuki Suika (16 203), Inaba Tewi (15 908), Usami Renko (15 726), Maribel Hearn (15 348), Hijiri Byakuren (14 790), Houjuu Nue (14 247), Yagokoro Eirin (13 507), Mizuhashi Parsee (13 328), Yasaka Kanako (13 304), Kagiyama Hina (12 344), Toyosatomimi No Miko (11 539), Daiyousei (11 526), Hoshiguma Yuugi (10 694), Mononobe No Futo (10 675), Shiki Eiki (10 655), Wriggle Nightbug (10 485), Onozuka Komachi (10 406), Imaizumi Kagerou (10 234), Toramaru Shou (9 024), Himekaidou Hatate (8 960), Murasa Minamitsu (8 758), Kaku Seiga (8 490), Hata No Kokoro (8 133), Ibaraki Kasen (7 760), Nagae Iku (7 715), Miyako Yoshika (7 600), Clownpiece (7 467), Junko (7 330), Kasodani Kyouko (7 252), Soga No Tojiko (7 248), Kumoi Ichirin (7 166), Kurodani Yamame (7 158), Sekibanki (6 849), Kijin Seija (6 800), Aki Minoriko (6 696), Hieda No Akyuu (6 473), Hecatia Lapislazuli (5 967), Sukuna Shinmyoumaru (5 946), Futatsuiwa Mamizou (5 839), Letty Whiterock (5 821), Aki Shizuha (5 807) |
| 2 | Kantai Collection | 40 | 390 026 | 9 751 | 0 | Kaga (22 236), Shimakaze (20 841), Hibiki (18 106), Shigure (17 858), Kongou (14 084), Inazuma (13 583), Akagi (13 023), Fubuki (12 988), Yuudachi (12 210), Tenryuu (12 042), Ikazuchi (11 471), Hamakaze (10 954), Zuikaku (10 785), Akatsuki (10 697), Haruna (10 502), Kashima (10 077), Nagato (9 842), Suzuya (9 665), Ryuujou (8 981), Houshou (8 366), Murakumo (7 801), Amatsukaze (7 791), Yamato (7 593), Yukikaze (7 478), Ushio (7 453), Atago (7 220), Akebono (6 994), Shoukaku (6 990), Ooyodo (6 799), Northern Ocean Princess (6 766), Kitakami (6 585), Asashio (6 297), Prinz Eugen (6 053), Mutsu (5 913), Amiral (version féminine) (5 707), Tatsuta (5 703), Takao (5 673), Ooi (5 648), Sendai (5 629), Musashi (5 622) |
| 3 | Blue Archive | 32 | 336 281 | 10 509 | 3 | Hina (20 083), Yuuka (19 286), Asuna (18 944), Mika (16 615), Hoshino (15 525), Rio (15 201), Kisaki (13 473), Toki (12 368), Aris (12 132), Kayoko (11 919), Mari (11 820), Shiroko (11 667), Kazusa (11 403), Koharu (10 418), Seia (9 726), Noa (8 748), Karin (8 717), Plana (8 621), Kei (8 030), Arona (8 011), Momoi (7 945), Aru (7 810), Hanako (7 685), Ako (7 150), Hasumi (7 122), Nozomi (6 972), Kanna (6 786), Midori (6 622), Saori (6 581), Hikari (6 465), Mutsuki (6 371), Neru (6 065) |
| 4 | Hololive (VTubers) | 31 | 304 171 | 9 812 | 4 | Houshou Marine (18 122), Gawr Gura (16 569), Shirakami Fubuki (16 277), Hoshimachi Suisei (15 473), Ouro Kronii (14 872), Ninomae Ina'nis (12 973), Mori Calliope (12 884), Usada Pekora (12 086), Nekomata Okayu (11 897), Takanashi Kiara (10 659), Sakura Miko (10 372), Tokoyami Towa (10 052), Nanashi Mumei (9 742), Minato Aqua (9 686), Ookami Mio (8 685), Oozora Subaru (8 074), Shiori Novella (7 989), Amane Kanata (7 895), Nerissa Ravencroft (7 811), Hakos Baelz (7 773), Yukihana Lamy (7 746), Watson Amelia (7 473), Inugami Korone (7 432), Shirogane Noel (7 428), Sakamata Chloe (7 086), Shishiro Botan (6 640), Fuwawa Abyssgard (6 402), Mococo Abyssgard (6 325), Irys (6 045), La+ Darknesss (6 004), Ceres Fauna (5 699) |
| 5 | Fate | 21 | 241 052 | 11 479 | 4 | Artoria Pendragon (46 589), Mash Kyrielight (21 101), Fujimaru Ritsuka (version féminine) (16 648), Jeanne d'Arc Alter (13 896), Abigail Williams (12 776), Nero Claudius (11 477), Illyasviel von Einzbern (11 232), Tohsaka Rin (11 022), Scathach (9 553), Tamamo no Mae (9 232), Jeanne d'Arc (8 810), Okita Souji (7 997), Baobhan Sith (7 909), Shuten Douji (7 868), Matou Sakura (6 927), Mordred (6 787), Minamoto No Raikou (6 698), Bb (6 633), Morgan Le Fay (6 349), Medusa (5 881), Ereshkigal (5 667) |
| 6 | Genshin Impact | 17 | 195 675 | 11 510 | 17 | Lumine (22 526), Raiden Shogun (22 191), Ganyu (20 301), Hu Tao (14 677), Furina (14 220), Nahida (13 637), Yae Miko (12 564), Columbina (10 163), Mona (10 025), Keqing (8 469), Kamisato Ayaka (7 422), Klee (7 279), Sandrone (7 225), Eula (6 504), Shenhe (6 420), Nilou (6 027), Arlecchino (6 025) |
| 7 | Love Live! | 15 | 109 313 | 7 288 | 0 | Hinoshita Kaho (9 217), Nishikino Maki (8 441), Yazawa Nico (7 875), Tojo Nozomi (7 838), Sonoda Umi (7 764), Fujishima Megumi (7 619), Momose Ginko (7 447), Otomune Kozue (7 306), Ayase Eli (7 286), Murano Sayaka (7 148), Watanabe You (6 788), Osawa Rurino (6 701), Anyoji Hime (6 096), Minami Kotori (5 929), Yugiri Tsuzuri (5 858) |
| 8 | Uma Musume | 11 | 100 315 | 9 120 | 0 | Agnes Tachyon (14 682), Manhattan Cafe (13 668), Gold Ship (11 256), Rice Shower (10 302), Daiwa Scarlet (9 151), Mejiro McQueen (8 921), Tokai Teio (7 366), Oguri Cap (7 006), Silence Suzuka (6 531), Nice Nature (5 723), Satono Diamond (5 709) |
| 9 | Pokémon | 10 | 80 557 | 8 056 | 19 | Dawn (9 689), Lillie (9 471), Rosa (9 091), May (8 947), Hilda (8 285), Marnie (8 247), Cynthia (7 824), Gloria (6 880), Serena (6 263), Iono (5 860) |
| 10 | Honkai: Star Rail | 9 | 84 566 | 9 396 | 2 | Firefly (16 858), Stelle (13 482), March 7th (9 803), Cyrene (9 293), Kafka (8 223), Sparkle (8 093), Acheron (6 907), Silver Wolf (6 238), Robin (5 669) |
| 11 | The Idolmaster | 9 | 58 209 | 6 468 | 0 | Shibuya Rin (7 495), Shinosawa Hiro (7 218), Kisaragi Chihaya (7 022), Hoshii Miki (6 870), Amami Haruka (6 385), Higuchi Madoka (5 990), Kikuchi Makoto (5 954), Shijou Takane (5 661), Yumemi Riamu (5 614) |
| 12 | Arknights | 8 | 61 271 | 7 659 | 0 | Amiya (12 466), Texas (8 753), Lappland (7 346), Skadi (6 972), Suzuran (6 926), Kal'tsit (6 734), Angelina (6 196), Exusiai (5 878) |
| 13 | BanG Dream! | 7 | 63 876 | 9 125 | 0 | Togawa Sakiko (11 951), Chihaya Anon (11 037), Nagasaki Soyo (9 641), Misumi Uika (8 143), Shiina Taki (8 028), Wakaba Mutsumi (7 765), Yahata Umiri (7 311) |
| 14 | Vocaloid | 5 | 202 168 | 40 434 | 1 | Hatsune Miku (148 218), Kagamine Rin (26 700), Megurine Luka (14 069), Meiko (7 090), Gumi (6 091) |
| 15 | Madoka Magica | 5 | 115 273 | 23 055 | 0 | Akemi Homura (30 350), Kaname Madoka (30 338), Miki Sayaka (20 387), Sakura Kyoko (17 230), Tomoe Mami (16 968) |
| 16 | Zenless Zone Zero | 5 | 43 424 | 8 685 | 8 | Belle (10 422), Ellen Joe (9 830), Remielle Dan (8 672), Hoshimi Miyabi (8 160), Jane Doe (6 340) |
| 17 | K-On! | 5 | 42 454 | 8 491 | 0 | Akiyama Mio (10 612), Nakano Azusa (9 313), Hirasawa Yui (8 991), Tainaka Ritsu (7 609), Kotobuki Tsumugi (5 929) |
| 18 | Girls und Panzer | 5 | 36 913 | 7 383 | 0 | Nishizumi Miho (10 781), Nishizumi Maho (7 095), Darjeeling (6 780), Itsumi Erika (6 336), Anchovy (5 921) |
| 19 | Bocchi the Rock! | 4 | 42 221 | 10 555 | 1 | Gotoh Hitori (18 203), Kita Ikuyo (9 488), Ijichi Nijika (7 858), Yamada Ryo (6 672) |
| 20 | Chainsaw Man | 3 | 28 322 | 9 441 | 4 | Makima (11 208), Reze (10 314), Power (6 800) |
| 21 | Honkai Impact 3rd | 3 | 27 989 | 9 330 | 0 | Elysia (13 901), Kiana Kaslana (8 140), Raiden Mei (5 948) |
| 22 | Cho Kaguya-hime! | 3 | 26 022 | 8 674 | 0 | Sakayori Iroha (10 852), Kaguya (7 966), Runami Yachiyo (7 204) |
| 23 | Final Fantasy | 2 | 29 492 | 14 746 | 2 | Tifa Lockhart (17 346), Aerith Gainsborough (12 146) |
| 24 | Evangelion | 2 | 28 318 | 14 159 | 3 | Souryuu Asuka Langley (17 707), Ayanami Rei (10 611) |
| 25 | UTAU / Synthesizer V | 2 | 27 047 | 13 524 | 1 | Kasane Teto (18 996), Adachi Rei (8 051) |
| 26 | Frieren | 2 | 26 354 | 13 177 | 2 | Frieren (16 473), Fern (9 881) |
| 27 | La Mélancolie de Haruhi Suzumiya | 2 | 20 484 | 10 242 | 0 | Suzumiya Haruhi (11 191), Nagato Yuki (9 293) |
| 28 | One Piece | 2 | 19 240 | 9 620 | 4 | Nami (11 332), Nico Robin (7 908) |
| 29 | Magical Girl Lyrical Nanoha | 2 | 18 479 | 9 240 | 0 | Fate Testarossa (10 093), Takamachi Nanoha (8 386) |
| 30 | Spy×Family | 2 | 18 456 | 9 228 | 1 | Yor Briar (11 618), Anya (6 838) |
| 31 | Xenoblade Chronicles | 2 | 18 101 | 9 050 | 2 | Pyra (9 603), Mythra (8 498) |
| 32 | KonoSuba | 2 | 17 828 | 8 914 | 3 | Megumin (10 967), Aqua (6 861) |
| 33 | Lycoris Recoil | 2 | 15 522 | 7 761 | 0 | Nishikigi Chisato (8 609), Inoue Takina (6 913) |
| 34 | Gundam | 2 | 15 439 | 7 720 | 0 | Suletta Mercury (8 112), Miorine Rembran (7 327) |
| 35 | Alien Stage | 2 | 15 380 | 7 690 | 0 | Sua (7 840), Mizi (7 540) |
| 36 | Girls Band Cry | 2 | 15 358 | 7 679 | 0 | Iseri Nina (7 928), Kawaragi Momoka (7 430) |
| 37 | Street Fighter | 2 | 15 200 | 7 600 | 4 | Chun-li (9 312), Cammy White (5 888) |
| 38 | Kemono Friends | 2 | 14 325 | 7 162 | 0 | Serval (8 411), Kaban (5 914) |
| 39 | Project Moon (Limbus Company) | 2 | 13 584 | 6 792 | 0 | Ishmael (6 892), Don Quixote (6 692) |
| 40 | Lucky Star | 2 | 13 156 | 6 578 | 0 | Izumi Konata (6 610), Hiiragi Kagami (6 546) |
| 41 | My Hero Academia | 2 | 12 536 | 6 268 | 9 | Mirko (6 552), Uraraka Ochaco (5 984) |

*Franchises à un seul personnage : The Legend of Zelda (Princess Zelda (17 092)), Danganronpa (Nanami Chiaki (14 101)), NieR (2B (12 524)), A Certain Magical Index / Railgun (Misaka Mikoto (10 943)), Re:Zero (Rem (10 404)), VOICEROID (Yuzuki Yukari (9 956)), Card Captor Sakura (Kinomoto Sakura (9 119)), Kill la Kill (Matoi Ryuuko (8 835)), Super Mario (Princess Peach (8 759)), Gochūmon wa Usagi Desu ka? (Kafuu Chino (8 324)), Metroid (Samus Aran (8 252)), Fire Emblem (Byleth (version féminine) (7 496)), Darkstalkers (Morrigan Aensland (7 320)), Tsukihime (Arcueid Brunestud (7 077)), Sailor Moon (Tsukino Usagi (6 915)), Monogatari (Oshino Shinobu (6 837)), Girls' Frontline (HK416 (6 823)), My Dress-Up Darling (Kitagawa Marin (6 578)), Omori (Aubrey (6 575)), Azur Lane (Taihou (6 490)), Sword Art Online (Asuna (6 132)), Fatal Fury / King of Fighters (Shiranui Mai (6 079)), Gloutons et Dragons (Dungeon Meshi) (Marcille Donato (5 965)), Code Geass (C.C. (5 893)), Nijisanji (VTubers) (Ange Katrina (5 755)), Nikki (Infinity Nikki) (Nikki (5 739)), Wuthering Waves (Rover (version féminine) (5 686)).*

## 2. Par images cumulées (top 25)

| # | Franchise | Images cumulées | Part des 388 | Personnages |
|---|---|---|---|---|
| 1 | Touhou Project | 1 564 758 | 33,1 % | 75 |
| 2 | Kantai Collection | 390 026 | 8,2 % | 40 |
| 3 | Blue Archive | 336 281 | 7,1 % | 32 |
| 4 | Hololive (VTubers) | 304 171 | 6,4 % | 31 |
| 5 | Fate | 241 052 | 5,1 % | 21 |
| 6 | Vocaloid | 202 168 | 4,3 % | 5 |
| 7 | Genshin Impact | 195 675 | 4,1 % | 17 |
| 8 | Madoka Magica | 115 273 | 2,4 % | 5 |
| 9 | Love Live! | 109 313 | 2,3 % | 15 |
| 10 | Uma Musume | 100 315 | 2,1 % | 11 |
| 11 | Honkai: Star Rail | 84 566 | 1,8 % | 9 |
| 12 | Pokémon | 80 557 | 1,7 % | 10 |
| 13 | BanG Dream! | 63 876 | 1,4 % | 7 |
| 14 | Arknights | 61 271 | 1,3 % | 8 |
| 15 | The Idolmaster | 58 209 | 1,2 % | 9 |
| 16 | Zenless Zone Zero | 43 424 | 0,9 % | 5 |
| 17 | K-On! | 42 454 | 0,9 % | 5 |
| 18 | Bocchi the Rock! | 42 221 | 0,9 % | 4 |
| 19 | Girls und Panzer | 36 913 | 0,8 % | 5 |
| 20 | Final Fantasy | 29 492 | 0,6 % | 2 |
| 21 | Chainsaw Man | 28 322 | 0,6 % | 3 |
| 22 | Evangelion | 28 318 | 0,6 % | 2 |
| 23 | Honkai Impact 3rd | 27 989 | 0,6 % | 3 |
| 24 | UTAU / Synthesizer V | 27 047 | 0,6 % | 2 |
| 25 | Frieren | 26 354 | 0,6 % | 2 |

## 3. Comparaison avec la sélection rule34

- **81 personnages sur 388** figurent dans les deux sélections : Hatsune Miku, Hakurei Reimu, Kirisame Marisa, Izayoi Sakuya, Artoria Pendragon, Kochiya Sanae, Patchouli Knowledge, Yakumo Yukari, Reisen Udongein Inaba, Lumine, Raiden Shogun, Mash Kyrielight, Ganyu, Kasane Teto, Asuna, Gotoh Hitori, Houshou Marine, Souryuu Asuka Langley, Tifa Lockhart, Princess Zelda, Firefly, Gawr Gura, Frieren, Rio, Ouro Kronii, Hu Tao, Furina, Mori Calliope, Yae Miko, 2B, Aerith Gainsborough, Yor Briar, Nami, Makima, Tohsaka Rin, Megumin, Ayanami Rei, Belle, Rem, Reze, Mona, Fern, Ellen Joe, Dawn, Pyra, Lillie, Chun-li, Rosa, May, Matoi Ryuuko, Princess Peach, Karin, Mythra, Keqing, Hilda, Samus Aran, Marnie, Kafka, Hoshimi Miyabi, Nico Robin, Cynthia, Byleth (version féminine), Kamisato Ayaka, Morrigan Aensland, Tsukino Usagi, Gloria, Aqua, Power, Minamoto No Raikou, Kitagawa Marin, Mirko, Eula, Taihou, Shenhe, Jane Doe, Serena, Asuna, Shiranui Mai, Arlecchino, Uraraka Ochaco, Cammy White.
- Franchises à au moins 3 personnages dans la sélection rule34 mais **absentes** des 388 de Danbooru : League of Legends (19), Marvel (12), My Little Pony (11), Overwatch (11), Naruto (10), DC Comics (9), Sonic (7), Dragon Ball (7), Resident Evil (5), Bleach (5), RWBY (5), Avatar (Le Dernier Maître de l'air + La Légende de Korra) (5), Undertale (4), Doki Doki Literature Club (4), Persona 5 (4), Dead or Alive (4), Hololive (4), The Witcher (3), Demon Slayer (3), Five Nights at Freddy's (3), Mass Effect (3), Splatoon (3), Miss Kobayashi's Dragon Maid (3), Adventure Time (3), Cyberpunk 2077 (3), Steven Universe (3). Leurs personnages ont moins de 5 614 images sur Danbooru, par exemple Raven (39 707 publications sur rule34, 1 954 images sur Danbooru) ou Loona (43 049 contre 592).
- Franchises très présentes sur Danbooru mais (presque) absentes de rule34 : Kantai Collection (40 contre 0), Love Live! (15 contre 0), Uma Musume (11 contre 0), The Idolmaster (9 contre 0), Arknights (8 contre 0), BanG Dream! (7 contre 0), Vocaloid (5 contre 1), Madoka Magica (5 contre 0), K-On! (5 contre 0), Girls und Panzer (5 contre 0).
- Interprétation (non mesurée) : Danbooru est une base d'illustrations surtout japonaises (fan art, doujin, tout public compris) ; rule34.xxx est un site explicite avec une forte part occidentale (comics, cartoons, furry, jeux occidentaux). Les deux classements mesurent donc deux publics différents.
