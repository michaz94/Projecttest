# Analyse du catalogue MAL : séries Action, Fantasy / Surnaturel / Sci-Fi, Comedy et Romance

Date : 2026-10-07
Source : `data/catalogue_mal_shonen.json` (copie de `Benchmark Oeuvre/Myanimelist/catalogue_mal_shonen.json` du dépôt `michaz94/Projecttest`).

> **Qui dit quoi.** Les constats de départ sont les tiens (§1). Les chiffres sont calculés sur le catalogue. Les jugements sur les étiquettes « mal étiquetées » (§5 à §7) viennent de moi (IA), à partir de ce que je sais des prémisses des séries, pas du catalogue. Ce sont des propositions à valider ou à corriger.

---

## 0. Le catalogue

- **2 951 mangas** classés « Shounen » par MAL, publiés depuis 1980, collectés le 2026-09-30.
- **Action :** 1 154 séries. **Comedy :** 1 265. **Romance :** 743.
- Le filtre « Shounen » de MAL désigne un magazine de prépublication, pas un registre narratif (le fichier le précise). C'est pour cela que Comedy dépasse Action.
- Les genres sont des étiquettes multiples, attribuées par MAL. Les « thèmes » (School, Super Power, Vampire, etc.) sont une autre liste d'étiquettes.
- Manquants : 79 séries sans genre. Les manfras comme Radiant sont absentes.
- `membres` = personnes qui ont la série dans leur liste MAL. C'est une mesure de notoriété sur une plateforme anglophone, pas des ventes ni des lectures. Tous les classements « top N » ci-dessous sont faits par nombre de membres.

---

## 1. Tes constats de départ

1. La plupart des séries d'action sont aussi fantasy ou surnaturel. Le reste serait sci-fi, ou pas nommé comme tel (SNK « dark fantasy », MHA « Sci-Fi »).
2. La plupart des séries Comedy sont Romance, avec au moins 30 % de plus que l'action.

---

## 2. Vérification sur tout le catalogue

### Action

| Ce que tu dis | Résultat | Verdict |
|---|---|---|
| La plupart des Action sont Fantasy ou Supernatural | **58,2 %** (672 sur 1 154). Fantasy 37,5 %, Supernatural 27,4 %, les deux 6,7 %. | Confirmé |
| Le reste est Sci-Fi | Sur les 482 restantes, **30,1 %** sont Sci-Fi (145). **69,9 %** n'ont aucune des trois étiquettes (337). | Non confirmé |
| SNK n'est pas nommé fantasy ; MHA est « Sci-Fi » | SNK : Action, Award Winning, Drama, Suspense ; thèmes Gore, Military, Survival. MHA : Action seulement ; thèmes School, Super Power. | SNK confirmé. MHA n'est pas étiqueté Sci-Fi dans le catalogue. |

- Fantasy ou Supernatural ou Sci-Fi : 817 sur 1 154 (**70,8 %**).
- En comptant aussi des thèmes fantastiques (Super Power, Mythology, Mecha, Vampire, Isekai, Time Travel, Reincarnation, Space) : 873 sur 1 154 (**75,6 %**).
- Les 337 séries sans aucune des trois étiquettes sont surtout Action + Comedy (133), Drama, Adventure, Romance, Ecchi.
- Séries notées par au moins 1 000 personnes (532 séries Action) : Fantasy ou Supernatural = **64,8 %**. Au moins 10 000 notes (127 séries) : **64,6 %**.

### Comedy et romance

| Mesure | Catalogue entier | Notateurs ≥ 1 000 | Notateurs ≥ 10 000 |
|---|---|---|---|
| Part de Romance parmi les Comedy | **39,4 %** (499 / 1 265) | **51,1 %** | **58,3 %** |
| Part de Romance parmi les Action | **12,7 %** (147 / 1 154) | **17,3 %** | **13,4 %** |
| Écart (points) | 26,7 | 33,9 | 44,9 |
| Rapport | ×3,1 | ×3,0 | ×4,4 |

