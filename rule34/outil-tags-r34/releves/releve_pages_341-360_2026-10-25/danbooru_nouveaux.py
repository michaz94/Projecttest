# Tags Danbooru des 29 nouveaux personnages féminins (pages 341-360), 25/10/2026.
# Nom testé -> alias actif éventuel -> compteur. Ajoute dtags/res dans app_tri/danbooru_2026-10-24.json (idempotent) ; journal dans danbooru_nouveaux.json.
import urllib.request, urllib.parse, json, time
UA={'User-Agent':'EdeniaResearch/1.0'}
def get(u):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception: time.sleep(3)
CAND={'vi':['vi_(league_of_legends)'],'isabella_valentine':['isabella_valentine','ivy_valentine'],'gawr_gura':['gawr_gura'],
'misato_katsuragi':['katsuragi_misato'],'trixie_(mlp)':['trixie_lulamoon','trixie_(mlp)'],'tenten':['tenten_(naruto)','tenten'],
'felicia_(darkstalkers)':['felicia_(vampire)','felicia_(darkstalkers)'],'kit_(gameoverse)':['kit_(gameoverse)','kit_bodega'],
'hestia_(danmachi)':['hestia_(danmachi)'],'max_caulfield':['max_caulfield'],'sayori_(doki_doki_literature_club)':['sayori_(doki_doki_literature_club)'],
'vaggie_(hazbin_hotel)':['vaggie_(hazbin_hotel)','vaggie'],'mitsuki_bakugou':['bakugou_mitsuki'],'kallen_stadtfeld':['kouzuki_kallen'],
'melony_(pokemon)':['melony_(pokemon)'],'lapis_lazuli_(steven_universe)':['lapis_lazuli_(steven_universe)'],'female_chara':['chara_(undertale)'],
'raven_team_leader':['raven_team_leader'],'lucyna_kushinada':['lucy_(cyberpunk)','lucyna_kushinada'],'katarina_du_couteau':['katarina_(league_of_legends)'],
'komi_shuuko':['komi_shuuko'],'firefly_(honkai:_star_rail)':['firefly_(honkai:_star_rail)'],'taihou_(azur_lane)':['taihou_(azur_lane)'],
'edelgard_von_hresvelg':['edelgard_von_hresvelg'],'mavuika_(genshin_impact)':['mavuika_(genshin_impact)'],'patchouli_knowledge':['patchouli_knowledge'],
'ghislaine_dedoldia':['ghislaine_dedoldia'],'star_butterfly':['star_butterfly'],'tharja_(fire_emblem)':['tharja_(fire_emblem)']}
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
    log[t]={'retenu':best,'essais':essais}; print(t,best,essais if not best or best[0]!=cs[0] else '')
    if best: D['dtags'][t]=best[0]; D['res'][best[0]]=[best[1],best[2]]
json.dump(D,open(P,'w'),ensure_ascii=False)
json.dump(log,open('danbooru_nouveaux.json','w'),ensure_ascii=False,indent=1)
