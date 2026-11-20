# Relevé des pages 301-310 (pid 6000-6180) du 24/10/2026 et mise à jour des sélections (méthode A de l'audit).
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_301-310_2026-10-24/'
DATE='2026-10-24'; SRC='pages 301-310'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'
GN='genre non défini / au choix'
T=[
(301,'espèce','espèce','hypno','Hypno (espèce Pokémon)','Pokémon',7456,CA),
(301,'espèce','espèce','delphox','Goupelin / Delphox (espèce Pokémon)','Pokémon',7455,C),
(301,'catégorie','catégorie','npc_trainer','Dresseur PNJ (catégorie)','Pokémon',7449,C),
(302,'doublon','doublon','gwen_stacy_(spider-verse)','Gwen Stacy (version Spider-Verse, déjà dans l’union de gwen_stacy)','Marvel',7415,C),
(302,F_,PF,'poison_ivy','Poison Ivy','DC Comics',7409,C),
(303,F_,PF,'zero_two_(darling_in_the_franxx)','Zero Two','Darling in the Franxx',7392,C),
(303,M_,'personnage masculin','legoshi_(beastars)','Legoshi','Beastars',7379,C),
(305,M_,'personnage masculin','denji_(chainsaw_man)','Denji','Chainsaw Man',7348,C),
(305,M_,'personnage masculin','big_macintosh_(mlp)','Big Macintosh','My Little Pony',7346,C),
(305,'doublon','doublon','amelie_lacroix','Amélie Lacroix (vrai nom de Widowmaker, déjà widowmaker)','Overwatch',7335,C),
(305,F_,PF,'karin_(blue_archive)','Karin (Kakudate Karin)','Blue Archive',7334,C),
(305,F_,PF,'queen_chrysalis_(mlp)','Reine Chrysalis','My Little Pony',7334,C),
(306,F_,PF,'nakano_nino','Nino Nakano','The Quintessential Quintuplets',7314,CA),
(306,F_,PF,'zenin_maki','Maki Zen’in','Jujutsu Kaisen',7312,C),
(306,'doublon','doublon','toga_himiko','Himiko Toga (nom inversé, déjà dans l’union de himiko_toga)','My Hero Academia',7296,C),
(306,F_,PF,'colette_(brawl_stars)','Colette','Brawl Stars',7293,CA),
(307,F_,PF,'princess_jasmine','Jasmine','Aladdin',7287,C),
(307,F_,PF,'noelle_holiday','Noelle Holiday','Deltarune',7286,CA),
(307,F_,PF,'zhu_yuan','Zhu Yuan','Zenless Zone Zero',7274,C),
(308,M_,'personnage masculin','finn_the_human','Finn','Adventure Time',7259,C),
(308,M_,'personnage masculin','raikage','Raikage (titre, surtout A / Ay)','Naruto',7255,C),
(308,F_,PF,'usagi_tsukino','Usagi Tsukino (Sailor Moon)','Sailor Moon',7255,C),
(308,'doublon','doublon','k/da_ahri','Ahri (skin K/DA, déjà ahri)','League of Legends',7251,C),
(308,F_,PF,'gotou_hitori','Hitori Gotō','Bocchi the Rock!',7250,C),
(308,M_,'personnage masculin','yorha_9s','9S','NieR: Automata',7235,C),
(309,F_,PF,'luz_noceda','Luz Noceda','Luz à Osville (The Owl House)',7228,C),
(310,'doublon','doublon','artoria_pendragon_(lancer)','Artoria Pendragon (Lancer) : version d’un autre Servant, non additionnée (même règle que l’audit)','Fate',7181,C),
]
assert len(T)==27
with open(D+'tags_personnages_pages_301-310.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 24/10/2026 ; retenus si > 150
G={
 'poison_ivy':('( pamela_isley ~ poison_ivy_(dcau) ~ poison_ivy_(arkham) ~ poison_ivy_(arkham_knight) ~ poison_ivy_(fortnite) ~ poison_ivy_(harley_quinn) ~ pamela_isley_(shg) ~ poison_ivy_(injustice) ) -poison_ivy',42),
 'zero_two_(darling_in_the_franxx)':('zero_two -zero_two_(darling_in_the_franxx)',42),
 'karin_(blue_archive)':('( kakudate_karin ~ karin_kakudate ) -karin_(blue_archive)',0),
 'queen_chrysalis_(mlp)':('queen_chrysalis -queen_chrysalis_(mlp)',0),
 'nakano_nino':('nino_nakano -nakano_nino',42),
 'zenin_maki':('maki_zenin -zenin_maki (mesure antérieure du 24/10)',0),
 'princess_jasmine':('( jasmine_(aladdin) ~ princess_jasmine_(disney) ) -princess_jasmine',210),
 'noelle_holiday':('( noelle_holiday_(dark_world_form) ~ noelle_holiday_(light_world_form) ) -noelle_holiday',None),
 'usagi_tsukino':('( sailor_moon ~ tsukino_usagi ) -usagi_tsukino',630),
 'luz_noceda':('( luz_noceda_(beta) ~ luz_noceda_(titan) ~ luz_noceda_(timeskip) ) -luz_noceda',0),
}
new=[t for t in T if t[1]==F_]; assert len(new)==13
# 1) sélection non dédupliquée : 242 + 13
sel=list(csv.DictReader(open(B+'selection_242_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(243+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==255
with open(B+'selection_255_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 217 + 12
dd=list(csv.DictReader(open(B+'doublons/selection_243_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    gain=0; mes=''
    if t[3] in G:
        q,pid=G[t[3]]; g=0 if pid is None else pid+21
        mes=f"{q} ≈ {g}" if g<=150 else q
        if pid is None: mes=f"{q} = 0"
        if g>150: gain=g
        elif pid is not None: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(243+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==256
with open(B+'doublons/selection_256_dedupliquee_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 156 + 11
au=list(csv.DictReader(open(B+'autres_tags_personnages_175_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==189
with open(B+'autres_tags_personnages_189_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'])
