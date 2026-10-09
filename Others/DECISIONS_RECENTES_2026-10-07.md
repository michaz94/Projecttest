# Décisions récentes et précisions (6-7 octobre 2026)

## Statut de ce document

- **En cas de contradiction avec un ancien MD du dépôt, ce document l'emporte** (règle donnée par l'utilisateur : en cas d'incohérence, la version la plus récente fait foi ; il n'a pas la force de tout ranger ni de tout synchroniser).
- **Source unique des statuts (décision du 7 oct.) : `fiches_references_projet.yaml`.** Il fait foi pour les statuts (relation, décision, limites de lecture, gimmicks, personnages, folklore). Une vue lisible (`VUE_references_projet.md`, générée par `generer_vue_md.py`) a existé ; l'utilisateur les a retirés du dépôt le 9 oct. 2026, le YAML se lit seul. Ce document-ci garde les précisions, le vocabulaire et les passages périmés ; en cas d'écart sur un statut, c'est le YAML qui l'emporte.
- Les anciens documents ne sont **pas modifiés**. Les passages devenus faux sont listés au §4, sans correction.
- Rappel de la règle de `01_CONTEXTE_ET_SUITE` §2 : on distingue **(U)** ce que l'utilisateur a dit ou décidé, **(IA)** les propositions de l'assistant (jamais des décisions implicites), **(dépôt)** ce qui est écrit dans les documents.

---

## 1. Précisions de l'utilisateur (U)