- « La plupart des Comedy sont Romance » : faux sur le catalogue entier (39 %), vrai pour les séries connues (51 % et 58 %).
- « Au moins 30 % de plus que l'action » : vrai en rapport (×3). En points, 26,7 sur le catalogue entier (légèrement sous 30), puis 34 et 45 pour les séries plus connues.
- Dans l'autre sens, **67,2 %** des Romance sont aussi Comedy.

---

## 2 bis. Autres mesures utiles (catalogue entier)

- Parts de Comedy parmi les Action : 29,6 % (342 / 1 154). Part d'Action parmi les Comedy : 27,0 % (342 / 1 265).

---

## 3. Limiter aux plus gros succès d'Action (par membres)

### Fantasy ou Supernatural, et Romance

| Palmarès | F ou S | Autres : Sci-Fi | Autres : ni l'un ni l'autre | Romance chez Action | Romance chez Comedy (même top) |
|---|---|---|---|---|---|
| Top 25 | **80 %** (20) | 0 sur 5 | 5 | 0 % (0) | 48 % (12) |
| Top 50 | **72 %** (36) | 2 sur 14 | 12 | 0 % (0) | 58 % (29) |
| Top 100 | **66 %** (66) | 7 sur 34 | 27 | 13 % (13) | 57 % (57) |
| Top 200 | **66 %** (131) | 10 sur 69 | 59 | 16 % (33) | 58 % (115) |
| Catalogue entier (rappel) | 58 % | 30 % | 70 % | 12,7 % | 39,4 % |

- Plus on se limite aux plus gros succès, plus la part de fantasy/surnaturel monte (58 % → 80 %).
- Le « reste = sci-fi » est encore moins vrai : dans le top 50, seules 2 séries sur 14 sont Sci-Fi (Evangelion, Gintama).
- Même classement par nombre de notateurs : résultats à 1 ou 2 points près.
- Top 25 et top 50 : petits échantillons (une série déplace le pourcentage de 2 à 4 points).

Top 10 par membres : Chainsaw Man, One Piece, Shingeki no Kyojin, Jujutsu Kaisen, Kimetsu no Yaiba, Boku no Hero Academia, Naruto, Bleach, Spy x Family, JoJo partie 7 (Steel Ball Run). Seuil du top 50 : 105 258 membres ; seuil du top 100 : 39 187.

---

## 4. Top 50 : en ajoutant les thèmes fantastiques

Thèmes comptés comme « fantastiques » (mon choix) : Super Power, Mythology, Vampire, Isekai, Time Travel, Reincarnation, Magical Sex Shift, Mahou Shoujo.

- **41 sur 50 (82 %)** ont un genre Fantasy/Supernatural ou un de ces thèmes. **43 sur 50 (86 %)** avec la sci-fi (genre Sci-Fi, thèmes Mecha et Space).
- Les thèmes font entrer 5 séries : My Hero Academia (Super Power), Tokyo Revengers (Time Travel), JoJo parties 1 et 2 (Vampire), Reborn! (Super Power).
- **9 séries restent** (7 sans la sci-fi) : SNK (3), Spy x Family (9), JoJo 6 (18), GTO (26), Ansatsu Kyoushitsu (31), Sakamoto Days (33), Evangelion (38, Sci-Fi), JoJo 5 (41), Gintama (50, Sci-Fi).

### Après correction des étiquettes (mon avis, voir §5)

- Seules **GTO et Sakamoto Days** restent sans élément fantastique, surnaturel ou sci-fi : **48 sur 50 (96 %)** (47 sur 50 si Spy x Family compte).

---

## 5. Séries mal étiquetées (mon avis)

Du top 50 : 4 séries sûres (SNK, JoJo 5 et 6, Ansatsu Kyoushitsu) ; Spy x Family discutable ; GTO et Sakamoto Days bien étiquetées.

Une incohérence **prouvée par le catalogue lui-même** : les JoJo parties 3, 4 et 7 sont étiquetées Supernatural, mais pas les parties 5 et 6, qui ont le même système de Stands.

---

## 6. Top 100 : les 25 séries sans genre ni thème fantastique

