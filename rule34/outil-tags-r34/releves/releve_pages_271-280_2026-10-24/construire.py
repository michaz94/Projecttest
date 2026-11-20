# Relevé des pages 271-280 (pid 5400-5580) du 24/10/2026 et mise à jour des sélections (méthode A de l'audit).
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_271-280_2026-10-24/'
DATE='2026-10-24'; SRC='pages 271-280'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'
T=[
(271,'doublon','doublon','lara_croft_(classic)','Lara Croft (version classique, déjà lara_croft)','Tomb Raider',8647,C),
(271,F_,PF,'uzaki_hana','Hana Uzaki',"Uzaki-chan veut traîner !",8621,C),
(271,'espèce','espèce','goodra','Muplodocus (Goodra)','Pokémon',8619,C),
(271,F_,PF,'tohsaka_rin','Rin Tohsaka','Fate',8612,C),
(272,M_,'personnage masculin','moxxie_(helluva_boss)','Moxxie','Helluva Boss',8599,C),
(272,M_,'personnage masculin','sasuke_uchiha','Sasuke Uchiha','Naruto',8584,C),
(273,F_,PF,'lola_bunny','Lola Bunny','Looney Tunes',8547,C),
(273,M_,'personnage masculin','freddy_(fnaf)','Freddy Fazbear',"Five Nights at Freddy's",8525,C),
(274,'doublon','doublon','bruce_wayne','Bruce Wayne (nom civil, déjà batman)','DC Comics',8496,C),
(274,F_,PF,'yuri_(doki_doki_literature_club)','Yuri','Doki Doki Literature Club',8466,C),
(275,F_,PF,'stocking_anarchy','Stocking Anarchy','Panty & Stocking with Garterbelt',8450,C),
(275,F_,PF,'mavis_dracula','Mavis Dracula','Hôtel Transylvanie',8447,C),
(275,M_,'personnage masculin','beast_boy','Beast Boy','DC Comics',8422,C),
(275,'catégorie','catégorie','unknown_character','Personnage inconnu','—',8413,C),
(276,F_,PF,'rogue_(x-men)','Malicia (Rogue)','Marvel',8410,C),
(276,M_,'personnage masculin','leon_scott_kennedy','Leon S. Kennedy','Resident Evil',8377,C),
(277,M_,'personnage masculin','bonnie_(fnaf)','Bonnie',"Five Nights at Freddy's",8339,C),
(278,F_,PF,'palutena','Palutena','Kid Icarus',8318,CA),
(278,'espèce','espèce','xenomorph','Xénomorphe','Alien',8292,CA),
(278,F_,PF,'marceline','Marceline','Adventure Time',8284,C),
(278,F_,PF,'minamoto_no_raikou_(fate/grand_order)','Minamoto no Raikou','Fate',8282,C),
(279,F_,PF,'eve_(stellar_blade)','Eve','Stellar Blade',8265,C),
(279,'espèce','espèce',"twi'lek","Twi'lek",'Star Wars',8260,C),
(279,'espèce','espèce','mewtwo','Mewtwo','Pokémon',8257,CA),
(279,M_,'personnage masculin','venti_(genshin_impact)','Venti','Genshin Impact',8243,C),
(280,M_,'personnage masculin','knuckles_the_echidna','Knuckles','Sonic',8228,C),
(280,F_,PF,'android_21','C-21 (Android 21)','Dragon Ball',8209,CA),
]
assert len(T)==27
with open(D+'tags_personnages_pages_271-280.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 24/10/2026 ; retenus si > 150
G={ # tag: (recherche, dernier pid ou None si 0 résultat, gain retenu)
 'tohsaka_rin':('rin_tohsaka -tohsaka_rin',None),
 'stocking_anarchy':('stocking_(psg) -stocking_anarchy',42),
 'rogue_(x-men)':('( anna_marie ~ rogue_(marvel_rivals) ~ rogue_(evolution) ~ rogue_(savage_land) ) -rogue_(x-men)',210),
 'marceline':('( marceline_abadeer ~ marceline_the_vampire_queen ) -marceline',0),
 'minamoto_no_raikou_(fate/grand_order)':('minamoto_no_raikou_(fate) -minamoto_no_raikou_(fate/grand_order)',672),
 'android_21':('( android_21_(human) ~ android_21_(evil) ~ android_21_(good) ) -android_21',0),
}
new=[t for t in T if t[1]==F_]; assert len(new)==12
# 1) sélection non dédupliquée : 204 + 12
sel=list(csv.DictReader(open(B+'selection_204_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(205+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==216
with open(B+'selection_216_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 205 + 12
dd=list(csv.DictReader(open(B+'doublons/selection_205_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    gain=0; mes=''
    if t[3] in G:
        q,pid=G[t[3]]; g=0 if pid is None else pid+21
        mes=f"{q} ≈ {g}" if g<=150 else q
        if pid is None: mes=f"{q} = 0"
        if g>150: gain=g
        elif pid is not None: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(205+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==217
with open(B+'doublons/selection_217_dedupliquee_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 141 + 15
au=list(csv.DictReader(open(B+'autres_tags_personnages_141_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==156
with open(B+'autres_tags_personnages_156_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'])
