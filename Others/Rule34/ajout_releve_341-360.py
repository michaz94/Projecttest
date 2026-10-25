# Tags de franchise pour les franchises apparues avec le relevé 341-360 (25/10/2026).
# rule34 : liste des tags (recherche par nom exact, type Copyright vérifié) ; Danbooru : API tags.json (post_count, catégorie 3).
# À relancer APRÈS choisir_tags.py, ajout_releve_311-330.py et ajout_releve_331-340.py (choisir_tags.py réécrit le CSV).
import csv
P='/home/user/outil_tags_r34/franchises/tags_franchise/tags_franchise_2026-10-24.csv'
L='liste des tags (tag principal, type Copyright)'; D='API tags.json (post_count)'
NEW=[('rule34','Azur Lane','azur_lane',75216,L,''),
('rule34','Code Geass','code_geass',14511,L,'code_geass:oz_the_reflection : 140'),
('rule34','DanMachi','dungeon_ni_deai_wo_motomeru_no_wa_machigatteiru_darou_ka',11683,L,'danmachi : 1179'),
('rule34','Gameoverse','gameoverse',6629,L,''),
('rule34','Life is Strange','life_is_strange',11710,L,'life_is_strange:_true_colors : 1032 ; life_is_strange:_double_exposure : 682'),
('rule34','Mushoku Tensei','mushoku_tensei',19302,L,'mushoku_tensei:_isekai_ittara_honki_dasu : 4949'),
('rule34','Ranma ½','ranma_1/2',9263,L,''),
('rule34','Soulcalibur','soul_calibur',14013,L,'soul_calibur_iv : 738 ; soul_calibur_vi : 714'),
('rule34','Star vs. les forces du mal','star_vs_the_forces_of_evil',14290,'liste des tags (tag principal, type Copyright, ambiguous)','star_vs._the_forces_of_evil : 53'),
('danbooru','Azur Lane','azur_lane',159242,D,''),
('danbooru','Lucky Star','lucky_star',14802,D,''),
('danbooru','My Dress-Up Darling','sono_bisque_doll_wa_koi_wo_suru',8182,D,''),
('danbooru','My Hero Academia','boku_no_hero_academia',45963,D,''),
('danbooru','Omori','omori',24604,D,'')]
rows=list(csv.DictReader(open(P,encoding='utf-8-sig')))
have={(r['site'],r['franchise']) for r in rows}
add=[dict(zip(['site','franchise','tag','publications','methode','autres_tags'],x)) for x in NEW if (x[0],x[1]) not in have]
with open(P,'w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,list(rows[0].keys())); w.writeheader(); w.writerows(rows+add)
print(len(add),'ajoutées ;',len(rows)+len(add),'lignes')
