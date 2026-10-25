# Parts par période sur rule34 pour le top 20 général TierMaker (onglet Analyse).
# Effectif cumulé à chaque borne = pid de la dernière page + 21 (± 21) ; total = compteur EdeniaList (23-25/10/2026).
# Taux = posts du personnage pour 1 million d'ID attribués pendant la période (approximation du volume du site :
# les posts supprimés gardent leur ID).
import csv
from scipy.stats import spearmanr
B = [0, 2_000_000, 7_000_000, 11_927_000, 19_130_000]
P = ['≤ mars 2016', 'avr. 2016 – nov. 2022', 'nov. 2022 – déc. 2024', 'déc. 2024 – oct. 2026']
# nom, origine, année de 1re apparition, pid<2M, pid<7M, pid<11,927M, total
D = [
 ('2B','Japon',2017,0,14616,26502,43048), ('Chel','Occident',2000,210,1848,4914,11392),
 ('Shego','Occident',2002,1512,2982,4620,7856), ('Starfire','Occident',1980,2226,7434,13104,21791),
 ('Raven','Occident',1980,2814,13818,24444,39707), ('Hélène Parr','Occident',2004,840,4410,9198,15935),
 ('Mirko','Japon',2019,None,5502,14238,31266), ('Chun-Li','Japon',1991,6804,14532,24948,41013),
 ('Tsunade','Japon',2001,2562,11760,21252,40786), ('D.Va','Occident',2016,42,13860,22218,35763),
 ('Fubuki','Japon',2012,126,2982,6300,14451), ('Jessica Rabbit','Occident',1988,2436,4578,6930,12174),
 ('Tifa','Japon',1997,6300,21714,34230,54505), ('Samus','Japon',1986,3486,15918,24528,37248),
 ('Yor','Japon',2019,None,3192,12306,32882), ('Marin','Japon',2018,None,3108,8862,29857),
 ('Kim Possible','Occident',2002,3654,5586,8190,12439), ('Nami','Japon',1997,4326,13524,28560,58263),
 ('Yoruichi','Japon',2003,1218,3990,9282,21936), ('Ada Wong','Japon',1998,630,5250,12390,23269)]
H = {'2B':6216,'Chel':1638,'Shego':588,'Starfire':2940,'Raven':5796,'Hélène Parr':2478,'Mirko':4578,'Chun-Li':7686,'Tsunade':3486,
     'D.Va':5418,'Fubuki':1428,'Jessica Rabbit':1092,'Tifa':8106,'Samus':5040,'Yor':2856,'Marin':3150,'Kim Possible':756,'Nami':6216,
     'Yoruichi':2688,'Ada Wong':6888}  # pid dernière page, tag -ai_generated id:>11927000
rows = []
for n, o, an, a, b, c, tot in D:
    cum = [0 if a is None else a + 21, b + 21, c + 21, tot]
    per = [cum[0]] + [cum[i] - cum[i-1] for i in range(1, 4)]
    taux = [per[i] / ((B[i+1] - B[i]) / 1e6) for i in range(4)]
    r = dict(personnage=n, origine=o, premiere_apparition=an, total=tot)
    for i in range(4):
        r[f'posts_{i+1}'] = per[i]; r[f'taux_{i+1}'] = round(taux[i])
    r['posts_4_sans_ia'] = H[n] + 21; r['part_ia_4'] = round((1 - (H[n] + 21) / per[3]) * 100)
    r['taux_4_sans_ia'] = round((H[n] + 21) / ((B[4] - B[3]) / 1e6))
    r['evolution_dernier_vs_precedent'] = round(taux[3] / taux[2], 2)
    r['part_du_total_depuis_dec2024'] = round(per[3] / tot * 100)
    rows.append(r)
for i in range(4):
    for k, r in enumerate(sorted(rows, key=lambda r: -r[f'taux_{i+1}'])): r[f'rang_{i+1}'] = k + 1
for k, r in enumerate(sorted(rows, key=lambda r: -r['taux_4_sans_ia'])): r['rang_4_sans_ia'] = k + 1
out = '/home/user/outil_tags_r34/temporalite/top20_general_parts_par_periode_2026-10-25.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print('Périodes:', P)
for r in sorted(rows, key=lambda r: r['rang_4']):
    print(f"{r['personnage']:15s} {r['origine']:9s} {r['premiere_apparition']}  taux " + ' / '.join(f"{r[f'taux_{i}']:5d}" for i in range(1,5)),
          '  rangs', [r[f'rang_{i}'] for i in range(1,5)], ' évol', r['evolution_dernier_vs_precedent'], ' %depuis déc24', r['part_du_total_depuis_dec2024'], ' P4 sans IA', r['taux_4_sans_ia'], 'rang', r['rang_4_sans_ia'], 'IA%', r['part_ia_4'])
for o in ['Occident', 'Japon']:
    x = [r for r in rows if r['origine'] == o]
    print(o, len(x), 'somme taux par période', [sum(r[f'taux_{i}'] for r in x) for i in range(1,5)],
          'part du groupe dans le top20 (%)', [round(100*sum(r[f'taux_{i}'] for r in x)/sum(r[f'taux_{i}'] for r in rows)) for i in range(1,5)])
    print('   part du groupe, P4 sans IA (%)', round(100*sum(r['taux_4_sans_ia'] for r in x)/sum(r['taux_4_sans_ia'] for r in rows)), ' IA% médian P4', sorted(r['part_ia_4'] for r in x)[len(x)//2])
# indice de consensus TierMaker vs taux par période
IX = {'2B':98.0,'Chel':93.6,'Shego':92.0,'Starfire':91.9,'Raven':91.7,'Hélène Parr':91.5,'Mirko':85.4,'Chun-Li':85.0,'Tsunade':83.2,'D.Va':82.3,
      'Fubuki':81.2,'Jessica Rabbit':79.7,'Tifa':78.8,'Samus':76.7,'Yor':76.6,'Marin':76.6,'Kim Possible':76.2,'Nami':75.8,'Yoruichi':75.8,'Ada Wong':75.0}
for i in range(1,5):
    print('ρ indice TM vs taux période', i, spearmanr([IX[r['personnage']] for r in rows], [r[f'taux_{i}'] for r in rows]))
print('ρ indice TM vs P4 sans IA', spearmanr([IX[r['personnage']] for r in rows], [r['taux_4_sans_ia'] for r in rows]))
print('ρ indice TM vs total cumulé', spearmanr([IX[r['personnage']] for r in rows], [r['total'] for r in rows]))
