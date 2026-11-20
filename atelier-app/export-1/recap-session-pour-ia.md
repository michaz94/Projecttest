# Récapitulatif complet de la session — à transmettre à une autre IA

> **Mode d'emploi** : ce document est écrit pour qu'une IA reprenne le travail sans rien reperdre. Il résume une longue session de travail (plus de 130 tours utilisateur) entre Michaz (l'utilisateur, humain) et un agent IA sur Arena.ai. Tout ce qui est marqué « confirmé » a été dit explicitement par l'utilisateur. Ce qui n'est pas confirmé est signalé comme tel.

---

## 0. MIGRATION : l'utilisateur quitte cette plateforme — les exports

L'utilisateur migre vers une autre IA. Quatre archives ZIP (< 25 Mo chacune) ont été produites à partir de `resultat/` — elles contiennent TOUT le important de la session :

| ZIP | Contenu |
|---|---|
| `export-1-app-atelier.zip` (~1,6 Mo) | **L'app principale** `atelier-index.html` (v24) + `atelier-sw.js` + la référence `atelier-v7-corrige/` + la visionneuse FLB (`visionneuse/`) + `wiki-influences-fusion.html` (page Influences) + textes `influences-atelier/` + **ce récapitulatif** |
| `export-2-modeles-fandom.zip` (~2,9 Mo) | Les modèles pour vrais wikis : `modele-wiki/` (Wikipédia), `modele-wiki-fandom/` (Fandom + les 6 aperçus : article, catégorie, liste, accueil — mobile et web), source React `personal-fandom-wiki-template-fusion.zip` |
| `export-3-rapports-codes.zip` (~2,0 Mo) | `code-fandom/` (le vrai code visionneuse/galeries/infobox Fandom), audit d'articles, comparaison, captures d'« Article détaillé », fonds de listes, dossier World Anvil, recherche Akutami, dump du sommaire Fandom |
| `export-4-doc-hors-ligne.zip` (~9,3 Mo) | Le miroir hors ligne de 112 pages de documentation Fandom + World Anvil (270 images intégrées) |

**PAS inclus dans les exports** (et pourquoi) : les sources de travail `work/` (builders `build_*.py`, wikicodes sources `work/page-categorie/` et `work/page-accueil/`, code source de la lightbox `work/lightbox/`, textes World Anvil `work/wa/`, CSS Wayback `work/wayback/`) — les aperçus livrés sont auto-contenus, mais si la nouvelle IA doit RÉGÉNÉRER quelque chose, ces sources manqueront ; les uploads de l'utilisateur (contexte seulement) ; les zones de données non approuvées au nettoyage. Le récapitulatif reste la référence : il liste chaque livrable et son rôle.

---

## 1. Qui est l'utilisateur

- **Prénom/pseudo : Michaz.** Il est en France (heure de Paris).
- **Il travaille exclusivement à travers l'IA** : il ne dessine pas et n'écrit pas lui-même — c'est lui qui dicte, l'IA rédige, code et produit les livrables.
- **Il travaille depuis son téléphone** (Android, Chrome). Conséquence confirmée : ne jamais suggérer d'outils de bureau comme les devtools ou « Inspecter ».
- **Langue : français.** Toute la conversation et les livrables sont en français. Il aime le format « guide analytique » pour les explications.
- **Il est créateur d'univers** (worldbuilding) avec deux projets de manga en tête, aux stades embryonnaires :
  - **Edenia** — univers fantasy (esthétique influencée par Warcraft, mais plus proche de Runeterra, dit-il) ;
  - **Arcana** — univers urbain moderne (idée d'une organisation « grise » façon Fondation SCP, qu'il juge lui-même « cliché »).
- **Lecture en cours (confirmé à la dictée)** : *Worm* de Wildbow (arrêté vers l'arc 9-10 ; interdiction de spoilers au-delà de l'arc 10) et *The Stormlight Archive* (11 premiers chapitres seulement ; interdiction de spoilers Stormlight).
- **Documents uploadés** : à traiter comme du contexte uniquement, jamais transcrire dans les livrables.

## 2. Les règles de travail qu'il a fixées (confirmées)

1. **« Ne crée ni n'invente rien. »** La recherche est bienvenue, mais pas l'invention. Chaque élément repris d'un site réel doit être tracé (source, date, licence, auteurs).
2. **Rédaction** : n'écrire QUE ce qu'il dicte. Les fautes d'orthographe peuvent être corrigées, le placement dans les sections Fandom est négociable. Les sections vides reçoivent « À compléter », et on lui dit où chaque élément a été placé.
3. **Quand une demande est ambiguë, demander** — ne jamais choisir une option à sa place en silence (il a confirmé plusieurs fois, tour 46 notamment).
4. **Jamais supprimer un livrable ou un upload sans son accord explicite.**
5. **Il n'aime pas les réponses où l'IA « fait à sa place »** : les options sont présentées, c'est lui qui tranche. Beaucoup de ses demandes d'option sont restées sans réponse (voir §9).
6. Il a demandé explicitement de **ne pas déduire ses préférences** : tout ce qui n'est pas confirmé par lui doit être signalé comme non confirmé.

## 3. Le projet principal : « l'Atelier »

Une application web mono-fichier (HTML/CSS/JS, service worker, IndexedDB) — un wiki personnel mobile-first pour son worldbuilding, progressivement construit sur toute la session.

- **Fichier principal** : `resultat/atelier-index.html` (miroir de travail : `work/mwapp/public/atelier/index.html`). Service worker `sw.js`, version courante **atelier-v24** (tour 111).
- **Il a tranché une ambiguïté importante (confirmé, tour 102)** : la VRAIE app est l'ancienne `atelier-index.html` (celle d'origine, enrichie), PAS la variante `atelier-v7-corrige` (une réécriture comparée pendant les tours 94-100, conservée comme référence).
- **Structure de l'app** : Accueil (salutation « Bonsoir, Michaz », Re-plongez-vous, compteurs, prompt du jour), Mondes (cartes Edenia/Arcana), articles par catégories (personnage #4da3ff, lieu #4cc38a, faction #ff7a5c, artefact #eebf4d, événement #8f7bff, concept #5fd4e6), Épinglés, Réglages, tiroir (Idées, Épinglés, Corbeille, Sommaire en DERNIER), barre du bas Accueil · Mondes · (+) · Épinglés · Réglages, le (+) ouvrant des actions de création.
- **Style actuel de l'article (tour 108-109)** : titre Cinzel 27px ; corps Manrope 16px `#e6e6e6`, gras `#f4f1ef` ; h2 en Barlow Condensed 31.9px avec soulignement (1px + segment de 90px couleur catégorie) — **sans barre verticale** (rejet confirmé tour 122) ; h3 25.3px ; liens et actions en or `#eebf4d`, jamais de soulignement de lien ; ordre mobile : intro courte → infobox repliée → sommaire → sections.
- **La visionneuse d'images « FLB »** (écrite sur mesure, tours 64-101) est LA visionneuse de tous les livrables : barre du haut 57px noire 60%, compteur en bas centré, vignettes 44px, image contenue avec contour 15px jamais agrandie, fermeture par tap sur le vide, bouton Retour du téléphone qui ferme, zoom 2,5×/6×. Une version de test automatique existe (`work/lightbox/test/t_visionneuses.py`, 60 vérifications — dernière exécution : 60/60).
- **Wikicode maison supporté** dans les articles : `[[lien]]`, `{{slug}}` (transclusion), `{{Article détaillé|Titre}}` (tour 109, pluralisation automatique acceptant aussi `{{Articles détaillés|A|B}}` — c'est un ajout maison, Wikipédia n'a pas ce modèle pluriel, signalé à l'utilisateur), notes `[^1]`, spoilers `||…||`, citations, listes, et depuis le **tour 111 : tableaux markdown complets avec alignements** (`| --- |`, `| :--- |`, `| :---: |`, `| ---: |`), l'onglet « Tableau » de la bibliothèque d'insertion est actif (3 squelettes), et le bug d'aller-retour Visuel↔Source qui détruisait les tableaux est corrigé. Test dédié 9/9.
- **Contenu de démonstration** : articles seed (Archimage Kael Valerius, Sun Citadel, Sol-Blade…) ; Edenia et Arcana n'ont que des noms (confirmé tour 105).

## 4. Les livrables de la session (où ils sont)

Tout est dans `/home/user` :
- `resultat/atelier-index.html` — l'app principale (v24).
- `resultat/modele-wiki/` — modèle d'article + infobox pour wiki MediaWiki/Wikipédia, et un aperçu HTML à onglets (`apercu-modele-article.html`) avec l'onglet « Modèle:Article détaillé ». (Les zips ont été SUPPRIMÉS sur ordre explicite de l'utilisateur après le nettoyage ; recréables en une commande.)
- `resultat/modele-wiki-fandom/` — l'équivalent pour Fandom (article, infobox portable, licence Rubik), avec quatre aperçus : article mobile et web, ET pages catégorie mobile et web (`apercu-categorie-*.html`, tour 112 : descriptions réelles de Hunterpedia/One Piece, index réel de Catégorie:Personnages — 389 pages — et Help:DynamicPageList intégral ; la mise en page de liste est reconstituée, signalée dans les aperçus).
- `resultat/wiki-influences-fusion.html` — la page « Influences » (React fusionné, voir §6).
- `resultat/modele-wiki-fandom/apercu-liste-{mobile,web}.html` — aperçus de la **page-liste** « List of Fullmetal Alchemist characters » (fma.fandom.com) : wikicode intégral 12,4 Ko avec 214 `{{Char|image|Nom}}` (cases rouges #E00000, 164px), `<tabber>` par familles, sommaire rouge ; 4 vrais avatars Elric embarqués ; onglet « Modèles » avec le code exact de `{{Char}}` (Jppcouto) et du sommaire (LostRunes).
- `resultat/modele-wiki-fandom/apercu-accueil-{mobile,web}.html` — aperçus de la **page d'accueil d'un univers** : column tags réels (gauche fluide + droite 300px), page principale réelle du wiki HxH FR (Gorgo616, 2019, contenu dans des transclusions Modèle), **Mobile Main Page DÉPRÉCIÉE** (preuve : Help:Mobile Main Page, 22/07/2026 — l'accueil mobile réel = stats + description + tendance) ; contenu « À compléter » partout (règle de dictée) ; les onglets → Catégories et → Pages-listes relient les deux systèmes de liens.
- `resultat/world-anvil-fonctionnalites.html` — dossier des 21 fonctionnalités World Anvil comparées à Fandom et à l'Atelier (tour récent ; l'utilisateur a dit « non ce n'est pas ce que j'ai demandé » SANS préciser pourquoi — deux questions de clarification posées, restées sans réponse).
- `resultat/documentation-fandom-worldanvil.html` — doc hors ligne (14 Mo).
- `resultat/code-fandom/` — le vrai code de la visionneuse Fandom (Wayback + ancien dépôt open source), avec README détaillé des comportements relevés.
- `resultat/audit-articles/`, `resultat/comparaison/`, `resultat/visionneuse/`, `resultat/fonds-listes/`, `resultat/article-detaille/` (captures JPEG), `rapport-tailles.md` (racine).
- Sauvegardes avant chaque modification d'atelier : `work/atelier-index.avant-tXX.html`.

### Hiérarchie : quel code fait autorité, et à quoi chacun sert

| Code / fichier | Statut | À quoi il sert |
|---|---|---|
| `resultat/atelier-index.html` (miroir : `work/mwapp/public/atelier/index.html`) | **LE code principal — prioritaire sur tout** | L'app elle-même, le livrable final. Toute nouvelle fonctionnalité se code ICI. Les autres fichiers ne sont que des annexes de démonstration ou des modèles pour sites réels. |
| `work/mwapp/public/atelier/sw.js` | Principal (accompagne l'app) | Le service worker de l'app ; à re-versionner à chaque modification (v24 actuellement), sinon le téléphone sert l'ancienne version. |
| `work/merged/` → `resultat/wiki-influences-fusion.html` | Secondaire, autonome | La page « Influences » (React). Livrable séparé avec sa propre typographie (DM Sans, Barlow Condensed) et ses tons coral/violet/or/cyan. Les changements d'Atelier ne s'y propagent PAS, et inversement. |
| `resultat/modele-wiki/` et `resultat/modele-wiki-fandom/` (+ zips) | Modèles, pas du code d'app | Du wikicode à coller dans un VRAI wiki (MediaWiki/Wikipédia ou Fandom). Les aperçus HTML qu'ils contiennent (`apercu-*.html`) sont des démos à onglets servant à COMPARER les rendus (Lire / Wikicode / Infobox / Article détaillé / Principal). Régénérés par `work/build_apercu.py` et `work/build_fandom2.py`. |
| `atelier-v7-corrige/` | **Référence figée — ne jamais y coder** | La comparaison des tours 94-100. Il a explicitement tranché (tour 102) : ce n'est PAS l'app. Certains de ses designs (cartes d'accueil) ont été reportés dans l'app principale, rien de plus. |
| `work/lightbox/` (lightbox.js/.css, inject.py, test) | Composant partagé | Le code source de la visionneuse FLB, injectée dans tous les livrables HTML par `inject.py`, plus son test automatique (60 vérifications). À modifier seulement quand on change la visionneuse elle-même. |
| `work/wayback/`, `work/wa/`, `work/article-detaille/` | Archives de recherche | CSS et pages réels relevés (Fandom, World Anvil, Wikipédia). Servent de preuve/source ; ne pas modifier. |
| `resultat/world-anvil-fonctionnalites.html`, `rapport-tailles.md`, `resultat/audit-articles/` | Rapports | Documents de consultation. L'audit ne modifie jamais l'app sans son choix. |

## 5. Comment on travaille (méthode confirmée et validée par lui)

- **Récupération du vrai code** (demandée explicitement au tour 127) : Wikicode via `action=raw`, HTML réel via `api.php?action=parse`, dépendances suivies jusqu'au bout (modules Lua → leurs requires → etc.), CSS depuis les vraies feuilles (Common.css, Gadget-Mobile.css pour Wikipédia ; captures Wayback de load.php pour Fandom dont les pages normales renvoient 403). Chaque source est créditée (CC BY-SA 4.0 Wikipédia ; CC-BY-SA wikis Fandom ; LGPL pour l'icône loupe Searchtool.svg).
- **Playwright** sert aux captures et aux tests automatiques (il ne voit pas les outils de bureau — l'IA, elle, s'en sert et lui montre des captures JPEG).
- **Les captures d'écran que lui envoie sont la référence absolue du rendu Fandom** (le site bloque les robots).
- **Contrainte d'espace** : le workspace a un plafond ~128 Mo. État au dernier rapport : **~128 Mo atteint** (alerte donnée). Liste de nettoyage proposée (non validée) : `work/scrape/` (~12 Mo), `work/cmp/`+`work/toctest/` (~13 Mo), `work/wayback/` (~7 Mo), vieilles sauvegardes (~10 Mo). **Aucune suppression sans son accord.**

## 6. La page « Influences » (détail demandé récemment)

- C'est un projet React (`work/merged/`) : la page de ses influences dictées, fusion de deux versions (base v1 + en-tête et barres h2 colorées de v2, confirmé tour 6).
- **Répartition du contenu (confirmée en fin de session)** : TOUT le récit et les listes viennent de lui (dictée) ; l'IA n'a ajouté QUE : les 11 notes de bas de page de vérification (dont une affirmaton fausse repérée dans la source d'une note — la note 2), deux phrases de chapeau, et la forme (style).
- Typographies : DM Sans 17.6px pour le corps, Barlow Condensed pour les titres (confirmé tour 121), tonalités coral/violet/or/cyan, barre collante (tour 120).
- La liste des influences citées dans le texte a été fournie au tour précédent (Fondation SCP → Lovecraft, Doctor Who, Urban Rivals, mangas, Worm, Watchmen, Runeterra…).

## 7. Historique condensé de ce qui a été fait (par thèmes)

1. **Tours 1-5** : tests de mémoire (CAN 2025 : Sénégal ; Super Bowl LX : Seahawks 29-13), recherche World Anvil, dates de coupure des modèles.
2. **Tours 6-18** : fusion de la page Influences ; typographie ; règles de dictée ; recherche Akutami ; interview (règle : les questions d'interview n'apparaissent jamais dans la page).
3. **Tours 20-44** : recherche doc Fandom/World Anvil ; sommaire de l'Atelier (portage du code Wikia ToC, GPL, avec corrections word-break/scroll-lock ; numérotation jamais modifiée ; Sommaire en dernier dans le tiroir).
4. **Tours 45-55** : modèle MediaWiki ; format Atelier ; Markdown vs Wikitext ; comparaisons de style.
5. **Tours 56-62** : article Fandom complet (wikitext + infobox portable), aperçus mobile ET web séparés (confirmé tour 61), rapport de comparaison. Règle : ne JAMAIS mélanger du Wikipédia ou du bureau dans le look Fandom mobile (confirmé tour 58).
6. **Tours 64-101** : la visionneuse FLB — plusieurs moteurs comparés, le sien retenu et tuné (les valeurs exactes au §3), injectée partout, un test auto de 60 vérifications.
7. **Tours 102-118** : intégration dans la VRAIE app ; barre du bas + actions (+) ; Edenia/Arcana noms seulement ; accueil réorganisé (ordre confirmé) ; vignette = 1re image (couverture incluse, confirmé tour 112) ; listes sur fond `#17171a` sans retours ; fonds de listes générés (tour 113) ; **braises d'ambiance actives mais UNIQUEMENT sur les 4 vues de liste** (confirmé tour 118).
8. **Tour 114** : il voulait des fonds plus vivants et un paysage fantasy pour Mondes — **toutes les propositions d'images refusées deux fois ; ne pas régénérer sans demander.**
9. **Tours 119-124** : audit comparé des pages d'article (Atelier/Fandom/Wikipédia/Influences, scores 3.4/3.5/4.1/3.8 — l'audit ne propose jamais sans son choix) ; série de correctifs confirmés (tour 120 : infobox repliée mobile avec champs clés choisis dans l'éditeur, h1 27px, or pour liens/actions seulement, tailles infobox 11/13/14px, intro avant infobox mobile seulement ; tour 121 : titres de section en style Influences, JAMAIS de section avant l'infobox ; tour 122 : texte `#e6e6e6`, plus de barre verticale h2) ; explication des conventions de liens de titre (tour 123) ; captures Wikipédia d'« Article détaillé » (tour 124).
10. **Tours 125-127** : option B (lien Sol-Blade dans la phrase de Kael, confirmé) ; option A (Article détaillé) en TEST ; **tour 127** : mise des codes EXACTS réels (Wikipédia `{{Article détaillé}}` + ses 6 modules Lua listés, non portable ; Fandom `{{Principal}}` de Hunter × Hunter FR, une ligne, portable) dans les aperçus, avec crédits, licences, rendus comparés (loupe disparaît sur mobile Wikipédia — prouvé par les feuilles de style réelles), zips refaits, 60/60.
11. **Intermèdes** : palmarès The Best de mémoire (jusqu'à 2024 ; l'édition 2025 déclarée hors mémoire, refusée par honnêteté, deux essais identiques) ; explication de la méthode de mémoire (entraînement + notes de session) ; explication du choix HTML vs Markdown ; CAN 2025 connue via l'entraînement.
12. **Tour 111 (dernier code app)** : tableaux markdown complets dans l'Atelier (§3).
13. **Après le tour 127** : recherche « catégories Fandom = tags ? » (confirmé : outil de navigation, index auto depuis les tags ; Help:Categories + Help:DynamicPageList récupérés en intégral) ; construction des aperçus catégorie mobile/web ; **nettoyage « zone A » validé par lui** (36 fichiers + work/solo supprimés, 128,2→123,2 Mo) puis suppression des deux zips des modèles sur son ordre (→ ~119-120 Mo). Restent non approuvés : zone C (scrape/cmp/toctest/wayback ~32 Mo) et zone B (atelier-v7-corrige, référence conservée).
14. **Recherches « catégories et pages-listes »** : catégories Fandom = tags confirmés (Help:Categories) ; DynamicPageList récupérée en intégral (activée à la demande) ; codes réels des pages-listes : Hunterpedia (modèles-galeries) et **FMA** (tabber + `{{Char}}`, sources dans `work/page-categorie/`) ; page principale réelle de HxH FR + Help:Main page/column tags + Mobile Main Page dépréciée (sources dans `work/page-accueil/`). Aperçus livrés : catégorie, liste, accueil (mobile + web chacun).

## 8. Ce qui reste à faire / en attente de réponse

- Workspace : 120,4 Mo (marge ~7,6 Mo) après le nettoyage zone A validé. Si besoin de marge : zones C (~32 Mo, données re-téléchargeables) et B (v7-corrige, référence) — rien sans son OK.
- **Le dossier World Anvil** : il a dit « c'est pas ce que j'ai demandé » sans préciser. Deux questions posées (voulait-il la réponse dans le chat ? de vraies captures ?) : **sans réponse.** À reprendre avec lui.
- Son test de l'option A « Article détaillé » (tour 125) : garder ou retirer ? **Pas de réponse.**
- Ajouter la ligne `{{Principal|…}}` aux fichiers du modèle Fandom (proposé tour 127) : **pas de réponse.**
- **Options anciennes jamais tranchées** (à ne PAS traiter sans lui) : garder « Bonsoir, Michaz » ? retirer la tapisserie ? paysage fantasy Mondes (refus 2×, redemander avant de régénérer) ? couleur catégorie Artefacts ? garder le gras `#f4f1ef` ? garder l'option A ? séparer le halo des braises ? descriptions Edenia/Arcana (tour 105 : noms seulement, tranché) ; tourn-100 options diverses.
- Ajouter la capture Udanland (tableau de bord World Anvil de l'utilisateur) au dossier : proposé, sans réponse.

## 9. Préférences esthétiques confirmées (chacune avec le code qu'elle concerne — aucune déduction)

### Sur l'Atelier — `resultat/atelier-index.html` (le code principal)
- Palette : fond `#141519`/`#171310`, panneaux sombres, or `#eebf4d` réservé aux liens et actions (tour 120), catégories colorées (§3).
- Titres : Cinzel pour le titre d'article (27px), Barlow Condensed pour les h2 (31.9px) — confirmé tours 120-121.
- Il aime : les cartes anguleuses (coins droits pour les mondes, tour 112), les braises d'ambiance UNIQUEMENT sur les 4 vues de liste (tour 118), les fonds plats `#17171a` pour Articles/Catégories/Épinglés (tour 117), l'ordre de l'accueil (tours 107-111), la salutation « Bonsoir, Michaz » conservée (mais la question « la garder ? » reste ouverte).
- Il n'aime PAS (confirmé par rejet, sur CE code) : les barres verticales à côté des h2 (tour 122), les soulignements de liens (tour 120), un titre de section avant l'infobox (tour 121), le fond v7 en remplacement de l'app (tour 102).
- **Non confirmé sur l'Atelier** : ses goûts de fonds d'écran (deux refus sans commentaire au tour 114, pour Mondes/l'accueil) ; séparer le halo des braises (tour 106, sans réponse) ; la couleur de la catégorie Artefacts (tour 120, sans réponse) ; garder le gras `#f4f1ef` (tour 122, sans réponse).

### Sur la page Influences — `resultat/wiki-influences-fusion.html` (code secondaire, autonome)
- Corps DM Sans 17.6px `#e6e6e6`, titres Barlow Condensed, tons coral `#ff7a5c` / violet `#b57bff` / or `#ffc24a` / cyan `#4fd6e0`, barre collante (tours 120-122 — ces choix ont aussi été portés sur les SECTIONS de l'Atelier, pas l'inverse).
- **Ne jamais placer un titre de section avant l'infobox dans l'Atelier** — règle née de la comparaison avec cette page (tour 121).

### Sur les aperçus Fandom — `resultat/modele-wiki-fandom/apercu-*.html` (démos comparatives, pas l'app)
- Titres repliables : VIEUX design Fandom, sans cartes arrondies (tour 27).
- JAMAIS de mélange Wikipédia/ordinateur dans le look Fandom mobile ; baser le rendu sur SES captures d'écran (tour 58).
- Deux aperçus distincts, mobile (412px) et web (tour 61).

### Sur les modèles pour vrais wikis — `resultat/modele-wiki*/` (wikicode, pas du code d'app)
- Code EXACT réel exigé, crédité (tour 127) ; rien d'inventé.

### Transverse (tous les livrables)
- Captures et images de test en JPEG plutôt que supprimées (tour 75) ; toute image des livrables ouvrable en visionneuse FLB (tour 64) ; chaque modification commentée « tour N » et sw.js re-versionné (rituel de l'Atelier) ; aucun livrable supprimé sans son OK.
- **Non confirmé transverse** : pourquoi le dossier World Anvil ne convenait pas ; s'il veut un jour écrire le récit (vue « Recueil ») ou rester sur le lore.

## 10. Divers utiles pour la reprise

- **Environnement** : les paquets ne survivent pas aux réinitialisations (Playwright à réinstaller : `pip install -q playwright && python3 -m playwright install chromium`). `node_modules` non persisté (npm install avant tout build Vite dans `work/merged`). Fichiers lourds : penser au plafond 128 Mo ; convertir les captures en JPEG.
- **Sites bloqués** : Fandom (403 hors api.php), worldanvil.com (403 ; passer par des lecteurs externes). Wikipédia et api.php Fandom passent.
- **Le rituel de rebuild complet** est documenté dans la mémoire de travail (ordre des builders, inject.py FLB, rezips, test 60).
- **Ton à tenir avec lui** : direct, honnête (dire « je ne sais pas »), options numérotées, réponses courtes en français, jamais de décision silencieuse. Il apprécie les explications de méthode (« comment tu as fait et pourquoi ») — plusieurs tours entiers y ont été consacrés.
