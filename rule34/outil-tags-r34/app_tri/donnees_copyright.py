# Filtres « Copyright » de l'application EdeniaList (25/10/2026).
# Seuls des tags de type Copyright sur rule34.xxx sont proposés (type vérifié un par un dans la liste des tags, 25/10/2026).
# Écartés car pas Copyright : movie (Metadata, 873), toby_fox (Artist, 2 817).
#
# Rattachement d'un personnage à un tag :
#  1. par franchise : studio, éditeur ou magazine d'origine de la franchise (ou co-producteur) ;
#  2. franchise rachetée plus tard (Marvel, Star Wars, Simpson → Disney ; DC, Scooby-Doo, Mortal Kombat → Warner ;
#     Tomb Raider → Square Enix ; Persona → Sega ; Mass Effect → EA ; Fallout (Interplay) → Bethesda) : retenue seulement si au moins 10 % des posts de la
#     franchise portent aussi le tag sur rule34 (mesure ci-dessous) ;
#  3. Marvel Rivals : par personnage, si au moins 10 % des posts du personnage portent aussi marvel_rivals.
#  4. Films Spider-Verse (Sony Pictures Animation) : par personnage, si au moins 10 % de ses posts portent un des deux tags
#     Copyright des films (spider-man:_into_the_spider-verse, spider-man:_across_the_spider-verse). Le tag studio
#     sony_pictures_animation lui-même n'est posé que sur ≈ 1,4 % des posts gwen_stacy (≈ 273), d'où la mesure par les titres.
# Les tags d'éditeur sont posés de façon irrégulière sur rule34 (one_piece ∧ shounen_jump ≈ 9 261 / 162 820 = 5,7 %) :
# la co-occurrence ne sert donc qu'aux cas 2 et 3, pas à exclure une franchise d'origine.
import json, collections
from especes_filtre import especes_de, tags_especes   # catégorie de filtre « Espèce » (25/10/2026)

