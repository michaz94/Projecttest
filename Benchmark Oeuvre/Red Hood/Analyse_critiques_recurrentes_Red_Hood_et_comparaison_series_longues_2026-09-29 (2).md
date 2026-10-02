# Red Hood — les critiques occidentales récurrentes, leur mécanisme, et ce que les séries longues font autrement

Créé le 29 septembre 2026 · **Mis à jour le 2 octobre 2026** (correction du codage Visuel vs Monde au §2.2 et ajout des données empiriques des 4 piliers *Fullmetal Alchemist*, *Hunter × Hunter*, *Jujutsu Kaisen* et *One Piece* aux §2.3 et §4). Complète la synthèse v3 (`../synthese_red_hood.md`) sans la remplacer.

**Question traitée :** pourquoi *The Hunters Guild: Red Hood* n'a pas retenu son public occidental (6,41 sur MAL ; 3,62 → 3,29 sur Goodreads du tome 1 au tome 3) là où d'autres battle shōnen retiennent le leur — quelles critiques reviennent, pourquoi elles apparaissent, et à quels endroits précis les séries longues font autre chose.

**Ce que ce document n'est pas :** une explication de la décision de Shueisha ; une mesure de préférences occidentales représentatives ; une recette. Les mécanismes décrits sont des hypothèses appuyées sur des déclarations de lecteurs et sur une comparaison de fabrication ; ils ne sont ni pondérés causalement ni garantis transférables.

---

## 0. Réponse courte

