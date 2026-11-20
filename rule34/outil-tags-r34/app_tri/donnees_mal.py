# Page « MyAnimeList » d'EdeniaList (25/10/2026) : top 100 des personnages favoris de MyAnimeList.
# Source : https://myanimelist.net/character.php (limit=0 et limit=50), relevé du 25/10/2026, pages brutes dans
# myanimelist/brut/ (top_0.html, top_50.html) et extraction dans myanimelist/brut/top100_mal_brut_2026-10-25.json.
# « Favoris » = nombre de membres MAL qui ont mis le personnage dans leurs favoris (tous genres confondus, comme sur MAL).
# Nom affiché (ordre prénom nom), œuvre et sexe : ajoutés à la main. Sexe « ? » : Hange Zoë (genre laissé ouvert par l'auteur)
# et Rimuru Tempest (slime sans sexe).
# Lien avec EdeniaList : tag rule34 si le personnage est dans la sélection Rule34 de l'application (compteurs audités),
# sinon dans le Top Danbooru (compteur rule34 de l'autocomplétion), sinon parmi les masculins du classement des
# franchises « tous » (compteur du tag seul). Aucun nouveau compteur n'a été relevé pour cette page.
import json, csv
B = '/home/user/outil_tags_r34/'
raw = json.load(open(B + 'myanimelist/brut/top100_mal_brut_2026-10-25.json', encoding='utf-8'))
# rang : (nom affiché, œuvre, sexe, lien) ; lien = ('r', tag app Rule34) | ('d', tag Top Danbooru) | ('t', franchise, nom) | None
M = {
 1: ('Lelouch Lamperouge', 'Code Geass', 'M', None), 2: ('Monkey D. Luffy', 'One Piece', 'M', ('r', 'monkey_d_luffy')),
 3: ('Levi Ackerman', "L'Attaque des Titans", 'M', None), 4: ('L (Lawliet)', 'Death Note', 'M', None),
 5: ('Roronoa Zoro', 'One Piece', 'M', ('t', 'One Piece', 'Roronoa Zoro')), 6: ('Killua Zoldyck', 'Hunter x Hunter', 'M', None),
 7: ('Rintarou Okabe', 'Steins;Gate', 'M', None), 8: ('Light Yagami', 'Death Note', 'M', None),
 9: ('Edward Elric', 'Fullmetal Alchemist', 'M', None), 10: ('Naruto Uzumaki', 'Naruto', 'M', ('r', 'uzumaki_naruto')),
 11: ('Guts', 'Berserk', 'M', None), 12: ('Gintoki Sakata', 'Gintama', 'M', ('t', 'Gintama', 'Gintoki Sakata')),
 13: ('Eren Jäger (Yeager)', "L'Attaque des Titans", 'M', None), 14: ('Kurisu Makise', 'Steins;Gate', 'F', None),
 15: ('Itachi Uchiha', 'Naruto', 'M', None), 16: ('Satoru Gojo', 'Jujutsu Kaisen', 'M', ('t', 'Jujutsu Kaisen', 'Satoru Gojo')),
 17: ('Mikasa Ackerman', "L'Attaque des Titans", 'F', ('r', 'mikasa_ackerman')), 18: ('Ken Kaneki', 'Tokyo Ghoul', 'M', None),
 19: ('Hachiman Hikigaya', 'Oregairu', 'M', None), 20: ('Spike Spiegel', 'Cowboy Bebop', 'M', None),
 21: ('Kakashi Hatake', 'Naruto', 'M', None), 22: ('Rem', 'Re:Zero', 'F', ('r', 'rem_(re:zero)')),
 23: ('Saitama', 'One Punch Man', 'M', None), 24: ('Joseph Joestar', "JoJo's Bizarre Adventure", 'M', None),
 25: ('Arataka Reigen', 'Mob Psycho 100', 'M', None), 26: ('Megumin', 'KonoSuba', 'F', ('r', 'megumin')),
 27: ('Hitagi Senjougahara', 'Monogatari', 'F', None), 28: ('Kazuto Kirigaya (Kirito)', 'Sword Art Online', 'M', None),
 29: ('Mai Sakurajima', 'Bunny Girl Senpai', 'F', None), 30: ('Violet Evergarden', 'Violet Evergarden', 'F', None),
 31: ('Roy Mustang', 'Fullmetal Alchemist', 'M', None), 32: ('Yato', 'Noragami', 'M', None),
 33: ('Zero Two', 'Darling in the Franxx', 'F', ('r', 'zero_two_(darling_in_the_franxx)')), 34: ('Ichigo Kurosaki', 'Bleach', 'M', ('r', 'ichigo_kurosaki')),
 35: ('Kiyotaka Ayanokouji', 'Classroom of the Elite', 'M', None), 36: ('Osamu Dazai', 'Bungou Stray Dogs', 'M', None),
 37: ('Thorfinn', 'Vinland Saga', 'M', None), 38: ('Hisoka Morow', 'Hunter x Hunter', 'M', None),
 39: ('Kamina', 'Gurren Lagann', 'M', None), 40: ('Eikichi Onizuka', 'GTO', 'M', None),
 41: ('Saber (Artoria Pendragon)', 'Fate', 'F', ('r', 'artoria_pendragon')), 42: ('Sanji', 'One Piece', 'M', None),
 43: ('Shinobu Oshino', 'Monogatari', 'F', ('d', 'oshino_shinobu')), 44: ('Frieren', 'Frieren', 'F', ('r', 'frieren')),
 45: ('Taiga Aisaka', 'Toradora!', 'F', None), 46: ('Asuka Langley Souryuu', 'Evangelion', 'F', ('r', 'asuka_langley_sohryu')),
 47: ('Koyomi Araragi', 'Monogatari', 'M', None), 48: ('Son Goku', 'Dragon Ball', 'M', ('r', 'son_goku')),
 49: ('Askeladd', 'Vinland Saga', 'M', None), 50: ('Sasuke Uchiha', 'Naruto', 'M', ('r', 'sasuke_uchiha')),
 51: ('Subaru Natsuki', 'Re:Zero', 'M', None), 52: ('Asuna Yuuki', 'Sword Art Online', 'F', ('r', 'yuuki_asuna')),
 53: ('Alucard', 'Hellsing', 'M', None), 54: ('Yuno Gasai', 'Mirai Nikki', 'F', None),
 55: ('Holo', 'Spice and Wolf', 'F', None), 56: ('Erwin Smith', "L'Attaque des Titans", 'M', None),
 57: ('C.C.', 'Code Geass', 'F', ('d', 'c.c.')), 58: ('Shigeo Kageyama (Mob)', 'Mob Psycho 100', 'M', None),
 59: ('Johan Liebert', 'Monster', 'M', None), 60: ('Homura Akemi', 'Madoka Magica', 'F', ('d', 'akemi_homura')),
 61: ('Jotaro Kujo', "JoJo's Bizarre Adventure", 'M', ('r', 'jotaro_kujo')), 62: ('Kurapika', 'Hunter x Hunter', 'M', None),
 63: ('Kaguya Shinomiya', 'Kaguya-sama: Love is War', 'F', ('r', 'shinomiya_kaguya')), 64: ('Marin Kitagawa', 'My Dress-Up Darling', 'F', ('r', 'kitagawa_marin')),
 65: ('Maomao', 'Les Carnets de l\u2019apothicaire', 'F', None), 66: ('Izuku Midoriya', 'My Hero Academia', 'M', ('r', 'izuku_midoriya')),
 67: ('Kaori Miyazono', 'Your Lie in April', 'F', None), 68: ('Rin Tohsaka', 'Fate', 'F', ('r', 'tohsaka_rin')),
 69: ('Shouto Todoroki', 'My Hero Academia', 'M', None), 70: ('Tanjirou Kamado', 'Demon Slayer', 'M', None),
 71: ('Emilia', 'Re:Zero', 'F', ('r', 'emilia_(re:zero)')), 72: ('Kusuo Saiki', 'The Disastrous Life of Saiki K.', 'M', None),
 73: ('Katsuki Bakugo', 'My Hero Academia', 'M', ('r', 'katsuki_bakugou')), 74: ('Rimuru Tempest', 'Moi, quand je me réincarne en Slime', '?', None),
 75: ('Senkuu Ishigami', 'Dr. Stone', 'M', None), 76: ('Nico Robin', 'One Piece', 'F', ('r', 'nico_robin')),
 77: ('Yukino Yukinoshita', 'Oregairu', 'F', None), 78: ('Denji', 'Chainsaw Man', 'M', ('r', 'denji_(chainsaw_man)')),
 79: ('Power', 'Chainsaw Man', 'F', ('r', 'power_(chainsaw_man)')), 80: ('Kurumi Tokisaki', 'Date A Live', 'F', None),
 81: ('Revy', 'Black Lagoon', 'F', None), 82: ('Gon Freecss', 'Hunter x Hunter', 'M', None),
 83: ('Houtarou Oreki', 'Hyouka', 'M', None), 84: ('Izaya Orihara', 'Durarara!!', 'M', None),
 85: ('Sebastian Michaelis', 'Black Butler', 'M', None), 86: ('Rei Ayanami', 'Evangelion', 'F', ('r', 'rei_ayanami')),
 87: ('Natsu Dragneel', 'Fairy Tail', 'M', None), 88: ('Miku Nakano', 'The Quintessential Quintuplets', 'F', ('r', 'nakano_miku')),
 89: ('Trafalgar Law', 'One Piece', 'M', None), 90: ('Yuu Ishigami', 'Kaguya-sama: Love is War', 'M', None),
 91: ('Armin Arlelt', "L'Attaque des Titans", 'M', None), 92: ('Shinji Ikari', 'Evangelion', 'M', None),
 93: ('Vegeta', 'Dragon Ball', 'M', ('t', 'Dragon Ball', 'Vegeta')), 94: ('Kazuma Satou', 'KonoSuba', 'M', None),
 95: ('Hange Zoë', "L'Attaque des Titans", '?', None), 96: ('Koro-sensei', 'Assassination Classroom', 'M', None),
 97: ('Gyro Zeppeli', "JoJo's Bizarre Adventure", 'M', None), 98: ('Rias Gremory', 'High School DxD', 'F', ('r', 'rias_gremory')),
 99: ('Musashi Miyamoto', 'Vagabond', 'M', None), 100: ('Rikka Takanashi', 'Chuunibyou demo Koi ga Shitai!', 'F', None),
}
assert sorted(M) == list(range(1, 101))
R = {o['t']: o for o in json.load(open(B + 'app_tri/donnees_app_2026-10-24.json', encoding='utf-8'))}
D = {o['td']: o for o in json.load(open(B + 'app_tri/donnees_app_top_danbooru_2026-10-24.json', encoding='utf-8'))}
T = json.load(open(B + 'franchises/tous_personnages_liste_2026-10-25.json', encoding='utf-8'))
# rang Rule34 dans la sélection de l'application (même calcul que la page : r = publications, gain d'union compris)
rgR = {o['t']: i for i, o in enumerate(sorted(R.values(), key=lambda o: -o['r']), 1)}
out = []
for x in raw:
    n, u, s, lien = M[x['rang']]
    o = dict(r=x['rang'], n=n, nm=x['nom_mal'], jp=x['jp'], u=u, s=s, f=x['fav'], url=x['url'],
             an=(x['anime'] or [''])[0], mg=(x['manga'] or [''])[0], lk='', t='', r34=None, g=0, db=None, rg=None, rd=None)
    if lien and lien[0] == 'r':
        a = R[lien[1]]; o.update(lk='r', t=a['t'], r34=a['r'], g=a['g'], db=a['d'] or None, rg=rgR[a['t']], rd=D[a['td']]['rd'] if a['td'] in D else None)
    elif lien and lien[0] == 'd':
        a = D[lien[1]]; o.update(lk='d', t=a['t'], r34=a['r'], db=a['d'], rd=a['rd'])
    elif lien:
        c = [p for p in T[lien[1]] if p[0] == lien[2]]
        assert len(c) == 1, lien
        o.update(lk='t', r34=c[0][1])
    out.append(o)
json.dump(out, open(B + 'app_tri/donnees_mal_2026-10-25.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
# CSV de la page (UTF-8 avec BOM)
with open(B + 'myanimelist/top100_personnages_favoris_mal_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['rang', 'personnage', 'nom_mal', 'oeuvre', 'sexe', 'favoris', 'url_mal', 'tag_rule34', 'rule34', 'danbooru', 'source_compteurs', 'date_releve'])
    for o in out:
        w.writerow([o['r'], o['n'], o['nm'], o['u'], o['s'], o['f'], o['url'], o['t'], o['r34'] if o['r34'] is not None else '',
                    o['db'] or '', {'r': 'sélection Rule34 (auditée)', 'd': 'Top Danbooru (rule34 : autocomplétion)', 't': 'franchises « tous » (tag seul)', '': ''}[o['lk']], '2026-10-25'])
import collections
print(len(out), collections.Counter(o['s'] for o in out), collections.Counter(o['lk'] for o in out), sum(o['f'] for o in out))
