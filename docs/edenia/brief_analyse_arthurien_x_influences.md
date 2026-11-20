# Brief pour une autre IA : inductions, déductions et abductions sur les personnages arthuriens, rapprochées des influences du projet Edenia

*Écrit le 9 oct. 2026. **Aligné le 11 oct. 2026 sur `fiches_references_projet.yaml` : seuls Brocéliande et Le Lac sont décidés (les six autres lieux sont envisagés) ; limite de *The Way of Kings* = chap. 1 à 15 ; Merlin : voir la note plus bas. Les analyses du §7 ont été faites avant ces changements.** Ce document sert à refaire, vérifier ou approfondir une analyse déjà faite une première fois (§7). Il ne remplace pas la lecture des sources. Lis les sources avant de lire les résultats du §7.*

---

## 0. En une phrase

L'utilisateur prépare un **battle shōnen occidental** (nom provisoire : *Edenia*). Il veut savoir **comment les personnages du corpus arthurien sont construits** (fonction, rôle, histoire, design, personnalité) et **comment ils se rapprochent de ses influences**. Il veut aussi **relier ces résultats à son projet**, en s'appuyant sur le *Dictionnaire féodal* (1820) et sur les articles du *Dictionnaire infernal* (1825) qu'il a choisis.

## 1. La demande, telle qu'elle a été faite

> « Peut-on faire des inductions, abductions et déductions sur les personnages du corpus arthurien et leurs rapprochements dans leurs fonctions, rôle, histoire, design et personnalité avec mes influences, comme je l'avais fait avec Perceval et Gon ? Donne-moi une réponse complète, ça peut m'être très très utile pour la création de mon projet. De plus, relie tes résultats avec mon projet, avec des déductions, propositions et abductions sur mon projet. Lis aussi le Dictionnaire féodal et les articles des personnages historiques que j'ai choisis du Dictionnaire infernal. Donne-moi une réponse complète et approfondie, car je pense que c'est là que tout peut concorder. »

