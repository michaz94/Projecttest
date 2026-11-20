# Classement des franchises sur Danbooru (24/10/2026 ; étendu à 307, 336 puis 388 le 25/10 avec les données du 24/10) : sélection propre à Danbooru = les 388 personnages féminins
# les plus fréquents (même effectif que la sélection rule34), à partir du top 600 des tags de personnage.
import json,csv,collections,re
B='/home/user/outil_tags_r34/franchises/'
top=json.load(open(B+'danbooru/top2000_personnages_danbooru_2026-10-24.json'))[:600]
d=json.load(open(B+'danbooru/collecte_2026-10-24.json'))
imp=json.load(open(B+'danbooru/implications_2026-10-24.json'))
N=388
# --- exclusions (motif) ---
AVATAR={'sensei_(blue_archive)','doodle_sensei_(blue_archive)','admiral_(kancolle)','warrior_of_light_(ff14)','trailblazer_(honkai:_star_rail)',
 'inkling_player_character','octoling_player_character','trainer_(umamusume)','producer_(idolmaster)','doctor_(arknights)','rover_(wuthering_waves)',
 'commander_(azur_lane)','kris_(deltarune)','paimon_(genshin_impact)'}
ESPECE={'gardevoir','pikachu','eevee','rotom','kyubey','manjuu_(azur_lane)','boo_tao_(genshin_impact)','kirby'}
OBJET={'shanghai_doll','rensouhou-chan','senketsu'}
AMBIGU={'saotome_ranma','oyama_mahiro'}   # garçon transformé en fille
FEM_FORCE={'anya_(spy_x_family)'}        # fille ; ratio 1girl/1boy faible car souvent avec Loid ou Damian
MASC_FORCE={'kel_(omori)'}
SEUIL=0.55
def genre(n,x):
    if n in AVATAR: return 'genre au choix / non défini'
    if n in ESPECE: return 'espèce / créature'
    if n in OBJET: return 'objet animé'
    if n in AMBIGU: return 'ambigu (garçon devenu fille)'
    if n in FEM_FORCE: return 'féminin'
    if n in MASC_FORCE: return 'masculin'
    g,b=x['girl'],x['boy']; return 'féminin' if g/(g+b)>=SEUIL else 'masculin'
# versions : un tag qui implique un autre personnage est déjà compté dans le parent (Danbooru ajoute le parent automatiquement)
GARDE_ENFANT={'stelle_(honkai:_star_rail)','female_rover_(wuthering_waves)'}  # parent = avatar sans genre
FR={'touhou':'Touhou Project','kantai_collection':'Kantai Collection','blue_archive':'Blue Archive','hololive':'Hololive (VTubers)',
 'fate_(series)':'Fate','genshin_impact':'Genshin Impact','umamusume':'Uma Musume','love_live!':'Love Live!','idolmaster':'The Idolmaster',
 'mahou_shoujo_madoka_magica':'Madoka Magica','vocaloid':'Vocaloid','pokemon':'Pokémon','honkai:_star_rail':'Honkai: Star Rail',
 'honkai_impact_3rd':'Honkai Impact 3rd','arknights':'Arknights','bang_dream!':'BanG Dream!','zenless_zone_zero':'Zenless Zone Zero',
 'final_fantasy':'Final Fantasy','the_legend_of_zelda':'The Legend of Zelda','mario_(series)':'Super Mario','utau':'UTAU / Synthesizer V',
 'bocchi_the_rock!':'Bocchi the Rock!','k-on!':'K-On!','girls_und_panzer':'Girls und Panzer','neon_genesis_evangelion':'Evangelion',
 'chainsaw_man':'Chainsaw Man','sousou_no_frieren':'Frieren','one_piece':'One Piece','spy_x_family':'Spy×Family','street_fighter':'Street Fighter',
 'xenoblade_chronicles_(series)':'Xenoblade Chronicles','re:zero_kara_hajimeru_isekai_seikatsu':'Re:Zero','kono_subarashii_sekai_ni_shukufuku_wo!':'KonoSuba',
 'lyrical_nanoha':'Magical Girl Lyrical Nanoha','suzumiya_haruhi_no_yuuutsu':'La Mélancolie de Haruhi Suzumiya','danganronpa_(series)':'Danganronpa',
 'nier_(series)':'NieR','toaru_majutsu_no_index':'A Certain Magical Index / Railgun','cho_kaguya-hime!':'Cho Kaguya-hime!','cardcaptor_sakura':'Card Captor Sakura',
 'kill_la_kill':'Kill la Kill','lycoris_recoil':'Lycoris Recoil','kemono_friends':'Kemono Friends','gochuumon_wa_usagi_desu_ka?':'Gochūmon wa Usagi Desu ka?',
 'metroid':'Metroid','gundam':'Gundam','girls_band_cry':'Girls Band Cry','alien_stage':'Alien Stage','fire_emblem':'Fire Emblem','omori':'Omori',
 'darkstalkers':'Darkstalkers','tsukihime':'Tsukihime','bishoujo_senshi_sailor_moon':'Sailor Moon','project_moon':'Project Moon (Limbus Company)',
 'monogatari_(series)':'Monogatari','girls\'_frontline':"Girls' Frontline",'boku_no_hero_academia':'My Hero Academia','lucky_star':'Lucky Star',
 'sono_bisque_doll_wa_koi_wo_suru':'My Dress-Up Darling','azur_lane':'Azur Lane','sword_art_online':'Sword Art Online','fatal_fury':'Fatal Fury / King of Fighters',
 'wuthering_waves':'Wuthering Waves','dungeon_meshi':'Gloutons et Dragons (Dungeon Meshi)','ranma_1/2':'Ranma ½','naruto_(series)':'Naruto',
 'tengen_toppa_gurren_lagann':'Gurren Lagann','code_geass':'Code Geass','nikki_(series)':'Nikki (Infinity Nikki)','nijisanji':'Nijisanji (VTubers)',
 'overwatch':'Overwatch','voiceroid':'VOICEROID','rozen_maiden':'Rozen Maiden','one-punch_man':'One Punch Man','shingeki_no_kyojin':"L'Attaque des Titans",
 'watashi_ga_motenai_no_wa_dou_kangaetemo_omaera_ga_warui!':'WataMote','gridman_universe':'Gridman','mahou_shoujo_no_majo_saiban':'Mahō Shōjo no Majo Saiban',
 'go-toubun_no_hanayome':'The Quintessential Quintuplets','league_of_legends':'League of Legends','panty_&_stocking_with_garterbelt':'Panty & Stocking with Garterbelt',
 'persona':'Persona','resident_evil':'Resident Evil','jojo_no_kimyou_na_bouken':'JoJo','dragon_ball':'Dragon Ball','jujutsu_kaisen':'Jujutsu Kaisen'}
