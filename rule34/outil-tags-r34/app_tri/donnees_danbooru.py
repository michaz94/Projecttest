# Liste « Top Danbooru » de l'application (24/10/2026 ; étendue à 307, 336 puis 388 le 25/10) : les 388 personnages féminins les plus fréquents sur Danbooru,
# avec leur compteur rule34 (autocomplétion du 24/10 ; tag principal rule34 choisi parmi le nom Danbooru, le nom inversé
# et la variante de qualificatif de la même œuvre ; non audité, sauf pour les 50 déjà présents dans la sélection rule34).
import csv,json
B='/home/user/outil_tags_r34/'
sel=list(csv.DictReader(open(B+'franchises/danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv',encoding='utf-8-sig')))
app={o['td']:o for o in json.load(open(B+'app_tri/donnees_app_2026-10-24.json')) if o['s']=='F'}
A=json.load(open(B+'app_tri/r34_top_danbooru_autocomplete_2026-10-24.json'))
# tag principal rule34 quand il diffère du nom Danbooru (relevé 24/10, autocomplétion)
R34TAG={'kirisame_marisa':('marisa_kirisame',5270),'izayoi_sakuya':('sakuya_izayoi',6900),'komeiji_koishi':('koishi_komeiji',3039),
'kochiya_sanae':('sanae_kochiya',6786),'konpaku_youmu':('youmu_konpaku',3657),'yakumo_yukari':('yukari_yakumo',5138),'komeiji_satori':('satori_komeiji',2986),
'kaname_madoka':('madoka_kaname',4802),'sakura_kyoko':('sakura_kyouko',1479),'saigyouji_yuyuko':('yuyuko_saigyouji',3183),'inubashiri_momiji':('momiji_inubashiri',4238),'yakumo_ran':('ran_yakumo',2937),
'kaenbyou_rin':('rin_kaenbyou',2104),'moriya_suwako':('suwako_moriya',1523),'reiuji_utsuho':('utsuho_reiuji',2533),'kazami_yuuka':('yuuka_kazami',973),
'tatara_kogasa':('kogasa_tatara',1775),'kawashiro_nitori':('nitori_kawashiro',1917),'houraisan_kaguya':('kaguya_houraisan',1366),'hinanawi_tenshi':('tenshi_hinanawi',1978),
'kamishirasawa_keine':('keine_kamishirasawa',1489),'ibuki_suika':('suika_ibuki',1197),'inaba_tewi':('tewi_inaba',1297),'usami_renko':('renko_usami',380),
'houjuu_nue':('nue_houjuu',1512),'yagokoro_eirin':('eirin_yagokoro',1842),'yasaka_kanako':('kanako_yasaka',1316),'shiki_eiki':('eiki_shiki',1079),
'onozuka_komachi':('komachi_onozuka',1367),'imaizumi_kagerou':('kagerou_imaizumi',1977),'himekaidou_hatate':('hatate_himekaidou',1048),
'murasa_minamitsu':('minamitsu_murasa',532),'kaku_seiga':('seiga_kaku',848),
'kaga_(kancolle)':('kaga_(kantai_collection)',1839),'shimakaze_(kancolle)':('shimakaze_(kantai_collection)',3834),'hibiki_(kancolle)':('hibiki_(kantai_collection)',420),
'shigure_(kancolle)':('shigure_(kantai_collection)',682),'kongou_(kancolle)':('kongou_(kantai_collection)',1065),'inazuma_(kancolle)':('inazuma_(kantai_collection)',255),
'akagi_(kancolle)':('akagi_(kantai_collection)',451),'fubuki_(kancolle)':('fubuki_(kantai_collection)',537),'yuudachi_(kancolle)':('yuudachi_(kantai_collection)',472),
'tenryuu_(kancolle)':('tenryuu_(kantai_collection)',1247),'ikazuchi_(kancolle)':('ikazuchi_(kantai_collection)',216),'hamakaze_(kancolle)':('hamakaze_(kantai_collection)',2247),
'zuikaku_(kancolle)':('zuikaku_(kantai_collection)',584),'akatsuki_(kancolle)':('akatsuki_(kantai_collection)',159),'haruna_(kancolle)':('haruna_(kantai_collection)',744),
'kashima_(kancolle)':('kashima_(kantai_collection)',1952),'nagato_(kancolle)':('nagato_(kantai_collection)',807),'suzuya_(kancolle)':('suzuya_(kantai_collection)',1148),
'ryuujou_(kancolle)':('ryuujou_(kantai_collection)',246),'houshou_(kancolle)':('houshou_(kantai_collection)',456),
'abigail_williams_(fate)':('abigail_williams_(fate/grand_order)',724),'akiyama_mio':('mio_akiyama_(k-on!)',4623),'nakano_azusa':('azusa_nakano_(k-on!)',2588),
'hirasawa_yui':('yui_hirasawa_(k-on!)',2220),'kinomoto_sakura':('sakura_kinomoto',427),'takamachi_nanoha':('nanoha_takamachi',1590),
"jeanne_d'arc_alter_(fate)":("jeanne_d'arc_alter_(fate)",1076),"jeanne_d'arc_(fate)":("jeanne_d'arc_(fate)",4578),"ninomae_ina'nis":("ninomae_ina'nis",4241),
# extension au top 243 (24/10, autocomplétion)
'murakumo_(kancolle)':('murakumo_(kantai_collection)',488),'amatsukaze_(kancolle)':('amatsukaze_(kantai_collection)',554),'ibaraki_kasen':('kasen_ibaraki',1497),
'nagae_iku':('iku_nagae',1017),'tainaka_ritsu':('ritsu_tainaka_(k-on!)',1699),'tojo_nozomi':('toujou_nozomi',1854),
# extension au top 256 (24/10, autocomplétion)
'miyako_yoshika':('yoshika_miyako',390),'yamato_(kancolle)':('yamato_(kantai_collection)',781),'yukikaze_(kancolle)':('yukikaze_(kantai_collection)',152),'ushio_(kancolle)':('ushio_(kantai_collection)',525)}
NOTE_TAG={'miyako_yoshika':"autre tag rule34 : miyako_yoshika 211 (non additionné)",'shuten_douji_(fate)':"autre tag rule34 du même personnage : shuten_douji_(fate/grand_order) 456 (non additionné, recouvrement inconnu)",'tojo_nozomi':"autre tag rule34 : tojo_nozomi 78 (non additionné)",'ibaraki_kasen':"autre tag rule34 : ibaraki_kasen 285 (non additionné)",'nagae_iku':"autre tag rule34 : nagae_iku 191 (non additionné)","jeanne_d'arc_alter_(fate)":"autre tag rule34 du même personnage : jeanne_d'arc_(alter)_(fate) 562 (non additionné, recouvrement inconnu)"}
# extension au top 293 (relevé 311-330, 24/10, autocomplétion)
R34TAG.update({'atago_(kancolle)':('atago_(kantai_collection)',1679),'akebono_(kancolle)':('akebono_(kantai_collection)',200),
'shoukaku_(kancolle)':('shoukaku_(kantai_collection)',486),'kasodani_kyouko':('kyouko_kasodani',369),'kumoi_ichirin':('ichirin_kumoi',222),
'kurodani_yamame':('yamame_kurodani',559),'ishmael_(project_moon)':('ishmael_(limbus_company)',1652)})
NOTE_TAG.update({'matou_sakura':"autre tag rule34 : sakura_matou 351 (non additionné)",'meiko_(vocaloid)':"autre tag rule34 : meiko 484 (ambigu, non additionné)",
'ishmael_(project_moon)':"autre tag rule34 : ishmael_(project_moon) 100 (non additionné)",'atago_(kancolle)':"autre tag rule34 : atago_(kancolle) 13 (non additionné)"})
# extension au top 307 (relevé 331-340, 25/10, autocomplétion)
R34TAG.update({'anya_(spy_x_family)':('anya_forger',1243),"hk416_(girls'_frontline)":("hk416_(girls'_frontline)",1246),
'ooyodo_(kancolle)':('ooyodo_(kantai_collection)',392),'kijin_seija':('seija_kijin',546),'darjeeling_(girls_und_panzer)':('darjeeling',1204)})
NOTE_TAG.update({'anya_(spy_x_family)':"autre tag rule34 : anya_(spy_x_family) 33 (non additionné)",'kijin_seija':"autre tag rule34 : kijin_seija 174 (non additionné)",
'darjeeling_(girls_und_panzer)':"autre tag rule34 : darjeeling_(girls_und_panzer) 26 (non additionné)",'ooyodo_(kancolle)':"autre tag rule34 : ooyodo_(kancolle) 2 (non additionné)",
"hk416_(girls'_frontline)":"autre tag rule34 : hk416 17 (non additionné)"})
# extension au top 336 (relevé 341-360, 25/10, autocomplétion)
R34TAG.update({"kal'tsit_(arknights)":("kal'tsit_(arknights)",993),'yamada_ryo':('yamada_ryou',1324),'izumi_konata':('konata_izumi',1997),
'hiiragi_kagami':('kagami_hiiragi',2160),'kitakami_(kancolle)':('kitakami_(kantai_collection)',207),'aki_minoriko':('minoriko_aki',537),
'don_quixote_(project_moon)':('don_quixote_(limbus_company)',2363)})
NOTE_TAG.update({'yamada_ryo':"autre tag rule34 : yamada_ryo 10 (non additionné)",'izumi_konata':"autre tag rule34 : izumi_konata 134 (non additionné)",
'hiiragi_kagami':"autre tag rule34 : hiiragi_kagami 32 (non additionné)",'kitakami_(kancolle)':"autre tag rule34 : kitakami_(kancolle) 5 (non additionné)",
'aki_minoriko':"autre tag rule34 : aki_minoriko 139 (non additionné)",'don_quixote_(project_moon)':"autre tag rule34 : don_quixote_(project_moon) 135 (non additionné)"})
# extension au top 388 (relevé 361-390, 25/10, autocomplétion)
R34TAG.update({'asashio_(kancolle)':('asashio_(kantai_collection)',362),'prinz_eugen_(kancolle)':('prinz_eugen_(kantai_collection)',735),
'mutsu_(kancolle)':('mutsu_(kantai_collection)',696),'takao_(kancolle)':('takao_(kantai_collection)',1283),'ooi_(kancolle)':('ooi_(kantai_collection)',321),
'sendai_(kancolle)':('sendai_(kantai_collection)',288),'musashi_(kancolle)':('musashi_(kantai_collection)',880),'tatsuta_(kancolle)':('tatsuta_(kantai_collection)',460),
'female_admiral_(kancolle)':('female_admiral_(kantai_collection)',218),'kotobuki_tsumugi':('tsumugi_kotobuki_(k-on!)',1997),
'futatsuiwa_mamizou':('mamizou_futatsuiwa',522),'aki_shizuha':('shizuha_aki',295),'nikki_(nikki)':('nikki_(infinity_nikki)',147)})
NOTE_TAG.update({k:f"autre tag rule34 : {k} {v} (non additionné)" for k,v in [('asashio_(kancolle)',23),('prinz_eugen_(kancolle)',12),('mutsu_(kancolle)',14),
 ('takao_(kancolle)',49),('ooi_(kancolle)',18),('sendai_(kancolle)',6),('musashi_(kancolle)',27),('tatsuta_(kancolle)',3),('female_admiral_(kancolle)',1),
 ('kotobuki_tsumugi',3),('futatsuiwa_mamizou',100),('aki_shizuha',68),('nikki_(nikki)',16)]})