# tag : (libellé, groupe, publications rule34 au 25/10/2026, note)
J, A, C, M = 'Jeux vidéo', 'Animation, cinéma et télévision', 'Comics', 'Manga'
TAGS = {
 'nintendo': ('Nintendo', J, 1131492, ''),
 'game_freak': ('Game Freak', J, 86689, ''),
 'marvel_rivals': ('Marvel Rivals', J, 66093, 'par personnage : au moins 10 % de ses posts avec marvel_rivals'),
 'sega': ('Sega', J, 169810, ''),
 'atlus': ('Atlus', J, 28086, ''),
 'capcom': ('Capcom', J, 141086, ''),
 'square_enix': ('Square Enix', J, 44257, ''),
 'riot_games': ('Riot Games', J, 106249, ''),
 'blizzard_entertainment': ('Blizzard Entertainment', J, 130063, ''),
 'hoyoverse': ('HoYoverse (miHoYo)', J, 84053, 'tag « Copyright, ambiguous » ; mihoyo : 82 820'),
 'cd_projekt_red': ('CD Projekt Red', J, 40401, ''),
 'bioware': ('BioWare', J, 9545, ''),
 'electronic_arts': ('Electronic Arts', J, 11593, ''),
 'bandai_namco': ('Bandai Namco', J, 36325, 'tag « Copyright, ambiguous »'),
 'type-moon': ('Type-Moon', J, 7338, ''),
 'epic_games': ('Epic Games', J, 38376, ''),
 'supercell': ('Supercell', J, 15057, ''),
 'scottgames': ('ScottGames', J, 37662, ''),
 'naughty_dog': ('Naughty Dog', J, 7943, ''),
 'hypergryph': ('Hypergryph', J, 1939, ''),
 'cygames': ('Cygames', J, 3826, ''),
 'snk': ('SNK', J, 34558, ''),
 'koei_tecmo': ('Koei Tecmo', J, 1514, ''),
 'team_cherry': ('Team Cherry', J, 7724, ''),
 'team_shanghai_alice': ('Team Shanghai Alice (ZUN)', J, 1421, 'cercle de ZUN, auteur de Touhou Project (type Copyright vérifié le 25/10/2026)'),
 'wayforward': ('WayForward', J, 4674, ''),
 'bethesda_softworks': ('Bethesda Softworks', J, 13658, 'The Elder Scrolls, Fallout (espèces en option)'),
 'arc_system_works': ('Arc System Works', J, 4410, ''),
 'fromsoftware': ('FromSoftware', J, 31900, 'from_software : 61 (tag Général)'),
 'bungie': ('Bungie', J, 3913, 'Halo (espèces en option)'),
 'disney': ('Disney', A, 280814, ''),
 'pixar': ('Pixar', A, 24474, ''),
 'dreamworks': ('DreamWorks', A, 42156, ''),
 'cartoon_network': ('Cartoon Network', A, 103791, ''),
 'nickelodeon': ('Nickelodeon', A, 70574, ''),
 'warner_brothers': ('Warner Bros.', A, 26655, 'warner_bros : 3 661'),
 'hanna-barbera': ('Hanna-Barbera', A, 15563, ''),
 'hasbro': ('Hasbro', A, 119066, ''),
 '20th_century_fox': ('20th Century Fox', A, 8219, ''),
 'lucasfilm': ('Lucasfilm', A, 5560, ''),
 'sony_pictures_animation': ('Sony Pictures Animation', A, 2896, 'Hôtel Transylvanie ; Spider-Verse par personnage (au moins 10 % de ses posts avec un tag des films)'),
 'studio_trigger': ('Studio Trigger', A, 10813, ''),
 'vivziepop': ('Vivziepop', A, 10184, ''),
 'rooster_teeth': ('Rooster Teeth', A, 4868, ''),
 'glitch_productions': ('Glitch Productions', A, 30510, ''),
 'gainax': ('Gainax', A, 2768, ''),
 'marvel': ('Marvel', C, 227574, 'tag « Copyright, ambiguous » ; marvel_comics : 180 739'),
 'dc_comics': ('DC Comics', C, 182623, ''),
 'shounen_jump': ('Shōnen Jump', M, 62929, 'Weekly Shōnen Jump et Shōnen Jump+ ; shonen_jump : 5 655 ; shounen_jump+ : 822'),
 'shueisha': ('Shueisha', M, 6228, ''),
 'kodansha': ('Kodansha', M, 334, 'tag peu utilisé sur rule34'),
 'shogakukan': ('Shogakukan', M, 40, 'tag peu utilisé sur rule34'),
}

