# Catégorie de filtre « Espèce » d'EdeniaList (25/10/2026).
# Demande : une catégorie de filtre (comme Animanga, Comics…) qui liste les espèces ; cliquer sur « Inkling » affiche les personnages Inkling.
# Périmètre choisi par toi (option 1) : toute espèce ou race DÉFINIE PAR SON ŒUVRE (nom ou classification propre à l'univers),
# même si son tag rule34 est petit. Pas de tag « Humain » (ni l'humain de World of Warcraft), pas d'animaux réels
# (renard, lapin, chauve-souris…), pas de créatures génériques du folklore (démon, vampire, elfe, ange, fée, dragon, oni,
# kitsune, succube, sorcière, fantôme) ni de robots / androïdes génériques.
# Espèce = fait canonique de l'œuvre (profil officiel ou wiki de l'œuvre) ; les cas douteux sont laissés sans espèce (liste DOUTE).
# Les fiches « espèce » de l'option Espèces reçoivent leur propre tag (Inkling → Inkling, Gardevoir → Gardevoir…).

# id : (libellé, œuvre, note)
ESP = {
 'mobien': ('Mobien', 'Sonic', "animaux anthropomorphes de Mobius ; terme des séries animées et des comics (tag rule34 mobian_(species)), les jeux ne nomment pas l'espèce"),
 'hellhound': ('Hellhound', 'Helluva Boss', "classe de démons de l'univers Hazbin Hotel / Helluva Boss"),
 'imp': ('Imp', 'Helluva Boss', "classe de démons de l'univers Hazbin Hotel / Helluva Boss"),
 'poney_terrestre': ('Poney terrestre', 'My Little Pony', "une des tribus de poneys de My Little Pony"),
 'pegase': ('Pégase', 'My Little Pony', "une des tribus de poneys de My Little Pony"),
 'licorne': ('Licorne', 'My Little Pony', "une des tribus de poneys de My Little Pony"),
 'alicorne': ('Alicorne', 'My Little Pony', "poney à ailes et corne (Celestia, Luna, Cadance ; Twilight Sparkle depuis la fin de la saison 3)"),
 'changelin': ('Changelin', 'My Little Pony', ''),
 'monstre_ut': ('Monstre (Undertale / Deltarune)', 'Undertale / Deltarune', "race des monstres de l'univers de Toby Fox (Toriel et Asriel : monstres « boss »)"),
 'hylien': ('Hylien', 'The Legend of Zelda', ''),
 'twili': ('Twili', 'The Legend of Zelda', 'Twilight Princess (2006)'),
 'gerudo': ('Gerudo', 'The Legend of Zelda', ''),
 'koopa': ('Koopa', 'Super Mario', ''),
 'inkling': ('Inkling', 'Splatoon', ''),
 'octoling': ('Octaling (Octoling)', 'Splatoon', ''),
 'vastaya': ('Vastaya', 'League of Legends', ''),
 'yordle': ('Yordle', 'League of Legends', ''),
 'togruta': ('Togruta', 'Star Wars', ''),
 'twilek': ("Twi'lek", 'Star Wars', ''),
 'asari': ('Asari', 'Mass Effect', ''),
 'saiyan': ('Saiyan', 'Dragon Ball', 'Kefla : fusion de deux Saiyans (Kale et Caulifla)'),
 'shinigami': ('Shinigami (Bleach)', 'Bleach', "âmes combattantes de la Soul Society ; Ichigo : hybride (humain, Shinigami, Hollow, Quincy)"),
 'kryptonien': ('Kryptonien', 'DC Comics', ''),
 'tamaraneen': ('Tamaranéen', 'DC Comics', ''),
 'mutant': ('Mutant (Marvel)', 'Marvel', "Homo superior, nés avec le gène X"),
 'symbiote': ('Symbiote (Klyntar)', 'Marvel', ''),
 'faunus': ('Faunus', 'RWBY', ''),
 'gemme': ('Gemme', 'Steven Universe', ''),
 'bonbon': ('Peuple bonbon', 'Adventure Time', 'Princesse Chewing-gum : souveraine et créatrice du peuple bonbon, faite de chewing-gum'),
 'thiren': ('Thiren', 'Zenless Zone Zero', "humanoïdes aux traits animaux (Jane Doe : rat ; Ellen Joe : requin ; Miyabi : renard)"),
 'adepte': ('Adepte', 'Genshin Impact', "Ganyu : moitié adepte (qilin), moitié humaine"),
 'lame_xc2': ('Lame (Blade)', 'Xenoblade Chronicles 2', "Pyra et Mythra : l'Aegis, Lame légendaire"),
 'klaxo': ('Klaxo Sapiens (hybride)', 'Darling in the Franxx', "Zero Two : hybride humain / klaxosaure"),
 'cerinien': ('Cérinien', 'Star Fox', "Krystal : dernière survivante de la planète Cerinia"),
 'tarkatan': ('Tarkatan', 'Mortal Kombat', "Mileena : clone hybride tarkatan / édénien"),
 'edenien': ('Édénien', 'Mortal Kombat', "Mileena : clone hybride tarkatan / édénien"),
 'kanmusu': ('Kanmusu (fille-navire)', 'Kantai Collection', ''),
 'uma_musume': ('Uma Musume', 'Uma Musume', "filles aux oreilles et à la queue de cheval portant le nom d'un cheval de course"),
 'friend_kf': ('Friend (Kemono Friends)', 'Kemono Friends', 'animal transformé en fille'),
 't_doll': ('T-Doll (poupée tactique)', "Girls' Frontline", ''),
 'cautus': ('Cautus', 'Arknights', 'Amiya : Cautus / Chimère (profil officiel)'),
 'chimere_ak': ('Chimère (Arknights)', 'Arknights', 'Amiya : Cautus / Chimère (profil officiel)'),
 'lupo': ('Lupo', 'Arknights', ''),
 'aegir': ('Aegir', 'Arknights', ''),
 'vulpo': ('Vulpo', 'Arknights', ''),
 'lunarien': ('Lunarien', 'Touhou Project', ''),
 'lapin_lunaire': ('Lapin lunaire', 'Touhou Project', ''),
 'demi_fantome': ('Demi-fantôme', 'Touhou Project', 'moitié humaine, moitié fantôme'),
 'ancetre': ('Ancêtre véritable (True Ancestor)', 'Tsukihime', ''),
 # relevé 341-360 (25/10/2026)
 'mewmain': ('Mewmain (Mewman)', 'Star vs. les forces du mal', 'habitants humanoïdes du royaume de Mewni ; Star : princesse de Mewni'),
 'homme_bete_mt': ('Homme-bête (Mushoku Tensei)', 'Mushoku Tensei', 'race des hommes-bêtes ; Ghislaine : tribu Dedoldia'),
 'kansen': ('KAN-SEN (fille-navire)', 'Azur Lane', ''),
 'abyssal': ('Abyssal (Shinkaisei-kan)', 'Kantai Collection', "ennemies des kanmusu ; Northern Ocean Princess : « princesse » abyssale"),
 # relevé 361-390 (25/10/2026)
 'sheikah': ('Sheikah', 'The Legend of Zelda', 'Purah : chercheuse sheikah'),
 'sankta': ('Sankta', 'Arknights', 'Exusiai : Sankta (auréole et ailes de lumière)'),
 'halovien': ('Halovien (Halovian)', 'Honkai: Star Rail', 'Robin : Halovienne de Penacony'),
}
# personnage (tag rule34 ou Danbooru) -> espèces
PERSO = {
 'rouge_the_bat': ['mobien'], 'amy_rose': ['mobien'], 'vanilla_the_rabbit': ['mobien'], 'cream_the_rabbit': ['mobien'], 'sally_acorn': ['mobien'],
 'sonic_the_hedgehog': ['mobien'], 'tails_the_fox': ['mobien'], 'knuckles_the_echidna': ['mobien'],
 'loona_(helluva_boss)': ['hellhound'], 'millie_(helluva_boss)': ['imp'], 'moxxie_(helluva_boss)': ['imp'],
 'pinkie_pie_(mlp)': ['poney_terrestre'], 'applejack_(mlp)': ['poney_terrestre'], 'big_macintosh_(mlp)': ['poney_terrestre'],
 'fluttershy_(mlp)': ['pegase'], 'rainbow_dash_(mlp)': ['pegase'], 'rarity_(mlp)': ['licorne'], 'shining_armor_(mlp)': ['licorne'],
 'twilight_sparkle_(mlp)': ['alicorne'], 'princess_celestia_(mlp)': ['alicorne'], 'princess_luna_(mlp)': ['alicorne'], 'princess_cadance_(mlp)': ['alicorne'],
 'queen_chrysalis_(mlp)': ['changelin'],
 'toriel': ['monstre_ut'], 'asriel_dreemurr': ['monstre_ut'], 'susie_(deltarune)': ['monstre_ut'], 'noelle_holiday': ['monstre_ut'],
 'princess_zelda': ['hylien'], 'link': ['hylien'], 'midna': ['twili'], 'bowser': ['koopa'],
 'callie_(splatoon)': ['inkling'], 'marie_(splatoon)': ['inkling'], 'marina_(splatoon)': ['octoling'],
 'ahri': ['vastaya'], 'poppy': ['yordle'], 'tristana': ['yordle'], 'ahsoka_tano': ['togruta'], "liara_t'soni": ['asari'],
 'son_goku': ['saiyan'], 'caulifla': ['saiyan'], 'kefla': ['saiyan'],
 'shihouin_yoruichi': ['shinigami'], 'kuchiki_rukia': ['shinigami'], 'matsumoto_rangiku': ['shinigami'], 'ichigo_kurosaki': ['shinigami'],
 'supergirl': ['kryptonien'], 'power_girl': ['kryptonien'], 'starfire': ['tamaraneen'],
 'emma_frost': ['mutant'], 'psylocke ∪ psylocke_(kwannon)': ['mutant'], 'rogue_(x-men)': ['mutant'], 'venom_(marvel)': ['symbiote'],
 'blake_belladonna': ['faunus'], 'peridot_(steven_universe)': ['gemme'], 'princess_bubblegum': ['bonbon'],
 'jane_doe_(zenless_zone_zero)': ['thiren'], 'ellen_joe': ['thiren'], 'hoshimi_miyabi': ['thiren'],
 'ganyu_(genshin_impact)': ['adepte'], 'pyra': ['lame_xc2'], 'mythra': ['lame_xc2'], 'zero_two_(darling_in_the_franxx)': ['klaxo'],
 'krystal': ['cerinien'], 'mileena': ['tarkatan', 'edenien'],
 # Top Danbooru (tag Danbooru)
 'serval_(kemono_friends)': ['friend_kf'], "hk416_(girls'_frontline)": ['t_doll'],
 'amiya_(arknights)': ['cautus', 'chimere_ak'], 'texas_(arknights)': ['lupo'], 'lappland_(arknights)': ['lupo'], 'skadi_(arknights)': ['aegir'], 'suzuran_(arknights)': ['vulpo'],
 'houraisan_kaguya': ['lunarien'], 'yagokoro_eirin': ['lunarien'], 'reisen_udongein_inaba': ['lapin_lunaire'], 'konpaku_youmu': ['demi_fantome'],
 'arcueid_brunestud': ['ancetre'],
 # relevé 341-360 (25/10/2026)
 'trixie_(mlp)': ['licorne'], 'lapis_lazuli_(steven_universe)': ['gemme'], 'star_butterfly': ['mewmain'], 'ghislaine_dedoldia': ['homme_bete_mt'],
 'northern_ocean_princess': ['abyssal'],
 # relevé 361-390 (25/10/2026)
 'xayah': ['vastaya'], 'vex_(league_of_legends)': ['yordle'], 'purah': ['sheikah'], 'pearl_(steven_universe)': ['gemme'],
 # Surge : classée Mobien (tenrec né sur la planète de Sonic, puis modifiée par le Dr Starline ; à la différence de Shadow, créé artificiellement)
 'muffet': ['monstre_ut'], 'undyne': ['monstre_ut'], 'surge_the_tenrec': ['mobien'], 'magik_(illyana_rasputin)': ['mutant'],
 'angelina_(arknights)': ['vulpo'], 'exusiai_(arknights)': ['sankta'], 'robin_(honkai:_star_rail)': ['halovien'],
}
# exceptions à l'espèce de franchise (Northern Ocean Princess : abyssale, pas kanmusu)
SANS_FRANCHISE = {'northern_ocean_princess', 'female_admiral_(kancolle)'}  # Amiral (version féminine) : humaine, pas kanmusu
# toute la franchise
FRANCHISE = {'Kantai Collection': ['kanmusu'], 'Uma Musume': ['uma_musume'], 'Azur Lane': ['kansen']}
# fiches de l'option Espèces dont l'espèce existe déjà ci-dessus (même tag pour la fiche et les personnages)
FICHE = {'inkling': 'inkling', 'octoling': 'octoling', 'koopa': 'koopa', 'yordle': 'yordle', 'togruta': 'togruta', 'asari': 'asari',
         'changeling': 'changelin', 'gerudo': 'gerudo', "twi'lek": 'twilek'}
