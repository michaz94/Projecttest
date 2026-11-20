# Franchises les plus représentées, TOUS personnages confondus (24/10/2026 ; mises à jour du 25/10 avec les pages 331-340, 341-360 puis 361-390) :
# 388 féminins (sélection auditée, médium v12) + 65 masculins (46 de l'application de tri + 19 des pages 331-390, compteur du tag seul)
# + 6 personnages au genre non défini / au choix, relevés dans les pages 1 à 390 de la liste des tags rule34.xxx (seuil ≈ 5 000 publications).
import csv, json, collections
B = '/home/user/outil_tags_r34/'
fem = list(csv.DictReader(open(B+'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv', encoding='utf-8-sig')))
assert len(fem) == 388
app = json.load(open(B+'app_tri/donnees_app_2026-10-24.json'))
mas = [o for o in app if o['s'] == 'M']
assert len(mas) == 46
# genre non défini / au choix : seulement les personnages qui ne sont pas déjà comptés par une version féminine ou masculine
# (Byleth : byleth_(fire_emblem)_(female) déjà compté ; Commandant Shepard : femshep déjà compté ; Kindred : Agneau déjà comptée ;
#  Chara : female_chara déjà compté depuis le relevé 341-360 ; relevé 361-390 : Corrin (corrin_(fire_emblem)_(female)), Ranma (ranma-chan) et V de Cyberpunk 2077 (valerie_(cyberpunk_2077)) déjà comptés par leur version féminine ; the_avatar : sens indéterminé, exclu). MalO / SCP-1471 : 4 tags du même personnage non fusionnés, compté avec le plus gros (scp-1471-a).
AUTRES = [('Kris', 'Deltarune', 'kris_(deltarune)', 10733), ('Frisk', 'Undertale', 'frisk', 8006), ('MalO (SCP-1471)', 'SCP Foundation', 'scp-1471-a', 11431),
          ('Sensei', 'Blue Archive', 'sensei_(blue_archive)', 6953),
          ('Robin', 'Fire Emblem', 'robin_(fire_emblem)', 6456),  # Robin : pas de tag de version féminine dans la sélection
          ('Villageois·e', 'Animal Crossing', 'villager_(animal_crossing)', 5732)]  # relevé 341-360
# masculins des pages 331-360, pas (encore) dans l'application de tri : compteur du tag seul (liste des tags du 25/10), doublons non audités
# (les 5 des pages 311-330 sont dans l'application depuis le 25/10)
M_331 = [('Ren Amamiya (Joker)', 'Persona 5', 6500), ('Superman', 'DC Comics', 6474), ("Wolf O'Donnell", 'Star Fox', 6360),
         ('Ganondorf', 'The Legend of Zelda', 6286),
         ('Luigi', 'Super Mario', 6177), ('Robin (DC)', 'DC Comics', 6158), ('Beerus', 'Dragon Ball', 6078), ('Boruto Uzumaki', 'Naruto / Boruto', 5944),
         ('Roronoa Zoro', 'One Piece', 5823), ('Son Gohan', 'Dragon Ball', 5762), ('Satoru Gojo', 'Jujutsu Kaisen', 5745),
         # relevé 361-390
         ('Falco Lombardi', 'Star Fox', 5534), ('Gintoki Sakata', 'Gintama', 5489), ('Ben Tennyson', 'Ben 10', 5465),
         ('Protagoniste de Summertime Saga', 'Summertime Saga', 5318), ('Scout', 'Team Fortress 2', 5311), ('Caelus (Pionnier)', 'Honkai: Star Rail', 5228),
         ('Vegeta', 'Dragon Ball', 5067), ('Naoto Hachiōji (Senpai)', 'Arrête de me chauffer, Nagatoro', 5025)]
N = {'Sonic the Hedgehog': 'Sonic', 'Resident Evil 4': 'Resident Evil', 'Resident Evil Village': 'Resident Evil',
     'Marvel (Les 4 Fantastiques)': 'Marvel', 'Naruto / Boruto': 'Naruto', 'Konosuba': 'KonoSuba', 'One-Punch Man': 'One Punch Man',
     'Neon Genesis Evangelion': 'Evangelion', 'League of Legends / Arcane': 'League of Legends', 'Fate/Grand Order': 'Fate',
     "Avatar, le dernier maître de l'air": "Avatar (Le Dernier Maître de l'air + La Légende de Korra)",
     'La Légende de Korra': "Avatar (Le Dernier Maître de l'air + La Légende de Korra)"}
P = []
for x in fem: P.append(dict(nom=x['personnage'], f=N.get(x['univers'], x['univers']), s='F', pub=int(x['publications'])))
for o in mas: P.append(dict(nom=o['n'], f=N.get(o['u'], o['u']), s='M', pub=int(o['r'])))
for n, u, c in M_331: P.append(dict(nom=n, f=N.get(u, u), s='M', pub=c))
for n, u, t, c in AUTRES: P.append(dict(nom=n, f=u, s='?', pub=c))
G = collections.defaultdict(list)
for p in P: G[p['f']].append(p)
tot = sum(p['pub'] for p in P)
fmt = lambda n: f"{n:,}".replace(',', ' ')
rows = []
for f, L in G.items():
    L.sort(key=lambda p: -p['pub']); s = sum(p['pub'] for p in L); c = collections.Counter(p['s'] for p in L)
    rows.append(dict(franchise=f, personnages=len(L), feminins=c['F'], masculins=c['M'], genre_autre=c['?'], publications=s,
                     part=round(100*s/tot, 1), personnages_liste=', '.join(f"{p['nom']}{' ♂' if p['s']=='M' else (' (genre non défini)' if p['s']=='?' else '')} ({fmt(p['pub'])})" for p in L)))