25 séries sur 100 n'ont ni genre F/S ni thème fantastique ; 7 d'entre elles sont Sci-Fi ; **18 restent**.

| Rang | Série | Verdict | Pourquoi |
|---|---|---|---|
| 3 | Shingeki no Kyojin | Mal étiquetée | Les Titans. |
| 18 | JoJo partie 6 | Mal étiquetée | Les Stands. |
| 41 | JoJo partie 5 | Mal étiquetée | Les Stands. |
| 31 | Ansatsu Kyoushitsu | Mal étiquetée | Le professeur est une créature aux pouvoirs surhumains. |
| 73 | Ranma ½ | Mal étiquetée | La malédiction de Jusenkyo. |
| 75 | Darwin's Game | Mal étiquetée | Les Sigils. |
| 56 | Highschool of the Dead | Mal étiquetée (MAL : Horror) | Les zombies. |
| 9 | Spy x Family | Discutable | La télépathie d'Anya (élément secondaire). |
| 91 | Mx0 | Je ne sais pas | Je ne la connais pas assez. |
| 97 | Yozakura-san Chi no Daisakusen | Je ne sais pas | Je ne la connais pas assez. |
| 26 | GTO | Bien étiquetée | Aucun élément fantastique. |
| 33 | Sakamoto Days | Bien étiquetée (je la connais moins) | Aucun élément surnaturel connu. |
| 51 | Rurouni Kenshin | Bien étiquetée | Combats exagérés, sans surnaturel. |
| 65 | Kenichi | Bien étiquetée | Arts martiaux exagérés. |
| 66 | Akumetsu | Bien étiquetée | Justicier dans un Japon réaliste. |
| 70 | Kishuku Gakkou no Juliet | Bien étiquetée | Comédie romantique d'école. |
| 72 | Angel Densetsu | Bien étiquetée | Comédie, sans surnaturel. |
| 88 | Yankee-kun to Megane-chan | Bien étiquetée | Comédie romantique de délinquants. |

Les 7 séries Sci-Fi de ce groupe : Evangelion (38), Gintama (50), World Trigger (79), Hokuto no Ken (80), Trigun (85), Apocalypse no Toride (90), Bloody Monday (96). Leur étiquette semble juste, sauf peut-être Bloody Monday (thriller de piratage), dont je ne suis pas sûr.

### Comptage

| Comptage | Séries avec un élément Fantasy/Supernatural/Sci-Fi (sur 100) |
|---|---|
| Étiquettes MAL (genres) seules | 73 |
| + thèmes fantastiques + Sci-Fi | 82 |
| Après mes 7 corrections | **89** |
| Fourchette selon mes doutes | 88 à 92 |

---

## 7. Top 100 : répartition Fantasy / Supernatural / Sci-Fi

### Selon les étiquettes MAL (73 séries ; aucune n'a les trois)

Totaux par genre : **Fantasy 42, Supernatural 30, Sci-Fi 12.**

**Fantasy seule (33)** : Chainsaw Man (1), One Piece (2), Kimetsu no Yaiba (5), Naruto (7), Fullmetal Alchemist (11), Hunter x Hunter (12), Fairy Tail (13), Black Clover (15), Claymore (17), Soul Eater (20), Noragami (22), Jigokuraku (24), Akame ga Kill! (25), Nanatsu no Taizai (27), Dragon Ball (28), D.Gray-man (29), Boruto (36), Owari no Seraph (40), Mashle (45), Kagurabachi (46), Gachiakuta (48), Mato Seihei no Slave (57), Tsubasa RESERVoir CHRoNiCLE (59), Gokurakugai (64), InuYasha (67), Eden no Ori (71), Sousei no Onmyouji (74), Black Cat (81), Toriko (82), Naruto Gaiden (83), Trinity Seven (84), Boruto Two Blue Vortex (92), Magi Sinbad no Bouken (100).

