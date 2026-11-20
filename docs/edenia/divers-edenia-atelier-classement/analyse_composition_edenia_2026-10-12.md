# Analyse de composition : Edenia (nom provisoire)
## Y a-t-il une logique dans tes choix, et que permettent-ils d'inférer ?

**Date :** 12 octobre 2026 (dépôt au commit `b1bffb0`).
**Statut :** ce document contient **uniquement des analyses et des hypothèses de l'IA**. Il ne décide rien, ne change aucun statut et ne doit pas être recopié dans le YAML. Le YAML reste la seule source des statuts.

> **Mise à jour (12 oct., 2ᵉ partie) :** un addendum en fin de document (§7 à §10) ajoute *Hearthstone* comme déclencheur de l'œuvre et refait la partie *Dictionnaire infernal* à partir de **tes extraits** (`Pdfmd/`). Il met à jour L2, L3, L4, L5, L6, L8, P4, P7 et T1, ajoute un principe P-D, une tension T9 et les possibilités P9 à P13. Le §11 intègre tes réponses du même jour (Hearthstone joué de 2015 à 2023, mafia, noms, « Terre dévastée », règle France / Angleterre / Allemagne). Correction : dans les §1-§6, les articles GOMORY, FURFUR, MARBAS, STOLAS et COUR INFERNALE viennent de la base complète, **pas** de tes extraits.

**Fichiers lus :** `fiches_references_projet.yaml` (version du 12 oct.), `inference_du_projet.md`, `modeles_royaumes_et_regimes.md`, `structures_narratives_comparees.md`, `fiches_oeuvres_v3.md`, `debuts_et_goals_protagonistes.md`, `BRIEF_analyse_arthurien_x_influences.md`, `annexe_hypotheses_IA.md`, `critique_vacance_et_codificateur.md`, `Fiche_creatures_et_figures_folkloriques_statuts`, `Synthese_comparative_4_piliers_vs_Red_Hood.md`, ainsi que la base `dictionnaire_infernal_1825_4_tomes_complets.json` (2 517 articles).

### Étiquettes de source
| Étiquette | Sens |
|---|---|
| **(U)** | tu l'as dit (repris du YAML ou d'un fichier qui te cite) |
| **(YAML)** / **(dépôt : fichier)** | écrit dans ton dépôt |
| **(DI 1825, id)** | lu aujourd'hui dans la base du *Dictionnaire infernal* de ton dépôt |
| **(vérifié)** | vérifié aujourd'hui sur une source web (indiquée) |
| **(mémoire)** | connaissance de l'IA, **non vérifiée** |
| **(IA)** | raisonnement ou proposition de l'IA |

### Les trois types de raisonnement employés
- **Déduction :** si A et B sont vrais, alors C l'est forcément. C'est le plus solide.
- **Induction :** une même régularité revient sur plusieurs cas. C'est probable, mais un contre-exemple suffit à la faire tomber.
- **Abduction :** la meilleure explication de ce qu'on observe. C'est le plus fragile, d'où un **test** pour chaque abduction.

Les tests sont **facultatifs**. Ils servent à vérifier une inférence, pas à te forcer à trancher.

---

## 1. Ce que le dépôt contient vraiment (comptage)

### 1.1 Les statuts dans le YAML
Le champ `statut_decision` apparaît **29 fois** : `decide` 4 · `envisage` 11 · `interet` 10 · `non_precise` 4. À ces champs s'ajoutent les listes : 1 élément de folklore décidé, 12 envisagés et 33 en intérêt (24 créatures de la carte et 9 autres), plus 2 lieux arthuriens décidés et 6 envisagés.
On compte **31 fiches de référence** : 17 `influence`, 6 `reference`, 1 `influence+reference` (Red Hood), 4 `corpus_de_traditions`, 2 `source_documentaire` et 1 sans statut (Fabula Fantasia).

### 1.2 Ce qui est décidé
| Domaine | Décidé |
|---|---|
| Support | manga, dans le système de parution française (U, `structures…` §40) ; genre « battle shōnen occidental durable, édition traditionnelle » (YAML) |
| Monde | fantasy multi-héritages ; zone western + zone industrielle type *BioShock Infinite* ; un seul monde, une seule époque (YAML) |
| Technologie | plafond théorique 1950 hors technologie magique ; **armes à feu plafonnées à 1860** (YAML, 12 oct.) |
| Esthétique | « archaïque mais pas trop » (YAML) |
| Lieux | Forêt de conte ; Région montagnarde enneigée ; Brocéliande ; Le Lac (YAML) |
| Matière arthurienne | noms de lieux français uniquement ; personnages arthuriens = inspirations avec d'autres noms ; se détacher de *Seven Deadly Sins* et de *Radiant* sur ce plan ; nom de famille de Brann laissé vide (YAML) |
| Folklore | Agrippa (YAML) |

### 1.3 Ce qui n'est pas décidé
L'histoire, l'objectif du protagoniste, le système de pouvoirs, le type d'affrontement dominant, la mortalité, le gimmick d'Edenia et la cosmologie ne sont pas décidés. Pour trois de ces points, tu as répondu « je ne sais pas » (`structures…` §36 et §40).

> **Déduction 1 (sûre) :** toutes les décisions portent sur le **cadre** (support, monde, technologie, esthétique, lieux, noms). **Aucune ne porte sur le récit.** Edenia se construit donc « monde d'abord ». Ce n'est pas un défaut : c'est un fait, que `inference_du_projet.md` §0 constatait déjà. Mais cela borne l'analyse : on peut inférer une **logique de monde et de ton**, pas une histoire.

### 1.4 Ce que tu as lu de tes influences
Sur les 17 `influence`, **9 ne sont lues ou vues qu'en partie** : *YYH* (ch. 129), *One Piece* (ch. 984), *JJK* (anime, ép. 59), *Harry Potter* (livres : quelques-uns), *Worm* (arc 9), *Stormlight* (15 chapitres), *Game of Thrones* (S1-S7), *Kingkiller* (8 chapitres), *Le Seigneur des Anneaux* (livre II, ch. 10) (YAML).
Les romans occidentaux sont surtout lus **au début** : 8 chapitres de *Kingkiller*, 15 de *Stormlight*, 2-3 de *La Horde* (référence).

> **Déduction 2 (sûre) :** une œuvre lue sur ses premiers chapitres ne peut te transmettre que **ce qui se trouve dans ses premiers chapitres** : la manière d'ouvrir, la voix, le ton, l'entrée dans le monde, la présentation des personnages. Elle ne peut pas te transmettre une architecture d'ensemble (arcs, fin, structure globale).
> **Induction associée :** c'est cohérent avec l'axe de travail de tout le dépôt, centré sur le **démarrage** : l'échec de *Red Hood* au ch. 18, `debuts_et_goals_protagonistes.md`, les comparaisons Jajanken « premiers chapitres », les tomes 1-2 sur Goodreads. Ce qui t'occupe, ce sont **le démarrage et la durée**.

---

## 2. Les lignes de force (Observé → Raisonnement → Ce que ça dit → Test)

### L1. Une forme japonaise, une matière populaire française

**Observé**
- La forme est un battle shōnen manga, en parution française (U). La liste des gimmicks de référence est entièrement japonaise : Pirate, Ninja, Shinigami, Hunter… (YAML).
- La matière est française : lieux arthuriens **français uniquement** (U) ; folklore de la carte de France ; *Dictionnaire infernal* et *Dictionnaire féodal* ; Bibliothèque bleue ; Renaissance ; bas et milieu Moyen Âge (YAML).
- `fiches_oeuvres_v3.md` place *Radiant* seul au barreau « **forme industrielle** » de l'échelle de l'emprunt : c'est la seule œuvre de ta grille qui emprunte une **forme** (le nekketsu) plutôt qu'un contenu.
- Le dépôt nomme Ankama comme ton « éditeur cible » (dépôt : `critique_vacance…` §4 ; le YAML ne le dit pas). Ankama est aussi l'éditeur de *Radiant* (dépôt : fiche Radiant).

**Déduction 3 :** Edenia occupe **le même barreau d'emprunt que *Radiant*** (forme shōnen japonaise, auteur occidental, parution française). La forme ne peut donc pas l'en distinguer. Restent deux leviers : la **matière** et l'**exécution**.

**Abduction 1 :** c'est ce qui expliquerait pourquoi *Radiant* est « un cas spécial » (U, 8 oct.) et pourquoi tu cherches à « ne pas trop te rapprocher » (YAML). Ce n'est pas une question de goût, c'est une question de **position** : c'est l'œuvre qui occupe ta case.

**Ce que ça dit de l'œuvre :** plusieurs de tes décisions ressemblent à une **différenciation par la matière** :
- « français uniquement » pour les lieux arthuriens, alors que *Radiant* puise dans le celtique et l'irlandais (Caislean Merlin, Boadicée, Dullahan ; dépôt : fiche Radiant) ;
- un folklore **régional** précis (une créature, une région) plutôt qu'un fonds celtique général ;
- « se détacher de *Radiant* sur le plan arthurien » (U, 9 oct.).

Les reproches du public à *Radiant* donnent aussi une liste de ce qu'il faut exécuter autrement (dépôt : fiche Radiant, rubrique Faiblesse) : « pot-pourri » de nekketsu, trop de texte, monde jugé incohérent, héros agaçant.

**Test :** peux-tu dire en une phrase ce qu'Edenia contient et que *Radiant* (tomes 1-6) ne contient pas ? Si la réponse tient à la matière (« la France des provinces et de ses diables », par exemple), l'abduction tient.

---

### L2. La France comme carte cachée du royaume principal

**Observé**
- Tes repères d'échelle sont **la France entre 1000 et 1805** (U, 11 oct.).
- Les zones décidées ou citées correspondent à des régions françaises :
  - Brocéliande (Bretagne) ;
  - Région montagnarde enneigée, avec les Barbegazi placés « Alpes (est) » sur la carte (dépôt : fiche créatures) ;
  - région désertique « inspirée du Languedoc » (U, « je crois ») ;
  - Forêt de conte, collines à pierres dressées (YAML).
