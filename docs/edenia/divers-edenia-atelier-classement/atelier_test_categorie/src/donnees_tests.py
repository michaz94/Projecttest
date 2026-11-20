# -*- coding: utf-8 -*-
"""Catégorie « Tests visuels » : les 12 images PixAI envoyées le 15 oct. 2026, plus une fiche sur les outils.
Rien n'est canon. Les images ne représentent ni Brann, ni Cosmo, ni Harley (précision de l'utilisateur, 15 oct.).
Titres et descriptions : lecture de l'IA, signalée comme telle sur chaque fiche."""
from donnees_yaml import page

NON_CANON = ("Pas canon. Image générée avec PixAI pour tester un style ou un design. "
             "Elle ne représente ni Brann, ni Cosmo, ni Harley (ta précision du 15 oct.).")
A_COMPLETER = [
    "Projet : compatible avec Edenia (ta précision du 15 oct. : « toutes ces images sont Edenia compatible »). Projet d'origine non précisé.",
    "Ce que l'image teste : non précisé.",
    "Ton avis : non précisé (à garder, bof ou à rejeter).",
    "Réglages : non notés (modèle, LoRA et intensités, prompt). Une capture du panneau de paramètres de ton historique PixAI suffit.",
]
LOGOS = "Des emblèmes d'autres œuvres sont visibles. C'est sans problème pour un test, mais à retirer d'un design final destiné à un éditeur."

# (n°, fichier d'origine, sous-catégorie, titre, ce qu'on voit (lecture de l'IA), logos d'autres œuvres ?)
IMAGES = [
    (1, "media_1791812835.png", "seul", "Garçon brun, ruelle médiévale de nuit",
     "Garçon brun aux cheveux en pétard, souriant, mains en griffes, devant une pleine lune. Ruelle pavée bordée de maisons à colombages et de tours pointues. Tenue sombre ample, ceinture de corde, sandales.", False),
    (2, "media_1791813319.png", "seul", "Garçon brun, ruelle médiévale de jour",
     "Même type de personnage que le test 01, en plein jour, dans une ruelle pavée. Détails de tenue proches de Naruto : brassard à spirale, sandales ninja, ceinture de corde, sacoche.", True),
    (3, "media_1792029871.png", "seul", "Combattante noir et or, poing en avant",
     "Jeune femme aux cheveux noirs et blonds, coiffe à deux pointes, tenue noire, poing en raccourci vers le lecteur. Boucle de ceinture en « X » jaune, façon X-Men.", True),
    (4, "media_1792029902.png", "seul", "Combattante noir et or, pose basse",
     "Même type de personnage que le test 03, en pose basse dans un intérieur en bois. Bandeau orné de disques, ceinture jaune nouée.", False),
    (5, "media_1792040381.png", "seul", "Portrait aux longs cheveux noirs",
     "Personnage aux longs cheveux noirs, pensif, main au menton, chemise claire. Rendu plus sobre et plus proche du seinen que les autres tests.", False),
    (6, "media_1792052016.png", "duo", "Duo en forêt, traits rouges",
     "Deux garçons à la peau foncée, l'un blond au-dessus, l'autre aux cheveux bouclés en contre-plongée. Forêt verte, coups de pinceau rouges, emblème d'araignée sur le pull.", True),
    (7, "media_1792053518.png", "seul", "Garçon blond en sweat gris, gros plan",
     "Garçon blond aux cheveux en pétard, peau foncée, sweat à capuche gris, en mouvement vers le lecteur. Fond rose et bleu façon Spider-Verse, emblème d'araignée.", True),
    (8, "media_1792053652.png", "seul", "Garçon blond, plongée en forêt",
     "Garçon blond aux cheveux en pétard en gros plan, regard déterminé, forêt en arrière-plan. Veste noire avec emblème d'araignée rouge.", True),
    (9, "media_1792053849.png", "duo", "Duo empilé façon affiche, forêt",
     "Composition d'affiche : une fille blonde bras croisés au premier plan, un garçon en manteau noir et rouge derrière elle. Forêt, emblème d'araignée sur le t-shirt.", True),
    (10, "media_1792053855.png", "duo", "Duo empilé, silhouette sombre",
     "Une fille blonde au premier plan et une grande silhouette sombre au masque rouge derrière elle, motif de toile d'araignée. Fond violet, rose et orange.", True),
    (11, "media_1792054876.png", "duo", "Duo en forêt, mains jointes",
     "Garçon blond et fille aux cheveux noirs face à face, mains jointes, dans une forêt d'automne. Format carré. Grands yeux et visage rond, proches de Disney.", False),
    (12, "media_1792088390.png", "duo", "Duo en forêt, bras tendus",
     "Garçon blond et fille aux cheveux noirs, bras tendus l'un vers l'autre, en forêt. Format carré. Grands yeux et visage rond, proches de Disney.", False),
]

