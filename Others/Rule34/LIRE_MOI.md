# Récapitulatif et reprise de ton outil

## Ton objectif
Comparer les personnages les plus représentés sur Rule34.xxx d’après le **nombre de publications associées aux tags**, sans afficher ni télécharger d’images. Ce n’est pas un classement des recherches, des vues ou des visiteurs.

## La méthode retenue
Nous avons essayé une API et Termux, puis retenu **Google Colab sur Android**, plus pratique pour toi. Le notebook final n’utilise **aucune clé API**. Il lit les tableaux publics de tags triés par compteur décroissant, garde les entrées étiquetées **Character** par le site et crée des CSV dans un ZIP.

`pid` est un décalage : page 1 = pid 0 ; page 88 = pid 1740 ; page 108 = pid 2140.

Les catégories générales restent incluses à ta demande. Il ne faut donc pas confondre nombre de tags et nombre de personnes individuelles. Les alias ne sont pas fusionnés.

## Dernier résultat conservé
La collecte sauvegardée date du **27 septembre 2026**. Elle s’est terminée à la **page 107**, avec **42 tags Character**. Après exclusion manuelle des catégories générales et des tags d’espèces Gardevoir, Lucario et Renamon, nous avions retenu **24 personnages individuels nommés**, dont **21 féminins** et 3 masculins (Sonic, Naruto et Link).

Rouge the Bat était 16e dans le classement des tags et 4e dans la sélection féminine, avec **45 037 publications**. Ces chiffres sont historiques, pas une nouvelle vérification du site.

## Fichiers disponibles
- `Outil_tags_reprise_107_Colab.ipynb` : notebook prêt à importer dans Colab.
- `collecteur_tags.py` : même logique de collecte en Python, utilisable hors Colab.
- `classement_42_tags_2026-09-27.csv` : classement complet conservé.
- `classement_21_personnages_feminins_2026-09-27.csv` : sélection féminine, noms et univers.
- `rapport_dernier_export.json` : rapport de la dernière collecte.
- `dernier_export_2026-09-27.zip` : ton export original intact, avec une extension ZIP correcte.

## Utiliser le notebook sur Android
1. Télécharge `Outil_tags_reprise_107_Colab.ipynb`.
2. Ouvre https://colab.research.google.com/ dans Chrome et connecte-toi à Google.
3. Dans **Ouvrir un notebook → Importer**, choisis le fichier. Selon l’interface, le menu peut apparaître sous **Fichier**. La version pour ordinateur de Chrome peut aider.
4. Lance la cellule **Installation**.
5. Modifie les champs de la cellule **Collecte**, puis lance-la.
6. À la fin ou après un arrêt géré, clique sur **Télécharger le ZIP**. Ce bouton peut être réutilisé sans relancer la collecte.

## Deux usages différents
### Continuer l’ancienne collecte
Réglages proposés dans ce notebook :
```python
PAGE_DEBUT = 108
PAGE_FIN = 139
LIMITE_NOUVEAUX_PERSONNAGES = 20
```
Les **42 anciens tags sont intégrés**, le compteur de nouveaux résultats commence à **0/20**, et la collecte peut parcourir 32 nouvelles pages, de 108 à 139 incluses. L’objectif est au maximum 20 nouveaux résultats retenus, soit 62 anciens et nouveaux réunis. Le plafond de pages ou une erreur peut empêcher d’atteindre cet objectif.

**Attention après une longue interruption :** cette reprise conserve les compteurs du 27 septembre et les combine avec des relevés plus récents. La position des tags peut avoir changé ; les contrôles peuvent donc arrêter le script. Ce n’est pas une actualisation fiable de l’ancien classement.

### Refaire un relevé actuel depuis le début
Pour récupérer des données plus récentes sans réutiliser les anciens compteurs :
```python
PAGE_DEBUT = 1
PAGE_FIN = 139
LIMITE_NOUVEAUX_PERSONNAGES = 42
```
Cela demande les 42 premiers tags Character rencontrés dans le parcours trié, et non une actualisation ciblée des mêmes 42 anciens tags. Les catégories et le nombre de personnages féminins peuvent donc changer. Le script n’a pas été testé en direct aujourd’hui et l’accès au site n’est pas garanti.

### Autre page de départ
Si tu choisis une page différente de **1 ou 108**, le script collecte uniquement l’intervalle demandé, **sans réutiliser l’ancien export**. Les rangs sont alors locaux à cet intervalle, pas ceux de tout le site. Il ne faut pas croire qu’une modification du champ de départ mémorise automatiquement une collecte précédente.

## Réglages et comportement conservés
- Pages de début et de fin modifiables, toutes deux incluses.
- Le compteur porte sur les **nouveaux résultats**, pas sur les anciens déjà enregistrés.
- Pause de **3 secondes** entre les requêtes.
- Toutes les catégories Character sont conservées.
- Arrêt à l’objectif de nouveaux résultats, après contrôle du seuil des ex aequo, ou à la page de fin, ou sur erreur/interruption.
- Chaque page étant lue entièrement, quelques tags supplémentaires peuvent figurer dans le CSV complet ; le fichier `nouveaux_resultats.csv` respecte la limite de résultats retenus.
- Les sauvegardes intermédiaires restent dans la session Colab. Elles ne sont pas automatiquement enregistrées dans Drive ou sur ton téléphone : télécharge le ZIP avant de supprimer l’environnement.

## Problèmes déjà rencontrés
- **« Objectif déjà couvert »** : une ancienne version comptait les anciens résultats dans la limite. La version fournie compte uniquement les nouveaux.
- **Faux doublons** : certains noms contiennent des caractères Unicode invisibles. Le script utilise désormais l’identifiant exact dans le lien, pas seulement le texte affiché.
- **HTTP 429** : limitation des requêtes par le site. Le script s’arrête, sans réessai automatique ni contournement. Respecte le `Retry-After` s’il est fourni et évite les relances en boucle. Trois secondes de pause ne garantissent pas la levée d’un blocage.
- **HTTP 403 / CAPTCHA** : accès refusé ou protection ; arrêt, sans contournement.
- **Ordre décroissant non respecté / tags répétés** : les données ont pu bouger ou la pagination être inattendue. Le script arrête le parcours plutôt que de valider un classement douteux.

## Limites du classement
Les relevés successifs ne forment pas un instantané parfaitement synchronisé. Les anciens exports ne contiennent pas tous les noms des tags non-Character ; les contrôles historiques peuvent donc être incomplets. Les libellés Character viennent du site et incluent des catégories, des espèces et des groupes. Le filtre féminin a été appliqué séparément aux anciens résultats, pas automatiquement par le collecteur.

## Python hors Colab (optionnel)
Installe `requests` et `beautifulsoup4`, puis :
```bash
python collecteur_tags.py --debut 108 --fin 139 --nouveaux 20
```
Hors Colab, le ZIP est créé localement ; le bouton de téléchargement est spécifique à Colab.