# franchise (libellés rule34 et Danbooru de l'application) -> tags
JUMP = ['shounen_jump', 'shueisha']
F = {
 'Pokémon': ['nintendo', 'game_freak'], 'Super Mario': ['nintendo'], 'The Legend of Zelda': ['nintendo'], 'Fire Emblem': ['nintendo'],
 'Splatoon': ['nintendo'], 'Animal Crossing': ['nintendo'], 'Star Fox': ['nintendo'], 'Metroid': ['nintendo'], 'Kid Icarus': ['nintendo'],
 'WarioWare': ['nintendo'], 'Xenoblade Chronicles 2': ['nintendo'], 'Xenoblade Chronicles': ['nintendo'],
 'Bayonetta': ['sega', 'nintendo'],
 'Sonic the Hedgehog': ['sega'], 'Sonic': ['sega'],
 'Persona 5': ['atlus'],
 'Resident Evil': ['capcom'], 'Resident Evil Village': ['capcom'], 'Resident Evil 4': ['capcom'], 'Street Fighter': ['capcom'], 'Darkstalkers': ['capcom'],
 'Final Fantasy VII': ['square_enix'], 'Final Fantasy': ['square_enix'], 'NieR: Automata': ['square_enix'], 'NieR': ['square_enix'],
 'My Dress-Up Darling': ['square_enix'],
 'League of Legends': ['riot_games'], 'League of Legends / Arcane': ['riot_games'],
 'Overwatch': ['blizzard_entertainment'],
 'Genshin Impact': ['hoyoverse'], 'Zenless Zone Zero': ['hoyoverse'], 'Honkai: Star Rail': ['hoyoverse'], 'Honkai Impact 3rd': ['hoyoverse'],
 'The Witcher': ['cd_projekt_red'], 'Cyberpunk 2077': ['cd_projekt_red'], 'Cyberpunk: Edgerunners': ['cd_projekt_red', 'studio_trigger'],
 'Mass Effect': ['bioware', 'electronic_arts'], 'Apex Legends': ['electronic_arts'],
 'The Idolmaster': ['bandai_namco'],
 'Fate': ['type-moon'], 'Tsukihime': ['type-moon'],
 'Fortnite': ['epic_games'], 'Brawl Stars': ['supercell'], "Five Nights at Freddy's": ['scottgames'], 'The Last of Us': ['naughty_dog'], 'Crash Bandicoot': ['naughty_dog'],
 'Arknights': ['hypergryph'], 'Uma Musume': ['cygames'],
 'La Reine des neiges': ['disney'], 'Aladdin': ['disney'], 'Zootopie': ['disney'], 'Kim Possible': ['disney'],
 'Luz à Osville (The Owl House)': ['disney'], 'Les Indestructibles': ['disney', 'pixar'], 'Qui veut la peau de Roger Rabbit': ['disney'],
 "La Route d'Eldorado (DreamWorks)": ['dreamworks'], 'Les Bad Guys': ['dreamworks'],
 'Adventure Time': ['cartoon_network'], 'Ben 10': ['cartoon_network'], 'Le Monde incroyable de Gumball': ['cartoon_network'],
 'Steven Universe': ['cartoon_network'], 'Foster, la maison des amis imaginaires': ['cartoon_network'],
 "Avatar, le dernier maître de l'air": ['nickelodeon'], 'La Légende de Korra': ['nickelodeon'], 'Ma vie de robot ado': ['nickelodeon'],
 'Looney Tunes': ['warner_brothers'], 'Scooby-Doo': ['hanna-barbera'],
 'My Little Pony': ['hasbro'], 'Les Simpson': ['20th_century_fox'], 'Star Wars': ['lucasfilm'], 'Hôtel Transylvanie': ['sony_pictures_animation'],
 # franchises des espèces (option, donnees_especes.py)
 'Digimon': ['bandai_namco'], 'Warcraft': ['blizzard_entertainment'], 'Final Fantasy XIV': ['square_enix'], 'Alien': ['20th_century_fox'],
 'Halo': ['bungie'], 'The Elder Scrolls': ['bethesda_softworks'], 'Fallout': ['bethesda_softworks'],
 # franchises du relevé 331-340 (25/10/2026) ; Miraculous : aucun tag Copyright de studio trouvé (zag* : aucun)
 'Les Griffin (Family Guy)': ['20th_century_fox'], 'Guilty Gear': ['arc_system_works'], 'Elden Ring': ['fromsoftware'], 'Monogatari': ['kodansha'],
 'Kill la Kill': ['studio_trigger'], 'Darling in the Franxx': ['studio_trigger'],
 'Helluva Boss': ['vivziepop'], 'Hazbin Hotel': ['vivziepop'], 'RWBY': ['rooster_teeth'],
 'Marvel': ['marvel'], 'Marvel (Les 4 Fantastiques)': ['marvel'], 'DC Comics': ['dc_comics'],
 'One Piece': JUMP, 'Naruto': JUMP, 'Naruto / Boruto': JUMP, 'Dragon Ball': JUMP, 'Bleach': JUMP, 'My Hero Academia': JUMP,
 'Demon Slayer': JUMP, 'Jujutsu Kaisen': JUMP, 'Chainsaw Man': JUMP, 'Spy×Family': JUMP, 'Black Clover': JUMP, 'Dandadan': JUMP,
 "JoJo's Bizarre Adventure": JUMP, 'Yu-Gi-Oh!': JUMP,
 'One Punch Man': ['shueisha'], 'One-Punch Man': ['shueisha'],
 "L'Attaque des Titans": ['kodansha'], 'Fairy Tail': ['kodansha'], 'Arrête de me chauffer, Nagatoro': ['kodansha'], 'Sailor Moon': ['kodansha'],
 'The Quintessential Quintuplets': ['kodansha'], 'Card Captor Sakura': ['kodansha'], 'Frieren': ['shogakukan'], 'Komi cherche ses mots': ['shogakukan'],
 'Fatal Fury / King of Fighters': ['snk'], 'Dead or Alive': ['koei_tecmo'], 'Hollow Knight': ['team_cherry'], 'Shantae': ['wayforward'],
 'The Amazing Digital Circus': ['glitch_productions'], 'Evangelion': ['gainax'], 'Neon Genesis Evangelion': ['gainax'], 'Gurren Lagann': ['gainax'],
 'Panty & Stocking with Garterbelt': ['gainax'],
 # franchises du relevé 341-360 (25/10/2026) ; sans tag Copyright retenu : Code Geass (sunrise : type non vérifié), DanMachi, Mushoku Tensei,
 # Azur Lane, Lucky Star, Omori (tags d'éditeur ou de studio absents ou sous 250 posts sur rule34)
 'Soulcalibur': ['bandai_namco'], 'Life is Strange': ['square_enix'], 'Star vs. les forces du mal': ['disney'],
 'Gameoverse': ['glitch_productions'],
 # relevé 361-390 (25/10/2026) ; sans tag Copyright retenu : Sword Art Online, Roshidere (Kadokawa : kadokawa_corporation 165, kadokawa_shoten 127),
 # Miss Kobayashi's Dragon Maid (futabasha 1, kyoto_animation 63), Haydee, Les Tortues Ninja (rachat Nickelodeon : co-tag 9,1 % < 10 %)
 'Ranma ½': ['shogakukan'], 'Touhou Project': ['team_shanghai_alice'],  # ajouté à ta demande (25/10) 'Akame ga Kill!': ['square_enix'], 'Kaguya-sama: Love is War': ['shueisha'],
 'Trials of Mana (Seiken Densetsu 3)': ['square_enix'], 'Final Fight': ['capcom'],
 'La Petite Sirène (Disney)': ['disney'], 'Raiponce (Disney)': ['disney'], 'Gravity Falls': ['disney'],
 'Le Laboratoire de Dexter': ['cartoon_network'], 'Dragons (DreamWorks)': ['dreamworks'], 'Kung Fu Panda': ['dreamworks'],
}
# Teen Titans (2003) et Teen Titans Go! sont des séries Cartoon Network ; co-tag cartoon_network mesuré : Raven ≈ 9,4 %, Starfire ≈ 12,8 %, Beast Boy ≈ 7,7 %
PERSO = {'raven_(dc)': ['cartoon_network'], 'starfire': ['cartoon_network'], 'beast_boy': ['cartoon_network']}
# Marvel Rivals : posts « personnage ∧ marvel_rivals » (dernière page + 21) / publications du personnage, 25/10/2026
RIVALS = {'emma_frost': (12999, 20269), 'invisible_woman': (8757, 10816), 'squirrel_girl_(marvel)': (7077, 10093),
          'psylocke ∪ psylocke_(kwannon)': (6783, 10006), 'venom_(marvel)': (3843, 13135), 'rogue_(x-men)': (2121, 8641),
          'black_cat_(marvel)': (3381, 15119), 'spider-man': (2877, 20916), 'black_widow_(marvel)': (1407, 10379),
          'gwen_stacy': (105, 19716), 'she-hulk': (147, 7675), 'mary_jane_watson': (105, 7592),
          # relevé 361-390 (même méthode, 25/10/2026)
          'magik_(illyana_rasputin)': (4137, 5651), 'luna_snow': (5313, 5510)}
