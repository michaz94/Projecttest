# Addendum — MAL, voix japonaises, Manga Plus, sommaires en parallèle, grille de lecture par chapitre

Complète `Analyse_critiques_recurrentes_Red_Hood_et_comparaison_series_longues_2026-09-29.md` (même dossier). **Mis à jour le 2 octobre 2026** avec la vérification des 18 planches du chapitre 1 de *Red Hood* (`p000`–`p017`) et l'extraction des 3 couches JSON de réception pour *Fullmetal Alchemist*, *Hunter × Hunter*, *Jujutsu Kaisen* et *One Piece*. Répond aux manques signalés le 29 septembre : absence de lecture chapitre par chapitre, sommaires non mis en parallèle, MAL et opinions japonaises non exploités, Manga Plus absent, comparateurs non testés contre les sept questions du §6.

Convention inchangée : **[D]** = documenté (source citée, vérifiable) ; **[I]** = interprétation ; **[H]** = hypothèse à tester.

---

## 0. Ce que cet addendum ajoute, et ce qu'il ne règle pas

Ajouté aujourd'hui :

- les 20 critiques MAL de Red Hood, datées et classées (`mal_reviews_red_hood_2026-09-29.csv`) ;
- des sources japonaises non utilisées jusqu'ici : un fil 5ch d'août 2021 (au moment du ch. 9), un blog spécialisé dans les séries arrêtées de Jump, trois réponses Yahoo! Chiebukuro (8 nov. 2021), les 9 avis lecteurs Bookmeter du tome 1 et les 6 avis mechacomic ;
- les positions au sommaire (ToC) des 20 premiers chapitres de One Piece et Hunter × Hunter, ajoutées à celles déjà en dépôt (Naruto, Bleach, MHA, JJK, 5 séries courtes) et mises en parallèle avec Red Hood (`toc_premiers_chapitres_parallele_…csv`) ;
- une grille de lecture par chapitre construite sur les questions Q1–Q7 du §6, pré-remplie pour Red Hood (18 ch.), One Piece, HxH et JJK (10 ch. chacun), avec le **niveau de preuve indiqué ligne par ligne** (`grille_lecture_par_chapitre_Q1-Q7_2026-09-29.csv`).

Non réglé, et à dire clairement :

1. **Je n'ai lu les planches d'aucune de ces séries.** Je ne peux pas ouvrir Manga Plus, Shonen Jump+ ni un scan ; ce que je « sais » des chapitres vient de résumés publics, de mémoire et des commentaires de lecteurs. Pour Red Hood, la grille ne contient que ce que le corpus de commentaires ou les blogs japonais attestent ; le reste est marqué « à remplir à la lecture ». Pour OP/HxH/JJK, les lignes sont marquées « mémoire + résumés — à vérifier ». Ce n'est pas la lecture empirique que vous décrivez ; c'est son échafaudage. La lecture elle-même, vous pouvez la faire (vous avez les lecteurs légaux) ; moi non.
2. **Manga Plus** : l'API a refusé la connexion depuis mon environnement (réponse « Account Banned » sur la première requête, cf. §4). Aucune donnée Manga Plus n'a donc été obtenue. Le §4 dit ce que vous pouvez relever vous-même en un quart d'heure et ce que cela prouverait ou non.
3. **MAL n'est pas une source japonaise.** MyAnimeList est un site anglophone ; ses critiques relèvent du public occidental (surtout nord-américain). Les voix japonaises sont au §3.

---

## 1. Trois niveaux de preuve, désormais explicites

| Niveau | Ce que c'est | Où dans les fichiers |
|---|---|---|
| A — mesures | ToC Jajanken, notes et effectifs Goodreads/Bookmeter/mechacomic/MAL, comptes de commentaires par chapitre | CSV ToC, codage par chapitre, CSV MAL |
| B — paroles de lecteurs | Reddit (4 432 commentaires), MAL (20 critiques + forum), 5ch/blogs/Chiebukuro/Bookmeter (japonais) | analyse principale §3, cet addendum §2–3 |
| C — faits structurels des chapitres | qui apparaît, ce que le héros fait, ce qui est perdu, quand l'objectif est dit | grille Q1–Q7 — **niveau le plus faible tant que les planches ne sont pas lues** |

