# -*- coding: utf-8 -*-
"""Classement des influences d'Edenia par élément du manga.

Reproductible : toutes les preuves sont dans PREUVES ci-dessous (et exportées dans preuves.csv).
Barème (une preuve = un élément documenté dans le dépôt ou dit par l'utilisateur) :
  D = 3   trace dans une décision (YAML, statut « decide »)
  E = 2   trace dans un élément envisagé (statut « envisage »)
  U = 2   déclaration explicite de l'utilisateur sur l'usage ou le poids de l'œuvre pour CET élément
          (inspiration nommée d'un personnage, aspect visé, « grande influence sur l'esthétique »…)
  I = 1   intérêt, non précisé, ou mention par l'utilisateur dans une liste de cet élément
  H = 0.5 hypothèse de l'IA non validée (affichée à part, poids faible)
Plafond : pour une même influence, dans un même élément, au plus 3 preuves de même type comptent
(pour qu'une longue liste n'écrase pas une décision).
Les repoussoirs (« distance à maintenir », « critiqué ») ne sont pas comptés : ils sont listés à part.
"""
import csv, collections, os

POINTS = {"D": 3, "E": 2, "U": 2, "I": 1, "H": 0.5}
PLAFOND = 3

CAT = collections.OrderedDict([
    ("MONDE",    "Monde : structure, zones, géographie politique (pôle B2)"),
    ("TECH",     "Technologie et époque (pôle B2)"),
    ("MATIERE",  "Matière : folklore, légendes, occultisme, au-delà (pôle B)"),
    ("SOCIETE",  "Société et institutions : rangs, titres, organisations (pôle B)"),
    ("POUVOIRS", "Pouvoirs et gimmick (pôle B2, système)"),
    ("PERSO",    "Personnages (pôle C)"),
    ("TRAIT",    "Visuel : trait et style de dessin (pôle A1)"),
    ("CHARA",    "Visuel : chara-design et tenues (pôle A3)"),
    ("DECORS",   "Visuel : décors et ambiance (pôle A2)"),
    ("NARR",     "Narration : structure et intrigue (pôle D1-D2)"),
    ("TON",      "Narration : ton et émotion (pôle D3)"),
    ("ACTION",   "Action et combats (pôle E)"),
    ("BIO",      "Poids biographique : ce que tu dis de toi (hors œuvre)"),
])
POLES = collections.OrderedDict([
    ("D — Narration / Scénario", ["NARR", "TON"]),
    ("C — Personnages", ["PERSO"]),
    ("A — Visuel", ["TRAIT", "CHARA", "DECORS"]),
    ("B — Monde / Système", ["MONDE", "TECH", "MATIERE", "SOCIETE", "POUVOIRS"]),
    ("E — Action / Tactique", ["ACTION"]),
])

RT = "Runeterra (LoL, Arcane, Legends of Runeterra)"
W3 = "The Witcher 3"
FMA = "Fullmetal Alchemist"
BSI = "BioShock Infinite"
BS1 = "BioShock (premier du nom)"
ARTH = "Légende arthurienne (Perceval, Vulgate)"
FOLK = "Folklore français (carte « Mythical Beasts of France »)"
SHREK = "Shrek"
NAR = "Naruto"
UR = "Urban Rivals"
SCP = "Fondation SCP (dont la Chicago Spirit)"
WC = "Warcraft / Hearthstone"
SA = "The Stormlight Archive"
HP = "Harry Potter (films et livres)"
OCC = "Occultisme et ésotérisme"
DI = "Dictionnaire infernal (Collin de Plancy)"
DF = "Dictionnaire féodal (1820)"
BB = "Bibliothèque bleue"
DANTE = "Dante (Inferno, Purgatorio)"
CATH = "Tradition catholique (Limbes, purgatoire)"
MARV = "X-Men / Marvel (Magik)"
DORO = "Dorohedoro"
HB = "Hellboy"
GRECO = "Folklores gréco-égyptiens"
BLEACH = "Bleach"
HXH = "Hunter × Hunter"
OP = "One Piece"
YYH = "Yu Yu Hakusho"
JJK = "Jujutsu Kaisen"
WORM = "Worm"
GOT = "Game of Thrones"
LOTR = "Le Seigneur des anneaux"
AOT = "L'Attaque des Titans"
RH = "The Hunters Guild: Red Hood"
TAR = "Quentin Tarantino"
RAD = "Radiant / Fabula Fantasia (Tony Valente)"
CAP = "Capcom / Street Fighter (jeux de combat)"
OW = "Overwatch"
GIG = "Gigantic"
BEN = "Ben 10"
SOUL = "Soul Eater"
ASIA = "Inspirations asiatiques (source non précisée)"
WATCH = "Watchmen"
MART = "Films d'arts martiaux"
CATCH = "Catch (WWE, NJPW, AEW)"
CONTES = "Contes européens (tradition)"
REN = "Renaissance (période)"
MOYA = "Moyen Âge, bas et milieu (période)"
LOVE = "H. P. Lovecraft"
PF = "La Princesse et la Grenouille (Disney, 2009)"
FDO = "Frère des ours (Disney, 2003)"
RAI = "Raiponce / Tangled (Disney, 2010)"
DISNEY = "Disney / Pixar (style d'animation)"
MANGA = "Codes du manga (yeux, forme du visage)"
SEMI = "Cartoon semi-réaliste (famille de styles)"
SHAD = "Shadman"
QUIRK = "Quirkilicious (Drake Tsui)"
ATT = "atie1225 (鉄, illustrateur sur X)"
SPV = "Spider-Verse (films d'animation Spider-Man)"
GACHI = "Gachiakuta (Kei Urana, graffitis d'Ando Hideyoshi)"
DREAM = "DreamWorks Animation (style)"
KANE = "Kaneoya Sachiko (écrit « Kanoaya Sachiko »)"
JOMARO = "Jomaro Kindred (concept artist, Hearthstone)"
MADU = "Joe Madureira"
NOMURA = "Tetsuya Nomura / Kingdom Hearts (style de personnages)"
BOON = "The Boondocks"