# Avis donnés par l'utilisateur (15 oct.), remplacent la ligne « Ton avis » par défaut
# Versions noir et blanc des tests 11 et 12 (images envoyées le 16 oct., prompt et LoRA donnés le 17 oct.)
NB_FICHIER = {11: "media_1792113468.png", 12: "media_1792172128.png"}
NB_REGLAGES = "Réglages de la version noir et blanc : prompt donné le 17 oct. (voir « Version noir et blanc ») ; modèle principal et intensités des LoRA non précisés."
NB_SEC = ("Version noir et blanc (16 oct.)", [
    "LoRA de rendu manga : « JUJUTSU KAISEN style(MANGA) | Gege Akutami style [OLD] » (NoobAI-XL), déclencheurs « monochrome, manga style, greyscale ». Ta précision du 17 oct.",
    "Les autres LoRA présents dans le prompt (d'après leurs mots déclencheurs) : ATIE1225 STYLE, Gachiakuta Manga Style et Gachiakuta Cover Art Style. « (naruto style:0.5) » est un tag, pas un LoRA. Le négatif commence par « (color) ».",
    "Le prompt demande deux personnages existants : « miles_morales\\(spider-verse\\) » et « violet_parr\\(the incredibles\\) ». <b>Le visage façon Disney/Pixar de la fille vient de ce tag</b>, pas d'un mélange de LoRA (lecture de l'IA).",
    "Couleurs de cheveux et de peau non attribuées à un personnage dans le prompt : elles changent de personne d'une image à l'autre (lecture de l'IA).",
    "Lecture de l'IA : rendu manga réussi (lignes de vitesse, hachures, cheveux en pointes). Mais le gris est lisse, sans trame en points, alors que l'image de présentation du LoRA en a ; la version noir et blanc du test 11 garde des yeux rouges, un reste de couleur.",
])

AVIS = {9: "Ton avis : compatible avec Edenia, mais doit sonner légèrement moins moderne, à cause du jean (ta précision du 15 oct.).",
        10: "Ton avis : compatible avec Edenia, mais doit sonner légèrement moins moderne, à cause du jean (ta précision du 15 oct.)."}

TESTS = []
for n, f, sub, titre, vu, logos in IMAGES:
    k = f"test{n:02d}"
    ac = [AVIS[n] if (n in AVIS and l.startswith("Ton avis")) else l for l in A_COMPLETER]
    extra = {}
    if n in NB_FICHIER:
        ac = [NB_REGLAGES if l.startswith("Réglages") else l for l in ac]
        extra = dict(gal=[f"{k}nb"], galcap={f"{k}nb": f"Test {n:02d}, version noir et blanc · PixAI · pas canon"})
    secs = [("À compléter par toi", ac),
            ("Ce qu'on voit (lecture de l'IA, à confirmer)", [vu] + ([LOGOS] if logos else []))]
    if n in NB_FICHIER:
        secs.append(NB_SEC)
    TESTS.append(page('tests', f"Test {n:02d} · {titre}", sub, 'np',
                      vu.split('. ')[0] + '.',
                      f"<b>Test {n:02d}</b> : image générée avec PixAI pour tester un style ou un design. Statut non précisé.",
                      secs, src=f"Image PixAI envoyée le 15 oct. ({f})" + (f" ; version noir et blanc envoyée le 16 oct. ({NB_FICHIER[n]}) ; prompt donné le 17 oct." if n in NB_FICHIER else ""), warn=NON_CANON,
                      rel=['tests/outils-pixai'], sl=f"test-{n:02d}", img=k,
                      imgcap=f"Test {n:02d} · PixAI · pas canon", **extra))

