# Tags de franchise pour les franchises apparues avec le relevé 361-390 (25/10/2026).
# rule34 : liste des tags (recherche par nom exact, type Copyright vérifié) ; Danbooru : API tags.json (post_count, catégorie 3).
# À relancer APRÈS choisir_tags.py et les ajout_releve_311-330 / 331-340 / 341-360 (choisir_tags.py réécrit le CSV).
import csv
P='/home/user/outil_tags_r34/franchises/tags_franchise/tags_franchise_2026-10-24.csv'
L='liste des tags (tag principal, type Copyright)'; D='API tags.json (post_count)'
NEW=[('rule34','Akame ga Kill!','akame_ga_kill!',8273,L,'akame_ga_kill : 139'),
('rule34','Dragons (DreamWorks)','how_to_train_your_dragon',11224,L,'how_to_train_your_dragon_2 : 2087'),
('rule34','Final Fight','final_fight',6907,L,''),
('rule34','Gintama','gintama',11742,L,''),
('rule34','Gravity Falls','gravity_falls',14265,L,''),
('rule34','Haydee','haydee_(game)',5086,L,''),
('rule34','Kaguya-sama: Love is War','kaguya-sama_wa_kokurasetai_~tensai-tachi_no_renai_zunousen~',14532,'liste des tags (tag principal, type Copyright, ambiguous)','kaguya-sama_love_is_war : 28'),
('rule34','Kung Fu Panda','kung_fu_panda',7888,L,'kung_fu_panda_4 : 312'),
('rule34','La Petite Sirène (Disney)','the_little_mermaid',6269,L,'the_little_mermaid_(1989_film) : 3329'),
('rule34','Le Laboratoire de Dexter',"dexter's_laboratory",6981,"autocomplétion (type non vérifiable : la liste des tags ne trouve pas les noms avec apostrophe)",''),
('rule34','Les Tortues Ninja','teenage_mutant_ninja_turtles',11810,L,'tmnt_1987 : 3520 ; tmnt : 2190'),
('rule34','Raiponce (Disney)','tangled',7447,L,'tangled:_the_series : 1262'),
('rule34','Roshidere','tokidoki_bosotto_russian_de_dereru_tonari_no_alya-san',7000,L,'roshidere : 487'),
('rule34','Summertime Saga','summertime_saga',10612,'liste des tags (tag principal, type Copyright, ambiguous)',''),
('rule34','Team Fortress 2','team_fortress_2',19977,L,''),
('rule34','Trials of Mana (Seiken Densetsu 3)','seiken_densetsu_3',5944,L,'trials_of_mana : 1095'),
('rule34','Warcraft','warcraft',85711,L,'world_of_warcraft : 112098 (tag du jeu, plus gros que celui de la licence)'),
('danbooru','Code Geass','code_geass',15173,D,''),
('danbooru','Fatal Fury / King of Fighters','fatal_fury',8101,D,'the_king_of_fighters : 16982'),
('danbooru','Gloutons et Dragons (Dungeon Meshi)','dungeon_meshi',14879,D,''),
('danbooru','Nijisanji (VTubers)','nijisanji',93579,D,''),
('danbooru','Nikki (Infinity Nikki)','nikki_(series)',13128,D,'infinity_nikki : 6564'),
('danbooru','Sword Art Online','sword_art_online',19375,D,''),
('danbooru','Wuthering Waves','wuthering_waves',59614,D,'')]
rows=list(csv.DictReader(open(P,encoding='utf-8-sig')))
have={(r['site'],r['franchise']) for r in rows}
add=[dict(zip(['site','franchise','tag','publications','methode','autres_tags'],x)) for x in NEW if (x[0],x[1]) not in have]
with open(P,'w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,list(rows[0].keys())); w.writeheader(); w.writerows(rows+add)
print(len(add),'ajoutées ;',len(rows)+len(add),'lignes')
