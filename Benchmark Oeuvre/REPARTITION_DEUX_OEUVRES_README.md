# Répartition des notes Goodreads — deux ensembles

**Date du zip :** 2026-09-27
**Périmètre :** évolution de la moyenne + répartition histogramme (1–5 étoiles) + mécanique des notes, sur deux corpus :

1. **Stormlight Archive — T1 + T2** (*The Way of Kings*, *Words of Radiance*)
2. **Le Seigneur des anneaux — T1 + T2 + T3** (*Fellowship*, *Two Towers*, *Return of the King*)

## Contenu du zip

### 1. Rapports (.md)

- `Analyse_complete_Stormlight_Archive_Goodreads_2026-09-27.md` — analyse consolidée TWoK + WoR (moyenne + répartition + mécanique).
- `Analyse_complete_Seigneur_des_anneaux_Goodreads_SensCritique_2026-09-22.md` — analyse complète Fellowship + Two Towers + Return of the King (Goodreads /5 et SensCritique /10).

### 2. Données de séries historiques (moyenne par date, par palier de notes)

- `evolution_note_the_way_of_kings_repartition_2026-09-22.csv`
- `evolution_note_words_of_radiance_repartition_2026-09-22.csv`
- `evolution_note_fellowship_goodreads_2026-09-22.csv`
- `evolution_note_two_towers_goodreads_2026-09-22.csv`
- `evolution_note_return_king_goodreads_2026-09-22.csv`

### 3. Répartitions d'histogrammes (5★ / 4★ / 3★ / 2★ / 1★ par date)

- `repartition_fellowship_goodreads_2026-09-22.csv`
- `repartition_two_towers_goodreads_2026-09-22.csv`
- `repartition_return_king_goodreads_2026-09-22.csv`

### 4. Mécanique des notes

- `mecanique_notes_lotr_goodreads_2026-09-22.csv` — décomposition 5★/4★ et scénarios pour les trois tomes LOTR.

## Conventions

- Plateforme Goodreads sur /5, SensCritique sur /10 ; jamais fusionnées.
- Moyennes Goodreads arrondies à deux décimales par la plateforme ; les valeurs à cinq décimales sont reconstruites à partir des histogrammes 1–5 étoiles.
- Histogrammes dont le total ne correspond pas au compteur principal Goodreads sont marqués comme « exclu » dans les `.md`.
- Captures Internet Archive utilisées pour la reconstruction historique ; dates et URL exactes dans les `.md`.