TESTS.append(page('tests', 'Outils PixAI (modèles et LoRA)', 'methode', 'np',
    'Ta méthode de test : modèles de la famille Illustrious, deux LoRA de base, et le style ajouté par les tags.',
    'Ce que tu utilises pour tes <b>tests visuels</b>, d\'après tes documents PixAI (septembre) et les pages PixAI de tes LoRA (15 oct.). '
    'Ce sont des <b>outils</b> : ce qu\'ils produisent (trait épais, rendu « official art ») ne compte pas comme une influence d\'Edenia.',
    [('Modèles de base (31 recettes analysées)', [
        'coco-Illustrious-NoobXL-Style v3.0 : 10 recettes.',
        'coco-Illustrious-NoobAI-XL-Style v7.0 : 8 recettes.',
        'coco-Illustrious-NoobXL-Style v2.0 : 4 recettes.',
        'WAI-NSFW-illustrious-SDXL v14.0 : 4 recettes ; WAI-illustrious-SDXL v16.0 : 4 recettes.']),
     ('LoRA de base', [
        'ATIE1225 STYLE (A BB EY, Illustrious-XL v1.0), déclencheurs « atie1225 style, drawing style » : 24 recettes, intensité 0,6 à 0,8. L\'auteur conseille « autour de 0,7 ».',
        'Gachiakuta Manga Style (Zerobeastskaiai, versions NoobAI et Illustrious), déclencheurs « urana_kei, gachiakuta, official_art » : 16 recettes, 0,4 à 0,7.',
        'Gachiakuta Cover Art Style (Hideyoshi Andou, par Busei, NoobAI-XL), déclencheur « gachiakuta cover art style » : 8 recettes, 0,7 à 0,9.']),
     ('Autre LoRA (rendu manga noir et blanc)', [
        'JUJUTSU KAISEN style(MANGA) | Gege Akutami style [OLD] (NoobAI-XL, mis en ligne le 11 janvier 2025), déclencheurs « monochrome, manga style, greyscale » : utilisé pour les versions noir et blanc des tests 11 et 12 (ta précision du 17 oct.). Intensité conseillée : non indiquée sur sa page.']),
     ('Accélérateur', [
        'DMD2 : 12 recettes, intensité 0,2 à 0,4. Il permet moins d\'étapes et un CFG bas ; il ne change pas le style. D\'où ta préférence « CFG sous 4 ».']),
     ('Tags de style que tu ajoutes', [
        '« Jujutsu Kaisen style » (8 recettes), « Street Fighter characters » (5), « semi-realistic » (5), « Naruto coloring style » et « Disney style » (2 chacun).',
        'Les tags de tes deux LoRA de base sont dans 30 recettes sur 31.']),
     ('Pour aller plus loin', [
        'Fiche complète, avec sources et conseils : recherche_pixai/modeles_et_tags_pixai.md.'])],
    src='Tes documents PixAI « Arcana » (PDF, sept.) ; pages PixAI des LoRA (15 oct.)', sl='outils-pixai'))

SUBS_TESTS = {'seul': 'Personnage seul', 'duo': 'Duos et affiches', 'methode': 'Méthode et outils'}

