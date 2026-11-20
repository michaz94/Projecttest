# Squirrel Girl sur Danbooru, mois par mois (2021-01 à 2026-09) + total des uploads du site pour normaliser (24/10/2026)
import urllib.request, json, time, calendar
UA = {'User-Agent': 'EdeniaResearch/1.0'}
def cnt(q):
    for k in range(3):
        try:
            r = json.loads(urllib.request.urlopen(urllib.request.Request('https://danbooru.donmai.us/counts/posts.json?tags=' + q, headers=UA), timeout=60).read())
            return r['counts']['posts']
        except Exception as e:
            time.sleep(3)
    return None
out = []
for y in range(2021, 2027):
    for m in range(1, 13):
        if (y, m) > (2026, 9): break
        d = f"date:{y}-{m:02d}-01..{y}-{m:02d}-{calendar.monthrange(y, m)[1]}"
        sg = cnt('squirrel_girl_(marvel)+' + d); tot = cnt(d); mr = cnt('squirrel_girl_(marvel)+marvel_rivals+' + d)
        out.append(dict(mois=f"{y}-{m:02d}", squirrel_girl=sg, dont_marvel_rivals=mr, uploads_site=tot)); print(out[-1]); time.sleep(0.3)
json.dump(out, open('danbooru_mensuel_2026-10-24.json', 'w'), indent=0)