1. **Le public occidental engagé (Reddit) n'est pas parti.** Les comptes actifs par fil se stabilisent autour de 95–140 du chapitre 3 au chapitre 14, puis remontent à 210–245 pour la fin. Ce public a surtout parlé de deux choses : les designs féminins (≈ 25 % des comptes) et la peur de l'axe (≈ 25 % des comptes, jusqu'à 23 % des commentaires sur les chapitres 15–18).
2. **La critique de fond y est minoritaire mais consensuelle** : ≈ 21 % des comptes formulent au moins une critique substantielle ; ces commentaires sont peu nombreux mais fortement approuvés (scores médians de 13 à 74 pour les critiques structurelles, contre 5–6 pour les commentaires d'axe ou de design).
3. **Le public occidental large (Goodreads, lecture par tome) est celui qui décroche** : 3,62 → 3,48 → 3,29, avec des avis du type « bored, gave up halfway », « nothing happened in book 2 ». C'est ce public-là, pas Reddit, qui ressemble au lecteur d'une édition française par tome.
4. **Les critiques convergent sur cinq points structurels**, formulés dès le chapitre 3 et consolidés en bilan au chapitre 18 : (a) un protagoniste sans présence ni horizon ; (b) un casting élargi avant que le duo existe ; (c) un examen qui suspend la promesse (les monstres disparaissent) ; (d) des enjeux désamorcés (personne ne meurt, tout le monde passe) ; (e) un rythme de prologue jugé gaspillé (ch. 2–4). S'y ajoutent trois critiques secondaires : lisibilité de l'action, flashback/exposition mal placés, sentiment de dérivatif (Claymore, MHA) au chapitre 1.
5. **Aux mêmes endroits (chapitres 1–20), One Piece, Hunter × Hunter et Jujutsu Kaisen font des choix opposés** : but à long horizon énoncé au chapitre 1, casting ajouté un par un via une scène vécue, protagoniste qui agit et paie, enjeux létaux dans l'initiation elle-même, et — pour HxH — un examen qui *est* la promesse (chasser, survivre) au lieu de la suspendre. Ce n'est pas une preuve causale : c'est là que la différence de fabrication est la plus nette.
6. **Le récit d'un « fossé Occident/Japon » n'est pas soutenu** par le corpus : les rares voix japonaises disent la même chose (« ennuyeux à partir de l'examen »), le précommande Amazon.jp du tome 1 était faible, et Goodreads occidental donne 3,5.

---

## 1. Corpus et méthode

| Ensemble | Contenu | Usage ici |
|---|---|---|
| Reddit r/manga, 18 fils [DISC] | **4 432 commentaires, 1 382 comptes uniques**, fenêtre J+7 par fil ; scores archivés en 2022 (pas J+7) | Codage lexical de tous les commentaires ; lecture intégrale des ~220 commentaires de premier niveau les mieux notés (12–13 par chapitre) ; lecture d'un échantillon aléatoire de 120 commentaires de premier niveau (40 par phase) |
| Goodreads | Notes des trois tomes ; 11 avis textuels déjà extraits dans la synthèse v2 | Contraste « lecteur par tome » |
| MAL | Note 6,41 pondérée ; captures historiques | Contexte |
| Corpus de comparaison | Sakamoto Days (506 commentaires), Ayashimon, Neru dans le même classeur ; Jajanken ; notes Goodreads T1/T2 de Naruto, Bleach, JJK, MHA | Contraste |

**Phases :** 1–5 prologue (hameau) ; 6–14 Ironworks et examen ; 15–18 révélation méta et fin.

**Limites.** Le codage lexical produit des faux positifs et négatifs ; les pourcentages sont des ordres de grandeur, pas des mesures. Reddit est auto-sélectionné, anglophone, sans profil d'âge ni de pays. Un score Reddit mesure l'approbation des présents, pas la fréquence d'une opinion dans le lectorat. Goodreads mélange lecteurs payants, bibliothèques et exemplaires de presse NetGalley. La comparaison de fabrication (§4) repose sur la connaissance des œuvres, chapitre par chapitre, pas sur des données de réception de ces œuvres ; elle est vérifiable mais n'a pas été revérifiée planche par planche pour ce document. Un seul analyste, non aveugle aux hypothèses de la synthèse v2.

Script et tableaux rejouables : `coder_commentaires_red_hood.py`, `red_hood_codage_par_chapitre.csv`, `red_hood_codage_par_phase.csv`, `red_hood_codage_par_categorie.csv`.

---

## 2. Ce que les chiffres disent avant les citations

### 2.1 Présence et tonalité par phase (Reddit)

| Phase | Commentaires | Comptes uniques | % avec ≥ 1 critique substantielle | % avec ≥ 1 marqueur positif | % mentionnant axe / classement |
|---|---:|---:|---:|---:|---:|
| 1–5 prologue | 1 337 | 617 | 8,3 | 26,3 | 5,1 |
| 6–14 examen | 1 666 | 598 | 8,8 | 25,5 | 11,3 |
| 15–18 fin | 1 429 | 654 | 18,4 | 17,0 | 23,4 |

Comptes uniques par chapitre : 313 · 165 · 113 · 133 · 138 · 143 · **179** (ch. 7, Debonair) · 138 · 109 · 119 · 101 · 106 · 95 · 96 · **243** (ch. 15, révélation) · 235 · 211 · 230.

Lecture : le noyau Reddit se forme au chapitre 3 (≈ 100–140 comptes) et ne se réduit plus ; il *grossit* quand la série menace de finir. La discussion critique ne domine jamais — même à la fin, elle ne dépasse pas un commentaire sur cinq. Ce que la fin change, c'est que la critique devient rétrospective et structurée (bilans du chapitre 18).

### 2.2 Ce dont on parle (Reddit, 18 fils)

#### 2.2.A — Mesure nettoyée de l'attraction : Visuel/Dessin (`A1/A2/A3`) vs Monde/Conte de fées (`B1/B2`)
*(Correction méthodologique du 2 octobre 2026 : dans la première version du tableau 2.2.B ci-dessous, la ligne « Designs féminins (681) » incluait toute occurrence des prénoms `Grimm` ou `Debonair`, y compris lorsqu'un lecteur commentait leurs actions ou dialogues. Le tableau 2.2.A ci-dessous sépare strictement les commentaires portant sur le visuel/physique de la simple mention du nom des personnages, et ajoute la mesure du pôle Monde / Conte de fées qui manquait dans la v1).*

| Périmètre (Reddit `r/manga`) | Effectif (`N`) | **Pôle Visuel Total (`A1 ∪ A2 ∪ A3`)** | `A1` Style / Trait / Pages | `A2` Designs Monstres | `A3` Chara-design & Physique *(sans faux positif sur le nom)* | **Pôle Monde / Conte Total (`B1 ∪ B2`)** | `B1` Conte de fées / Folklore | `B2` Dark Fantasy / Chasse / Lore |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Chapitre 1 — 1er niveau (vérifié)** | **185 comm.** *(180 comptes)* | **48,1 %** *(89)*<br>*(44,9 % pos. / 3,2 % crit.)* | **28,6 %** *(53)* | **10,8 %** *(20)* | **22,7 %** *(42)* | **32,4 %** *(60)*<br>*(29,7 % pos. / 2,7 % crit.)* | **13,5 %** *(25)* | **24,3 %** *(45)* |
| **Chapitre 1 — Tous commentaires** | **446 comm.** *(313 comptes)* | **31,6 %** comm. *(141)*<br>**40,3 %** comptes *(126)* | **17,9 %** *(80)*<br>*23,6 % cptes* | **6,3 %** *(28)*<br>*8,6 % cptes* | **14,3 %** *(64)*<br>*18,8 % cptes* | **23,3 %** comm. *(104)*<br>**29,1 %** comptes *(91)* | **9,4 %** *(42)*<br>*12,1 % cptes* | **17,7 %** *(79)*<br>*23,0 % cptes* |
| **Prologue (Chapitres 1 à 5)** | **1 337 comm.** *(617 comptes)* | **19,4 %** comm. *(259)*<br>**32,6 %** comptes *(201)* | **10,8 %** *(145)*<br>*19,8 % cptes* | **3,0 %** *(40)*<br>*6,0 % cptes* | **9,7 %** *(130)*<br>*18,5 % cptes* | **14,1 %** comm. *(188)*<br>**22,0 %** comptes *(136)* | **5,2 %** *(69)*<br>*9,1 % cptes* | **10,5 %** *(141)*<br>*17,3 % cptes* |
| **Série entière (Chapitres 1 à 18)** | **4 432 comm.** *(1 382 comptes)* | **16,2 %** comm. *(717)*<br>**30,5 %** comptes *(421)* | **7,5 %** *(332)*<br>*16,4 % cptes* | **1,8 %** *(81)*<br>*4,9 % cptes* | **9,3 %** *(413)*<br>*21,1 % cptes* | **10,7 %** comm. *(474)*<br>**20,7 %** comptes *(286)* | **4,0 %** *(179)*<br>*9,6 % cptes* | **7,7 %** *(343)*<br>*15,5 % cptes* |

#### 2.2.B — Tableau général des catégories et des critiques structurelles (Reddit, 18 fils)

| Catégorie (codage lexical) | Commentaires | Comptes uniques | Score médian |
|---|---:|---:|---:|
| Pôle Visuel nettoyé (`A1 ∪ A2 ∪ A3` : trait, monstres, designs/physique) | **717** | **421** | 6 |
| ...dont Chara-design & physique féminin strict (`A3`, hors simple mention des prénoms) | **413** *(681 avec prénoms)* | **292** *(345)* | 6 |
| Pôle Monde / Conte de fées / Dark Fantasy (`B1 ∪ B2`) | **474** | **286** | 6 |
| Axe, classement, ToC, « please survive » | 591 | 351 | 5 |
| Humour, « lol », scènes drôles | 284 | 175 | 7 |
| Rythme, gaspillage, « condense », « took N chapters » | 183 | 113 | 8 |
| Écriture / éditeur (« writing… poor », « editor », Samurai 8) | 129 | 87 | 8 |
| Art et designs (positif) | 132 | 107 | 5 |
| Méta / révélation, réaction négative | 70 | 57 | 5 |
| Dérivatif (Claymore, MHA, « generic ») | 57 | 50 | 7 |
| Velou intelligent / stratège (positif) | 52 | 43 | 10 |
| Exposition, « too technical », scheming | 48 | 39 | 10 |
| Lisibilité de l'action | 44 | 37 | 7 |
| Protagoniste effacé / fade | 36 | 33 | **13** |
| Enjeux faibles | 26 | 24 | 6 |
| Trop de personnages trop tôt | 22 | 20 | **37** |
| Examen comme détour | 20 | 19 | **13** |
| Flashback / exposition mal placés | 7 | 7 | **74** |
| Promesse de chasse aux monstres non tenue | 7 | 7 | 12 |

Lecture : les critiques structurelles sont rares en volume et hautes en approbation. Un commentaire « trop de personnages » ou « flashback au mauvais moment » est écrit par peu de gens mais voté par beaucoup. À l'inverse, l'axe et les designs remplissent la conversation avec des scores individuels bas : beaucoup d'émetteurs, peu d'approbation par message.

### 2.3 Le lecteur par tome (Goodreads)

| | T1 (ch. 1–7) | T2 (ch. 8–13 + bonus) | T3 (ch. 14–18 + prototype) |
|---|---:|---:|---:|
| Note | 3,62 | 3,48 | 3,29 |
| Notateurs | 439 | 232 | 180 |

Comparaison élargie aux **7 grands succès du shōnen** (Tome 1 → Tome 2 sur Goodreads) :
- **Fullmetal Alchemist** : **4,54** *(198 634 votes)* → **4,51** *(23 057 votes)* ;
- **Hunter × Hunter** : **4,53** *(70 744 votes)* → **4,42** *(7 561 votes)* ;
- **Jujutsu Kaisen** : **4,49** *(73 124 votes)* → **4,46** *(38 692 votes)* ;
- **One Piece** : **4,49** *(194 014 votes)* → **4,36** *(34 869 votes)* ;
- **Naruto** : **4,41** *(251 143 votes)* → **4,44** *(32 323 votes)* ;
- **My Hero Academia** : **4,28** *(158 556 votes)* → **4,43** *(36 952 votes)* ;
- **Bleach** : **4,27** *(202 963 votes)* → **4,30** *(20 535 votes)*.

Les cinq séries axées malgré un MAL > 7 vont de 3,33 à 4,12 sur des effectifs minuscules (11–72 notes). *Red Hood* (**3,62 → 3,48 → 3,29**) se situe donc dans la zone des séries interrompues, avec un effectif dix fois plus grand, et la note baisse à chaque tome. Ce n'est pas une cohorte suivie : les 180 notateurs du T3 ne sont pas nécessairement un sous-ensemble des 439 du T1.

---

## 3. Les critiques récurrentes — ce qui est dit, quand, et pourquoi

Format : citations datées avec identifiant et score ; mécanisme proposé ; contre-voix. Les citations sont des exemples lus, pas des mesures de fréquence.

### 3.1 Le protagoniste sans présence ni horizon

**Ce qui est dit.**
- Ch. 3 — « Velou is already annoying… I get his character but it doesn't fit in this world » (larbearforpresident, h4tt4t6, 10).
- Ch. 11 — « Velou's role in the manga is… quite strange. He's not a classic shonen protagonist (Luffy, Naruto, Ichigo), but he's also not interesting in his own way (Grimm carried out the first arc and now he's sharing the spotlight with other characters) » (Honyakusha-san, hd84eax, 38). — « It's only chapter 11, yet the MC is almost completely absent » (Iamnothereorthere, hd837jp, 22).
- Ch. 13 — « The main character is in like four pages. Lucky for us we need to make sure all the unnamed extras pass instead of the main character facing tension » (2xrainbows, hf8u2a5, 34). — « the character[s] talk up praise of Velou but all he's done is basically getting captured » (CTheng, hf8inas, 155).
- Ch. 16 — « most of the long running manga have a super end-game goal for their MCs and Velou just seems like he wanted to be a hunter, and then what? » (GGMaXThreeOne, hhvjonf, 5).
- Ch. 18 — « Velou's lack of notoriousness. Both personality and his screentime » (SolracXD, hjoltu3, 352). — « his personality is as generic as they come » (Googleflax, hjorftt, 86).

**Quand.** Dès le chapitre 3, puis en continu pendant l'examen, puis en bilan.

**Pourquoi (mécanisme proposé).** Deux choses distinctes se cumulent. *L'horizon* : le but de Velou est un métier (devenir chasseur), atteint au chapitre 14 ; il n'y a pas d'objectif au-delà qui donne au lecteur une raison d'imaginer le chapitre 200. *La présence* : le trait apprécié de Velou — il réfléchit, il planifie, il refuse — est un trait qui s'exerce hors-champ ou en dialogue ; dans l'examen, les actions sont exécutées par d'autres (Bonkers, Merrio) sur son plan. Le lecteur peut admirer le plan et ne pas *vivre* avec le personnage. Un protagoniste stratège n'est pas le problème ; un protagoniste stratège dont la stratégie remplace la scène l'est.

**Contre-voix.** Le même trait est loué avec insistance : « I really like that his strength so far is his intelligence » (esn_crvg, ch. 10, hckk3wm, **468**) ; « he doesn't need Grimm to do literally everything for him » (snakebit1995, ch. 2, 173) ; « Other typical shounen protagonist would have just joined » (lizard81288, ch. 2, h41e7wb, 87). Sur Goodreads, un lecteur défend l'examen précisément parce qu'il « did a lot to further Velou's character as a strategist » (MajesticalLion, GRR4355962082). L'appréciation existe ; elle ne s'est pas convertie en attachement suffisant chez ceux qui ont formulé le bilan.

### 3.2 Le casting élargi avant que le duo existe

**Ce qui est dit.**
- Ch. 13 — « Too many characters have been introduced for this early on in the story, and the MCs has been pushed to the side » (LordScyther998, hf8f6op, 80). — « The whole trust and working together stuff… should've been saved for a later arc; not literally the second arc and involves a bunch of randos, that we barely know » (CTheng, hf8inas, 155).
- Ch. 14 — « The trust and friendship card has been played too soon » (Aventure_Bleu, hg40jku, 209).
- Ch. 15 — « He should've chosen two side characters… by chapter 15 of MHA, the LOV had already started attacking USJ. Chapter 15 of JJK is when Gojo first uses his Domain Expansion. But here we're still stuck in the initial training arc » (MicZiC15, hgzzqug, 278).
- Ch. 17 — « The relationship between Velou and his team feels soooo artificial because we haven't seen them really connect » (RojasDaMighty, hisofpy, 1).
- Ch. 18 — « There should have been more time for Velou and Grimm to develop their mentor/student relationship before shoving them into a cast of 15+ characters… adding more characters than there are chapters is too much » (Googleflax, hjorftt, 86).

**Quand.** À partir du chapitre 9 (arrivée des candidats), culminant aux chapitres 13–14 quand le récit demande au lecteur de se réjouir d'une victoire collective.

**Pourquoi.** Le récit demande une émotion (la confiance qui gagne) avant d'avoir construit son support (des liens vécus). La réaction « artificial » ne dit pas que les personnages sont mauvais — Bonkers, Merrio, Debonair sont aimés — mais que la *relation* n'a pas de scènes derrière elle. C'est le mécanisme 2 de la synthèse v2, ici daté : le duo Grimm–Velou a eu cinq chapitres, dont trois de combat contre des adversaires jugés « inconséquents » ; il est ensuite dilué dans quinze personnes.

**Contre-voix.** « I don't mind the focus on new characters. It kind of reminds me of the Chūnin Exams » (ch. 13, échantillon aléatoire, 12). Sur Goodreads : « I really like that we are getting to see more of the characters that are on the Ironworks » (Jill, GRR5428598512).

### 3.3 L'examen comme suspension de la promesse

**Ce qui est dit.**
- Ch. 10 — « this chapter was too technical… chapters with characters mostly scheming is [not] a good idea. The amount [of] flashbacks don't help » (SaKaly, hckk89x, 23).
- Ch. 12 — « This exam portion is dragging, I hope that we see some more monsters soon » (USBacon, hed7pez, 7).
- Ch. 13 — « I'm kinda getting bored of this training arc now » (LordScyther998, 80).
- Ch. 15 — « we stayed in a box for 9 chapters » (MicZiC15, 278). — « Some of the developments in the first half would probably have been useful… like 5 chapters ago » (Chespineapple, hgzrita, 239).
- Ch. 18 — « it was the fortress that really killed it, a series about fantastical monsters shouldn't take away the monsters early on » (115_zombie_slayer, hjox0wv, 120). — « The examination arc really pulled it down. Before that it had a decent world and story » (Time_Significance, hjoi9ex, 53). — « Combining the ironworks arc to be training and exam arc was the biggest drawback » (BuFett, hjshdxk, 3).
- Goodreads T2 — « Nothing happened in book 2. They didn't even finish the test which only lasts for two hours… I have no desire to read the rest » (Ryan, GRR5651632418). — « The mystery is interesting, but not a big enough draw for me to want to read the next one » (Jen, GRR5323212620).

**Quand.** Le glissement commence au chapitre 10 (premier chapitre « technique ») ; la formulation « détour » domine les bilans.

**Pourquoi.** Ce qui a fait essayer la série — monstres grotesques, chasse, écologie de contes, duo — n'est plus à l'écran entre les chapitres 9 et 14 : un jeu de gendarmes et voleurs entre humains dans un bâtiment fermé. Le problème n'est pas la *durée* d'un examen (HxH en fait 38 chapitres) mais son *contenu par rapport à la promesse*. Et le plaisir de substitution proposé — la stratégie — est celui qui donne le moins de scènes au protagoniste (cf. 3.1). Les deux critiques se renforcent.

**Contre-voix.** « When's the last time we've had an entrance exam that felt like an actual *exam* rather than a poorly disguised tournament? » (Iamnothereorthere, ch. 10, hckkfrn, 69) ; « Love how they execute this test. Remind me of HxH » (ch. 14, 37) ; « I'm hearing a lot of people attribute its failure to the exam arc being too boring, but I don't necessarily agree » (MajesticalLion, Goodreads). L'examen a des défenseurs explicites ; ils sont moins nombreux et moins votés que ses critiques dans les bilans.

### 3.4 Les enjeux désamorcés

**Ce qui est dit.**
- Ch. 14 — « this manga is about hunt[ing] genocidal demi-human/monsters… this exam is so lighthearted… No conflict, No stakes (if you fail you can retake next year), No danger, All according to Velou's plan. Last arc, no villager die[d]. This arc, everyone is passing » (KakiLangit2579, hg46vfq, 27).
- Ch. 18 — « the actual exam being more serious with maybe a small mortality rate could have created better tension » (SolracXD, 352).
- Ch. 18 — « the protagonist couldn't spare 10 minutes to cry about his dead parent » (ParticularAlbatross4, hjqk7ka, 2 — déclare avoir abandonné au chapitre 1).

**Quand.** Formulé rétrospectivement, mais les faits sont dès le chapitre 5 (le hameau détruit, personne ne meurt) et au chapitre 14 (tout le monde passe).

**Pourquoi.** La série installe une menace (loups-garous mangeurs d'hommes, extermination) et retire systématiquement la conséquence. Le lecteur a apprécié la surprise une fois (« What a nice twist. So use[d] to everybody dies stories », ch. 5, 149) ; répétée, elle devient un signal que le récit ne fera pas payer. Ce n'est pas une demande de morts — la synthèse v2 le note — mais une demande de *coût*.

**Contre-voix.** Ch. 5, 149 et 122 : des lecteurs sont soulagés que personne ne meure. Le désaccord porte sur ce que « conséquence » veut dire, pas sur un goût du massacre.

### 3.5 Le rythme du prologue

**Ce qui est dit.**
- Ch. 3 — « the writing is… abysmal » (lakesidewoods, h4tsg48, 50).
- Ch. 18 — « The series took 5 chapters just to establish Velou's motivation because it wasted Ch. 2–4 on fighting two completely inconsequential goons… You could condense the first 15 chapters into around 5 or 6… Slow pacing is fine but it has to be JUSTIFIED » (Technocity777, hjolvp8, 315). — « Chapter 1 could have ended with Cinderella and the big wolf showing up and chapter 2 with the hamlet destruction » (SolracXD, 352). — « the pacing and writing was incredibly poor, especially in the opening chapters » (The_Blackest_Knight, hjopy1u, 59).

**Pourquoi.** Deux chapitres et demi (2–4) sont consacrés à deux loups-garous dont la mort ne change rien à l'intrigue ; l'antagoniste réel et le mobile du héros arrivent au chapitre 5. Les lecteurs *sur le moment* avaient loué « economical storytelling » (riddlemyfiddle11, ch. 5, 368) : la critique du prologue est presque entièrement rétrospective. Elle n'en est pas moins consensuelle dans les bilans, ce qui suggère qu'elle décrit un coût cumulé plutôt qu'un rejet immédiat.

### 3.6 Critiques secondaires, présentes tôt

- **Lisibilité de l'action** (37 comptes, surtout ch. 3) : « The action is super hard to follow because of how messy it is » (TheAdamena, h4tqjok, 25) ; « the lack of backgrounds… is the only thing bugging me » (SaKaly, ch. 3, 274). Un lecteur se demande si le support numérique aggrave (ch. 4, 2) ; Goodreads (Jen) mentionne la petite taille d'écran.
- **Flashback et exposition mal placés** (7 comptes, score médian 74) : « I kinda dig Bonkers' backstory but man that was an awkward way to tell it » (topurrisfeline, ch. 12, hecuktv, 158) ; « i dont need to hear a dedicated chapter about characters this early in the game » (SuperUnhappyman, hecreeh, 76) ; « someone else's flashback right now during critical "hook" chapters » (riddlemyfiddle11, hecs4u8, 121). L'inverse a été loué au chapitre 4 : « I was worried we'd have an exposition dump… but I'm glad it was to buy time to trick Dodou » (SaKaly, 43). **La même technique est acceptée quand elle a une fonction dramatique et rejetée quand elle en manque.**
- **Dérivatif** (50 comptes, concentrés au ch. 1 : 18 commentaires) : « The author is clearly a big fan of early Claymore » (HaudNomen, h384208, 77) ; « A new take on fairy tales is kinda a trite thing at this point » (riddlemyfiddle11, h3835rv, 90) ; « a more boring version of Claymore… It lacks the mystery and the fear » (Giddypinata, h4wc49e, 3). La familiarité a aussi rassuré (synthèse v2, §1). Le point utile est que le reproche vient de la *mise en scène des villageois et de la chasseuse* — la partie la plus attendue — pas des loups-garous, unanimement trouvés singuliers.
- **Le méta arrivé trop tôt** (57 comptes en négatif ; beaucoup plus en positif) : « This development is just so absurd that it just upsets me… these ideas could be great if they are just given time » (WhoiusBarrel, ch. 16, hhvalxr, 568) ; « We went from "the power of friendship" to "the hunters guild are the ultimate baddies writing fate in a magic book" in TWO CHAPTERS » (tiktakdoh, hhvffdz, 186) ; « the twist… would have been really great if it'd happened 100–200 chapters into the story rather than 15 » (Googleflax). Le même virage est célébré : « The fucking balls » (WhoiusBarrel, ch. 17, hirrqe0, **1 113**). Ce n'est pas une critique de la série telle que conçue mais de la série telle que compressée ; elle confirme en creux ce que les lecteurs attendaient d'un horizon long.

### 3.7 Deux non-critiques qui structurent pourtant la réception

- **Les designs féminins comme premier moteur de la conversation.** 345 comptes ; c'est la catégorie la plus fournie. Elle a fait essayer (« I originally only checked this out cause I saw some of that art of Grimm », snakebit1995, h383zye, 217) et elle a fait rester certains. Elle a aussi un revers documenté : « Read only up to the third chapter tbh and lost interest. Honestly, most of the time all I hear is about the thicc women in the series so meh. If that is the only thing being raved about, I guess I saved my time » (Arcanvas, ch. 18, hjp01xs, 8) ; « I still don't see what many western fans saw in Red Hood (besides… muscle mommies Grimm and Debonair) » (The_Blackest_Knight, 59). Quand l'enthousiasme visible d'une communauté porte sur un attribut périphérique, il renseigne mal les lecteurs extérieurs sur ce qu'il y a à lire.
- **La peur de l'axe comme contenu.** 351 comptes. À partir du chapitre 9, une part croissante des messages ne parle plus du chapitre mais du classement. Un lecteur s'en plaint au chapitre 15 (WillBlaze, 31). La synthèse v2 en fait un « niveau social » ; on ajoute ici que cette conversation a produit un récit auto-flatteur — « the single greatest example of the disconnect between the Western and Japanese manga fanbase », avec « 200,000 views on the English Manga Plus app » (hcm59f6, ch. 10, 26) — que les données contredisent (§5).

---

## 4. Aux mêmes endroits, ce que les séries longues font autrement

**Statut de cette section :** analyse de fabrication, fondée sur la connaissance des œuvres chapitre par chapitre (vérifiable, non revérifiée planche par planche ici). Ce n'est pas de la réception, sauf mention. Les lecteurs de Red Hood eux-mêmes ont posé la comparaison : « those series all had WAY more accomplished in 15 chapters than Red Hood did » (Technocity777, 315) ; « by chapter 15 of MHA, the LOV had already started attacking USJ. Chapter 15 of JJK is when Gojo first uses his Domain Expansion » (MicZiC15, 278).

| Dimension | Red Hood (ch. 1–18) | One Piece (ch. 1–~20) | Hunter × Hunter (ch. 1–~20, examen jusqu'au 38) | Jujutsu Kaisen (ch. 1–~20) |
|---|---|---|---|---|
| **But du héros au ch. 1** | Devenir chasseur (métier). Mobile personnel au ch. 5 (hameau détruit) | « Je serai le Roi des Pirates » ; le chapeau de Shanks comme dette | Retrouver Ging et comprendre pourquoi il a préféré être Hunter à être père | Mots du grand-père mourant (« aide les gens, meurs entouré ») ; puis exécution différée jusqu'à avoir mangé tous les doigts |
| **Horizon au-delà du premier arc** | Absent jusqu'au ch. 15 (le méta) | Explicite dès la page 1 (One Piece, Grand Line) | Explicite (Ging) ; le Hunter Exam est la *condition* du but | Explicite et à compte à rebours (20 doigts, puis mourir) |
| **Ce que fait le héros dans l'initiation** | Planifie ; capturé ; « in like four pages » (ch. 13) | Combat, décide, recrute ; chaque adversaire tombe par lui | Combat, grimpe, pêche, vole le badge de Hisoka ; refuse d'abandonner | Combat, meurt (ch. 9), revient, s'entraîne, choisit |
| **Ajout du casting** | 2 (Grimm, Velou) → ~15 candidats d'un coup (ch. 9) | Un par arc, chacun via sa blessure (Zoro/Kuina ch. 5 ; Nami/mystère ; Usopp/père) | Trois compagnons en 3 chapitres (Leorio, Kurapika sur le bateau ; Killua ch. 6), chacun avec un mobile énoncé en une scène | Trois en 3 chapitres (Megumi, Nobara), chacun avec une ligne morale nette (« je sauve injustement » ; « être moi à Tokyo ») |
| **Liens vécus avant d'être sollicités** | Duo : 5 chapitres, dont 3 de combats « inconséquents » | Zoro se lie par une dette de vie ; Coby par un choix | La tempête, le marais, la tour : épreuves partagées avant toute « équipe » | La mort de Yuji au ch. 9 soude le trio avant tout événement collectif |
| **Enjeux dans l'initiation** | Personne ne meurt au hameau ; tout le monde passe l'examen | Exécution de Zoro ; ville détruite ; chien Chouchou | Des candidats meurent ; Hisoka blesse Leorio (ch. 8) ; Killua tue (ch. 18, ch. 36) | Le protagoniste meurt ; Junpei meurt (ch. 27) |
| **La promesse pendant l'initiation** | Les monstres disparaissent ; jeu humain en lieu clos | Chaque île = un nouvel adversaire et un nouveau décor | L'examen *est* la chasse : traque, survie, adversaires monstrueux (Hisoka) | Missions avec fléaux dès le ch. 4 ; ennemi thématique (Mahito) au ch. 19 |
| **Exposition** | Une ruse (ch. 4, louée) ; puis « too technical » (ch. 10), flashback secondaire (ch. 12) | Minimale ; les règles arrivent par l'usage | Les règles de chaque phase sont énoncées en une page, puis jouées | Système posé en 2 chapitres, puis démontré ; le méta-plafond (Gojo/Jogo) au ch. 14–15 |
| **Événement de type « examen »** | Ch. 6–14 (arc 2) | Aucun | Ch. 5–36 (arc 1, c'est la prémisse) | Ch. 32–54 (Kyoto), *après* l'investissement émotionnel |

**Ce que la comparaison montre, et ce qu'elle ne montre pas.**

- L'examen n'est pas fautif en soi : HxH le fait plus long et plus tôt. La différence est que chez Togashi l'examen est *le contenu promis* (chasse, survie, monstres, un tueur en liberté) et que le héros y agit et y risque ; chez Kawaguchi il est un *intermède humain* dans une série de monstres, avec un héros qui coordonne.
- Le « protagoniste stratège » n'est pas fautif : Kurapika, Megumi, plus tard Nami. Mais aucun n'est le protagoniste des vingt premiers chapitres ; les trois séries confient le début à un héros qui agit d'abord et paie.
- Le casting large n'est pas fautif : MHA en a 20 dès le chapitre 5. Mais MHA (lecteur MicZiC15) ne les *explique* pas tous ; deux ou trois sont développés, les autres attendent.
- La révélation lente n'est pas fautive : JJK a démarré mal au ToC (corpus Jajanken) et s'est redressé. Ce qui se redresse, c'est une série qui a déjà un héros, un compte à rebours et des morts.
- **Rien ici n'établit qu'un autre découpage aurait sauvé Red Hood.** La comparaison localise les différences de fabrication aux endroits exacts où les lecteurs ont formulé leurs critiques ; elle ne mesure pas le poids de chacune.

Un lecteur a proposé une restructuration complète (BuFett, ch. 18, hjshdxk, 3) : deux chapitres de hameau, dix chapitres de voyage Grimm–Velou en chassant des créatures, un ou deux chapitres d'examen sans entraînement. Ce plan n'a aucune valeur prédictive ; il est cité parce qu'il exprime, en creux, exactement les quatre attentes ci-dessus (promesse tenue, duo construit, héros actif, casting différé).

---

### 4.2 Confirmation empirique dans les données de réception des 4 piliers (Goodreads Tomes 1–2, MAL `N = 240`, Reddit JJK 2018 Ch. 1–18)

Pour vérifier si ces différences de fabrication se traduisent dans ce que les lecteurs occidentaux retiennent effectivement des premiers tomes, trois jeux de données JSON ont été extraits le 2 octobre 2026 (`goodreads_tomes_1_2_5_series.json` [311 critiques], `mal_reviews_5_series.json` [240 critiques], `reddit_jjk_2018_ch1_18.json` [164 commentaires des chapitres 1 à 18 de *JJK* en mars–juillet 2018]) :

| Série | **Goodreads Tome 1** (`N = 30`/série)<br>Mentions **Visuel/Dessin** | **Goodreads Tome 1**<br>Mentions **Monde/Système** | **Goodreads Tome 1**<br>Mentions **Personnages/Duo** | **Goodreads Tome 1**<br>Mentions **Histoire/Rythme** | **MAL** (`N = 240`)<br>Part des mentions du dessin comportant une **réserve** *(simple, brouillon, confus)* | **Reddit Ch. 1–18 à chaud**<br>Rang du **Visuel** dans la discussion |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Red Hood** | **56,7 %** *(17/30)*<br>*(58,6 % en EN)* | **63,3 %** *(19/30)* | **63,3 %** *(19/30)* | **66,7 %** *(20/30)* | **22,2 %** *(4/18)*<br>*(70 % d'éloge pur sur 20)* | **Rang 1** (**16,2 %** sur Ch.1–18 ; **48,1 %** au Ch.1 top-level) |
| **Fullmetal Alchemist** | **30,0 %** *(9/30)*<br>*(36,4 % en EN)* | **70,0 %** *(21/30)* | **73,3 %** *(22/30)* | **63,3 %** *(19/30)* | **22,5 %** *(9/40)*<br>*(« simple mais lisible »)* | — *(pré-Reddit)* |
| **One Piece** | **26,7 %** *(8/30)*<br>*(28,0 % en EN)* | **53,3 %** *(16/30)* | **60,0 %** *(18/30)* | **70,0 %** *(21/30)* | **33,3 %** *(15/45)*<br>*(« excentrique, s'apprivoise »)* | — *(pré-Reddit)* |
| **Hunter × Hunter** | **23,3 %** *(7/30)*<br>*(29,2 % en EN)* | **33,3 %** *(10/30)* | **56,7 %** *(17/30)* | **50,0 %** *(15/30)* | **31,8 %** *(7/22)*<br>*(« simple/irrégulier mais écriture géniale »)* | — *(pré-Reddit)* |
| **Jujutsu Kaisen** | **16,7 %** *(5/30)*<br>*(17,9 % en EN)* | **40,0 %** *(12/30)* | **70,0 %** *(21/30)* | **50,0 %** *(15/30)* | **41,7 %** *(15/36)*<br>*(« rough, sketchy »)* | **Rang 4** (**12,2 %** sur Ch.1–18 en 2018, derrière Rythme **22,6 %** et Persos **20,7 %**) |

**Trois constats empiriques :**
1. **Au Tome 1, *Red Hood* dépend 2 à 3,4 fois plus du signal visuel (`56,7 %`) que les quatre piliers (`16,7 %` à `30,0 %`)** : dans les grands succès, ce qui retient le lecteur dès le Tome 1 est d'abord le noyau de personnages (`56,7 %` à `73,3 %`) et l'élan dramatique (`50,0 %` à `70,0 %`).
2. **Dans *Fullmetal Alchemist* Tome 1 (ch. 1–4), le Monde (`70,0 %`) est indissociable de la blessure des frères Elric (`73,3 %`)** : la loi de l'Échange équivalent n'est pas enseignée dans une salle de cours au chapitre 5, elle est incarnée dès les premières pages par le bras d'Edward et l'armure d'Alphonse.
3. **Le face-à-face Reddit entre *Jujutsu Kaisen* (Ch. 1–18 en 2018) et *Red Hood* (Ch. 1–18 en 2021) montre une symétrie inversée** : au chapitre 2 de *JJK* (`86e0kt`), des lecteurs jugeaient la prémisse d'exorcisme banale et prédisaient son annulation avant *Bozebeats* (*« probably the most likely to get axed out of the 3 jump starts »* — `u/SuperSceptile2821`). Mais dès les chapitres 8 à 17 (mort de Yuji au ch. 9, puis Gojo vs Jogo au ch. 15), l'exécution fait basculer la réception : *« Exorcist manga has been done to death, but the pacing, panelling, and characterization of this work are top notch. Goes to show how much more important execution is than premise »* (`u/flamecircle`, +28, ch. 13–17).

---

## 5. « Le public occidental » n'est pas un

Trois publics apparaissent dans le corpus, avec des verdicts différents.

1. **Le noyau Reddit** (≈ 100–140 comptes par fil, anglophones, familiers du Jump) : enthousiaste, tolérant au rythme, mobilisé par les designs et par la survie de la série ; critique en minorité et surtout en bilan. Son verdict global est « du potentiel gâché ». Il ne mesure ni achat ni rétention : un compte peut écrire au chapitre 15 sans avoir lu depuis le 10 (synthèse v2).
2. **Le lecteur par tome** (Goodreads, dont NetGalley et bibliothèques) : plus casual, moins informé du contexte Jump, juge un objet fermé de 7 chapitres. Verdict : 3,6 puis 3,3 ; « bored », « nothing happened », « not a big enough draw ». **C'est le public dont le comportement ressemble le plus à celui d'un acheteur d'édition française** : pas de fil hebdomadaire, pas de ToC, une décision tous les six mois.
3. **Les non-lecteurs informés** : ceux qui ont arrêté au chapitre 1 ou 3 et reviennent au chapitre 18 pour dire pourquoi (Arcanvas ; ParticularAlbatross4). Ils citent la mort expédiée du maire et la réputation « thicc » comme motifs de ne pas investir.

Deux éléments déplacent le récit du « fossé Occident/Japon » :
- Au chapitre 16, un lecteur poste les rangs de précommande Amazon.jp du 4 novembre 2021 : Red Hood T1 **#58 140** (tout manga papier) / #12 772 (shōnen numérique), contre Neru #33 832, Sakamoto Days T4 #5 070, Elusive Samurai T3 #1 843 (KakiLangit2579, hhvgnza, 57). Un instantané, pas une vente ; mais il va dans le sens d'un tome 1 faible au Japon, cohérent avec le ToC.
- Les rares voix japonaises du corpus disent « moins intéressant à partir de l'examen, je voulais continuer la chasse » (synthèse v2, §6) — la même chose que 115_zombie_slayer.

Le fossé documenté n'est donc pas géographique. Il sépare **une communauté de discussion** qui a aimé la série et **des lecteurs de tomes** — occidentaux aussi — qui l'ont trouvée lente et sans enjeu.

---

## 6. Ce que ça donne pour un projet publié par tome — des questions, pas des règles

Reprend et précise les sept questions posées précédemment (message du 29 septembre). Chaque question naît d'une critique datée ci-dessus ; un projet peut y répondre autrement que les trois séries de comparaison.

1. **L'horizon.** Quand le héros a obtenu ce qu'il veut au tome 1, que veut-il encore ? Si la réponse n'existe pas avant le tome 3, le lecteur par tome n'a aucune raison d'acheter le tome 2 (GGMaXThreeOne ; Ryan sur Goodreads).
2. **La présence.** Dans chaque chapitre, quelle scène le héros *fait-il* — pas seulement décide-t-il ? Un stratège peut porter une série ; un stratège hors-champ, non (esn_crvg vs 2xrainbows : le même trait, deux verdicts selon qu'il est montré ou rapporté).
3. **L'ordre d'arrivée.** Combien de personnes le lecteur doit-il aimer avant d'avoir une raison d'aimer les deux premières ? Googleflax : « adding more characters than there are chapters is too much ».
4. **La promesse pendant l'initiation.** Si le monde promet des monstres, un arc sans monstres est un arc où le lecteur attend. HxH montre qu'une initiation peut *être* la promesse.
5. **Le coût.** Qu'est-ce qui est perdu, définitivement, dans le premier tome ? Pas nécessairement une vie ; mais quelque chose (KakiLangit2579).
6. **La fonction de l'explication.** Chaque exposition ou flashback a-t-il une raison d'être *à cet endroit* ? Le chapitre 4 (ruse) et le chapitre 12 (flashback de Bonkers) sont la même technique avec deux réceptions opposées.
7. **Ce que la communauté visible dira de toi.** Si le premier attribut dont on parle est périphérique (ici les designs féminins), il attire un public et en détourne un autre (Arcanvas). Ce n'est pas un jugement moral ; c'est une question de signal.

---

## 7. Fichiers

- `coder_commentaires_red_hood.py` — codage rejouable (pandas, openpyxl).
- `red_hood_codage_par_chapitre.csv` — comptes, premier niveau, comptes uniques et catégories par chapitre.
- `red_hood_codage_par_phase.csv` — pourcentages par phase.
- `red_hood_codage_par_categorie.csv` — commentaires, comptes uniques, score médian par catégorie.
- Source : `../posts_scores_et_commentaires_associes.xlsx` (feuille `Commentaires_associes`) ; citations Goodreads : `../synthese_red_hood.md`, identifiants GRR.

Identifiants Reddit : `https://www.reddit.com/r/manga/comments/<id_fil>/comment/<id_commentaire>/` ; les `id_fil` sont dans `../scores_reddit_archives.csv`.