rows.sort(key=lambda o: -o['publications'])
for i, o in enumerate(rows, 1): o['rang_publications'] = i
rows.sort(key=lambda o: (-o['personnages'], -o['publications']))
for i, o in enumerate(rows, 1): o['rang_personnages'] = i
cols = ['rang_personnages', 'rang_publications', 'franchise', 'personnages', 'feminins', 'masculins', 'genre_autre', 'publications', 'part', 'personnages_liste']
with open(B+'franchises/classement_franchises_tous_personnages_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as fo:
    w = csv.DictWriter(fo, cols); w.writeheader()
    for o in rows: w.writerow({**o, 'part': str(o['part']).replace('.', ',')})
old = {r['franchise']: r for r in csv.DictReader(open(B+'franchises/classement_franchises_388_2026-10-25.csv', encoding='utf-8-sig'))}
L = ["# Franchises les plus représentées sur rule34.xxx — tous personnages (25 octobre 2026)", "",
     f"*Base : les {len(P)} personnages relevés dans les pages 1 à 390 de la liste des tags (au moins ≈ 5 000 publications) : 388 féminins (sélection auditée), 65 masculins (46 de l'application de tri, dont 23 audités pour les doublons ; 19 des pages 331-390 comptés avec leur tag seul : Ren Amamiya, Superman, Wolf O'Donnell, Ganondorf, Luigi, Robin (DC), Beerus, Boruto, Zoro, Gohan, Gojo, Falco, Gintoki, Ben Tennyson, protagoniste de Summertime Saga, Scout, Caelus, Vegeta, Naoto Hachiōji) et 6 au genre non défini ou au choix (Kris, Frisk, MalO, Sensei de Blue Archive, Robin de Fire Emblem, Villageois·e d'Animal Crossing). Byleth, le Commandant Shepard, Kindred, Chara, Corrin, Ranma et V (Cyberpunk 2077) ne sont pas ajoutés une 2e fois (déjà comptés par leur version féminine). Espèces (Gardevoir, Lucario…), catégories et doublons exclus.*", "",
     f"**{len(rows)} franchises**, dont {sum(1 for o in rows if o['personnages']==1)} avec un seul personnage. ♂ = masculin.", "",
     "**Limites :** (1) les masculins des pages 1 à 107 ont été notés lors d'un premier relevé moins détaillé ; (2) une image avec deux personnages de la même franchise compte deux fois dans le cumul ; (3) MalO est compté avec un seul de ses 4 tags.", "",
     "## 1. Par nombre de personnages", "",
     "| # | Franchise | Personnages | ♀ | ♂ | Autre | Publications cumulées | Rang filles seules | Personnages (publications) |", "|---|---|---|---|---|---|---|---|---|"]
for o in rows:
    if o['personnages'] < 3: continue
    L.append(f"| {o['rang_personnages']} | {o['franchise']} | {o['personnages']} | {o['feminins']} | {o['masculins']} | {o['genre_autre']} | {fmt(o['publications'])} | {old[o['franchise']]['rang_personnages'] if o['franchise'] in old else '—'} | {o['personnages_liste']} |")
L += ["", "*Les franchises à 1 ou 2 personnages figurent dans le CSV.*", "", "## 2. Par publications cumulées (top 30)", "",
      "| # | Franchise | Publications cumulées | Part | Personnages | dont ♂ |", "|---|---|---|---|---|---|"]
for o in sorted(rows, key=lambda o: o['rang_publications'])[:30]:
    L.append(f"| {o['rang_publications']} | {o['franchise']} | {fmt(o['publications'])} | {str(o['part']).replace('.', ',')} % | {o['personnages']} | {o['masculins']} |")
open(B+'franchises/classement_franchises_tous_personnages_2026-10-25.md', 'w', encoding='utf-8').write('\n'.join(L)+'\n')
# détail par personnage pour l'application EdeniaList (page Franchises)
json.dump({f: [[p['nom'], p['pub'], p['s']] for p in sorted(Lp, key=lambda p: -p['pub'])] for f, Lp in G.items()},
          open(B+'franchises/tous_personnages_liste_2026-10-25.json', 'w', encoding='utf-8'), ensure_ascii=False)
for o in rows[:22]: print(o['rang_personnages'], o['franchise'], o['personnages'], o['feminins'], o['masculins'], o['genre_autre'], o['publications'], '| rang pub', o['rang_publications'], '| ancien', old.get(o['franchise'], {}).get('rang_personnages'))
print()
for o in sorted(rows, key=lambda o: o['rang_publications'])[:12]: print(o['rang_publications'], o['franchise'], o['publications'], o['part'], o['personnages'], o['masculins'])
print(len(rows), len(P), sum(1 for o in rows if o['personnages']==1))
for o in rows:
    if o['masculins'] and o['feminins']==0: print('sans F :', o['franchise'], o['personnages_liste'][:120])