# Personnages JOUABLES dans Marvel Rivals (liste des 54 héros au 25/10/2026, saison 10.5 ; jeu sorti le 6/12/2024) : demande du 25/10,
# ils reçoivent aussi le tag de médium « Jeux vidéo » (m:jv), en plus de leur médium d'origine (Comics). Le classement par médium ne change pas.
# Absents du roster : Gwen Stacy (Spider-Gwen n'est pas jouable ; Peni Parker l'est), She-Hulk, Mary Jane Watson.
ROSTER = {'emma_frost', 'invisible_woman', 'squirrel_girl_(marvel)', 'psylocke ∪ psylocke_(kwannon)', 'rogue_(x-men)', 'black_cat_(marvel)',
          'black_widow_(marvel)', 'magik_(illyana_rasputin)', 'luna_snow', 'spider-man', 'venom_(marvel)'}
# Spider-Verse : posts « personnage ∧ ( spider-man:_into_the_spider-verse ~ spider-man:_across_the_spider-verse ) » (dernière page + 21) / publications du personnage, 25/10/2026
# (tags des films : 11 789 et 8 599 posts, type Copyright vérifié)
SPIDERVERSE = {'gwen_stacy': (9891, 19716), 'spider-man': (2541, 20916)}
# franchises rachetées : co-tag mesuré (posts « franchise ∧ tag » / publications du tag de franchise), 25/10/2026
RACHATS = [('marvel', 'disney', 7497, 227574, False), ('star_wars', 'disney', 1575, 54108, False), ('the_simpsons', 'disney', 399, 14245, False),
           ('dc_comics', 'warner_brothers', 3213, 182623, False), ('mortal_kombat', 'warner_brothers', 357, 28580, False),
           ('velma_dinkley', 'warner_brothers', 819, 14935, False), ('tomb_raider', 'square_enix', 273, 33341, False),
           ('persona_5', 'sega', 3759, 42686, False), ('mass_effect', 'electronic_arts', 3843, 37164, True),
           ('the_witcher_(series)', 'cd_projekt_red', 26943, 43239, True), ('who_framed_roger_rabbit', 'disney', 7287, 11658, True),
           ('bayonetta_(character)', 'nintendo', 819, 6850, True), ('bayonetta_(character)', 'sega', 1113, 6850, True),
           ('pokemon', 'nintendo', 660429, 958042, True), ('spy_x_family', 'shounen_jump', 315, 35524, None),
           ('one_piece', 'shounen_jump', 9261, 162820, None), ('fallout', 'bethesda_softworks', 5145, 18913, True),
           ('teenage_mutant_ninja_turtles', 'nickelodeon', 1071, 11810, False)]