# pas de compteur rule34 demandé pour un personnage d'apparence enfantine (compteur affiché 0)
SANS_R34={'northern_ocean_princess'}
J,A_,AU='Jeux vidéo','Animanga','Autres'
MED={'Touhou Project':(J,"série de shoot'em up doujin (depuis 1996)"),'Kantai Collection':(J,'jeu par navigateur (2013)'),'Blue Archive':(J,''),
'Uma Musume':(J,"projet multimédia de Cygames annoncé en 2016 comme jeu mobile ; l'anime (2018) est sorti avant le jeu (2021)"),
'Hololive (VTubers)':(AU,'VTubeuses : avatars de streameuses réelles'),'Vocaloid':(AU,'logiciel de synthèse vocale'),'UTAU / Synthesizer V':(AU,'voix de synthèse'),
'VOICEROID':(AU,'logiciel de synthèse vocale'),'Kemono Friends':(J,"projet multimédia : jeu mobile (2015) et manga, rendu célèbre par l'anime de 2017"),
'BanG Dream!':(A_,'projet multimédia de Bushiroad (musique, anime, jeu)'),'Love Live!':(A_,'projet multimédia (magazine, musique, anime, jeux)'),
'Fate':(J,'Fate/stay night est un visual novel (2004) ; les autres viennent surtout du jeu mobile Fate/Grand Order'),
'Magical Girl Lyrical Nanoha':(A_,''),'Madoka Magica':(A_,'anime original (2011)'),'Girls Band Cry':(A_,'anime original (2024)'),'The Idolmaster':(J,'série de jeux de Namco (2005)'),'Alien Stage':(AU,'série animée web sud-coréenne (VIVINOS, 2022)'),
'Tsukihime':(J,'visual novel de Type-Moon (2000)'),'Project Moon (Limbus Company)':(J,'jeu de Project Moon (Limbus Company, 2023)'),
'Lucky Star':(A_,'manga (2004), connu surtout par l\'anime (2007)'),'Omori':(J,'jeu vidéo indépendant (2020)'),'Monogatari':(A_,"romans (light novels) de Nisio Isin (2006), connus surtout par l'anime (2009)"),"Girls' Frontline":(J,'jeu mobile (2016)')}
# relevé 361-390 (top 388)
MED.update({'Gloutons et Dragons (Dungeon Meshi)':(A_,''),'Code Geass':(A_,'anime original (2006)'),'Sword Art Online':(A_,"light novel (2009), connu surtout par l'anime (2012)"),
 'Nijisanji (VTubers)':(AU,'VTubeuses : avatars de streameuses réelles'),'Nikki (Infinity Nikki)':(J,'série de jeux mobiles de Papergames (Infinity Nikki, 2024)'),
 'Wuthering Waves':(J,''),'Fatal Fury / King of Fighters':(J,'')})
