# Relevé des pages 361-390 (pid 7200-7780) du 25/10/2026 et mise à jour des sélections (méthode A de l'audit).
# Lit les sélections 335 / 336 / 241 (relevé 341-360) et écrit 387 / 388 / 270.
# Numéro de page exact relevé (notes_pages.txt).
import csv, re
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_361-390_2026-10-25/'
DATE='2026-10-25'; SRC='pages 361-390'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'; PM='personnage masculin'
GN='genre non défini / au choix'; DB='doublon'; ES='espèce'; CAT='catégorie'
# page et type relevés
PG={}; TY={}
for l in open(D+'notes_pages.txt',encoding='utf-8'):
    m=re.match(r'(\d{3}) ',l)
    if not m: continue
    for t,c,ty in re.findall(r"([a-z0-9_\-'().!:]+) (\d{4}) (Character(?:, ambiguous)?)",l.split('| Copyright')[0]):
        PG[t]=(m.group(1),int(c)); TY[t]=ty
# tag : (groupe, nature, personnage, univers)
K={
'muffet':(F_,PF,'Muffet','Undertale'),
'ty_lee':(F_,PF,'Ty Lee',"Avatar, le dernier maître de l'air"),
'magik_(illyana_rasputin)':(F_,PF,'Magik (Illyana Rasputin)','Marvel'),
'surge_the_tenrec':(F_,PF,'Surge the Tenrec','Sonic'),
'fujiwara_chika':(F_,PF,'Chika Fujiwara','Kaguya-sama: Love is War'),
'super_crown':(CAT,'catégorie (objet : la Super Couronne de Super Mario Bros. U Deluxe, à l’origine de Bowsette)','super_crown','Super Mario'),
'juno_(overwatch)':(F_,PF,'Juno','Overwatch'),
'satoshi_(pokemon)':(DB,DB,'Sacha / Ash Ketchum (nom japonais ; masculin, déjà dans les autres tags : ash_ketchum)','Pokémon'),
'sakura_kasugano':(F_,PF,'Sakura Kasugano','Street Fighter'),
'orc_(warcraft)':(ES,ES,'Orc (Warcraft)','Warcraft'),
'ashido_mina':(DB,DB,'Mina Ashido (2e tag, déjà dans son union : gain de 420 déjà compté)','My Hero Academia'),
'krystal_(star_fox)':(DB,DB,'Krystal (2e tag, déjà dans son union : gain de 399 déjà compté)','Star Fox'),
'falco_lombardi':(M_,PM,'Falco Lombardi','Star Fox'),
'samui':(F_,PF,'Samui','Naruto'),
'jaina_proudmoore':(F_,PF,'Jaina Proudmoore','Warcraft'),
'nakano_miku':(F_,PF,'Miku Nakano','The Quintessential Quintuplets'),
'luna_snow':(F_,PF,'Luna Snow (Seol Hee)','Marvel'),
'corrin_(fire_emblem)_(female)':(F_,PF,'Corrin (version féminine)','Fire Emblem'),
'gintoki_sakata':(M_,PM,'Gintoki Sakata','Gintama'),
"april_o'neil":(F_,PF,"April O'Neil",'Les Tortues Ninja'),
'gloria_(pokemon)':(F_,PF,'Gloria','Pokémon'),
'ben_tennyson':(M_,PM,'Ben Tennyson','Ben 10'),
"kai'sa":(F_,PF,"Kai'Sa",'League of Legends'),
'rapunzel':(F_,PF,'Raiponce (Rapunzel)','Raiponce (Disney)'),
"dexter's_mom":(F_,PF,'La mère de Dexter','Le Laboratoire de Dexter'),
'esdeath_(akame_ga_kill!)':(F_,PF,'Esdeath','Akame ga Kill!'),
'v_(cyberpunk_2077)':(GN,'personnage (homme ou femme au choix du joueur)','V (Cyberpunk 2077)','Cyberpunk 2077'),
'luxray':(ES,ES,'Luxray (Luxray)','Pokémon'),
'tohru_(dragon_maid)':(F_,PF,'Tohru',"Miss Kobayashi's Dragon Maid"),
'riesz':(F_,PF,'Riesz','Trials of Mana (Seiken Densetsu 3)'),
'pomni':(DB,DB,'Pomni (2e tag ; pomni sans pomni_(the_amazing_digital_circus) ≤ 42, rien à ajouter)','The Amazing Digital Circus'),
'ninetales':(ES,ES,'Feunard (Ninetales)','Pokémon'),
'annie_leonhardt':(F_,PF,'Annie Leonhart',"L'Attaque des Titans"),
'harley_quinn_(injustice)':(DB,DB,'Harley Quinn, version Injustice (sans harley_quinn ≤ 42, rien à ajouter)','DC Comics'),
'poison_(final_fight)':(F_,PF,'Poison','Final Fight'),
'rey':(F_,PF,'Rey','Star Wars'),
'pearl_(steven_universe)':(F_,PF,'Perle (Pearl)','Steven Universe'),
'tawna_bandicoot':(F_,PF,'Tawna Bandicoot','Crash Bandicoot'),
'main_character_(summertime_saga)':(M_,PM,'Protagoniste de Summertime Saga','Summertime Saga'),
'shinomiya_kaguya':(F_,PF,'Kaguya Shinomiya','Kaguya-sama: Love is War'),
'scout_(team_fortress_2)':(M_,PM,'Scout','Team Fortress 2'),
'jolyne_kujo':(F_,PF,'Jolyne Cujoh (Kujo)',"JoJo's Bizarre Adventure"),
'luna_snow_(marvel_rivals)':(DB,DB,'Luna Snow, version Marvel Rivals (sans luna_snow ≤ 42, rien à ajouter)','Marvel'),
'salazzle':(ES,ES,'Malamandre (Salazzle)','Pokémon'),
'gwen_(league_of_legends)':(F_,PF,'Gwen','League of Legends'),
'sunflower_(pvz)':(ES,'espèce (plante de Plants vs. Zombies)','Tournesol (Sunflower)','Plants vs. Zombies'),
'marisa_kirisame':(F_,PF,'Marisa Kirisame','Touhou Project'),
'unohana_retsu':(F_,PF,'Retsu Unohana','Bleach'),
'undyne':(F_,PF,'Undyne','Undertale'),
'irelia_xan':(F_,PF,'Irelia','League of Legends'),
'caelus_(honkai:_star_rail)':(M_,PM,'Caelus (Pionnier)','Honkai: Star Rail'),
'ranma-chan':(F_,PF,'Ranma-chan (Ranma sous sa forme féminine)','Ranma ½'),
'reisen_udongein_inaba':(F_,PF,'Reisen Udongein Inaba','Touhou Project'),
'amber_(genshin_impact)':(F_,PF,'Amber','Genshin Impact'),
'master_tigress':(F_,PF,'Maître Tigresse','Kung Fu Panda'),
'pyrrha_nikos':(F_,PF,'Pyrrha Nikos','RWBY'),
'quarian':(ES,ES,'Quarien (Quarian)','Mass Effect'),
'xayah':(F_,PF,'Xayah','League of Legends'),
'psylocke_(marvel_rivals)':(DB,DB,'Psylocke, version Marvel Rivals (déjà mesurée dans son union : ≤ 42)','Marvel'),
'alisa_mikhailovna_kujou':(F_,PF,'Alisa Mikhailovna Kujou (Alya)','Roshidere'),
'anubis':(CAT,'catégorie (divinité égyptienne, pas un personnage d’une œuvre)','anubis','Mythologie égyptienne'),
'riolu':(ES,ES,'Riolu','Pokémon'),
'vex_(league_of_legends)':(F_,PF,'Vex','League of Legends'),
'kirigaya_suguha':(F_,PF,'Suguha Kirigaya (Leafa)','Sword Art Online'),
'yukari_yakumo':(F_,PF,'Yukari Yakumo','Touhou Project'),
'zeraora':(ES,ES,'Zeraora','Pokémon'),
'astrid_hofferson':(F_,PF,'Astrid Hofferson','Dragons (DreamWorks)'),
'purah':(F_,PF,'Purah','The Legend of Zelda'),
'ariel':(F_,PF,'Ariel','La Petite Sirène (Disney)'),
'ayase_seiko':(F_,PF,'Seiko Ayase (grand-mère de Momo)','Dandadan'),
'valerie_(cyberpunk_2077)':(F_,PF,'V (version féminine, Valerie)','Cyberpunk 2077'),
'vegeta':(M_,PM,'Vegeta','Dragon Ball'),
'lena_oxton':(DB,DB,'Tracer (nom civil ; lena_oxton sans tracer = 0)','Overwatch'),
'hilda_valentine_goneril':(F_,PF,'Hilda Valentine Goneril','Fire Emblem'),
'fionna_the_human_girl':(F_,PF,'Fionna','Adventure Time'),
'wendy_corduroy':(F_,PF,'Wendy Corduroy','Gravity Falls'),
'haru_okumura':(F_,PF,'Haru Okumura','Persona 5'),
'kirlia':(ES,ES,'Kirlia','Pokémon'),
'naoto_hachioji_(senpai)':(M_,PM,'Naoto Hachiōji (Senpai)','Arrête de me chauffer, Nagatoro'),
'artoria_pendragon_(fate)':(DB,DB,'Artoria Pendragon (2e tag, déjà dans son union : gain de 1 323 déjà compté)','Fate'),
'haydee':(F_,PF,'Haydee','Haydee'),
}
assert set(K)==set(PG), (set(K)^set(PG))
T=[(PG[t][0],)+K[t][:2]+(t,)+K[t][2:]+(PG[t][1],TY[t]) for t in sorted(K,key=lambda t:-PG[t][1])]
assert len(T)==81
with open(D+'tags_personnages_pages_361-390.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 25/10/2026 ; retenus si > 150 (journal : pids.txt)
G={
 'nakano_miku':('miku_nakano -nakano_miku',0),
 'magik_(illyana_rasputin)':('( magik_(marvel_rivals) ~ magik_(marvel_tokon) ~ magik_(infernal_idol) ~ magik_(punkchild) ~ magik_(darkchylde) ~ illyana_rasputin ) -magik_(illyana_rasputin)',84),
 'luna_snow':('( luna_snow_(marvel_rivals) ~ luna_snow_(cool_summer) ) -luna_snow',0),
 'tohru_(dragon_maid)':("( tohru_(maidragon) ~ tohru_(miss_kobayashi's_dragon_maid) ) -tohru_(dragon_maid)",84),
 'marisa_kirisame':('kirisame_marisa -marisa_kirisame',294),
 'yukari_yakumo':('yakumo_yukari -yukari_yakumo',168),
 'esdeath_(akame_ga_kill!)':('( esdeath ~ esdeath_(akame_ga_kill) ) -esdeath_(akame_ga_kill!)',294),
 "april_o'neil":("( 4 tags de version april_o'neil_(…) ) -april_o'neil",0),
 'sakura_kasugano':('sakura_kasugano_(fortnite) -sakura_kasugano',0),
 'rapunzel':('( rapunzel_(tangled) ~ rapunzel_tangled ~ rapunzel_(disney) ) -rapunzel',882),
 'tawna_bandicoot':('tawna_bandicoot_(crash_4) -tawna_bandicoot',0),
 'jolyne_kujo':('jolyne_cujoh -jolyne_kujo',None),
 'undyne':('( undyne_(deltarune) ~ undyne_(undertale) ) -undyne',0),
 'purah':('( purah_(tears_of_the_kingdom) ~ purah_(age_of_calamity) ~ purah_(breath_of_the_wild) ) -purah',0),
 'ariel':('ariel_(the_little_mermaid) -ariel',1470),
 'hilda_valentine_goneril':('( 4 tags de version hilda_valentine_goneril_(…) ) -hilda_valentine_goneril',0),
 'fionna_the_human_girl':('( fionna_the_human ~ fionna_campbell ) -fionna_the_human_girl',0),
 'haru_okumura':('( haru_okumura_(noir) ~ okumura_haru ) -haru_okumura',0),
 'unohana_retsu':('( unohana_yachiru ~ retsu_unohana ) -unohana_retsu',0),
 'kirigaya_suguha':('( leafa ~ leafa_(sao) ) -kirigaya_suguha',378),
}
NM={'muffet':'variantes : muffet_(undertale) ≤ 57 (autocomplétion)','ty_lee':'variantes : ≤ 3 (autocomplétion)',
    'surge_the_tenrec':'variantes : ≤ 23 chacune (autocomplétion)','fujiwara_chika':'variantes : chika_fujiwara ≤ 45 (autocomplétion)',
    'juno_(overwatch)':'aucune variante (autocomplétion)','samui':'variantes : samui_(naruto) ≤ 48 (autocomplétion)',
    'jaina_proudmoore':'variantes : jaina_(hots_model) ≤ 98 (autocomplétion)','corrin_(fire_emblem)_(female)':'variantes : ≤ 2 (autocomplétion) ; Corrin (tag corrin_(fire_emblem), genre au choix) reste dans les autres tags',
    'gloria_(pokemon)':'aucune variante (autocomplétion)',"kai'sa":"variantes non vérifiables (l'autocomplétion et la recherche de tags ne gèrent pas l'apostrophe)",
    "dexter's_mom":"variantes non vérifiables (apostrophe)",'riesz':'variantes : ≤ 2 (autocomplétion)','annie_leonhardt':'variantes : annie_leonhart ≤ 128 (autocomplétion)',
    'poison_(final_fight)':'variantes : poison_(final_fight)_(younger) ≤ 10 (autocomplétion)','rey':'variantes : rey_(star_wars) 540, non mesuré (tag rey ambigu)',
    'pearl_(steven_universe)':'variantes : pearl_(gem) 2 505 (tag générique de la pierre, non additionné)','shinomiya_kaguya':'variantes : ≤ 4 (autocomplétion)',
    'gwen_(league_of_legends)':'aucune variante (autocomplétion)','irelia_xan':'variantes : irelia ≤ 39 (autocomplétion)',
    'ranma-chan':'aucune variante (autocomplétion) ; Ranma Saotome (tag ranma_saotome, genre non défini) reste dans les autres tags','reisen_udongein_inaba':'variantes : reisen ≤ 117 (ambigu, autocomplétion)',
    'amber_(genshin_impact)':'aucune variante (autocomplétion)','master_tigress':'variantes : tigress_(kung_fu_panda) ≤ 115 (autocomplétion)',
    'pyrrha_nikos':'variantes : ≤ 15 (autocomplétion)','xayah':'variantes : ≤ 1 (autocomplétion)','alisa_mikhailovna_kujou':'aucune variante (autocomplétion)',
    'vex_(league_of_legends)':'aucune variante (autocomplétion)','astrid_hofferson':'aucune variante (autocomplétion)','ayase_seiko':'variantes : seiko_ayase ≤ 69 (autocomplétion)',
    'valerie_(cyberpunk_2077)':'aucune variante (autocomplétion) ; V (tag v_(cyberpunk_2077), genre au choix) reste dans les autres tags',
    'wendy_corduroy':'variantes : ≤ 4 (autocomplétion)','haydee':'le tag de licence haydee_(game) (5 086) n’est pas additionné'}
new=[t for t in T if t[1]==F_]; assert len(new)==52, len(new)
# 1) sélection non dédupliquée : 335 + 52
sel=list(csv.DictReader(open(B+'selection_335_personnages_feminins_2026-10-25.csv',encoding='utf-8-sig')))
assert len(sel)==335
for i,t in enumerate(new):
    sel.append({'rang':str(336+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
with open(B+'selection_387_personnages_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 336 + 52
dd=list(csv.DictReader(open(B+'doublons/selection_336_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig')))
assert len(dd)==336
for i,t in enumerate(new):
    gain=0; mes=NM.get(t[3],'')
    if t[3] in G:
        q,pid=G[t[3]]
        if pid is None: mes=f"{q} = 0"
        else:
            g=pid+21; mes=f"{q} ≈ {g}"
            if g>150: gain=g
            else: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(336+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==388
with open(B+'doublons/selection_388_dedupliquee_audit_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 241 + 29
au=list(csv.DictReader(open(B+'autres_tags_personnages_241_hors_feminins_2026-10-25.csv',encoding='utf-8-sig')))
assert len(au)==241
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==270
with open(B+'autres_tags_personnages_270_hors_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(t[1] for t in T))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'][:70])
print('seuil (dernier) :',dd[-1]['personnage'],dd[-1]['publications_dedup'])
