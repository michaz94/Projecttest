# Relevé des pages 281-290 (pid 5600-5780) du 24/10/2026 et mise à jour des sélections (méthode A de l'audit).
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_281-290_2026-10-24/'
DATE='2026-10-24'; SRC='pages 281-290'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'
GN='genre non défini / au choix'
T=[
(281,F_,PF,'batgirl','Batgirl','DC Comics',8195,C),
(281,'doublon','doublon','ada_wong_(adriana)','Ada Wong (version RE4 remake, déjà ada_wong)','Resident Evil',8188,C),
(281,F_,PF,'mash_kyrielight','Mash Kyrielight','Fate',8183,C),
(282,'doublon','doublon','natasha_romanoff','Black Widow (nom civil, déjà black_widow_(marvel))','Marvel',8121,C),
(282,'doublon','doublon','ahri_(league_of_legends)','Ahri (2e tag, déjà ahri)','League of Legends',8118,C),
(283,'espèce','espèce','flareon','Pyroli (Flareon)','Pokémon',8107,C),
(283,'espèce','espèce','typhlosion','Typhlosion','Pokémon',8090,C),
(284,F_,PF,'marie_rose','Marie Rose','Dead or Alive',8052,CA),
(284,F_,PF,'marge_simpson','Marge Simpson','Les Simpson',8044,C),
(285,F_,PF,'dark_magician_girl','Magicienne des Ténèbres (Dark Magician Girl)','Yu-Gi-Oh!',8007,C),
(285,GN,'personnage (genre non défini)','frisk','Frisk','Undertale',8006,CA),
(286,'espèce','espèce','lugia','Lugia','Pokémon',7966,C),
(286,F_,PF,'ouro_kronii','Ouro Kronii','Hololive',7959,C),
(287,F_,PF,'camilla_(fire_emblem)','Camilla','Fire Emblem',7940,C),
(287,F_,PF,'loba_(apex_legends)','Loba','Apex Legends',7917,CA),
(287,F_,PF,'marie_(splatoon)','Marie','Splatoon',7911,C),
(288,F_,PF,'squirrel_girl_(marvel)','Squirrel Girl','Marvel',7888,C),
(289,F_,PF,'shego','Shego','Kim Possible',7856,C),
(290,'doublon','doublon','harley_quinn_(classic)','Harley Quinn (version classique, déjà harley_quinn)','DC Comics',7829,C),
(290,F_,PF,'panam_palmer','Panam Palmer','Cyberpunk 2077',7822,C),
(290,'espèce','espèce','yoshi','Yoshi','Super Mario',7821,C),
(290,'doublon','doublon','white_queen','Emma Frost (surnom « Reine blanche », déjà emma_frost)','Marvel',7817,C),
(290,GN,'personnage (genre non défini)','chara','Chara','Undertale',7814,CA),
]
assert len(T)==23
with open(D+'tags_personnages_pages_281-290.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 24/10/2026 ; retenus si > 150
G={ # tag: (recherche, dernier pid ou None si 0 résultat) ; gain = dernier pid + 21, retenu si > 150
 'batgirl':('( barbara_gordon ~ batgirl_(barbara_gordon) ~ batgirl_(cassandra_cain) ~ batgirl_(gotham_knights) ~ batgirl_(arkham_knight) ~ batgirl_(dcau) ~ batgirl_(stephanie_brown) ) -batgirl',966),
 'mash_kyrielight':('( mash_kyrielight_(dangerous_beast) ~ shielder_(fate/grand_order) ~ shielder_(fate) ~ mash_kyrielight_(swimsuit_of_perpetual_summer) ) -mash_kyrielight',420),
 'marie_rose':('marie_rose_(devilish_servant_against_the_splashing_waves) -marie_rose',0),
 'ouro_kronii':('( ouro_kronii_(maid) ~ ouro_kronii_(1st_costume) ) -ouro_kronii',0),
 'loba_(apex_legends)':('loba_andrade -loba_(apex_legends)',0),
 'squirrel_girl_(marvel)':('( squirrel_girl_(marvel_rivals) ~ squirrel_girl ~ doreen_green ~ squirrel_girl_(sunshine_squirrel) ~ squirrel_girl_(symbiote_squirrel) ) -squirrel_girl_(marvel)',2184),
}
new=[t for t in T if t[1]==F_]; assert len(new)==12
# 1) sélection non dédupliquée : 216 + 12
sel=list(csv.DictReader(open(B+'selection_216_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(217+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==228
with open(B+'selection_228_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 217 + 12
dd=list(csv.DictReader(open(B+'doublons/selection_217_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    gain=0; mes=''
    if t[3] in G:
        q,pid=G[t[3]]; g=0 if pid is None else pid+21
        mes=f"{q} ≈ {g}" if g<=150 else q
        if pid is None: mes=f"{q} = 0"
        if g>150: gain=g
        elif pid is not None: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(217+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==229
with open(B+'doublons/selection_229_dedupliquee_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 156 + 11
au=list(csv.DictReader(open(B+'autres_tags_personnages_156_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==167
with open(B+'autres_tags_personnages_167_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'])
