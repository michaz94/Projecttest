# Relevé des pages 251-260 (pid 5000-5180) du 24/10/2026 et mise à jour des sélections.
import csv, os
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_251-260_2026-10-24/'
DATE='2026-10-24'; SRC='pages 251-260'
C='Character'; CA='Character, ambiguous'
# page, groupe, nature, tag, personnage, univers, publications, type_site
T=[
(251,'féminin','personnage féminin','yuuki_asuna','Asuna Yuuki','Sword Art Online',9577,CA),
(252,'féminin','personnage féminin','sally_acorn','Sally Acorn','Sonic the Hedgehog',9562,C),
(253,'féminin','personnage féminin','belle_(zenless_zone_zero)','Belle','Zenless Zone Zero',9531,C),
(253,'masculin','personnage (masculin)','batman','Batman','DC Comics',9505,C),
(253,'féminin','personnage féminin','susie_(deltarune)','Susie','Deltarune',9501,C),
(254,'féminin','personnage féminin','kafka_(honkai:_star_rail)','Kafka','Honkai: Star Rail',9473,C),
(254,'catégorie','catégorie','regional_form_(pokemon)','Forme régionale','Pokémon',9448,C),
(254,'féminin','personnage féminin','arlecchino_(genshin_impact)','Arlecchino','Genshin Impact',9440,C),
(255,'féminin','personnage féminin','ilulu_(dragon_maid)','Ilulu','Miss Kobayashi\'s Dragon Maid',9382,CA),
(256,'féminin','personnage féminin','rebecca_(edgerunners)','Rebecca','Cyberpunk: Edgerunners',9371,CA),
(256,'féminin','personnage féminin','nicole_watterson','Nicole Watterson','Le Monde incroyable de Gumball',9366,C),
(256,'féminin','personnage féminin','yamamura_sadako','Sadako Yamamura','Ring (roman et films)',9347,C),
(256,'masculin','personnage (masculin)','fujimaru_ritsuka_(male)','Ritsuka Fujimaru (version masculine du protagoniste)','Fate/Grand Order',9338,C),
(256,'genre non défini / au choix','duo (Agneau féminine, Loup masculin)','kindred','Kindred (Agneau et Loup)','League of Legends',9330,C),
(257,'masculin','personnage (masculin)','boyfriend_(friday_night_funkin)','Boyfriend','Friday Night Funkin\'',9298,C),
(257,'doublon','doublon','karen_starr','Power Girl (nom civil, déjà power_girl)','DC Comics',9294,C),
(257,'féminin','personnage féminin','reze_(chainsaw_man)','Reze','Chainsaw Man',9293,C),
(257,'doublon','doublon','yoruichi_shihouin','Yoruichi (ordre occidental, déjà shihouin_yoruichi)','Bleach',9281,C),
(258,'féminin','personnage féminin','kasane_teto','Kasane Teto','UTAU / Synthesizer V',9269,C),
(258,'doublon','doublon','miles_prower','Tails (nom complet, déjà tails_the_fox ; masculin)','Sonic the Hedgehog',9251,C),
(258,'masculin','personnage (masculin)','asriel_dreemurr','Asriel Dreemurr','Undertale',9224,CA),
(259,'féminin','personnage féminin','kiryuuin_satsuki','Satsuki Kiryuin','Kill la Kill',9215,C),
(259,'espèce','espèce','leafeon','Phyllali','Pokémon',9213,C),
(259,'féminin','personnage féminin','marnie_(pokemon)','Rosemary (Marnie)','Pokémon',9208,C),
(259,'doublon','doublon','link_(breath_of_the_wild)','Link (version Breath of the Wild, déjà link ; masculin)','The Legend of Zelda',9200,C),
(260,'féminin','personnage féminin','nicole_demara','Nicole Demara','Zenless Zone Zero',9149,CA),
(260,'espèce','espèce','viera','Viera','Final Fantasy',9125,C),
]
assert len(T)==27
with open(D+'tags_personnages_pages_251-260.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Unions OU (dernier pid + 21, ±21), 24/10/2026
U=[('Yoruichi','shihouin_yoruichi','shihouin_yoruichi ∪ yoruichi_shihouin',21936,25368),
   ('Power Girl','power_girl','power_girl ∪ karen_starr',13711,13902),
   ('Asuna Yuuki','yuuki_asuna','yuuki_asuna ∪ asuna_(sao) ∪ asuna_yuuki',9577,10458),
   ('Sadako Yamamura','yamamura_sadako','yamamura_sadako ∪ sadako_yamamura',9347,9744),
   ('Ilulu','ilulu_(dragon_maid)','ilulu_(dragon_maid) ∪ ilulu_(maidragon) ∪ ilulu',9382,9618),
   ('Rebecca','rebecca_(edgerunners)','rebecca_(edgerunners) ∪ rebecca_(cyberpunk)',9371,9492),
   ('Kasane Teto','kasane_teto','kasane_teto ∪ kasane_teto_(sv)',9269,9156)]
UN={}
with open(D+'unions_pages_251-260.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['personnage','tag_principal','recherche','tag_seul_autocomplete','dernier_pid','union','gain','gain_pct','retenu','date_releve'])
    for p,t,r,s,pid in U:
        u=pid+21; g=u-s; keep=g>150
        UN[t]=(u if keep else s, r if keep else 'tag seul')
        w.writerow([p,t,r,s,pid,u,g,round(100*g/s,1),'union' if keep else 'tag seul (gain ≤ bruit ±150)',DATE])
# 1) sélection non dédupliquée : 172 + nouvelles
sel=list(csv.DictReader(open(B+'selection_172_personnages_feminins_2026-10-23.csv',encoding='utf-8-sig')))
new=[t for t in T if t[1]=='féminin']
assert len(new)==15
for i,t in enumerate(new):
    sel.append({'rang':str(173+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
with open(B+'selection_187_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée : 173 + nouvelles, Yoruichi et Power Girl mises à jour
dd=list(csv.DictReader(open(B+'doublons/selection_173_dedupliquee_2026-10-24.csv',encoding='utf-8-sig')))
for r in dd:
    if r['tag'] in ('shihouin_yoruichi','power_girl'):
        u,m=UN[r['tag']]; r['publications_dedup']=str(u); r['methode']='union OU '+m+' (pages 251-260)'
for i,t in enumerate(new):
    u,m=UN.get(t[3],(t[6],'tag seul'))
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(173+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'publications_dedup':str(u),
               'methode':'tag seul' if m=='tag seul' else 'union OU '+m,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else:
        r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
with open(B+'doublons/selection_188_dedupliquee_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 124 + 12
au=list(csv.DictReader(open(B+'autres_tags_personnages_124_hors_feminins_2026-10-23.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!='féminin':
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==136
with open(B+'autres_tags_personnages_136_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
from collections import Counter
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC or r['tag'] in ('shihouin_yoruichi','power_girl'): print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'])
print(len(sel),len(dd))