# (catégorie, influence, type, preuve, source)
PREUVES = [
    # ---------------- MONDE ----------------
    ("MONDE", RT, "U", "Note du dépôt : « Référence principale du monde. Edenia en est proche »", "YAML"),
    ("MONDE", RT, "E", "Plan politique envisagé (royaume principal, cités-États, royaumes adjacents) ; modèle de monde « W3 + Runeterra + FMA »", "YAML, U 11 oct."),
    ("MONDE", RT, "I", "Zone de brouillon « Nouvelle-Orléans / Caraïbes » inspirée de Bilgewater", "YAML (intérêt)"),
    ("MONDE", RT, "I", "Zone de brouillon « Piltover / Columbia »", "YAML (intérêt)"),
    ("MONDE", W3, "U", "Aspect visé : structure du monde (« U avait déjà cité The Witcher 3 comme modèle du monde »)", "YAML"),
    ("MONDE", W3, "E", "Plan envisagé ; modèle de monde « W3 + Runeterra + FMA »", "YAML, U 11 oct."),
    ("MONDE", W3, "I", "Zone marais : le brouillon cite Velen", "YAML (intérêt)"),
    ("MONDE", FMA, "E", "Plan envisagé ; modèle de monde « W3 + Runeterra + FMA »", "YAML, U 11 oct."),
    ("MONDE", FMA, "I", "« FMA correspond au modèle un pays principal, avec des régions culturelles et des voisins »", "YAML (intérêt)"),
    ("MONDE", BSI, "D", "Zone industrielle de type BioShock Infinite", "YAML (décidé)"),
    ("MONDE", BSI, "I", "Zone de brouillon « Piltover / Columbia »", "YAML (intérêt)"),
    ("MONDE", BS1, "I", "« Piltover-BioShock 1 / Gadgetzan » (brouillon) ; source de la zone mafieuse", "YAML ; U 12 oct."),
    ("MONDE", ARTH, "D", "Lieux décidés Brocéliande et Le Lac ; règle « lieux arthuriens français uniquement »", "YAML (décidé)"),
    ("MONDE", ARTH, "E", "Six lieux envisagés (Douloureuse Garde, Bénoïc, Gaunes, Trèbes, Montlair, Terre Déserte)", "YAML (envisagé)"),
    ("MONDE", ARTH, "I", "Zone de brouillon « Brocéliande, forêt féerique avec une école »", "YAML (intérêt)"),
    ("MONDE", FOLK, "E", "Région montagnarde enneigée (décidée) avec les Barbegazi comme créature locale (envisagés)", "YAML"),
    ("MONDE", FOLK, "U", "Héritage francophone gardé entre les zones", "U 12 oct."),
    ("MONDE", FOLK, "I", "Héritages « répartis par régions » (une des deux façons retenues)", "YAML"),
    ("MONDE", OCC, "U", "Règle France, sinon Angleterre et Allemagne : « pays principaux de l'occultisme »", "U 12 oct."),
    ("MONDE", SHREK, "I", "Zone marais « style bayou ou marais de Shrek »", "YAML (intérêt)"),
    ("MONDE", UR, "U", "« attrait […] pour les univers hétéroclites, avec des gangs et des designs reconnaissables »", "influences-atelier.md"),
    ("MONDE", UR, "I", "Aspect visé : plusieurs zones culturelles dans un même lieu", "YAML (intérêt)"),
    ("MONDE", SCP, "U", "Chicago Spirit citée comme source de la zone mafieuse ; structure sociale gardée", "U 12 oct."),
    ("MONDE", WC, "I", "Gadgetzan dans la liste de zones du brouillon (rapprochement déjà fait par toi)", "YAML ; U 12 oct."),
    ("MONDE", WC, "H", "Monde en mosaïque de factions hérité des jeux de cartes (principe P-D)", "IA, 12 oct."),
    ("MONDE", PF, "I", "Les deux images vont à la zone marais (« style bayou »)", "U 12 oct. ; zone en intérêt"),
    ("MONDE", PF, "I", "Les deux images vont à la zone Nouvelle-Orléans / Caraïbes", "U 12 oct. ; zone en intérêt"),
    ("MONDE", SA, "I", "Zone désertique pensée d'après les Plaines Brisées de Roshar", "U 12 oct."),
    # ---------------- TECH ----------------
    ("TECH", BSI, "I", "Contrainte liée dans la fiche : le plafond technologique (1950, baisse à 1914 envisagée)", "YAML"),
    ("TECH", BSI, "H", "1914 (envisagé) proche de 1912, date de BioShock Infinite", "IA (déduction 7)"),
    ("TECH", OCC, "U", "Occultisme des années 1890-1910 en tête ; « je ne veux pas dépasser 1914 »", "U 12 oct."),
    ("TECH", OCC, "H", "1914 ferme aussi la grande époque des sociétés occultes (Belle Époque)", "IA (abduction 10)"),
    ("TECH", SCP, "I", "Chicago Spirit, organisation du début du XXᵉ siècle, gardée sous 1914", "U 12 oct."),
    ("TECH", BS1, "I", "Gardé seulement pour ce qui tient sous 1914", "U 12 oct."),
    ("TECH", RAD, "I", "Cadre temporel flou comme Radiant", "YAML"),
    ("TECH", RT, "I", "Cadre temporel flou comme Runeterra", "YAML"),
    ("TECH", RT, "H", "Inégalité régionale par les ressources « comme les autres modèles » (Piltover)", "IA (interprétation)"),
    ("TECH", OP, "I", "Cadre temporel flou comme One Piece", "YAML"),
    ("TECH", NAR, "I", "Cadre temporel flou comme Naruto", "YAML"),
    ("TECH", REN, "I", "Renaissance : science, folklore, superstitions, croyances, magie", "YAML (intérêt)"),
    ("TECH", MOYA, "I", "Bas et milieu Moyen Âge", "YAML (intérêt)"),
    # ---------------- MATIERE ----------------
    ("MATIERE", DI, "D", "Agrippa", "YAML (décidé)"),
    ("MATIERE", DI, "E", "Gremory/Gomory", "YAML (envisagé)"),
    ("MATIERE", DI, "E", "Furfur", "YAML (envisagé)"),
    ("MATIERE", DI, "E", "Marbas", "YAML (envisagé)"),
    ("MATIERE", DI, "E", "Stolas", "YAML (envisagé)"),
    ("MATIERE", DI, "I", "Figures non précisées : Faust, Albert le Grand, Grandier, Merlin, Abel de Larue", "YAML"),
    ("MATIERE", DI, "I", "Cour infernale", "YAML (intérêt)"),
    ("MATIERE", FOLK, "E", "Barbegazi", "YAML (envisagé)"),
    ("MATIERE", FOLK, "E", "Mélusine", "YAML (envisagé)"),
    ("MATIERE", FOLK, "E", "Ankou", "YAML (envisagé)"),
    ("MATIERE", FOLK, "E", "Mourioche, Petit Homme rouge, Gayant, Houeron, Tarasque", "YAML (envisagé)"),
    ("MATIERE", FOLK, "I", "Loup-garou, Vouivre, Fée…", "YAML (intérêt)"),
    ("MATIERE", FOLK, "I", "Gargouille, Dame verte, Chien noir de Pontgibaud…", "YAML (intérêt)"),
    ("MATIERE", FOLK, "I", "Les 24 créatures de la carte en intérêt", "YAML (intérêt)"),
    ("MATIERE", ARTH, "D", "Personnages arthuriens : des inspirations seulement, sous d'autres noms", "YAML (décidé)"),
    ("MATIERE", OCC, "I", "Penche vers l'ambiance (symboles, décors, objets rituels) ; livres de sorts : « ce qui compte surtout : les symboles sur le livre » ; volontairement non tranché", "YAML, U 7 oct."),
    ("MATIERE", REN, "I", "Renaissance : folklore, superstitions, croyances, magie", "YAML (intérêt)"),
    ("MATIERE", BB, "I", "Le contenu des livres de la Bibliothèque bleue", "YAML (intérêt)"),
    ("MATIERE", BB, "H", "Matrice commune de la chevalerie, du conte et de la superstition", "IA (abduction 4)"),
    ("MATIERE", DANTE, "I", "Inferno", "YAML (intérêt)"),
    ("MATIERE", DANTE, "I", "Purgatorio", "YAML (intérêt)"),
    ("MATIERE", CATH, "I", "Limbo catholique", "YAML (intérêt)"),
    ("MATIERE", CATH, "I", "Purgatoire classique", "YAML (intérêt)"),
    ("MATIERE", MARV, "I", "Limbo de Magik", "YAML (intérêt)"),
    ("MATIERE", DORO, "I", "Enfer et démons de Dorohedoro", "YAML (intérêt)"),
    ("MATIERE", W3, "I", "Chasse sauvage, découverte avec The Witcher 3", "YAML, fiche créatures"),
    ("MATIERE", HB, "I", "Chasse sauvage, retrouvée dans Hellboy", "fiche créatures"),
    ("MATIERE", UR, "I", "Yétis (groupe), inspirés des Frozn", "YAML (intérêt)"),
    ("MATIERE", PF, "H", "Masques, statuettes et bougies du salon : l'occultisme d'ambiance vers lequel tu penches", "IA, 12 oct."),
    ("MATIERE", GRECO, "I", "Corpus cité, sans usage précisé", "YAML"),
    # ---------------- SOCIETE ----------------
    ("SOCIETE", DI, "U", "Aspect visé : les hiérarchies", "YAML"),
    ("SOCIETE", DI, "I", "Cour infernale", "YAML (intérêt)"),
    ("SOCIETE", DI, "H", "L'enfer copie la monarchie humaine (Abigor, Adraméleck, Léonard dans tes extraits)", "IA (déduction 4, L3)"),
    ("SOCIETE", DF, "I", "Source documentaire du dépôt (titres, chevalerie, champions)", "YAML (dépôt)"),
    ("SOCIETE", DF, "H", "Chevalerie interdite au roturier", "IA (BRIEF A5)"),
    ("SOCIETE", BLEACH, "U", "Aspect visé : la structure du Gotei 13", "YAML, U 8 oct."),
    ("SOCIETE", HXH, "I", "Gimmick Hunter : un statut délivré par une institution", "YAML"),
    ("SOCIETE", RH, "H", "Modèle de la guilde", "IA (7 oct.)"),
    ("SOCIETE", RT, "E", "École ou académie à cadre vestimentaire imposé (envisagée) ; tenue Academy Ekko", "YAML"),
    ("SOCIETE", HP, "I", "École de type Harry Potter à Brocéliande", "YAML (intérêt)"),
    ("SOCIETE", ARTH, "H", "Goal « devenir chevalier » = goal d'ouverture de Perceval", "IA (déduction 5)"),
    ("SOCIETE", RAD, "I", "Tenue Fabula Fantasia : « surtout pour des personnages de profession Chevalier »", "YAML"),
    ("SOCIETE", SCP, "U", "Zone mafieuse : seulement la structure sociale", "U 12 oct."),
    ("SOCIETE", WC, "I", "Gadgetzan : ville tenue par des familles criminelles", "U 12 oct."),
    # ---------------- POUVOIRS ----------------
    ("POUVOIRS", FMA, "U", "Aspect visé : les deux traditions d'alchimie", "YAML"),
    ("POUVOIRS", FMA, "I", "Gimmick Alchimiste", "YAML"),
    ("POUVOIRS", BLEACH, "U", "Aspect visé : le Bankai", "YAML, U 8 oct."),
    ("POUVOIRS", BLEACH, "I", "Gimmick Shinigami", "YAML"),
    ("POUVOIRS", OP, "I", "Gimmick Pirate", "YAML"),
    ("POUVOIRS", NAR, "I", "Gimmick Ninja", "YAML"),
    ("POUVOIRS", HXH, "I", "Gimmick Hunter", "YAML"),
    ("POUVOIRS", JJK, "H", "« Version améliorée et modernisée de Bleach et de YYH » (ton jugement, pas un usage)", "YAML, U 8 oct."),
    ("POUVOIRS", ARTH, "H", "« Chevalier » comme gimmick latent", "IA (abduction 3)"),
    ("POUVOIRS", DI, "H", "Grandier comme matière du gimmick Exorciste ; rites à conditions", "IA (addendum §8)"),
    # ---------------- PERSO ----------------
    ("PERSO", OP, "U", "Luffy, inspiration de Brann", "YAML"),
    ("PERSO", YYH, "U", "Yusuke, inspiration de Brann", "YAML"),
    ("PERSO", FMA, "U", "Edward, inspiration de Brann", "YAML"),
    ("PERSO", ARTH, "U", "Perceval, inspiration de Brann", "YAML"),
    ("PERSO", ARTH, "H", "Goal de Brann = goal d'ouverture de Perceval", "IA (déduction 5)"),
    ("PERSO", RT, "U", "Ekko, inspiration de Cosmo", "YAML"),
    ("PERSO", HXH, "U", "Killua, inspiration de Cosmo", "YAML"),
    ("PERSO", HXH, "H", "Cosmo construit comme le « second aimé »", "IA (induction 4)"),
    ("PERSO", NAR, "U", "Shisui, inspiration de Cosmo", "YAML"),
    ("PERSO", SA, "U", "Shallan, inspiration de Harley", "YAML"),
    ("PERSO", HP, "U", "Hermione, inspiration de Harley", "YAML"),
    ("PERSO", HP, "U", "Luna Lovegood, personnalité visée pour Harley", "U 12 oct."),
    ("PERSO", HP, "I", "Le nom « Harley » rapproche d'Hermione", "U 12 oct."),
    ("PERSO", WORM, "U", "Tattletale, inspiration de Harley", "YAML"),
    ("PERSO", MARV, "U", "Magik, inspiration de Harley", "YAML"),
    ("PERSO", SOUL, "U", "Maka Albarn, personnalité visée pour Harley", "U 12 oct."),
    ("PERSO", BEN, "I", "Gwen Tennyson : prénom et modèle d'origine de Harley", "U 12 oct."),
    ("PERSO", BEN, "I", "« Bran » rapproché de Ben 10", "U 12 oct."),
    ("PERSO", GOT, "I", "Le nom « Bran » vient de GoT", "U 12 oct."),
    ("PERSO", WC, "I", "« Brann » vient de Hearthstone", "U 12 oct."),
    # ---------------- TRAIT ----------------
    ("TRAIT", DISNEY, "U", "« Disney Pixar est le style que je cherche à atteindre »", "U 12 oct."),
    ("TRAIT", MANGA, "U", "« légèrement différent, pour qu'il soit plus manga compatible, c'est surtout pour les yeux et la forme du visage »", "U 12 oct."),
    ("TRAIT", SEMI, "U", "« J'aime bien le style semi-realistic cartoon, je trouve que ça peut rendre bien en manga »", "U 12 oct."),
    ("TRAIT", SHAD, "U", "« Mes autres références en termes de dessin »", "U 12 oct."),
    ("TRAIT", QUIRK, "U", "« Mes autres références en termes de dessin »", "U 12 oct."),
    ("TRAIT", JJK, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", ATT, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", SHAD, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", DISNEY, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", SPV, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", NAR, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", GACHI, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", QUIRK, "U", "« Je crois que mon style artistique se trouve dans […] » (liste de 8 noms)", "U 15 oct."),
    ("TRAIT", ATT, "U", "« Atie1225 me sert plus comme un Lora de base » (le mot « sketchy », jugé trop fort, retiré par toi le 15 oct.)", "U 15 oct."),
    ("TRAIT", GACHI, "U", "« Gachiakuta (il y a deux modèles que j'utilise), c'est le deuxième Lora qui me sert de base »", "U 15 oct."),
    ("TRAIT", QUIRK, "U", "« Quirikilicious surtout son style sur S.I.N est le style artistique que j'aime le plus »", "doc. PixAI « Arcana 2 » (PDF, sept.)"),
    ("TRAIT", JJK, "U", "Tag positif habituel : « Jujutsu Kaisen Style (et ces dérivés) »", "doc. PixAI « Arcana 2 » (PDF, sept.)"),
    ("TRAIT", CAP, "I", "Tags habituels : « parfois Street Fighters Characters »", "doc. PixAI « Arcana 2 » (PDF, sept.)"),
    ("TRAIT", SHAD, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", GACHI, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", ATT, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", KANE, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", QUIRK, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", DISNEY, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", DREAM, "I", "« Lora Préféré : Shadman, Gachiakuta, Attie, Kanoaya Sachiko, Quirkilicious, Disney Pixar, DreamWorks »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", JOMARO, "I", "« Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", MADU, "I", "« Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", NOMURA, "I", "« Artiste non loraisé mais que j'aime bien : Jomaro Kindred, Joe Madureira, Tetsuya Nomura »", "doc. PixAI « Arcana Art », partie 1 (PDF, sept.)"),
    ("TRAIT", RAI, "I", "Cinq dessins de Raiponce donnés comme exemples du style cherché", "U 12 oct."),
    ("TRAIT", RT, "I", "Art de Runeterra perçu comme « plus semi-réaliste stylisé et plus compatible avec le manga shōnen »", "Benchmark Oeuvre/01_CONTEXTE_ET_SUITE"),
    # ---------------- CHARA ----------------
    ("CHARA", RT, "D", "« Archaïque mais pas trop » (décidé), inspiré de Radiant et de Runeterra", "YAML"),
    ("CHARA", RT, "U", "Emprunt de tenue : Academy Ekko, « tenue qui l'inspire le plus » (Cosmo)", "YAML, U 7 oct."),
    ("CHARA", RAD, "D", "« Archaïque mais pas trop » (décidé), inspiré de Radiant et de Runeterra", "YAML"),
    ("CHARA", RAD, "U", "Emprunt de tenue : « style copié/inspiré de Radiant »", "YAML, U 7 oct."),
    ("CHARA", RAD, "U", "Fabula Fantasia : tenue de Brann (« moins claire »)", "YAML"),
    ("CHARA", HP, "E", "Harry Potter (films) : aspect visé esthétique et visuels", "YAML (envisagé)"),
    ("CHARA", HP, "I", "Test de tenue « proche de Harry Potter », dont tu aimes beaucoup le rendu", "YAML"),
    ("CHARA", JJK, "I", "Même test de tenue : « un peu de Jujutsu Kaisen »", "YAML"),
    ("CHARA", CAP, "U", "Projet de jeu à 16 ans : « esthétique Capcom de Street Fighter », légèrement transféré dans tes mangas", "influences-atelier.md"),
    ("CHARA", UR, "U", "« des designs reconnaissables » ; designs du projet de jeu", "influences-atelier.md"),
    ("CHARA", OW, "I", "Designs du projet de jeu", "influences-atelier.md"),
    ("CHARA", DI, "U", "Gremory, Furfur, Marbas et Stolas sont choisis « surtout pour leur design et leur représentation artistique »", "YAML, fiche créatures"),
    ("CHARA", RAI, "U", "Harley : « pour moi son apparence ressemble à Raiponce de Tangled »", "U 12 oct."),
    ("CHARA", RAI, "H", "Raiponce est un conte des Grimm, donc allemand : cohérent avec ta règle France, Angleterre, Allemagne", "IA, 12 oct."),
    ("CHARA", NAR, "H", "Ch. 679 : tenues d'aventuriers de fantasy européenne (cotte de mailles, cape, chapeau de mage)", "IA, 12 oct."),
    ("CHARA", ASIA, "E", "Personnages d'inspiration asiatique", "YAML (envisagé)"),
    ("CHARA", ASIA, "I", "Objets bouddhiques japonais", "YAML (intérêt)"),
    ("CHARA", BOON, "I", "Cosmo, test de design : « (the boondocks:1.2) »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    ("CHARA", NAR, "I", "Cosmo, test de design : « shisui uchiha », « blue tunic, baggy pants, leg bandages »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    ("CHARA", NOMURA, "I", "Cosmo, test de design : « kingdom hearts Character style »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    ("CHARA", JJK, "I", "Cosmo, test de design : « Jujutsu Kaisen Character style »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    ("CHARA", CAP, "I", "Cosmo, test de design : « street fighter Characters style »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    # ---------------- DECORS ----------------
    ("DECORS", OCC, "I", "Cosmo, test de design : « (Occultism aesthetic), esoterism »", "tests PixAI « Cosmo Dumas » (docs Arcana 2 et Arcana Art, sept.)"),
    ("DECORS", SHREK, "D", "Forêt de conte (décidée) : 3 des 5 images de décor sont des peintures de développement de Shrek", "YAML"),
    ("DECORS", SHREK, "E", "Ambiance des lieux (envisagée) : peinture de développement de Shrek n° 1 (planche d'origine)", "YAML"),
    ("DECORS", SHREK, "E", "Ambiance des lieux : peinture de développement de Shrek n° 2 (planche d'origine)", "YAML"),
    ("DECORS", SHREK, "E", "Ambiance des lieux : peinture de développement de Shrek n° 3 (planche d'origine)", "YAML"),
    ("DECORS", SHREK, "E", "Ambiance des lieux : foule aux torches et épouvantail au crépuscule", "U 12 oct."),
    ("DECORS", SHREK, "E", "Ambiance des lieux : pierres levées au clair de lune", "U 12 oct."),
    ("DECORS", SHREK, "E", "Ambiance des lieux : colline et grand arbre au coucher du soleil", "U 12 oct."),
    ("DECORS", SHREK, "I", "Marais de Shrek", "YAML (intérêt)"),
    ("DECORS", SHREK, "I", "Test de tenue dans un lieu « Shrekien »", "YAML"),
    ("DECORS", NAR, "I", "Forêt de conte : 1 des 5 images (ch. 679)", "YAML"),
    ("DECORS", NAR, "E", "Ambiance des lieux (envisagée) : double page couleur du ch. 679", "YAML"),
    ("DECORS", WC, "U", "« grande influence sur l'esthétique […] surtout les paysages forestiers »", "influences-atelier.md"),
    ("DECORS", WC, "H", "The Witchwood : forêt corrompue, loups-garous", "IA (§11.1)"),
    ("DECORS", RT, "U", "« Mais en vrai, l'esthétique d'Edenia est beaucoup plus proche de Runeterra » (dit à propos des paysages)", "influences-atelier.md"),
    ("DECORS", BSI, "H", "Le « type BioShock Infinite » de la zone industrielle est aussi un modèle visuel", "IA"),
    ("DECORS", PF, "E", "Ambiance des lieux : marais bleu, bateau coincé dans un cyprès (arbre de Mama Odie)", "U 12 oct."),
    ("DECORS", PF, "E", "Ambiance des lieux : salon du sorcier (« Dr. Duvalier », masques, bougies, cartes)", "U 12 oct."),
    ("DECORS", FDO, "E", "Ambiance des lieux : vallée, rivière et montagnes", "U 12 oct."),
    ("DECORS", CONTES, "U", "« atmosphère de conte européen au sens large (tous types de contes) »", "YAML"),
    # ---------------- NARR ----------------
    ("NARR", SA, "U", "Seule œuvre citée sans protagoniste central ; « peut avoir des répercussions sur comment [tu traites] Edenia »", "structures… §34"),
    ("NARR", SA, "I", "Narration différente de celle du Seigneur des anneaux", "structures… §32"),
    ("NARR", SA, "I", "« cette impression de maîtrise »", "influences-atelier.md"),
    ("NARR", GOT, "I", "Pas de protagoniste central (ta correction)", "structures… §34"),
    ("NARR", ARTH, "I", "Vulgate : pas de protagoniste central", "structures… §34"),
    ("NARR", HXH, "U", "« l'exposition est une épreuve » (ton addendum)", "structures… §2"),
    ("NARR", HXH, "I", "Pas de schéma répété ; exception tardive au protagoniste central", "structures… §32, §34"),
    ("NARR", OP, "U", "« montrée, pas dite » (ton addendum)", "structures… §2"),
    ("NARR", OP, "I", "Schéma répété", "structures… §32"),
    ("NARR", LOTR, "I", "Schéma répété", "structures… §32"),
    ("NARR", BLEACH, "U", "Aspect visé : « la narration sur le Gotei 13 »", "YAML, U 8 oct."),
    ("NARR", WORM, "I", "« surtout à partir de l'arc 3, où ils font un braquage » ; « déconstruction du genre »", "influences-atelier.md"),
    ("NARR", AOT, "I", "« impression de maîtrise »", "influences-atelier.md"),
    ("NARR", TAR, "H", "Le lieu de convergence installé tôt (Inglourious Basterds)", "IA (structures… §2, P5)"),
    # ---------------- TON ----------------
    ("TON", HXH, "U", "Ton visé « plus proche de Red Hood / HxH que de FMA »", "YAML, U 7 oct."),
    ("TON", RH, "U", "Ton visé « plus proche de Red Hood / HxH que de FMA »", "YAML, U 7 oct."),
    ("TON", TAR, "I", "« c'est plus Tarantino, son style et sa filmographie complète » (l'élément visé n'est pas précisé ; rangé ici par l'IA)", "YAML, U 8 oct."),
    ("TON", RH, "I", "Relecture de contes (associée à Shrek, 3 oct.)", "YAML"),
    ("TON", SHREK, "I", "Relecture de contes (3 oct.)", "YAML"),
    ("TON", GOT, "I", "« plus sérieux »", "influences-atelier.md"),
    ("TON", AOT, "I", "« tellement différent » ; « plus sérieux »", "influences-atelier.md"),
    ("TON", WORM, "I", "« rationnel et réaliste »", "influences-atelier.md"),
    ("TON", SA, "I", "« ancré dans le réel (grounded) et réaliste, avec des enjeux élevés où l'on ressent la tension »", "influences-atelier.md"),
    ("TON", WATCH, "I", "Une de tes œuvres préférées ; Worm = « HxH + Watchmen »", "influences-atelier.md, YAML"),
    # ---------------- ACTION ----------------
    ("ACTION", WORM, "U", "« J'adore les combats tactiques »", "influences-atelier.md"),
    ("ACTION", SA, "U", "« des combats stratégiques »", "influences-atelier.md"),
    ("ACTION", CAP, "I", "Projet de jeu : personnages de mêlée à combos, légèrement transféré dans tes mangas", "influences-atelier.md"),
    ("ACTION", GIG, "I", "Projet de jeu : modèle Gigantic (mêlée et tireurs)", "influences-atelier.md"),
    ("ACTION", HXH, "I", "« À peu près tout ce que je dis sur Worm […] se retrouve dans Hunter x Hunter »", "influences-atelier.md"),
    ("ACTION", MART, "H", "Dans ton répertoire, sans usage dit", "répertoire"),
    ("ACTION", CATCH, "H", "Dans ton répertoire (et les Huracan d'Urban Rivals), sans usage dit", "répertoire"),
    ("ACTION", DI, "H", "Mélye : l'épée bat l'enchantement (rejoint le plafond 1860)", "IA (addendum §8.4 F)"),
    # ---------------- BIO ----------------
    ("BIO", WC, "U", "« t'a donné l'envie de créer cette œuvre de fantasy »", "U 12 oct."),
    ("BIO", WC, "U", "« grande influence sur l'esthétique d'Edenia »", "influences-atelier.md"),
    ("BIO", WC, "I", "Environ huit ans de jeu (2015-2023)", "U 12 oct. ; calendrier vérifié"),
    ("BIO", SCP, "U", "« source d'inspiration première, celle qui relie énormément de choses » (surtout Arcana)", "influences-atelier.md"),
    ("BIO", UR, "U", "« une énorme source d'inspiration » ; « une grande part d'influence »", "influences-atelier.md"),
    ("BIO", WORM, "U", "Rangé dans les « inspirations majeures »", "influences-atelier.md"),
    ("BIO", SA, "U", "Rangé dans les « inspirations majeures »", "influences-atelier.md"),
    ("BIO", HXH, "I", "A détrôné One Piece vers 14 ans", "influences-atelier.md"),
    ("BIO", OP, "I", "Manga préféré vers 11 ans", "influences-atelier.md"),
    ("BIO", AOT, "I", "« passé devant »", "influences-atelier.md"),
    ("BIO", LOVE, "I", "« mon auteur de romans préféré »", "influences-atelier.md"),
    ("BIO", WATCH, "I", "« une de mes œuvres préférées »", "influences-atelier.md"),
    ("BIO", CAP, "I", "Projet de jeu vers 16 ans", "influences-atelier.md"),
]

REPOUSSOIRS = [
    (RAD, "« distance à maintenir » sur les autres aspects, non précisés (6 oct. ; « ne porte plus nécessairement sur tout ») ; se détacher de Radiant sur le plan arthurien (décidé, portée non précisée)", "YAML"),
    ("The Seven Deadly Sins", "se détacher de SDS sur le plan arthurien (décidé, portée non précisée)", "YAML"),
    (FMA, "cadre militaire : « distance à maintenir », « pour l'instant » (7 oct.) ; ton visé « plus proche de Red Hood / HxH que de FMA »", "YAML"),
    (RH, "« explication par l'antagoniste (critiquée) »", "structures… §2"),
    (WC, "Warcraft perçu comme « hard rock / solennel » (une perception, pas un rejet)", "Benchmark Oeuvre/01_CONTEXTE_ET_SUITE"),
]


# Liste complète. (groupe, nom, influence canonique dans PREUVES ou None, statut_relation dans le YAML ou "")
REPERTOIRE = [
    ("Littérature, mythes et imaginaires", "The Stormlight Archive", SA, "influence"),
    ("Littérature, mythes et imaginaires", "Game of Thrones", GOT, "influence"),
    ("Littérature, mythes et imaginaires", "La légende arthurienne", ARTH, ""),
    ("Littérature, mythes et imaginaires", "Harry Potter", HP, "influence (films et livres)"),
    ("Littérature, mythes et imaginaires", "H. P. Lovecraft", LOVE, ""),
    ("Littérature, mythes et imaginaires", "Le Seigneur des anneaux", LOTR, "influence"),
    ("Littérature, mythes et imaginaires", "The Kingkiller Chronicle", None, "influence"),
    ("Littérature, mythes et imaginaires", "Mother of Learning", None, ""),
    ("Littérature, mythes et imaginaires", "La Horde du Contrevent", None, "référence (« sans doute un peu moins »)"),
    ("Littérature, mythes et imaginaires", "Shakespeare", None, ""),
    ("Littérature, mythes et imaginaires", "La Fondation SCP", SCP, ""),
    ("Littérature, mythes et imaginaires", "The Magnus Archives", None, ""),
    ("Littérature, mythes et imaginaires", "L'occultisme, l'ésotérisme", OCC, ""),
    ("Comics et super-héros", "Worm / Parahumans", WORM, "influence"),
    ("Comics et super-héros", "Watchmen (comic, série)", WATCH, ""),
    ("Comics et super-héros", "X-Men", MARV, ""),
    ("Comics et super-héros", "Batman", None, ""),
    ("Comics et super-héros", "Spider-Man", SPV, ""),
    ("Comics et super-héros", "Invincible", None, ""),
    ("Comics et super-héros", "Hellboy", HB, ""),
    ("Comics et super-héros", "Deadly Class", None, ""),
    ("Comics et super-héros", "Teen Titans", None, ""),
    ("Comics et super-héros", "Joe Madureira", None, ""),
    ("Comics et super-héros", "Marvel Rivals", None, ""),
    ("Manga et animation", "Yu Yu Hakusho", YYH, "influence"),
    ("Manga et animation", "Hunter x Hunter", HXH, "influence"),
    ("Manga et animation", "Jujutsu Kaisen", JJK, "influence"),
    ("Manga et animation", "JoJo's Bizarre Adventure (parties 4 et 5)", None, ""),
    ("Manga et animation", "Naruto", NAR, "influence"),
    ("Manga et animation", "L'Attaque des Titans", AOT, ""),
    ("Manga et animation", "One Piece", OP, "influence"),
    ("Manga et animation", "Dorohedoro", DORO, ""),
    ("Manga et animation", "Solo Leveling", None, ""),
    ("Manga et animation", "Fullmetal Alchemist", FMA, "référence"),
    ("Manga et animation", "The Hunters Guild: Red Hood", RH, "influence + référence"),
    ("Manga et animation", "World Trigger", None, ""),
    ("Manga et animation", "Magi", None, ""),
    ("Manga et animation", "The Seven Deadly Sins", None, "(repoussoir arthurien)"),
    ("Manga et animation", "Steins;Gate", None, ""),
    ("Manga et animation", "Bakemonogatari", None, ""),
    ("Manga et animation", "Kekkai Sensen", None, ""),
    ("Manga et animation", "Haikyu!!", None, ""),
    ("Manga et animation", "Hayao Miyazaki", None, ""),
    ("Jeux vidéo et univers associés", "World of Warcraft, Hearthstone", WC, "influence"),
    ("Jeux vidéo et univers associés", "League of Legends, Legends of Runeterra, Arcane", RT, "influence"),
    ("Jeux vidéo et univers associés", "The Witcher (surtout The Witcher 3)", W3, "référence"),
    ("Jeux vidéo et univers associés", "BioShock (série)", BSI, "influence (Infinite)"),
    ("Jeux vidéo et univers associés", "Urban Rivals", UR, "référence"),
    ("Jeux vidéo et univers associés", "Grand Theft Auto V", None, ""),
    ("Jeux vidéo et univers associés", "Street Fighter, Marvel vs. Capcom, Capcom vs. SNK, SNK, Capcom", CAP, ""),
    ("Jeux vidéo et univers associés", "Overwatch", OW, ""),
    ("Jeux vidéo et univers associés", "Final Fantasy", None, ""),
    ("Jeux vidéo et univers associés", "Tekken", None, ""),
    ("Jeux vidéo et univers associés", "Apex Legends", None, ""),
    ("Cinéma, séries et spectacle", "Breaking Bad", None, ""),
    ("Cinéma, séries et spectacle", "Quentin Tarantino", TAR, "influence"),
    ("Cinéma, séries et spectacle", "Doctor Who", None, ""),
    ("Cinéma, séries et spectacle", "The X-Files", None, ""),
    ("Cinéma, séries et spectacle", "Terminator (1 et 2)", None, ""),
    ("Cinéma, séries et spectacle", "Alien", None, ""),
    ("Cinéma, séries et spectacle", "Mad Max", None, ""),
    ("Cinéma, séries et spectacle", "Disney et Pixar (dont La Princesse et la Grenouille, Frère des ours, Raiponce)", (PF, FDO, RAI, DISNEY), ""),
    ("Cinéma, séries et spectacle", "Les Affranchis", None, ""),
    ("Cinéma, séries et spectacle", "Fargo (saisons 1 et 2)", None, ""),
    ("Cinéma, séries et spectacle", "Films d'arts martiaux", MART, ""),
    ("Cinéma, séries et spectacle", "Le catch", CATCH, ""),
]
HORS_REPERTOIRE = [
    (DI, "YAML (source documentaire) ; extraits dans Pdfmd/"),
    (FOLK, "YAML, fiche créatures"),
    (DF, "YAML (source documentaire, apportée par le dépôt)"),
    (BB, "YAML"),
    (DANTE, "YAML (au-delà)"),
    (CATH, "YAML (au-delà)"),
    (GRECO, "YAML (corpus de traditions)"),
    (CONTES, "YAML (ambiance des lieux)"),
    (REN, "YAML (brouillons)"),
    (MOYA, "YAML (brouillons)"),
    (SHREK, "YAML (influence) ; DreamWorks, donc pas dans « Disney et Pixar »"),
    (RAD, "YAML (référence, « un cas spécial ») ; Fabula Fantasia sans statut_relation"),
    (BLEACH, "YAML (référence)"),
    (ASIA, "YAML (envisagé)"),
    (BEN, "conversation du 12 oct. (noms)"),
    (SOUL, "conversation du 12 oct. (Maka)"),
    (GIG, "récit de influences-atelier.md (projet de jeu)"),
    (BS1, "conversation du 12 oct. (zone mafieuse)"),
    (SHAD, "conversations du 12 et du 15 oct. (références de dessin)"),
    (QUIRK, "conversations du 12 et du 15 oct. (références de dessin) ; doc. PixAI (« le style artistique que j'aime le plus »)"),
    (ATT, "conversation du 15 oct. (style artistique ; écrit d'abord « Att1e125 », corrigé en « atie1225 »)"),
    (GACHI, "conversation du 15 oct. (style artistique) ; doc. PixAI (LoRA préférés)"),
    (DREAM, "doc. PixAI « Arcana Art » (LoRA préférés)"),
    (KANE, "doc. PixAI « Arcana Art » (LoRA préférés) ; orthographe probable « Kaneoya », non confirmée"),
    (JOMARO, "doc. PixAI « Arcana Art » (artistes aimés, sans LoRA)"),
    (MADU, "doc. PixAI « Arcana Art » (artistes aimés, sans LoRA)"),
    (NOMURA, "doc. PixAI « Arcana Art » (artistes aimés) ; test de Cosmo (Kingdom Hearts)"),
    (BOON, "test PixAI de Cosmo Dumas"),
]


def section_liste():
    present = {inf for c, inf, t, p, s in PREUVES if c != "BIO" and t != "H"}
    out = ["| Groupe (ton répertoire) | Influence | Statut dans le YAML | Trace documentée dans Edenia ? |",
           "|---|---|---|---|"]
    for g, n, canon, st in REPERTOIRE:
        cs = canon if isinstance(canon, tuple) else (canon,)
        if any(c in present for c in cs):
            out.append(f"| {g} | {n} | {st or '—'} | oui |")
            continue
        trace = "oui" if canon in present else ("hypothèse IA seulement" if canon and canon in {i for _, i, *_ in PREUVES} else "aucune trace documentée")
        out.append(f"| {g} | {n} | {st or '—'} | {trace} |")
    out.append("")
    out.append("**Hors répertoire, mais présents dans le dépôt ou dits en conversation :**\n")
    out.append("| Influence | Où elle apparaît | Trace documentée dans Edenia ? |")
    out.append("|---|---|---|")
    for canon, ou in HORS_REPERTOIRE:
        out.append(f"| {canon} | {ou} | {'oui' if canon in present else 'non'} |")
    n_rep = len(REPERTOIRE)
    n_tr = sum(1 for _, _, c, _ in REPERTOIRE if any(x in present for x in (c if isinstance(c, tuple) else (c,))))
    return "\n".join(out), n_rep, n_tr


def score(cat):
    tot = collections.defaultdict(float)
    det = collections.defaultdict(lambda: collections.Counter())
    pv = collections.defaultdict(list)
    for c, inf, t, p, s in PREUVES:
        if c != cat:
            continue
        if det[inf][t] < PLAFOND:
            tot[inf] += POINTS[t]
        det[inf][t] += 1
        pv[inf].append((t, p, s))
    return tot, det, pv


def classement(tot, det):
    def solide(inf):
        return tot[inf] - min(det[inf]["H"], PLAFOND) * POINTS["H"]
    order = sorted(tot, key=lambda i: (-tot[i], -solide(i), i))
    rangs, prev, r = [], None, 0
    for n, inf in enumerate(order, 1):
        if tot[inf] != prev:
            r = n
            prev = tot[inf]
        rangs.append((r, inf))
    return rangs


def fmt_det(c):
    return " · ".join(f"{t}×{c[t]}" for t in "DEUIH" if c[t])


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "preuves.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["element", "influence", "type", "points", "preuve", "source"])
        for c, inf, t, p, s in PREUVES:
            w.writerow([CAT[c], inf, t, POINTS[t], p, s])
    out = []
    for cat, lib in CAT.items():
        tot, det, pv = score(cat)
        out.append(f"\n### {lib}\n")
        out.append("| Rang | Influence | Score | Détail | Preuves principales |")
        out.append("|---:|---|---:|---|---|")
        for r, inf in classement(tot, det):
            preuves = " ; ".join(p for t, p, s in pv[inf] if t != "H")
            preuves = (preuves[:257].rsplit(" ", 1)[0] + " …") if len(preuves) > 260 else (preuves or "*(hypothèse IA seulement)*")
            hyp = [p for t, p, s in pv[inf] if t == "H"]
            if hyp:
                preuves += " — *hyp. IA : " + hyp[0][:120] + "*"
            out.append(f"| {r} | {inf} | {tot[inf]:g} | {fmt_det(det[inf])} | {preuves} |")
    # synthèse par pôle
    out.append("\n### Synthèse par pôle de ta grille (pôle D toujours présent)\n")
    out.append("| Pôle | 1ᵉʳ | 2ᵉ | 3ᵉ | 4ᵉ | 5ᵉ |")
    out.append("|---|---|---|---|---|---|")
    for pole, cats in POLES.items():
        agg = collections.defaultdict(float)
        for c in cats:
            t, d, _ = score(c)
            for k, v in t.items():
                agg[k] += v
        top = sorted(agg, key=lambda i: (-agg[i], i))[:5]
        out.append(f"| **{pole}** | " + " | ".join(f"{i} ({agg[i]:g})" for i in top) + " |")
    # général
    agg = collections.defaultdict(float)
    nb = collections.defaultdict(set)
    for c in CAT:
        if c == "BIO":
            continue
        t, d, _ = score(c)
        for k, v in t.items():
            agg[k] += v
            nb[k].add(c)
    out.append("\n### Classement général sur l'œuvre (somme des 12 éléments, hors biographie)\n")
    out.append("| Rang | Influence | Score total | Nombre d'éléments touchés (sur 12) | Éléments |")
    out.append("|---:|---|---:|---:|---|")
    order = sorted(agg, key=lambda i: (-agg[i], -len(nb[i]), i))
    prev, r = None, 0
    for n, inf in enumerate(order, 1):
        if agg[inf] != prev:
            r, prev = n, agg[inf]
        if n > 20:
            break
        els = ", ".join(sorted(nb[inf], key=list(CAT).index))
        out.append(f"| {r} | {inf} | {agg[inf]:g} | {len(nb[inf])} | {els} |")

    # robustesse : le classement général change-t-il si l'on change le barème ?
    def general(points, plafond, avec_h=True):
        agg = collections.defaultdict(float)
        cnt = collections.defaultdict(collections.Counter)
        for c, inf, t, p, src in PREUVES:
            if c == "BIO" or (t == "H" and not avec_h):
                continue
            k = (inf, c)
            if cnt[k][t] < plafond:
                agg[inf] += points[t]
            cnt[k][t] += 1
        return sorted(agg, key=lambda i: (-agg[i], i))[:8]
    variantes = [
        ("Barème de base (D3 E2 U2 I1 H0,5, plafond 3)", POINTS, PLAFOND, True),
        ("Sans les hypothèses de l'IA", POINTS, PLAFOND, False),
        ("Décisions très lourdes (D5 E2 U2 I1)", {"D": 5, "E": 2, "U": 2, "I": 1, "H": 0.5}, PLAFOND, False),
        ("Barème plat (toute preuve = 1)", {"D": 1, "E": 1, "U": 1, "I": 1, "H": 0}, PLAFOND, False),
        ("Sans plafond", POINTS, 99, False),
    ]
    out.append("\n### Test de robustesse du classement général (8 premiers)\n")
    out.append("| Variante | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    court = lambda n: n.split(" (")[0]
    for nom, pts, pl, h in variantes:
        out.append(f"| {nom} | " + " | ".join(court(i) for i in general(pts, pl, h)) + " |")
    out.append("\n### Repoussoirs (non comptés dans les scores)\n")
    out.append("| Influence | Ce qu'on évite | Source |")
    out.append("|---|---|---|")
    for inf, p, s in REPOUSSOIRS:
        out.append(f"| {inf} | {p} | {s} |")
    liste, n_rep, n_tr = section_liste()
    open(os.path.join(here, "_liste.md"), "w", encoding="utf-8").write(liste + f"\n\n*{n_tr} entrées du répertoire sur {n_rep} ont une trace documentée.*\n")
    open(os.path.join(here, "_tableaux.md"), "w", encoding="utf-8").write("\n".join(out))
    print("\n".join(out))
