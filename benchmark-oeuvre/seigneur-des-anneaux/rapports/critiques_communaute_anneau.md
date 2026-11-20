# Critiques de *La Communauté de l'Anneau* (livre) : Goodreads et SensCritique

Objet : noter les défauts qu'on reproche à une œuvre qui a réussi, pour compléter la grille Q1-Q7 de `structures_narratives_comparees.md` (qui ne contient que des réussites). Origine : ton message « elles ont aussi des défauts ».

## 0. Cadre et niveau de preuve

- **Limite anti-spoil respectée.** Seul ce qui concerne le tome I (livres I et II) est repris. Un extrait lu dépassait cette limite : je ne l'ai pas repris. Le sort de Boromir et de la Communauté n'est pas indiqué.
- **Collecte refaite avec Python**, après ta remarque. La première version avait été faite à la main avec `fetch_page` ; ce qui suit la remplace.
  - **Goodreads** : API GraphQL de la page (clé publique lue dans la page), filtre par note. **781 avis à 1 étoile : tous collectés** (total annoncé : 781). **2 119 avis à 2 étoiles sur 2 145 (99 %)**. La pagination plantait quand un avis supprimé cassait le jeton ; `completer_goodreads_2_etoiles.py` saute l'obstacle en abaissant le score du jeton de 1 (4 sauts). Les avis de même score situés juste après un obstacle ont pu être perdus : il manque 26 avis. Fichier : `data/goodreads_communaute_1_2_raw.json` ; scripts : `collecter_goodreads_communaute.py` puis `completer_goodreads_2_etoiles.py`.
  - **Goodreads 3★** : **6 968 avis sur 7 245 (96 %)**. Le tri par défaut échoue sur des avis supprimés ; la collecte utilise le tri « les plus récents » (`collecter_goodreads_note.py 3 NEWEST`), avec reprise après interruption. Quand un avis supprimé bloque, le script recule le jeton de quelques secondes à quelques jours et passe à la suite : il manque 277 avis, supprimés ou sautés. Fichier : `data/goodreads_communaute_3_raw.json`.
  - **SensCritique** : API GraphQL du site. **36 critiques collectées** avec texte complet (le site en annonce 37). Fichier : `data/senscritique_communaute_raw.json` ; script : `collecter_senscritique_communaute.py`.
  - **Comptages** : `analyser_critiques_communaute.py` (mots-clés, voir §2bis). Il ne modifie rien.
  - **Pas collectés** : les avis à 4 et 5 étoiles de Goodreads.
- **Non-spoil.** Les avis contiennent parfois la suite de la saga. 429 avis (9 à 1★, 89 à 2★ et 327 à 3★ en Goodreads, 4 en SensCritique) contiennent des mots qui annoncent les tomes suivants. Je ne les ai pas lus pour citer ; ils sont comptés mais jamais cités. Les fichiers JSON bruts contiennent ces avis : ne pas les ouvrir à la main si tu veux éviter les spoilers.
- **Niveau de preuve.** B pour les citations (textes vérifiés dans les fichiers). C pour les pourcentages : ce sont des **comptages de mots-clés**, pas une lecture avis par avis. Ils comptent surtout l'anglais et le français ; 195 avis Goodreads sont dans d'autres langues et passent donc à travers les mots-clés.
- Les citations en anglais sont **traduites par moi** (« trad. IA ») ; les citations françaises sont textuelles.

## 1. Notes globales (contexte)

