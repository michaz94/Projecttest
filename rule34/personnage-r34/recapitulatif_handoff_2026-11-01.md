# Récapitulatif de passation (Handoff IA) — Session du 01/11/2026

Ce document résume l’intégralité des règles permanentes, de l’état des fichiers livrés et des décisions techniques prises durant la session, afin de poursuivre le travail avec une autre IA sans perte de contexte ni erreur méthodologique.

---

## 1. Règles permanentes & contraintes strictes de l’utilisateur

1. **Langue & posture** :
   - Toujours répondre en **français clair et direct**.
   - **« N’invente rien »** : tout chiffre, rang ou constat doit reposer sur une source vérifiée ou un calcul reproductible.
   - Ne pas écrire de fiction à la place de l’utilisateur ; prouver l’utilité de l’IA par des outils concrets d’audit, de tri, de croisement et de visualisation.
   - Toujours distinguer explicitement la provenance d’une affirmation : **`(U)`** (dit par l’utilisateur), **`(YAML)`** (`fiches_references_projet.yaml`, seule source d’autorité canonique pour *Edenia*), **`(dépôt)`** (fichiers du dépôt) et **`(IA)`** (inférence/sélection de l’IA).
   - Quand l’utilisateur dit *« Rien pour l’instant »*, ne lancer aucune tâche non demandée.

2. **Plafonds anti-spoilers absolus (ne jamais dépasser, même par allusion)** :
   - **Chainsaw Man** : **≤ Tome 1 (chapitres 1 à 7)** — interdiction absolue de mentionner la vraie nature de Makima ou de Reze, ou tout événement ultérieur.
   - **NieR: Automata** : interdiction absolue de mentionner la désignation cachée de 2B.
   - **The Last of Us** : interdiction absolue sur *Part II*.
   - **Overwatch (2026 — *Reign of Talon*)** : ne jamais commenter le lore 2026 ni le personnage `Domina` (sa `note` reste volontairement vide `""`).
   - **Jujutsu Kaisen** : ≤ Épisode 59 (fin saison 2).
   - **One Piece** : ≤ Chapitre 984.
   - **Radiant** & **Fabula Fantasia** : ≤ Tome 6.
   - **Worm** : ≤ Arc 9.
   - **Archives de Roshar (Stormlight)** : ≤ *La Voie des Rois* chapitre 15 + 3 interludes.
   - **Yu Yu Hakusho** : ≤ Chapitre 129 / Épisode 78.
   - **Game of Thrones** : Saisons 1 à 7 uniquement.
   - **Le Nom du Vent (Kingkiller)** : ≤ Chapitre 8.
   - **La Horde du Contrevent** : ≤ Chapitres 2–3.
   - **Le Seigneur des Anneaux** : ≤ Livre II, chapitre 10.
   - **Harry Potter** : films + quelques livres.
   - **Fils-des-Brumes (Mistborn)** : rien lu (zéro spoiler).

3. **Règle d’analyse des classements de personnages** :
   - Toujours **séparer l’attrait physique / le boost morphologique ou vestimentaire** ET **le biais propre à chaque plateforme** (ex. Rule34 très orienté 3D Blender/SFM occidentale et furry vs Danbooru orienté illustration 2D animanga/gacha vs sondages lecteurs / MAL) **de la personnalité et de l’écriture**. Ne jamais interpréter un haut rang sur un site adulte comme une pure victoire d’écriture.

---

## 2. Les 3 chantiers réalisés et leurs fichiers livrables

### A. Audit du dépôt `Projecttest` & noyau *Edenia*
- **Fichier livré** : `rapport_situation_projecttest_2026-11-01.md` + dossier consolidé `edenia/` (**342/342** vérifications d’intégrité validées).
- **Règle d’autorité** : seul `edenia/fiches_references_projet.yaml` gouverne les statuts de décision du projet *Edenia* (`decide`, `envisage`, `interet`, constat personnel, etc.). Les fichiers `Edenia.html`, `inference_du_projet.md` et `classement_influences/` en découlent.