| # | Précision | Remplace ou complète |
|---|---|---|
| 1 | **Edenia est le nom provisoire du battle shōnen.** | `recap-session-pour-ia.md` et `influences-atelier.md` : « univers fantasy » seulement. |
| 2 | **Radiant est une référence, pas une influence.** Il sert de point de comparaison : l'utilisateur le comprend et essaie de ne pas s'en rapprocher trop (précisé le 7 oct. : ce n'est qu'un usage possible d'une référence, voir §3). | Nouveau (aucun MD ne classe Radiant). La page « Influences » ne cite pas Radiant. |
| 3 | **En cas d'incohérence, prendre la version la plus récente.** | Nouveau (règle de travail). |
| 4 | **Perceval = Perceval le Gallois** (inspiration de Brann). | Confirmation d'une supposition de l'IA. |
| 5 | **Les plus gros succès du battle shōnen ont presque tous un gimmick reconnaissable** : Pirate, Ninja, Shinigami, Épéiste/Samurai, Mage, Exorciste, Alchimiste. Hunter (Hunter × Hunter) ne rentre pas dans une case comme les autres. | Nouveau. |
| 6 | **Trois personnages dans Edenia**, avec seulement leurs inspirations (noms exacts demandés) : voir §2. | `recap-session` : « Edenia et Arcana n'ont que des noms ». |
| 7 | Les observations sur le catalogue MAL (action surtout fantasy/surnaturel ; comedy souvent romance) ne l'intéressent pas vraiment. | Archivées dans `analyse_mal_action_shonen.md`, sans valeur de décision. |
| 8 | **Plafond technologique théorique : 1950, hors technologie magique** (remplace 1930). La technologie magique reste non décidée. Les deux régimes (ordinaire / magique) sont voulus. | Remplace la décision du 3 oct. (1930). |
| 9 | **Harry Potter : films pour l'esthétique et les visuels seulement (statut : envisagé) ; les livres contiennent du matériau supplémentaire, intéressant** (quelques livres lus). Fonction des livres : non tranchée. | Remplace « rôle d'Harry Potter : non tranché ». Deux fiches YAML. |
| 10 | **Système de pouvoirs** : critère « éviter les pouvoirs sans limite (broken) » ; limites de portée, de puissance, de vitesse affirmées ; « plus le pouvoir est puissant, plus il demande de conditions » explicitement non décidé ; une limite de portée est structurante en soi ; hypothèses « matériel » et « enclencheur » à réexaminer. | Bloc `projet.systeme_de_pouvoirs` du YAML. |
| 11 | **Fullmetal Alchemist** : les deux alchimies servent à approfondir un système de pouvoirs ; du cadre militaire, « rien pour l'instant ». | Fiche FMA du YAML. |
| 12 | **Ton visé plus proche de Red Hood / Hunter × Hunter que de Fullmetal Alchemist.** Pas d'écart déclaré sur FMA (précisé le 7 oct.). | Fiches Red Hood et HxH (aspect « ton »). Rien sur la fiche FMA. |
| 13 | **« Archaïque mais pas trop »** = un style vestimentaire qui peut paraître daté. **Anachronisme** = éléments vestimentaires modernes dans un récit au cadre plus ancien : pas décidé, mais « a une part de vérité ». | Distingue deux notions que `Esthetique_vestimentaire_anachronique_Battle_Shonen.md` (§3.1) présente comme une seule (« archaïque mais pas trop (anachronique / hybride) » validée). |
| 14 | **Le style vestimentaire est copié/inspiré de Radiant et de Runeterra.** Les cadres temporels de Radiant, Runeterra, One Piece et Naruto sont flous (époques mélangées). | Radiant devient aussi une source d'inspiration (tenue) : `statut_relation: reference`, avec emprunt sur la tenue et distance sur les autres aspects. Le MD esthétique ne cite pas Radiant. |
| 15 | **Tenues-repères en images** : Academy Ekko (Cosmo Dumas) ; Fabula Fantasia, tome 1 (Brann, surtout pour des « Chevaliers », inspiration moins claire) ; une tenue d'académie **envisagée** (sans lacets aux baskets) ; une image dont le style global correspond à l'univers. | Bloc `projet.esthetique_vestimentaire` : images décrites en texte, fichiers non cités. Fabula Fantasia est une nouvelle fiche. |
| 16 | **Occultisme** : penche vers l'ambiance, volontairement non tranché (terme trop vague). **Personnages d'inspiration asiatique** : envisagé. **Objets bouddhiques japonais** : goût (intérêt). **Héritages mélangés** : dans les mêmes tenues et répartis par régions, articulation non décidée. | Reportés depuis la fiche vêtements du 5 oct. dans le YAML (blocs `occultisme`, `heritages_melanges`, `inspirations_visuelles_non_decidees`). |
| 17 | **Fabula Fantasia est un spin-off de Radiant** (Tony Valente, Ankama, tome 1 le 5 déc. 2025 ; vérifié sur Nautiljon). | Fiche Fabula Fantasia et fiche Radiant liées. Conséquence sur la limite de lecture : proposition de l'IA, à valider (voir §5). |

Les lignes 8 à 12 viennent du document `DELTA_a_reporter_dans_fiches_references_projet.md` (comparaison faite dans une autre discussion du 7 oct.) : je les ai reportées telles quelles, sans pouvoir vérifier la discussion d'origine.

Précédemment, il avait aussi demandé de **ne rien utiliser des tomes 7 et suivants de Radiant** et de garder les limites anti-spoil de `fiches_oeuvres_v3.md` (source unique : Worm = fin de l'arc 9 « Sentinel »).

## 2. Les trois personnages d'Edenia (U : noms et inspirations ; contenu des fiches = inspirations seulement)

| Personnage | Inspiré de |
|---|---|
| **Cosmo Dumas** | Ekko, Killua Zoldyck, Shisui Uchiha |
| **Brann** | Monkey D. Luffy, Yusuke Urameshi, Edward Elric, Perceval le Gallois |
| **Harley Delphine** | Shallan Davar (The Stormlight Archive), Hermione Granger, Lisa Wilbourne aka Tattletale, Magik (Illyana Rasputin) |

Ces fiches sont créées par `atelier-index.html` (création automatique au premier chargement, sans écraser une page déjà modifiée). Orthographes choisies par l'IA : « Uchiha » et « Rasputin » (graphies d'origine ; les éditions françaises écrivent « Uchiwa » et « Raspoutine »).

## 3. Influence et référence : emploi dans le projet

Le dépôt n'a **pas de définition écrite** de la différence. Deux emplois coexistent :

- **Dans le dépôt**
  - `frise_arbre_influences_v3.md` : une *influence* est un lien entre œuvres, avec un niveau de preuve (A à D). Le tableau §7 « classe des références » : une **référence [U]** est une chose que l'utilisateur a nommée pour son projet, ce qui ne permet pas d'en déduire un choix de conception.
  - `01_CONTEXTE_ET_SUITE` §2-3 : « références et préférences » ne sont pas des décisions de conception.
  - `influences-atelier.md` : une influence est ce qui a façonné l'utilisateur (histoire personnelle : SCP, Urban Rivals, etc.).
- **Définition donnée par l'utilisateur le 7 oct. (remplace ma formulation précédente, trop étroite) :**
  - **Influence** = ce qui l'a façonné, avec son histoire personnelle (SCP, Urban Rivals, etc.). La définition de `influences-atelier.md` est confirmée.
  - **Référence** = même chose avec moins de cette dimension personnelle. Ce n'est pas forcément un point de comparaison dont il s'éloigne : ce peut aussi être des éléments d'une œuvre qu'il pioche et s'approprie, avec un degré de changement variable.
  - **Red Hood** est dans les deux cas : certains éléments ont confirmé ce qu'il voulait faire (grâce à la compréhension de l'œuvre et des réactions du public), d'autres lui ont montré ce qu'il ne veut pas faire.
  - **Hypothèse de l'utilisateur** (formulée avec un doute) : poussés à la limite, les deux termes sont équivalents ; une influence serait une référence pas encore comprise ou étudiée. Statut : non tranchée, voir la discussion du 7 oct. Ne pas la traiter comme une règle.

