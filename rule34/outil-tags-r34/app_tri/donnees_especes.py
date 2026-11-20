# Espèces ajoutables en option dans EdeniaList (25/10/2026).
# Source : autres_tags_personnages_270_hors_feminins_2026-10-25.csv (groupe « espèce », 74 tags relevés pages 1-390).
# Retenues : espèces au design défini venant d'une œuvre précise (58 ; +3 le 25/10 avec les pages 331-340 : Mangriff, Deathclaw, Guilmon ; +9 avec les pages 361-390 : Orc de Warcraft, Luxray, Feunard, Malamandre, Tournesol de PvZ, Quarien, Riolu, Zeraora, Kirlia).
# Écartées (7) :
#   robloxian (avatar Roblox personnalisable, pas de design défini) ; protogen (espèce furry de création originale, pas d'une œuvre) ;
#   human_(world_of_warcraft) (humain, pas de design propre) ; mobian_(species) (tous les animaux de Sonic, designs variés) ;
#   vastaya (League of Legends, designs très variés : Ahri, Xayah, Rakan…) ; gem_(species) (Steven Universe, chaque Gemme a son design) ;
#   pal_(species) (toutes les créatures de Palworld).
# Tags généraux non retenus (pas des espèces d'une œuvre) : mythologie, oc / original_character, etc.
# Danbooru et e621 : API tags.json, 25/10/2026 (réponses brutes : especes_api_2026-10-25.json).
# Furry : mêmes critères que classer_v9.py : (1) animal anthropomorphe ou créature animale ; (2) indice e621 >= 2
#   (indice = (e621 / rule34) / (743 132 / 3 721 392)).
import csv, json
B = '/home/user/outil_tags_r34/'
REF = 743132 / 3721392
rows = {r['tag']: r for r in csv.DictReader(open(B + 'autres_tags_personnages_270_hors_feminins_2026-10-25.csv', encoding='utf-8-sig')) if r['groupe'] == 'espèce'}
API = json.load(open(B + 'app_tri/especes_api_2026-10-25.json'))
EXCLUES = {'robloxian', 'protogen', 'human_(world_of_warcraft)', 'mobian_(species)', 'vastaya', 'gem_(species)', 'pal_(species)'}
JV, AN, CA, AU = 'Jeux vidéo', 'Animanga', 'Cartoons', 'Autres'
# tag rule34 : (nom affiché, œuvre, médium d'origine, animal ?, tag Danbooru ou '', tag e621 ou '')
P = 'Pokémon'
E = {
 'gardevoir': ('Gardevoir', P, JV, 1, 'gardevoir', 'gardevoir'),
 'lucario': ('Lucario', P, JV, 1, 'lucario', 'lucario'),
 'renamon': ('Renamon', 'Digimon', AN, 1, 'renamon', 'renamon'),
 'draenei': ('Draeneï', 'Warcraft', JV, 0, 'draenei', 'draenei'),
 'umbreon': ('Noctali (Umbreon)', P, JV, 1, 'umbreon', 'umbreon'),
 'night_elf': ('Elfe de la nuit', 'Warcraft', JV, 0, 'night_elf_(warcraft)', 'night_elf'),
 'lopunny': ('Lockpin (Lopunny)', P, JV, 1, 'lopunny', 'lopunny'),
 'yordle': ('Yordle', 'League of Legends', JV, 0, 'yordle', 'yordle'),
 'inkling': ('Inkling', 'Splatoon', JV, 0, 'inkling', 'inkling'),
 "miqo'te": ("Miqo'te", 'Final Fantasy XIV', JV, 0, "miqo'te", "miqo'te"),
 'eevee': ('Évoli (Eevee)', P, JV, 1, 'eevee', 'eevee'),
 'pikachu': ('Pikachu', P, JV, 1, 'pikachu', 'pikachu'),
 'blood_elf': ('Elfe de sang', 'Warcraft', JV, 0, 'blood_elf_(warcraft)', 'blood_elf'),
 'sylveon': ('Nymphali (Sylveon)', P, JV, 1, 'sylveon', 'sylveon'),
 'koopa': ('Koopa', 'Super Mario', JV, 1, 'koopa_troopa', 'koopa'),
 'vaporeon': ('Aquali (Vaporeon)', P, JV, 1, 'vaporeon', 'vaporeon'),
 'octoling': ('Octaling (Octoling)', 'Splatoon', JV, 0, 'octoling', 'octoling'),
 'glaceon': ('Givrali (Glaceon)', P, JV, 1, 'glaceon', 'glaceon'),
 'zoroark': ('Zoroark', P, JV, 1, 'zoroark', 'zoroark'),
 'charizard': ('Dracaufeu (Charizard)', P, JV, 1, 'charizard', 'charizard'),
 'braixen': ('Roussil (Braixen)', P, JV, 1, 'braixen', 'braixen'),
 'au_ra': ('Au Ra', 'Final Fantasy XIV', JV, 0, 'au_ra', 'au_ra'),
 'asari': ('Asari', 'Mass Effect', JV, 0, 'asari_(mass_effect)', 'asari'),
 'hilichurls_(species)': ('Brutocollinus (Hilichurl)', 'Genshin Impact', JV, 0, 'hilichurl_(genshin_impact)', 'hilichurl'),
 'togruta': ('Togruta', 'Star Wars', AU, 0, 'togruta', 'togruta'),
 'arcanine': ('Arcanin (Arcanine)', P, JV, 1, 'arcanine', 'arcanine'),
 'cinderace': ('Pyrobut (Cinderace)', P, JV, 1, 'cinderace', 'cinderace'),
 'espeon': ('Mentali (Espeon)', P, JV, 1, 'espeon', 'espeon'),
 'worgen': ('Worgen', 'Warcraft', JV, 1, 'worgen', 'worgen'),
 'absol': ('Absol', P, JV, 1, 'absol', 'absol'),
 'lycanroc': ('Lougaroc (Lycanroc)', P, JV, 1, 'lycanroc', 'lycanroc'),
 'meowscarada': ('Miascarade (Meowscarada)', P, JV, 1, 'meowscarada', 'meowscarada'),
 'changeling': ('Changelin', 'My Little Pony', CA, 1, '', 'changeling_(mlp)'),
 'blaziken': ('Braségali (Blaziken)', P, JV, 1, 'blaziken', 'blaziken'),
 'leafeon': ('Phyllali (Leafeon)', P, JV, 1, 'leafeon', 'leafeon'),
 'viera': ('Viera', 'Final Fantasy', JV, 0, 'viera', 'viera'),
 'jolteon': ('Voltali (Jolteon)', P, JV, 1, 'jolteon', 'jolteon'),
 'goodra': ('Muplodocus (Goodra)', P, JV, 1, 'goodra', 'goodra'),
 'xenomorph': ('Xénomorphe', 'Alien', AU, 0, 'xenomorph', 'xenomorph'),
 "twi'lek": ("Twi'lek", 'Star Wars', AU, 0, "twi'lek", "twi'lek"),
 'mewtwo': ('Mewtwo', P, JV, 1, 'mewtwo', 'mewtwo'),
 'flareon': ('Pyroli (Flareon)', P, JV, 1, 'flareon', 'flareon'),
 'typhlosion': ('Typhlosion', P, JV, 1, 'typhlosion', 'typhlosion'),
 'lugia': ('Lugia', P, JV, 1, 'lugia', 'lugia'),
 'yoshi': ('Yoshi (espèce)', 'Super Mario', JV, 1, 'yoshi', 'yoshi'),
 'hypno': ('Hypnomade (Hypno)', P, JV, 1, 'hypno', 'hypno_(pokemon)'),
 'delphox': ('Goupelin (Delphox)', P, JV, 1, 'delphox', 'delphox'),
 'argonian': ('Argonien', 'The Elder Scrolls', JV, 1, 'argonian', 'argonian'),
 'sangheili': ('Sangheili (Élite)', 'Halo', JV, 0, 'sangheili', 'sangheili'),
 'vulpix': ('Goupix (Vulpix)', P, JV, 1, 'vulpix', 'vulpix'),
 'tauren': ('Tauren', 'Warcraft', JV, 1, 'tauren_(warcraft)', 'tauren'),
 'incineroar': ('Félinferno (Incineroar)', P, JV, 1, 'incineroar', 'incineroar'),
 'gerudo': ('Gerudo', 'The Legend of Zelda', JV, 0, 'gerudo', 'gerudo'),
 'snivy': ('Vipélierre (Snivy)', P, JV, 1, 'snivy', 'snivy'),
 'raichu': ('Raichu', P, JV, 1, 'raichu', 'raichu'),
 # pages 331-340 (25/10/2026)
 'zangoose': ('Mangriff (Zangoose)', P, JV, 1, 'zangoose', 'zangoose'),
 'deathclaw': ('Deathclaw', 'Fallout', JV, 1, 'deathclaw', 'deathclaw'),
 'guilmon': ('Guilmon', 'Digimon', AN, 1, 'guilmon', 'guilmon'),
 # pages 361-390 (25/10/2026)
 'orc_(warcraft)': ('Orc (Warcraft)', 'Warcraft', JV, 0, '', ''),
 'luxray': ('Luxray', P, JV, 1, 'luxray', 'luxray'),
 'ninetales': ('Feunard (Ninetales)', P, JV, 1, 'ninetales', 'ninetales'),
 'salazzle': ('Malamandre (Salazzle)', P, JV, 1, 'salazzle', 'salazzle'),
 'sunflower_(pvz)': ('Tournesol (Plants vs. Zombies)', 'Plants vs. Zombies', JV, 0, '', 'sunflower_(pvz)'),
 'quarian': ('Quarien', 'Mass Effect', JV, 0, 'quarian', 'quarian'),
 'riolu': ('Riolu', P, JV, 1, 'riolu', 'riolu'),
 'zeraora': ('Zeraora', P, JV, 1, 'zeraora', 'zeraora'),
 'kirlia': ('Kirlia', P, JV, 1, 'kirlia', 'kirlia'),
}
NOTE = {
 'renamon': "franchise Digimon : jouet virtuel Bandai à l'origine, connue surtout par l'anime ; rangée en Animanga",
 'yordle': "humanoïde (comme Poppy, laissée en jeux vidéo)", 'sangheili': "extraterrestre non animal : laissé hors Furry malgré l'indice, à confirmer",
 'xenomorph': "créature extraterrestre non animale : laissée hors Furry malgré l'indice, à confirmer ; film Alien (1979)",
 'togruta': "espèce des films Star Wars (L'Attaque des clones, 2002) ; Ahsoka Tano en est la plus connue",
 "twi'lek": "espèce des films Star Wars (Le Retour du Jedi, 1983)", 'koopa': "Danbooru : pas de tag d'espèce, koopa_troopa utilisé",
 'changeling': "Danbooru : aucun tag trouvé", 'deathclaw': "créature mutante (caméléon) de la série Fallout (1997)",
'orc_(warcraft)': "Danbooru : orc_(warcraft) 0 ; e621 : seul le tag général orc (tous les orques), non utilisé", 'sunflower_(pvz)': "plante de Plants vs. Zombies (PopCap, 2009), souvent dessinée en fille humanisée ; Danbooru : pas de tag",
 'quarian': "Danbooru : quarian est un tag général (catégorie 0)", 'guilmon': "Digimon Tamers (anime, 2001), comme Renamon : rangé en Animanga", 'viera': "Final Fantasy Tactics Advance, XII et XIV",
}
assert set(E) | EXCLUES == set(rows), set(rows) ^ (set(E) | EXCLUES)
out = []
for t, (n, u, mo, ani, td, te) in E.items():
    r = int(rows[t]['publications'])
    d = API['db'][td][0] if td else 0
    e6 = API['e6'].get(te)
    e6 = e6[0] if isinstance(e6, list) else 0
    idx = e6 / r / REF
    furry = bool(ani and idx >= 2)
    note = (f"médium d'origine : {mo} ; " if furry else '') + f"e621 {e6} publications, indice e621 {idx:.2f}" + (" ; " + NOTE[t] if t in NOTE else '')
    if ani and not furry: note += " ; créature animale mais indice e621 < 2 : laissée dans son médium d'origine"
    out.append(dict(n=n, u=u, s='E', m='Furry' if furry else mo, mo=note, t=t, r=r, b=r, g=0,
                    q="espèce : doublons non audités", a=0, td=td, d=d, e=1, om=mo))
json.dump(out, open(B + 'app_tri/donnees_especes_2026-10-25.json', 'w', encoding='utf-8'), ensure_ascii=False)
import collections
print(len(out), collections.Counter(o['m'] for o in out))
print([o['n'] for o in out if E[o['t']][3] and o['m'] != 'Furry'])
