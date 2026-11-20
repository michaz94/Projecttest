# Données de la page « Franchises » d'EdeniaList (24/10/2026 ; mises à jour du 25/10 : pages 331-340, 341-360 puis 361-390).
# Sources : franchises/classement_franchises_tous_personnages_2026-10-25.csv (+ tous_personnages_liste json),
#           franchises/classement_franchises_388_2026-10-25.csv (rule34, filles seules),
#           franchises/classement_franchises_danbooru_388_2026-10-25.csv (Danbooru, filles seules).
import csv, json, re
B = '/home/user/outil_tags_r34/franchises/'
R = re.compile(r'(.*?) \((\d[\d  ]*)\)(?:, |$)')
lire = lambda f: list(csv.DictReader(open(B+f, encoding='utf-8-sig')))
num = lambda s: int(re.sub(r'\D', '', s))
def liste(txt, n, p):
    L = [[a, num(c), 'F'] for a, c in R.findall(txt)]
    assert len(L) == n and sum(x[1] for x in L) == p, (txt[:60], len(L), n)
    return L
tous_l = json.load(open(B+'tous_personnages_liste_2026-10-25.json', encoding='utf-8'))
T = [dict(f=r['franchise'], n=int(r['personnages']), nf=int(r['feminins']), nm=int(r['masculins']), na=int(r['genre_autre']),
          p=int(r['publications']), pt=float(r['part'].replace(',', '.')), rn=int(r['rang_personnages']), rp=int(r['rang_publications']),
          l=tous_l[r['franchise']]) for r in lire('classement_franchises_tous_personnages_2026-10-25.csv')]
F = [dict(f=r['franchise'], n=int(r['personnages']), nf=int(r['personnages']), nm=0, na=0, p=int(r['publications']),
          pt=float(r['part'].replace(',', '.')), rn=int(r['rang_personnages']), rp=int(r['rang_publications']),
          l=liste(r['personnages_liste'], int(r['personnages']), int(r['publications']))) for r in lire('classement_franchises_388_2026-10-25.csv')]
D = [dict(f=r['franchise'], n=int(r['personnages']), nf=int(r['personnages']), nm=0, na=0, p=int(r['publications']),
          pt=float(r['part'].replace(',', '.')), rn=int(r['rang_personnages']), rp=int(r['rang_publications']),
          l=liste(r['liste'], int(r['personnages']), int(r['publications'])), r34=int(r['r34_personnages'] or 0)) for r in lire('classement_franchises_danbooru_388_2026-10-25.csv')]
assert len(T) == 150 and sum(o["n"] for o in T) == 459 and sum(o["n"] for o in F) == 388 and sum(o["n"] for o in D) == 388
# correspondance des noms (même libellé dans les deux classements, sauf exceptions ci-dessous)
ALIAS = {'Hololive (VTubers)': 'Hololive', 'Final Fantasy': 'Final Fantasy VII', 'Xenoblade Chronicles': 'Xenoblade Chronicles 2', 'NieR': 'NieR: Automata'}
for o in D: o['k'] = ALIAS.get(o['f'], o['f'])
noms_f = {o['f'] for o in F}
for o in D:
    if o['r34'] and o['k'] not in noms_f: print('libellé Danbooru sans équivalent rule34 :', o['f'], o['r34'])
# nombre total de publications du tag de la franchise sur chaque site (franchises/tags_franchise/choisir_tags.py)
TG = {(r['site'], r['franchise']): r for r in csv.DictReader(open(B+'tags_franchise/tags_franchise_2026-10-24.csv', encoding='utf-8-sig'))}
MANQUE = set()
for site, LL in (('rule34', T), ('rule34', F), ('danbooru', D)):
    for o in LL:
        if (site, o['f']) not in TG: MANQUE.add((site, o['f'])); continue
        r = TG[(site, o['f'])]; o['tp'] = int(r['publications']); o['tt'] = r['tag']
        o['ta'] = ('union mesurée par recherche OR' if 'union' in r['methode'] else '') + (('autre tag : ' + r['autres_tags']) if r['autres_tags'] else '')
assert not MANQUE, sorted(MANQUE)
out = dict(T=T, F=F, D=D)
json.dump(out, open('/home/user/outil_tags_r34/app_tri/donnees_franchises_2026-10-24.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(T), len(F), len(D))
