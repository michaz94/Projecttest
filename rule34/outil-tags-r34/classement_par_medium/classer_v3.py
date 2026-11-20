# Classement par médium v3 (24/10/2026) : base = sélection dédupliquée 205 (pages 1-270), compteurs du 24/10.
import csv, json
from collections import defaultdict
B='/home/user/outil_tags_r34/'
src=open(B+'classement_par_medium/classer.py',encoding='utf-8').read()
# reprend U, EXC, NOTE, FURRY de la v2 sans relancer son calcul
ns={}; exec(src.split('out=[]')[0].replace("sel=list(","_sel=(").replace("cmp_={","_cmp={"),ns)
A,C,J,W,H,F=ns['A'],ns['C'],ns['J'],ns['W'],ns['H'],ns['F']
U=ns['U']; EXC=ns['EXC']; NOTE=ns['NOTE']; FURRY=set(ns['FURRY'])
cmp_={r['tag_r34']:r for r in csv.DictReader(open(B+'comparaison_sites_195_personnages_2026-10-23.csv',encoding='utf-8-sig'))}
U.update({"Sword Art Online":A,"Miss Kobayashi's Dragon Maid":A,"Cyberpunk: Edgerunners":A,"Honkai: Star Rail":J,"Deltarune":J,
          "Le Monde incroyable de Gumball":W,"Ring (roman et films)":H,"UTAU / Synthesizer V":H,"Dead or Alive":J,"Crash Bandicoot":J})
EXC["sally_acorn"]=(W,"créée pour la série animée Sonic le Rebelle (SatAM, 1993) et les comics Archie, absente des jeux d'origine")
# 24/10 : déplacées en dessins animés occidentaux à la demande de l'utilisateur (popularité rule34 surtout liée à la série 2003)
EXC["raven_(dc)"]=(W,"créée dans les comics (1980) ; déplacée ici à ta demande car sa popularité vient surtout de la série Teen Titans (2003) : 52 % de ses publications ont le tag purple_hair (look de la série), 2,5 % black_hair sans purple_hair")
EXC["starfire"]=(W,"créée dans les comics (1980) ; déplacée ici à ta demande comme Raven (série Teen Titans, 2003) ; tags de version : starfire_(teen_titans) 2 442, starfire_(comics) 1 773")
NOTE["rebecca_(edgerunners)"]="créée pour l'anime Cyberpunk: Edgerunners (2022), univers du jeu Cyberpunk 2077"
NOTE["bowsette"]="création de fans (2018) à partir de Super Mario ; indice e621 1,33 (bowsette_meme), personnage humanoïde"
NOTE["yamamura_sadako"]="roman de Kōji Suzuki (1991) puis films"
NOTE["kasane_teto"]="voix de synthèse UTAU (2008), comme Hatsune Miku pour Vocaloid"
# e621 des nouvelles candidates furry (24/10/2026, API tags.json) ; référence = 743 132 / 3 721 392
REF=743132/3721392
E621_NEW={"sally_acorn":7447,"nicole_watterson":8221,"susie_(deltarune)":9305,"coco_bandicoot":7078,"millie_(helluva_boss)":5190}
FURRY|=set(E621_NEW)|{"lamb_(league_of_legends)"}
sel=list(csv.DictReader(open(B+'doublons/selection_205_dedupliquee_2026-10-24.csv',encoding='utf-8-sig')))
out=[]
for r in sel:
    t=r['tag']; uni=r['univers']
    m=U[uni]; note=NOTE.get(t,'')
    if t in EXC: m,note=EXC[t]
    if uni=='Vocaloid': note="logiciel de synthèse vocale (mascotte), ni jeu ni anime à l'origine"
    if uni=='The Witcher': note="personnage des romans d'Andrzej Sapkowski ; classé en jeux vidéo à ta demande"
    mo=m; pub=int(r['publications_dedup'])
    if t in FURRY:
        m=F
        if t in cmp_: note=f"médium d'origine : {mo} ; e621 {int(cmp_[t]['e621'])} publications, indice e621 {cmp_[t]['indice_e621']}"
        elif t in E621_NEW:
            e=E621_NEW[t]; note=f"médium d'origine : {mo} ; e621 {e} publications, indice e621 {e/int(r['tag_seul_24_10'])/REF:.2f}"
        else: note=f"médium d'origine : {mo} ; pas de tag séparé sur e621, indice estimé à 3,08 via le tag commun kindred_(lol) (5 730)"
        if t=="millie_(helluva_boss)": note+=" ; diablotine (imp) et non animal : rangée en Furry comme Toriel, à confirmer"
    if r['methode'].startswith('union'): note=(note+' ; ' if note else '')+'compté par union de tags (doublons)'
    out.append(dict(medium=m,medium_origine=mo,personnage=r['personnage'],univers=uni,tag=t,publications=pub,note=note,date_releve='2026-10-24'))