| Site | Note | Volume | Répartition |
|---|---|---|---|
| Goodreads (page de l'œuvre) | 4,41 / 5 | 3 244 487 notes ; 59 044 avis | 5★ 60 % ; 4★ 25 % ; 3★ 9 % ; 2★ 2 % ; 1★ 1 % (55 633 notes à 1★, dont **781 avec un texte**) |
| SensCritique (traduction Francis Ledoux) | 8,3 / 10 | 7 363 notes ; 37 critiques annoncées, 36 collectées | des 36 critiques : 5/10 ×3 ; 6/10 ×3 ; 7/10 ×6 ; 8/10 ×7 ; 9/10 ×12 ; 10/10 ×5. **Aucune critique n'est notée en dessous de 5/10.** |

Les notes basses sont donc rares (environ 3 % de 1★ et 2★ sur Goodreads). Les reproches qui suivent viennent d'une petite minorité, et souvent de lecteurs qui notent quand même 5 à 7 sur 10.

## 2. Les reproches, par thème

| # | Reproche | Qui le dit (source) | Formulation |
|---|---|---|---|
| 1 | **Début lent** (prologue, Comté, avant Bree ou Fondcombe) | SensCritique : Cloclo183 (9/10), batman1985 (7/10), Vyty (6/10). Goodreads : plusieurs discussions et extraits | Cloclo183 : « L'entrée en matière de ce 1er tome est laborieuse », « trop de description tue la description ». batman1985 : « se taper un prologue sur ce qu'est un Hobbit n'aide pas à bien rentrer dans le bouquin ». Vyty : défaut « particulièrement sensible durant les premières centaines de pages ». Goodreads : « ça devient intéressant à partir de Strider », « à partir de Bree » (trad. IA, plusieurs lecteurs) |
| 2 | **Tom Bombadil, jugé inutile** | SensCritique : batman1985. Goodreads : plusieurs lecteurs | batman1985 : « les passages avec Tom Bombadil […] sont, à mon sens, inutiles ». Goodreads : un lecteur a abandonné le livre « à chaque fois que Frodon rencontre Tom Bombadil » (trad. IA) ; un autre : « charmant, mais largement sans objet » (trad. IA) |
| 3 | **Chansons et poèmes** | Goodreads (extraits et discussions) | « Les chansons et poèmes sont là pour faire joli et m'ont franchement ennuyé » (trad. IA). Des lecteurs disent sauter les poèmes en italique (trad. IA) |
| 4 | **Descriptions de paysages et de marche** | SensCritique : MaxGix (5/10). Goodreads : plusieurs extraits | MaxGix : « du détail, encore du détail et pour finir du détail » ; il regrette un récit de Gandalf ou d'Aragorn sur les ruines traversées « au lieu de nous balancer une vague présentation sur 3 lignes ». Goodreads : la « minutie géographique » fatigue ; « quinze pages » de « la route descendait puis remontait » (trad. IA) |
| 5 | **Personnages peu caractérisés, dialogues interchangeables** | SensCritique : Vyty. Goodreads : un avis | Vyty : « Tous ces personnages ne sont jamais caractérisés que par leur statut social et "historique" » ; « il leur manque toujours une âme ». Goodreads : le dialogue de chacun est « identique », au point que les noms des Compagnons sont « interchangeables », sauf Gandalf et peut-être Grands-Pas (trad. IA) |
| 6 | **Tension qui retombe ; danger mal raconté** | SensCritique : batman1985. Goodreads : un avis | batman1985 : la manière de raconter le danger « parait soit totalement anodine soit mal décrite » ; la réplique de Legolas devant le Balrog est « d'un ridicule sans nom ». Goodreads : certaines scènes sont racontées après coup, ce qui « vole presque tout le suspense » (trad. IA) |
| 7 | **L'univers passe avant le récit** | SensCritique : Vyty. Goodreads : J.G. Keely | Vyty : le récit est « un prétexte à développer cet univers » ; il parle de « projet vain ». Keely (note 3★) : « l'ajout de détails n'est pas l'ajout de profondeur » (trad. IA) |
| 8 | **Pas de fin** (premier volume) | Goodreads : un avis | « Vous n'aurez pas de fin ici […] c'est la première partie d'un roman » (trad. IA) |
| 9 | **Manichéisme, côté « roman de jeunesse », burlesque** | SensCritique : damon8671 (7/10). Goodreads : J.G. Keely | damon8671 : le rythme « peut être assez laborieux », « un manichéisme entache un peu la maturité du propos », « un trop burlesque par moment » ; il juge aussi que la fin est « un peu trop confuse » dans ses conséquences. Keely : une morale « dualiste », des personnages et une structure « trop plats » (trad. IA) ; sa critique vise Tolkien en général, pas seulement ce volume |
| 10 | **Traduction française** | SensCritique : Vyty | L'ancienne traduction aurait un style « d'une lourdeur rare » ; la nouvelle serait « une véritable réussite ». Hors périmètre de la grille (le défaut vient de la traduction, pas de la structure) |

## 2bis. Fréquences (comptage de mots-clés ; niveau C)

Effectifs : Goodreads 1★ = 781 avis (tous) ; Goodreads 2★ = 2 119 avis (sur 2 145) ; Goodreads 3★ = 6 968 avis (sur 7 245) ; SensCritique = 36 critiques (de 5 à 10/10). Un avis peut compter dans plusieurs lignes. **Seule la ligne Tom Bombadil est un comptage fiable** (nom précis). Les autres lignes sont approximatives (un mot comme « détail » ou « film » peut être positif ou neutre).

| Thème (mots-clés) | GR 1★ (781) | GR 2★ (2 119) | GR 3★ (6 968) | SensCritique (36) |
|---|---|---|---|---|
| Lent, ennuyeux, laborieux | 289 (37 %) | 898 (42 %) | 2 236 (32 %) | 19 (53 %) |
| **Tom Bombadil cité** | 35 (4 %) | 110 (5 %) | 438 (6 %) | 10 (28 %) |
| Chansons, poèmes | 76 (10 %) | 262 (12 %) | 989 (14 %) | 7 (19 %) |
| Descriptions, détails | 106 (14 %) | 403 (19 %) | 1 297 (19 %) | 23 (64 %) |
| Marche, voyage | 79 (10 %) | 270 (13 %) | 924 (13 %) | 4 (11 %) |
| Personnages plats, indistincts | 30 (4 %) | 100 (5 %) | 294 (4 %) | 1 (3 %) |
| Prologue, exposition | 18 (2 %) | 65 (3 %) | 213 (3 %) | 3 (8 %) |
| Langue, style, lourdeur | 43 (6 %) | 176 (8 %) | 501 (7 %) | 10 (28 %) |
| Mot « film » ou « Jackson » cité (pas un jugement) | 181 (23 %) | 608 (29 %) | 1 954 (28 %) | 23 (64 %) |
| « Il ne se passe rien » | 19 (2 %) | 42 (2 %) | 61 (1 %) | 0 |
| Manichéisme, morale | 5 (1 %) | 18 (1 %) | 77 (1 %) | 4 (11 %) |
| Fin, absence de conclusion | 22 (3 %) | 68 (3 %) | 301 (4 %) | 0 |
| Abandon (DNF) | 111 (14 %) | 142 (7 %) | 159 (2 %) | 2 (6 %) |
| Fondcombe, Conseil, Moria, Lórien cités | 13 (2 %) | 76 (4 %) | 416 (6 %) | 16 (44 %) |
| Bree, Strider, Aragorn cités | 9 (1 %) | 86 (4 %) | 362 (5 %) | 10 (28 %) |

**Ce que les chiffres montrent :**
- **« Lent » est de loin le reproche principal** : 37 % des avis à 1★, 42 % des avis à 2★, 32 % des avis à 3★ et 53 % des critiques SensCritique.
- **Tom Bombadil** : cité par 4 % des avis à 1★, 5 % des avis à 2★, 6 % des avis à 3★ et 28 % des critiques SensCritique (10 sur 36 ; sur les 9 que j'ai pu lire, 5 le critiquent ou le jugent dispensable, 4 l'aiment). Chez les mécontents de Goodreads, il pèse peu. Chez les lecteurs français plutôt satisfaits, il est le sujet de discussion n° 1.
- **Chansons, descriptions et marche** passent devant Bombadil chez les mécontents (12 %, 19 % et 13 % des avis à 2★ ; 14 %, 19 % et 13 % à 3★).
- **« Il ne se passe rien » littéralement** : 2 % seulement. Les lecteurs disent « lent » ou « ennuyeux », pas « rien ne se passe ».
- **« Le livre démarre à Bree ou au Conseil »** : peu soutenu par les chiffres. Seuls 9 avis à 2★ et 48 avis à 3★ (0,7 %) lient explicitement une amélioration à l'arrivée de Strider, à Fondcombe, au Conseil ou à la Moria. Mon rapprochement n° 1 plus bas reste donc une hypothèse, un peu mieux soutenue par les avis à 3★.
- **Le film** est cité dans 23 % des avis à 1★ et 29 % des avis à 2★, mais **ce n'est pas un jugement** : la plupart disent seulement qu'ils ont vu les films avant. Le jugement « le film est meilleur » est explicite dans **23 avis sur 772 à 1★ (3 %)** et **124 sur 2 030 à 2★ (6 %)** et **305 sur 6 641 à 3★ (5 %)** (lecture des phrases, textes non spoilers). Sur SensCritique, **aucune critique ne dit que le film est meilleur** ; plusieurs disent que le livre « enrichit » le film.
- **Abandon** : 14 % des avis à 1★, 7 % des avis à 2★ et 2 % des avis à 3★ disent avoir abandonné ou ne pas avoir fini.
- **Effet d'échantillon.** Sur les 540 premiers avis à 2★ (les plus aimés, collectés en premier), les taux étaient plus hauts : Bombadil 11 %, chansons 21 %, descriptions 29 %. Avec les 2 119 avis, ils baissent. Les avis les plus aimés sont donc plus détaillés et citent plus de défauts précis que l'ensemble.

**Avis à 3★ qui situent le moment où le livre s'améliore** (trad. IA) :
- « Les choses se sont améliorées quand tout le monde a quitté Fondcombe » (3★, 6 j'aime).
- « Puis Grands-Pas est arrivé et ça a commencé à devenir intéressant » (3★, 3 j'aime).
- « Je me disais : sors de la Comté et ça ira mieux. Puis : sors de Fondcombe. Enfin : arrive à la Moria… et tu sais quoi ? Ça devenait un peu… » (3★, 3 j'aime ; l'extrait que j'ai gardé s'arrête là).

**Avis les plus aimés** (nombre de « j'aime », Goodreads) :
- Le plus aimé des avis à 2★ (1 987 j'aime) : « Tous les poèmes et chansons sont là pour faire joli, et franchement, ils m'ont profondément ennuyé » (trad. IA). Il dit aussi avoir abandonné à Tom Bombadil (trad. IA).
- 2★, 240 j'aime : le dialogue de chaque personnage est « identique », les noms des Compagnons sont « interchangeables » (trad. IA).
- 2★, 88 j'aime : le lecteur se plaint de « pages et pages de descriptions de paysage » à la place de l'action (trad. IA).
- 1★ : un avis résume le livre par « ils marchent, ils marchent, et il ne se passe rien » (trad. IA, avis de 2022).

## 3. Ce que disent aussi les mêmes avis

- Les avis lus **concèdent la richesse du monde** : Vyty (« je ne connais aucun monde fictif créé avec une telle solidité »), MaxGix (« l'art du détail »), batman1985 (« un travail titanesque »), Keely (la minutie de Tolkien, même s'il juge qu'elle ne sert pas le récit).
- Quelques-uns situent **le moment où le livre « démarre »** : l'arrivée de Grands-Pas (Goodreads, 9 avis), « la constitution de la fraternité, après une bonne moitié de ce premier tome » (Vyty), la partie chez les elfes jugée « très réussie » (batman1985). Sur SensCritique, 16 critiques sur 36 citent Fondcombe, le Conseil, la Moria ou la Lórien, le plus souvent en bien.
- Les reproches **coexistent avec de bonnes notes** : Cloclo183 note 9/10 en écrivant « laborieux ». Un défaut de rythme n'empêche donc pas un lecteur de noter haut.
- Une critique nuance le défaut du début : la Comté est un contraste voulu avec le monde dangereux (Goodreads, un avis).

## 4. Rapprochements avec la grille (idées de l'IA, à discuter)

Ce sont mes lectures, pas des faits établis. Les cellules de la grille viennent de `structures_narratives_comparees.md` (partie D, vérifiée sur le PDF).

1. **« Début lent » ↔ Q1 repoussée.** La grille note que le Livre I ne donne qu'une destination (Fondcombe) et que la raison de fond arrive au Conseil (livre II, ch. 2, vers les trois cinquièmes du volume). Le reproche « lent » est massif dans les chiffres (§2bis). Mais seule une minorité d'avis (9 sur Goodreads) dit que ça démarre à Bree, à Fondcombe ou au Conseil : le lien avec Q1 reste une hypothèse, non confirmée par le corpus.
2. **« Début lent » ↔ Q2 faible.** La grille relève que Frodon est surtout réactif jusqu'au ch. 9. Le reproche « il ne se passe rien » pourrait venir de là. Piste, non prouvée.
3. **« Exposition lourde » ↔ Q6.** Le prologue et le ch. 2 font environ 20 000 mots avant le départ. batman1985 vise le prologue ; Keely vise « les détails ». Même zone du texte.
4. **Tom Bombadil et le rythme danger/refuge.** La grille voit dans l'alternance danger/refuge (Vieille Forêt, Bombadil, Tertres, Bree) un mécanisme qui fait monter les enjeux. Plusieurs lecteurs voient la même alternance comme un frein. **Le même mécanisme est une force pour l'un et un défaut pour l'autre.**
5. **Q5 (coût irréversible) arrive tard** : la première blessure irréversible est au ch. 11 sur 12. Je n'ai pas cherché ce point dans les avis par mot-clé ; je ne peux donc rien affirmer. Les reproches comptés (§2bis) portent surtout sur le rythme, les chansons, les descriptions et la marche.
6. **Ce que cela change pour la grille.** Un livre très réussi a un début que beaucoup de lecteurs jugent lent. La grille ne peut donc pas être lue comme « tout cocher = réussite ». Cela recoupe la limite n° 2 que j'avais notée (biais de survivant).

## 5. Limites de cette collecte et suite possible

- **Biais de sélection.** On n'a que des avis à 1 ou 2 étoiles (Goodreads) et une critique SensCritique (toutes à 5/10 ou plus). Ces lecteurs ne sont pas représentatifs : 97 % des notes Goodreads sont à 3 étoiles ou plus.
- **Goodreads 2★** : 2 119 sur 2 145 ; 26 avis manquent à cause des jetons cassés (voir §0).
- **Goodreads 3★** : 6 968 sur 7 245 ; 277 avis manquent (supprimés ou sautés). Les avis à 4 et 5 étoiles ne sont pas collectés.
- **Comptages par mots-clés** : l'anglais et le français seulement ; les avis dans d'autres langues sont sous-comptés. Pour des chiffres plus solides, il faudrait lire et classer un échantillon à la main (par exemple 50 avis).
- **Q7 (signal visible, réception)** : ces notes pourraient remplir Q7 pour la *Communauté*, mais je n'ai pas revérifié la définition exacte de Q7 dans l'addendum.
- **Autres œuvres** : le même script peut être adapté à *The Way of Kings* (avec filtre anti-spoil strict) ou à d'autres livres.
