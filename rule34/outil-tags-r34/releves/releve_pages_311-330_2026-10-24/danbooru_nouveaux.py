# Tags Danbooru des 37 nouveaux personnages féminins (pages 311-330), 24/10/2026 : nom testé -> alias actif éventuel -> compteur.
# Ajoute dtags/res dans app_tri/danbooru_2026-10-24.json (idempotent).
import urllib.request, urllib.parse, json, time
UA={'User-Agent':'EdeniaResearch/1.0'}
def get(u):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception: time.sleep(3)
CAND={'kamisato_ayaka':['kamisato_ayaka'],'mileena':['mileena_(mortal_kombat)'],'caulifla':['caulifla'],'mori_calliope':['mori_calliope'],'houshou_marine':['houshou_marine'],
'rio_(blue_archive)':['rio_(blue_archive)','tsukatsuki_rio'],'diane_foxington':['diane_foxington'],'peridot_(steven_universe)':['peridot_(steven_universe)'],'temari':['temari_(naruto)','temari'],
'nejire_hado':['hadou_nejire'],'chica_(fnaf)':['chica_(fnaf)','chica'],'evelyn_chevalier':['evelyn_chevalier','evelyn_(zenless_zone_zero)'],'daphne_blake':['daphne_blake'],
'hermione_granger':['hermione_granger'],'princess_cadance_(mlp)':['princess_cadance'],'poppy':['poppy_(league)','poppy_(league_of_legends)'],'caitlyn_kiramman':['caitlyn_(league)','caitlyn_(league_of_legends)'],
"lana's_mother_(pokemon)":["lana's_mother_(pokemon)"],'ashley_graves':['ashley_(warioware)','ashley_graves'],'bea_(pokemon)':['bea_(pokemon)'],'sakuya_izayoi':['izayoi_sakuya'],
'uzaki_tsuki':['uzaki_tsuki'],'jenny_wakeman':['jenny_wakeman'],'yoko_littner':['yoko_littner'],'burnice_white':['burnice_white'],'callie_(splatoon)':['callie_(splatoon)'],
'bayonetta_(character)':['bayonetta','bayonetta_(character)'],'miss_fortune':['miss_fortune_(league)','miss_fortune_(league_of_legends)'],'sanae_kochiya':['kochiya_sanae'],
'judy_alvarez':['judy_alvarez'],'frankie_foster':['frankie_foster'],'lisa_(genshin_impact)':['lisa_(genshin_impact)'],'meow_skulls_(fortnite)':['meow_skulls_(fortnite)','meow_skulls'],
'evelynn':['evelynn_(league)','evelynn_(league_of_legends)'],'jean_gunnhildr':['jean_(genshin_impact)'],'nemona_(pokemon)':['nemona_(pokemon)'],'skyla_(pokemon)':['skyla_(pokemon)']}
P='/home/user/outil_tags_r34/app_tri/danbooru_2026-10-24.json'
D=json.load(open(P)); log={}
for t,cs in CAND.items():
    best=None
    for c in cs:
        q=urllib.parse.quote(c)
        al=get(f'https://danbooru.donmai.us/tag_aliases.json?search%5Bantecedent_name%5D={q}&search%5Bstatus%5D=active') or []
        name=al[0]['consequent_name'] if al else c
        tg=get('https://danbooru.donmai.us/tags.json?search%5Bname%5D='+urllib.parse.quote(name)) or []
        if tg and tg[0]['post_count']>0:
            best=(name,tg[0]['post_count'],tg[0]['category']); break
        time.sleep(0.3)
    log[t]=best; print(t,best)
    if best: D['dtags'][t]=best[0]; D['res'][best[0]]=[best[1],best[2]]
json.dump(D,open(P,'w'),ensure_ascii=False)
