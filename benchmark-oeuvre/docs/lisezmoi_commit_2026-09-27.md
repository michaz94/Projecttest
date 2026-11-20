# Paquet de commit — correction « One Piece 116 » (27/09/2026)

**Mode d'emploi** : extraire ce zip **à la racine du dépôt**. Les dossiers `livrables/` et `work/`
se superposent à l'arborescence existante ; aucun autre fichier n'est touché.

## A. Cœur de la correction (à committer)

### Données recalculées — 11 fichiers

| Fichier | Avant | Après |
|---|---:|---:|
| `percentiles_tous_corpus_principaux_2026-09-22` (csv, json, xlsx) | 1 202 lignes — 603 GR + 599 SC | **1 201** — 602 GR + 599 SC |
| `percentiles_tous_corpus_principaux_2026-09-20` (csv, json, xlsx) | 1 196 lignes — 600 GR + 596 SC | **1 195** — 599 GR + 596 SC |
| `percentiles_avec_nombre_votes_2026-09-22` (csv, json, xlsx) | 1 202 lignes | **1 201** |
| `percentiles_avec_nombre_votes_2026-09-20` (csv, xlsx) | 1 196 lignes | **1 195** (+ feuille « Cycles » recalculée) |

Le côté SensCritique est inchangé. Paramètres du score robuste réestimés :
Goodreads `C = 4,40151`, `m = 5 892,5` (fichiers du 22/09).

### Documentation — 7 fichiers

| Fichier | Nature |
|---|---|
| `Note_retrait_One_Piece_116_2026-09-27.md` | **nouveau** — note de correction détaillée |
| `Percentiles_tous_corpus_principaux_2026-09-22.md` | encadré de correction, N=602 |
| `Percentiles_tous_corpus_principaux_2026-09-20.md` | encadré de correction, N=599 (560 mangas) |
| `Percentiles_avec_nombre_de_votes_2026-09-22.md` | encadré de correction, nouveaux `C` et `m` |
| `Percentiles_avec_nombre_de_votes_2026-09-20.md` | encadré + moyennes par cycle recalculées |
| `Analyse_complete_Seigneur_des_anneaux_Goodreads_SensCritique_2026-09-22.md` | section 5 : rangs désormais sur 602 |
| `work/corriger_retrait_op116.py` | **nouveau** — script de correction rejouable |

Chaque classeur `.xlsx` porte aussi une ligne « Correction 27/09/2026 » dans l'onglet Synthèse.

## B. Documents du 27/09 joints (facultatif)

À retirer du commit s'ils y sont déjà — ils ne font pas partie de la correction des percentiles :

- `livrables/Notes_SensCritique_11_oeuvres_principales_2026-09-27.md`
- `livrables/Analyse_complete_Stormlight_Archive_Goodreads_2026-09-27.md`
- `livrables/repartition_deux_oeuvres_2026-09-27.zip`

## C. Message de commit suggéré

```
Percentiles : retrait de One Piece 116 (chapitre, pas un tome relié)

- Retire l'entrée Goodreads « ONE PIECE 116 » du corpus principal : chapitre de
  l'édition originale, sans fiche SensCritique (la série s'arrête au tome 115).
- Recalcule percentiles, rangs et scores ajustés Goodreads de la plateforme :
  603 -> 602 œuvres (fichiers du 22/09), 600 -> 599 (fichiers du 20/09).
- Réestime les paramètres du score robuste : C = 4,40151 ; m = 5 892,5.
- Met à jour les notes de synthèse et ajoute la note de correction détaillée.
- SensCritique inchangé ; Black Clover 37-38 et Hunter x Hunter 39 conservés
  (fiches SensCritique existantes mais moins de 5 notes).
```

## D. Ce qui n'est pas dans ce paquet

- `work/backup_avant_retrait_op116/` — sauvegardes avant correction, inutiles au commit (Git fait office d'historique).
- `work/one_piece_goodreads_2026-09-19.csv` — relevé source laissé **intact** volontairement (la ligne `volume = 116` doit être exclue à toute régénération future).
- Le reste de `livrables/` et `work/` — hors périmètre de cette correction.
