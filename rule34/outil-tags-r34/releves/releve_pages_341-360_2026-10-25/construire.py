# Relevé des pages 341-360 (pid 6800-7180) du 25/10/2026 et mise à jour des sélections (méthode A de l'audit).
# Lit les sélections 306 / 307 / 223 (relevé 331-340) et écrit 335 / 336 / 241.
# Numéro de page exact non noté pendant le relevé : colonne page = « 341-360 ».
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_341-360_2026-10-25/'
DATE='2026-10-25'; SRC='pages 341-360'; P='341-360'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'; PM='personnage masculin'
GN='genre non défini / au choix'; DB='doublon'; EX='exclu'
T=[
(P,F_,PF,'vi','Vi','League of Legends / Arcane',6222,C),
(P,EX,'avatar d’une personne réelle (YouTubeur·se), exclu','jaiden','Jaiden (avatar de la YouTubeuse·eur Jaiden Animations)','Jaiden Animations (YouTube)',6220,CA),
(P,F_,PF,'isabella_valentine','Ivy Valentine (Isabella Valentine)','Soulcalibur',6191,C),
(P,M_,PM,'luigi','Luigi','Super Mario',6177,CA),
(P,F_,PF,'gawr_gura','Gawr Gura','Hololive',6164,CA),
(P,F_,PF,'misato_katsuragi','Misato Katsuragi','Evangelion',6164,C),
(P,M_,PM,'robin_(dc)','Robin (DC ; surtout Dick Grayson, Jason Todd, Tim Drake, Damian Wayne)','DC Comics',6158,C),
(P,F_,PF,'trixie_(mlp)','Trixie Lulamoon','My Little Pony',6137,C),
(P,F_,PF,'tenten','Tenten','Naruto',6132,C),
(P,F_,PF,'felicia_(darkstalkers)','Felicia','Darkstalkers',6117,C),
(P,DB,DB,'orihime_inoue','Orihime Inoue (2e tag ; orihime_inoue sans inoue_orihime = 0, rien à ajouter)','Bleach',6109,C),
(P,M_,PM,'beerus','Beerus','Dragon Ball',6078,C),
(P,F_,PF,'kit_(gameoverse)','Kit (Kit Bodega)','Gameoverse',6069,CA),
(P,F_,PF,'hestia_(danmachi)','Hestia','DanMachi',6063,C),
(P,DB,DB,'ashley_graham_(ella_freya)','Ashley Graham, version modèle Ella Freya (≈ 21 publications sans ashley_graham, non additionnées)','Resident Evil 4',6057,C),
(P,F_,PF,'max_caulfield','Max Caulfield','Life is Strange',6042,C),
(P,F_,PF,'sayori_(doki_doki_literature_club)','Sayori','Doki Doki Literature Club',6010,C),
(P,GN,'ambigu (garçon devenu fille)','ranma_saotome','Ranma Saotome','Ranma ½',5998,C),
(P,F_,PF,'vaggie_(hazbin_hotel)','Vaggie','Hazbin Hotel',5958,C),
(P,DB,DB,'midnight_lycanroc','Lougaroc forme Crépusculaire/Nocturne (forme de l’espèce lycanroc, déjà relevée : 9 986)','Pokémon',5951,C),
(P,F_,PF,'mitsuki_bakugou','Mitsuki Bakugo','My Hero Academia',5948,C),
(P,M_,PM,'uzumaki_boruto','Boruto Uzumaki','Naruto / Boruto',5944,CA),
(P,F_,PF,'kallen_stadtfeld','Kallen Stadtfeld (Kozuki)','Code Geass',5920,C),
(P,DB,DB,'sailor_moon','Sailor Moon (identité d’Usagi Tsukino, déjà dans son union : gain de 651 déjà compté)','Sailor Moon',5912,C),
(P,F_,PF,'melony_(pokemon)','Melony (Lona)','Pokémon',5911,C),
(P,F_,PF,'raven_team_leader','Raven Team Leader','Fortnite',5862,C),
(P,DB,DB,'clark_kent','Clark Kent (identité civile de Superman, masculin ; recouvrement avec superman non mesuré)','DC Comics',5852,C),
(P,DB,DB,'chel_(the_road_to_el_dorado)','Chel (2e tag, déjà dans son union : gain de 525 déjà compté)',"La Route d'Eldorado (DreamWorks)",5849,C),
(P,F_,PF,'lapis_lazuli_(steven_universe)','Lapis Lazuli','Steven Universe',5844,C),
(P,F_,PF,'female_chara','Chara (version féminine)','Undertale',5842,C),
(P,M_,PM,'roronoa_zoro','Roronoa Zoro','One Piece',5823,C),
(P,F_,PF,'lucyna_kushinada','Lucy (Lucyna Kushinada)','Cyberpunk: Edgerunners',5815,C),
(P,F_,PF,'katarina_du_couteau','Katarina','League of Legends',5811,C),
(P,DB,DB,'jill_valentine_(julia_voth)','Jill Valentine, version modèle Julia Voth (≈ 21 publications sans jill_valentine, non additionnées)','Resident Evil',5811,C),
(P,F_,PF,'komi_shuuko','Shuuko Komi (mère de Shouko)','Komi cherche ses mots',5778,CA),
(P,F_,PF,'firefly_(honkai:_star_rail)','Firefly','Honkai: Star Rail',5770,C),
(P,F_,PF,'taihou_(azur_lane)','Taihou','Azur Lane',5769,C),
(P,DB,DB,'rangiku_matsumoto','Rangiku Matsumoto (2e tag ; rangiku_matsumoto sans matsumoto_rangiku = 0, rien à ajouter)','Bleach',5765,C),
(P,M_,PM,'son_gohan','Son Gohan','Dragon Ball',5762,C),
(P,F_,PF,'edelgard_von_hresvelg','Edelgard von Hresvelg','Fire Emblem',5756,C),
(P,F_,PF,'mavuika_(genshin_impact)','Mavuika','Genshin Impact',5748,C),
(P,M_,PM,'satoru_gojo','Satoru Gojo','Jujutsu Kaisen',5745,C),
(P,F_,PF,'patchouli_knowledge','Patchouli Knowledge','Touhou Project',5736,C),
(P,GN,'personnage (homme ou femme au choix du joueur)','villager_(animal_crossing)','Villageois·e (avatar du joueur)','Animal Crossing',5732,C),
(P,F_,PF,'ghislaine_dedoldia','Ghislaine Dedoldia','Mushoku Tensei',5699,C),
(P,F_,PF,'star_butterfly','Star Butterfly','Star vs. les forces du mal',5697,C),
(P,F_,PF,'tharja_(fire_emblem)','Tharja','Fire Emblem',5693,C),
]
assert len(T)==47
with open(D+'tags_personnages_pages_341-360.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 25/10/2026 ; retenus si > 150 (journal : pids.txt)
G={
 'vi':('vi_(league_of_legends) -vi',168),
 'gawr_gura':('( gawr_gura_(1st_costume) ~ gawr_gura_(casual) ~ gawr_gura_ch. ~ gawr_gura_(3rd_costume) ) -gawr_gura',None),
 'misato_katsuragi':('katsuragi_misato -misato_katsuragi',126),
 'trixie_(mlp)':('( trixie_lulamoon ~ trixie_lulamoon_(eg) ) -trixie_(mlp)',84),
 'tenten':('tenten_(genin) -tenten',0),
 'felicia_(darkstalkers)':('felicia darkstalkers -felicia_(darkstalkers)',42),
 'max_caulfield':('max_caulfield_(double_exposure) -max_caulfield',0),
 'sayori_(doki_doki_literature_club)':('sayori doki_doki_literature_club -sayori_(doki_doki_literature_club)',None),
 'vaggie_(hazbin_hotel)':('vaggie -vaggie_(hazbin_hotel)',0),
 'mitsuki_bakugou':('bakugou_mitsuki -mitsuki_bakugou',84),
 'lapis_lazuli_(steven_universe)':('lapis_lazuli_(gem) -lapis_lazuli_(steven_universe)',0),
 'firefly_(honkai:_star_rail)':('( firefly_(spring_missive)_(…) ~ firefly_(ar-26710)_(…) ) -firefly_(honkai:_star_rail)',None),
 'taihou_(azur_lane)':('( 6 tags de tenue taihou_(…)_(azur_lane) ) -taihou_(azur_lane)',0),
 'edelgard_von_hresvelg':('( 4 tags de version edelgard_von_hresvelg_(…) ) -edelgard_von_hresvelg',None),
 'katarina_du_couteau':('katarina_(league_of_legends) -katarina_du_couteau',42),
 'raven_team_leader':('( raven_team_leader_(fortnite) ~ raven_team_leader_(cuddly) ) -raven_team_leader',0),
 'kallen_stadtfeld':('kouzuki_kallen -kallen_stadtfeld',0),
 'lucyna_kushinada':('lucy_(cyberpunk) -lucyna_kushinada',0),
}
NM={'isabella_valentine':'variantes : ivy_valentine ≤ 2 (autocomplétion)','hestia_(danmachi)':'autre tag : hestia 200 (ambigu, non mesuré)',
    'kit_(gameoverse)':'aucune variante hors cosplay (autocomplétion)','melony_(pokemon)':'autre tag : melony 63 (ambigu, non mesuré)',
    'female_chara':'aucune variante (female_character 255 = tag générique) ; Chara (tag chara, genre au choix) reste dans les autres tags',
    'komi_shuuko':'variantes : ≤ 1 (autocomplétion)','mavuika_(genshin_impact)':'variantes : mavuika ≤ 48 (autocomplétion)',
    'patchouli_knowledge':'variantes : ≤ 8 (autocomplétion)','ghislaine_dedoldia':'variantes : ≤ 8 (autocomplétion)',
    'star_butterfly':'variantes : ≤ 16 (autocomplétion)','tharja_(fire_emblem)':'variantes : ≤ 104 au total (autocomplétion)'}
new=[t for t in T if t[1]==F_]; assert len(new)==29
# 1) sélection non dédupliquée : 306 + 29
sel=list(csv.DictReader(open(B+'selection_306_personnages_feminins_2026-10-25.csv',encoding='utf-8-sig')))
assert len(sel)==306
for i,t in enumerate(new):
    sel.append({'rang':str(307+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
with open(B+'selection_335_personnages_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 307 + 29
dd=list(csv.DictReader(open(B+'doublons/selection_307_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig')))
assert len(dd)==307
for i,t in enumerate(new):
    gain=0; mes=NM.get(t[3],'')
    if t[3] in G:
        q,pid=G[t[3]]
        if pid is None: mes=f"{q} = 0"
        else:
            g=pid+21; mes=f"{q} ≈ {g}"
            if g>150: gain=g; mes=q+f' ≈ {g}'
            else: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(307+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==336
with open(B+'doublons/selection_336_dedupliquee_audit_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 223 + 18
au=list(csv.DictReader(open(B+'autres_tags_personnages_223_hors_feminins_2026-10-25.csv',encoding='utf-8-sig')))
assert len(au)==223
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==241
with open(B+'autres_tags_personnages_241_hors_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(t[1] for t in T))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'][:70])
print('seuil (dernier) :',dd[-1]['personnage'],dd[-1]['publications_dedup'])
