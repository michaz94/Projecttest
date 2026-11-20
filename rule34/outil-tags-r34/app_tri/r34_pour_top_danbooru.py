# Compteurs rule34 (autocomplétion, 24/10/2026) pour les personnages du top 293 Danbooru (incrémental : les tags déjà relevés sont gardés) absents de la sélection rule34.
import csv,json,time,urllib.request,urllib.parse,re,html
B='/home/user/outil_tags_r34/'
D=json.load(open(B+'app_tri/danbooru_2026-10-24.json'))['dtags']
inv={v:k for k,v in D.items()}
sel=list(csv.DictReader(open(B+'franchises/danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv',encoding='utf-8-sig')))
def ac(q):
    u='https://api.rule34.xxx/autocomplete.php?q='+urllib.parse.quote(q)
    for k in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
        except Exception: time.sleep(3)
    return []
import os
# 25/10 (extensions à 336 puis 388) : pas de compteur rule34 demandé pour un personnage d'apparence enfantine
SANS_R34={'northern_ocean_princess'}
P=B+'app_tri/r34_top_danbooru_autocomplete_2026-10-24.json'
out=json.load(open(P)) if os.path.exists(P) else {}
for r in sel:
    t=r['tag']
    if t in inv or t in out or t in SANS_R34: continue
    res=ac(t); time.sleep(0.35)
    m={x['value']:int(re.search(r'\((\d+)\)$',x['label']).group(1)) for x in res}
    out[t]={'exact':m.get(t),'propositions':[html.unescape(x['label']) for x in res[:6]]}
json.dump(out,open(B+'app_tri/r34_top_danbooru_autocomplete_2026-10-24.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(1 for v in out.values() if v['exact'] is None))
for t,v in out.items():
    if v['exact'] is None: print(t,v['propositions'])