def franchise(x):
    c=[t for t,f in x['cop']]
    if c[0]=='honkai_(series)':
        for t in c[1:]:
            if t in('honkai:_star_rail','honkai_impact_3rd'): return t
    return c[0]
NOMS={"hk416_(girls'_frontline)":'HK416','fujimaru_ritsuka_(female)':'Fujimaru Ritsuka (version féminine)','2b_(nier:automata)':'2B',"jeanne_d'arc_alter_(fate)":"Jeanne d'Arc Alter","jeanne_d'arc_(fate)":"Jeanne d'Arc",'illyasviel_von_einzbern':'Illyasviel von Einzbern','tamamo_no_mae_(fate)':'Tamamo no Mae','mejiro_mcqueen_(umamusume)':'Mejiro McQueen','female_rover_(wuthering_waves)':'Rover (version féminine)','female_byleth_(fire_emblem)':'Byleth (version féminine)','c.c.':'C.C.','female_admiral_(kancolle)':'Amiral (version féminine)'}
def nom(n):
    if n in NOMS: return NOMS[n]
    s=re.sub(r'_\((?!1st)[^)]*\)$','',n); return ' '.join(w[:1].upper()+w[1:] for w in s.replace('_',' ').split())
rows=[]
for i,t in enumerate(top,1):
    n=t['name']; x=d[n]; g=genre(n,x)
    par=imp.get(n,[]); motif=''
    if par and n not in GARDE_ENFANT: motif='version (implique '+', '.join(par)+')'
    elif g!='féminin': motif=g
    f=franchise(x)
    rows.append(dict(rang_danbooru=i,tag=n,personnage=nom(n),franchise_tag=f,franchise=FR.get(f,f),publications=t['post_count'],
        posts_1girl=x['girl'],posts_1boy=x['boy'],part_1girl=round(x['girl']/(x['girl']+x['boy']),2),genre=g,retenu='' if motif else 'oui',motif=motif))
fem=[r for r in rows if r['retenu']=='oui'][:N]
assert len(fem)==N
seuil=fem[-1]['publications']
for r in rows:
    if r['retenu']=='oui' and r['publications']<seuil or (r['retenu']=='oui' and r not in fem): r['retenu']='non (hors des 388)'