### B. Benchmark Oeuvre v3.1
- **Fichier livré** : `Benchmark-Oeuvre-v3.1.html` (~351 Ko, bundle autonome sans dépendance externe) + sources Vite dans `benchmark-astra-max/`.
- Contient le comparateur multicritère d’œuvres v3.1 et la matrice **Hadamard 668**.

### C. Application autonome `top-feminin-rule34-ia-bot.html` (~18,1 Mo, 100 % hors-ligne)
Outil principal enrichi tout au long de la deuxième moitié de la session. Il croise :
- La base historique **Années / Mois** (`P.d`, `P.my` : 2011–2026, avec/sans IA, avec/sans bots).
- L’onglet **Archétypes** (200 fiches d’archétypes majeurs avec bios sans spoilers, attributs physiques/vestimentaires et galeries d’images).
- L’onglet **`Règle SFW ★`** (**230 personnages** au total = **200 Archétypes F** + **21 Témoins F hors Archétypes** + **9 H/Autre**).

---

## 3. Spécifications exactes de l’onglet `Règle SFW ★` (à préserver impérativement)

### 3.1. Formule mathématique unifiée Danbooru (post-réforme du 25 mai 2022)
- **Pourquoi l’ancien ratio `Safebooru ÷ Danbooru` a été abandonné** :
  1. Safebooru plafonnait artificiellement ou produisait des anomalies (> 100 % ou faux 60 % sur *Overwatch* / *Toriel*).
  2. Sur Danbooru, un audit mensuel et quotidien sur `1girl` a prouvé que la **bascule vers la classification humaine native `rating:g` vs `rating:s` a eu lieu exactement le `2022-05-25`** (le taux `G / (G+S)` passe brutalement de ~33–35 % avant mai 2022 à > 51 % dès le 25 mai 2022).
  3. **Avant le 25/05/2022**, le script automatique de Danbooru bloquait en `Sensitive (rating:s)` des illustrations totalement sages dès qu’elles portaient un tag de tenue canonique comme `bodysuit` (*D.Va*), `maid` (*Rem*) ou `thighhighs` / robe fendue (*2B*). **Après le 25/05/2022**, les posts `rating:s` sont réellement suggestifs (pin-ups, maillots, sous-vêtements) et **ne doivent surtout pas** être fusionnés dans `Safe`.
- **Formule exacte appliquée aux 230 personnages** :
  $$\text{Score SFW corrigé} = \frac{G_{\text{total}} + 0{,}5 \times S_{\text{avant le 2022-05-25}}}{\text{Total Danbooru}}$$
- **Champs stockés dans `RULE_PAYLOAD.rd[tag]`** (tous issus de l’API `counts/posts.json` de Danbooru sur le tag `category=4` exact) :
  - `db` (total Danbooru), `g` (`rating:g`), `s` (`rating:s` total), `spre` (`rating:s date:<2022-05-25`), `qe` (`rating:q` + `rating:e`), `pct` (Score SFW corrigé en %), `gs` (`(g+s)/db` en %), `r34` (cumul Rule34 **sans IA ni bots**, égal à `sum(y.sbsi)` dans `P.d`), `cat`, `star`, `wit`, `tm` (`[rang_TierMaker, note]`), `ext` (sondages officiels / MAL), `note`.

### 3.2. Barre 3 couleurs remplie à 100 % sur chaque carte
Chaque carte affiche une barre empilée couvrant **exactement 100 % de `db`** avec nombres de posts et `%` :
- 🟢 **Safe (SFW corrigé)** : `(g + 0.5 × spre) / db`
- 🟡 **Sensitive net** : `(s - 0.5 × spre) / db`
- 🔴 **Q+E (Questionable + Explicit)** : `qe / db`

