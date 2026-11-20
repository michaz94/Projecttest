# Danbooru (skins Jinx/Psylocke impliquent déjà le tag de base ; spider-gwen n'implique pas gwen_stacy -> union) : images mises en ligne par mois, oct. 2025 → sept. 2026, pour 6 personnages (24/10/2026)
import urllib.request, json, time, calendar
UA = {'User-Agent': 'EdeniaResearch/1.0'}
T = {'Magik': 'magik_(x-men)', 'Jinx': 'jinx_(league)', 'Gwen Stacy / Spider-Gwen': '~gwen_stacy+~spider-gwen', 'Nami': 'nami_(one_piece)', 'Frieren': 'frieren', 'Psylocke': 'psylocke'}
def cnt(q):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request('https://danbooru.donmai.us/counts/posts.json?tags=' + q, headers=UA), timeout=60).read())['counts']['posts']
        except Exception: time.sleep(3)
tot = {o['mois']: o['uploads_site'] for o in json.load(open('../squirrel_girl_rivals/danbooru_mensuel_2026-10-24.json'))}
mois = [m for m in tot if '2025-10' <= m <= '2026-09']
out = {}
for n, t in T.items():
    out[n] = {}
    for m in mois:
        y, mm = map(int, m.split('-')); out[n][m] = cnt(f"{t}+date:{y}-{mm:02d}-01..{y}-{mm:02d}-{calendar.monthrange(y, mm)[1]}"); time.sleep(0.25)
    s = sum(out[n].values()); print(n, s, round(s / 12, 1), 'par mois', round(s / sum(tot[m] for m in mois) * 1e4, 2), 'pour 10k', list(out[n].values()))
json.dump(dict(tags=T, mensuel=out, uploads_site={m: tot[m] for m in mois}), open('danbooru_12mois_2026-10-24.json', 'w'), ensure_ascii=False, indent=0)