Conséquence pour `fiches_references_projet.yaml` (appliquée le 7 oct.) : `statut_relation` accepte `influence+reference` (Red Hood) ; `emprunt_ou_ecart` accepte `confirmation` ; Red Hood a deux champs vides à remplir par l'utilisateur, `elements_confirmes` et `elements_a_eviter`. Les autres œuvres (hors Radiant et Red Hood) restent à `influence` par défaut (choix de l'IA, à confirmer). La frise v3 a une notion voisine : l'**écart délibéré** (§ 4.C).

## 3bis. Échelle décisionnelle (document de l'utilisateur, 7 oct. 2026)

Source : `Fiche_creatures_et_figures_folkloriques_statuts.md` (uploads). Elle prolonge les quatre catégories de `01_CONTEXTE_ET_SUITE` (références et préférences / décisions validées / indéterminations / propositions de l'assistant).

| Barreau | Sens (d'après la fiche) | Remarque |
|---|---|---|
| **Non précisé** | élément cité, statut non dit | |
| **Intérêt** | ce qui t'intéresse ou te plaît ; pas une décision pour l'œuvre | Nommé « Référence » dans la fiche de l'utilisateur ; **renommé « Intérêt » à sa demande (7 oct.)** pour ne pas le confondre avec la « référence » du §3. |
| **Envisagé** | élément auquel l'utilisateur a réfléchi comme une possibilité réelle pour l'œuvre, sans l'avoir validé ; il peut encore l'abandonner | Définition proposée par l'IA et **validée par l'utilisateur le 7 oct.** (la fiche disait : « piste sérieuse, non validée »). Test : s'être déjà demandé « où et comment l'utiliser ? » = envisagé ; sinon = intérêt. |
| **Décidé** | choisi pour l'œuvre | |

- **Vocabulaire :** le barreau bas s'appelle désormais « Intérêt ». « Référence » garde le sens du §3 (usage conscient d'une œuvre, avec plus ou moins de changement). Le sens générique du dépôt (tout ce qui est nommé) reste une source de confusion, non traitée.
- **Statuts connus (fiche de l'utilisateur) :** décidé = Agrippa. Envisagés = Barbegazi (rétrogradé de « décidé » à « envisagé » à la demande de l'utilisateur, 7 oct.), Mélusine, Ankou, Mourioche, Le Petit Homme rouge, Gayant, Le Houeron, Tarasque, Gremory/Gomory, Furfur, Marbas, Stolas. Intérêt = les 24 autres créatures de la carte (32 au total, comptées sur l'image), Chasse sauvage, Cour infernale, Limbo catholique, Limbo de Magik, enfer de *Dorohedoro*, *Inferno* et *Purgatorio*, purgatoire classique. Non précisé = les autres figures du Dictionnaire infernal.
- **Dans le YAML :** champ `statut_decision` (valeurs `non_precise | interet | envisage | decide`) sur chacune des 29 fiches. Renseigné pour BioShock Infinite (`decide`, zone industrielle, décision du 3 oct.), Mélusine et Petit Homme rouge (`envisage`) et Chasse sauvage (`interet`) ; vide pour les autres. Bloc `projet.folklore` : décidés et envisagés en liste, intérêts en deux listes (24 créatures de la carte, autres éléments). Bloc `projet.personnages_edenia` : les trois personnages et leurs inspirations (§2).
- **Limite :** l'échelle donne le degré de décision d'un élément, pas son degré de changement par rapport à l'œuvre source ; c'est le rôle d'`emprunt_ou_ecart`. Deux axes distincts.

## 4. Passages des anciens MD devenus faux ou périmés (non corrigés)

| Fichier | Passage | Ce qui est vrai maintenant |
|---|---|---|
| `Atelier App/Export 1/recap-session-pour-ia.md` §1, §3, §7 | Edenia et Arcana « n'ont que des noms » ; deux projets de manga. | Edenia = battle shōnen (nom provisoire) ; trois fiches de personnages. |
| `recap-session-pour-ia.md` §1 ; `frise_arbre_influences_v3.md` (lignes ~147, 401, 480) | Worm : « arc 9-10 », « limite arc 10 ». | Limite : fin de l'arc 9 « Sentinel ». |
| `Others/RECAPITULATIF_POUR_AUTRE_IA.md` ligne ~45 | Red Hood est de « Yūto Suzuki ». | Yuki Kawaguchi (VIZ). Yūto Suzuki est l'auteur de Sakamoto Days. |
| `Benchmark Oeuvre/01_CONTEXTE_ET_SUITE (1).md` §3 | Zones western et industrielle « envisagées » ; cosmologie, pouvoirs, intrigue ouverts. | Décisions du 3 oct. (un seul monde, plafond technologique 1930 **puis 1950 hors technologie magique le 7 oct.**, esthétique « archaïque mais pas trop ») : `Etude_complete_Dictionnaire_Infernal_1825.md` §4.2 et `Esthetique_…` §4.1. |
| `01_CONTEXTE_ET_SUITE` §8 | Tous les ZIP supprimés. | Plusieurs ZIP sont présents dans le dépôt. |
| `analyse_mal_action_shonen.md` | Source : `data/catalogue_mal_shonen.json`. | Chemin réel : `Benchmark Oeuvre/Myanimelist/catalogue_mal_shonen.json`. |
| `Esthetique_vestimentaire_anachronique_Battle_Shonen.md` (dans les ZIP `Others/workspace_*.txt`, deux versions : 3 régimes, 20 Ko, et 4 régimes, 28 Ko ; la plus récente corrige Naruto) | §3.1 : esthétique « archaïque mais pas trop (anachronique / hybride) » **validée** ; ne cite ni Radiant ni Fabula Fantasia ; écrit « Yūki Kawaguchi ». | Seul « archaïque mais pas trop » est décidé ; anachronisme non décidé ; Radiant est une source d'inspiration pour la tenue ; Yuki Kawaguchi. |
| `Fiche_vetements_9_images_reference (1).md` (5 oct.) | Zones western et industrielle « envisagées » ; technologie « jusqu'à environ 1945, envisagé » ; Radiant « référence et goût, pas une règle » ; « référence » et « goût » pour le barreau bas. | **Le YAML fait foi (décision du 7 oct.)** : zones dans le cadre validé ; plafond théorique 1950 hors technologie magique ; emprunt sur la tenue pour Radiant ; barreau « Intérêt ». Bandeau ajouté en tête de la fiche. |
| `fiches_references_projet.yaml` (en-tête) | « Aucun autre fichier n'a été modifié. » | **Corrigé le 7 oct.** : l'en-tête indique maintenant les mises à jour. |
| `Atelier App/Export 1/atelier-index.html` | Enregistre `./sw.js` ; le fichier présent s'appelle `atelier-sw.js` (v6, alors que `recap-session` annonce v24). | Le mode hors-ligne n'est pas actif tel quel. |

**À préciser :** Red Hood est donné à « 18 chapitres » (`01_CONTEXTE` §5, plusieurs analyses) et à 23 chapitres, en 3 tomes (MAL). Les deux sont peut-être compatibles (18 = fin de la prépublication annoncée ; 23 = total des tomes). Non vérifié.

## 5. Questions ouvertes (à trancher par l'utilisateur)

1. **Red Hood** : à la fois influence et référence (précisé par l'utilisateur le 7 oct.). Reste à noter quels éléments confirment ses choix et lesquels sont à éviter ; champ encore vide dans le YAML.
2. Les autres œuvres du YAML sont-elles toutes des influences, ou certaines sont-elles des références de comparaison comme Radiant ?
3. Œuvres associées aux gimmicks Épéiste/Samurai, Mage, Exorciste.
4. Gimmick d'Edenia (champs `gimmick_edenia` et `type_gimmick_edenia` vides dans le YAML).
5. **Esthétique : précisé le 7 oct.** (voir ligne 13 du §1). Reste à dire si l'anachronisme sera décidé ; le MD esthétique (§3.1) le donne comme validé.
6. **Fabula Fantasia et la limite de Radiant (fin du tome 6)** : le YAML applique par prudence la limite de Radiant à tout contenu de Fabula Fantasia qui en dépend. Proposition de l'IA, à valider ; tu n'as pas dit que tu lirais Fabula Fantasia.
7. Limites « One Piece = fin du tome 97 » et « Yu Yu Hakusho = chapitre 129 » : interprétation appliquée, confirmation non reçue.

## 6. Propositions de l'IA (non décisions)

- Typologie des gimmicks : identité / discipline / statut institutionnel / mixte. Hunter = statut institutionnel (licence délivrée par une association, après examen) ; confirmé par des sources pour Hunter × Hunter et Red Hood, de mémoire pour les autres séries.
- Si Edenia a un gimmick, il pourrait appartenir à l'un de ces trois types ; rien n'est décidé.
- Constat observé : plusieurs séries ont un arc d'examen ou de sélection lié au statut (Hunter × Hunter, Naruto, Black Clover, Kimetsu no Yaiba). Observation de mémoire, non vérifiée.

---

## Mise à jour du 9 oct. 2026 : matière arthurienne et nom de Brann

Source : toi (U). Détail dans `fiches_references_projet.yaml`, bloc `projet.arthurien`.

| # | Décision | Note |
|---|---|---|
| 16 | **Noms de lieux arthuriens français uniquement.** Lieux décidés : Brocéliande, Douloureuse Garde, Bénoïc, Gaunes, Trèbes, Montlair, La Terre Déserte, Le Lac (de la Dame du Lac). | Exception : lieux gardés pour la langue française du texte, même hors de France (Douloureuse Garde ; localisation non vérifiée). |
| 17 | **Personnages arthuriens = inspirations, avec des noms différents** : Perceval, Arthur, Merlin, Lancelot, Gauvain, Morgan, Guenièvre. | Seul lien fixé : Perceval → Brann. Merlin, Arthur et Lancelot comme personnages de toile de fond : abandonné. |
| 18 | **Se détacher de *Seven Deadly Sins* et de *Radiant* sur le plan arthurien.** | Portée exacte non précisée ; le statut de Radiant comme référence ne change pas. |
| 19 | **Le nom de famille de Brann est retiré** (« Pandragon ») et **laissé vide**. | Les mentions « Brann Pandragon » plus haut ont été remplacées par « Brann ». |
| 20 | **Barbegazi : envisagé** (pas décidé). La région montagnarde enneigée reste décidée. | Réponse à la question sur leur statut. |
| 21 | **Goal de Brann : intérêt**, « devenir chevalier, ou un goal similaire ». | Statut `interet` de l'échelle : ça t'intéresse, ce n'est pas décidé. |
| 22 | **Âge des personnages : on garde « peut-être 15-19 ans »** (pas de 17-19 ans). | Inchangé dans `inference_du_projet.md`. |
| 23 | **Le YAML est un fichier unique** : la version épurée a remplacé l'original le 9 oct. | Les retraits sont listés dans `epuration_yaml_retire.md`. |
| 24 | **Le personnage qui passe des épreuves est retiré.** | Il avait dit « oui » plus tôt. Ajusté dans `inference_du_projet.md` ; absent du YAML. |
