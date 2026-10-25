"""Publications Danbooru par année d'upload (metatag date:AAAA-01-01..AAAA-12-31), pour tester la thèse « production par unité de temps » (24 oct. 2026)."""
import json,subprocess,time,urllib.parse,concurrent.futures as cf
P={"Marin Kitagawa":"kitagawa_marin","Yor Forger":"yor_briar","2B":"2b_(nier:automata)","Makima":"makima_(chainsaw_man)","Frieren":"frieren",
 "Fern":"fern_(sousou_no_frieren)","Power":"power_(chainsaw_man)","Ai Hoshino":"hoshino_ai_(oshi_no_ko)","Raiden Shogun":"raiden_shogun","Zero Two":"zero_two_(darling_in_the_franxx)",
 "Rem":"rem_(re:zero)","Mirko":"mirko","Ochaco":"uraraka_ochako","Himiko Toga":"toga_himiko","Momo Yaoyorozu":"yaoyorozu_momo","Albedo":"albedo_(overlord)",
 "Nami":"nami_(one_piece)","Nico Robin":"nico_robin","Boa Hancock":"boa_hancock","Tsunade":"tsunade_(naruto)","Hinata":"hyuuga_hinata","Bulma":"bulma","C-18":"android_18",
 "Mikasa":"mikasa_ackerman","Asuka":"souryuu_asuka_langley","Rei":"ayanami_rei","Rias Gremory":"rias_gremory","Yoruichi":"shihouin_yoruichi","Orihime":"inoue_orihime",
 "Tifa":"tifa_lockhart","Samus":"samus_aran","Chun-Li":"chun-li","Peach":"princess_peach","Zelda":"princess_zelda","Lara Croft":"lara_croft","Aerith":"aerith_gainsborough",
 "Hatsune Miku":"hatsune_miku","Yor (variante)":"yor_forger"}
YEARS=list(range(2006,2027))
def cnt(tags):
    u="https://danbooru.donmai.us/counts/posts.json?tags="+urllib.parse.quote(tags)
    for a in range(4):
        r=subprocess.run(['curl','-s','-A','EdeniaResearch/1.0',u],capture_output=True,text=True).stdout
        try: return json.loads(r)['counts']['posts']
        except Exception: time.sleep(2)
    return None
jobs=[(n,t,y) for n,t in P.items() for y in YEARS]+[("_TOTAL","",y) for y in YEARS]
out={}
with cf.ThreadPoolExecutor(8) as ex:
    futs={ex.submit(cnt,(f"{t} " if t else "")+f"date:{y}-01-01..{y}-12-31"):(n,t,y) for n,t,y in jobs}
    for f in cf.as_completed(futs):
        n,t,y=futs[f]; out.setdefault(n,{"tag":t,"annees":{}})["annees"][y]=f.result()
json.dump(out,open('/home/user/outil_tags_r34/production_temps/danbooru_annuel_2026-10-24.json','w'),ensure_ascii=False,indent=0)
print('ok',sum(1 for n in out for y in out[n]['annees'] if out[n]['annees'][y] is None),'échecs')