- Les créatures envisagées sont « réparties sur toute la France » : Ankou (Bretagne), Mélusine (centre-ouest), Gayant (Nord), Tarasque (Provence), Petit Homme rouge (région parisienne), Houeron (Est) (dépôt : fiche créatures, d'après la position sur la carte).
- Les zones **non françaises** de tes brouillons portent toutes un nom d'ailleurs : Nouvelle-Orléans/Caraïbes (Bilgewater), Piltover/Columbia, mafieux de la Prohibition, Ionia, Freljord, Tibétains-Yéti (YAML, brouillon), plus les personnages d'inspiration asiatique et les folklores gréco-égyptiens.

**Induction 1 :** ce qui relève de la France est rattaché à des **régions de terre** (forêt, montagne, désert, lande). Ce qui n'en relève pas est rattaché à des **ports, des villes-machines ou des confins** (Caraïbes, Piltover, Columbia, Freljord, Tibet).

**Abduction 2 :** le plan « un royaume principal + des cités-États + des royaumes adjacents » (U, 11 oct.) recouvrirait cette séparation :
- le **royaume principal** serait une « France de conte » dont les provinces portent chacune leur folklore ;
- les **cités-États et les adjacents** porteraient les héritages non français.

Cela rendrait compatibles les deux façons d'organiser les héritages que tu as retenues (YAML) : « **répartis par régions** » à l'échelle du monde, « **dans les mêmes tenues** » dans les villes cosmopolites.

**Appui supplémentaire (vérifié) :** Columbia, la cité de *BioShock Infinite*, est décrite comme une « *floating steampunk city-state* » (Wikipédia EN, *BioShock Infinite*). Ta zone industrielle décidée est donc, dans son modèle, **déjà une cité-État**.

**Test :** imagines-tu un héritage non français (asiatique, gréco-égyptien, caribéen) **à l'intérieur** du royaume principal, en dehors d'une ville ? Si oui, l'abduction tombe en partie.

---

### L3. Un monde de rangs, côté humain et côté infernal, construit sur le même modèle

**Observé**
- Le *Dictionnaire infernal* est visé pour ses **hiérarchies** (YAML).
- Tes titres viennent de tes brouillons : vassal, comte, baron, seigneur, empereur, intendant, shérif, **chambellan**, première lame, champion (YAML).
- Dans *Bleach*, ce qui t'intéresse, ce sont le Bankai, **la structure du Gotei 13** et « la narration sur le Gotei 13 » (U, 8 oct.).
- Les quatre démons envisagés portent **des titres féodaux** dans ta propre source (lu aujourd'hui) :
  - GOMORY : « puissant **duc** des enfers » (DI 1825) ;
  - FURFUR : « Grand **comte** des enfers » ;
  - MARBAS : « Grand **président** des enfers » ;
  - STOLAS : « Grand **prince** des enfers ».
- L'article **COUR INFERNALE** (DI 1825, `DI1825_T2_355`, 634 mots) dit, mot pour mot, que selon les démonographes « **tout s'y gouvernait comme ici-bas**, qu'il y avait là des princes, des nobles, de la canaille ». Il liste ensuite des **ministères** (« Adrameleck, grand chancelier », Astaroth grand trésorier, Nergal chef de la police secrète, Baal général en chef), une **justice** (Lucifer grand-justicier), une **maison des princes** (« Chamoos, grand-chambellan », graphie de l'OCR, entre autres) et des **ambassadeurs par pays** : « Belphégor, ambassadeur en France. Mammon, ambassadeur en Angleterre. Belial, ambassadeur en Italie… ». Il cite enfin Berbiguier (1821) : « Cette cour a aussi ses représentans sur la terre ».

**Déduction 4 (sûre, sur ta source) :** dans ton corpus, la hiérarchie infernale **n'est pas un système à part**. C'est une **copie explicite d'une monarchie humaine**, avec les mêmes offices (chambellan, chancelier, trésorier, justicier, général) et une diplomatie **par pays**. Un des titres de tes brouillons (« chambellan ») y figure tel quel.

**Conséquence pour la question ouverte de `inference_du_projet.md` §1.2** (« la hiérarchie des démons double-t-elle celle des institutions humaines, ou l'ignore-t-elle ? ») : ta source penche nettement pour « **elle la double** ». Ce n'est pas une décision, mais ce n'est plus seulement une idée de l'IA : c'est **le texte de 1825**.

**Nuance (observée) :** tu as écrit qu'il ne faut « pas se focaliser seulement sur la partie populaire (les 72 démons) » du dictionnaire (U, brouillons). Or Gremory, Furfur, Marbas et Stolas appartiennent tous à cette liste de 72 (vérifié : liste de l'*Ars Goetia*, numéros 56, 34, 5 et 36). Tu les as choisis pour leur design (dépôt : fiche créatures). La Cour infernale, elle, est justement **hors de la liste des 72** : c'est la partie du dictionnaire qui va dans le sens de ta remarque.

**Test :** te représentes-tu un démon comme ayant un **office** (chambellan, ambassadeur) en plus d'un **rang** (duc, comte) ? Si oui, la ligne L3 est cohérente avec ton envie.

---

### L4. Le statut conféré : « Chevalier », gimmick latent

**Observé** (six signaux indépendants)
1. Goal de Brann : « devenir chevalier, ou un goal similaire » (U, `interet`).
2. Tenue de Brann d'après *Fabula Fantasia* : elle a sa place « surtout pour des personnages de **profession** « Chevalier » » (U, YAML). Note le mot « profession ».
3. Matière arthurienne décidée (lieux et inspirations).
4. Vocabulaire : « tournoi de chevalerie », « champion », « première lame » (U, brouillons).
5. Le *Dictionnaire féodal* : ORDRES DE CHEVALERIE, CHAMPIONS, JUGEMENS (dépôt : BRIEF §7, D1 et D3).
6. Ta liste de gimmicks est **entièrement faite de métiers ou de statuts** : Pirate, Ninja, Shinigami, Épéiste/Samurai, Mage, Exorciste, Alchimiste, Hunter (YAML).

**Déduction 5 :** dans le *Conte du Graal*, le premier but déclaré de Perceval est de trouver « le roi qui fait les chevaliers » (dépôt : `debuts…`, lu en ancien français). Perceval est une des quatre inspirations de Brann (YAML). Le goal qui t'intéresse pour Brann est donc **exactement** le goal d'ouverture de son inspiration médiévale. C'est la **seule** de ses quatre inspirations dont le goal coïncide avec le sien : Luffy veut devenir Roi des pirates, Yusuke revenir à la vie, Edward récupérer les corps.

**Induction 2 :** « Chevalier » a la même forme que les entrées de ta liste de gimmicks : un métier ou un statut que le héros **obtient** ou **porte**.

**Abduction 3 :** « Chevalier » est le **candidat implicite** au champ `gimmick_edenia`, aujourd'hui vide. C'est ce que suggère la convergence des six signaux, pas ce que tu as dit.

**Le risque, par déduction :** les tomes 1-6 de *Radiant* contiennent l'**Ordre des Chevaliers-Sorciers**, **Caislean Merlin** et une île-continent de chevaliers (dépôt : fiche Radiant). Et la tenue de Brann vient du spin-off de *Radiant*. Le gimmick le plus soutenu par tes choix tombe donc **précisément** dans la zone où tu as décidé de te détacher de *Radiant* (décision 18). C'est la tension la plus importante du dossier.

**Ce que tes sources offrent pour s'en distinguer (constat sur le dépôt) :** l'angle **féodal et juridique** du *Dictionnaire féodal*, que *Radiant* n'exploite pas dans les tomes 1-6 tels que la fiche les décrit :
- il faut être « noble de père et de mère, trois générations » ;
- « on ne voit pas qu'un bon roturier soit jamais entré dans la chevalerie » ;
- la félonie ;
- le champion du jugement par combat (dépôt : BRIEF §7, D1 à D3).

Avec un Brann **sans nom de famille** (décidé), le goal « devenir chevalier » devient **une transgression sociale**. L'IA avait déjà formulé cette idée (BRIEF, A5) ; elle est ici rattachée à la tension avec *Radiant*.

**Test :** si quelqu'un te demandait « c'est quoi le Pirate / le Ninja d'Edenia ? », répondrais-tu « Chevalier » ? Et en quoi ton chevalier n'est-il pas un Chevalier-Sorcier de *Radiant* ?

---

### L5. Un temps de conte borné pour garder le corps-à-corps

**Observé, dans l'ordre chronologique**
- 8 oct. (U) : « l'échelle de puissance […], le style des combats, les armes ont un impact sur le style de récit. Certaines scènes comme la guerre peuvent être obsolètes, par exemple le *sword fighting* » (`structures…` §36).
- 12 oct. (U) : armes à feu plafonnées à **1860** (décidé) ; plafond général abaissé de 1950 à **1914** (envisagé) ; régions inégales selon les **ressources magiques et naturelles** (envisagé).
- *BioShock Infinite* se passe en **1912** (vérifié : Wikipédia EN).

**Déduction 6 :** le plafond 1860 répond à ta propre observation du 8 octobre. Il exclut la mitrailleuse et la poudre sans fumée (dépôt : `modeles…` §5.3), ce qui garde l'épée viable. Ce n'est pas un choix isolé : c'est **la réponse logique au problème que tu avais posé quatre jours plus tôt**.

**Déduction 7 :** le passage de 1950 à 1914 **rapproche le plafond de la date de *BioShock Infinite*** (1912). La zone industrielle décidée tient donc presque entière sous le nouveau plafond.

**Déduction 8 :** une cité volante comme Columbia **dépasse** toute technologie de 1914. Dans Edenia, seule la **technologie magique** (hors plafond, décidé) peut la porter. Le principe « les ressources magiques font l'avance technologique » (envisagé le 12 oct.) n'est donc pas un ajout arbitraire : c'est **la condition pour que la zone industrielle décidée et le plafond 1914 tiennent ensemble**.

**Ce que ça dit de l'œuvre :** ta logique technologique est **cohérente et cumulative** (8 oct. → 12 oct.). Le monde a trois régimes : ordinaire (médiéval à 1860), industriel (jusqu'à 1914) et magique (sans plafond). C'est exactement la proposition « décrire le temps par régimes » de `inference_du_projet.md` §1.4, que tes décisions viennent remplir.

**Deux frictions** (voir §3) : la zone « mafieux années 20-30 » et l'iconographie du western.

---

### L6. Le conte relu, et une matrice commune : la Bibliothèque bleue

