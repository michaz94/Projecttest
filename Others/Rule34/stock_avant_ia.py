# Effet du temps sur la part d'IA : stock publié avant le 18/11/2022 (id:<7000000, ancre vérifiée) vs part IA.
# Comptes = pid de la dernière page + 21 (± 21). Total = compteur EdeniaList (24-25/10) ; sans IA = relevé du 25/10 (Marin, Frieren : 24/10).
# Avant id 7 000 000, le site ne compte qu'environ 8 757 posts tagués ai_generated (dernier pid 8 736).
import csv
from scipy.stats import spearmanr
D = [  # personnage, médium, total, sans_ia, pid_avant_2022_11
 ('Rouge the Bat','Furry',45414,41517,17766),('Amy Rose','Furry',41846,37317,16632),('Twilight Sparkle','Furry',30892,28203,20706),
 ('Fluttershy','Furry',26448,23793,17346),('Loona','Furry',43049,31857,8568),('Judy Hopps','Furry',26160,19719,10920),
 ('Tifa Lockhart','Jeux vidéo',54505,38871,21714),('Princesse Peach','Jeux vidéo',50552,36477,16338),('Lara Croft','Jeux vidéo',32891,27447,14028),
 ('Chun-Li','Jeux vidéo',41013,30219,14532),('2B','Jeux vidéo',43048,29085,14616),('Samus Aran','Jeux vidéo',37248,26985,15918),
 ('D.Va','Jeux vidéo',35763,26019,13860),('Mercy','Jeux vidéo',30462,24255,14490),('Ahri','Jeux vidéo',29877,15813,10038),
 ('Hatsune Miku','Autres',41506,27783,9786),('Raven','Cartoons',39707,27153,13818),
 ('Nami','Animanga',58263,27531,13524),('Nico Robin','Animanga',35080,16905,8106),('Sakura Haruno','Animanga',40018,24507,15876),
 ('Ochako Uraraka','Animanga',35111,19677,8526),('Miruko','Animanga',31266,16863,5502),('C-18','Animanga',30868,18795,10584),
 ('Marin Kitagawa','Animanga',29857,9676,3108),('Frieren','Animanga',28757,10130,0)]
rows = []
for n, m, tot, sia, pid in D:
    av = pid + 21; ia = tot - sia; apres = tot - av
    rows.append(dict(personnage=n, medium=m, total=tot, sans_ia=sia, ia=ia, part_ia=round(ia/tot*100), avant_nov2022=av,
                     part_avant=round(av/tot*100), humain_depuis=sia-av, part_ia_depuis_nov2022=round(ia/apres*100)))
rows.sort(key=lambda r: r['part_ia'])
with open('/home/user/outil_tags_r34/sans_ia/stock_avant_ia_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
print('part_avant vs part_ia', spearmanr([r['part_avant'] for r in rows],[r['part_ia'] for r in rows]))
print('part_avant vs part_ia_depuis', spearmanr([r['part_avant'] for r in rows],[r['part_ia_depuis_nov2022'] for r in rows]))
import statistics as st
for m in ['Furry','Jeux vidéo','Animanga']:
    x=[r for r in rows if r['medium']==m]; print(m, 'méd part_ia', st.median([r['part_ia'] for r in x]), 'méd part_avant', st.median([r['part_avant'] for r in x]), 'méd ia_depuis', st.median([r['part_ia_depuis_nov2022'] for r in x]))