assert len(out)==205
out.sort(key=lambda x:-x['publications'])
for i,o in enumerate(out,1): o['rang_general_205']=i
G=defaultdict(list)
for o in out: G[o['medium']].append(o)
rows=[]
for m in [A,J,C,W,F,H]:
    for i,o in enumerate(G[m],1): o['rang_medium']=i; rows.append(o)
cols=['medium','medium_origine','rang_medium','rang_general_205','personnage','univers','tag','publications','note','date_releve']
with open(B+'classement_par_medium/classement_r34_par_medium_2026-10-24.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,cols,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
# Markdown
fmt=lambda n:f"{n:,}".replace(',',' ')
order=[A,J,C,W,F,H]; tot=sum(o['publications'] for o in out)
L=["# Classement rule34 par médium : personnages féminins (v3)","",
"*Relevé du 24 octobre 2026. Base : les 205 personnages féminins de `doublons/selection_205_dedupliquee_2026-10-24.csv` (liste des tags rule34.xxx, pages 1 à 270, soit environ 8 650 publications au minimum). Tous les compteurs datent du 24/10 ; les personnages ayant plusieurs tags sont comptés par union (recherche OU), sans double comptage.*","",
"**Règle de classement :** chaque personnage est rangé selon le médium où il a été créé (exceptions indiquées en Note ; Raven et Starfire, créées dans les comics, sont rangées en dessins animés occidentaux à ta demande, pour la série Teen Titans de 2003). L'Animanga regroupe le manga, l'anime et les light novels.","",
"**Furry :** classement séparé ; ses personnages sont retirés de leur médium d'origine (indiqué en Note). Critères : (1) animal anthropomorphe ou créature animale ; (2) indice e621 d'au moins 2 (part sur e621 rapportée à la part sur rule34). Midna (2,74) et Bowsette restent hors Furry (personnages humanoïdes).","",
"## Synthèse","","| Médium | Personnages | Publications cumulées | Part | Moyenne par personnage |","|---|---|---|---|---|"]
for m in order:
    g=G[m]; s=sum(o['publications'] for o in g)
    L.append(f"| {m} | {len(g)} | {fmt(s)} | {s/tot*100:.1f} % | {fmt(round(s/len(g)))} |")
L.append(f"| **Total** | **{len(out)}** | **{fmt(tot)}** | 100 % | |")
for m in order:
    L+=["",f"## {m} ({len(G[m])})","","| # | Rang général (sur 205) | Personnage | Œuvre | Publications | Note |","|---|---|---|---|---|---|"]
    for o in G[m]: L.append(f"| {o['rang_medium']} | {o['rang_general_205']} | {o['personnage']} | {o['univers']} | {fmt(o['publications'])} | {o['note']} |")
open(B+'classement_par_medium/classement_r34_par_medium_2026-10-24.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
for m in order:
    s=sum(o['publications'] for o in G[m]); print(f"## {m} : {len(G[m])} / {s}")
    for o in G[m][:12]: print(o['rang_medium'],o['rang_general_205'],o['personnage'],'|',o['univers'],o['publications'])