B = '/home/user/outil_tags_r34/app_tri/'
R = json.load(open(B + 'donnees_app_2026-10-24.json')); D = json.load(open(B + 'donnees_app_top_danbooru_2026-10-24.json'))
ES = json.load(open(B + 'donnees_especes_2026-10-25.json', encoding='utf-8'))

# ---- tags « Médium et type » (classement EdeniaList, pas des tags rule34) ----
# médium = médium d'origine ; les personnages Furry gardent aussi leur médium d'origine (indiqué dans la note du classement v9).
G0 = 'Médium et type (classement EdeniaList)'
MED = {'m:animanga': ('Animanga', "médium d'origine (classement EdeniaList, pas un tag rule34)"),
       'm:jv': ('Jeux vidéo', "médium d'origine (classement EdeniaList, pas un tag rule34) ; inclut aussi les personnages jouables dans Marvel Rivals, quel que soit leur médium d'origine"),
       'm:comics': ('Comics', "médium d'origine (classement EdeniaList, pas un tag rule34)"),
       'm:cartoons': ('Cartoons / anim. occ.', "médium d'origine : animation occidentale (classement EdeniaList, pas un tag rule34)"),
       'm:autres': ('Autres', "ni animanga, ni jeu vidéo, ni comics, ni animation occidentale (VTubers, Vocaloid, romans, films en prises de vues réelles…)"),
       'm:furry': ('Furry', "classement Furry d'EdeniaList : animal anthropomorphe ou créature animale et indice e621 >= 2 ; garde aussi son médium d'origine"),
       'm:film': ('Film', "œuvre principale = long métrage de cinéma (y compris adaptations de romans ou de contes quand le personnage tel qu'il est dessiné vient du film) ; les adaptations au cinéma de personnages venus d'ailleurs (Spider-Verse, films Marvel ou DC) ne comptent pas"),
       'm:espece': ('Fiche espèce (option)', "espèce d'une œuvre précise (option « Espèces », désactivée par défaut, liste Rule34)")}
MKEY = {'Animanga': 'm:animanga', 'Jeux vidéo': 'm:jv', 'Comics': 'm:comics', 'Cartoons': 'm:cartoons', 'Autres': 'm:autres'}
FILM = {'Zootopie', 'Les Indestructibles', 'La Reine des neiges', 'Star Wars', 'Qui veut la peau de Roger Rabbit',
        "La Route d'Eldorado (DreamWorks)", 'Hôtel Transylvanie', 'Aladdin', 'Les Bad Guys', 'Ring (roman et films)', 'Alien',
        'La Petite Sirène (Disney)', 'Raiponce (Disney)', 'Dragons (DreamWorks)', 'Kung Fu Panda'}
