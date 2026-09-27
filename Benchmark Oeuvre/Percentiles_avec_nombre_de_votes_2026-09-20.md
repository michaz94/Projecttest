# Effet du nombre de votes sur les percentiles — 2026-09-20

## Réponse courte

**Oui, mais le résultat dépend de ce que signifie « prendre le nombre de votes en compte ».** Deux calculs complémentaires ont été testés.

1. **Percentile pondéré par les votes** : chaque notation devient une unité. Cela change les seuils et percentiles, mais une note brute supérieure reste toujours devant une note brute inférieure. Ce calcul mesure surtout où se concentre la popularité.
2. **Score ajusté pour robustesse** : les moyennes fondées sur peu de votes sont ramenées vers la moyenne du corpus. Cette méthode peut réellement changer l’ordre des œuvres.

**Correction du 27/09/2026** — retrait de l'entrée « ONE PIECE 116 » (Goodreads), chapitre de l'édition originale et non un tome relié. La population Goodreads passe de 600 à 599 œuvres ; les paramètres `C` et `m`, les percentiles pondérés, les scores ajustés et les moyennes par cycle ont été recalculés. Détail : `Note_retrait_One_Piece_116_2026-09-27.md`.

## Paramètres du test de robustesse

`score ajusté = (v × R + m × C) / (v + m)`

- `R` : note affichée ; `v` : nombre de notations ; `C` : moyenne simple de la plateforme ; `m` : nombre médian de notations du corpus.
- Goodreads : C = 4,401, m = 5814,0 votes.
- SensCritique : C = 7,113, m = 211,0 votes.

## Changements remarquables

- Goodreads : *Words of Radiance* devient n°1 ajusté ; *One Piece* 103 passe du rang brut 1 au rang ajusté 39.
- Goodreads : *Worm* passe de P89,65 à P90,57 ajusté ; ses 10 769 notes dépassent le volume médian du corpus.
- SensCritique : *Worm* passe de P99,92 à P58,64 ajusté, soit du rang 1 au rang 247, parce que son 9,7 repose sur seulement 11 notes.
- SensCritique : *Le Trône de fer — Intégrale 3* devient n°1 ajusté avec 8,5 sur 3 965 notes.

## Effet moyen par cycle

| Plateforme | Cycle | P brut moyen | P ajusté moyen | Écart |
|---|---|---:|---:|---:|
| Goodreads | Stormlight Archive | 80,15 | 82,15 | +2,00 |
| Goodreads | A Song of Ice and Fire | 47,26 | 47,86 | +0,60 |
| Goodreads | Harry Potter | 77,33 | 87,66 | +10,33 |
| Goodreads | Kingkiller Chronicle | 78,55 | 90,73 | +12,19 |
| Goodreads | The Witcher | 8,98 | 2,47 | −6,51 |
| Goodreads | Arthur fondateur | 1,24 | 2,59 | +1,35 |
| SensCritique | Stormlight Archive | 92,90 | 87,16 | −5,74 |
| SensCritique | A Song of Ice and Fire | 92,15 | 97,67 | +5,52 |
| SensCritique | Harry Potter | 75,85 | 90,50 | +14,65 |
| SensCritique | Kingkiller Chronicle | 95,81 | 98,57 | +2,77 |
| SensCritique | The Witcher | 64,15 | 74,01 | +9,85 |
| SensCritique | Arthur fondateur | 68,48 | 52,87 | −15,61 |

## Attention

Le percentile pondéré par les votes ne doit pas être appelé un classement de qualité : les œuvres très populaires dominent mécaniquement la population. Le score ajusté est préférable pour tester la robustesse, mais le choix de `m` reste une convention et doit être présenté comme une analyse de sensibilité.