for f in ['Genshin Impact','Honkai: Star Rail','Honkai Impact 3rd','Zenless Zone Zero','Arknights','Pokémon','Final Fantasy','The Legend of Zelda','Super Mario',
          'Street Fighter','Metroid','NieR','Xenoblade Chronicles','Danganronpa']: MED.setdefault(f,(J,''))
for f in ['A Certain Magical Index / Railgun','Bocchi the Rock!','Card Captor Sakura','Chainsaw Man','Cho Kaguya-hime!','Evangelion','Frieren','Girls und Panzer',
          'Gochūmon wa Usagi Desu ka?','Gundam','K-On!','Kill la Kill','KonoSuba','La Mélancolie de Haruhi Suzumiya','Lycoris Recoil','One Piece','Re:Zero','Spy×Family']: MED.setdefault(f,(A_,''))
out=[]
for x in sel:
    t=x['tag']; f=x['franchise']; d=int(x['publications'])
    if t in app:   # déjà dans la sélection rule34 : mêmes données (auditées)
        o=dict(app[t]); o['u']=f; o['d']=d; o['rd']=int(x['rang_388']); out.append(o); continue
    m,note=MED[f]
    if t in SANS_R34:
        out.append(dict(n=x['personnage'],u=f,s='F',m=m,mo=note,t=t,r=0,b=0,g=0,q="compteur rule34 non relevé (personnage d'apparence enfantine)",a=0,td=t,d=d,rd=int(x['rang_388']))); continue
    if t in R34TAG: rt,c=R34TAG[t]
    else: rt,c=t,A[t]['exact']
    assert c is not None,t
    q='tag rule34 = nom Danbooru' if rt==t else f'tag rule34 différent du nom Danbooru ({t})'
    if t in NOTE_TAG: q+=' ; '+NOTE_TAG[t]
    out.append(dict(n=x['personnage'],u=f,s='F',m=m,mo=note,t=rt,r=c,b=c,g=0,q=q,a=0,td=t,d=d,rd=int(x['rang_388'])))
assert len(out)==388
json.dump(out,open(B+'app_tri/donnees_app_top_danbooru_2026-10-24.json','w'),ensure_ascii=False)
import collections; print(collections.Counter(o['m'] for o in out)); print(sum(1 for o in out if o['a']), sum(o['r'] for o in out), sum(o['d'] for o in out))
for o in sorted(out,key=lambda o:o['r'])[:8]: print(o['n'],o['t'],o['r'],o['d'])
