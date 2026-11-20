# Tableau DeviantArt vs rule34 sans IA (25/10/2026). Tag principal = nom complet collé (non ambigu) ; variantes non additionnées (doublons possibles).
import json, csv
from scipy.stats import spearmanr
R = json.load(open('brut_top15_tags_2026-10-25.json'))
S = {r['personnage']: int(r['sans_ia']) for r in csv.DictReader(open('../sans_ia/top_rule34_sans_ia_2026-10-25.csv', encoding='utf-8-sig'))}
P = {'Rouge the Bat': 'rougethebat', 'Tifa Lockhart': 'tifalockhart', 'Amy Rose': 'amyrose', 'Princesse Peach': 'princesspeach', 'Loona': 'loonahelluvaboss',
     'Chun-Li': 'chunli', '2B': '2b', 'Twilight Sparkle': 'twilightsparkle', 'Hatsune Miku': 'hatsunemiku', 'Nami': 'namionepiece', 'Lara Croft': 'laracroft',
     'Raven': 'raventeentitans', 'Samus Aran': 'samusaran', 'Princesse Zelda': 'princesszelda', 'D.Va': 'dva'}
AMB = {'tifa', 'nami', 'raven', 'zelda', 'samus'}
rows = []
for n, t in P.items():
    v = R[n + '|' + t]; num = 50000 if v == '≥50 000' else v
    autres = '; '.join(f"{k.split('|')[1]} {R[k]}" + (' (ambigu)' if k.split('|')[1] in AMB else '') for k in R if k.startswith(n + '|') and k != n + '|' + t)
    rows.append(dict(personnage=n, tag_principal=t, deviantart=v, num=num, rule34_sans_ia=S[n], da_pour_100_r34=round(num / S[n] * 100), autres_tags=autres))
rows.sort(key=lambda r: -r['num'])
for i, r in enumerate(rows, 1): r['rang_da'] = i
rs = sorted(rows, key=lambda r: -r['rule34_sans_ia'])
for i, r in enumerate(rs, 1): r['rang_r34_sans_ia'] = i
with open('deviantart_top15_vs_rule34_sans_ia_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, [k for k in rows[0] if k != 'num']); w.writeheader(); [w.writerow({k: v for k, v in r.items() if k != 'num'}) for r in rows]
for r in rows: print(r['rang_da'], r['personnage'], r['deviantart'], r['rule34_sans_ia'], r['rang_r34_sans_ia'], r['da_pour_100_r34'])
print(spearmanr([r['num'] for r in rows], [r['rule34_sans_ia'] for r in rows]))