# personnages Furry masculins sans note de médium d'origine dans donnees.py
ORIG_M = {'Sonic': 'Jeux vidéo', 'Tails': 'Jeux vidéo', 'Shadow': 'Jeux vidéo', 'Nick Wilde': 'Cartoons', 'Foxy': 'Jeux vidéo',
          'Fox McCloud': 'Jeux vidéo', 'Ralsei': 'Jeux vidéo', 'Spike': 'Cartoons'}
def origine(o):
    if o['m'] != 'Furry': return o['m']
    if o.get('om'): return o['om']
    if o['n'] in ORIG_M: return ORIG_M[o['n']]
    x = o['mo'].split("médium d'origine : ")[1].split(' ;')[0].strip()
    x = {"Cartoons / films d'animation occidentaux": 'Cartoons'}.get(x, x)
    assert x in MKEY, (o['n'], x)
    return x
def med_de(o):
    s = [MKEY[origine(o)]]
    if o['m'] == 'Furry': s.append('m:furry')
    if o['u'] in FILM: s.append('m:film')
    if o.get('e'): s.append('m:espece')
    if o['t'] in ROSTER and 'm:jv' not in s: s.insert(1, 'm:jv')   # jouable dans Marvel Rivals
    return s
def tags_de(o):
    s = list(F.get(o['u'], []))
    s += PERSO.get(o['t'], [])
    if o['t'] in RIVALS and RIVALS[o['t']][0] / RIVALS[o['t']][1] >= 0.10: s.append('marvel_rivals')
    if o['t'] in SPIDERVERSE and SPIDERVERSE[o['t']][0] / SPIDERVERSE[o['t']][1] >= 0.10: s.append('sony_pictures_animation')
    for t in s: assert t in TAGS, t
    return med_de(o) + especes_de(o) + sorted(set(s), key=list(TAGS).index)
out = {'tags': [dict(t=k, l=v[0], g=G0, p=None, n=v[1], k='m') for k, v in MED.items()] + tags_especes(ES) + [dict(t=k, l=v[0], g=v[1], p=v[2], n=v[3], k='c') for k, v in TAGS.items()],
       'r': [tags_de(o) for o in R], 'd': [tags_de(o) for o in D], 'e': [tags_de(o) for o in ES]}
assert all(f in {o['u'] for o in R + D + ES} for f in FILM), [f for f in FILM if f not in {o['u'] for o in R + D + ES}]
# contrôle : chaque franchise du tableau existe dans au moins une liste
noms = {o['u'] for o in R} | {o['u'] for o in D} | {o['u'] for o in ES}
absentes = [f for f in F if f not in noms]
assert not absentes, absentes
json.dump(out, open(B + 'donnees_copyright_2026-10-25.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
cop = lambda o: [t for t in tags_de(o) if not t.startswith(('m:', 's:'))]
for nom, L in (('rule34', R), ('danbooru', D), ('especes', ES)):
    c = collections.Counter(t for o in L for t in tags_de(o))
    print(nom, sum(1 for o in L if cop(o)), '/', len(L), 'avec au moins un tag Copyright ;', dict(c.most_common()))
print('Marvel Rivals :', [o['n'] for o in R if 'marvel_rivals' in tags_de(o)])
# contrôle et résumé de la catégorie « Espèce »
import especes_filtre as EF
cles = {t['t'] for t in out['tags']}
tous = R + D + ES
assert all(k in cles for o in tous for k in tags_de(o) if k.startswith('s:'))
connus = {o['t'] for o in tous} | {o.get('td') for o in tous}
assert all(k in connus for k in EF.PERSO), [k for k in EF.PERSO if k not in connus]
ce = collections.Counter(k for L in (R, D) for o in L for k in especes_de(o))
print('Espèce :', len(tags_especes(ES)), 'tags ;', sum(1 for o in R if especes_de(o)), '/', len(R), 'Rule34 ;', sum(1 for o in D if especes_de(o)), '/', len(D), 'Danbooru ;', dict(ce.most_common()))
