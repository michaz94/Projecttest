# Tags de franchise pour les franchises apparues avec le relevé 331-340 (25/10/2026).
# rule34 : liste des tags (recherche par nom avec joker, type Copyright vérifié) ; Danbooru : API tags.json (post_count).
# À relancer APRÈS choisir_tags.py puis ajout_releve_311-330.py (choisir_tags.py réécrit le CSV).
import csv
P='/home/user/outil_tags_r34/franchises/tags_franchise/tags_franchise_2026-10-24.csv'
L='liste des tags (tag principal, type Copyright)'; D='API tags.json (post_count)'
NEW=[('rule34','Miraculous','miraculous_ladybug',11615,L,'miraculous:_tales_of_ladybug_and_cat_noir : 5134'),
('rule34','Les Griffin (Family Guy)','family_guy',13233,L,''),
('rule34','Guilty Gear','guilty_gear',24780,L,'guilty_gear_strive : 11808 ; guilty_gear_xrd : 2149'),
('rule34','Elden Ring','elden_ring',28711,L,'elden_ring_nightreign : 3357'),
('danbooru','Monogatari','monogatari_(series)',21386,D,''),
('danbooru',"Girls' Frontline","girls'_frontline",81383,D,'')]
rows=list(csv.DictReader(open(P,encoding='utf-8-sig')))
have={(r['site'],r['franchise']) for r in rows}
add=[dict(zip(['site','franchise','tag','publications','methode','autres_tags'],x)) for x in NEW if (x[0],x[1]) not in have]
with open(P,'w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,list(rows[0].keys())); w.writeheader(); w.writerows(rows+add)
print(len(add),'ajoutées ;',len(rows)+len(add),'lignes')
