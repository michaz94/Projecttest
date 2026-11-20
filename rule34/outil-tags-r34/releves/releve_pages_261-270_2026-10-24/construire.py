# Relevé des pages 261-270 (pid 5200-5380) du 24/10/2026 et mise à jour des sélections.
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_261-270_2026-10-24/'
DATE='2026-10-24'; SRC='pages 261-270'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'
T=[
(261,F_,PF,'serena_(pokemon)','Serena','Pokémon',9105,C),
(261,'doublon','doublon','selina_kyle','Catwoman (nom civil, déjà catwoman)','DC Comics',9084,C),
(262,F_,PF,'millie_(helluva_boss)','Millie','Helluva Boss',9057,C),
(262,F_,PF,'lusamine_(pokemon)','Elsa-Mina (Lusamine)','Pokémon',9049,C),
(263,'doublon','doublon','invisible_woman_(marvel_rivals)','Femme invisible (version Marvel Rivals, déjà invisible_woman)','Marvel (Les 4 Fantastiques)',9034,C),
(263,'espèce','espèce','jolteon','Voltali','Pokémon',9015,C),
(264,F_,PF,'kamado_nezuko','Nezuko Kamado','Demon Slayer',8977,C),
(264,F_,PF,'bowsette','Bowsette (version féminine de Bowser, création de fans, 2018)','Super Mario',8977,CA),
(264,'catégorie','catégorie','mutant_(marvel)','Mutant (Marvel)','Marvel',8932,C),
(264,F_,PF,'yelan_(genshin_impact)','Yelan','Genshin Impact',8929,CA),
(264,F_,PF,'natsuki_(doki_doki_literature_club)','Natsuki','Doki Doki Literature Club',8919,C),
(264,F_,PF,'akali','Akali','League of Legends',8918,CA),
(265,F_,PF,'lucina_(fire_emblem)','Lucina','Fire Emblem',8865,C),
(267,F_,PF,'higashiyama_kobeni','Kobeni Higashiyama','Chainsaw Man',8827,C),
(268,F_,PF,'lamb_(league_of_legends)','Agneau (Lamb, moitié féminine de Kindred)','League of Legends',8777,C),
(268,F_,PF,'kasumi_(doa)','Kasumi','Dead or Alive',8751,C),
(268,F_,PF,'sona_buvelle','Sona','League of Legends',8740,C),
(268,F_,PF,'coco_bandicoot','Coco Bandicoot','Crash Bandicoot',8730,C),
(269,'catégorie','catégorie (groupe)','team_rocket','Team Rocket','Pokémon',8713,C),
(269,F_,PF,'makoto_niijima','Makoto Niijima','Persona 5',8698,C),
(270,F_,PF,'shenhe_(genshin_impact)','Shenhe','Genshin Impact',8671,C),
(270,F_,PF,'lillie_(pokemon)','Lilie (Lillie)','Pokémon',8651,CA),
]
assert len(T)==22
with open(D+'tags_personnages_pages_261-270.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Unions OU (dernier pid + 21, ±21), 24/10/2026
U=[('Catwoman','catwoman','catwoman ∪ selina_kyle',10167,10290),
   ('Femme invisible','invisible_woman','invisible_woman ∪ sue_storm ∪ invisible_woman_(marvel_rivals)',10816,10836),
   ('Serena','serena_(pokemon)','serena_(pokemon) ∪ serena_(pokemon_games)',9105,9072),
   ('Nezuko Kamado','kamado_nezuko','kamado_nezuko ∪ nezuko_kamado ∪ nezuko_(demon_form)',8977,9786),
   ('Akali','akali','akali ∪ akali_jhomen_tethi ∪ akali_(league_of_legends)',8918,9912),
   ('Kobeni Higashiyama','higashiyama_kobeni','higashiyama_kobeni ∪ kobeni_higashiyama',8827,9156),
   ('Sona','sona_buvelle','sona_buvelle ∪ sona_(league_of_legends)',8740,9072),
   ('Makoto Niijima','makoto_niijima','makoto_niijima ∪ makoto_niijima_(queen) ∪ niijima_makoto',8698,8694)]
UN={}
with open(D+'unions_pages_261-270.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['personnage','tag_principal','recherche','tag_seul_autocomplete','dernier_pid','union','gain','gain_pct','retenu','date_releve'])
    for p,t,r,s,pid in U:
        u=pid+21; g=u-s; keep=g>150
        UN[t]=(u if keep else s, r if keep else 'tag seul')
        w.writerow([p,t,r,s,pid,u,g,round(100*g/s,1),'union' if keep else 'tag seul (gain ≤ bruit ±150)',DATE])
new=[t for t in T if t[1]==F_]; assert len(new)==17
# 1) sélection non dédupliquée : 187 + 17
sel=list(csv.DictReader(open(B+'selection_187_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(188+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==204
with open(B+'selection_204_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée : 188 + 17 (Catwoman et Femme invisible : gains dans le bruit, inchangées)
dd=list(csv.DictReader(open(B+'doublons/selection_188_dedupliquee_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    u,m=UN.get(t[3],(t[6],'tag seul'))
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(188+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'publications_dedup':str(u),
               'methode':'tag seul' if m=='tag seul' else 'union OU '+m,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==205
with open(B+'doublons/selection_205_dedupliquee_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 136 + 5
au=list(csv.DictReader(open(B+'autres_tags_personnages_136_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==141
with open(B+'autres_tags_personnages_141_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['personnage'],r['publications_dedup'],r['methode'][:20])