### 3.3. Les 4 catégories propres (0 garde-fou manuel, `RULE_CATS`)
1. **`morpho` (42 F)** — *Boost morphologique / tenue / 3D suggestive* : `< 20,5 %` SFW corrigé **ou** `≥ 50 % Q+E` (avec `db ≥ 120`).
   - Ex. : *Eve (3,5 %), Domina (5,1 %), Elastigirl (7,3 %), Emma Frost (7,7 %), Asuna BA (8,0 %), Black Cat (8,4 %), Mirko (8,5 %), Nicole (8,9 %), Squirrel Girl (10,5 %), Burnice (10,9 %), Yoruichi (11,3 % / 51,2 % Q+E), Mai Shiranui (11,8 %), Tsunade (12,3 % / 63,2 % Q+E), Raven (12,6 %), Psylocke (14,2 %), Rangiku (15,0 % / 50,3 % Q+E), Invisible Woman (15,8 %), Purah (16,3 %), Velma (21,4 % / 56,2 % Q+E)*.
2. **`ecriture` (40 F / 47 tous genres)** — *Piliers d’écriture / charisme sobre* : `≥ 45,0 %` SFW corrigé sur capteur Danbooru fiable.
   - Ex. : *Violet Evergarden (85,6 %), Hornet (72,0 %), Pomni (69,5 %), Gardevoir (64,8 %), Hatsune Miku (62,9 %), Kurisu (61,2 %), Marcille (60,1 %), Aerith (59,6 %), Riza Hawkeye (58,9 %), Maomao (58,8 %), Furina (57,6 %), Ranni (57,4 %), Frieren (56,5 %), Momo Ayase (56,5 %), Rukia (55,5 %), Zelda (53,8 %), Power (53,5 %), Kushina (53,3 %), Mikasa (50,8 %), Makima (49,4 %), Nobara (48,0 %), Artoria (47,9 %), Maki Zenin (46,8 %), Kaguya (45,7 %), Sakura (45,4 %)*.
3. **`royale` (80 F)** — *Voie royale (double moteur écriture + design attractif)* : `20,5 % à 44,9 %` SFW corrigé sur capteur fiable.
   - Ex. : *Lumine (44,6 %), Byleth F (42,5 %), Jinx (41,9 %), Hitagi (41,1 %), Nico Robin (40,9 %), Rem (39,7 %), Zero Two (39,7 %), Fern (38,5 %), D.Va (37,7 %), Mai Sakurajima (36,4 %), Ochako (36,0 %), Holo (35,9 %), Hinata (35,3 %), Raiden (34,3 %), Yor (34,0 %), Tifa (31,8 %), Nami (30,7 %), Shadowheart (28,4 %), Cynthia (27,7 %), Chun-Li (27,2 %), 2B (25,3 %), Marin (22,8 %), Übel (21,4 %)*.
4. **`biais3d` (61 F)** — *Biais de site (3D occidentale Blender/SFM, Comics, Furry ou petit échantillon `db < 250`)* : `db < 250` **ou** œuvre non-Animanga avec `R34 ÷ DB ≥ 6,5×`.
   - Ex. : *Overwatch* aligné par époque (*Juno 38,3 %, Pharah 37,5 %, Tracer 37,4 %, Sombra 37,3 %, Kiriko 36,6 %, Mercy 36,0 %* vs *Widowmaker 29,3 %*), *Resident Evil* (*Claire 44,8 %, Jill 43,8 %, Ada 40,5 %, Dimitrescu 26,6 %*), *The Witcher* (*Ciri 59,5 % / 30,0×*, *Yennefer 44,8 % / 32,3×*), *Lara Croft (21,2 % / 39,5×)*, *Loba (44,6 % / 14,8×)*, *Amy Rose (77,9 %)*, *Toriel (60,3 %)*.