**Observé**
- Ambiance « de conte européen au sens large » (U) ; Forêt de conte (décidée) ; marais de Shrek ; lieu « Shrekien » ; *Shrek* et *Red Hood* associés à la relecture de contes (U, 3 oct.) ; *Fabula Fantasia* (« fabula » = récit, fable).
- Bibliothèque bleue : intérêt pour **le contenu des livres** (U, qui précise que cela n'a rien à voir avec le métier de colporteur).
- Ce que contenait la Bibliothèque bleue (vérifié : Médiathèque de Troyes ; Plume d'histoire) :
  - des **romans de chevalerie**, dont ***Mélusine*** ;
  - *La devise des armes des chevaliers de la **Table Ronde*** ;
  - des **contes** (dont ceux de Perrault) ;
  - des **prophéties**, de l'**astrologie**, des almanachs ;
  - des danses macabres et des vies de saints.

**Déduction 9 (sur sources vérifiées) :** trois de tes matières, qui semblent hétérogènes, **circulaient dans les mêmes petits livres** pendant près de trois siècles :
- la **chevalerie arthurienne** (décidée) ;
- le **conte** (ambiance décidée) ;
- la **superstition, la prophétie et l'astrologie** (cousines de l'occultisme « d'ambiance » de ton YAML et du *Dictionnaire infernal*).

Mélusine, que tu envisages, en fait partie.

**Abduction 4 :** ton intérêt pour la Bibliothèque bleue serait le **liant historique** de ton projet : la culture populaire française de l'imprimé, où chevaliers, fées, diables et almanachs se côtoient. Cela expliquerait pourquoi ces matières te semblent aller ensemble sans que tu aies eu besoin de le justifier.

**Lien avec un détail du YAML :** pour les livres de sorts, ce qui compte surtout, ce sont « **les symboles sur le livre** » (U, 7 oct.). Dans l'article AGRIPPA (décidé), le chien noir familier porte « un collier garni de clous qui formaient des **inscriptions nécromantiques** » (DI 1825, lu aujourd'hui). Ta seule figure décidée est donc attachée, dans ta source, à un **objet-symbole**, ce qui correspond à ta préférence.

**Test :** quand tu penses « Bibliothèque bleue », penses-tu aux romans de chevalerie et aux contes, ou plutôt aux almanachs et aux prophéties ? Si c'est aux deux, l'abduction 4 tient.

---

### L7. Le ton : l'exposition sous tension

**Observé**
- Ton visé plus proche de *Red Hood* et *HxH* que de *FMA* (U, 7 oct.) ; Tarantino, « son style et sa filmographie complète » (U, 8 oct.) ; *Worm*, « HxH + Watchmen » (U).
- `structures…` §4 a déjà relevé que **l'examen Hunter fonctionne comme la scène de la ferme d'*Inglourious Basterds*** : l'exposition se fait par un interrogatoire sous tension.
- Schéma de *HxH* : « duel résolu par l'exploitation d'une règle » (dépôt : fiche HxH).
- Reproche le plus durable du public à *Radiant* : « beaucoup d'explications plutôt que de la mise en scène », « trop de blabla explicatif » (dépôt : fiche Radiant). Reproche fait à *Red Hood* : « explication par l'antagoniste (critiquée) » (dépôt : addendum, cité dans `structures…` §3).

**Induction 3 :** tes influences de ton (HxH, Tarantino) partagent un même procédé : **l'information passe par une scène où quelque chose est en jeu** (examen, interrogatoire, duel de règles), pas par un bloc d'explication.

**Déduction 10 :** ce procédé est l'opposé exact du défaut le plus cité chez *Radiant*, l'œuvre qui occupe ta case (L1). Tes goûts de ton forment donc, sans que tu l'aies dit, **une réponse au principal défaut de ton concurrent le plus proche**.

**Test :** dans les scènes que tu imagines, l'exposition passe-t-elle déjà par un dialogue sous tension ? Si oui, L7 décrit ton goût. Si non, c'est une piste et pas un constat.

---

### L8. Les trois personnages : une composition par rôles

**Observé** (YAML ; rôles dans les œuvres sources d'après le dépôt et la mémoire)

| Personnage | Inspirations | Place de ces inspirations dans leur œuvre |
|---|---|---|
| **Brann** | Luffy, Yusuke, Edward, Perceval | **4 sur 4 sont le protagoniste central** de leur œuvre (dépôt : fiches et `debuts…`) |
| **Cosmo Dumas** | Ekko, Killua, Shisui | Killua est deutéragoniste (vérifié Fandom, BRIEF) et **1ᵉʳ des sondages officiels de HxH** (dépôt : fiche HxH) ; Shisui est un personnage secondaire (mémoire ; le BRIEF a vérifié sur Fandom : Anbu, meilleur ami d'Itachi, « Body Flicker ») ; Ekko est un champion de *League of Legends*, univers sans protagoniste unique (mémoire) |
| **Harley Delphine** | Shallan, Hermione, Tattletale, Magik | Shallan : point de vue principal (lu, `structures…` partie E) ; Hermione : deutéragoniste (mémoire) ; Tattletale : « 1ʳᵉ » des brackets de *Worm* (dépôt : fiche Worm) ; Magik : sorcière liée aux Limbes (vérifié Fandom, BRIEF) |

**Induction 4 :** les trois personnages sont construits **par rôle**, pas par mélange au hasard :
- **Brann = le héros** : uniquement des protagonistes centraux, dont trois héros de battle shōnen à goal simple ;
- **Cosmo = le second aimé** : il réunit des « seconds rôles » ; Killua est l'exemple type du second plus aimé que le héros ;
- **Harley = le savoir et le secret** : quatre figures de l'intelligence, de l'information ou du savoir caché.

C'est cohérent avec l'inférence existante « élan / ruse / savoir » (`inference_du_projet.md` §1.5), en plus précis.

**Déduction 11 :** Harley est **le seul personnage dont une inspiration figure aussi dans ta liste de l'au-delà** : « Limbo de Magik » est en `interet` (YAML). Agrippa, ta seule figure décidée, est dans ta source un savant « **trop instruit peut-être pour le temps où il parut ; on l'accusa de sorcellerie** » (DI 1825, AGRIPPA).
**Abduction 5 :** Harley serait le **point de contact** du récit avec l'occulte et l'au-delà « en fond », par le savoir (Agrippa) plutôt que par le combat. L'idée « Harley paie son savoir » existe déjà (BRIEF, A4) ; elle est ici rattachée à Agrippa et au Limbo.

**Induction faible (à vérifier) :** les trois inspirations de Cosmo ont peut-être en commun le **prodige rapide**. le « Body Flicker » de Shisui est vérifié (Fandom, BRIEF) ; pour Killua (vitesse) et Ekko (temps), c'est de mémoire. *Attention :* une « limite de vitesse décidée » citée par une autre discussion n'existe pas dans le YAML (dépôt : `modeles…` §5.3). Je ne m'appuie donc pas dessus.

**Observation sur les noms (pas une inférence sur ton intention) :**
- « Dumas » et « Delphine » sont des noms français ; « Brann » ne l'est pas.
- **Brann Bronzebeard**, avec deux « n », est un explorateur nain de *Warcraft / Hearthstone*, fondateur de la Ligue des explorateurs, au « courage excessif » (vérifié : Hearthstone wiki). *Warcraft / Hearthstone* fait partie de tes influences (YAML).
- Je ne sais pas si le nom vient de là, de *Bran* dans *Game of Thrones* ou d'ailleurs. **Question simple, si tu veux y répondre :** d'où vient « Brann » ?

**Tension avec les données du dépôt (hypothèse de l'IA déjà archivée, pas une règle) :** `annexe_hypotheses_IA.md` §1 observe que le protagoniste n'est le préféré que dans 2 cas sur 8 mesurables. Construire Cosmo à partir de Killua, c'est construire **le profil qui bat le héros** dans *HxH*. Que Cosmo dépasse Brann en popularité serait alors une conséquence probable, pas un accident. *Hypothèse sur n = 8, sans causalité.*

---

### L9. *Witcher 3* + *Runeterra* + *FMA* : des couches plutôt qu'un dosage

**Observé :** tu as dit « les trois en mélangé », sans dosage (U, 11 oct.). Selon toi, *FMA* correspond au modèle « un pays principal, avec des régions culturelles et des voisins pas forcément visités » (U, « je crois »). Tes brouillons citent Velen (*Witcher 3*) pour le marais, et tu as découvert la Chasse sauvage avec *Witcher 3* (dépôt : fiche créatures). *Runeterra* est ta « référence principale du monde » (dépôt) et ton modèle de tenues (U).

**Abduction 6 :** chacune des trois œuvres fournit une **couche différente**, ce qui expliquerait l'impossibilité de donner un dosage :

| Couche | Œuvre | Ce qu'elle apporte (d'après tes propres mots) |
|---|---|---|
| **Topologie** (combien de pays, lesquels on visite) | *FMA* | « un pays principal, des voisins pas forcément visités » (U) |
| **Diversité des régimes et des esthétiques** | *Runeterra* | une région = un régime et un style (dépôt : `modeles…` §4, type H) ; tenues |
| **Texture des marges** (folklore, marais, cité libre, guerre) | *Witcher 3* | Velen, la Chasse sauvage, Novigrad (dépôt : `modeles…` §4) |

**Déduction 12 :** les trois modèles placent tous une **puissance impériale** dans ou près du monde visité : Nilfgaard, Noxus, Amestris (dépôt : `modeles…` §4, type D). Or tes brouillons contiennent une zone « **Empire** » et le titre « **empereur** » (U, `interet`), alors que ton plan ne mentionne pas d'empire.
**Abduction 7 :** l'« Empire » serait **un des royaumes adjacents**, sur le modèle Nilfgaard/Noxus. C'est cohérent avec ta distance au cadre militaire de *FMA* (U), qui écarte un royaume principal impérial.

**Test :** dans ta tête, l'Empire est-il le royaume principal, un voisin, ou un passé (un empire déchu) ?

---

## 3. Tensions et frictions repérées

| # | Tension | Raisonnement | Gravité |
|---|---|---|---|
| **T1** | Zone « mafieux années 20-30 (prohibition) » (`interet`) ↔ armes à feu 1860 (décidé) et plafond 1914 (envisagé) | L'imagerie de la Prohibition repose sur la mitraillette Thompson (vers 1919-1921) et l'automobile (mémoire). Avec tes plafonds, la zone ne peut garder que **le modèle social** (pouvoir non étatique, type O de `modeles…`) et le **costume**, pas l'armement. | Moyenne : la zone n'est qu'en `interet` |
| **T2** | Zone **western** (décidée) ↔ armes à feu 1860 | Les armes emblématiques du western classique, le Colt Single Action Army et la Winchester 1873, datent de **1873** (mémoire). À 1860, on a le revolver à percussion et, selon ce que tu inclus, les carabines Spencer et Henry (dépôt : `modeles…` §5.3). Ton western serait **« d'avant le western »** côté armes. | Faible si c'est voulu ; à savoir pour le design |
| **T3** | Gimmick latent « Chevalier » ↔ distance à *Radiant* | Voir L4 : c'est le recouvrement le plus fort (Chevaliers-Sorciers, Caislean Merlin, tenue tirée de *Fabula Fantasia*). | **Forte** |
| **T4** | « Ne pas se focaliser sur les 72 démons » ↔ les 4 démons envisagés sont dans les 72 | Voir L3. La Cour infernale offre la partie « hors 72 ». | Faible (choix de design assumé) |
| **T5** | Tournoi de chevalerie (`interet`) ↔ retrait du « personnage qui passe des épreuves » (9 oct.) | Un tournoi est une épreuve. S'en servir comme **lieu de convergence** (voir P5) n'est pas la même chose qu'une **formation par épreuves**, mais la frontière est mince. | À surveiller |
| **T6** | Trois modèles d'institution en concurrence : **académie** (Academy Ekko, « Barrier Mage », école de Brocéliande, *Harry Potter*), **guilde** (*HxH*, *Red Hood*), **chevalerie** (L4) | La tenue qui t'inspire le plus est **un uniforme d'académie** (U : « tenue qui l'inspire le plus »). Le ton te tire vers la **guilde**, et le goal de Brann vers la **chevalerie**. | Ouverte, et c'est normal à ce stade |
| **T7** | *Shrek* (parodie) ↔ ton sérieux *HxH* / *Red Hood* | Tu associes *Shrek* à la **relecture** de contes, pas forcément à son humour (U, 3 oct.). L'humour de *Radiant* est un reproche récurrent (dépôt). | Faible, si *Shrek* sert pour l'ambiance et la relecture |
| **T8** | « Un seul monde, une seule époque » ↔ des époques mélangées dans les inspirations | Résolu par « temps flou » et par les régimes (L5) : l'unité est **chronologique**, le mélange est **stylistique**. | Résolue |

---

## 4. Verdict : y a-t-il une logique ?

**Oui.** Trois principes suffisent à expliquer la grande majorité de ce qui est décidé ou envisagé :

| Principe (inféré par l'IA) | Ce qu'il explique | Lignes |
|---|---|---|
| **P-A. Forme shōnen japonaise, matière populaire française** | manga en parution française, gimmicks-métiers, lieux arthuriens français, folklore régional, DI et DF, Bibliothèque bleue, distance à *Radiant* | L1, L2, L6 |
| **P-B. Un monde de rangs**, où l'ordre humain et l'ordre infernal suivent le même modèle de cour | titres des brouillons, Gotei 13, démons à titres féodaux, Cour infernale, chevalerie, institutions | L3, L4 |
| **P-C. Un temps de conte borné pour garder le combat rapproché**, débloqué par la magie | 1860, 1914, *BioShock* 1912, technologie magique, inégalité par les ressources, régimes de temps | L5 |

Le **ton** (L7) et la **composition des personnages** (L8) obéissent à une logique distincte : celle d'un lecteur qui retient ce qui fait **durer** une série (le second aimé, l'exposition sous tension, le héros à goal simple).

**Ce que ces trois principes n'expliquent pas (le reste) :** *Urban Rivals*, *Worm*, les objets bouddhiques, les personnages d'inspiration asiatique, les folklores gréco-égyptiens, Tarantino (sauf pour le ton). Pour les héritages non français, L2 propose une place (cités-États, adjacents). Pour le reste, je ne vois pas de logique et je n'en invente pas.

**Ce que dit l'œuvre, en une phrase (synthèse de l'IA, à ta validation) :**
> Un battle shōnen à la japonaise dont le monde est une France de conte, tenue par des rangs qui se reflètent du château jusqu'en enfer, à une époque où l'épée compte encore parce que la poudre s'est arrêtée en 1860 et où seule la magie va plus loin.

---

## 5. Possibilités qu'on peut inférer (propositions de l'IA, non décidées)

Chaque possibilité indique d'où elle vient, ce qu'elle produirait, son risque et son test. Aucune ne remplit un champ vide du YAML.

### P1. Le royaume principal comme « France de conte » en provinces
- **D'où :** L2 (abduction 2) et L9.
- **Ce que ça produit :** chaque province a sa créature et son paysage (Bretagne et Ankou ; Alpes et Barbegazi ; Provence et Tarasque ; Nord et Gayant). Le tableau « région → héritage → créatures → paysage → tenues » proposé dans `inference_du_projet.md` §1.1 devient simple à remplir.
- **Risque :** une carte trop calquée sur la France (lisible pour un Français, plate pour les autres). Ta « parution française » (décidée) limite ce risque.
- **Test :** voir L2.

### P2. Des démons ambassadeurs, un par royaume
- **D'où :** déduction 4 (COUR INFERNALE : « Belphégor, ambassadeur en France… », « cette cour a aussi ses représentans sur la terre »), plus ton plan « royaume principal + adjacents ».
- **Ce que ça produit :** un au-delà présent « **en fond** », comme tu le souhaites (U), sans cosmologie à expliquer. Chaque royaume a son représentant infernal, avec un **office** (chambellan, chancelier) et un **rang** (duc, comte) tirés de ta source.
- **Risque :** un ton trop satirique. Collin de Plancy écrit ces listes avec ironie (ton « voltairien », d'après les champs de la base).
- **Test :** voir L3.

### P3. « Chevalier » comme métier interdit au roturier
- **D'où :** L4 (abduction 3, déduction 5) et BRIEF A5.
- **Ce que ça produit :** un goal court et lisible (« devenir chevalier ») qui est **en même temps une transgression** (pas de nom, pas de lignage), ce qui distingue Brann du Chevalier-Sorcier de *Radiant* par l'angle **féodal**.
- **Risque :** T3. Et un goal « compétitif » (accéder à un rang) est, dans l'hypothèse archivée de l'IA, moins porteur d'attachement qu'un goal de liberté (annexe §1, n = 8, sans causalité).
- **Test :** voir L4.

### P4. L'inégalité technologique comme fabrique d'accusations de sorcellerie
- **D'où :** L5 (régions inégales) + AGRIPPA (« trop instruit […] on l'accusa de sorcellerie ») + BRIEF D5 (« le savoir qui innove passe pour de la magie »).
- **Ce que ça produit :** un ingénieur d'une cité-État avancée est pris pour un sorcier dans une province à technologie de 1860. Cela donne un conflit **sans antagoniste** : le décalage de technologie suffit. Le lien avec Harley (L8) est direct.
- **Risque :** que la frontière entre « technologie magique » et « technologie de 1914 » devienne floue pour le lecteur. Il faudrait un signe visuel distinctif.
- **Test :** dans une province, quelqu'un saurait-il distinguer une machine d'un sortilège ?

### P5. Le tournoi de chevalerie comme lieu de convergence
- **D'où :** tes trois personnages « probablement séparés » (dépôt : `structures…` §35 ; *attention*, l'annexe §10.3 signale que la citation n'a pas été relue à la source) ; le lieu de convergence installé tôt (*Basterds*, Yorknew : `structures…` §2 et §4) ; tournoi et foires en `interet`.
- **Ce que ça produit :** un événement d'origine européenne (tournoi, foire) qui joue le rôle structurel de l'examen Hunter ou de l'examen chūnin : **réunir des fils séparés en un lieu et une date**.
- **Risque :** T5. Il faut qu'il serve à **réunir**, pas à **former par épreuves** (que tu as retiré).
- **Test :** le tournoi te plaît-il comme événement du monde, indépendamment des héros ?

### P6. Une cause différente par couche de territoire
- **D'où :** `modeles…` §5.2 propose trois causes concurrentes (H1 ressource, H2 histoire et guerre, H3 géographie et réseau) ; L9 propose trois couches.
- **Ce que ça produit :** pas besoin de choisir une cause unique.
  - Les **cités-États** suivraient la **ressource** (H1, comme Piltover, et comme ta règle envisagée du 12 oct.).
  - Le **royaume principal** suivrait l'**histoire** (H2 : qui a gagné quelles guerres, comme le *Witcher*). Les lieux arthuriens envisagés évoquent des royaumes conquis (BRIEF A2, affaibli : tu ne connais pas ces lieux).
  - Les **confins** (western, désert) suivraient la **distance au centre** (H3 : le shérif aux marges).
- **Risque :** une complexité à doser pour un manga.
- **Test :** la question de `modeles…` §5.2 (« qu'est-ce qui rend différentes la cité industrielle et une baronnie rurale ? ») reste le meilleur test. La réponse peut être « pas la même chose selon la zone ».

### P7. La Bibliothèque bleue comme réservoir de récits et d'objets
- **D'où :** déduction 9 et abduction 4.
- **Ce que ça produit :** des objets du monde (almanachs, prophéties, livrets de chevalerie, contes) qui portent des **symboles** (ta priorité pour les livres) sans effet magique visible, ce qui est cohérent avec ton occultisme « d'ambiance » (U). Et un réservoir de récits que ton monde peut citer comme ses propres légendes, Mélusine comprise.
- **Risque :** aucun pour la cohérence ; le colportage est écarté comme tu l'as précisé.
- **Test :** voir L6.

### P8. Cosmo, le « second aimé » : décider s'il doit éclipser Brann
- **D'où :** L8 (Cosmo construit sur Killua) et annexe §1 (hypothèse archivée).
- **Ce que ça produit :** soit l'effet est **assumé** (le second aimé fait vivre le duo, comme Killua), soit il est **compensé** en donnant à Brann ce qui manque aux héros moins aimés de ton corpus. Ce point reste à étudier ; je n'ai pas de donnée pour dire quoi.
- **Risque :** l'hypothèse repose sur n = 8 sondages hétérogènes.
- **Test :** aucun pour l'instant. C'est une vigilance, pas une question à trancher.

---

## 6. Limites de cette analyse

- **Aucune relecture des œuvres.** Les rôles d'Ekko, d'Hermione, de Tattletale et la « vitesse » de Killua sont **de mémoire** (signalé). Les dates d'armes (Thompson, Colt SAA et Winchester 1873) sont **de mémoire**.
- **Vérifié aujourd'hui :**
  - les articles GOMORY, FURFUR, MARBAS, STOLAS, COUR INFERNALE et AGRIPPA dans la base DI 1825 de ton dépôt ;
  - *BioShock Infinite* en 1912 et Columbia comme cité-État (Wikipédia EN) ;
  - le contenu de la Bibliothèque bleue (Médiathèque de Troyes, Plume d'histoire) ;
  - Brann Bronzebeard (Hearthstone wiki) ;
  - les numéros de l'*Ars Goetia*.
- **Les limites anti-spoil sont respectées** : rien au-delà de *Radiant* tome 6, *JJK* ép. 59, *One Piece* ch. 984, *Stormlight* ch. 15, *Worm* arc 9, *LotR* livre II ch. 10, *Kingkiller* ch. 8, *GoT* S7. Les éléments de *HxH* cités (Killua) relèvent d'une œuvre sans limite indiquée.
- **Les inductions reposent sur de petits ensembles** (6 signaux pour L4, 4 inspirations par personnage). Elles indiquent une direction, elles ne prouvent rien.
- **Je n'ai pas lu** tes documents « Worldbuilding parties 1 et 2 » ni le « document sans titre 29 » : ils ne sont pas dans le dépôt, seules leurs validations y sont.
- **Rien n'a été écrit dans le YAML.**


---
---

# ADDENDUM du 12 octobre 2026 (2ᵉ partie) : Hearthstone, et tes propres extraits du *Dictionnaire infernal*

**Pourquoi cet addendum :**
1. Tu as précisé que *Hearthstone* t'a beaucoup influencé et **t'a donné l'envie de créer cette œuvre de fantasy** (U, 12 oct.). Ton dépôt disait seulement : « grande influence sur l'esthétique d'Edenia » (`influences-atelier.md`).
2. Tu m'as reproché, à juste titre, de ne pas avoir utilisé **tes extraits** (`Pdfmd/Dictionnaire_Infernal_Extraits.md` et `…_43-88.md`) pour le *Dictionnaire infernal*.

**Correction :** dans les §1 à §6, j'ai cherché Gomory, Furfur, Marbas, Stolas et la COUR INFERNALE dans la **base complète** de 1825. Aucun de ces articles n'est dans tes extraits. Dans tes extraits, je n'avais exploité qu'AGRIPPA. Ce qui suit repart de **ta sélection** : 89 articles, environ 44 800 mots d'après mon comptage. Les citations ci-dessous viennent de ces deux fichiers (versions 1818, 1825 ou 1863 selon l'article).

**Nouvelles étiquettes :** **(extraits, ARTICLE)** = lu aujourd'hui dans tes fichiers `Pdfmd/`.

---

## 7. Hearthstone : est-ce que ça change la dimension de l'analyse ?

### 7.1 Ce qui change : on passe de l'influence esthétique au déclencheur

| Avant (dépôt) | Maintenant (U, 12 oct.) |
|---|---|
| Runeterra = référence principale ; Warcraft/WoW = secondaire, perçu « hard rock / solennel » (`Benchmark Oeuvre/01_CONTEXTE_ET_SUITE`) | *Hearthstone* est **à l'origine de ton envie** de faire cette œuvre de fantasy |
| Warcraft : « grande influence sur l'esthétique […] surtout les paysages forestiers. Mais en vrai, l'esthétique d'Edenia est beaucoup plus proche de Runeterra » (U, `influences-atelier.md`) | — |

**Déduction 12 :** ces deux informations ne se contredisent pas, parce qu'elles ne répondent pas à la même question :
- *Hearthstone* répond à **« pourquoi un monde de fantasy, et de quelle forme ? »** ;
- Runeterra répond à **« à quoi il ressemble ? »** ;
- *HxH*, *AoT* et *GoT* (découverts entre 14 et 16 ans, « plus sérieux », U) répondent à **« sur quel ton ? »**.

**Ce que ça change dans l'analyse :** les §2 à §4 cherchaient la logique dans le **contenu** (France, rangs, temps borné). *Hearthstone* invite à chercher aussi une logique dans la **forme du désir de départ** : quel genre de monde tu as eu envie de construire. C'est un niveau en dessous des trois principes P-A, P-B et P-C. Il ne les remplace pas.

**Ce que ça ne change pas :** *Hearthstone* n'explique ni la matière française (L1, L2), ni le *Dictionnaire infernal*, ni la Bibliothèque bleue (L6). Ces choix ont une autre source.

### 7.2 Une logique de jeu de cartes (induction)

**Observé :** trois jeux de cartes jalonnent ta généalogie.

| Âge | Jeu | Ce que tu en dis ou ce qu'on en sait |
|---|---|---|
| vers 11 ans | *Urban Rivals* | « attrait pour les jeux de cartes en ligne et pour les **univers hétéroclites, avec des gangs et des designs reconnaissables** » (U) ; clans-mélanges : Skeelz = HP + X-Men, Frozn = nordique + Yéti + technologie, Raptors = Mad Max + Jurassic Park (U) |
| vers 14 ans | *Hearthstone* | ton entrée dans Warcraft, vers la Ligue des explorateurs (12 nov. 2015, ta note de bas de page) |
| ? | *Legends of Runeterra* | dans ton répertoire (U) |

**Induction 5 :** dans ces trois jeux, le monde se présente sous la même forme : des **factions juxtaposées**, chacune avec un **thème** et un **design reconnaissable**, et une **image par carte**. Ta liste de zones des brouillons a exactement cette forme : chaque zone porte le nom d'une source (Bilgewater, Piltover/Columbia, Gadgetzan, marais de Shrek, Brocéliande-Harry Potter, Ionia, Freljord). Tu dis toi-même que ces zones sont « inspirés des MMORPG et des contes » (U, YAML).

**De mémoire (non vérifié) :** dans *Legends of Runeterra*, les cartes sont classées **par région** (Ionia, Freljord, Piltover et Zaun, Bilgewater…). Si c'est exact, les régions de Runeterra que tu cites sont, dans un de tes jeux, **littéralement des factions de cartes**.

**Abduction 6 :** ta formule « le monde hétéroclite […] c'est plutôt une **convention de base**, sinon le monde paraîtrait répétitif » (U) est une **convention de jeu de cartes** : une extension (ou un clan) = un thème neuf. Cela explique trois choses que les §2-§4 laissaient de côté :
1. ***Urban Rivals*** : je l'avais classé dans « ce que les trois principes n'expliquent pas » (§4). Il s'explique maintenant : c'est **le premier modèle de la mosaïque**.
2. **Le choix par l'image :** Gremory, Furfur, Marbas et Stolas sont choisis « pour leur design et leurs fanarts » (dépôt : fiche créatures). Les créatures viennent d'une **carte illustrée** (« Mythical Beasts of France »). Tes images sont un « réservoir d'éléments à combiner » (U). C'est la manière dont on lit une carte à jouer : **l'illustration d'abord**.
3. **Les gimmicks-métiers :** dans *Hearthstone*, on joue une **classe** (Mage, Paladin, Chasseur… ; mémoire). Ta liste de gimmicks contient trois métiers **sans œuvre attachée** : Épéiste/Samurai, Mage, Exorciste (YAML). Hypothèse **faible** : « Mage » pourrait venir de là. Pour « Exorciste », tes extraits offrent une meilleure source (voir §8.3, GRANDIER).

**Nouveau principe proposé (IA) :**

> **P-D. Un monde en mosaïque de factions lisibles**, hérité des jeux de cartes (*Urban Rivals* → *Hearthstone* → *Legends of Runeterra*) : chaque zone a son thème et son design, et l'hétérogénéité est une règle, pas un défaut.

P-D ne contredit pas P-A : la **forme** est une mosaïque de jeu de cartes, la **matière** du royaume principal est française.

### 7.3 Ce que Hearthstone soutient (élément par élément)

| Élément d'Edenia | Lien avec *Hearthstone* / Warcraft | Force |
|---|---|---|
| **« Gadgetzan »** dans ta liste de zones (« Piltover-BioShock 1 / Gadgetzan », YAML) | Dans *Hearthstone*, *Mean Streets of Gadgetzan* (1ᵉʳ déc. 2016) se passe dans une « **ville portuaire sans loi** » dirigée par **trois familles criminelles** : les Grimy Goons (brutes), le Jade Lotus (assassins) et le Kabal (**lanceurs de sorts**) (vérifié : hearthstone.wiki.gg, page « Expansion »). Tu l'aurais découvert vers 15 ans si tu jouais encore. | **Forte** : le nom est dans ton brouillon |
| **Forêt de conte** (décidée) | Tu dis que Warcraft t'a influencé « surtout [pour] les paysages forestiers » (U). *The Witchwood* (12 avril 2018) se passe à Gilneas, un royaume de **worgens** (loups-garous), dont une sorcière a **corrompu la forêt voisine** (vérifié : wiki Fandom). | **Forte** pour la forêt (tes mots) ; *Witchwood* : à confirmer (as-tu joué cette extension ?) |
| **Brann** (nom) | Ton entrée dans *Hearthstone* coïncide avec la **Ligue des explorateurs**. Brann Barbe-de-Bronze est le fondateur de la Ligue des explorateurs (vérifié lors de la 1ʳᵉ partie : hearthstone.wiki.gg). | L'hypothèse se renforce, mais **seule ta réponse peut la confirmer** |
| **Chevalier / tournoi** (L4, P5) | *Le Grand Tournoi* (24 août 2015, mécanique « Joute », vérifié) sort trois mois avant ton entrée. La classe Paladin et l'ordre de la Main d'argent (mémoire). | **Faible** : on ne sait pas si tu y as joué |
| **Royaume principal + cités-États + royaumes adjacents** (envisagé) | Les royaumes humains de Warcraft avec Dalaran, cité-État de mages (mémoire). | Faible : tu cites *Witcher 3*, Runeterra et *FMA* pour ce point, pas Warcraft |
| **Armes à feu limitées, corps-à-corps dominant** (L5) | Dans Warcraft, des nains armés de fusils dans un monde où l'épée domine (mémoire). | Faible : simple compatibilité |

### 7.4 Ce que Hearthstone explique : la friction T1 s'atténue

**Rappel de T1 (§3) :** la zone « mafieux années 20-30 (prohibition) » suppose la mitraillette Thompson et l'automobile, ce qui heurte tes plafonds (1860 pour les armes, 1914 envisagé).

**Abduction 7 :** si ton idée de mafia vient (aussi) de **Gadgetzan**, elle n'a pas besoin de l'armement historique. Le modèle de Gadgetzan est **une ville-port sans loi, tenue par des familles criminelles**, dont une famille de **sorciers**. C'est un modèle social (pouvoir non étatique, type O de `modeles…`) qui tient **sans Thompson**, et où la magie remplace l'arme à feu moderne. T1 passe donc de « moyenne » à « **faible** » si c'est bien ta source. Question à te poser : « mafieux années 20-30 » et « Gadgetzan » désignent-ils la même zone dans ton brouillon ?

### 7.5 Une tension de ton à garder en tête

- *Hearthstone* a un ton **humoristique et léger** (mémoire, mais très largement connu).
- Tu perçois Warcraft comme « **hard rock / solennel** » (dépôt : Benchmark).
- Le ton visé pour Edenia vient de *HxH* et de *Red Hood* (YAML), avec Tarantino.

**Formule de synthèse (IA, à valider) :** *le désir de monde vient de Hearthstone, le visuel de Runeterra, le ton de HxH.* C'est cohérent avec ton parcours : *HxH*, *AoT* et *GoT* arrivent juste **après** *Hearthstone* (entre 14 et 16 ans) et sont décrits comme « plus sérieux » (U). Le risque : que l'héritage « cartes » pousse vers des zones-gags. Ta remarque sur *Shrek* (relecture, pas parodie, U) montre que tu fais déjà ce tri.

### 7.6 Une nouvelle tension : la carte contre le mythe (T9)

**T9 :** l'héritage du jeu de cartes pousse à présenter chaque créature comme **une carte** : un design, un coût, un effet. Or ta note demande de **ne pas réduire les mythes à des pouvoirs, des coûts ou des ennemis** (dépôt : fiche créatures, §5). Ce n'est pas un défaut, c'est une **vigilance** : ton goût du design « à la carte » et ton respect du mythe tirent dans deux sens. Tes extraits (§8.4 C) montrent une issue : des objets et des rites que les gens **croient** efficaces, et non des « pouvoirs » de jeu.

---

## 8. Tes extraits du *Dictionnaire infernal*, refaits à partir de ta sélection

### 8.1 Ce que contiennent tes extraits, par rapport à tes statuts

| Statut (YAML) | Élément | Dans tes extraits ? |
|---|---|---|
| décidé | Agrippa | ✅ (3 179 mots, le plus long) |
| **envisagé** | **Mélusine** | ✅ (746 mots, versions 1818/1825) : **le seul élément « envisagé » présent** |
| envisagé | Gremory, Furfur, Marbas, Stolas | ❌ (tu as exclu les trois derniers parce que leur contenu est pauvre, d'après la fiche créatures) |
| envisagé | Barbegazi, Ankou, Mourioche, Petit Homme rouge, Gayant, Houeron, Tarasque | ❌ (ils viennent de la carte illustrée) |
| non précisé | Faust, Albert le Grand, Grandier, Merlin, Abel de Larue | ✅ tous les cinq (2 948, 2 228, 2 191, 1 029 et 1 013 mots) |
| intérêt | Chasse sauvage, Loup-garou, Chien noir de Pontgibaud, Fée, Cour infernale | pas sous ces noms, mais **MONSIEUR DE LAFOREST**, **DÉMONS FAMILIERS**, **MÉLYE** et **ADRAMÉLECK** s'en approchent (voir plus bas) |

**Constat :** le reproche est fondé. Les sept figures nommées de ton YAML qui sont dans tes extraits (Agrippa, Mélusine et les cinq « non précisé ») totalisent environ **13 300 mots**, soit à peu près 30 % de tes extraits. Je n'en avais utilisé qu'une.

### 8.2 Mélusine (envisagée) : ce que dit ton extrait

**Ce que dit le texte (extraits, MÉLUSINE, 1818/1825) :**
- Sa mère la condamne à « être moitié serpent tous les samedis, et d'être fée jusqu'au jour du jugement, **à moins qu'elle ne trouvât un chevalier** qui voulût être son mari, et qui ne vît jamais sa forme de serpent ».
- Elle épouse Raimondin, « fils du comte de Forez », et « bâtit le château de Lusignan ».
- Chacun de ses fils naît avec **une marque visible** : un œil rouge et l'autre bleu, « une griffe de lion sur la joue », un seul œil qui voit à vingt et une lieues, « Geoffroi à la grande dent », un troisième œil au milieu du front…
- Ses fils épousent les héritières de Chypre, d'Arménie, du Luxembourg et de Bohême, et l'un devient « roi de Bretagne ».
- Raimondin rompt sa promesse : il fait « une ouverture **avec son épée** » et la voit en serpent. Elle s'envole.
- Depuis, « lorsque Lusignan change de seigneur, ou qu'il doit mourir quelqu'un de sa lignée, elle paraît trois jours avant sur les tours du château ».
- Ses lettres étaient « scellées de son **sceau** […] sur lequel était gravée une sirène, il ne fallait plus songer qu'à obéir aveuglément ».

**Ce que ça rejoint dans ton projet (observations) :**

| Dans l'extrait | Dans ton projet | Ligne |
|---|---|---|
| la délivrance passe par **un chevalier** | goal de Brann : « devenir chevalier » (`interet`) | L4 |
| Forez, Lusignan, Bretagne | lieux français (décidé pour l'arthurien) | L2 |
| roman de colportage | Mélusine figure dans la Bibliothèque bleue (vérifié, 1ʳᵉ partie) | L6 |
| un **sceau gravé** qui commande l'obéissance | « ce qui compte surtout : les **symboles** sur le livre » (U, 7 oct.) | L6, P7 |
| une lignée qui essaime dans **plusieurs royaumes** | royaume principal + royaumes adjacents (envisagé) | L2, L9 |
| une apparition qui **annonce les changements de seigneur** | un monde de rangs et de successions | L3 |
| des fils aux **marques visibles** | des designs reconnaissables (P-D) | §7.2 |

**Abduction 8 :** Mélusine est, dans tes extraits, le point où **quatre de tes lignes se croisent** : la chevalerie (L4), la France de conte (L2), la Bibliothèque bleue (L6) et le monde de rangs (L3). Cela pourrait expliquer pourquoi elle est la seule figure de tes extraits à être passée en « envisagé ».

**Test :** qu'est-ce qui t'attire dans Mélusine : la **fée-serpent** (le design), le **pacte rompu** (le récit) ou la **fondatrice de lignée** (le monde) ?

### 8.3 Les cinq figures « non précisé » et Agrippa

| Figure (mots) | Ce que dit ton extrait (cité) | Ce que ça rejoint |
|---|---|---|
| **MERLIN** (1 029) | « Merlin **n'est pas né en Angleterre** […] ; il reçut le jour en **Basse-Bretagne, dans l'île de Sein** ». Il se retire « dans une forêt profonde de la Bretagne ». Il donne « à l'un des chevaliers errants, **qui firent la gloire de la France**, une épée enchantée ». Il fabrique une chambre « où ne pouvaient entrer que les braves amans et les amantes fidèles », une couronne « qui se troublait sur la tête d'une coquette », une épée « qui jetait des étincelles dans les mains des guerriers intrépides ». Il vit encore, enfermé par Viviane, « dans une forêt des environs du Finistère nommée **Brocéliande** » ; Gauvain « l'entendit, mais ne put le voir ». | **Déduction 13 :** ton extrait propose déjà **une matière arthurienne francisée** : Merlin y est breton, Brocéliande y est en Bretagne, et les chevaliers errants font « la gloire de la France ». C'est exactement la logique de ta décision « lieux arthuriens français uniquement » et de **Brocéliande** (décidée). Je ne sais pas si l'extrait a précédé la décision : c'est une **convergence**, pas une preuve de cause. *Remarque (mémoire) : on situe aujourd'hui Brocéliande à Paimpont, en Ille-et-Vilaine, pas dans le Finistère.* Ta décision « pas de nom direct comme Merlin » laisse intacts les **objets qui testent la vertu**, qui ne dépendent pas du nom. |
| **FAUST** (2 948) | « un **barbet noir** qui formait des cercles rapides » ; Méphistophélès apparaît « sous le costume d'un jeune seigneur, vêtu avec la dernière élégance » ; pacte « **signé de son sang** […] s'obligeait à le servir **vingt-quatre ans** ». | un pacte **à durée fixe** (une règle avec une échéance) ; le chien noir (voir §8.4 A) |
| **ALBERT LE GRAND** (2 228) | « il fit un **automate** qui lui servait d'oracle […]. Il fut trente ans à le composer, avec des **métaux bien choisis**, et sous l'inspection des astres. C'est ce qu'on appelle l'**androïde** d'Albert-le-Grand » ; on prête « à Virgile, au pape Sylvestre II et à Roger Bacon, de pareilles androïdes ». | **technologie magique hors plafond** (décidé) et P4 : ton extrait contient une **machine faite par la magie et la science ensemble**, ce que ta zone *BioShock* suppose (déduction 8, L5) |
| **GRANDIER** (2 191) | Loudun, couvent des Ursulines (1626) : des religieuses se disent possédées ; trois ennemis du curé Grandier (Mignon, Barot, Trinquant) l'accusent de les avoir ensorcelées ; « l'évêque de Poitiers le condamna **sans l'entendre** ». Le mot « exorcisme » et ses dérivés reviennent 10 fois dans l'article. | **le gimmick « Exorciste »**, qui n'a **aucune œuvre attachée** dans ton YAML : c'est dans ton extrait la matière d'exorcisme la plus riche. Et P4 : l'accusation de sorcellerie y est **une arme politique** entre notables, pas seulement un malentendu technique. |
| **ABEL DE LARUE** (1 013) | Coulommiers, 1582 : un savetier accusé d'avoir « noué l'aiguillette » ; « un **barbet noir** lui avait apparu » et le conduit « dans une chambre du couvent appelée **la Librairie** » ; puis « un **grimoire** s'était présenté à lui ». | le livre de sorts (U : ce qui compte, ce sont les symboles) ; le chien noir |
| **AGRIPPA** (décidé, 3 179) | « il menait en sa compagnie un diable sous la figure d'un **chien noir** » ; le collier « garni de clous qui formaient des inscriptions nécromantiques » ; son disciple Wier dit qu'il « avait constamment **deux chiens dans son étude** », et qu'au XVᵉ siècle « montrer de l'attachement pour un animal » suffisait à passer pour sorcier. | déjà dans L6 et L8 |

### 8.4 Ce qui revient d'un article à l'autre (inductions sur ta sélection)

**A. Le chien noir, compagnon du savant**
- **Observé :** 3 des 6 figures savantes de ton YAML ont un **chien noir démoniaque** dans tes extraits : Agrippa, Faust, Abel de Larue. S'y ajoutent DÉMONS FAMILIERS, où un démon rend visite à un baron dans sa tour d'étude et « s'entretenait avec lui sur divers objets, sans jamais lui faire aucun mal », et le **Chien noir de Pontgibaud**, en `interet` sur ta carte des créatures.
- **Induction 6 :** dans ta sélection, le **familier** est le lien récurrent entre le savoir et l'enfer.
- **Lien :** Harley = « le savoir et le secret » (L8, abduction 5). Simple possibilité, voir P12.

**B. Les naissances et les lignées surnaturelles**
- **Observé :**
  - MERLIN : « fils d'un démon incube et d'une jeune druidesse, fille d'un roi des Bretons ».
  - APOLLONIUS : conçu sans père ; « un des plus hauts salamandres fut son père, selon les cabalistes ».
  - MÉROVÉE : sa mère « fut surprise par un monstre qui sortit des flots » ; mais « Sauval croit que cette fable fut **inventée par Mérovée lui-même pour imprimer du respect** dans l'esprit des siens ».
  - MÉLUSINE : fondatrice d'une lignée de rois.
  - GRANGE DU DIABLE (2ᵉ partie) : une femme enfante un monstre ; « sa race est éteinte sur la terre ».
  - AYMAR : son talent est « attribué à l'époque précise de sa naissance », car « son frère […] ne pouvait rien faire avec la baguette ».
- **Induction 7 :** six articles de ta sélection traitent d'une **origine surnaturelle**.
- **Prudence :** tu as **retiré** « Pandragon » du nom de Brann (décidé, 9 oct.). Cela suggère que tu ne veux pas d'un Brann « héritier caché ». Je ne propose donc **pas** d'origine secrète pour Brann. L'article MÉROVÉE offre un autre angle : **la lignée surnaturelle comme fiction politique**, inventée pour légitimer un pouvoir. Cela rejoint P3 (« Chevalier », métier interdit au roturier) : les nobles justifient leur rang par des origines merveilleuses ; Brann, sans nom, n'en a aucune. Voir P11.

**C. Des objets et des rites à conditions, porteurs d'inscriptions**
- **Observé :**
  - BAGUETTE MAGIQUE : elle doit être « de coudrier, de la pousse de l'année », coupée « le premier mercredi de la lune, entre onze heures et minuit » ; on écrit dessus « au gros bout le mot *Agla*, au milieu *On*, et *Tetragrammaton* au petit bout ».
  - POULE NOIRE : « à minuit, dans un carrefour », il faut « ne se point retourner ».
  - MAIN DE GLOIRE : une recette longue, puis « ceux qui y sont demeurent immobiles ».
  - SUREAU : on frappe l'habit avec un bâton de sureau, et « tous les coups retomberont sur l'échine du sorcier coupable ».
  - Les objets de Merlin qui **testent la vertu** (chambre, couronne, épée).
  - MÉLYE : la méchante fée possède un livre « qui portait le **nom de Médée** ».
  - MÉLUSINE : le sceau gravé d'une sirène.
  - AGRIPPA : le collier à inscriptions.
- **Induction 8 :** dans tes extraits, le pouvoir est très souvent **attaché à une inscription ou à une condition précise** (heure, lieu, geste interdit). Quatre fois au moins, c'est un **signe écrit ou gravé** (baguette, livre de Mélye, sceau, collier). Cela soutient ta préférence pour « les symboles sur le livre » (U).
- **Ce que tu as déjà confirmé :** l'intérêt pour les « pratiques et objets occultes » (fiche créatures, §4.1). Ce qui est nouveau ici, c'est le **mécanisme commun** : la condition et l'inscription.
- **Lien avec T9 :** ce sont des rites **auxquels les gens croient**, pas des « pouvoirs » de jeu. C'est une façon d'avoir des règles sans réduire le mythe à une carte.

**D. L'enfer administré : L3 tient sur ta propre sélection**
- **Observé :**
  - ABIGOR : « Grand-duc aux enfers. Il se montre sous la figure d'un **beau cavalier, portant la lance, l'étendard ou le sceptre** » ; il connaît « les secrets de la guerre » et « enseigne aux chefs les moyens de se faire aimer du soldat » ; « soixante légions ».
  - ADRAMÉLECK : « grand chancelier des enfers », président du haut conseil.
  - LÉONARD : « grand maître des sabbats, chef des démons subalternes, **inspecteur général** de la sorcellerie ».
  - AGUERRE : Pierre d'Aguerre, « maître des cérémonies du sabbat », range l'assemblée avec un bâton doré « **comme un mestre-de-camp** ».
  - FAVIER : un démon arrive « chargé d'un grand in-folio » où il a écrit « en manière d'histoire suivie » les péchés d'un mourant : un **archiviste**.
  - DÉMONOCRATIE (« gouvernement des démons ») ; PANDOEMONIUM (« capitale de l'empire infernal »).
- **Mise à jour de L3 :** dans la 1ʳᵉ partie, je fondais la déduction 4 sur COUR INFERNALE, qui **n'est pas** dans tes extraits. Elle tient maintenant **sur ta propre sélection** : rangs (grand-duc), offices (chancelier, inspecteur général, maître des cérémonies, archiviste), grades militaires (mestre-de-camp), capitale. P2 (démons ambassadeurs) reste fondé, lui, sur COUR INFERNALE, donc **hors de tes extraits**. Je le signale.
- **Abigor et L4 :** ta sélection contient un **démon-chevalier** (« beau cavalier », lance, étendard) qui enseigne le commandement. Avec LÉONARD (le bouc à trois cornes), c'est un des rares démons de tes extraits décrits **par leur apparence**, ce qui correspond à ta façon de choisir les démons (par le design). C'est le seul qui ait l'allure d'un chevalier.

**E. La France, région par région**
- **Observé :** Bretagne (Merlin, île de Sein, Brocéliande ; « en Bretagne », POULE NOIRE), **Champagne** (GRANGE DU DIABLE, Sézanne), Brie (Coulommiers et Meaux, ABEL DE LARUE), Poitou (Loudun et Poitiers, GRANDIER ; Lusignan, MÉLUSINE), Forez (MÉLUSINE), Dauphiné et Lyon (AYMAR), **Fontainebleau** (MONSIEUR DE LAFOREST), pays de Labour (AGUERRE), **Languedoc** (ALBIGEOIS), Paris.
- **Mise à jour de L2 :** ta sélection est **ancrée région par région**, comme ta carte des créatures. L2 (la France comme carte cachée) tient aussi sur tes extraits.

**Trois liens précis avec des zones de ton YAML :**

1. **Région montagnarde enneigée (décidée) et Barbegazi (envisagé).**
   - MONTAGNARDS : « Démons qui font leur séjour dans les **mines sous les montagnes**, et tourmentent les mineurs. Ils ont **trois pieds de haut**, un visage horrible, un air de vieillesse, une camisole et un **tablier de cuir**, comme les ouvriers qui travaillent aux mines […]. Ces démons n'étaient point malfaisants, et **entendaient la plaisanterie** ; mais une insulte leur était sensible. »
   - **Abduction 9 :** c'est, dans ta propre source, l'équivalent français des **nains mineurs de Warcraft**. De mémoire, Brann Barbe-de-Bronze est un nain de Forgefer, une cité creusée dans une montagne enneigée (Dun Morogh). Ton extrait offre donc un pont entre ton goût Warcraft et ta matière française, pour une région que tu as déjà décidée. Voir P9.
   - *Attention :* tu as écarté le mot « montagnard » **pour décrire tes images de paysage** (YAML). Ça ne concerne pas cet article, mais le nom serait à éviter tel quel.
2. **Forêt de conte (décidée), Chasse sauvage et Loup-garou (intérêt).**
   - MONSIEUR DE LAFOREST : « le fantôme, plus connu sous le titre de *grand Veneur* de la forêt de Fontainebleau » ; un enfant trouvé « vêtu d'une peau de loup, et courant comme un petit **loup-garou** » dit que « monsieur de Laforêt lui avait donné sa peau ».
   - La fiche créatures signalait l'article VENEUR dans la base, mais pas celui-ci : **ta propre sélection contient déjà la figure française de la chasse fantôme**, liée au loup-garou. *The Witchwood* (forêt corrompue, royaume de loups-garous, vérifié) et *The Witcher 3* (par lequel tu as découvert la Chasse sauvage, U) vont dans le même sens. Trois de tes sources se rencontrent dans **la forêt hantée** : Warcraft, *Witcher 3* et ta sélection du *Dictionnaire infernal*.
3. **Région désertique « inspirée du Languedoc » (non précisé), ancien nom de brouillon « Terre dévastée » (origine non confirmée).**
   - ALBIGEOIS, ton seul article sur le Languedoc : la croisade, « l'horrible sac de Béziers », « Tuez-les tous, Dieu connaîtra ceux qui sont à lui », « soixante mille habitants » (chiffre du dictionnaire, non vérifié).
   - ⚠️ **Corrigé au §11.4 :** « Terre dévastée » est une proposition d'une IA, pas ton nom. Les hypothèses (a)-(c) ci-dessous sont caduques.
   - ~~Trois origines possibles du nom, que je ne peux pas départager :~~
     - (a) cet article (le Languedoc **dévasté** par la croisade) ;
     - (b) **la Terre Déserte**, lieu arthurien que tu envisages (royaume de Claudas dans le *Lancelot* ; dépôt : BRIEF A2) ;
     - (c) la « terre gaste » du Graal (mémoire).
   - Seul toi peux le dire. Si c'est (a), la région n'est pas seulement désertique : elle porte **la mémoire d'une guerre de religion**, ce qui rejoindrait P6 (le royaume suit l'histoire). *Prudence :* ALBIGEOIS mentionne aussi l'**Inquisition**. *Radiant* en a une (dépôt : fiche Radiant), donc cette piste pourrait te rapprocher de ce que tu veux éviter.

**F. Le conte et la chevalerie dans tes extraits (L6 et L5)**
- **GRANGE DU DIABLE** est ton **2ᵉ article le plus long** (2 982 mots) et le seul étiqueté « conte populaire ». Un fermier **champenois** se voit proposer par le diable de finir sa grange « avant le chant du coq » contre « l'enfant que ta femme porte dans son sein ». La Champagne est la région de Troyes, berceau de la Bibliothèque bleue (vérifié, 1ʳᵉ partie, pour Troyes). **L6 se renforce :** dans ta sélection, conte, pacte et diable sont **dans le même texte**.
- **MÉLYE** (413 mots), tiré des romans de chevalerie (Amadis, la fée Urgande) :
  - les fées sont inégales en puissance ;
  - Esplandian a « une **épée enchantée qui devait rompre tous les charmes** » ;
  - « bien qu'immortelles de leur nature, les fées n'étaient **pas à l'épreuve d'un bon coup d'épée** […] pourvu qu'elle fût violente ».
- **Lien avec L5 :** tu as plafonné les armes à feu à 1860 pour **garder l'épée viable** (déduction 6). Ta propre sélection contient la règle de conte correspondante : **l'épée bat l'enchantement**. C'est une convergence, pas une preuve que tu y as pensé.
- **Le pôle nordique :** SURTUR (fin du monde par le feu, le « pont Bifsort », c'est-à-dire Bifröst) et MAGIE ISLANDAISE (esprits aériens, corbeaux consultés par les rois). Ils rejoignent **Freljord** et **Tibétains-Yéti** de ton brouillon, et les Frozn d'*Urban Rivals* (« nordique + Yéti + technologie », U). *Erreur de la source :* le dictionnaire attribue Surtur « aux Celtes » ; c'est une figure de la mythologie **nordique** (mémoire, mais très sûr).

### 8.5 Récapitulatif : ce que tes extraits ajoutent aux lignes de la 1ʳᵉ partie

| Ligne | Avant | Avec tes extraits |
|---|---|---|
| **L2** France cachée | carte des créatures + lieux arthuriens | + 10 régions dans tes extraits ; **Merlin breton et Brocéliande en Bretagne dans ta propre source** (déduction 13) |
| **L3** rangs | COUR INFERNALE (hors extraits) | **tient sur tes extraits** : Abigor, Adraméleck, Léonard, Aguerre, Favier |
| **L4** chevalier | 6 signaux | + Mélusine (la délivrance par un chevalier), Merlin (chevaliers errants « gloire de la France »), Mélye, **Abigor (démon-chevalier)** ; *Le Grand Tournoi* (à confirmer) |
| **L5** épée viable | plafond 1860 | + MÉLYE : l'épée bat l'enchantement |
| **L6** conte / Bibliothèque bleue | sources web | + GRANGE DU DIABLE (conte champenois, 2ᵉ article le plus long), MÉLUSINE, MÉLYE |
| **L8** Harley = savoir | Agrippa, Limbo de Magik | + le chien noir des savants (Agrippa, Faust, Abel), DÉMONS FAMILIERS |
| **P4** accusations de sorcellerie | Agrippa + inégalité technique | + **androïde d'Albert le Grand** (magie-technique), **Grandier** (l'accusation comme arme politique) |
| **P7** objets à symboles | Bibliothèque bleue | + baguette à inscriptions, sceau de Mélusine, livre « Médée » de Mélye |
| **T1** mafia ↔ 1860 | moyenne | **faible** si la source est Gadgetzan (§7.4) |
| **§4 « non expliqué »** | *Urban Rivals* | expliqué par **P-D** (mosaïque de jeu de cartes) |

---

## 9. Nouvelles possibilités (propositions de l'IA, non décidées)

### P9. Un peuple des mines pour la région enneigée
- **D'où :** MONTAGNARDS (tes extraits) + Région montagnarde enneigée (décidée) + Barbegazi (envisagé) + ton goût Warcraft (abduction 9).
- **Ce que ça produit :** une population de petits mineurs, vieux d'apparence, en tablier de cuir, qui « entendent la plaisanterie » mais ne pardonnent pas l'insulte. Un caractère tout fait, **de source française**, qui comble l'envie « nains de Warcraft » sans les copier.
- **Risque :** ressembler trop aux nains de fantasy classique. L'apparence démoniaque (« visage horrible ») et l'insulte vengée les distinguent.
- **Test :** quand tu as mis MONTAGNARDS dans tes extraits, pensais-tu aux nains ?

### P10. La mafia selon Gadgetzan
- ⚠️ **Mis à jour au §11.2 :** tu avais déjà fait le rapprochement, et tu gardes seulement la structure sociale, sous 1914.
- **D'où :** §7.4.
- **Ce que ça produit :** des familles criminelles qui tiennent une cité-port, dont une famille de **sorciers**. La zone « mafieux » existe **sans armes modernes**, la magie tient le rôle de la mitraillette.
- **Risque :** que la zone ressemble trop à Gadgetzan. Le costume années 20-30 (que tu gardes en `interet`) la distingue.
- **Test :** « mafieux années 20-30 » et « Gadgetzan » sont-ils la même zone ?

### P11. La lignée merveilleuse comme fiction de pouvoir
- **D'où :** MÉROVÉE (« fable inventée […] pour imprimer du respect »), MÉLUSINE (fondatrice de lignées), P3, et le retrait de « Pandragon ».
- **Ce que ça produit :** les grandes familles du royaume revendiquent une origine surnaturelle (une fée, un monstre marin) pour fonder leur rang. Brann, **sans nom de famille**, n'a rien de tel. Son goal de chevalier heurte donc aussi **un récit officiel**, pas seulement une règle. Cela évite le « héros élu ».
- **Risque :** un thème politique lourd pour un début de shōnen. Il peut rester **en fond**, comme tu le veux pour l'au-delà.
- **Test :** cela te plaît-il que les lignées « magiques » soient peut-être fausses ?

### P12. Le familier du savant
- **D'où :** induction 6 (chien noir : Agrippa, Faust, Abel ; DÉMONS FAMILIERS ; Chien noir de Pontgibaud).
- **Ce que ça produit :** un compagnon animal, éventuellement démoniaque, attaché à une figure de savoir. C'est aussi un **design reconnaissable** (P-D) et un **objet-symbole** possible (le collier à inscriptions d'Agrippa).
- **Risque :** cliché du familier. La version de tes extraits a un **coût social** : au XVᵉ siècle, aimer un animal suffisait à passer pour sorcier (AGRIPPA). C'est ce qui la rend moins banale.
- **Test :** aucun pour l'instant. À rapprocher de Harley seulement si tu le souhaites ; je ne l'affirme pas.

### P13. Des objets qui jugent leur porteur
- **D'où :** MERLIN (chambre, couronne, épée qui étincelle pour les intrépides), MÉLYE (épée qui rompt les charmes), induction 8.
- **Ce que ça produit :** des objets du monde qui **réagissent à une qualité morale** (courage, fidélité), avec des inscriptions. Ce sont des règles visibles, sans système de pouvoirs à expliquer. Ils sont compatibles avec le goal « devenir chevalier » : l'objet peut reconnaître ce que le rang refuse.
- **Risque :** l'« épée qui choisit l'élu » est un cliché arthurien, et la zone *Radiant* est proche (T3). Il faut garder la **condition morale** et laisser tomber l'idée d'élu.
- **Test :** préfères-tu un objet qui **juge** (Merlin) ou un objet qui **annule** la magie (Mélye) ?

---

## 10. Limites de cet addendum

- **Vérifié aujourd'hui (web) :** les dates et thèmes de *Mean Streets of Gadgetzan*, *The Witchwood* et *Le Grand Tournoi* (hearthstone.wiki.gg et wiki Fandom, page « Expansion »).
- **De mémoire (non vérifié) :** les classes de *Hearthstone* ; Dalaran ; les nains de Forgefer et Dun Morogh ; les régions-factions de *Legends of Runeterra* ; le ton humoristique de *Hearthstone* ; la localisation de Brocéliande à Paimpont ; Surtur nordique ; la « terre gaste ».
- **Inconnu :** quelles extensions de *Hearthstone* tu as réellement jouées, et pendant combien de temps. Les liens avec *Gadgetzan* (cité dans ton brouillon) et avec la forêt (tes mots) sont solides ; les autres dépendent de ta réponse.
- **Ordre chronologique inconnu :** je ne sais pas si tes extraits ont été faits avant ou après tes décisions (lieux français, Brocéliande, plafond 1860). Les liens du §8 sont des **convergences**, pas des causes.
- **Lu en entier :** MÉLUSINE, MERLIN, MÉLYE, ABIGOR, ALBIGEOIS, MÉROVÉE, MONTAGNARDS, SURTUR, MAGIE ISLANDAISE, LÉONARD, DÉMONS FAMILIERS, SUREAU, PANDOEMONIUM, DÉMONOCRATIE, BAGUETTE MAGIQUE, MONSIEUR DE LAFOREST, FAVIER, AGUERRE. **Lu en partie** (début ou passages ciblés) : FAUST, ALBERT LE GRAND, GRANDIER, ABEL DE LARUE, AYMAR, MAIN DE GLOIRE, POULE NOIRE, GRANGE DU DIABLE, APOLLONIUS, MONSTRES, ALCHIMIE, DÉMONIAQUES. **Non lus** cette fois : SABBAT, PACTE, SORCIERS, MAGICIENS, ÂME, MALÉFICES et une quarantaine d'articles courts.
- **Rien n'a été écrit dans le YAML.** Les statuts ne changent pas.


---

## 11. Tes réponses du 12 octobre et ce qu'elles changent

### 11.1 Hearthstone : huit ans d'extensions, pas un simple premier contact

**Ce que tu as dit (U) :** tu as joué la Ligue des explorateurs, Gadgetzan, les Dieux très anciens, « en vrai un peu tous », et tu t'es arrêté·e **après l'extension western**.

**Ce que ça donne (calendrier vérifié, hearthstone.wiki.gg) :**
- de la Ligue des explorateurs (novembre 2015) à l'extension western (« SitB », novembre 2023), soit **environ huit ans** ;
- 23 extensions principales dans cet intervalle, d'après mon comptage sur ce calendrier, plus des aventures ;
- de **14 ans à environ 22 ans** si l'on suit ta chronologie. Cela recouvre *HxH*, *AoT*, *GoT*, ton projet de jeu à 16 ans et les débuts d'Edenia.

**Conséquence pour P-D (la mosaïque de factions) :** l'abduction 6 se renforce nettement. Il ne s'agit plus d'un jeu découvert à 14 ans, mais d'**une habitude de huit ans** : recevoir environ trois mondes à thème par an, chacun avec ses designs. Ta liste de zones ressemble à ce rythme : des thèmes ajoutés les uns après les autres, sans souci d'unité historique.

**Des titres qui recoupent tes zones et tes intérêts.** Les titres sont vérifiés dans le calendrier ; le contenu des extensions est **de mémoire**.

| Extension (date) | Thème (mémoire, sauf mention) | Chez toi |
|---|---|---|
| *Les Murmures des Dieux très anciens* (avril 2016) | horreur lovecraftienne | occultisme ; enfer et démons de *Dorohedoro* (intérêt) |
| *Mean Streets of Gadgetzan* (déc. 2016) | familles criminelles (vérifié) | zone mafieuse (§11.2) |
| *The Witchwood* (avril 2018) | forêt corrompue, loups-garous (vérifié) | Forêt de conte (décidée), Loup-garou (intérêt) |
| *Scholomance Academy* (août 2020) | école de magie | école de Brocéliande, Academy Ekko : le modèle « académie » de T6 |
| *Darkmoon Faire* (nov. 2020) | fête foraine | foires (intérêt) |
| *Murder at Castle Nathria* (août 2022) | cour noble gothique | un monde de rangs (L3) |
| extension western (nov. 2023) | western | **zone western (décidée)** |

**Lecture prudente :** ces recoupements sont des **compatibilités**. Le western, l'école ou la foire ont d'autres sources chez toi (*BioShock*, *Harry Potter*, les brouillons). Ce que Hearthstone ajoute de sûr, c'est **la forme** (une mosaïque de thèmes successifs), pas chaque contenu.

**Mise à jour du §7.3 :** les liens avec *The Witchwood* passent de « à confirmer » à **probables**, puisque tu as joué « un peu tous ». *Le Grand Tournoi* était déjà sorti à ton arrivée ; le lien reste faible.

### 11.2 La zone mafieuse : la structure sociale seulement, sous 1914

**Ce que tu as dit (U) :**
- tu avais déjà fait le rapprochement avec Gadgetzan ;
- tu gardes **seulement la structure sociale** ;
- tu avais en tête la **Chicago Spirit** de SCP, **l'occultisme des années 1890-1910** et ***BioShock* 1** ;
- tu ne veux **pas dépasser 1914**.

**Vérifié (SCP Wiki, page « Groups of Interest ») :** la Chicago Spirit est présentée comme la plus grande organisation criminelle « anormale » de l'hémisphère occidental au début du XXᵉ siècle. Elle recrute des individus aux **capacités anormales** et fabrique ou exploite des **artefacts anormaux**. Son influence s'étend notamment à la **Nouvelle-Orléans** et à une **cité-État** extradimensionnelle, Three Portlands. Elle prospère ensuite pendant la Prohibition. Un wiki secondaire (NamuWiki) date sa fondation de **1893** ; non vérifié sur le SCP Wiki.

**Ce que ça change :**
- **T1 est résolue par ta décision**, plus par mon hypothèse : structure sociale gardée, armement d'après 1914 exclu.
- **Convergence :** tes deux sources de mafia, la Chicago Spirit et Gadgetzan, ont le même trait. C'est une **pègre qui se sert de la magie** : des recrues aux capacités anormales d'un côté, la famille de sorciers du Kabal de l'autre. Elles vont donc dans le même sens que P10.
- **Coïncidence notable :** la Chicago Spirit est liée à la Nouvelle-Orléans. Ta zone « Nouvelle-Orléans / Caraïbes » est inspirée de Bilgewater.
- ***BioShock* 1** se passe en 1960, d'après ma mémoire. Tu n'en gardes donc que ce qui tient sous 1914 : l'ambiance et l'organisation, pas la technologie.

**Abduction 10 : la date de 1914 ferme aussi l'époque de ton occultisme.**
- **Observé :** ton occultisme de référence date des **années 1890-1910** (U). *BioShock Infinite* se passe en **1912** (vérifié). Ton plafond envisagé est **1914**.
- **De mémoire :** la Belle Époque se termine conventionnellement en 1914. C'est aussi la grande période des sociétés occultes françaises, anglaises et allemandes : l'Ordre kabbalistique de la Rose-Croix de Stanislas de Guaita et Papus en France (1888), la Golden Dawn à Londres (1888), l'Ordo Templi Orientis dans l'espace germanique (années 1900).
- **Hypothèse :** le plafond de 1914 n'est pas seulement technique. Il **referme la période historique de l'occultisme qui t'intéresse**, et cette période concerne justement les trois pays de ta règle (§11.4).
- **Test :** si tu imagines Edenia en 1925, est-ce que c'est l'arme qui te gêne, ou l'ambiance ?

### 11.3 Les noms : Brann, et l'ancienne Gwen

**Ce que tu as dit (U) :**
- **Bran** vient de *GoT*, puis **Brann** de Hearthstone.
- Harley devait d'abord s'appeler **Gwen**, d'après Gwen Tennyson. « Bran » était un rapprochement avec ***Ben 10***.
- Tu as ensuite choisi **Harley**, qui rapproche d'**Hermione**. Tu voulais une personnalité plus proche de **Shallan**, de **Maka Albarn**, puis, après réflexion, de **Luna Lovegood**, en raison de sa popularité.
- « Harley Delphine » est un **nom provisoire, pas encore vraiment décidé**.

**Ce que ça confirme et ce que ça corrige :**
- **Brann :** mon hypothèse Hearthstone est **confirmée, mais en deuxième couche** : *GoT* d'abord, Hearthstone ensuite. Le nom a donc trois couches : Ben, Bran, Brann.
- **Le duo d'origine était un duo à la *Ben 10*.** De mémoire, Ben et Gwen Tennyson sont des cousins : le héros impulsif, et la fille intelligente qui devient magicienne dans les séries suivantes. Si c'est exact, cela soutient l'induction 4 (Harley = le savoir) et l'abduction 5 (Harley = le contact avec l'occulte), **dès l'origine du personnage**.
- **Luna choisie « suite à sa popularité » :** c'est la même logique que celle de L8. Tu composes avec **ce que les lecteurs aiment** : Killua est 1ᵉʳ des sondages de *HxH*, Tattletale 1ʳᵉ des classements de *Worm*. Luna figure dans les personnages les plus appréciés de *Harry Potter* selon la fiche de ton dépôt (sondages Bloomsbury/Guardian 2011, etc.).
- **Un déplacement du personnage (hypothèse) :** de mémoire, Hermione incarne le savoir scolaire et la règle. Luna est celle qui croit à des créatures dont les autres se moquent. Maka est élève d'une académie de combat. Harley semble glisser du **savoir officiel** vers un **savoir marginal**, celui qu'on prend pour de la superstition. C'est exactement la matière du *Dictionnaire infernal*, où Agrippa passe pour sorcier parce qu'il est « trop instruit ».
- **Test :** Harley sait-elle des choses **vraies que personne ne croit** (Luna), ou des choses **que tout le monde apprend mieux qu'elle** (Hermione) ?

**À reporter dans le YAML si tu le veux :**
- Maka Albarn et Luna Lovegood ne figurent pas dans les inspirations de Harley ;
- le nom « Harley Delphine » y apparaît sans mention de son caractère provisoire.

Je ne modifie pas le YAML moi-même.

### 11.4 « Terre dévastée », et ta règle France / Angleterre / Allemagne

**Ce que tu as dit (U) :**
- « Terre dévastée » est **une proposition d'une IA**. Le YAML parle à tort d'un « ancien nom de brouillon » : à corriger.
- Tu pensais à une zone inspirée des **Plaines Brisées de Roshar** et du **western**.
- Tu l'as reliée au Languedoc pour garder **un héritage francophone entre les zones**.
- Toutes les zones et tous les lieux envisagés ou choisis ont un rapport avec la France, ou à la rigueur avec l'Angleterre et l'Allemagne. Ce sont les **pays principaux de l'occultisme**, et ils échangeaient beaucoup entre eux.

**Ce que ça annule :** mes hypothèses (a), (b) et (c) sur l'origine du nom (§8.4 E3). La piste ALBIGEOIS n'explique pas le nom. Elle reste seulement une **matière possible** pour la région.

**Déduction 14 : ta règle tient sur toutes tes figures du *Dictionnaire infernal*.** D'après tes extraits :

| Figure (statut) | Origine selon ton extrait | Pays |
|---|---|---|
| Agrippa (décidé) | « naquit à Cologne en 1486 » | Allemagne |
| Albert le Grand (non précisé) | « né dans la Souabe » ; « mourut à Cologne » | Allemagne |
| Faust (non précisé) | « né à Weymar (Weimar) » ou « à Gundling, dans le Wurtemberg » | Allemagne |
| Merlin (non précisé) | « en Basse-Bretagne, dans l'île de Sein » (Angleterre selon la tradition courante, que l'extrait conteste) | France / Angleterre |
| Grandier (non précisé) | Loudun | France |
| Abel de Larue (non précisé) | Coulommiers | France |
| Mélusine (envisagée) | Lusignan, Forez | France |

**7 sur 7.** La matière arthurienne (anglo-française) et le *Dictionnaire infernal* (français) entrent aussi dans la règle.

**Ce que la règle explique dans tes zones (observations) :**
- « Nouvelle-Orléans / Caraïbes » et le **marais type bayou** : de mémoire, la Louisiane et les Antilles sont des terres d'héritage **francophone**. Ces zones respectent donc la règle, même si leur modèle (Bilgewater) vient de Runeterra.
- **Brocéliande** : France.
- **Western** : rattaché au Languedoc (ta réponse).
- **Mafia de Chicago** : structure sociale seulement (§11.2).
- Les zones du brouillon que tu **n'as pas validées** (Ionia, Freljord, Tibétains-Yéti) sont justement celles qui **sortent de la règle**. C'est peut-être une coïncidence : elles ont été laissées de côté pour une question de vocabulaire, pas rejetées.
- **Exceptions qui restent :** les personnages d'inspiration asiatique (envisagé) et les objets bouddhiques (intérêt). La règle porte sur les **lieux et l'héritage des zones** ; elle ne dit rien des personnages.

**Mise à jour de L2 :** ce n'était pas une « carte cachée » à deviner. **C'est une règle que tu appliques consciemment**, avec une justification historique (les échanges occultistes entre ces trois pays). L2 passe d'**abduction** à **règle énoncée par toi**. Cela rejoint aussi P-A (forme japonaise, matière française), qu'il faudrait élargir : **matière française, à la rigueur anglaise et allemande**.

**Le modèle des Plaines Brisées :** ton dépôt classe déjà les Plaines Brisées dans le type **P, « zone de guerre commune »** (plusieurs pouvoirs se disputent un même terrain) (`modeles…`, tableau des types). Je n'ajoute rien sur Roshar au-delà de ce que ton dépôt contient, pour respecter ta limite de lecture.

### P14. Un Languedoc « brisé » et un western francophone (proposition de l'IA, non décidée)
- **D'où :** ta réponse (Plaines Brisées + western + héritage francophone).
- **Ce que ça produit (de mémoire, à vérifier) :**
  - Les **Grands Causses** et leurs **gorges** (Tarn, Jonte) sont des plateaux calcaires coupés de canyons profonds. C'est un équivalent réel et français de « plateaux séparés par des gouffres ». Le Gévaudan (actuelle Lozère) faisait partie de la province de Languedoc, et c'est le pays de la **Bête du Gévaudan**. Je ne sais pas si elle figure sur ta carte des créatures ; elle n'est pas dans ton YAML.
  - Les **gardians de Camargue**, gardiens de chevaux et de taureaux, sont souvent appelés les « cow-boys » français. Une partie de la Camargue (la Petite Camargue) est dans le Gard, donc en Languedoc. Cela donne au western **un héritage francophone** au lieu d'un simple décor américain.
- **Risque :** trop de géographie réelle pour un monde de fantasy. Comme pour tes autres zones, il s'agirait d'un **héritage**, pas d'une carte.
- **Test :** dans ta zone, le western est-il **un paysage** (plateaux, canyons) ou **un mode de vie** (élevage, cavaliers, frontière) ? Les Causses répondent au premier, la Camargue au second.

### 11.5 Vérifications de cette section
- **Vérifié aujourd'hui (web) :** le calendrier des extensions de Hearthstone (hearthstone.wiki.gg) ; la Chicago Spirit (SCP Wiki).
- **Lu dans tes extraits aujourd'hui :** les lieux de naissance d'Agrippa, d'Albert le Grand et de Faust.
- **Lu dans ton dépôt :** les Plaines Brisées en type P (`modeles…`) ; la popularité de Luna (fiche *Harry Potter*).
- **De mémoire, non vérifié :**
  - le contenu des extensions autres que *Gadgetzan* et *The Witchwood* ;
  - la date de *BioShock* 1 ;
  - les sociétés occultes de 1888-1900 ;
  - Ben et Gwen Tennyson ; Hermione, Luna, Maka ;
  - la Louisiane et les Antilles francophones ;
  - les Causses, le Gévaudan et la Camargue.
- **Rien n'a été écrit dans le YAML.** Trois corrections y seraient utiles, si tu le décides :
  - « Terre dévastée » : proposition d'une IA, pas un nom de brouillon ;
  - Harley Delphine : nom provisoire ;
  - Maka Albarn et Luna Lovegood comme inspirations de personnalité.

### 11.6 Réponses suivantes (12 oct.)
- **Zone western = un paysage** (U). Tu n'as pas encore pensé au mode de vie. Dans P14, la piste des **Causses et des gorges** est donc la bonne ; la Camargue (mode de vie) est mise de côté pour l'instant. Lien avec ton YAML : tu veux un **vocabulaire de paysage plus précis** avant d'ajouter des zones (`a_preciser`). Les Causses en fournissent un (de mémoire, à vérifier) : *causse* (plateau calcaire), *gorge*, *corniche*, *aven* (gouffre naturel) et *chaos rocheux*, comme le chaos de Montpellier-le-Vieux.
- **Harley** : tu ne sais pas répondre à la question Luna/Hermione. Tu connais peu Luna en dehors de sa personnalité, et Harley est un personnage que tu as **du mal à définir** (U). Aucune conclusion n'est tirée ; voir la réponse dans la conversation pour une méthode possible.