**Supernatural seule (22)** : Jujutsu Kaisen (4), Bleach (8), JoJo parties 7, 4 et 3 (10, 44, 49), Fire Punch (16), Dandadan (19), Ao no Exorcist (32), Jujutsu Kaisen 0 (39), Beelzebub (42), Mirai Nikki (47), Death Note Tanpenshuu (52), Imawa no Kuni no Alice (55), Air Gear (58), Yuu Yuu Hakusho (61), Shaman King (62), Undead Unluck (78), Bakemonogatari (86), Nurarihyon no Mago (87), Mahou Shoujo of the End (95), Defense Devil (98), Kamisama no Iutoori (99).

**Sci-Fi seule (7)** : Evangelion (38), Gintama (50), World Trigger (79), Hokuto no Ken (80), Trigun (85), Apocalypse no Toride (90), Bloody Monday (96).

**Deux étiquettes (11)**
- Fantasy + Supernatural (6) : Kuroshitsuji (30), Rosario to Vampire (53), Negima! (63), Rosario to Vampire Season II (69), Yu-Gi-Oh! (89), Shingeki no Kyojin: Before the Fall (94).
- Fantasy + Sci-Fi (3) : Kaijuu 8-gou (23), Enen no Shouboutai (35), UQ Holder! (77).
- Supernatural + Sci-Fi (2) : Deadman Wonderland (21), Psyren (54).

### Les 16 séries sans étiquette MAL, rattachées à un genre (mon choix)

- **Fantasy (3)** : Shingeki no Kyojin (3), Ranma ½ (73), Dragon Ball Super (60).
- **Supernatural (9)** : JoJo parties 1, 2, 5 et 6 (34, 43, 41, 18), Highschool of the Dead (56), Darwin's Game (75), Medaka Box (68), Code:Breaker (93), Reborn! (37).
- **Sci-Fi (4)** : My Hero Academia (6, d'après ton classement), Vigilante (76, même univers), Tokyo Revengers (14, voyage dans le temps), Ansatsu Kyoushitsu (31, hésitation avec Supernatural).

Totaux après ajouts : Fantasy 45, Supernatural 39, Sci-Fi 16 (une série à deux étiquettes est comptée dans les deux totaux, donc les totaux ne s'additionnent pas).

Le rattachement est un choix de classement : plusieurs séries pourraient aller ailleurs (Reborn! en Fantasy, Tokyo Revengers en Supernatural).

### Résultat : les séries ni Fantasy, ni Sci-Fi, ni Supernatural (11)

| Rang | Série | Certitude |
|---|---|---|
| 26 | GTO | Sûr |
| 51 | Rurouni Kenshin | Sûr |
| 65 | Kenichi | Sûr |
| 66 | Akumetsu | Sûr |
| 70 | Kishuku Gakkou no Juliet | Sûr |
| 72 | Angel Densetsu | Sûr |
| 88 | Yankee-kun to Megane-chan | Sûr |
| 33 | Sakamoto Days | Probable |
| 9 | Spy x Family | Discutable |
| 91 | Mx0 | Je ne sais pas |
| 97 | Yozakura-san Chi no Daisakusen | Je ne sais pas |

---

## 8. Limites et points ouverts

- Les étiquettes MAL sont éditoriales : « sans étiquette fantasy » ne veut pas dire « réaliste ». Les séries où le surnaturel est une règle du monde (Stands, Titans) ne sont pas toujours étiquetées.
- La liste des thèmes « fantastiques » est mon choix. Pour le top 100, j'ai aussi compté Urban Fantasy ; pour le top 50, non (sans effet sur le résultat).
- Le classement par membres mesure la notoriété sur MAL (plateforme anglophone), pas les ventes.
- Le catalogue ne contient que des mangas « shounen » (créneau de magazine). Le catalogue anime de MAL peut donner d'autres résultats ; je ne l'ai pas utilisé.
- À valider par toi : le rattachement des séries mal étiquetées (§5 à §7), et les trois cas incertains (Spy x Family, Mx0, Yozakura-san Chi no Daisakusen). Je ne connais pas assez Mx0 ni Yozakura-san.
- Rien de cette analyse n'est utilisé comme décision de conception pour Edenia. C'est une observation (tu m'as dit qu'elle n'a pas vraiment d'intérêt pour toi).
