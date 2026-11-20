# Tags Danbooru des 14 nouveaux personnages féminins (pages 331-340) et des 5 masculins des pages 311-330 ajoutés à l'application, 25/10/2026.
# Nom testé -> alias actif éventuel -> compteur. Ajoute dtags/res dans app_tri/danbooru_2026-10-24.json (idempotent) ; journal dans danbooru_nouveaux.json.
import urllib.request, urllib.parse, json, time
UA={'User-Agent':'EdeniaResearch/1.0'}
def get(u):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception: time.sleep(3)
CAND={'ayane_(doa)':['ayane_(doa)'],'ashe_(overwatch)':['ashe_(overwatch)'],'tristana':['tristana_(league)','tristana_(league_of_legends)','tristana'],
'marinette_dupain-cheng':['marinette_dupain-cheng','ladybug_(character)'],'amity_blight':['amity_blight'],'anna_(frozen)':['anna_(frozen)'],'lois_griffin':['lois_griffin'],
'bridget':['bridget_(guilty_gear)'],'hyuuga_hanabi':['hyuuga_hanabi'],'honoka_(doa)':['honoka_(doa)'],'sakura_futaba':['sakura_futaba'],
'ragatha_(the_amazing_digital_circus)':['ragatha_(the_amazing_digital_circus)','ragatha_(tadc)','ragatha'],'queen_marika_the_eternal':['queen_marika_the_eternal','marika_(elden_ring)'],
'hoshimi_miyabi':['hoshimi_miyabi'],
# masculins des pages 311-330
'dick_grayson':['dick_grayson'],'jax_(the_amazing_digital_circus)':['jax_(the_amazing_digital_circus)','jax_(tadc)'],'shining_armor_(mlp)':['shining_armor','shining_armor_(mlp)'],
'ichigo_kurosaki':['kurosaki_ichigo'],'ash_ketchum':['satoshi_(pokemon)','ash_ketchum']}
P='/home/user/outil_tags_r34/app_tri/danbooru_2026-10-24.json'
D=json.load(open(P)); log={}
for t,cs in CAND.items():
    best=None; essais=[]
    for c in cs:
        q=urllib.parse.quote(c)
        al=get(f'https://danbooru.donmai.us/tag_aliases.json?search%5Bantecedent_name%5D={q}&search%5Bstatus%5D=active') or []
        name=al[0]['consequent_name'] if al else c
        tg=get('https://danbooru.donmai.us/tags.json?search%5Bname%5D='+urllib.parse.quote(name)) or []
        essais.append([c,name,tg[0]['post_count'] if tg else None])
        if tg and tg[0]['post_count']>0:
            best=(name,tg[0]['post_count'],tg[0]['category']); break
        time.sleep(0.3)
    log[t]={'retenu':best,'essais':essais}; print(t,best)
    if best: D['dtags'][t]=best[0]; D['res'][best[0]]=[best[1],best[2]]
json.dump(D,open(P,'w'),ensure_ascii=False)
json.dump(log,open('danbooru_nouveaux.json','w'),ensure_ascii=False,indent=1)
