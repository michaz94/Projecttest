# Projecttest — Nexus Wiki, benchmarks et projet Edenia

Dépôt de recherche et de développement : application **Nexus Wiki** (Vite + React),
benchmarks d'œuvres (notes, corpus, classements), projet créatif **Edenia**,
analyses Rule34 et sources historiques (*Dictionnaire infernal*, 1825).

## Arborescence

```
.
├── src/                          # Application Nexus Wiki (Vite + React + Tailwind)
├── index.html, package.json, vite.config.ts, tsconfig.json
├── atelier-app/                  # Atelier Fandom : exports, modèles wiki, templates
│   ├── export-1/                 #   Atelier V7, influences, visionneuse
│   ├── export-2/                 #   Modèles wiki + aperçus HTML
│   ├── export-3/                 #   Captures, audit, recherches
│   ├── exports-txt/              #   Dumps texte volumineux (1,6 à 13 Mo)
│   ├── fandom-template/          #   Template Fandom (extrait du ZIP)
│   └── shonen-manga-structuring-app/  # Snapshot ancien de l'app Next (voir myanimelist)
├── benchmark-oeuvre/             # Benchmarks notes / corpus / classements
│   ├── docs/                     #   Analyses et synthèses (.md)
│   ├── data/                     #   Données (.csv, .json, .xlsx)
│   ├── scripts/                  #   Scripts d'analyse (.py)
│   ├── myanimelist/              #   App Next.js + PostgreSQL (catalogue MAL)
│   ├── radiant/                  #   Radiant : rapports, données, scripts
│   ├── red-hood/                 #   Red Hood : docs/, data/, chapter/ (scans c001)
│   ├── seigneur-des-anneaux/     #   LOTR : data/, sources/, scripts/, rapports/
│   └── stormlight-archives/      #   Stormlight : critiques
├── dictionnaire-infernal/        # Scans 1825 (tomes 1 et 2) + extraits Markdown
├── docs/
│   ├── analyses/                 #   Analyses critiques (audience empruntée, Worm…)
│   ├── influences/               #   Frises d'influences (v1/v2/v3), relations, test-page.html
│   └── edenia/                   #   Projet Edenia : fiches, carnet de bord, structures…
│       ├── exports-txt/          #     Dumps workspace volumineux
│       └── divers-edenia-atelier-classement/  # Snapshot (atelier_test, classement, maj_depot)
└── rule34/                       # Analyses Rule34 / Danbooru / TierMaker
    ├── scripts/                  #   Scripts Python
    ├── data/                     #   CSV de classements et sélections
    ├── docs/                     #   Notes et classements (.md)
    ├── personnage-r34/           #   Handoff + page HTML (18 Mo)
    └── outil-tags-r34/           #   Outil tags complet (extrait du ZIP, .csv.gz conservés)
```

## Lancement

### Nexus Wiki (racine)

```bash
npm install
npm run dev     # développement
npm run build   # build (fichier unique via vite-plugin-singlefile)
```

### MyAnimeList — app Next.js (`benchmark-oeuvre/myanimelist/`)

```bash
cd benchmark-oeuvre/myanimelist
npm install
npm run dev
```

Nécessite une base PostgreSQL (`DATABASE_URL`, voir `drizzle.config.json`).
Le dossier `src/` a été restauré depuis le ZIP `shonen-manga-structuring-app (2).zip`
(l'upload initial n'avait conservé que les configs et `scripts/`).

### Autres snapshots

- `atelier-app/fandom-template/` : template Vite/Fandom (version antérieure de l'app racine).
- `atelier-app/shonen-manga-structuring-app/` : version **ancienne** de l'app Next
  (la version à jour est `benchmark-oeuvre/myanimelist/`).

## Notes de réorganisation (nov. 2026)

- **Nommage** : tout est en minuscules, sans espaces ni accents
  (`Benchmark Oeuvre` → `benchmark-oeuvre`, `Seigneur Des Anneaux` → `seigneur-des-anneaux`,
  `Personnage r34` → `personnage-r34`, `Pdfmd` → `dictionnaire-infernal`,
  `Others` → `docs/edenia/` + `rule34/`). Les fichiers de code extraits des ZIP
  conservent leur casse d'origine (`App.tsx`, `page.tsx`…).
- **Doublons supprimés** (contenu vérifié identique) : `analyse_critique_audience_empruntee (1).md`,
  `synthese_red_hood (1).html`, `critiques_senscritique_voie_des_rois (2).md`,
  `Others/uploads/…` (doublon de `fiche_creatures…`), `influences-atelier.txt`
  (identique au `.md`), plus 12 fichiers junk d'1 à 3 octets aux noms tronqués
  (`Kk`, `€tr`, `D`, `Ed`, `€ss`, `Dd`, `G`, `Reff`, `Hh`, `Tr`, `Bh`, `Chapter/D`).
- **ZIP dézippés** (10 + 1 imbriqué, aucun ZIP restant) : les contenus déjà présents
  en clair n'ont pas été dupliqués — seuls les fichiers absents ou différents ont
  été extraits (`relations_influences_v1.csv/json`, version ZIP de l'analyse LOTR,
  `src/` de MyAnimeList). Les deux ZIP Radiant ont été fusionnés dans `radiant/`
  (`LISEZMOI_donnees.md` pour le second LISEZMOI).
- **Versions conservées** : `frise_arbre_influences_v1/v2/v3.md` (v3 = dernière),
  `relations_influences_v1/v2`, snapshots dans `divers-edenia-atelier-classement/maj_depot/`.
- **Gros fichiers conservés dans Git** (au cas par cas, ~415 Mo au total) :
  `dictionnaire-infernal/*.pdf` (17–21 Mo), `docs/edenia/exports-txt/workspace_sans_github-1.txt` (21 Mo),
  `rule34/personnage-r34/top-feminin-rule34-ia-bot.html` (18 Mo),
  `atelier-app/exports-txt/export-5-sources-work.txt` (13 Mo),
  `docs/edenia/edenia.html` (8,7 Mo), `benchmark-oeuvre/red-hood/docs/posts_scores_commentaires.html` (5,1 Mo),
  `benchmark-oeuvre/seigneur-des-anneaux/data/goodreads_communaute_3_raw.json` (5,3 Mo).
  Si le dépôt devient trop lourd, envisager Git LFS ou un stockage externe pour ces fichiers.