### 3.4. Les 21 témoins féminins hors onglet `Archétypes` (`RULE_PAYLOAD.wl`)
- **Ne jamais les étiqueter « Hors R34 »**, car **11 d’entre elles figurent déjà dans la liste `Années` (`P.d`)** avec un badge cliquable `Années #<rang F sans IA/bot> ↗` (`RULE_PD_RK`) :
  - `artoria_pendragon_(fate)` (#70), `yennefer` (#79), `loba_(apex_legends)` (#110), `matsumoto_rangiku` (#127), `kugisaki_nobara` (#184), `uzumaki_kushina` (#188), `rem_(re:zero)` (#334), `daphne_blake` (#338), `zen'in_maki` (#346), `zero_two_(darling_in_the_franxx)` (#393), `shinomiya_kaguya` (#424).
- **10 témoins hors `P.d`** (étiquetés `★ Témoin hors liste`) :
  - `makise_kurisu`, `maomao_(kusuriya_no_hitorigoto)`, `marcille_donato`, `holo`, `riza_hawkeye`, `kusanagi_motoko`, `ubel_(sousou_no_frieren)`, `senjougahara_hitagi`, `violet_evergarden`, `sakurajima_mai`.

### 3.5. Règles d’interface (UI/UX) exigées par l’utilisateur dans `top-feminin-rule34-ia-bot.html`
- **Encadré explicatif `#rgRuleBox` (« La règle de lecture »)** : replié par défaut (`open = false`, `st.rgRuleOpen = false`).
- **Barres de filtres `Périmètre` et `Affichage`** : conserver impérativement en barres segmentées `.seg` (ne pas remplacer par des pilules multi-lignes).
- **Tri (`Trier par`)** : menu déroulant `<select id="selRgSort">` (regroupé en `★ Pertinence & Danbooru`, `Pourcentages (%)`, `Posts (volume)`, `Ratio`) associé à un **bouton séparé d’inversion d’ordre `#btnRgDir`** (`↓ Décroissant` / `↑ Croissant`, état `st.rgAsc`).
- **Visionneuse photo (`#imgLb`)** : fermer une image (croix, clic fond, touche Échap ou bouton Retour mobile) ne doit **jamais** recharger la page, relancer `render()`, ni faire sauter la position de défilement (`scrollY`).

---

## 4. Galeries d’images intégrées (`P.ai` / `AIMGS`) & conventions d’ajout

- **État actuel** : **82 personnages illustrés** (total **165 images** embarquées en `data:image/webp;base64,...` dans `P['ai']`).
- **Format d’encodage** :
  - Pour une image avec canal alpha (`RGBA` ou `P` avec transparence, `amin < 245`) : recadrage serré sur la boîte englobante `alpha > 4` avec `padding = 6px`, redimensionnement `LANCZOS` à `max_dim = 760px`, sauvegarde WebP `RGBA` (`quality = 84`, `alpha_quality = 90`, `method = 6`).
  - Pour une image opaque (`RGB`) : conserver en `RGB` (ne pas tenter de détourage automatique agressif sur fond blanc/gris si cela crée un halo crénelé, ex. *Elizabeth*), `max_dim = 760px`, WebP `quality = 84`.
- **Règles d’ordre dans chaque galerie personnage (`AIMGS[tag]`)** :
  1. **Mettre les rendus `full-body` (en pied, de la tête aux chaussures) sur fond transparent (`RGBA`) en premier (`index 0`)**.
  2. **Privilégier le médium d’origine lorsqu’il est en couleur** (ex. illustration manga couleur de Ryoko Kui en n°1 pour *Marcille* et *Frieren*, rendu 3D jeu officiel en n°1 pour *Overwatch 2*, *Marvel Rivals*, *Resident Evil*, *The Witcher 3*, etc. ; à l’inverse, une planche manga noir & blanc passe après les visuels couleur).
  3. Toujours **vérifier visuellement** les images fournies plutôt que de se fier aveuglément aux noms de fichiers web (ex. un fichier nommé `Nami-PNG-File.png` représentait en réalité *Nico Robin*).
- **Attention aux tags exacts dans `P.ai`** :
  - Mirko = `miruko` (et non `mirko`).
  - Maki Zenin = `zen'in_maki` dans `Règle SFW ★` (`zenin_maki` dans `P.d`).
  - Yennefer = `yennefer` dans `P.ai` / `P.d` / `RULE_PAYLOAD` (mais son tag Danbooru `category=4` est `yennefer_of_vengerberg`).
- **Liste complète des 82 tags déjà illustrés dans `P.ai`** :
  `ada_wong`, `aether_(genshin_impact)`, `akali`, `alcina_dimitrescu`, `android_21`, `anna_(frozen)`, `ashe_(overwatch)`, `ayase_momo`, `belle_(zenless_zone_zero)`, `black_cat_(marvel)`, `brigitte`, `burnice_white`, `byleth_(fire_emblem)_(female)`, `catwoman`, `chun-li`, `ciri`, `claire_redfield`, `d.va`, `domina`, `draco_malfoy_(redteneri)`, `elizabeth_comstock`, `ellen_joe`, `emma_frost`, `frieren`, `furina_(genshin_impact)`, `gwen_stacy`, `harley_quinn`, `ino_yamanaka`, `invisible_woman`, `jane_doe_(zenless_zone_zero)`, `jill_valentine`, `jubilee`, `juno_(overwatch)`, `juri_han`, `kiriko_(overwatch)`, `kitagawa_marin`, `kuchiki_rukia`, `kugisaki_nobara`, `lisa_(genshin_impact)`, `loba_(apex_legends)`, `lumine_(genshin_impact)`, `luna_snow`, `magik_(illyana_rasputin)`, `makima_(chainsaw_man)`, `marcille_donato`, `matsumoto_rangiku`, `mei_(overwatch)`, `mercy`, `miruko`, `mona_(genshin_impact)`, `nami_(one_piece)`, `nico_robin`, `nicole_demara`, `ochako_uraraka`, `pharah`, `power_(chainsaw_man)`, `princess_zelda`, `psylocke`, `purah`, `raiden_shogun`, `rapunzel`, `rebecca_(edgerunners)`, `rem_(re:zero)`, `remielle_dan`, `samsung_sam`, `shenhe_(genshin_impact)`, `sombra`, `spider-man`, `squirrel_girl_(marvel)`, `the_twins_(atomic_heart)`, `tifa_lockhart`, `tracer`, `uzumaki_kushina`, `widowmaker`, `xianyun_(genshin_impact)`, `yae_miko`, `yelan_(genshin_impact)`, `yennefer`, `yor_briar`, `yorha_2b`, `zen'in_maki`, `zhu_yuan`.

---

## 5. Pièges techniques API à connaître (pour éviter tout blocage)

1. **API Danbooru (`danbooru.donmai.us`)** :
   - Ne **jamais** utiliser `name_or_alias_matches` ni `tag_aliases.json` (non indexés → `HTTP 500` / timeout). Utiliser `tags.json?search[name_comma]=...` ou `autocomplete.json?search[query]=...&search[type]=tag_query` en filtrant `category == 4` (personnage).
   - Ne **jamais** paralléliser les requêtes `counts/posts.json` (`HTTP 429`). Utiliser une seule connexion `HTTPSConnection` keep-alive séquentielle avec `~0.12s` de pause par appel.
2. **API Rule34** :
   - `api.rule34.xxx` requiert désormais une authentification pour `dapi`, mais les cumuls propres **sans IA ni bots** sont déjà intégralement présents dans `P.d` (`sum(v.sbsi for v in d['y'].values())`), et `ac.rule34.xxx/autocomplete.php?q=...` reste public pour vérifier l’existence d’un tag.
3. **Modification programmatique de `top-feminin-rule34-ia-bot.html`** :
   - `const P={...};` et `const RULE_PAYLOAD={...};` sont des objets JSON sur une ligne dans la balise `<script>`. Toujours parser/réécrire proprement en Python (`json.loads` / `json.dumps(..., ensure_ascii=False, separators=(',',':'))`), puis extraire le `<script>` et valider avec `node --check` avant de livrer.