# ------------------------------------------------------------------ TIER LISTE DES TAGS DE PERSONNAGES (18 oct.)
# Rang = avis de l'utilisateur (18 oct.). Chiffres Danbooru relevés le 18 oct. 2026 (tags.json et counts/posts.json).
# Écriture PixAI = consigne du manuel NoobAI-XL (espaces, parenthèses échappées, tag de l'œuvre juste après).
# Colonne « apport au style » = lecture de l'IA.
# (rang, nom, tag Danbooru, images, dont tout public, écriture PixAI, apport au style)
TIER = [
    ('S', 'Violet Parr (Les Indestructibles)', 'violet_parr', 133, 16, r'violet parr, the incredibles',
     "Visage Pixar en 3D : grands yeux, petit nez, longs cheveux noirs raides. Dans tes tests 11 et 12, c'est ce tag qui donne le visage façon Disney de la fille."),
    ('S', 'Gwen Stacy (Spider-Verse)', 'spider-gwen', 1708, 483, r'spider-gwen, spider-verse',
     "Graphisme Spider-Verse (effets d'impression de comics) et silhouette de super-héroïne en capuche. Sur Danbooru, la Gwen des films est « spider-gwen » (Gwen de la Terre-65) ; « gwen_stacy » (1556 images) désigne le personnage en général."),
    ('S', 'Gwen Tennyson (Ben 10)', 'gwen_tennyson', 656, 75, r'gwen tennyson, ben 10',
     "Dessin animé télé occidental, formes simples et lisibles ; magie à énergie rose."),
    ('S', 'Raiponce (Disney)', 'rapunzel_(disney)', 554, 302, r'rapunzel \(disney\), tangled',
     "Visage de princesse Disney en 3D : très grands yeux, traits ronds, très longs cheveux blonds. Tu as dit que Harley ressemble à Raiponce."),
    ('A', 'Astrid (Dragons)', 'astrid_hofferson', 186, 90, r'astrid hofferson, how to train your dragon \(series\)',
     "DreamWorks en 3D ; tresse blonde, armure viking, hache. Le plus proche de la grammaire de tenue d'Edenia (base ancienne, fonctionnelle)."),
    ('A', 'Raven (Teen Titans)', 'raven_(dc)', 1948, 119, r'raven \(dc\), teen titans',
     "Cape à capuche, palette sombre, magie. Le tag est « raven_(dc) » dans les deux cas : 1880 de ses 1948 images portent aussi « teen_titans », donc DC et Teen Titans désignent surtout la même version."),
    ('A', 'Miles Morales (Spider-Verse)', 'miles_morales', 550, 347, r'miles morales, spider-verse',
     "Silhouette urbaine (sweat à capuche, baskets) et graphisme Spider-Verse. Son tag est dans le prompt de tes versions noir et blanc des tests 11 et 12."),
    ('A', 'Robin (Teen Titans)', 'robin_(dc)', 1072, 480, r'robin \(dc\), teen titans',
     "Cheveux noirs en pointes, masque, cape : silhouette proche du héros de shōnen. « robin_(dc) » est un titre porté par 6 personnages (Dick Grayson, Jason Todd, etc.) : « teen titans » resserre sur la bonne version (178 images avec les deux tags)."),
    ('B', 'Nami (One Piece)', 'nami_(one_piece)', 11299, 2867, r'nami \(one piece\), one piece',
     "Le seul personnage de manga de la liste : il tire vers le dessin d'Oda plutôt que vers le cartoon. De loin le plus d'images."),
    ('B', 'Shego (Kim Possible)', 'shego', 354, 26, r'shego, kim possible \(series\)',
     "Dessin animé Disney télé des années 2000, anguleux ; combinaison verte et noire. Très peu d'images tout public (7 %)."),
    ('B', 'Starfire (Teen Titans)', 'starfire', 988, 115, r'starfire, teen titans',
     "Teen Titans ; le tag couvre aussi les comics, mais 907 de ses 988 images portent « teen_titans »."),
]
TIER_DESC = {'S': 'Excellent', 'A': 'Bien', 'B': 'Moyen', 'C': 'Raté'}