cols=list(rows[0].keys())
with open(B+'danbooru/tri_top600_personnages_danbooru_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as fo:
    w=csv.DictWriter(fo,cols); w.writeheader(); w.writerows(rows)
for i,r in enumerate(fem,1): r['rang_388']=i
with open(B+'danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as fo:
    w=csv.DictWriter(fo,['rang_388']+cols); w.writeheader(); w.writerows(fem)
# --- franchises ---
G=collections.defaultdict(list)
for r in fem: G[r['franchise']].append(r)
tot=sum(r['publications'] for r in fem)
R34={r['franchise']:r for r in csv.DictReader(open(B+'classement_franchises_388_2026-10-25.csv',encoding='utf-8-sig'))}
ALIAS={'Hololive (VTubers)':'Hololive','Final Fantasy':'Final Fantasy VII','Xenoblade Chronicles':'Xenoblade Chronicles 2','NieR':'NieR: Automata','Fatal Fury / King of Fighters':'Fatal Fury / King of Fighters','UTAU / Synthesizer V':'UTAU / Synthesizer V'}
fr=[]
for f,L in G.items():
    s=sum(r['publications'] for r in L); k=R34.get(ALIAS.get(f,f))
    fr.append(dict(franchise=f,personnages=len(L),publications=s,part=round(100*s/tot,1),moyenne=round(s/len(L)),
        r34_personnages=k['personnages'] if k else 0,r34_rang=k['rang_personnages'] if k else '—',
        liste=', '.join(f"{r['personnage']} ({r['publications']:,})".replace(f"{r['publications']:,}",f"{r['publications']:,}".replace(',',' ')) for r in L)))
fr.sort(key=lambda o:-o['publications'])
for i,o in enumerate(fr,1): o['rang_publications']=i
fr.sort(key=lambda o:(-o['personnages'],-o['publications']))
for i,o in enumerate(fr,1): o['rang_personnages']=i
cols=['rang_personnages','rang_publications','franchise','personnages','publications','part','moyenne','r34_personnages','r34_rang','liste']
with open(B+'classement_franchises_danbooru_388_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as fo:
    w=csv.DictWriter(fo,cols); w.writeheader()
    for o in fr: w.writerow({**o,'part':str(o['part']).replace('.',',')})
json.dump(dict(seuil=seuil,tot=tot,nb=len(fr),solo=sum(1 for o in fr if o['personnages']==1),
   excl=collections.Counter(r['motif'].split(' (')[0] for r in rows if r['motif'] and r['rang_danbooru']<=fem[-1]['rang_danbooru'])),open('/tmp/stats.json','w'),ensure_ascii=False)
print(json.load(open('/tmp/stats.json')))
for o in fr[:35]: print(o['rang_personnages'],o['rang_publications'],o['franchise'],o['personnages'],o['publications'],o['part'],'| r34:',o['r34_personnages'],o['r34_rang'])
# --- Markdown ---
fmt=lambda n:f"{n:,}".replace(',',' ')
st=json.load(open('/tmp/stats.json'))
L=["# Franchises les plus représentées sur Danbooru (personnages féminins)","",
f"*Relevé du 24 octobre 2026 (API Danbooru). Base : sélection propre à Danbooru, c'est-à-dire les **388 personnages féminins les plus fréquents** (même effectif que la sélection rule34), soit tous les tags de personnage féminin à au moins **{fmt(seuil)} images**. Danbooru compte toutes les images, pas seulement les explicites.*","",
"**Méthode :**",
"- Top 600 des tags de personnage Danbooru (catégorie 4) triés par nombre d'images.",
f"- Genre : part des images du personnage taguées `1girl` parmi `1girl` + `1boy` (seuil 0,55), vérifiée à la main ; Anya (Spy×Family) est comptée fille malgré un ratio de 0,52 (souvent avec Loid ou Damian).",
"- Exclus : personnages masculins ; avatars du joueur au genre au choix (Sensei de Blue Archive, Amiral de KanColle, Dresseur d'Uma Musume, Producteur d'Idolmaster, Docteur d'Arknights, Rover, Trailblazer, Guerrier de la Lumière FF14, Inkling/Octoling joueur, Commandant d'Azur Lane) ; Kris (Deltarune) et Paimon (genre non précisé) ; espèces et créatures (Gardevoir, Pikachu, Évoli, Motisma, Kyubey, Manjuu, Kirby, Boo Tao) ; objets animés (poupée Shanghai, Rensouhou-chan, Senketsu).",
"- **Pas de doublons à additionner** : sur Danbooru, un tag de version (Saber, Madoka en magical girl, Shigure Kai Ni, costumes…) ajoute automatiquement le tag parent (implication), donc le parent compte déjà ces images. Les versions sont retirées pour ne pas compter deux fois. Exception : Stelle et Rover (féminin) sont gardées, car leur parent est un avatar sans genre.",
"- Franchise : tag Copyright le plus associé au personnage (`related_tag`). Danbooru regroupe les sous-séries sous un tag parent (Fate, The Idolmaster, Love Live!, BanG Dream!, Gundam, Final Fantasy) ; seul Honkai est séparé entre Star Rail et Impact 3rd, comme pour rule34.",
f"- **À trancher :** Mahiro Oyama (Onimai, garçon transformé en fille, 8 008 images) est classé ambigu et non compté ; s'il est compté fille, il entre à la place de {fem[-1]['personnage']} ({fem[-1]['franchise']}, {fmt(fem[-1]['publications'])}). Les VTubers Hololive/Nijisanji sont comptées : Danbooru les classe comme personnages.","",
f"**{st['nb']} franchises**, dont {st['solo']} avec un seul personnage. Fichiers de détail : `danbooru/selection_388_personnages_feminins_danbooru_2026-10-25.csv`, `danbooru/tri_top600_personnages_danbooru_2026-10-25.csv` (chaque exclusion avec son motif).","",
"## 1. Par nombre de personnages","","Départage à égalité : images cumulées. Colonne rule34 = nombre de personnages de la franchise dans la sélection rule34 des 388.","",
"| # | Franchise | Personnages | Images cumulées | Moyenne | rule34 | Personnages (images) |","|---|---|---|---|---|---|---|"]
for o in fr:
    if o['personnages']<2: continue
    L.append(f"| {o['rang_personnages']} | {o['franchise']} | {o['personnages']} | {fmt(o['publications'])} | {fmt(o['moyenne'])} | {o['r34_personnages']} | {o['liste']} |")
L+=["",f"*Franchises à un seul personnage : " + ', '.join(f"{o['franchise']} ({o['liste']})" for o in fr if o['personnages']==1)+".*","",
"## 2. Par images cumulées (top 25)","","| # | Franchise | Images cumulées | Part des 388 | Personnages |","|---|---|---|---|---|"]
for o in sorted(fr,key=lambda o:o['rang_publications'])[:25]:
    L.append(f"| {o['rang_publications']} | {o['franchise']} | {fmt(o['publications'])} | {str(o['part']).replace('.',',')} % | {o['personnages']} |")
open(B+'classement_franchises_danbooru_388_2026-10-25.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
# --- 3. Comparaison avec la sélection rule34 ---
Dm=json.load(open('/home/user/outil_tags_r34/app_tri/danbooru_2026-10-24.json'))['dtags']
r34t={Dm.get(x['tag']) for x in csv.DictReader(open('/home/user/outil_tags_r34/doublons/selection_388_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig'))}
com=[r for r in fem if r['tag'] in r34t]
dn={o['franchise'] for o in fr}|{'Final Fantasy VII','Xenoblade Chronicles 2','NieR: Automata'}
abs_=[(k,v) for k,v in R34.items() if k not in dn and int(v['personnages'])>=3]
abs_.sort(key=lambda kv:int(kv[1]['rang_personnages']))
L=["","## 3. Comparaison avec la sélection rule34","",
f"- **{len(com)} personnages sur 388** figurent dans les deux sélections : " + ', '.join(r['personnage'] for r in com)+".",
"- Franchises à au moins 3 personnages dans la sélection rule34 mais **absentes** des 388 de Danbooru : " + ', '.join(f"{k} ({v['personnages']})" for k,v in abs_)+". Leurs personnages ont moins de "+fmt(seuil)+" images sur Danbooru, par exemple Raven (39 707 publications sur rule34, 1 954 images sur Danbooru) ou Loona (43 049 contre 592).",
"- Franchises très présentes sur Danbooru mais (presque) absentes de rule34 : "+', '.join(f"{o['franchise']} ({o['personnages']} contre {o['r34_personnages']})" for o in fr if o['personnages']>=5 and int(o['r34_personnages'])<=1)+".",
"- Interprétation (non mesurée) : Danbooru est une base d'illustrations surtout japonaises (fan art, doujin, tout public compris) ; rule34.xxx est un site explicite avec une forte part occidentale (comics, cartoons, furry, jeux occidentaux). Les deux classements mesurent donc deux publics différents."]
open(B+'classement_franchises_danbooru_388_2026-10-25.md','a',encoding='utf-8').write('\n'.join(L)+'\n')
