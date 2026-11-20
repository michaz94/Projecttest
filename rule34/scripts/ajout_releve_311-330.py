# Tags de franchise pour les 14 franchises apparues avec le relevé 311-330 (24/10/2026).
# rule34 : autocomplétion api.rule34.xxx ; Danbooru : API tags.json (post_count). À relancer APRÈS choisir_tags.py (qui réécrit le CSV).
import csv
P='/home/user/outil_tags_r34/franchises/tags_franchise/tags_franchise_2026-10-24.csv'
A='autocomplétion (tag principal)'; D='API tags.json (post_count)'
NEW=[('rule34','Bayonetta','bayonetta',7435,A,'bayonetta_(series) : 399 ; bayonetta_2 : 2993 ; bayonetta_3 : 1149'),
('rule34','Fortnite','fortnite',128371,A,'fortnite:_battle_royale : 50511'),
('rule34','Foster, la maison des amis imaginaires',"foster's_home_for_imaginary_friends",7343,A,''),
('rule34','Gurren Lagann','tengen_toppa_gurren_lagann',8412,A,'gurren_lagann : 26'),
('rule34','Harry Potter','harry_potter',15186,A,'harry_potter_(series) : 1107'),
('rule34','Les Bad Guys','the_bad_guys',9802,A,'the_bad_guys_2 : 638'),
('rule34','Ma vie de robot ado','my_life_as_a_teenage_robot',8236,A,''),
('rule34','Mortal Kombat','mortal_kombat',28580,A,'mortal_kombat_11 : 8329 ; mortal_kombat_1_(2023) : 4877'),
('rule34','Steven Universe','steven_universe',36408,A,'steven_universe_future : 2333'),
('rule34','WarioWare','warioware',2115,A,'wario_(series) : 1032'),
('danbooru','Darkstalkers','darkstalkers',13503,D,''),
('danbooru','Project Moon (Limbus Company)','project_moon',51897,D,'limbus_company : 38984'),
('danbooru','Sailor Moon','bishoujo_senshi_sailor_moon',19680,D,''),
('danbooru','Tsukihime','tsukihime',16861,D,'')]
rows=list(csv.DictReader(open(P,encoding='utf-8-sig')))
have={(r['site'],r['franchise']) for r in rows}
add=[dict(zip(['site','franchise','tag','publications','methode','autres_tags'],x)) for x in NEW if (x[0],x[1]) not in have]
with open(P,'w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,list(rows[0].keys())); w.writeheader(); w.writerows(rows+add)
print(len(add),'ajoutées ;',len(rows)+len(add),'lignes')