def _tier_item(t):
    rang, nom, tag, n, g, ecr, apport = t
    pct = round(100 * g / n)
    return (f"<b>{nom}</b><br>À écrire dans PixAI : <code>{ecr}</code><br>"
            f"Tag Danbooru : <code>{tag}</code> · {n} images, dont {g} tout public ({pct} %)<br>"
            f"<i>Apport au style (lecture de l'IA) :</i> {apport}")

def _tier_board():
    """Tableau façon tier liste : une rangée colorée par rang, une carte par personnage (balises <span> : le bloc est rendu dans un <p>)."""
    rows = []
    for r in 'SABC':
        cards = []
        for t in TIER:
            if t[0] != r:
                continue
            nom, oeuvre = (t[1].split(' (', 1) + [''])[:2]
            cards.append(f'<span class="tier-card"><b>{nom}</b><small>{oeuvre.rstrip(")")}</small></span>')
        body = ''.join(cards) or '<span class="tier-empty">—</span>'
        rows.append(f'<span class="tier-row tier-{r}"><span class="tier-lbl"><b>{r}</b><small>{TIER_DESC[r]}</small></span>'
                    f'<span class="tier-cards">{body}</span></span>')
    return '<span class="tier-board" role="table" aria-label="Tier liste des tags de personnages">' + ''.join(rows) + '</span>'

# Données de la tier liste interactive (montée par corps.html, mountTier) ; le tableau fixe reste pour le PNG du fichier de recherche.
TIER_JS = []
for t in TIER:
    nom, oeuvre = (t[1].split(' (', 1) + [''])[:2]
    TIER_JS.append(dict(id=t[2], r=t[0], nom=nom, oeuvre=oeuvre.rstrip(')'), tag=t[2], n=t[3], g=t[4], ecr=t[5]))
_secs = [('Tier liste interactive', ['<span class="tl-mount">' + _tier_board() + '</span>'])]
_secs += [(f"Tier {r} — {TIER_DESC[r]}", [_tier_item(t) for t in TIER if t[0] == r]) for r in 'SAB' if any(t[0] == r for t in TIER)]
_secs += [
    ('Comment lire', [
        "<b>Le rang vient de ton avis</b> (18 oct.) sur ce que PixAI t'a donné. Il ne mesure pas la qualité du personnage.",
        "<b>Nombre d'images Danbooru :</b> indice de ce que le modèle connaît du personnage. Chiffres du 18 oct. 2026 : les modèles ont été entraînés sur des versions plus anciennes de Danbooru.",
        "<b>Part tout public :</b> quand elle est faible, le modèle a surtout vu le personnage dans des images non tout public. Garde « nsfw » en négatif pour les tests du projet.",
        "<b>Écriture PixAI :</b> consigne du manuel NoobAI-XL (espaces au lieu des tirets bas, parenthèses précédées de « \\ », tag de l'œuvre juste après). Non testée sur tes réglages.",
        "<b>Raven SHDBS :</b> tu préfères ce LoRA au tag. C'est un LoRA, pas un tag de personnage : il n'est pas classé ici.",
    ]),
    ('Pour aller plus loin', ['Fiche complète : recherche_pixai/tier_liste_tags_personnages.md.']),
]
TESTS.append(page('tests', 'Tier liste des tags de personnages', 'methode', 'np',
    'Tes 11 tags de personnages classés selon ton avis : 4 en S, 4 en A, 3 en B.',
    "Classement des <b>tags de personnages</b> que tu utilises sur PixAI. Le rang est <b>ton avis</b> ; "
    "les chiffres viennent de Danbooru ; la colonne « apport au style » est une <b>lecture de l'IA</b>.",
    _secs, src="Ton avis (18 oct.) ; Danbooru, tags.json et counts/posts.json (18 oct. 2026) ; manuel NoobAI-XL (28 nov. 2024)",
    rel=['tests/outils-pixai'], sl='tier-liste-personnages', tier=TIER_JS))