« Comme avec Perceval et Gon » renvoie à `structures_narratives_comparees.md` §10 (Gon et Perceval : tous deux partent de chez eux pour retrouver un parent absent ; l'objectif de Gon vient de lui, celui de Perceval lui est imposé par une humiliation publique).

## 2. Règles non négociables (elles viennent de l'utilisateur)

1. **Langue : français.** Propositions, récits, patterns : l'utilisateur préfère cela à une « théorie infaillible ».
2. **Répartition des raisonnements :**
   - **Induction et déduction** : sur le corpus, les références et les rapprochements (ce qu'il juge le plus pertinent).
   - **Abduction** : **seulement quand elle concerne SON projet**. Pas d'abduction sur les intentions des auteurs.
   - Format de l'abduction : **Observé → Abduction → Hypothèse (avec un test) → Proposition**.
3. **Pas de biais de confirmation.** Si l'utilisateur dit quelque chose de faux ou de fragile (par exemple « tout peut concorder »), le lui dire, avec nuance. Signaler les inférences fragiles.
4. **Étiqueter chaque affirmation** : *lu* (texte ou fichier ouvert), *dépôt* (résumé écrit dans une session précédente), *mémoire* (non vérifié), *relayé* (source secondaire). Ne jamais affirmer connaître une œuvre sans l'avoir vérifié. En cas de doute, fact-check.
5. **Hypothèses et propositions de l'IA = idées de l'IA.** Elles restent dans la conversation (ou `annexe_hypotheses_IA.md`). **Rien dans `fiches_references_projet*.yaml`** sans accord explicite. Le YAML ne contient que ce que l'utilisateur a dit ou décidé.
6. **Ne pas décider à sa place.** Ne pas fixer les rôles de Cosmo, Brann ou Harley. Ne pas lui demander de trancher ce qu'il n'a pas soulevé.
7. **Limites anti-spoil (lecture de l'utilisateur) :**
   - *Radiant* : jusqu'à la fin du tome 6 (rien des tomes 7+).
   - *Worm* : jusqu'à la fin de l'arc 9.
   - *Stormlight (The Way of Kings)* : Prélude, Prologue, chap. 1-15 et les 3 interludes (limite mise à jour le 11 oct. ; les analyses de ce brief et des fichiers liés couvrent les chap. 1-13).
   - *One Piece* : jusqu'au ch. 984 environ. *Yu Yu Hakusho* : jusqu'au ch. 129. *Jujutsu Kaisen* : anime S1 à S3 jusqu'à l'ép. 59.
   - Naruto, Bleach, HxH, FMA : pas de limite. *Harry Potter* : films vus, quelques livres.
   - Les recherches web ne sont pas interdites, mais **éviter les pages de wiki qui racontent la suite** pour les œuvres limitées.
8. **Rapports honnêtes** : dire ce qui a été lu et ce qui ne l'a pas été. Si deux documents se contredisent, prendre la version la plus récente.

## 3. État du projet (à la date du brief)

Source de vérité : `fiches_references_projet.yaml` (bloc `projet`, fichier unique depuis le 9 oct.). Lire ce fichier en entier avant de commencer.

- **Cadre :** monde de fantasy multi-héritages ; un seul monde, une seule époque ; zone western + zone industrielle de type BioShock Infinite ; plafond technologique 1950 hors technologie magique ; esthétique « archaïque mais pas trop » ; médium manga.
- **Gimmicks (métiers de shōnen) cités :** Pirate, Ninja, Shinigami, Épéiste/Samurai (sans œuvre associée), Mage, Exorciste, Alchimiste, Hunter.
- **Trois personnages d'Edenia (seulement leurs inspirations ; rôles non fixés) :**
  - **Cosmo Dumas** : Ekko, Killua Zoldyck, Shisui Uchiha.
  - **Brann** (nom de famille retiré) : Luffy, Yusuke Urameshi, Edward Elric, Perceval le Gallois.
  - **Harley Delphine** : Shallan Davar, Hermione Granger, Lisa Wilbourne (Tattletale), Magik (Illyana Rasputin).
- **Bloc `projet.arthurien` (décisions du 9 oct.) :**
  - Noms de **lieux arthuriens français** uniquement, avec l'**exception** de langue (La Douloureuse Garde est gardée).
  - Lieux décidés (11 oct.) : **Brocéliande et Le Lac (de la Dame du Lac)** seulement. Lieux **envisagés** (l'utilisateur ne les connaît pas) : **Douloureuse Garde, Bénoïc, Gaunes, Trèbes, Montlair, La Terre Déserte**. Au 9 oct., les huit étaient notés « décidés ».
  - **Aucun nom direct de personnage arthurien.** Les personnages arthuriens sont des **inspirations** avec des noms différents : **Perceval, Arthur, Merlin, Lancelot, Gauvain, Morgan, Guenièvre**. Lesquels inspirent quoi : non précisé.
  - Abandonné : Merlin, Arthur et Lancelot comme personnages de toile de fond. Précision du 11 oct. : Merlin était de base un personnage de l'œuvre ; la décision du 9 oct. (aucun nom direct) reste la plus récente.
  - Détachement de *Seven Deadly Sins* et de *Radiant* **sur le plan arthurien** (portée exacte non précisée ; Radiant reste `reference` dans le YAML).
- **Dictionnaire infernal :** *Agrippa* = décidé ; *Faust, Albert le Grand, Grandier, Merlin, Abel de Larue, etc.* = attrait fort, statut non précisé ; *Mélusine* = envisagé ; démons *Gremory/Gomory, Furfur, Marbas, Stolas* = envisagés (design). Intérêt : « Le Chien noir de Pontgibaud », la Chasse sauvage, la Cour infernale.
- **Autres décisions utiles :** âge possible 15-19 ans (« peut-être », de lui) ; le sujet principal n'est **pas** les hiérarchies ni l'institution ; pas de système de pouvoirs dans le YAML ; goal de Brann : intérêt, « devenir chevalier, ou un goal similaire » ; nom de famille de Brann laissé vide ; Barbegazi : envisagé.

## 4. Sources et accès

| Source | Où | Comment la lire | Limites |
|---|---|---|---|
| *Estoire de Merlin* (Vulgate, Sommer vol. II) | `sources_medievales/sommer_vulgate_vol2_merlin.txt` | `t = re.sub(r'\s+',' ', open(f,encoding='utf-8',errors='ignore').read())` puis `re.finditer` | OCR bruité ; résumés anglais de l'éditeur dans les marges (ne sont pas le texte médiéval) |
| *Lancelot propre* part. I (Sommer vol. III) | `sources_medievales/sommer_vulgate_vol3_lancelot_propre.txt` | idem | idem |
| *Charrette* (Tarbé 1849) | `sources_medievales/tarbe_1849_chevalier_de_la_charrette.txt` | idem | OCR |
| *Perceval* (Potvin, ms. de Mons) | `sources_medievales/potvin_t2.txt` (+ `t3`, `t4` continuations ; `perceval_le_gallois_t1` = **prose, pas Chrétien**) | idem | le *Conte du Graal* commence au vers 1283 |
| *Queste*, *Mort Artu* | **plus dans le workspace** | résumés dans `structures_narratives_comparees.md` §7 et `uploads/ages_vulgate_extraits.md` | pour les relire : archive.org `vulgateversionof05sommuoft` (vol. 5) et `…06…` (vol. 6), `https://archive.org/download/<id>/<id>_djvu.txt` ; un essai en oct. a eu des erreurs 401/404 |
| Âges dans la Vulgate | `uploads/ages_vulgate_extraits.md` | lire en entier | extraits de recherches sur « ans/aage » seulement |
| Débuts et goals des protagonistes | `debuts_et_goals_protagonistes.md` | §1 bis, §2 (Perceval, Charrette, Merlin, Lancelot) | résumés avec limites de lecture |
| Structures narratives | `structures_narratives_comparees.md` | §7 (cinq textes médiévaux), §10 (rapprochements), §11 (propositions) | §13 contient un désaccord non corrigé (HxH ch. 2 vs 7) |
| Fiches d'œuvres et sondages | `fiches_oeuvres_v3.md` | recherche par nom | 13 fiches avec « Force/Faiblesse » à refaire (⏳) |
| Hypothèses de l'IA | `annexe_hypotheses_IA.md` | « Étude de cas : Seth / Killua » | ce sont des hypothèses de l'IA, pas de l'utilisateur |
| **Dictionnaire infernal (ses extraits)** | dépôt GitHub `michaz94/Projecttest`, `Pdfmd/Dictionnaire_Infernal_Extraits.md` et `…_43-88.md` (versions 1818/1825/1844/1863 par article) | `re.search(r'^### NOM.*?(?=^### )', t, re.S\|re.M)` | extraits seulement ; vérifier la version (1825 de préférence) |
| **Dictionnaire féodal (1820)** | dépôt `michaz94/Projecttest`, `Others/workspace_2_dictionnaires_1820_1825.txt` (**c'est un ZIP renommé** : le copier en `.zip` et décompresser) → `dictionnaire_feodal_1820/dictionnaire_feodal_1820.db` (SQLite, table `articles` : `titre, categorie_principale, longueur_mots, texte`, 266 articles) | `sqlite3` ; lister les titres puis `select texte from articles where titre='CHAMPIONS'` | OCR bruité ; certains articles ne sont que des renvois (DUELS, ÉPREUVES → « Voyez Jugemens ») |
| Dictionnaire infernal complet | même ZIP : `dictionnaire_infernal_1825/dictionnaire_infernal_1825.db` | idem | ne pas charger les gros JSON en texte brut |
| Fiches de personnages d'influence | Fandom (`hunterxhunter`, `naruto`, `marvel`) via `action=parse&prop=text&redirects=1` + bs4, **User-Agent navigateur** | premiers paragraphes | spoilers possibles : lire seulement l'introduction ; voir §2 pour les limites |

Pour cloner le dépôt : `git clone --depth 1 https://github.com/michaz94/Projecttest`.

## 5. Méthode recommandée

1. **Lire** (ordre) : le bloc `projet` du YAML ; `ages_vulgate_extraits.md` ; `debuts_et_goals_protagonistes.md` §2 ; `structures` §7 et §10 ; puis les textes médiévaux ; puis les articles des deux dictionnaires.
2. **Pour chaque figure** (Perceval, Arthur, Merlin, Lancelot, Gauvain, Morgan, Guenièvre) : relever **fonction** (ce qu'elle fait pour l'intrigue), **rôle** (statut, relations), **histoire** (origine, parcours), **design** (couleur, armes, apparence, forme) et **personnalité** (réactions, mots du texte). Citer un extrait d'ancien français avec son lieu.
3. **Inductions** : régularités sur plusieurs figures ou textes. Écrire le nombre de cas (« 4 sur 4 », « 3 sur 6 ») et la preuve.
4. **Déductions** : prémisse (citée) → conséquence. Marquer où l'inférence est fragile.
5. **Rapprochements** : pour chaque influence de l'utilisateur (10 personnages), chercher la figure arthurienne la plus proche sur ≥ 2 axes. Noter **forte** (fonction + histoire + personnalité concordent), **moyenne**, **faible** (surface seulement : couleur, nom). Il y a 70 paires possibles : beaucoup de ressemblances sont du hasard. Dire ce qui compterait comme un contre-exemple.
6. **Dictionnaires** : pour chaque article choisi (Agrippa, Faust, Albert le Grand, Merlin, Grandier, Abel de Larue, Mélusine) : résumer, puis relier au projet. Pour le féodal : chercher ORDRES DE CHEVALERIE, CHAMPIONS, ÉCUYER, ÉPÉE, FÉLONIE, CHÂTEAUX, JUGEMENS, BÂTARDS, BÉJAUNES, CADETS, FOI ET HOMMAGE, ADULTÈRE, SEIGNEUR, BASTILLE, etc.
7. **Abductions sur le projet** : Observé → Abduction → Hypothèse (+ test) → Proposition. Seulement sur son projet.
8. **Fragilités** : lister ce qui n'est pas vérifié, les sources secondaires et les écarts entre documents.

## 6. Format de sortie attendu

1. Réponse courte (oui/non + règle de répartition des raisonnements + avertissement sur le biais de confirmation).
2. Ce qui a été lu / pas lu / de mémoire.
3. Inductions (tableau : régularité, preuve, source).
4. Déductions (prémisse → conséquence, avec les dictionnaires).
5. Rapprochements (tableau : figure, influence, axes, force).
6. Abductions et propositions sur le projet (format Observé/Abduction/Hypothèse/Proposition).
7. Fragilités.
8. Ce qui change par rapport aux analyses précédentes (consigne T215) : dire si les nouvelles informations changent le point de vue, contredisent une inférence ou en donnent de nouvelles.
9. Proposer, sans le faire, de ranger le résultat dans `annexe_hypotheses_IA.md`.

## 7. Résultats de la première passe (9 oct. 2026) : à vérifier, ne pas recopier aveuglément

### Inductions (I)

| # | Régularité | Preuve et lieu |
|---|---|---|
| I1 | Entrée dans le monde à 14-18 ans : Arthur 16, Lancelot 18, Perceval ≈ 15 (14 dans le ms. de Mons), Galaad 15/18, Dodinel 14, Sagremor 15 ; un groupe de jeunes attend Arthur pour être adoubé | `ages_vulgate_extraits.md` |
| I2 | Quelqu'un d'autre donne les armes ou le statut : la Dame du Lac arme Lancelot (armes blanches, anneau) ; l'archevêque fait Arthur chevalier ; Gauvain adoube Éliézer | `debuts_et_goals_protagonistes.md` §2 ; `ages_vulgate_extraits.md` |
| I3 | Identité différée (4 sur 4) : Lancelot apprend son nom sur une dalle à la Douloureuse Garde ; Merlin « nes sans pere » ; Arthur élevé par Antor ; Perceval tenu loin de la chevalerie par sa mère | Textes ; `debuts…` |
| I4 | Le maître est neutralisé par son élève : Niniane (« Nymenche ») apprend de Merlin et le scelle « en vne caue dedens la perilleuse forest de darnantes » ; Merlin approche Viviane en « samblance » de beau valet à la fontaine de la forêt de Briosque | `lancelot_propre` (grep `darnantes`, `nymenche`) ; `merlin` (grep `briosque`) |
| I5 | Le meilleur chevalier n'est pas l'élu (Lancelot / Galaad, Perceval) | `structures` §7 (résumé), **non relu au texte** |
| I6 | Les femmes distribuent le statut : la Dame du Lac arme ; la Reine accepte Lancelot comme son chevalier et lui envoie une épée ; Gauvain et ses compagnons sont appelés « chevaliers a la roine Genieure » | `debuts…` ; `merlin` (grep `a la roine genieure`) |
| I7 | Les lieux changent de sens : « des lors en auant fu apeles li chastiax la ioiouse garde » ; la « Noeue Ferté en Brocéliande » est un lieu de rendez-vous | `lancelot_propre` (grep `ioiouse garde`) ; `merlin` (grep `broceliande`) |
| I8 | Design porté par la couleur ou la forme : « li blans cheualiers » (armes blanches, puis écu vermeil, puis écu blanc) ; Merlin change d'apparence ; Excalibur « ieta ausi grant clarte comme se doi chierge i eussent este alumees » ; Morgan « iouene damoisele & gaie durement & moult enuoisie… moult estoit brune de vis » | grep `escalibor`, `morgain` dans `merlin` ; `lancelot_propre` |

Autres faits lus : la mère de Merlin le fait baptiser sous le nom de son grand-père (Merlin II) ; le conseil des diables décide d'« engendrer un homme qui aprendra les autres » (début de l'*Estoire de Merlin*) ; Morgan est « mise en vne maison de religion » pour apprendre lettres, arts et astronomie, puis apprend de Merlin « maintes merueilles » ; Guenièvre est fille unique de Léodégan de Carmélide, la terre doit lui échoir ; Gauvain « sires & maistres & compains de la table roonde » (« preudomme & boin cheualier & loial ») et tire Escalibor dans plusieurs scènes ; Arthur a 16 ans, retire l'épée d'un perron avec une enclume, et Escalibor est un nom « ebrieu » : « trenche fer & achier & fust ». Dans le *Lancelot propre*, le roi Arthur n'a pas le temps de secourir Ban (« auoit tant a faire de maintes pars »). Morgan n'apparaît **que** dans l'*Estoire de Merlin* parmi les textes du workspace (les autres occurrences de « morgan » sont des faux positifs : Glomorgan, « morgant »).

### Déductions (D)

- **D1** : ORDRES DE CHEVALERIE (DF) exige « noble de père et de mère, trois générations » et 21 ans ; « on ne voit pas qu'un bon roturier soit jamais entré dans la chevalerie ». ⇒ un héros sans nom ne peut devenir chevalier que si le récit lui donne une naissance cachée (explique I3). Écart : romans 14-18 ans, DF 21 ans. **Attention** : la « dispense » du DF concerne la naissance, pas l'âge.
- **D2** : FÉLONIE (DF) : le vassal qui a couché avec la femme du seigneur, l'a embrassée ou lui a déclaré sa passion commet une félonie ⇒ Lancelot/Guenièvre est un crime féodal avant d'être une faute morale.
- **D3** : CHAMPIONS et JUGEMENS (DF) : des champions louables, jugement par combat ⇒ la fonction de « champion » a une base institutionnelle ; la *Mort Artu* (résumé `structures` §7) fait défendre Guenièvre contre l'accusation d'empoisonnement.
- **D4** : CHÂTEAUX (DF) : « c'est sur cela que les romanciers ont forgé leurs chevaliers errans, et tant de géans et de monstres… l'origine des enchanteurs… et des châteaux enchantés » ⇒ la Douloureuse Garde (deux enceintes, nul n'en sort) correspond à cette lecture.
- **D5** : Faust (« les moines l'ont livré au diable » pour l'imprimerie), Albert le Grand (androïde-oracle brisé par Thomas d'Aquin), Agrippa (accusé de sorcellerie) ⇒ le savoir qui innove passe pour de la magie.
- **D6** : chien noir démon familier chez Agrippa, Faust (barbet noir) et Abel de Larue (barbet noir) = 3 articles sur les 6 choisis ; le YAML contient « Le Chien noir de Pontgibaud ».
- **D7** : DI Merlin : « enclos et invisible à l'ombre d'un bois d'aubépine » à Brocéliande par Viviane ; Gauvain « seul l'entendit, mais ne put le voir ».

### Rapprochements (R)

| Figure | Influence | Axes | Force |
|---|---|---|---|
| Perceval | Luffy (mémoire) | naïf, but simple déclenché par un adulte qui montre un statut | forte |
| Perceval | Edward (mémoire) | prendre un conseil à la lettre et en payer le prix | moyenne |
| Lancelot | Yusuke (mémoire) | agir par pitié sans calcul (premier acte de Lancelot) | moyenne |
| Lancelot | Killua | meilleur combattant écarté pour un attachement ; blanc (surface) | moyenne |
| Merlin | Edward (mémoire) | savant à la création contre nature, prix lourd | moyenne |
| Merlin | Ekko (mémoire) | savoir du temps, inventeur | faible |
| Gauvain | Shisui | modèle éclipsé, loyal, resté aimé | moyenne |
| Morgan | Shallan (lu) | l'élève qui prend le secret du maître | forte |
| Morgan / Viviane | Hermione (mémoire) | l'élève qui retourne le savoir | moyenne |
| Morgan | Magik | sorcière entraînée, attitude « mischievous », lien à un autre monde (Fandom) | moyenne |
| Guenièvre | Lisa (mémoire) | lire les gens | faible |
| Dame du Lac | Mélusine | lien de fée avec une condition | faible |

Vérifié sur Fandom : Killua (cheveux blancs, entraînement d'assassin, deutéragoniste), Shisui (Anbu, meilleur ami d'Itachi, « Body Flicker »), Magik (enlevée dans les Limbes, sorcière, attitude « mischievous »). Pour Ekko, Hermione, Lisa, Luffy, Yusuke et Edward : **mémoire, non vérifié**.

### Abductions et propositions (A)

- **A1** : fonctions sans noms. *Test :* « qui est l'Arthur de ton histoire ? » refusé d'être résolu par un seul personnage. *Proposition :* une fonction par personnage (Radiant critiqué comme « pot-pourri de nekketsu »).
- **A2** : la géographie arthurienne (huit lieux au 9 oct., six désormais envisagés) vient de l'ouverture du *Lancelot propre* (Ban, Bohort, Claudas : Bénoïc, Gaunes, Trèbes, Montlair, Terre Déserte). *Hypothèse :* un passé de royaumes conquis. *Proposition :* régions de conte nommées d'après ces lieux ; un enfant élevé loin par une figure féminine.
- **A3** : arc-forteresse à deux noms (Douloureuse → Joyeuse Garde ; arcs-lieux de HxH/OP : Heavens Arena, Impel Down).
- **A4** : savoir interdit (Faust, Agrippa, Albert, Grandier, Abel) + plafond « 1950 hors magie » ⇒ Harley « paie son savoir ».
- **A5** : métier plutôt qu'ordre : chevalier errant (CHÂTEAUX), champion (CHAMPIONS), écuyer (ÉCUYER). Sans nom de famille pour Brann, un roturier chevalier devient une transgression (D1).

### Fragilités connues de la première passe

- Beaucoup de rapprochements sont moyens ou faibles ; seuls Perceval–Luffy et Morgan–Shallan sont forts.
- Que Gornemant arme Perceval est **de mémoire** (le dépôt dit seulement « apprentissage chez Gornemant »).
- Le Dictionnaire féodal de 1820 est une compilation ironique et rationaliste, pas une source d'histoire médiévale.
- Viviane et la Dame du Lac sont traitées comme distinctes (le texte lu ne les identifie pas).
- Le motif « le second rôle écrase le héros » (Killua) vient de `annexe_hypotheses_IA.md` : c'est une hypothèse de l'IA, pas de l'utilisateur.

## 8. Pièges connus (déjà rencontrés)

- **Chercher sur le web avant d'ouvrir les documents du projet** a produit des erreurs. Lire d'abord le YAML, `debuts…`, `structures…` et `inference_du_projet.md`.
- L'OCR est bruité : toujours normaliser les espaces, essayer plusieurs graphies (`bertaigne`, `bretaigne` ; `gannes`, `gaunes` ; `iouene`, `jouene`).
- Les résumés anglais en marge de Sommer ne sont pas le texte médiéval : ne pas les citer comme tels.
- `fiches_references_projet.yaml` : toute valeur contenant « : » doit être entre guillemets ; toujours recharger avec `yaml.safe_load` après modification. Faire une sauvegarde avant d'écrire. Utiliser un remplacement avec `assert t.count(a)==1`.
- Ne pas relancer `refaire_force_faiblesse_avis.py`, `rapport_hxh_kite_hisoka.py` (ils écraseraient des retouches).
- Résultats web : filtrer les spoilers (Radiant, JJK après l'ép. 59, GoT S8, HxH Succession Contest).
- Dictionnaire féodal : les articles DUELS, ÉPREUVES, CHEVALERIE sont des renvois ou des notices de 4 à 20 mots. Utiliser JUGEMENS et ORDRES DE CHEVALERIE.

## 9. Checklist avant d'envoyer la réponse

- [ ] Chaque affirmation porte une étiquette (lu / dépôt / mémoire / relayé).
- [ ] Les abductions ne portent que sur le projet de l'utilisateur.
- [ ] Les rapprochements sont notés forte / moyenne / faible, avec au moins un contre-exemple discuté.
- [ ] Rien n'est écrit dans le YAML.
- [ ] Aucun spoiler au-delà des limites du §2.
- [ ] La réponse dit ce qui n'a pas été lu (Queste, Mort Artu) et ce qui vient de la mémoire.
- [ ] Une section « ce qui change par rapport aux analyses précédentes ».
- [ ] La fin propose de ranger le résultat dans `annexe_hypotheses_IA.md`, sans le faire.
