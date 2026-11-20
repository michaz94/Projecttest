# Seigneur des Anneaux (*La Communauté de l'Anneau*) : scripts, rapports, données

## scripts/ (à lancer depuis un dossier qui contient aussi `data/`)
- `collecter_goodreads_communaute.py` : 1★ et début des 2★ (API Goodreads).
- `completer_goodreads_2_etoiles.py` : reprise des 2★.
- `collecter_goodreads_note.py N [NEWEST|OLDEST] [reprendre]` : une note à la fois (utilisé pour les 3★).
- `collecter_top30_4_5.py` : les 30 avis les plus en avant à 5★ et 4★.
- `collecter_senscritique_communaute.py` : critiques SensCritique.
- `collecter_senscritique_voie_des_rois.py` : critiques SensCritique de *La Voie des rois 1* (pas le Seigneur des Anneaux ; son JSON n'est pas inclus car il contient des spoilers).
- `analyser_critiques_communaute.py` : thèmes, filtre anti-spoil, comptages.

## rapports/
- `critiques_communaute_anneau.md` : le rapport principal.
- `avis_top30_4_5_etoiles.md` et `_fr.md` : avis 4★/5★, originaux puis traduits avec éloges et reproches.
- `structures_narratives_comparees.md` : contient les parties A et D sur la *Communauté* (et d'autres œuvres).

## data/ (avis bruts, avec noms d'utilisateurs ; certains avis contiennent des spoilers)
- `goodreads_communaute_1_2_raw.json` (781 avis 1★, 2 119 avis 2★), `goodreads_communaute_3_raw.json` (6 968 avis 3★), `goodreads_communaute_top30_4_5_raw.json`, `senscritique_communaute_raw.json` (36 critiques).

## sources/
- Le PDF de la *Communauté* que tu as fourni (ne pas le publier : droits d'auteur).

## Non inclus, mais qui mentionnent le Seigneur des Anneaux
`fiches_references_projet.yaml`, `VUE_references_projet.md`, `fiches_oeuvres_v3.md`, `uploads/fiches_oeuvres (2).md` : quelques lignes seulement chacun, parmi d'autres œuvres.
