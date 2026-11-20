import csv
rows=list(csv.DictReader(open('classement_r34_par_medium_2026-10-23.csv',encoding='utf-8-sig')))
order=['Animanga','Jeux vidéo','Comics',"Cartoons / films d'animation occidentaux",'Furry','Hors des 4 médiums']
tot=sum(int(r['publications']) for r in rows)
L=["# Classement rule34 par médium : personnages féminins","",
"*Relevé du 23 octobre 2026. Base : les 172 personnages féminins de `selection_172_personnages_feminins_2026-10-23.csv`, relevés dans la liste des tags rule34.xxx jusqu'à la page 250 (environ 9 600 publications au minimum). Les compteurs sont ceux de `comparaison_sites_195_personnages_2026-10-23.csv`, mis à jour le 23 octobre.*","",
"**Règle de classement :** chaque personnage est rangé selon le médium où il a été créé. C'est généralement celui de sa franchise ; quand ce n'est pas le cas, c'est indiqué dans la colonne Note. L'Animanga regroupe le manga, l'anime et les light novels.","","**Furry :** ce classement est séparé des autres. Les personnages qui y figurent sont retirés de leur médium d'origine, qui reste indiqué dans la colonne Note. Deux critères sont exigés : (1) le personnage est un animal anthropomorphe ou une créature animale (y compris les poneys de My Little Pony, les animatroniques animaux de Five Nights at Freddy's et les insectes de Hollow Knight) ; (2) son indice e621 est d'au moins 2. L'indice e621 compare la part du personnage sur e621, le booru spécialisé furry, à sa part sur rule34. Les indices observés présentent un écart net : les 22 personnages retenus sont entre 2,33 et 8,02, tous les autres sont à 1,45 ou moins. Seule exception, Midna (indice 2,74) n'est pas un animal ; elle reste en jeux vidéo. Les personnages humains à oreilles animales (Ahri, Miruko, Blake…) ne sont pas comptés comme furry.","",
"## Synthèse","","| Médium | Personnages | Publications cumulées | Part | Moyenne par personnage |","|---|---|---|---|---|"]
fmt=lambda n:f"{n:,}".replace(',',' ')
for m in order:
    g=[r for r in rows if r['medium']==m]; s=sum(int(r['publications']) for r in g)
    L.append(f"| {m} | {len(g)} | {fmt(s)} | {s/tot*100:.1f} % | {fmt(round(s/len(g)))} |")
L.append(f"| **Total** | **{len(rows)}** | **{fmt(tot)}** | 100 % | |")
for m in order:
    g=[r for r in rows if r['medium']==m]
    L+=["",f"## {m} ({len(g)})","","| # | Rang général (sur 172) | Personnage | Œuvre | Publications | Note |","|---|---|---|---|---|---|"]
    for r in g: L.append(f"| {r['rang_medium']} | {r['rang_general_172']} | {r['personnage']} | {r['univers']} | {fmt(int(r['publications']))} | {r['note']} |")
open('classement_r34_par_medium_2026-10-23.md','w').write('\n'.join(L)+'\n')
print('\n'.join(L[:20]))
