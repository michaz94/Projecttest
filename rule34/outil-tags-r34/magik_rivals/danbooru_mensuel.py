# Magik sur Danbooru, mois par mois (2021-01 à 2026-09) ; uploads du site repris du relevé Squirrel Girl (même jour) (24/10/2026)
import urllib.request, json, time, calendar
UA = {'User-Agent': 'EdeniaResearch/1.0'}
T = 'magik_(x-men)'
def cnt(q):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request('https://danbooru.donmai.us/counts/posts.json?tags=' + q, headers=UA), timeout=60).read())['counts']['posts']
        except Exception: time.sleep(3)
tot = {o['mois']: o['uploads_site'] for o in json.load(open('../squirrel_girl_rivals/danbooru_mensuel_2026-10-24.json'))}
out = []
for mois in tot:
    y, m = map(int, mois.split('-')); d = f"date:{y}-{m:02d}-01..{y}-{m:02d}-{calendar.monthrange(y, m)[1]}"
    out.append(dict(mois=mois, magik=cnt(T + '+' + d), dont_marvel_rivals=cnt(T + '+marvel_rivals+' + d), uploads_site=tot[mois])); time.sleep(0.3)
json.dump(out, open('danbooru_mensuel_2026-10-24.json', 'w'), indent=0)
ex = dict(total=cnt(T), avant_2021=cnt(T + '+date:2005-01-01..2020-12-31'), oct2026=cnt(T + '+date:2026-10-01..2026-10-23'), avec_marvel_rivals=cnt(T + '+marvel_rivals'))
json.dump(ex, open('danbooru_totaux_2026-10-24.json', 'w'))
print(ex)
for o in out: print(o['mois'], o['magik'], o['dont_marvel_rivals'], end=' | ')
print()
def per(a, b):
    L = [o for o in out if a <= o['mois'] <= b]; s = sum(o['magik'] for o in L); t = sum(o['uploads_site'] for o in L); return s, round(s / t * 1e4, 2)
for n, a, b in [('2021-01..2024-02', '2021-01', '2024-02'), ('12 mois avant annonce (2023-03..2024-02)', '2023-03', '2024-02'), ('annonce→sortie (2024-03..2024-11)', '2024-03', '2024-11'),
                ('12 mois avant sortie (2023-12..2024-11)', '2023-12', '2024-11'), ('12 mois après (2024-12..2025-11)', '2024-12', '2025-11'), ('12 derniers (2025-10..2026-09)', '2025-10', '2026-09'), ('2024-12..2026-09', '2024-12', '2026-09')]:
    print(n, per(a, b))
