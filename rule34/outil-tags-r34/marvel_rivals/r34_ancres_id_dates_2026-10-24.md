# Rule34.xxx — correspondance ID ↔ date d'upload (relevé du 24/10/2026)

r34 n'a pas de métatag `date:` et son API (dapi) demande une authentification. En revanche, les ID de post sont attribués dans l'ordre chronologique, et la recherche `id:<N` fonctionne.

## Ancres vérifiées
- **Posts « milestone »** : dates lues dans les premiers commentaires.
- **Autres posts** : ligne la plus ancienne de `index.php?page=history&type=tag_history&id=N`.

| ID | Date d'upload |
|---|---|
| 7 000 000 | 2022-11-18 (historique des tags) |
| 8 000 000 | 2023-05-30 |
| 9 000 000 | 2023-11-17 |
| 10 000 000 | 2024-04-21 |
| 11 000 000 | 2024-08-20 |
| 11 945 800 | 2024-12-08 07:13 (historique des tags) |
| 12 481 632 | 2025-02-05 (historique des tags) |
| 13 000 000 | 2025-03-30 |
| 14 000 000 | 2025-07-03 |
| 15 000 000 | 2025-10-02 |
| 15 730 300 | 2025-12-06 09:49 (historique des tags) |
| 16 000 000 | 2025-12-30 |
| 18 000 000 | 2026-07-04 |
| 19 000 000 | 2026-10-10 |
| ~19 130 000 | ID max observé le 24/10/2026 |

## Bornes utilisées
| Date | ID borne | Méthode |
|---|---|---|
| 2023-12-06 | 9 122 000 | interpolation 9M→10M (~6,4 k/jour) |
| 2024-12-06 (lancement) | 11 927 000 | ancre 11 945 800, recalée de −2 jours |
| 2025-12-06 | 15 730 000 | ancre vérifiée |
| 2026-07-10 (Jubilee) | 18 057 000 | interpolation 18M→19M |

Précision estimée : ± 1 à 2 jours par borne.

## Limites
- **Effectifs** : effectif = pid de la dernière page + 21 (± 21).
- **Posts supprimés** : ils ne sont pas comptés, mais leurs ID existent quand même. La normalisation « par million d'ID » n'est donc qu'une approximation du volume total du site.
- **Psylocke** (corrigé le 24/10, piste donnée par l'utilisateur) : avant le jeu, le tag principal était `psylocke_(kwannon)`. Le tag simple `psylocke` ne comptait qu'environ 105 posts avant le 06/12/2024 contre environ 1 911 pour `psylocke_(kwannon)`, et tous les posts `psylocke` de cette période portaient aussi `psylocke_(kwannon)` (même nombre de résultats pour l'union). La série utilise donc l'union `( psylocke ~ psylocke_(kwannon) )`. Environ 99 % des posts du tag simple `psylocke` sont postérieurs au lancement du jeu.
