# Edenia : tes influences, classées par élément du manga

*12 octobre 2026. Sources : dépôt `michaz94/Projecttest` (commit b1bffb0), surtout `fiches_references_projet.yaml`, `influences-atelier.md` et `structures_narratives_comparees.md`, plus tes réponses du 12 octobre.*

*Mise à jour du 12 octobre : ajout de 6 nouvelles images à l'ambiance des lieux (Shrek, La Princesse et la Grenouille, Frère des ours), avec le statut que tu as donné : envisagé. La double page de Naruto y était déjà ; l'image « grok_… » n'est pas comptée (voir §5). Ajout aussi de Raiponce pour l'apparence de Harley, et d'un 12ᵉ élément, « trait et style de dessin » (pôle A1), d'après ce que tu as dit le même jour.*

*Mise à jour du 15 octobre : ta phrase « Je crois que mon style artistique se trouve dans Jujutsu Kaisen, Att1e125 [corrigé ensuite en atie1225], Shadman, Disney/Pixar, Spider-Verse, Naruto, Gachiakuta et Quirkilicious » est ajoutée au trait (pôle A1). Trois nouvelles entrées : atie1225 (que tu avais d'abord écrit « Att1e125 »), Spider-Verse (rattaché à « Spider-Man » de ton répertoire) et Gachiakuta. Tes 12 images du même jour sont décrites au §4 bis, sans être comptées dans les scores.*

*Mise à jour du 15 octobre (soir) : tes 4 documents de tests PixAI (« Arcana 2 », « Arcana 2.1 », « Arcana Art » parties 1 et 2) sont ajoutés. Au trait : Quirkilicious, « le style artistique que j'aime le plus » (surtout sur *S.I.N*) ; Jujutsu Kaisen comme tag positif habituel ; ta liste de LoRA préférés (dont deux nouveaux noms, DreamWorks et Kaneoya Sachiko) et tes trois artistes aimés sans LoRA (Jomaro Kindred, Joe Madureira, Tetsuya Nomura). Au chara-design : les tags de ton test de **Cosmo Dumas** (The Boondocks, Shisui, Kingdom Hearts, Jujutsu Kaisen, Street Fighter), comptés comme un test (I), pas comme une décision. Les outils (modèles, accélérateurs, réglages) ne sont pas des influences : voir `recherche_pixai/modeles_et_tags_pixai.md`.*

## 0. À lire d'abord

- **Ce qui est mesuré.** Ces scores mesurent les **traces documentées** de chaque influence dans Edenia (décisions, éléments envisagés, aspects visés, tes déclarations). Ils ne mesurent pas ton attachement à une œuvre. Pour ça, voir le classement 12, « poids biographique », tenu à part.
- **Le codage est de moi (IA).** C'est moi qui ai rangé chaque preuve dans un élément et un type. Toutes les preuves sont dans `preuves.csv`, et le script `classer_influences.py` recalcule tout. Si tu changes un type ou un barème, relance-le.
- **Ne pas lire « absente » comme « sans influence ».** Une œuvre sans trace peut t'avoir marqué sans que ce soit écrit. 36 entrées de ton répertoire sur 66 n'ont aucune trace documentée, dont 2 avec une simple hypothèse de l'IA (Lovecraft, Doctor Who, Breaking Bad…).
- **Ce qui ne change pas.** Le YAML reste la seule source des statuts. Je ne l'ai pas modifié, et les corrections à y faire sont listées au §5.

### Barème

| Type | Points | Ce que c'est |
|---|---:|---|
| **D** | 3 | Trace dans une décision (statut « décidé ») |
| **E** | 2 | Trace dans un élément envisagé |
| **U** | 2 | Déclaration explicite de ta part sur l'usage de l'œuvre pour cet élément (inspiration nommée d'un personnage, aspect visé, « grande influence sur… ») |
| **I** | 1 | Intérêt, non précisé, ou simple mention de ta part |
| **H** | 0,5 | Hypothèse de l'IA non validée. Toujours signalée en italique. |

- **Plafond.** Pour une même influence dans un même élément, au plus 3 preuves de même type comptent, pour qu'une liste de 24 créatures n'écrase pas une décision.
- **Pas de double compte.** Un même fait ne compte que dans un seul élément. Par exemple, la Forêt de conte compte dans « décors », pas aussi dans « monde ».
- **Ex aequo.** Deux influences au même score ont le même rang.
- **Repoussoirs.** Les influences dont tu veux t'éloigner (« distance à maintenir », « critiqué ») ne sont pas comptées. Elles sont listées au §3.

### Confiance par élément

| Élément | Confiance | Pourquoi |
|---|---|---|
| Matière (folklore, occultisme, au-delà) | **élevée** | Beaucoup de statuts posés par toi, à partir de tes propres extraits |
| Trait et style de dessin | **élevée** sur les références nommées | Tes phrases du 12 et du 15 octobre sont directes (la seconde avec « je crois »), et tes documents PixAI les confirment par l'usage ; mais rien n'est décidé, et tu as précisé que ton style est le même pour Edenia et Arcana |
| Chara-design et tenues | **élevée** | Une décision (« archaïque mais pas trop ») et des emprunts datés |
| Personnages | **élevée** sur les sources nommées | Classement très plat (11 ex aequo). Harley n'est pas définie pour l'instant. |
| Décors et ambiance | **moyenne à élevée** | La Forêt de conte est décidée, et l'ambiance des lieux compte maintenant 11 ou 12 images (envisagée, une planche d'inspiration, rien de définitif) |
| Monde | **moyenne** | Surtout de l'envisagé et de l'intérêt. Dosage W3, Runeterra, FMA : « je ne sais pas » |
| Société et institutions | **moyenne à faible** | Selon le brief, les hiérarchies et l'institution ne sont pas le sujet principal |
| Technologie et époque | **faible à moyenne** | Peu d'éléments, et le plafond de 1914 n'est qu'envisagé |
| Ton | **faible à moyenne** | Une seule déclaration ciblée (HxH, Red Hood) |
| Narration (structure, intrigue) | **faible** | Plafond de puissance, type d'affrontement, mortalité et but : tous « je ne sais pas » |
| Pouvoirs et gimmick | **faible** | Le système de pouvoirs a été retiré du YAML le 8 octobre |
| Action et combats | **très faible** | Aucune décision. Tout vient de ce que tu dis des œuvres. |

## 1. La liste de tes influences

L'ordre est celui de ton répertoire, qui ne donne « ni un ordre chronologique ni un degré d'importance ». La colonne « statut » reprend le `statut_relation` du YAML : *influence* = ce qui t'a façonné ; *référence* = point de comparaison ou éléments piochés.

| Groupe (ton répertoire) | Influence | Statut dans le YAML | Trace documentée dans Edenia ? |
|---|---|---|---|
| Littérature, mythes et imaginaires | The Stormlight Archive | influence | oui |
| Littérature, mythes et imaginaires | Game of Thrones | influence | oui |
| Littérature, mythes et imaginaires | La légende arthurienne | — | oui |
| Littérature, mythes et imaginaires | Harry Potter | influence (films et livres) | oui |
| Littérature, mythes et imaginaires | H. P. Lovecraft | — | hypothèse IA seulement |
| Littérature, mythes et imaginaires | Le Seigneur des anneaux | influence | oui |
| Littérature, mythes et imaginaires | The Kingkiller Chronicle | influence | aucune trace documentée |
| Littérature, mythes et imaginaires | Mother of Learning | — | aucune trace documentée |
| Littérature, mythes et imaginaires | La Horde du Contrevent | référence (« sans doute un peu moins ») | aucune trace documentée |
| Littérature, mythes et imaginaires | Shakespeare | — | aucune trace documentée |
| Littérature, mythes et imaginaires | La Fondation SCP | — | oui |
| Littérature, mythes et imaginaires | The Magnus Archives | — | aucune trace documentée |
| Littérature, mythes et imaginaires | L'occultisme, l'ésotérisme | — | oui |
| Comics et super-héros | Worm / Parahumans | influence | oui |
| Comics et super-héros | Watchmen (comic, série) | — | oui |
| Comics et super-héros | X-Men | — | oui |
| Comics et super-héros | Batman | — | aucune trace documentée |
| Comics et super-héros | Spider-Man | — | oui |
| Comics et super-héros | Invincible | — | aucune trace documentée |
| Comics et super-héros | Hellboy | — | oui |
| Comics et super-héros | Deadly Class | — | aucune trace documentée |
| Comics et super-héros | Teen Titans | — | aucune trace documentée |
| Comics et super-héros | Joe Madureira | — | aucune trace documentée |
| Comics et super-héros | Marvel Rivals | — | aucune trace documentée |
| Manga et animation | Yu Yu Hakusho | influence | oui |
| Manga et animation | Hunter x Hunter | influence | oui |
| Manga et animation | Jujutsu Kaisen | influence | oui |
| Manga et animation | JoJo's Bizarre Adventure (parties 4 et 5) | — | aucune trace documentée |
| Manga et animation | Naruto | influence | oui |
| Manga et animation | L'Attaque des Titans | — | oui |
| Manga et animation | One Piece | influence | oui |
| Manga et animation | Dorohedoro | — | oui |
| Manga et animation | Solo Leveling | — | aucune trace documentée |
| Manga et animation | Fullmetal Alchemist | référence | oui |
| Manga et animation | The Hunters Guild: Red Hood | influence + référence | oui |
| Manga et animation | World Trigger | — | aucune trace documentée |
| Manga et animation | Magi | — | aucune trace documentée |
| Manga et animation | The Seven Deadly Sins | (repoussoir arthurien) | aucune trace documentée |
| Manga et animation | Steins;Gate | — | aucune trace documentée |
| Manga et animation | Bakemonogatari | — | aucune trace documentée |
| Manga et animation | Kekkai Sensen | — | aucune trace documentée |
| Manga et animation | Haikyu!! | — | aucune trace documentée |
| Manga et animation | Hayao Miyazaki | — | aucune trace documentée |
| Jeux vidéo et univers associés | World of Warcraft, Hearthstone | influence | oui |
| Jeux vidéo et univers associés | League of Legends, Legends of Runeterra, Arcane | influence | oui |
| Jeux vidéo et univers associés | The Witcher (surtout The Witcher 3) | référence | oui |
| Jeux vidéo et univers associés | BioShock (série) | influence (Infinite) | oui |
| Jeux vidéo et univers associés | Urban Rivals | référence | oui |
| Jeux vidéo et univers associés | Grand Theft Auto V | — | aucune trace documentée |
| Jeux vidéo et univers associés | Street Fighter, Marvel vs. Capcom, Capcom vs. SNK, SNK, Capcom | — | oui |
| Jeux vidéo et univers associés | Overwatch | — | oui |
| Jeux vidéo et univers associés | Final Fantasy | — | aucune trace documentée |
| Jeux vidéo et univers associés | Tekken | — | aucune trace documentée |
| Jeux vidéo et univers associés | Apex Legends | — | aucune trace documentée |
| Cinéma, séries et spectacle | Breaking Bad | — | aucune trace documentée |
| Cinéma, séries et spectacle | Quentin Tarantino | influence | oui |
| Cinéma, séries et spectacle | Doctor Who | — | aucune trace documentée |
| Cinéma, séries et spectacle | The X-Files | — | aucune trace documentée |
| Cinéma, séries et spectacle | Terminator (1 et 2) | — | aucune trace documentée |
| Cinéma, séries et spectacle | Alien | — | aucune trace documentée |
| Cinéma, séries et spectacle | Mad Max | — | aucune trace documentée |
| Cinéma, séries et spectacle | Disney et Pixar (dont La Princesse et la Grenouille, Frère des ours, Raiponce) | — | oui |
| Cinéma, séries et spectacle | Les Affranchis | — | aucune trace documentée |
| Cinéma, séries et spectacle | Fargo (saisons 1 et 2) | — | aucune trace documentée |
| Cinéma, séries et spectacle | Films d'arts martiaux | — | hypothèse IA seulement |
| Cinéma, séries et spectacle | Le catch | — | hypothèse IA seulement |

**Hors répertoire, mais présents dans le dépôt ou dits en conversation :**

| Influence | Où elle apparaît | Trace documentée dans Edenia ? |
|---|---|---|
| Dictionnaire infernal (Collin de Plancy) | YAML (source documentaire) ; extraits dans Pdfmd/ | oui |
| Folklore français (carte « Mythical Beasts of France ») | YAML, fiche créatures | oui |
| Dictionnaire féodal (1820) | YAML (source documentaire, apportée par le dépôt) | oui |
| Bibliothèque bleue | YAML | oui |
| Dante (Inferno, Purgatorio) | YAML (au-delà) | oui |
| Tradition catholique (Limbes, purgatoire) | YAML (au-delà) | oui |
| Folklores gréco-égyptiens | YAML (corpus de traditions) | oui |
| Contes européens (tradition) | YAML (ambiance des lieux) | oui |
| Renaissance (période) | YAML (brouillons) | oui |
| Moyen Âge, bas et milieu (période) | YAML (brouillons) | oui |
| Shrek | YAML (influence) ; DreamWorks, donc pas dans « Disney et Pixar » | oui |
| Radiant / Fabula Fantasia (Tony Valente) | YAML (référence, « un cas spécial ») ; Fabula Fantasia sans statut_relation | oui |
| Bleach | YAML (référence) | oui |
| Inspirations asiatiques (source non précisée) | YAML (envisagé) | oui |
| Ben 10 | conversation du 12 oct. (noms) | oui |
| Soul Eater | conversation du 12 oct. (Maka) | oui |
| Gigantic | récit de influences-atelier.md (projet de jeu) | oui |
| BioShock (premier du nom) | conversation du 12 oct. (zone mafieuse) | oui |
| Shadman | conversations du 12 et du 15 oct. (références de dessin) | oui |
| Quirkilicious (Drake Tsui) | conversations du 12 et du 15 oct. (références de dessin) ; doc. PixAI (« le style artistique que j'aime le plus ») | oui |
| atie1225 (鉄, illustrateur sur X) | conversation du 15 oct. (style artistique ; écrit d'abord « Att1e125 », corrigé en « atie1225 ») | oui |
| Gachiakuta (Kei Urana, graffitis d'Ando Hideyoshi) | conversation du 15 oct. (style artistique) ; doc. PixAI (LoRA préférés) | oui |
| DreamWorks Animation (style) | doc. PixAI « Arcana Art » (LoRA préférés) | oui |
| Kaneoya Sachiko (écrit « Kanoaya Sachiko ») | doc. PixAI « Arcana Art » (LoRA préférés) ; orthographe probable « Kaneoya », non confirmée | oui |
| Jomaro Kindred (concept artist, Hearthstone) | doc. PixAI « Arcana Art » (artistes aimés, sans LoRA) | oui |
| Joe Madureira | doc. PixAI « Arcana Art » (artistes aimés, sans LoRA) | oui |
| Tetsuya Nomura / Kingdom Hearts (style de personnages) | doc. PixAI « Arcana Art » (artistes aimés) ; test de Cosmo (Kingdom Hearts) | oui |
| The Boondocks | test PixAI de Cosmo Dumas | oui |

*30 entrées du répertoire sur 66 ont une trace documentée.*

## 2. Classements par élément

*Détail : nombre de preuves par type. Les hypothèses de l'IA (H) sont en italique.*

### Monde : structure, zones, géographie politique (pôle B2)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Légende arthurienne (Perceval, Vulgate) | 6 | D×1 · E×1 · I×1 | Lieux décidés Brocéliande et Le Lac ; règle « lieux arthuriens français uniquement » ; Six lieux envisagés (Douloureuse Garde, Bénoïc, Gaunes, Trèbes, Montlair, Terre Déserte) ; Zone de brouillon « Brocéliande, forêt féerique avec une école » |
| 1 | Runeterra (LoL, Arcane, Legends of Runeterra) | 6 | E×1 · U×1 · I×2 | Note du dépôt : « Référence principale du monde. Edenia en est proche » ; Plan politique envisagé (royaume principal, cités-États, royaumes adjacents) ; modèle de monde « W3 + Runeterra + FMA » ; Zone de brouillon « Nouvelle-Orléans / Caraïbes » inspirée … |
| 3 | Folklore français (carte « Mythical Beasts of France ») | 5 | E×1 · U×1 · I×1 | Région montagnarde enneigée (décidée) avec les Barbegazi comme créature locale (envisagés) ; Héritage francophone gardé entre les zones ; Héritages « répartis par régions » (une des deux façons retenues) |
| 3 | The Witcher 3 | 5 | E×1 · U×1 · I×1 | Aspect visé : structure du monde (« U avait déjà cité The Witcher 3 comme modèle du monde ») ; Plan envisagé ; modèle de monde « W3 + Runeterra + FMA » ; Zone marais : le brouillon cite Velen |
| 5 | BioShock Infinite | 4 | D×1 · I×1 | Zone industrielle de type BioShock Infinite ; Zone de brouillon « Piltover / Columbia » |
| 6 | Fullmetal Alchemist | 3 | E×1 · I×1 | Plan envisagé ; modèle de monde « W3 + Runeterra + FMA » ; « FMA correspond au modèle un pays principal, avec des régions culturelles et des voisins » |
| 6 | Urban Rivals | 3 | U×1 · I×1 | « attrait […] pour les univers hétéroclites, avec des gangs et des designs reconnaissables » ; Aspect visé : plusieurs zones culturelles dans un même lieu |
| 8 | Fondation SCP (dont la Chicago Spirit) | 2 | U×1 | Chicago Spirit citée comme source de la zone mafieuse ; structure sociale gardée |
| 8 | La Princesse et la Grenouille (Disney, 2009) | 2 | I×2 | Les deux images vont à la zone marais (« style bayou ») ; Les deux images vont à la zone Nouvelle-Orléans / Caraïbes |
| 8 | Occultisme et ésotérisme | 2 | U×1 | Règle France, sinon Angleterre et Allemagne : « pays principaux de l'occultisme » |
| 11 | Warcraft / Hearthstone | 1.5 | I×1 · H×1 | Gadgetzan dans la liste de zones du brouillon (rapprochement déjà fait par toi) — *hyp. IA : Monde en mosaïque de factions hérité des jeux de cartes (principe P-D)* |
| 12 | BioShock (premier du nom) | 1 | I×1 | « Piltover-BioShock 1 / Gadgetzan » (brouillon) ; source de la zone mafieuse |
| 12 | Shrek | 1 | I×1 | Zone marais « style bayou ou marais de Shrek » |
| 12 | The Stormlight Archive | 1 | I×1 | Zone désertique pensée d'après les Plaines Brisées de Roshar |

### Technologie et époque (pôle B2)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Occultisme et ésotérisme | 2.5 | U×1 · H×1 | Occultisme des années 1890-1910 en tête ; « je ne veux pas dépasser 1914 » — *hyp. IA : 1914 ferme aussi la grande époque des sociétés occultes (Belle Époque)* |
| 2 | BioShock Infinite | 1.5 | I×1 · H×1 | Contrainte liée dans la fiche : le plafond technologique (1950, baisse à 1914 envisagée) — *hyp. IA : 1914 (envisagé) proche de 1912, date de BioShock Infinite* |
| 2 | Runeterra (LoL, Arcane, Legends of Runeterra) | 1.5 | I×1 · H×1 | Cadre temporel flou comme Runeterra — *hyp. IA : Inégalité régionale par les ressources « comme les autres modèles » (Piltover)* |
| 4 | BioShock (premier du nom) | 1 | I×1 | Gardé seulement pour ce qui tient sous 1914 |
| 4 | Fondation SCP (dont la Chicago Spirit) | 1 | I×1 | Chicago Spirit, organisation du début du XXᵉ siècle, gardée sous 1914 |
| 4 | Moyen Âge, bas et milieu (période) | 1 | I×1 | Bas et milieu Moyen Âge |
| 4 | Naruto | 1 | I×1 | Cadre temporel flou comme Naruto |
| 4 | One Piece | 1 | I×1 | Cadre temporel flou comme One Piece |
| 4 | Radiant / Fabula Fantasia (Tony Valente) | 1 | I×1 | Cadre temporel flou comme Radiant |
| 4 | Renaissance (période) | 1 | I×1 | Renaissance : science, folklore, superstitions, croyances, magie |

### Matière : folklore, légendes, occultisme, au-delà (pôle B)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Dictionnaire infernal (Collin de Plancy) | 11 | D×1 · E×4 · I×2 | Agrippa ; Gremory/Gomory ; Furfur ; Marbas ; Stolas ; Figures non précisées : Faust, Albert le Grand, Grandier, Merlin, Abel de Larue ; Cour infernale |
| 2 | Folklore français (carte « Mythical Beasts of France ») | 9 | E×4 · I×3 | Barbegazi ; Mélusine ; Ankou ; Mourioche, Petit Homme rouge, Gayant, Houeron, Tarasque ; Loup-garou, Vouivre, Fée… ; Gargouille, Dame verte, Chien noir de Pontgibaud… ; Les 24 créatures de la carte en intérêt |
| 3 | Légende arthurienne (Perceval, Vulgate) | 3 | D×1 | Personnages arthuriens : des inspirations seulement, sous d'autres noms |
| 4 | Dante (Inferno, Purgatorio) | 2 | I×2 | Inferno ; Purgatorio |
| 4 | Tradition catholique (Limbes, purgatoire) | 2 | I×2 | Limbo catholique ; Purgatoire classique |
| 6 | Bibliothèque bleue | 1.5 | I×1 · H×1 | Le contenu des livres de la Bibliothèque bleue — *hyp. IA : Matrice commune de la chevalerie, du conte et de la superstition* |
| 7 | Dorohedoro | 1 | I×1 | Enfer et démons de Dorohedoro |
| 7 | Folklores gréco-égyptiens | 1 | I×1 | Corpus cité, sans usage précisé |
| 7 | Hellboy | 1 | I×1 | Chasse sauvage, retrouvée dans Hellboy |
| 7 | Occultisme et ésotérisme | 1 | I×1 | Penche vers l'ambiance (symboles, décors, objets rituels) ; livres de sorts : « ce qui compte surtout : les symboles sur le livre » ; volontairement non tranché |
| 7 | Renaissance (période) | 1 | I×1 | Renaissance : folklore, superstitions, croyances, magie |
| 7 | The Witcher 3 | 1 | I×1 | Chasse sauvage, découverte avec The Witcher 3 |
| 7 | Urban Rivals | 1 | I×1 | Yétis (groupe), inspirés des Frozn |
| 7 | X-Men / Marvel (Magik) | 1 | I×1 | Limbo de Magik |
| 15 | La Princesse et la Grenouille (Disney, 2009) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Masques, statuettes et bougies du salon : l'occultisme d'ambiance vers lequel tu penches* |

### Société et institutions : rangs, titres, organisations (pôle B)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Dictionnaire infernal (Collin de Plancy) | 3.5 | U×1 · I×1 · H×1 | Aspect visé : les hiérarchies ; Cour infernale — *hyp. IA : L'enfer copie la monarchie humaine (Abigor, Adraméleck, Léonard dans tes extraits)* |
| 2 | Bleach | 2 | U×1 | Aspect visé : la structure du Gotei 13 |
| 2 | Fondation SCP (dont la Chicago Spirit) | 2 | U×1 | Zone mafieuse : seulement la structure sociale |
| 2 | Runeterra (LoL, Arcane, Legends of Runeterra) | 2 | E×1 | École ou académie à cadre vestimentaire imposé (envisagée) ; tenue Academy Ekko |
| 5 | Dictionnaire féodal (1820) | 1.5 | I×1 · H×1 | Source documentaire du dépôt (titres, chevalerie, champions) — *hyp. IA : Chevalerie interdite au roturier* |
| 6 | Harry Potter (films et livres) | 1 | I×1 | École de type Harry Potter à Brocéliande |
| 6 | Hunter × Hunter | 1 | I×1 | Gimmick Hunter : un statut délivré par une institution |
| 6 | Radiant / Fabula Fantasia (Tony Valente) | 1 | I×1 | Tenue Fabula Fantasia : « surtout pour des personnages de profession Chevalier » |
| 6 | Warcraft / Hearthstone | 1 | I×1 | Gadgetzan : ville tenue par des familles criminelles |
| 10 | Légende arthurienne (Perceval, Vulgate) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Goal « devenir chevalier » = goal d'ouverture de Perceval* |
| 10 | The Hunters Guild: Red Hood | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Modèle de la guilde* |

### Pouvoirs et gimmick (pôle B2, système)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Bleach | 3 | U×1 · I×1 | Aspect visé : le Bankai ; Gimmick Shinigami |
| 1 | Fullmetal Alchemist | 3 | U×1 · I×1 | Aspect visé : les deux traditions d'alchimie ; Gimmick Alchimiste |
| 3 | Hunter × Hunter | 1 | I×1 | Gimmick Hunter |
| 3 | Naruto | 1 | I×1 | Gimmick Ninja |
| 3 | One Piece | 1 | I×1 | Gimmick Pirate |
| 6 | Dictionnaire infernal (Collin de Plancy) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Grandier comme matière du gimmick Exorciste ; rites à conditions* |
| 6 | Jujutsu Kaisen | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : « Version améliorée et modernisée de Bleach et de YYH » (ton jugement, pas un usage)* |
| 6 | Légende arthurienne (Perceval, Vulgate) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : « Chevalier » comme gimmick latent* |

### Personnages (pôle C)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Harry Potter (films et livres) | 5 | U×2 · I×1 | Hermione, inspiration de Harley ; Luna Lovegood, personnalité visée pour Harley ; Le nom « Harley » rapproche d'Hermione |
| 2 | Hunter × Hunter | 2.5 | U×1 · H×1 | Killua, inspiration de Cosmo — *hyp. IA : Cosmo construit comme le « second aimé »* |
| 2 | Légende arthurienne (Perceval, Vulgate) | 2.5 | U×1 · H×1 | Perceval, inspiration de Brann — *hyp. IA : Goal de Brann = goal d'ouverture de Perceval* |
| 4 | Ben 10 | 2 | I×2 | Gwen Tennyson : prénom et modèle d'origine de Harley ; « Bran » rapproché de Ben 10 |
| 4 | Fullmetal Alchemist | 2 | U×1 | Edward, inspiration de Brann |
| 4 | Naruto | 2 | U×1 | Shisui, inspiration de Cosmo |
| 4 | One Piece | 2 | U×1 | Luffy, inspiration de Brann |
| 4 | Runeterra (LoL, Arcane, Legends of Runeterra) | 2 | U×1 | Ekko, inspiration de Cosmo |
| 4 | Soul Eater | 2 | U×1 | Maka Albarn, personnalité visée pour Harley |
| 4 | The Stormlight Archive | 2 | U×1 | Shallan, inspiration de Harley |
| 4 | Worm | 2 | U×1 | Tattletale, inspiration de Harley |
| 4 | X-Men / Marvel (Magik) | 2 | U×1 | Magik, inspiration de Harley |
| 4 | Yu Yu Hakusho | 2 | U×1 | Yusuke, inspiration de Brann |
| 14 | Game of Thrones | 1 | I×1 | Le nom « Bran » vient de GoT |
| 14 | Warcraft / Hearthstone | 1 | I×1 | « Brann » vient de Hearthstone |

### Visuel : trait et style de dessin (pôle A1)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Quirkilicious (Drake Tsui) | 7 | U×3 · I×1 | « Mes autres références en termes de dessin » ; « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; « Quirikilicious surtout son style sur S.I.N est le style artistique que j'aime le plus » ; « Lora Préféré : Shadman, Gachiakuta, … |
| 2 | Disney / Pixar (style d'animation) | 5 | U×2 · I×1 | « Disney Pixar est le style que je cherche à atteindre » ; « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks » |
| 2 | Gachiakuta (Kei Urana, graffitis d'Ando Hideyoshi) | 5 | U×2 · I×1 | « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; « Gachiakuta (il y a deux modèles que j'utilise), c'est le deuxième Lora qui me sert de base » ; « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, … |
| 2 | Shadman | 5 | U×2 · I×1 | « Mes autres références en termes de dessin » ; « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks » |
| 2 | atie1225 (鉄, illustrateur sur X) | 5 | U×2 · I×1 | « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; « Atie1225 me sert plus comme un Lora de base » (le mot « sketchy », jugé trop fort, retiré par toi le 15 oct.) ; « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, … |
| 6 | Jujutsu Kaisen | 4 | U×2 | « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) ; Tag positif habituel : « Jujutsu Kaisen Style (et ces dérivés) » |
| 7 | Cartoon semi-réaliste (famille de styles) | 2 | U×1 | « J'aime bien le style semi-realistic cartoon, je trouve que ça peut rendre bien en manga » |
| 7 | Codes du manga (yeux, forme du visage) | 2 | U×1 | « légèrement différent, pour qu'il soit plus manga compatible, c'est surtout pour les yeux et la forme du visage » |
| 7 | Naruto | 2 | U×1 | « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) |
| 7 | Spider-Verse (films d'animation Spider-Man) | 2 | U×1 | « Je crois que mon style artistique se trouve dans […] » (liste de 8 noms) |
| 11 | Capcom / Street Fighter (jeux de combat) | 1 | I×1 | Tags habituels : « parfois Street Fighters Characters » |
| 11 | DreamWorks Animation (style) | 1 | I×1 | « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks » |
| 11 | Joe Madureira | 1 | I×1 | « Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura » |
| 11 | Jomaro Kindred (concept artist, Hearthstone) | 1 | I×1 | « Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura » |
| 11 | Kaneoya Sachiko (écrit « Kanoaya Sachiko ») | 1 | I×1 | « Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks » |
| 11 | Raiponce / Tangled (Disney, 2010) | 1 | I×1 | Cinq dessins de Raiponce donnés comme exemples du style cherché |
| 11 | Runeterra (LoL, Arcane, Legends of Runeterra) | 1 | I×1 | Art de Runeterra perçu comme « plus semi-réaliste stylisé et plus compatible avec le manga shōnen » |
| 11 | Tetsuya Nomura / Kingdom Hearts (style de personnages) | 1 | I×1 | « Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura » |

### Visuel : chara-design et tenues (pôle A3)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Radiant / Fabula Fantasia (Tony Valente) | 7 | D×1 · U×2 | « Archaïque mais pas trop » (décidé), inspiré de Radiant et de Runeterra ; Emprunt de tenue : « style copié/inspiré de Radiant » ; Fabula Fantasia : tenue de Brann (« moins claire ») |
| 2 | Runeterra (LoL, Arcane, Legends of Runeterra) | 5 | D×1 · U×1 | « Archaïque mais pas trop » (décidé), inspiré de Radiant et de Runeterra ; Emprunt de tenue : Academy Ekko, « tenue qui l'inspire le plus » (Cosmo) |
| 3 | Capcom / Street Fighter (jeux de combat) | 3 | U×1 · I×1 | Projet de jeu à 16 ans : « esthétique Capcom de Street Fighter », légèrement transféré dans tes mangas ; Cosmo, test de design : « street fighter Characters style » |
| 3 | Harry Potter (films et livres) | 3 | E×1 · I×1 | Harry Potter (films) : aspect visé esthétique et visuels ; Test de tenue « proche de Harry Potter », dont tu aimes beaucoup le rendu |
| 3 | Inspirations asiatiques (source non précisée) | 3 | E×1 · I×1 | Personnages d'inspiration asiatique ; Objets bouddhiques japonais |
| 6 | Raiponce / Tangled (Disney, 2010) | 2.5 | U×1 · H×1 | Harley : « pour moi son apparence ressemble à Raiponce de Tangled » — *hyp. IA : Raiponce est un conte des Grimm, donc allemand : cohérent avec ta règle France, Angleterre, Allemagne* |
| 7 | Dictionnaire infernal (Collin de Plancy) | 2 | U×1 | Gremory, Furfur, Marbas et Stolas sont choisis « surtout pour leur design et leur représentation artistique » |
| 7 | Jujutsu Kaisen | 2 | I×2 | Même test de tenue : « un peu de Jujutsu Kaisen » ; Cosmo, test de design : « Jujutsu Kaisen Character style » |
| 7 | Urban Rivals | 2 | U×1 | « des designs reconnaissables » ; designs du projet de jeu |
| 10 | Naruto | 1.5 | I×1 · H×1 | Cosmo, test de design : « shisui uchiha », « blue tunic, baggy pants, leg bandages » — *hyp. IA : Ch. 679 : tenues d'aventuriers de fantasy européenne (cotte de mailles, cape, chapeau de mage)* |
| 11 | Overwatch | 1 | I×1 | Designs du projet de jeu |
| 11 | Tetsuya Nomura / Kingdom Hearts (style de personnages) | 1 | I×1 | Cosmo, test de design : « kingdom hearts Character style » |
| 11 | The Boondocks | 1 | I×1 | Cosmo, test de design : « (the boondocks:1.2) » |

### Visuel : décors et ambiance (pôle A2)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Shrek | 11 | D×1 · E×6 · I×2 | Forêt de conte (décidée) : 3 des 5 images de décor sont des peintures de développement de Shrek ; Ambiance des lieux (envisagée) : peinture de développement de Shrek n° 1 (planche d'origine) ; Ambiance des lieux : peinture de développement de Shrek n° 2 … |
| 2 | La Princesse et la Grenouille (Disney, 2009) | 4 | E×2 | Ambiance des lieux : marais bleu, bateau coincé dans un cyprès (arbre de Mama Odie) ; Ambiance des lieux : salon du sorcier (« Dr. Duvalier », masques, bougies, cartes) |
| 3 | Naruto | 3 | E×1 · I×1 | Forêt de conte : 1 des 5 images (ch. 679) ; Ambiance des lieux (envisagée) : double page couleur du ch. 679 |
| 4 | Warcraft / Hearthstone | 2.5 | U×1 · H×1 | « grande influence sur l'esthétique […] surtout les paysages forestiers » — *hyp. IA : The Witchwood : forêt corrompue, loups-garous* |
| 5 | Contes européens (tradition) | 2 | U×1 | « atmosphère de conte européen au sens large (tous types de contes) » |
| 5 | Frère des ours (Disney, 2003) | 2 | E×1 | Ambiance des lieux : vallée, rivière et montagnes |
| 5 | Runeterra (LoL, Arcane, Legends of Runeterra) | 2 | U×1 | « Mais en vrai, l'esthétique d'Edenia est beaucoup plus proche de Runeterra » (dit à propos des paysages) |
| 8 | Occultisme et ésotérisme | 1 | I×1 | Cosmo, test de design : « (Occultism aesthetic), esoterism » |
| 9 | BioShock Infinite | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Le « type BioShock Infinite » de la zone industrielle est aussi un modèle visuel* |

### Narration : structure et intrigue (pôle D1-D2)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | The Stormlight Archive | 4 | U×1 · I×2 | Seule œuvre citée sans protagoniste central ; « peut avoir des répercussions sur comment [tu traites] Edenia » ; Narration différente de celle du Seigneur des anneaux ; « cette impression de maîtrise » |
| 2 | Hunter × Hunter | 3 | U×1 · I×1 | « l'exposition est une épreuve » (ton addendum) ; Pas de schéma répété ; exception tardive au protagoniste central |
| 2 | One Piece | 3 | U×1 · I×1 | « montrée, pas dite » (ton addendum) ; Schéma répété |
| 4 | Bleach | 2 | U×1 | Aspect visé : « la narration sur le Gotei 13 » |
| 5 | Game of Thrones | 1 | I×1 | Pas de protagoniste central (ta correction) |
| 5 | L'Attaque des Titans | 1 | I×1 | « impression de maîtrise » |
| 5 | Le Seigneur des anneaux | 1 | I×1 | Schéma répété |
| 5 | Légende arthurienne (Perceval, Vulgate) | 1 | I×1 | Vulgate : pas de protagoniste central |
| 5 | Worm | 1 | I×1 | « surtout à partir de l'arc 3, où ils font un braquage » ; « déconstruction du genre » |
| 10 | Quentin Tarantino | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Le lieu de convergence installé tôt (Inglourious Basterds)* |

### Narration : ton et émotion (pôle D3)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | The Hunters Guild: Red Hood | 3 | U×1 · I×1 | Ton visé « plus proche de Red Hood / HxH que de FMA » ; Relecture de contes (associée à Shrek, 3 oct.) |
| 2 | Hunter × Hunter | 2 | U×1 | Ton visé « plus proche de Red Hood / HxH que de FMA » |
| 3 | Game of Thrones | 1 | I×1 | « plus sérieux » |
| 3 | L'Attaque des Titans | 1 | I×1 | « tellement différent » ; « plus sérieux » |
| 3 | Quentin Tarantino | 1 | I×1 | « c'est plus Tarantino, son style et sa filmographie complète » (l'élément visé n'est pas précisé ; rangé ici par l'IA) |
| 3 | Shrek | 1 | I×1 | Relecture de contes (3 oct.) |
| 3 | The Stormlight Archive | 1 | I×1 | « ancré dans le réel (grounded) et réaliste, avec des enjeux élevés où l'on ressent la tension » |
| 3 | Watchmen | 1 | I×1 | Une de tes œuvres préférées ; Worm = « HxH + Watchmen » |
| 3 | Worm | 1 | I×1 | « rationnel et réaliste » |

### Action et combats (pôle E)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | The Stormlight Archive | 2 | U×1 | « des combats stratégiques » |
| 1 | Worm | 2 | U×1 | « J'adore les combats tactiques » |
| 3 | Capcom / Street Fighter (jeux de combat) | 1 | I×1 | Projet de jeu : personnages de mêlée à combos, légèrement transféré dans tes mangas |
| 3 | Gigantic | 1 | I×1 | Projet de jeu : modèle Gigantic (mêlée et tireurs) |
| 3 | Hunter × Hunter | 1 | I×1 | « À peu près tout ce que je dis sur Worm […] se retrouve dans Hunter x Hunter » |
| 6 | Catch (WWE, NJPW, AEW) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Dans ton répertoire (et les Huracan d'Urban Rivals), sans usage dit* |
| 6 | Dictionnaire infernal (Collin de Plancy) | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Mélye : l'épée bat l'enchantement (rejoint le plafond 1860)* |
| 6 | Films d'arts martiaux | 0.5 | H×1 | *(hypothèse IA seulement)* — *hyp. IA : Dans ton répertoire, sans usage dit* |

### Poids biographique : ce que tu dis de toi (hors œuvre)

| Rang | Influence | Score | Détail | Preuves principales |
|---:|---|---:|---|---|
| 1 | Warcraft / Hearthstone | 5 | U×2 · I×1 | « t'a donné l'envie de créer cette œuvre de fantasy » ; « grande influence sur l'esthétique d'Edenia » ; Environ huit ans de jeu (2015-2023) |
| 2 | Fondation SCP (dont la Chicago Spirit) | 2 | U×1 | « source d'inspiration première, celle qui relie énormément de choses » (surtout Arcana) |
| 2 | The Stormlight Archive | 2 | U×1 | Rangé dans les « inspirations majeures » |
| 2 | Urban Rivals | 2 | U×1 | « une énorme source d'inspiration » ; « une grande part d'influence » |
| 2 | Worm | 2 | U×1 | Rangé dans les « inspirations majeures » |
| 6 | Capcom / Street Fighter (jeux de combat) | 1 | I×1 | Projet de jeu vers 16 ans |
| 6 | H. P. Lovecraft | 1 | I×1 | « mon auteur de romans préféré » |
| 6 | Hunter × Hunter | 1 | I×1 | A détrôné One Piece vers 14 ans |
| 6 | L'Attaque des Titans | 1 | I×1 | « passé devant » |
| 6 | One Piece | 1 | I×1 | Manga préféré vers 11 ans |
| 6 | Watchmen | 1 | I×1 | « une de mes œuvres préférées » |

## 3. Synthèses

### Synthèse par pôle de ta grille (pôle D toujours présent)

| Pôle | 1ᵉʳ | 2ᵉ | 3ᵉ | 4ᵉ | 5ᵉ |
|---|---|---|---|---|---|
| **D — Narration / Scénario** | Hunter × Hunter (5) | The Stormlight Archive (5) | One Piece (3) | The Hunters Guild: Red Hood (3) | Bleach (2) |
| **C — Personnages** | Harry Potter (films et livres) (5) | Hunter × Hunter (2.5) | Légende arthurienne (Perceval, Vulgate) (2.5) | Ben 10 (2) | Fullmetal Alchemist (2) |
| **A — Visuel** | Shrek (11) | Runeterra (LoL, Arcane, Legends of Runeterra) (8) | Quirkilicious (Drake Tsui) (7) | Radiant / Fabula Fantasia (Tony Valente) (7) | Naruto (6.5) |
| **B — Monde / Système** | Dictionnaire infernal (Collin de Plancy) (15) | Folklore français (carte « Mythical Beasts of France ») (14) | Légende arthurienne (Perceval, Vulgate) (10) | Runeterra (LoL, Arcane, Legends of Runeterra) (9.5) | Fullmetal Alchemist (6) |
| **E — Action / Tactique** | The Stormlight Archive (2) | Worm (2) | Capcom / Street Fighter (jeux de combat) (1) | Gigantic (1) | Hunter × Hunter (1) |

### Classement général sur l'œuvre (somme des 12 éléments, hors biographie)

| Rang | Influence | Score total | Nombre d'éléments touchés (sur 12) | Éléments |
|---:|---|---:|---:|---|
| 1 | Runeterra (LoL, Arcane, Legends of Runeterra) | 19.5 | 7 | MONDE, TECH, SOCIETE, PERSO, TRAIT, CHARA, DECORS |
| 2 | Dictionnaire infernal (Collin de Plancy) | 17.5 | 5 | MATIERE, SOCIETE, POUVOIRS, CHARA, ACTION |
| 3 | Folklore français (carte « Mythical Beasts of France ») | 14 | 2 | MONDE, MATIERE |
| 4 | Légende arthurienne (Perceval, Vulgate) | 13.5 | 6 | MONDE, MATIERE, SOCIETE, POUVOIRS, PERSO, NARR |
| 5 | Shrek | 13 | 3 | MONDE, DECORS, TON |
| 6 | Hunter × Hunter | 10.5 | 6 | SOCIETE, POUVOIRS, PERSO, NARR, TON, ACTION |
| 6 | Naruto | 10.5 | 6 | TECH, POUVOIRS, PERSO, TRAIT, CHARA, DECORS |
| 8 | The Stormlight Archive | 10 | 5 | MONDE, PERSO, NARR, TON, ACTION |
| 9 | Harry Potter (films et livres) | 9 | 3 | SOCIETE, PERSO, CHARA |
| 9 | Radiant / Fabula Fantasia (Tony Valente) | 9 | 3 | TECH, SOCIETE, CHARA |
| 11 | Fullmetal Alchemist | 8 | 3 | MONDE, POUVOIRS, PERSO |
| 12 | One Piece | 7 | 4 | TECH, POUVOIRS, PERSO, NARR |
| 12 | Bleach | 7 | 3 | SOCIETE, POUVOIRS, NARR |
| 12 | Quirkilicious (Drake Tsui) | 7 | 1 | TRAIT |
| 15 | Occultisme et ésotérisme | 6.5 | 4 | MONDE, TECH, MATIERE, DECORS |
| 15 | Jujutsu Kaisen | 6.5 | 3 | POUVOIRS, TRAIT, CHARA |
| 15 | La Princesse et la Grenouille (Disney, 2009) | 6.5 | 3 | MONDE, MATIERE, DECORS |
| 18 | Warcraft / Hearthstone | 6 | 4 | MONDE, SOCIETE, PERSO, DECORS |
| 18 | Worm | 6 | 4 | PERSO, NARR, TON, ACTION |
| 18 | BioShock Infinite | 6 | 3 | MONDE, TECH, DECORS |

### Test de robustesse du classement général (8 premiers)

| Variante | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Barème de base (D3 E2 U2 I1 H0,5, plafond 3) | Runeterra | Dictionnaire infernal | Folklore français | Légende arthurienne | Shrek | Hunter × Hunter | Naruto | The Stormlight Archive |
| Sans les hypothèses de l'IA | Runeterra | Dictionnaire infernal | Folklore français | Shrek | Légende arthurienne | Hunter × Hunter | Naruto | The Stormlight Archive |
| Décisions très lourdes (D5 E2 U2 I1) | Runeterra | Dictionnaire infernal | Légende arthurienne | Shrek | Folklore français | Radiant / Fabula Fantasia | Hunter × Hunter | Naruto |
| Barème plat (toute preuve = 1) | Runeterra | Dictionnaire infernal | Folklore français | Shrek | Hunter × Hunter | Naruto | The Stormlight Archive | Harry Potter |
| Sans plafond | Runeterra | Shrek | Dictionnaire infernal | Folklore français | Légende arthurienne | Hunter × Hunter | Naruto | The Stormlight Archive |

### Repoussoirs (non comptés dans les scores)

| Influence | Ce qu'on évite | Source |
|---|---|---|
| Radiant / Fabula Fantasia (Tony Valente) | « distance à maintenir » sur les autres aspects, non précisés (6 oct. ; « ne porte plus nécessairement sur tout ») ; se détacher de Radiant sur le plan arthurien (décidé, portée non précisée) | YAML |
| The Seven Deadly Sins | se détacher de SDS sur le plan arthurien (décidé, portée non précisée) | YAML |
| Fullmetal Alchemist | cadre militaire : « distance à maintenir », « pour l'instant » (7 oct.) ; ton visé « plus proche de Red Hood / HxH que de FMA » | YAML |
| The Hunters Guild: Red Hood | « explication par l'antagoniste (critiquée) » | structures… §2 |
| Warcraft / Hearthstone | Warcraft perçu comme « hard rock / solennel » (une perception, pas un rejet) | Benchmark Oeuvre/01_CONTEXTE_ET_SUITE |

## 4. Ce qu'il faut retenir

1. **Runeterra est la seule influence présente à la fois dans le monde et dans tout le visuel.** Elle touche 7 éléments sur 12, dont les trois éléments visuels. Elle reste 1ʳᵉ dans 4 des 5 variantes du test de robustesse. Dans la 5ᵉ, « sans plafond », elle passe 3ᵉ, derrière Shrek et le Dictionnaire infernal. C'est cohérent avec la note du dépôt (« Référence principale du monde ») et avec ta phrase « l'esthétique d'Edenia est beaucoup plus proche de Runeterra ».
2. **La matière d'Edenia est française et occulte.** Le Dictionnaire infernal et le folklore français sont très loin devant les autres en « matière » (11 et 9 points ; le 3ᵉ en a 4). Ça colle avec ta règle « France, sinon Angleterre ou Allemagne ». Le folklore ne touche toutefois que 2 éléments : il fournit des créatures et des régions, pas encore de structure ni de personnages.
3. **Il y a un fort écart entre ce que tu dis de toi et ce qui est documenté dans Edenia.**
   - Warcraft/Hearthstone est 1er en poids biographique (« t'a donné l'envie de créer cette œuvre »), mais 18ᵉ ex aequo en traces.
   - SCP est la « source d'inspiration première », mais seulement 23ᵉ. Tu as toi-même précisé qu'elle sert surtout à Arcana.
   - Urban Rivals est une « grande part d'influence », mais 18ᵉ ex aequo. Une partie de son poids passe pourtant par le trait : Quirkilicious est l'un de ses illustrateurs (point 7).
   - Lovecraft et Watchmen, tes favoris, n'ont presque aucune trace.

   Explication possible (hypothèse de l'IA) : ces influences agissent sur des choses diffuses, comme le goût des univers hétéroclites, les designs reconnaissables ou l'envie de créer, que le YAML ne capte pas en statuts.
4. **En personnages, le classement est plat.** Harry Potter n'est 1er que parce que Harley a trois appuis dans HP (Hermione, Luna, le nom). Harley cumule 7 sources (Shallan, Hermione, Luna, Tattletale, Magik, Maka, Gwen), contre 4 pour Brann et 3 pour Cosmo.
5. **La narration et l'action sont les éléments les moins documentés.** Leurs classements reposent sur ce que tu dis des œuvres (Stormlight sans protagoniste central, « l'exposition est une épreuve » dans HxH, les combats tactiques de Worm), pas sur des choix faits pour Edenia. Ces deux classements sont donc les plus susceptibles de changer.
6. **Shrek domine le visuel des lieux, et Disney y entre.** Shrek fournit 6 des images de l'ambiance des lieux. Il est maintenant 5ᵉ au classement général, alors qu'il ne touche que 3 éléments sur 12. La Princesse et la Grenouille arrive 2ᵉ en décors et 14ᵉ au général. Avec Frère des ours et Raiponce (l'apparence de Harley), ce sont les premières traces de « Disney et Pixar », une entrée de ton répertoire qui n'en avait aucune.
7. **Ton trait vise Disney, adapté au manga, mais Quirkilicious passe en tête.** Tes mots font de Disney/Pixar la cible principale (« le style que je cherche à atteindre »), avec deux ajustements, les yeux et la forme du visage.
   - **Quirkilicious est maintenant 1er du trait (7 points).** Dans tes documents PixAI, tu écris : « Quirikilicious surtout son style sur S.I.N est le style artistique que j'aime le plus ». *SIN* est son manga en ligne, publié de 2010 à 2018 (Inkblazers, puis Webtoon) ([quirkilicious.art](https://quirkilicious.art/pages/comic)).
   - **Disney/Pixar, Gachiakuta, Shadman et atie1225 suivent à 5 points.** Chacun gagne 1 point avec ta liste « Lora Préféré » (Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks).
   - **Jujutsu Kaisen passe à 4 points** : c'est ton tag positif habituel (« Jujutsu Kaisen Style (et ces dérivés) »). Naruto et Spider-Verse restent à 2 points.
   - **Les nouveaux noms ont 1 point chacun** : DreamWorks, Kaneoya Sachiko, Jomaro Kindred, Joe Madureira et Tetsuya Nomura.
     - Pour « Kanoaya Sachiko », PixAI propose un LoRA « Kaneoya Sachiko's Art Style » ([PixAI](https://pixai.art/model/1689528845610842293)). C'est probablement lui, mais je ne l'ai pas confirmé.
     - Jomaro Kindred a été Senior Concept Artist sur *Hearthstone* ([Hearthstone Wiki](https://hearthstone.wiki.gg/wiki/Jomaro_Kindred)).
   - **Deux ponts vérifiés avec tes influences de fond.** Drake Tsui (Quirkilicious) est l'un des illustrateurs d'*Urban Rivals* depuis 2010 ([Urban Rivals Wiki](https://urban-rivals.fandom.com/wiki/Drake_Tsui)), et Jomaro Kindred vient de Hearthstone. Deux de tes références de dessin viennent donc des deux jeux que tu cites le plus en poids biographique (voir le point 3). Cela peut expliquer en partie l'écart noté au point 3 : ces jeux agissent sur ton goût visuel.
   - **Lecture du barème.** Il compte combien de fois tu as nommé quelqu'un, pas la hiérarchie dans tes phrases. Disney reste « le style que je cherche à atteindre » (une cible), et Quirkilicious « le style que j'aime le plus » (un goût). Les deux ne s'opposent pas.
   - **Au classement général**, Naruto monte à 6ᵉ ex aequo (10,5 points) grâce à la tenue de Shisui dans le test de Cosmo. Quirkilicious entre 12ᵉ ex aequo (7 points), avec un seul élément touché.

8. **Radiant est à la fois 1er en tenues et repoussoir.** C'est ton « cas spécial » : emprunt sur la tenue, distance sur le plan arthurien et sur d'autres aspects non précisés.

## 4 bis. Tes 12 images du 15 octobre (lecture de l'IA, non comptée)

*Tout ce paragraphe est mon interprétation. Rien n'y entre dans les scores, pour qu'une hypothèse de l'IA ne décide pas d'un rang. Tu as précisé le 15 octobre : elles ont été **générées avec PixAI**, pour **tester des styles et des designs**, et **aucune ne représente Brann, Cosmo ou Harley**. Ta méthode, d'après toi : modèles de base de la famille Illustrious (surtout coco-style, en versions NoobAI-XL/Illustrious : v2, v3 et surtout v7, et WAI-NSFW-illustrious v16, avant v14), très peu de LoRA (presque toujours atie1225 et Gachiakuta), et surtout des **tags** dans le prompt pour ajouter des styles, avec des personnages existants comme base. Voir `recherche_pixai/modeles_et_tags_pixai.md`.*

*Conséquence : une partie de ce que je décris ci-dessous vient du **modèle** et des **LoRA**, pas d'une influence directe. Par exemple, les hachures et le trait épais correspondent aux tags conseillés par le LoRA Gachiakuta (« bold lineart, gritty, hatching »). Les prompts de ces 12 images ne sont pas dans tes documents : je ne peux donc pas séparer les deux pour elles. Mais dans tes documents, les tags du LoRA Gachiakuta (`urana_kei, gachiakuta, official_art`) et `atie1225 style, drawing style` sont présents dans 30 recettes sur les 31 que j'ai analysées. Le trait épais et les hachures viennent donc très probablement de ces deux outils.*

Ce qui revient d'une image à l'autre :

- **Le trait** : contour noir épais à épaisseur variable, hachures de manga sur les muscles et les plis, couleur peinte en aplats ombrés plutôt qu'en cel-shading net.
- **La couleur** : forêts vert-bleu contre rouges, oranges et roses saturés.
- **Spider-Verse, le plus visible** : emblèmes d'araignée sur 5 images, trames, coups de pinceau rose-rouge et effets de décalage.
- **Les cadrages d'action** : poing ou main en raccourci vers le lecteur, plongées et contre-plongées, duo empilé façon affiche. C'est courant dans le shōnen récent ; l'attribuer à JJK en particulier serait une supposition.
- **Naruto, surtout dans les tenues** : brassard à spirale, sandales ninja, ceinture de corde et moustaches sur le garçon brun aux cheveux en pétard (2 images, ruelles médiévales).
- **Disney et le semi-réaliste** : grands yeux expressifs et visages ronds sur les filles des 2 images carrées ; la fille aux longs cheveux sombres, plus sobre, est plus proche du seinen.
- **Un détail** : une boucle en « X » jaune façon X-Men sur une image.
- **Gachiakuta, pas clairement** : je ne reconnais pas nettement son style punk-graffiti (graffitis d'Ando Hideyoshi). Les coups de pinceau façon Spider-Verse s'en approchent un peu.

## 5. Points à reporter dans le YAML (je ne l'ai pas modifié)

- Inspirations de Harley : **Maka (Soul Eater) et Luna (Harry Potter)** manquent. Tu les as données le 12 octobre.
- Les noms (Ben 10, puis GoT, puis Hearthstone pour Brann ; Gwen pour Harley) ne sont pas dans le YAML.
- **Shrek, Bleach, Radiant, Ben 10, Soul Eater et Gigantic** ne sont pas dans le répertoire de `influences-atelier.md`, alors qu'ils comptent ici.
- **Barbegazi** : « Décidé » dans la fiche créatures, « envisagé » dans le YAML. Je les ai comptés comme envisagés.
- **Fabula Fantasia** n'a pas de `statut_relation`.
- **Ambiance des lieux** (ta réponse du 12 octobre) : ajouter les nouvelles images.
  - 3 captures de Shrek : la foule aux torches, les pierres levées, la colline.
  - 2 images de La Princesse et la Grenouille, rattachées aux zones « marais » et « Nouvelle-Orléans / Caraïbes », et un peu à l'ambiance générale.
  - 1 image de Frère des ours (Disney, 2003).

  `sources_visuelles` dit encore « cinq images ».
- **La Princesse et la Grenouille**, **Frère des ours** et **Raiponce** ne sont pas dans les `references` du YAML.
- **Harley, apparence** (ta phrase du 12 octobre) : « pour moi son apparence ressemble à Raiponce de Tangled ». Une image de test de Harley existe aussi : `images/fille_pose_gon_screencap.png`, dans la pose de Gon avec un rendu de capture d'anime. Statut non précisé ; Harley reste non définie pour l'instant.
- **Trait et style de dessin** (tes phrases du 12 octobre) :
  - cible principale : Disney/Pixar, rendu plus compatible avec le manga, surtout pour les yeux et la forme du visage ;
  - goût pour le cartoon semi-réaliste ;
  - autres références : Shadman et Quirkilicious ;
  - 5 dessins de Raiponce donnés en exemple (noms de fichiers PixAI et Grok : probablement générés ou retouchés par IA).

  Le 15 octobre : « Je crois que mon style artistique se trouve dans Jujutsu Kaisen, Att1e125 [corrigé ensuite en atie1225], Shadman, Disney/Pixar, Spider-Verse, Naruto, Gachiakuta et Quirkilicious ». 12 images jointes, générées avec PixAI pour tester des styles et des designs ; aucune ne représente un des trois personnages principaux ; statut non précisé. Outils : modèles Illustrious (coco-style v2, v3, v7 ; WAI-NSFW v16), LoRA atie1225 et Gachiakuta.

  Le YAML n'a pas de rubrique pour le trait.
- **Gachiakuta, Spider-Verse et atie1225** ne sont ni dans le répertoire ni dans le YAML. C'est aussi le cas des nouveaux noms tirés des documents PixAI : DreamWorks, Kaneoya Sachiko, Jomaro Kindred, Joe Madureira, Tetsuya Nomura et The Boondocks.
- **Cosmo Dumas, test de design** (documents PixAI) : tags « (the boondocks:1.2) », « shisui uchiha », « blue tunic, baggy pants, leg bandages », « kingdom hearts / Jujutsu Kaisen / street fighter Character style », « (Occultism aesthetic), esoterism ». Le YAML ne liste que Ekko, Killua et Shisui comme inspirations, et Academy Ekko comme tenue. Statut : **un essai** (ta réponse du 15 oct.), pas une piste de design.
- **Documents titrés « Arcana »** : ta réponse du 15 oct. : les tests valent pour les deux œuvres ; certains, « ultra urbain et moderne », sont plus proches d'Arcana, mais « le style artistique sur les deux œuvres reste logiquement le même ». Je compte donc tes goûts de dessin pour Edenia, et le test de Cosmo comme un essai. Les tests sur des personnages existants (Robin, Raven, Nami, Gwen…) restent non comptés : ce sont des bases de prompt, pas des choix pour Edenia.
- **Mot « sketchy »** : tu l'as jugé trop fort et retiré le 15 oct. Il n'est plus pris en compte pour atie1225.
- **Vigilance Shadman (publication) :** plusieurs articles rapportent des dessins sexualisés de mineurs, dont des personnes réelles (par exemple l'actrice Dafne Keen, alors âgée de 12 ans), et une arrestation à Los Angeles en octobre 2021 ([Yen.com.gh](https://yen.com.gh/facts-lifehacks/biographies/201519-who-shadman-infamous-all-hentai-artist/), [Distractify](https://www.distractify.com/p/what-happened-to-shadman)). Pour un projet visant l'édition traditionnelle, mieux vaut noter **les traits précis** que tu retiens de son dessin plutôt que son nom, surtout dans tout document destiné à un éditeur. Ce n'est qu'une recommandation : la référence reste comptée, puisque tu l'as donnée.
- **Vigilance 1914 :** La Princesse et la Grenouille se passe dans les années 1920. Les décors ne posent pas de problème ; les tenues et la technologie de cette époque, si.
- **Image « grok_… »** (Shrek dans les séquoias) : à vérifier si c'est la peinture d'origine ou une version passée par Grok. Je ne l'ai pas comptée comme nouvelle, au cas où ce serait l'une des trois peintures de Shrek de la planche d'origine.

## 6. Limites

- Le choix des éléments et le classement de chaque preuve sont de moi. Une autre IA ou toi pourriez ranger certaines preuves ailleurs, par exemple Tarantino en narration plutôt qu'en ton.
- Le barème donne des points ; il ne mesure pas une « part d'influence » en pourcentage. Ne pas lire « 18,5 contre 9 » comme « deux fois plus d'influence ».
- **atie1225 : identifié, mais style non vérifié.** C'est le compte X [@atie1225](https://x.com/atie1225), au nom de « 鉄 », basé en Chine et inscrit depuis novembre 2015 ; il est aussi sur Weibo et Xiaohongshu ([fiche Danbooru](https://danbooru.donmai.us/artists/240289), 364 images répertoriées). Sa bio est marquée 🔞 : une partie de ses dessins est pour adultes. Je n'ai pas pu afficher ses images depuis mon environnement : je ne décris donc pas son style et je ne le compare pas à tes images.
- **Thèmes : pas de classement.** Aucun thème n'est décidé, et l'occultisme n'est « ni thème ni sujet central pour l'instant ».
- Pour recalculer après une modification de `PREUVES` ou du barème : `python3 classer_influences.py`. Les tableaux sont réécrits dans `_tableaux.md`.
