# Relevé des pages 331-340 (pid 6600-6780) du 25/10/2026 et mise à jour des sélections (méthode A de l'audit).
# Lit les sélections 292 / 293 / 212 (relevé 311-330) et écrit 306 / 307 / 223.
import csv
from collections import Counter
B='/home/user/outil_tags_r34/'
D=B+'releves/releve_pages_331-340_2026-10-25/'
DATE='2026-10-25'; SRC='pages 331-340'
C='Character'; CA='Character, ambiguous'
F_='féminin'; PF='personnage féminin'; M_='masculin'; PM='personnage masculin'
GN='genre non défini / au choix'; ES='espèce'; DB='doublon'
T=[
(331,F_,PF,'ayane_(doa)','Ayane','Dead or Alive',6531,C),
(332,M_,PM,'ren_amamiya','Ren Amamiya (Joker)','Persona 5',6500,C),
(333,M_,PM,'superman','Superman','DC Comics',6474,C),
(333,GN,'personnage (homme ou femme au choix du joueur)','robin_(fire_emblem)','Robin (avatar de Fire Emblem Awakening)','Fire Emblem',6456,C),
(333,F_,PF,'ashe_(overwatch)','Ashe','Overwatch',6446,C),
(334,F_,PF,'tristana','Tristana','League of Legends',6442,C),
(334,ES,ES,'zangoose','Mangriff / Zangoose (espèce Pokémon)','Pokémon',6439,C),
(334,F_,PF,'marinette_dupain-cheng','Marinette Dupain-Cheng (Ladybug)','Miraculous',6437,C),
(334,F_,PF,'amity_blight','Amity Blight','Luz à Osville (The Owl House)',6411,C),
(335,ES,ES,'deathclaw','Deathclaw (espèce, Fallout)','Fallout',6406,C),
(335,F_,PF,'anna_(frozen)','Anna','La Reine des neiges',6383,C),
(335,F_,PF,'lois_griffin','Lois Griffin','Les Griffin (Family Guy)',6381,C),
(336,M_,PM,"wolf_o'donnell","Wolf O'Donnell",'Star Fox',6360,C),
(336,F_,PF,'bridget','Bridget','Guilty Gear',6349,CA),
(336,F_,PF,'hyuuga_hanabi','Hanabi Hyūga','Naruto',6341,CA),
(336,ES,ES,'guilmon','Guilmon (espèce Digimon)','Digimon',6338,C),
(337,F_,PF,'honoka_(doa)','Honoka','Dead or Alive',6332,CA),
(337,DB,DB,'marin_kitagawa','Marin Kitagawa (2e tag, déjà dans l’union : ≈ 945 publications sans kitagawa_marin, gain de 924 déjà compté)','My Dress-Up Darling',6327,C),
(338,F_,PF,'sakura_futaba','Futaba Sakura','Persona 5',6319,C),
(338,DB,DB,'yaoyorozu_momo','Momo Yaoyorozu (2e tag, déjà dans l’union : ≈ 189 publications sans momo_yaoyorozu, gain de 168 déjà compté)','My Hero Academia',6294,C),
(339,DB,DB,'saber','Saber (tag de classe de Fate ; ≈ 861 publications sans artoria_pendragon, non additionnées car le tag couvre aussi d’autres Servants Saber)','Fate',6291,CA),
(339,F_,PF,'ragatha_(the_amazing_digital_circus)','Ragatha','The Amazing Digital Circus',6289,C),
(339,M_,PM,'ganondorf','Ganondorf','The Legend of Zelda',6286,C),
(339,F_,PF,'queen_marika_the_eternal','Reine Marika l’Éternelle','Elden Ring',6277,C),
(340,F_,PF,'hoshimi_miyabi','Miyabi Hoshimi','Zenless Zone Zero',6264,CA),
]
assert len(T)==25
with open(D+'tags_personnages_pages_331-340.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['page','groupe','nature','tag','personnage','univers','publications','type_site','date_releve','source'])
    for t in T: w.writerow(list(t)+[DATE,SRC])
# Gains d'union mesurés par recherche négative (dernier pid + 21, ±21), 25/10/2026 ; retenus si > 150 (journal : pids.txt)
G={
 'marinette_dupain-cheng':('( marinette_cheng ~ marinette_cheng_(pv) ~ marinette_dupain-cheng_(pv) ~ ladybug_(character) ) -marinette_dupain-cheng',0),
 'hyuuga_hanabi':('( hanabi_hyuuga ~ hinata_hanabi ) -hyuuga_hanabi',126),
 'ragatha_(the_amazing_digital_circus)':('( ragatha ~ ragatha_(tadc) ~ 3 tags de tenue ) -ragatha_(the_amazing_digital_circus)',0),
 'amity_blight':('amity_blight_(beta) -amity_blight',0),
 'bridget':('bridget_(guilty_gear) -bridget',None),
 'sakura_futaba':('( 4 tags de tenue sakura_futaba_(…) ) -sakura_futaba',0),
}
NM={'ayane_(doa)':'variantes de la même personne : aucune (les autres ayane_ sont d’autres personnages)','ashe_(overwatch)':'variantes : ≤ 53 (autocomplétion)',
    'tristana':'variantes : ≤ 38 (autocomplétion)','anna_(frozen)':'aucune variante trouvée (autocomplétion)','lois_griffin':'aucune variante trouvée (autocomplétion)',
    'honoka_(doa)':'variantes : ≤ 102 (autocomplétion)','queen_marika_the_eternal':'variantes : ≤ 46 hors cosplay (autocomplétion)','hoshimi_miyabi':'variantes : ≤ 30 (autocomplétion)'}
new=[t for t in T if t[1]==F_]; assert len(new)==14
# 1) sélection non dédupliquée : 292 + 14
sel=list(csv.DictReader(open(B+'selection_292_personnages_feminins_2026-10-24.csv',encoding='utf-8-sig')))
assert len(sel)==292
for i,t in enumerate(new):
    sel.append({'rang':str(293+i),'personnage':t[4],'univers':t[5],'tag':t[3],'publications':str(t[6]),'date_releve':DATE,'source':SRC})
with open(B+'selection_306_personnages_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(sel[0].keys())); w.writeheader(); w.writerows(sel)
# 2) sélection dédupliquée (audit, méthode A) : 293 + 14
dd=list(csv.DictReader(open(B+'doublons/selection_293_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig')))
assert len(dd)==293
for i,t in enumerate(new):
    gain=0; mes=NM.get(t[3],'')
    if t[3] in G:
        q,pid=G[t[3]]
        if pid is None: mes=f"{q} = 0"
        else:
            g=pid+21; mes=f"{q} ≈ {g}"
            if g>150: gain=g; mes=q
            else: mes+=' (≤ 150)'
    dd.append({'rang_dedup':'','effet_dedup':'','rang_tag_seul_24_10':'','rang':str(293+i),'personnage':t[4],'univers':t[5],'tag':t[3],
               'publications':str(t[6]),'tag_seul_24_10':str(t[6]),'gain_dedup':str(gain),'publications_dedup':str(t[6]+gain),
               'methode':'tag + gain d’union (> 150)' if gain else 'tag seul','mesure_gain':mes,'date_releve':DATE,'source':SRC})
ts=sorted([r for r in dd if r['rang']!='—'],key=lambda r:-int(r['tag_seul_24_10']))
rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['rang']=='—': r['effet_dedup']='ajout'; r['rang_tag_seul_24_10']=''
    else: r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
assert len(dd)==307
with open(B+'doublons/selection_307_dedupliquee_audit_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
# 3) autres tags : 212 + 11
au=list(csv.DictReader(open(B+'autres_tags_personnages_212_hors_feminins_2026-10-24.csv',encoding='utf-8-sig')))
assert len(au)==212
for t in T:
    if t[1]!=F_:
        au.append({'groupe':t[1],'nature':t[2],'tag':t[3],'personnage':t[4],'univers':t[5],'publications':str(t[6]),'type_site':t[7],'date_releve':DATE,'source':SRC})
assert len(au)==223
with open(B+'autres_tags_personnages_223_hors_feminins_2026-10-25.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(au[0].keys())); w.writeheader(); w.writerows(au)
print(Counter(t[1] for t in T))
for r in dd:
    if r['source']==SRC: print(r['rang_dedup'],r['effet_dedup'],r['personnage'],r['publications_dedup'],r['methode'],'|',r['mesure_gain'][:70])
print('seuil (dernier) :',dd[-1]['personnage'],dd[-1]['publications_dedup'])
