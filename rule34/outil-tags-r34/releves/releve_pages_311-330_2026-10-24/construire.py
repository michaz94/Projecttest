# Relevé des pages 311-330 (pid 6200-6580) du 24/10/2026 et mise à jour des sélections (méthode A de l'audit).
# Lit la sélection dédupliquée 256 (avec la correction Batgirl = Barbara seule) et écrit les sélections 293.
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_311-330_2026-10-24/'
DATE='2026-10-24'; SRC='pages 311-330'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'; PM='personnage masculin'
GN='genre non défini / au choix'; ES='espèce'; CAT='catégorie'; DB='doublon'
T=[
(311,F_,PF,'kamisato_ayaka','Kamisato Ayaka','Genshin Impact',7125,C),
(311,F_,PF,'mileena','Mileena','Mortal Kombat',7123,C),
(311,F_,PF,'caulifla','Caulifla','Dragon Ball',7120,CA),
(312,F_,PF,'mori_calliope','Mori Calliope','Hololive',7114,C),
(312,F_,PF,'houshou_marine','Houshou Marine','Hololive',7105,C),
(312,DB,DB,'barbara_gordon','Barbara Gordon (déjà dans l’union de Batgirl)','DC Comics',7096,C),
(313,ES,ES,'argonian','Argonien (espèce, The Elder Scrolls)','The Elder Scrolls',7076,C),
(313,ES,ES,'sangheili','Sangheili / Élite (espèce, Halo)','Halo',7062,C),
(313,F_,PF,'rio_(blue_archive)','Rio (Tsukatsuki Rio)','Blue Archive',7060,C),
(313,DB,DB,'bulma','Bulma (2e tag : 0 publication hors de l’union de bulma_briefs)','Dragon Ball',7042,CA),
(313,F_,PF,'diane_foxington','Diane Foxington','Les Bad Guys',7036,C),
(314,F_,PF,'peridot_(steven_universe)','Péridot','Steven Universe',7018,CA),
(314,F_,PF,'temari','Temari','Naruto',7018,C),
(314,ES,ES,'vulpix','Goupix / Vulpix (espèce Pokémon)','Pokémon',7013,C),
(315,F_,PF,'nejire_hado','Nejire Hado','My Hero Academia',7003,CA),
(315,M_,PM,'dick_grayson','Dick Grayson (Robin / Nightwing)','DC Comics',7003,C),
(315,CAT,CAT,'background_character','Personnage d’arrière-plan (catégorie)','—',6995,C),
(315,F_,PF,'chica_(fnaf)','Chica',"Five Nights at Freddy's",6995,C),
(315,ES,ES,'tauren','Tauren (espèce, Warcraft)','Warcraft',6989,C),
(316,M_,PM,'jax_(the_amazing_digital_circus)','Jax','The Amazing Digital Circus',6977,CA),
(316,DB,DB,'squirrel_girl_(marvel_rivals)','Squirrel Girl (version Marvel Rivals, déjà dans l’union)','Marvel',6972,C),
(317,F_,PF,'evelyn_chevalier','Evelyn Chevalier','Zenless Zone Zero',6964,C),
(317,ES,ES,'incineroar','Félinferno / Incineroar (espèce Pokémon)','Pokémon',6964,C),
(317,F_,PF,'daphne_blake','Daphné Blake','Scooby-Doo',6963,CA),
(317,ES,ES,'gerudo','Gerudo (peuple, The Legend of Zelda)','The Legend of Zelda',6957,C),
(317,GN,GN,'sensei_(blue_archive)','Sensei (personnage du joueur, souvent dessiné en homme)','Blue Archive',6953,C),
(317,F_,PF,'hermione_granger','Hermione Granger','Harry Potter',6949,C),
(318,F_,PF,'princess_cadance_(mlp)','Princesse Cadance','My Little Pony',6936,C),
(318,F_,PF,'poppy','Poppy','League of Legends',6933,C),
(318,F_,PF,'caitlyn_kiramman','Caitlyn Kiramman','League of Legends / Arcane',6928,C),
(318,F_,PF,"lana's_mother_(pokemon)",'Mère de Lana (Néphie en VF)','Pokémon',6923,C),
(318,F_,PF,'ashley_graves','Ashley','WarioWare',6921,C),
(318,F_,PF,'bea_(pokemon)','Bea (Faïza en VF)','Pokémon',6916,C),
(319,F_,PF,'sakuya_izayoi','Sakuya Izayoi','Touhou Project',6900,C),
(319,F_,PF,'uzaki_tsuki','Tsuki Uzaki (mère de Hana)','Uzaki-chan veut traîner !',6896,C),
(319,F_,PF,'jenny_wakeman','Jenny Wakeman (XJ-9)','Ma vie de robot ado',6893,C),
(320,CAT,CAT,'scarlett_johansson','Scarlett Johansson (personne réelle, actrice)','—',6887,C),
(320,F_,PF,'yoko_littner','Yoko Littner','Gurren Lagann',6881,C),
(321,F_,PF,'burnice_white','Burnice White','Zenless Zone Zero',6871,C),
(321,F_,PF,'callie_(splatoon)','Callie','Splatoon',6865,C),
(321,F_,PF,'bayonetta_(character)','Bayonetta','Bayonetta',6850,C),
(321,M_,PM,'shining_armor_(mlp)','Shining Armor','My Little Pony',6848,C),
(322,F_,PF,'miss_fortune','Miss Fortune (Sarah Fortune)','League of Legends',6820,C),
(322,ES,ES,'snivy','Vipélierre / Snivy (espèce Pokémon)','Pokémon',6818,C),
(322,DB,DB,'kara_danvers','Kara Danvers (Supergirl ; ≈ 105 publications sans supergirl ni kara_zor-el, ≤ 150)','DC Comics',6814,CA),
(323,F_,PF,'sanae_kochiya','Sanae Kochiya','Touhou Project',6786,C),
(324,DB,DB,'brazilian_miku','Miku brésilienne (variante de fans de Hatsune Miku ; ≈ 315 publications sans hatsune_miku, non additionnées)','Vocaloid',6768,C),
(324,F_,PF,'judy_alvarez','Judy Alvarez','Cyberpunk 2077',6752,C),
(325,F_,PF,'frankie_foster','Frankie Foster','Foster, la maison des amis imaginaires',6704,C),
(326,DB,DB,'hana_song','Hana Song (vrai nom de D.Va, déjà d.va)','Overwatch',6680,C),
(326,F_,PF,'lisa_(genshin_impact)','Lisa','Genshin Impact',6659,C),
(327,F_,PF,'meow_skulls_(fortnite)','Meow Skulls','Fortnite',6650,CA),
(327,F_,PF,'evelynn','Evelynn','League of Legends',6637,C),
(328,F_,PF,'jean_gunnhildr','Jean Gunnhildr','Genshin Impact',6610,C),
(328,M_,PM,'ichigo_kurosaki','Ichigo Kurosaki','Bleach',6610,C),
(329,F_,PF,'nemona_(pokemon)','Nemona','Pokémon',6592,C),
(329,F_,PF,'skyla_(pokemon)','Skyla (Carolina en VF)','Pokémon',6588,C),
(330,M_,PM,'ash_ketchum','Ash Ketchum (Sacha en VF)','Pokémon',6576,C),
(330,DB,DB,'angela_ziegler','Angela Ziegler (vrai nom de Mercy, déjà mercy)','Overwatch',6561,C),
(330,ES,ES,'raichu','Raichu (espèce Pokémon)','Pokémon',6553,C),
]
assert len(T)==60
with open(D+'tags_personnages_pages_311-330.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 24/10/2026 ; retenus si > 150 (journal : pids.txt)
G={
 'kamisato_ayaka':('( kamisato_ayaka_(springbloom_missive) ~ kamisato_ayaka_(genshin_impact) ~ kamisato_ayaka_(heytea) ) -kamisato_ayaka',0),
 'mileena':('( mileena_(mk9) ~ mileena_(new_era) ~ mileena_(mkx) ~ mileena_(mortal_kombat) ~ mileena_(mk11) ~ mileena_(mk:deception) ) -mileena',0),
 'mori_calliope':('( 7 tags de tenue mori_calliope_(…) ) -mori_calliope',None),
 'houshou_marine':('( 6 tags de tenue houshou_marine_(…) ) -houshou_marine',0),
 'rio_(blue_archive)':('( tsukatsuki_rio ~ rio_tsukatsuki_(blue_archive) ~ rio_(armed)_(blue_archive) ) -rio_(blue_archive)',126),
 'peridot_(steven_universe)':('peridot_(gem) -peridot_(steven_universe)',0),
 'temari':('( temari_(naruto) ~ temari_nara ~ temari_(genin) ) -temari',0),
 'nejire_hado':('( hadou_nejire ~ nejire_hado_(hero_outfit) ~ nejire_hadou ~ hadou_nejire_(hero_outfit) ~ hado_nejire ) -nejire_hado',126),
 'daphne_blake':('( daphne_blake_(mystery_incorporated) ~ daphne_blake_(velma) ~ daphne_blake_(scoob) ) -daphne_blake',0),
 'caitlyn_kiramman':('caitlyn_(league_of_legends) -caitlyn_kiramman',168),
 'sakuya_izayoi':('izayoi_sakuya -sakuya_izayoi',252),
 'jenny_wakeman':('xj-9 -jenny_wakeman',0),
 'callie_(splatoon)':('( 5 tags de tenue callie_(…) ) -callie_(splatoon)',0),
 'miss_fortune':('( sarah_fortune ~ miss_fortune_(league_of_legends) ) -miss_fortune',84),
 'sanae_kochiya':('kochiya_sanae -sanae_kochiya',420),
 'meow_skulls_(fortnite)':('meow_skulls -meow_skulls_(fortnite)',378),
 'evelynn':('evelynn_(league_of_legends) -evelynn',0),
 'jean_gunnhildr':('( jean_(genshin_impact) ~ jean_gunnhildr_(sea_breeze_dandelion) ) -jean_gunnhildr',126),
 'lisa_(genshin_impact)':('( lisa_minci ~ lisa_minci_(genshin_impact) ) -lisa_(genshin_impact)',0),
}
# Notes de mesure sans recherche (variantes trop petites pour dépasser 150 : somme des compteurs d'autocomplétion)
NM={'caulifla':'variantes caulifla_(…) : ≤ 46 au total (autocomplétion)','diane_foxington':'variantes : ≤ 36 au total (autocomplétion)',
    'hermione_granger':'variantes : ≤ 9 (autocomplétion)','burnice_white':'variantes : ≤ 40 (autocomplétion)','skyla_(pokemon)':'variantes : ≤ 100 (autocomplétion)',
    'bayonetta_(character)':'bayonetta (tag de licence, 7 435) -bayonetta_(character) ≈ 651 : non additionné, car c’est le tag du jeu et non du personnage'}
new=[t for t in T if t[1]==F_]; assert len(new)==37
# 1) sélection non dédupliquée : 255 + 37
sel=list(csv.DictReader(open(B+'selection_255_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(256+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==292
with open(B+'selection_292_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 256 + 37
dd=list(csv.DictReader(open(B+'doublons/selection_256_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
assert any(r['tag']=='batgirl' and r['publications_dedup']=='7875' for r in dd)   # correction Barbara seule déjà appliquée
for i,t in enumerate(new):
    gain=0; mes=NM.get(t[3],'')
    if t[3] in G:
        q,pid=G[t[3]]
        if pid is None: mes=f"{q} = 0"
        else:
            g=pid+21; mes=f"{q} ≈ {g}"
            if g>150: gain=g; mes=q
            else: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(256+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==293
with open(B+'doublons/selection_293_dedupliquee_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 189 + 23
au=list(csv.DictReader(open(B+'autres_tags_personnages_189_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==212
with open(B+'autres_tags_personnages_212_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(t[1] for t in T))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'][:70])
