# Classement des franchises les plus représentées dans la sélection des 388 personnages féminins (25/10/2026 ; mise à jour après les relevés des pages 281-390).
import csv,collections
B='/home/user/outil_tags_r34/'
r=list(csv.DictReader(open(B+'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv',encoding='utf-8-sig')))
assert len(r)==388
# regroupement des libellés d'une même franchise
N={'Sonic the Hedgehog':'Sonic','Resident Evil 4':'Resident Evil','Resident Evil Village':'Resident Evil',
   'Marvel (Les 4 Fantastiques)':'Marvel','Naruto / Boruto':'Naruto','Konosuba':'KonoSuba','One-Punch Man':'One Punch Man',
   'Neon Genesis Evangelion':'Evangelion','League of Legends / Arcane':'League of Legends',
   "Avatar, le dernier maître de l'air":'Avatar (Le Dernier Maître de l\'air + La Légende de Korra)',
   'La Légende de Korra':'Avatar (Le Dernier Maître de l\'air + La Légende de Korra)'}
MS={"Cartoons / films d'animation occidentaux":'Cartoons','Hors des 4 médiums':'Autres'}
G=collections.defaultdict(list)
for x in r:
    x['pub']=int(x['publications']); G[N.get(x['univers'],x['univers'])].append(x)
tot=sum(x['pub'] for x in r)
rows=[]
for f,L in G.items():
    L.sort(key=lambda x:-x['pub']); s=sum(x['pub'] for x in L)
    med=collections.Counter(MS.get(x['medium'],x['medium']) for x in L)
    rows.append(dict(franchise=f,personnages=len(L),publications=s,part=round(100*s/tot,1),moyenne=round(s/len(L)),
        mediums=' / '.join(f'{m} {n}' if len(med)>1 else m for m,n in med.most_common()),
        personnages_liste=', '.join(f"{x['personnage']} ({x['pub']:,})".replace(f"{x['pub']:,}",f"{x['pub']:,}".replace(',',' ')) for x in L)))
# rang par nombre de personnages (départage : publications) et rang par publications cumulées
rows.sort(key=lambda o:(-o['publications']))
for i,o in enumerate(rows,1): o['rang_publications']=i
rows.sort(key=lambda o:(-o['personnages'],-o['publications']))
for i,o in enumerate(rows,1): o['rang_personnages']=i
cols=['rang_personnages','rang_publications','franchise','personnages','publications','part','moyenne','mediums','personnages_liste']
with open(B+'franchises/classement_franchises_388_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as fo:
    w=csv.DictWriter(fo,cols); w.writeheader()
    for o in rows: w.writerow({**o,'part':str(o['part']).replace('.',',')})
fmt=lambda n:f"{n:,}".replace(',',' ')
L=["# Franchises les plus représentées (personnages féminins, rule34.xxx)","",
"*Relevés des 24 et 25 octobre 2026. Base : les 388 personnages féminins de `doublons/selection_388_dedupliquee_audit_2026-10-25.csv`, c'est-à-dire tous les tags de personnage féminin à au moins 5 011 publications (liste des tags, pages 1 à 390). Les publications incluent les gains d'union de l'audit des doublons.*","",
f"**{len(rows)} franchises** au total, dont {sum(1 for o in rows if o['personnages']==1)} avec un seul personnage.","",
"**Regroupements :** Sonic + Sonic the Hedgehog ; Resident Evil + RE4 + RE Village ; Naruto + Naruto / Boruto ; Avatar + La Légende de Korra (suite officielle) ; Marvel inclut la Femme invisible ; League of Legends inclut Jinx (Arcane). Gardées séparées : Hazbin Hotel et Helluva Boss (même univers de Vivziepop, mais séries distinctes) ; Undertale et Deltarune ; Vocaloid et UTAU. Marvel et DC sont des univers partagés qui regroupent beaucoup de séries.","",
"**Limite :** seules les filles sont comptées ; une franchise riche en personnages masculins populaires (Naruto, Genshin Impact…) est donc sous-représentée par rapport à son poids total. Pour le poids total d'une franchise (tous personnages et images sans personnage), voir le Top 20 des tags Copyright (`copyright/top20_franchises_rule34_2026-10-24.csv`).","",
"## 1. Par nombre de personnages","",
"Départage à égalité : publications cumulées.","",
"| # | Franchise | Personnages | Publications cumulées | Moyenne | Médium | Personnages (publications) |","|---|---|---|---|---|---|---|"]
for o in rows:
    if o['personnages']<2: continue
    L.append(f"| {o['rang_personnages']} | {o['franchise']} | {o['personnages']} | {fmt(o['publications'])} | {fmt(o['moyenne'])} | {o['mediums']} | {o['personnages_liste']} |")
L+=["",f"*Les {sum(1 for o in rows if o['personnages']==1)} franchises à un seul personnage figurent dans le CSV.*","","## 2. Par publications cumulées (top 30)","",
"| # | Franchise | Publications cumulées | Part des 388 | Personnages | Rang par nombre |","|---|---|---|---|---|---|"]
for o in sorted(rows,key=lambda o:o['rang_publications'])[:30]:
    L.append(f"| {o['rang_publications']} | {o['franchise']} | {fmt(o['publications'])} | {str(o['part']).replace('.',',')} % | {o['personnages']} | {o['rang_personnages']} |")
open(B+'franchises/classement_franchises_388_2026-10-25.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
for o in sorted(rows,key=lambda o:o['rang_publications'])[:30]: print(o['rang_publications'],o['rang_personnages'],o['franchise'],o['personnages'],o['publications'],o['part'])
print(len(rows),sum(1 for o in rows if o['personnages']==1))
