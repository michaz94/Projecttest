# Relevé des pages 291-300 (pid 5800-5980) du 24/10/2026 et mise à jour des sélections (méthode A de l'audit).
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_291-300_2026-10-24/'
DATE='2026-10-24'; SRC='pages 291-300'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'
GN='genre non défini / au choix'
T=[
(291,F_,PF,'keqing_(genshin_impact)','Keqing','Genshin Impact',7793,C),
(292,F_,PF,'noelle_silva','Noelle Silva','Black Clover',7773,C),
(292,'doublon','doublon',"koriand'r","Starfire (nom tamaranien, déjà starfire)",'DC Comics',7764,C),
(292,'espèce','espèce','pal_(species)','Pal (espèce de Palworld)','Palworld',7753,C),
(293,GN,'personnage (homme ou femme au choix du joueur)','corrin_(fire_emblem)','Corrin','Fire Emblem',7730,C),
(294,F_,PF,'femshep','Commandant Shepard (version féminine)','Mass Effect',7700,C),
(294,F_,PF,'sonia_(pokemon)','Sonia','Pokémon',7693,C),
(294,'doublon','doublon','batman_(bruce_wayne)','Batman (Bruce Wayne, déjà batman ; masculin)','DC Comics',7685,C),
(295,F_,PF,'she-hulk','She-Hulk','Marvel',7675,C),
(295,F_,PF,'luxanna_crownguard','Lux','League of Legends',7671,C),
(295,F_,PF,'violet_parr','Violette Parr','Les Indestructibles',7665,C),
(295,'catégorie','catégorie','octoling_girl','Octaling fille','Splatoon',7661,C),
(295,F_,PF,'miranda_lawson','Miranda Lawson','Mass Effect',7641,C),
(296,'doublon','doublon','kara_zor-l','Power Girl (nom kryptonien, déjà power_girl)','DC Comics',7616,C),
(297,F_,PF,'mary_jane_watson','Mary Jane Watson','Marvel',7592,C),
(298,F_,PF,'soraka','Soraka','League of Legends',7538,C),
(299,F_,PF,'quetzalcoatl_(dragon_maid)','Lucoa (Quetzalcoatl)',"Miss Kobayashi's Dragon Maid",7517,CA),
(299,'doublon','doublon','gwen_tennyson_(classic)','Gwen Tennyson (version enfant de la série 2005, déjà gwen_tennyson ; gain non ajouté)','Ben 10',7514,C),
(299,'doublon','doublon','psylocke','Psylocke (déjà dans la sélection : union psylocke ∪ psylocke_(kwannon))','Marvel',7512,C),
(299,F_,PF,'brigitte','Brigitte','Overwatch',7504,C),
(299,F_,PF,'kyoka_jiro','Kyoka Jiro','My Hero Academia',7493,C),
(300,F_,PF,'kefla','Kefla','Dragon Ball',7491,C),
]
assert len(T)==22
with open(D+'tags_personnages_pages_291-300.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 24/10/2026 ; retenus si > 150
G={ # tag: (recherche, dernier pid ou None si 0 résultat) ; gain = dernier pid + 21, retenu si > 150
 'keqing_(genshin_impact)':('( keqing_(opulent_splendor)_(genshin_impact) ~ keqing ) -keqing_(genshin_impact)',0),
 'she-hulk':('( jennifer_walters ~ she-hulk_(fortnite) ~ she-hulk_(endlessillusion) ) -she-hulk',84),
 'mary_jane_watson':('( mary_jane_watson_(insomniac) ~ mary_jane_watson_(fortnite) ~ mary_jane_watson_(spider-man:_the_animated_series) ) -mary_jane_watson',0),
 'soraka':('soraka_(league_of_legends) -soraka',0),
 'quetzalcoatl_(dragon_maid)':("( lucoa ~ lucoa_(maidragon) ~ quetzalcoatl_(miss_kobayashi's_dragon_maid) ~ quetzalcoatl_(maidragon) ) -quetzalcoatl_(dragon_maid)",1134),
 'brigitte':('brigitte_lindholm -brigitte',0),
 'kyoka_jiro':('( jirou_kyouka ~ jiro_kyoka ) -kyoka_jiro',0),
 'kefla':('kefla_(dragon_ball) -kefla',0),
}
new=[t for t in T if t[1]==F_]; assert len(new)==14
# 1) sélection non dédupliquée : 216 + 12
sel=list(csv.DictReader(open(B+'selection_228_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    sel.append({'rang':str(229+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
assert len(sel)==242
with open(B+'selection_242_personnages_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 217 + 12
dd=list(csv.DictReader(open(B+'doublons/selection_229_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
for i,t in enumerate(new):
    gain=0; mes=''
    if t[3] in G:
        q,pid=G[t[3]]; g=0 if pid is None else pid+21
        mes=f"{q} ≈ {g}" if g<=150 else q
        if pid is None: mes=f"{q} = 0"
        if g>150: gain=g
        elif pid is not None: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(229+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==243
with open(B+'doublons/selection_243_dedupliquee_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 156 + 11
au=list(csv.DictReader(open(B+'autres_tags_personnages_167_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==175
with open(B+'autres_tags_personnages_175_hors_feminins_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(r['groupe'] for r in au))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'])
