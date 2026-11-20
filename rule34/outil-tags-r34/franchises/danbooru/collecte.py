# Collecte Danbooru (24/10/2026) pour les 600 personnages les plus fréquents :
# nombre de posts avec 1girl et avec 1boy (indice de genre), copyrights associés (related_tag), implications actives.
import json,time,urllib.request,urllib.parse,os
UA={'User-Agent':'EdeniaResearch/1.0'}
def get(u):
    for k in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40))
        except Exception as e: time.sleep(3+5*k)
    return None
top=json.load(open('top2000_personnages_danbooru_2026-10-24.json'))[:600]
OUT='collecte_2026-10-24.json'
res=json.load(open(OUT)) if os.path.exists(OUT) else {}
for i,t in enumerate(top):
    n=t['name']
    if n in res: continue
    q=urllib.parse.quote
    g=get(f"https://danbooru.donmai.us/counts/posts.json?tags={q(n)}+1girl"); time.sleep(0.25)
    b=get(f"https://danbooru.donmai.us/counts/posts.json?tags={q(n)}+1boy"); time.sleep(0.25)
    r=get(f"https://danbooru.donmai.us/related_tag.json?query={q(n)}&category=copyright&limit=6"); time.sleep(0.25)
    res[n]=dict(c=t['post_count'],girl=g and g['counts']['posts'],boy=b and b['counts']['posts'],
                cop=[(x['tag']['name'],round(x['frequency'],4)) for x in (r or {}).get('related_tags',[])])
    if i%20==0: json.dump(res,open(OUT,'w')); print(i,n,flush=True)
json.dump(res,open(OUT,'w'))
# implications (personnage enfant -> parent)
imp={}
names=[t['name'] for t in top]
for k in range(0,600,50):
    d=get("https://danbooru.donmai.us/tag_implications.json?limit=200&only=antecedent_name,consequent_name&search%5Bstatus%5D=active&search%5Bantecedent_name_comma%5D="+urllib.parse.quote(','.join(names[k:k+50])))
    for x in d or []: imp.setdefault(x['antecedent_name'],[]).append(x['consequent_name'])
    time.sleep(0.5)
json.dump(imp,open('implications_2026-10-24.json','w'))
print('FIN',len(res),len(imp))