Toute conclusion de type « voilà ce que OP fait autrement » repose sur C. Elle devient solide seulement quand une lecture des planches confirme la ligne de la grille.

---

## 2. MAL : 20 critiques (anglophones), ce qu'elles ajoutent

**[D] Effectifs.** 23 critiques affichées par MAL, 20 lisibles sans compte. Verdicts : 9 Recommended, 6 Mixed, 5 Not Recommended. Huit sont des critiques *préliminaires* écrites pendant la publication (juin–nov. 2021, entre le ch. 1 et le ch. 11) : 5 Recommended, 2 Mixed, 1 Not Recommended. Les douze écrites après la fin (nov. 2021 → mars 2025) se répartissent 4 / 4 / 4. **[I]** Même dessin que sur Reddit vs Goodreads : ceux qui écrivent *pendant* sont favorables ; le jugement rétrospectif est partagé.

**[D] Convergences avec Reddit** (déjà dans l'analyse principale, confirmées ici) : héros fade (« just another Deku/Tanjiro/Asta clone », « Velou is extremely dull »), trop de personnages d'un coup (« a TON of characters… while we still don't know the main character »), examen trop long et sans enjeu (« from chapter 7 to 14 stuck in a boring overcomplicated game » ; Giblow_20 : « like if HxH had Gon instantly put into the running portion of the exam for 10 chapters »), méta rejeté par ceux qui aimaient le début (Ciaran_Zagami : tomes 1–2 aimés, tome 3 détesté).

**[D] Ce que MAL apporte de neuf** (peu visible sur Reddit, où la discussion est hebdomadaire et courte) :

1. **La page elle-même.** jahver : « 8–10 speech bubbles on most pages », rien ne guide l'œil, avec une compilation d'images à l'appui (imgur.com/gallery/CF60TgJ). Chesed : « pages covered in speech bubbles ». ninjamrd : « walls of text ». dankchungus : cases « jammed », phylactères « in wrong spots ». **C'est la critique la plus proche d'une lecture de planches qui existe dans les corpus**, et elle recoupe mot pour mot les Japonais (§3 : « コマ割りや構図がごちゃごちゃ », « 説明コマにページが埋まる »). Elle ne figure pas dans les cinq critiques structurelles de l'analyse principale parce que Reddit en parle peu ; elle doit y être ajoutée comme sixième point, de nature différente : ce n'est pas un choix de récit mais de fabrication de page.
2. **Le refus de l'appel.** Sheev-san : à la fin du ch. 1 Velou refuse de suivre Grimm ; au ch. 5 il reçoit le même appel et l'accepte — « what was the point? ». Quatre chapitres pour revenir au point de départ dramatique. **[I]** C'est la version narrative précise du grief « prologue trop long » : ce n'est pas la longueur, c'est l'absence de déplacement du héros entre le ch. 1 et le ch. 5.
3. **La contradiction thématique.** Another_Badger : le discours de Grimm (les loups « ni bons ni mauvais », prédation sans morale) est démenti par des loups uniquement cruels ; le retour du maire est lu comme un appât ; les flashbacks disent au lecteur quoi ressentir avant qu'il ait pu se faire un avis. Sur Reddit, X-Vidar aimait justement ce discours au ch. 1, et Terrestrious (MAL, ch. 1) notait déjà la contradiction : **la promesse thématique du ch. 1 a été perçue, puis vue comme non tenue**.
4. **La chute du dessin.** Raiden316 : qualité en baisse après le ch. 1, derniers chapitres presque sans décors. Corrobore Chiebukuro (§3).
5. **Une heuristique de lecteur : les « 3 G » de Jump** (Giblow_20) — Guy, Goal, Gimmick, à poser au ch. 1. Red Hood n'aurait rempli que le Gimmick (les armes-contes de Grimm), en cinq chapitres. **[I]** Ce n'est pas une règle, c'est ce qu'un lecteur attentif *cherche* dans un ch. 1 de Jump ; c'est utile comme miroir de la Q1 (horizon) et de la Q2 (présence).

**[D] Côté positif**, toutes les critiques favorables citent le dessin, l'univers, « le potentiel », les femmes musclées ; SonTOSHI (Mixed) : combats « abstract art », « boring week to week ».

---

## 3. Voix japonaises : la même liste, dans le même ordre

Sources (toutes [D], consultées le 29/09/2026) :

- fil 5ch du 24–25 août 2021 (relayé par anige-sokuhouvip.com et manga.itsys-tech.com), c'est-à-dire *au moment du ch. 9*, quand l'augmentation de pages a été lue comme signal d'arrêt ;
- utikirimanga.hatenadiary.com (blog consacré aux séries arrêtées de Jump), billet du 1er avril 2022 ;
- Yahoo! Chiebukuro, « Red Hood a été arrêté. Qu'est-ce qui n'allait pas ? », 3 réponses du 8 nov. 2021 ;
- Bookmeter, tome 1 : 51 inscrits, 45 « lu », 9 avis (avec votes « Nice ») ;
- mechacomic : 6 avis, moyenne 2,2/5 ;
- blog Yarukimedesu (déjà dans le corpus) ;
- Amazon.jp (précommandes, déjà dans l'analyse principale).

### 3.1 Convergence point par point

| Critique occidentale (analyse principale §3) | Formulation japonaise [D] |
|---|---|
| 3.5 Prologue trop long / héros qui ne bouge pas | 5ch : « One Piece quitte le village de Fuusha **au ch. 1** ; Red Hood quitte enfin le premier village **au ch. 5** » ; « いつまで村にいるんだ » (« jusqu'à quand restent-ils au village ? ») ; mechacomic : « le one-shot étalé sur 3–4 chapitres, c'est ça l'erreur ; trop lent, ça a scellé son sort » |
| 3.3 L'examen suspend la promesse | mechacomic : « il aurait fallu résoudre quelques affaires de plus avant l'examen » ; 5ch : « si l'arc examen commence avant le ch. 10, c'est la voie de l'arrêt » (heuristique de lecteur) ; utikirimanga : « six chapitres pour des compagnons peu caractérisés et une épreuve tiède où personne ne meurt… c'est là, honnêtement, que l'arrêt s'est décidé » |
| 3.2 Casting élargi avant le duo | utikirimanga : Bremen « apparaît de façon signifiante et sort en 5 pages — était-ce nécessaire ? » ; « beaucoup de personnages, aucun creusé » |
| 3.1 Héros sans présence | 5ch : « le héros faible et le gros [Grimm] s'annulent : pour faire briller un héros faible, on rend Grimm incompétente, et le héros n'en paraît que plus factice » ; « aucune empathie possible, même pour le camp du héros ; pas une scène émouvante » |
| 3.4 Enjeux désamorcés | 5ch : « la défense du village, censée être l'accroche, est longue et ne débouche sur rien ; Grimm retient ses coups pour recruter/former et le village est détruit » ; Chiebukuro : « aucune tension du début à la fin » |
| Lisibilité / densité (MAL §2.1) | Chiebukuro : « découpage et compositions brouillons, difficile à lire » ; Bookmeter (avis le plus voté, 12 Nice) : « les explications de setting sont très longues et monotones ; que de l'explication, aucune accumulation de mise en scène… dommage que les pages se remplissent de cases explicatives alors que les grandes cases sont belles » ; 5ch : « dessin et setting entassés à la va-vite, ça n'entre pas dans la tête » |
| Méta mal reçu | Chiebukuro : « le méta final donne l'impression de rejeter la faute sur les lecteurs » ; utikirimanga : le méta a été *ajouté* pour la sérialisation (le one-shot était un shōnen classique) et « aurait mieux valu consacrer ces pages aux personnages et aux combats » |
| Dessin en baisse | Chiebukuro (réponse la plus complète) : « le dessin était l'atout, et le coût de production a baissé au fil des semaines » ; « pas fait pour l'hebdomadaire, sans marge » |

**[I]** Sur les six critiques structurelles, la liste japonaise est identique à la liste occidentale, avec en plus une insistance sur la *fabrication* (lisibilité, dessin qui baisse) que le public occidental du web hebdomadaire mentionne moins mais que MAL et Goodreads retrouvent. La thèse d'un « décalage Occident/Japon » ne tient pas mieux après cet élargissement qu'avant.

### 3.2 Le seul point de divergence apparente : les designs féminins

[D] Au Japon comme en Occident, les designs sont **le motif d'achat déclaré** : Bookmeter — « j'avoue, acheté parce qu'une grande nana musclée se bat » (avis le plus voté) ; « le facteur décisif est la maîtresse/héroïne, grande et cool, donc j'achète encore un moment » ; « nouvelle étoile du monde onee-shota chez Jump ». Et, comme en Occident, ils sont aussi un repoussoir : 5ch — « il ne reste que le fétichisme des femmes charpentées » ; Yarukimedesu — « 誰得 » (« pour qui ? ») à propos des physiques.

**[I]** Ce n'est donc pas une différence culturelle ; c'est la même ambivalence, formulée dans les deux langues : l'attribut le plus visible attire un public précis et signale aux autres que la série n'est pas pour eux (Q7). La différence est de degré : côté Reddit, les designs dominent la discussion ; côté japonais, ils sont cités puis écartés au profit du rythme.

### 3.3 Ce que les Japonais disent que les Occidentaux disent moins

- **[D] « Un one-shot réussi n'est pas une série. »** 5ch : « un one-shot marche avec une idée-crochet ; une série demande de la construction et du tempo ». C'est le même diagnostic que les lecteurs Reddit qui comparaient au prototype, mais formulé comme règle générale.
- **[D] Le signal éditorial lu en temps réel.** 5ch (24 août 2021, ch. 9) : « troisième page couleur avant le ch. 8 → sondages bons ; augmentation de pages avant le ch. 8 → message implicite "prépare la fin" ». Les lecteurs japonais avaient conclu à l'arrêt dès la fin août, soit **avant** que la plupart des critiques occidentales sur l'examen soient écrites. **[I]** Pour votre projet publié par tome, ce signal n'existe pas ; ce qui compte est la mécanique de lecteur sous-jacente (les sondages), pas le rituel.
- **[D] Chiebukuro** : « trop occupé à planter des indices, il a négligé l'histoire sous les yeux ». C'est la Q6 (fonction de l'exposition) dite en une phrase.

---

## 4. Manga Plus : tenté, bloqué ; ce que vous pouvez relever vous-même

**[D]** Requête à `jumpg-webapi.tokyo-cdn.com/api/title_detailV3?title_id=100165` depuis mon environnement : réponse « Account Banned » (blocage de plage d'adresses, pas lié à un compte). Le site web `mangaplus.shueisha.co.jp/titles/100165` charge ses données par cette même API ; les archives web n'en conservent pas le contenu. Aucun chiffre Manga Plus n'a donc été obtenu ; **je ne reprends pas** la valeur « rang 11 » citée par un commentaire Reddit du ch. 17 (Dexter973) comme si c'était une mesure.

Ce que vous pouvez relever dans l'application (une quinzaine de minutes, 18 lignes) :

| À noter par chapitre | Ce que cela permet | Ce que cela ne prouve pas |
|---|---|---|
| nombre de vues (« views ») | **la seule courbe de rétention occidentale par chapitre** disponible : vues ch. n / vues ch. 1, et où la pente casse (ch. 2 ? ch. 5 ? ch. 9 ?) | les vues sont cumulées depuis 2021 : les lecteurs tardifs (venus après l'arrêt, souvent pour le méta) lissent la courbe |
| nombre de commentaires | second indice d'engagement, comparable aux 18 fils Reddit et aux fils MAL (ch. 1 : 45 réponses ; ch. 12 : 15 ; ch. 18 : 30) | volume ≠ tonalité |
| même relevé pour un comparateur lancé en simultané sur Manga Plus (Ayashimon, nov. 2021 ; Sakamoto Days, nov. 2020) | normaliser : une chute de 60 % entre ch. 1 et ch. 10 est-elle spécifique ou générale ? | — |

Les commentaires Manga Plus eux-mêmes sont courts, non datés finement et non triables ; ils valent moins que Reddit/MAL pour le *pourquoi*. Leur nombre vaut pour le *quand*.

---

## 5. Les sommaires mis en parallèle

**[D] Rangs au sommaire (ToC) des 20 premiers chapitres.** Sources : Jajanken (One Piece, HxH et Red Hood relevés aujourd'hui ; les autres déjà en dépôt). Un WSJ compte ~19 titres en 1997–1999, ~20–22 en 2011–2024. Les huit premiers chapitres d'une nouveauté bénéficient d'un placement protégé ; le rang ne reflète les sondages qu'ensuite (c'est pourquoi la colonne « moy. 9–18 » est la seule à comparer).

| Série | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | moy. 9–18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Red Hood** (2021) | 1 | 6 | 8 | 5 | 9 | 8 | 12 | 8 | **18** | **21** | 18 | 21 | 18 | 20 | 19 | 20 | 17 | 20 | – | – | **19,2** |
| One Piece (1997) | 1 | 5 | 6 | 6 | 10 | 4 | 6 | 6 | 4 | 2 | 4 | 1 | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 3 | 2,3 |
| Hunter × Hunter (1998) | 1 | 4 | 3 | 8 | 5 | 9 | 7 | 6 | 4 | 5 | 8 | 3 | 6 | 6 | 3 | 5 | 7 | 6 | 3 | 6 | 5,3 |
| Naruto (1999) | 1 | 8 | 11 | 8 | 14 | 13 | 9 | 8 | 7 | 6 | 7 | 10 | 10 | 5 | 1 | 7 | 3 | 5 | 6 | 6 | 6,1 |
| Bleach (2001) | 1 | 8 | 14 | 7 | 6 | 11 | 12 | 6 | 8 | 12 | 10 | 11 | 1 | 7 | 4 | 8 | 17 | 13 | 8 | 19 | 9,1 |
| My Hero Academia (2014) | 1 | 7 | 9 | 14 | 14 | 9 | 11 | 7 | 10 | 5 | 2 | 6 | 3 | 6 | 10 | 7 | 5 | 3 | 6 | 7 | 5,7 |
| Jujutsu Kaisen (2018) | 1 | 9 | 13 | 8 | 7 | 10 | 9 | 10 | 15 | 13 | 15 | 14 | **18** | **19** | 7 | 7 | 14 | 15 | 7 | 3 | 13,7 |
| Kagami no Kuni no Harisugawa (2011, 27 ch.) | 1 | 6 | 11 | 5 | 8 | 8 | 7 | 4 | 8 | 5 | 5 | 5 | 10 | 11 | 16 | 18 | 11 | 14 | 20 | 21 | 10,3 |
| Lock On! (2019, 18 ch.) | 1 | 5 | 10 | 10 | 12 | 12 | 6 | 13 | 15 | 12 | 11 | 13 | 17 | 13 | 17 | 21 | 19 | 20 | – | – | 15,8 |
| Kiben Gakuha (2020, 18 ch.) | 1 | 6 | 7 | 10 | 14 | 11 | 16 | 17 | 14 | 17 | 19 | 21 | 21 | 20 | 20 | 20 | 19 | 19 | – | – | 19,0 |
| Tenmaku Cinema (2023, 21 ch.) | 1 | 4 | 8 | 5 | 10 | 6 | 14 | 16 | 18 | 20 | 19 | 17 | 17 | 22 | 18 | 17 | 18 | 17 | 16 | 20 | 18,3 |
| Green Green Greens (2024, 26 ch.) | 1 | 4 | 10 | 7 | 11 | 8 | 13 | 13 | 16 | 15 | 17 | 19 | 16 | 9 | 20 | 17 | 16 | 16 | 15 | 17 | 16,1 |

### 5.1 Trois lectures, du plus sûr au moins sûr

**[D] 1. Red Hood a la pire trajectoire du corpus.** Dès le premier chapitre où le rang dépend des sondages (ch. 9), il est 18e sur 20 ; il ne remonte jamais au-dessus de 17. Les cinq séries courtes déjà en dépôt descendent *progressivement* (Kagami reste dans le top 10 jusqu'au ch. 13 ; Lock On! et GGG oscillent entre 11 et 17 avant de couler). Red Hood ne descend pas : il est déjà en bas.

**[I] 2. Avec le décalage sondage→sommaire (≈ 7–8 numéros, hypothèse courante, non officielle), le rang du ch. 9 reflète les cartes reçues pour les ch. 1–2, celui du ch. 13 les ch. 5–6.** Si cette hypothèse tient, le verdict des lecteurs japonais est tombé **sur le village, pas sur l'examen** : les chapitres 1–3 (Grimm arrive, Dodou & Naraoia, exposition « loups et chasseurs ») étaient déjà classés derniers. L'examen n'a pas « tué » la série ; il n'a pas produit le redressement qu'elle devait produire. C'est cohérent avec ce que le fil 5ch disait *en temps réel* dès le ch. 9 (« jusqu'à quand restent-ils au village ? ») et avec la remarque MAL sur le refus de l'appel (§2.2). Cela **corrige une causalité rétrospective** présente chez beaucoup de lecteurs (et dans le blog utikirimanga) : « l'examen a décidé de l'arrêt ». Côté Occident, la donnée équivalente est la chute par tome sur Goodreads (439 → 232 → 180 notes) ; on ne dispose pas de cartes.

**[I] 3. Un mauvais départ au sommaire n'est pas une sentence — JJK en est la preuve dans ce même tableau.** JJK est 18e–19e aux ch. 13–14 (pire que Kagami, Lock On! ou GGG au même stade), puis 7e aux ch. 15–16 et 3e–5e à partir du ch. 20. Avec le même décalage, le creux correspond aux sondages sur les ch. 5–7 (exposition de l'énergie occulte, entrée dans le centre de détention) et la remontée aux ch. 7–9 : **Yuji cède le corps à Sukuna, perd son cœur, meurt (ch. 9)**. C'est la Q5 (coût irréversible) en version extrême, placée là où Red Hood plaçait le début de son examen. **[H]** Hypothèse, pas démonstration : il faudrait la vérifier sur les rangs chapitre par chapitre d'autres séries à creux précoce.

Deux nuances de prudence : HxH, souvent cité comme preuve qu'un examen peut ouvrir une série, n'a **jamais été en tête** pendant son examen (rangs 3–9) — il tenait le milieu haut du sommaire d'un magazine où One Piece et Kenshin occupaient les premières places, avec la notoriété de Togashi ; et Bleach a passé ses vingt premiers chapitres entre 6 et 19 avant de devenir un pilier. Le sommaire précoce est un thermomètre, pas un oracle.

---

## 6. Tester les comparateurs contre les sept questions — première passe (niveau C, à vérifier)

Lecture de la grille (`grille_lecture_par_chapitre_Q1-Q7_2026-09-29.csv`) pour les dix premiers chapitres. Chaque cellule est un fait structurel à confirmer sur les planches.

| Question du §6 | Red Hood | One Piece | Hunter × Hunter | Jujutsu Kaisen |
|---|---|---|---|---|
| Q1 Horizon : quand le héros dit ce qu'il veut | jamais avant le ch. 5 ; il *refuse* l'appel au ch. 1 ; l'horizon devient « réussir l'examen » (ch. 9–14), puis bascule méta (ch. 15) | ch. 1 (« Roi des Pirates » + rendre le chapeau) | ch. 1 (devenir Hunter pour retrouver Ging) | ch. 1 implicite (mots du grand-père), explicité ch. 2–3, avec date de péremption (mourir après les doigts) |
| Q2 Présence : le héros agit à l'image | initiative au ch. 1 (louée), ruse au ch. 4 (louée), raisonnement ch. 10 ; le reste du temps « rapporté » ou en retrait derrière Grimm (5ch : « s'annulent ») | chaque chapitre : frappe, escalade, encaisse, décide | pêche, sauve, frappe Hisoka, chasse | mange le doigt, reste seul, cède le corps, meurt |
| Q3 Ordre d'arrivée : combien à aimer avant d'aimer le duo | duo Velou/Grimm jamais installé comme duo *agissant* ; ch. 6–8 ajoutent fratrie, Debonair, Bonkers, Bremen ; ch. 9–13 « Les Six », Merriopios | 1 nouveau nom durable par arc : Coby (ch. 2), Zoro (ch. 3), Nami (ch. 8) ; les autres sont des adversaires jetables | Kurapika et Leorio au ch. 2, Killua au ch. 6, Hisoka au ch. 5 : quatre noms en six chapitres, tous *en action* | Fushiguro ch. 1, Gojo ch. 2, Nobara ch. 4 ; le trio est complet au ch. 4 et en mission au ch. 5 |
| Q4 Promesse pendant l'initiation | examen sans loups-garous (ch. 9–14) | pas d'initiation : la promesse est le récit | l'examen *est* la promesse : Hisoka mutile (ch. 5), tue (ch. 8), épargne (ch. 9) | première mission = fléau de classe S dès le ch. 6 |
| Q5 Coût irréversible dans les 10 premiers chapitres | villageois hors-champ ; Naraoia (ch. 3) ; **aucune perte pendant l'examen** (JP : « personne ne meurt ») | le bras de Shanks (ch. 1) ; Kuina (ch. 5, déjà payée) | un candidat mutilé (ch. 5), un tué (ch. 8) | grand-père (ch. 1), condamnation (ch. 2), cœur puis mort du héros (ch. 8–9) |
| Q6 Fonction de l'exposition | explication par l'antagoniste (ch. 3, critiquée) ; ruse (ch. 4, acceptée) ; flashback Bonkers (ch. 12, mal placé) ; déballage méta (ch. 15–16) ; densité de bulles constante (MAL/JP) | règle du fruit montrée, pas dite ; flashback Kuina posé au moment de l'engagement de Zoro | motifs extraits par interrogatoire (le capitaine, ch. 2) : l'exposition est une épreuve | règles données en quelques cases par Fushiguro/Gojo, puis mises à l'épreuve dans le chapitre suivant |
| Q7 Signal visible (vérifié dans les JSON T1 Goodreads & Reddit Ch.1–18) | **Visuel/Designs n°1** : **48,1 %** au Ch.1 top-level Reddit (`16,2 %` sur Ch.1–18) ; **56,7 %** sur Goodreads T1 ; **90,0 %** sur MAL | **Aventure/Émotion (70,0 %) & Persos (60,0 %)** sur Goodreads T1 ; Visuel seulement **26,7 %** (et 33,3 % des mentions MAL ont une réserve sur le style) | **Personnages (56,7 %) & Aventure (50,0 %)** sur Goodreads T1 ; Visuel seulement **23,3 %** (et 31,8 % des mentions MAL ont une réserve sur le trait) | **Personnages (70,0 % Goodreads T1 ; 20,7 % Reddit 2018) & Rythme/Action (22,6 % Reddit 2018)** ; Visuel seulement **16,7 %** sur Goodreads T1 et **12,2 %** sur Reddit 2018 |

**[I] Ce que la première passe montre** : sur Q1, Q2, Q5, les trois séries longues répondent *dans le chapitre 1* et Red Hood au plus tôt au ch. 5 ; sur Q3 et Q4, les trois répondent différemment entre elles (OP n'a pas d'initiation ; HxH en fait la promesse ; JJK la court-circuite par une mission) — il n'y a donc pas une « bonne » réponse, mais Red Hood n'en donne aucune.

### 6.1 Validité discriminante : ce qui manque pour parler de « base semi-objective »

Une liste de principes tirée des seules séries qui ont réussi est un biais de survivant. Pour qu'un principe soit retenu, il faut qu'il **discrimine** : présent chez celles qui durent, absent chez celles qui s'arrêtent. Deux contre-épreuves sont déjà disponibles dans vos données :

- **Ayashimon (arrêtée à 25 ch.)** : le commentaire Reddit le plus voté du ch. 2 (SirWeebBro, 74 points, cité dans `synthese_red_hood.md`) énumère précisément Q1, Q2, Q3 et les règles de combat comme *acquis en deux chapitres*. La série a quand même été arrêtée ; la critique qui monte ensuite est la répétition des combats (jonnovision1, ch. 4 puis ch. 25). **Conclusion [I] : Q1–Q3 sont nécessaires (leur absence coûte), pas suffisantes.**
- **JJK (§5.1, point 3)** : remplit Q1–Q3 au ch. 4 et se retrouve pourtant 18e–19e ; ce qui coïncide avec la remontée est Q5. **[H]** Le coût précoce serait le discriminant le plus fort ; à tester sur les cinq séries courtes (aucune n'a été lue).

Statut des principes candidats, en l'état :

| Principe candidat | Soutenu par | Contredit par | Statut |
|---|---|---|---|
| L'horizon est dit au ch. 1 (Q1) | OP, HxH, JJK ; absence chez RH critiquée dans les deux langues | Ayashimon l'a et s'arrête | nécessaire, non suffisant |
| Le héros agit à l'image chaque chapitre (Q2) | idem | idem | nécessaire, non suffisant |
| Pas plus d'un personnage durable par arc avant que le duo existe (Q3) | OP ; RH critiqué (« more characters than chapters ») | HxH en introduit quatre en six chapitres sans dommage — parce qu'ils agissent | à reformuler : *ce n'est pas le nombre, c'est le nombre de personnages qui n'agissent pas* |
| L'initiation contient la promesse du genre (Q4) | HxH, JJK ; RH et « examen avant ch. 10 » (heuristique 5ch) | OP n'a pas d'initiation du tout | conditionnel : *si* initiation, alors promesse dedans |
| Quelque chose est perdu pour de bon dans les 10 premiers chapitres (Q5) | OP, HxH, JJK ; RH (« personne ne meurt ») ; remontée de JJK | non testé sur les séries courtes | **le plus prometteur, le moins testé** |
| L'exposition a une fonction dramatique à l'endroit où elle est (Q6) | ch. 4 vs ch. 3/12 de RH ; JP « trop occupé à planter des indices » | — | soutenu, mais de nature qualitative |
| Densité de page lisible (nouveau, hors §6) | MAL, JP, Bookmeter ; jamais reproché à OP/HxH/JJK | — | soutenu ; vérifiable *uniquement* sur planches |

Rien de ceci n'est une recette : ce sont des questions auxquelles les séries qui durent répondent tôt, chacune à sa façon.

---

## 7. Protocole de lecture — ce que vous faites de la grille

Ce que la grille produit une fois remplie : une table où, pour chaque chapitre des quatre séries, on lit côte à côte *ce qui se passe* (vos colonnes Q1–Q6), *ce que les lecteurs en ont dit* (Q7, déjà remplie pour Red Hood) et *où le chapitre s'est classé* (ToC). C'est la forme la plus proche de la « lecture empirique » que vous demandez, et la seule où les principes du §6.1 peuvent être confirmés ou démentis.

1. **Ordre** : Red Hood ch. 1–5 d'abord (40 pages × 5) ; puis OP ch. 1–7, HxH ch. 1–9, JJK ch. 1–9 (≈ 45 min par série). Le méta de Red Hood (ch. 15–18) peut attendre : ce n'est pas là que les lecteurs sont partis.
2. **Par chapitre, cinq relevés brefs** : (Q2) une phrase sur ce que le héros *fait* de ses mains ; (Q1) l'horizon tel qu'il est dit ou montré ; (Q3) noms nouveaux + « agit / ne fait que parler » ; (Q5) ce qui est perdu ; (Q6) chaque bloc d'exposition > ½ page : qui parle, à qui, pourquoi maintenant.
3. **Un relevé de page, une fois par chapitre** : compter les bulles sur la double page la plus chargée. C'est le seul moyen de juger la critique « 8–10 bulles par page » (MAL) / « cases explicatives » (Bookmeter) ; la compilation imgur de jahver donne le point de départ.
4. **Croisement** : pour Red Hood, comparer vos relevés avec Q7 et le ToC ; pour les comparateurs, noter où votre relevé contredit la ligne pré-remplie (c'est attendu : elle vient de mémoire).
5. **Contre-épreuve** : quand vous aurez fait ces quatre séries, une série courte (Ayashimon, qui a 4 047 commentaires dans le classeur, ou une des cinq en dépôt) avec la même grille. Sans elle, le §6.1 reste une liste de survivants.

Ce que je peux faire ensuite à partir de vos relevés : recoder, recroiser avec les CSV, et réécrire le §6 de l'analyse principale en séparant ce que la lecture confirme de ce qu'elle infirme.

---

## 8. Fichiers de cet addendum (même dossier)

- `mal_reviews_red_hood_2026-09-29.csv` — 20 critiques MAL : utilisateur, date, verdict, préliminaire (oui/non), note, texte intégral.
- `toc_premiers_chapitres_parallele_red_hood_vs_comparateurs_2026-09-29.csv` — rangs ToC ch. 1–20, 12 séries, avec URL Jajanken par chapitre.
- `grille_lecture_par_chapitre_Q1-Q7_2026-09-29.csv` — 48 lignes (RH 18, OP 10, HxH 10, JJK 10), colonnes Q1–Q7 + niveau de preuve + « à vérifier ».
- Sources japonaises citées au §3 : utikirimanga.hatenadiary.com/entry/2022/04/01/225334 ; anige-sokuhouvip.com/blog-entry-45483.html ; manga.itsys-tech.com/post/21082503/ ; detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14252195599 ; bookmeter.com/books/18731371 ; mechacomic.jp/books/151422/reviews.
