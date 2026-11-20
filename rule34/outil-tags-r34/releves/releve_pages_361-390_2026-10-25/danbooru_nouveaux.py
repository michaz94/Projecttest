# Tags Danbooru des 52 nouveaux personnages féminins (pages 361-390), 25/10/2026.
# Nom testé -> alias actif éventuel -> compteur. Ajoute dtags/res dans app_tri/danbooru_2026-10-24.json (idempotent) ; journal dans danbooru_nouveaux.json.
import urllib.request, urllib.parse, json, time
UA={'User-Agent':'EdeniaResearch/1.0'}
def get(u):
    for k in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception: time.sleep(3)
CAND={'muffet':['muffet'],'ty_lee':['ty_lee'],'magik_(illyana_rasputin)':['magik_(marvel)','illyana_rasputin'],'surge_the_tenrec':['surge_the_tenrec'],
'fujiwara_chika':['fujiwara_chika'],'juno_(overwatch)':['juno_(overwatch)'],'sakura_kasugano':['kasugano_sakura'],'samui':['samui_(naruto)','samui'],
'jaina_proudmoore':['jaina_proudmoore'],'nakano_miku':['nakano_miku'],'luna_snow':['luna_snow'],'corrin_(fire_emblem)_(female)':['corrin_(female)_(fire_emblem)','corrin_(fire_emblem)_(female)'],
"april_o'neil":["april_o'neil"],'gloria_(pokemon)':['gloria_(pokemon)'],"kai'sa":["kai'sa"],'rapunzel':['rapunzel_(disney)','rapunzel'],
"dexter's_mom":["dexter's_mom"],'esdeath_(akame_ga_kill!)':['esdeath'],'tohru_(dragon_maid)':['tohru_(maidragon)','tohru_(dragon_maid)'],'riesz':['riesz'],
'annie_leonhardt':['annie_leonhart','annie_leonhardt'],'poison_(final_fight)':['poison_(final_fight)'],'rey':['rey_(star_wars)'],
'pearl_(steven_universe)':['pearl_(steven_universe)'],'tawna_bandicoot':['tawna_bandicoot'],'shinomiya_kaguya':['shinomiya_kaguya'],
'jolyne_kujo':['kujo_jolyne','jolyne_kujo'],'gwen_(league_of_legends)':['gwen_(league_of_legends)'],'marisa_kirisame':['kirisame_marisa'],
'unohana_retsu':['unohana_retsu'],'undyne':['undyne'],'irelia_xan':['irelia_(league_of_legends)','irelia'],'ranma-chan':['ranma-chan'],
'reisen_udongein_inaba':['reisen_udongein_inaba'],'amber_(genshin_impact)':['amber_(genshin_impact)'],'master_tigress':['tigress_(kung_fu_panda)','master_tigress'],
'pyrrha_nikos':['pyrrha_nikos'],'xayah':['xayah'],'alisa_mikhailovna_kujou':['alisa_mikhailovna_kujou'],'vex_(league_of_legends)':['vex_(league_of_legends)'],
'kirigaya_suguha':['kirigaya_suguha'],'yukari_yakumo':['yakumo_yukari'],'astrid_hofferson':['astrid_hofferson'],'purah':['purah'],
'ariel':['ariel_(disney)','ariel_(the_little_mermaid)'],'ayase_seiko':['ayase_seiko'],'valerie_(cyberpunk_2077)':['v_(cyberpunk)','valerie_(cyberpunk_2077)'],
'hilda_valentine_goneril':['hilda_valentine_goneril'],'fionna_the_human_girl':['fionna_campbell','fionna_the_human_girl'],'wendy_corduroy':['wendy_corduroy'],
'haru_okumura':['okumura_haru'],'haydee':['haydee_(game)','haydee']}
assert len(CAND)==52
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
# Corrections manuelles (recherche name_matches, 25/10/2026) :
#  magik -> magik_(x-men) 1 113 ; haydee -> haydee_(haydee) 49 (haydee_(game) = Copyright) ;
#  valerie_(cyberpunk_2077) : seul tag Danbooru = v_(cyberpunk) (344), commun aux deux versions de V -> non attribué ;
#  dexter's_mom : aucun tag Danbooru (0).
D=json.load(open(P))
for t,(n,c,k) in {'magik_(illyana_rasputin)':('magik_(x-men)',1113,4),'haydee':('haydee_(haydee)',49,4)}.items():
    D['dtags'][t]=n; D['res'][n]=[c,k]
D['dtags'].pop('valerie_(cyberpunk_2077)',None)
json.dump(D,open(P,'w'),ensure_ascii=False)
log['magik_(illyana_rasputin)']['retenu']=['magik_(x-men)',1113,4]; log['haydee']['retenu']=['haydee_(haydee)',49,4]; log['valerie_(cyberpunk_2077)']['retenu']=None
json.dump(log,open('danbooru_nouveaux.json','w'),ensure_ascii=False,indent=1)