# laissés sans espèce (doute ou espèce générique), à trancher si tu veux
DOUTE = {
 'shadow_the_hedgehog': "forme de vie artificielle créée par Gerald Robotnik, pas un Mobien de naissance",
 'blaze_the_cat': "vient de la dimension Sol ; « Mobien » non attesté pour elle",
 'ralsei': "statut (Darkner ou non) discuté dans Deltarune",
 'bowsette': "création de fans (couronne de Peach sur Bowser)",
 'squirrel_girl_(marvel)': "présentée comme mutante à ses débuts, statut flou ensuite",
 'charlie_morningstar_(hazbin_hotel)': "« Hellborn », fille de Lucifer et de Lilith : pas une classe comme Hellhound ou Imp",
 'gwen_tennyson': "humaine, un quart Anodite",
 'kit_(gameoverse)': "chatte humanoïde d'un monde de jeu vidéo ; nom d'espèce non attesté",
 'felicia_(darkstalkers)': "femme-chat (catwoman) de Darkstalkers : créature générique",
 'raven_team_leader': "costume d'ours ou personnage anthropomorphe : non tranché par Epic",
 'vaggie_(hazbin_hotel)': "ange exterminatrice déchue : créature générique (ange)",
 'firefly_(honkai:_star_rail)': "soldate modifiée de Glamoth (Fer-Cavalerie) : pas une espèce",
 'tohru_(dragon_maid)': "dragonne : créature générique (dragon)", 'ariel': "sirène : créature générique du folklore",
 'luna_snow': "pouvoirs de glace acquis (pas une espèce)", 'marcille_donato': "demi-elfe : créature générique (elfe)",
 'Touhou Project': "la plupart des personnages sont des yôkai du folklore japonais (vampire, kappa, tengu, oni, kitsune, fée…) : créatures génériques, non incluses ; seuls Lunarien, Lapin lunaire et Demi-fantôme sont propres à l'œuvre",
}

def especes_de(o):
    if o.get('e'):
        t = o['t']
        return ['s:' + FICHE.get(t, t)]
    s = []
    for k in (o['t'], o.get('td')):
        s += PERSO.get(k, [])
    if not ({o['t'], o.get('td')} & SANS_FRANCHISE): s += FRANCHISE.get(o['u'], [])
    return ['s:' + x for x in dict.fromkeys(s)]

def tags_especes(ES):
    """Liste des tags du groupe « Espèce » : espèces ci-dessus + fiches de l'option qui n'y sont pas."""
    L = [dict(t='s:' + k, l=v[0], g='Espèce', p=None, n=v[1] + (' · ' + v[2] if v[2] else ''), k='s') for k, v in ESP.items()]
    for o in ES:
        if o['t'] in FICHE: continue
        L.append(dict(t='s:' + o['t'], l=o['n'], g='Espèce', p=o['r'], n=o['u'] + ' · fiche de l’option Espèces', k='s'))
    return L
