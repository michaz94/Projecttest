# Top rule34 hors images IA (25/10/2026). Requête : `<tag ou union> -ai_generated`, pid=50000 -> dernière page.
# Estimation = pid de la dernière page + 21 (pages de 42 ; précision ± 21). Total brut = compteur EdeniaList (liste des tags, 24-25/10).
import json, csv
A = {o['t']: o for o in json.load(open('/home/user/outil_tags_r34/app_tri/donnees_app_2026-10-24.json', encoding='utf-8'))}
# tag EdeniaList : (dernier pid sans IA, requête)
P = {'rouge_the_bat': (41496, 'tag'), 'tifa_lockhart': (38850, 'tag'), 'amy_rose': (37296, 'tag'), 'princess_peach': (36456, 'tag'),
     'loona_(helluva_boss)': (31836, 'tag'), 'chun-li': (30198, 'tag'), 'yorha_2b': (29064, 'tag'), 'twilight_sparkle_(mlp)': (28182, 'tag'),
     'hatsune_miku': (27762, 'tag'), 'nami_(one_piece)': (27510, 'tag'), 'lara_croft': (27426, 'tag'), 'raven_(dc)': (27132, 'tag'),
     'samus_aran': (26964, 'tag'), 'princess_zelda': (26166, 'union princess_zelda ~ zelda_(tears_of_the_kingdom) ~ zelda_(breath_of_the_wild)'),
     'd.va': (25998, 'tag'), 'widowmaker': (24906, 'tag'), 'sakura_haruno': (24486, 'tag'), 'mercy': (24234, 'tag'),
     'fluttershy_(mlp)': (23772, 'tag'), 'harley_quinn': (21000, 'union harley_quinn ~ harley_quinn_(classic) ~ harley_quinn_(injustice)'),
     'judy_hopps': (19698, 'tag'), 'ochako_uraraka': (19656, 'union ochako_uraraka ~ uraraka_ochako'), 'android_18': (18774, 'tag'),
     'nico_robin': (16884, 'tag'), 'miruko': (16842, 'union miruko ~ rumi_usagiyama ~ mirko'), 'ahri': (15792, 'tag'),
     'sonic_the_hedgehog': (32634, 'tag'), 'uzumaki_naruto': (27720, 'tag'), 'link': (26292, 'tag'), 'tails_the_fox': (25368, 'tag'),
     'aether_(genshin_impact)': (23268, 'tag'), 'izuku_midoriya': (18522, 'union izuku_midoriya ~ midoriya_izuku')}
rows = []
for t, (pid, q) in P.items():
    o = A[t]; n = pid + 21
    rows.append(dict(personnage=o['n'], sexe=o['s'], oeuvre=o['u'], medium=o['m'], tag=t, requete=q, sans_ia=n, total_app=o['r'],
                     part_ia_approx=round(max(0, 1 - n / o['r']) * 100) if q == 'tag' or o['g'] else '', rang_brut_F=''))
F = sorted([o for o in A.values() if o['s'] == 'F'], key=lambda o: -o['r']); rb = {o['t']: i for i, o in enumerate(F, 1)}
for r in rows: r['rang_brut_F'] = rb.get(r['tag'], '')
rows.sort(key=lambda r: -r['sans_ia'])
with open('/home/user/outil_tags_r34/sans_ia/top_rule34_sans_ia_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
k = 0
for r in rows:
    if r['sexe'] == 'F':
        k += 1; print(k, r['personnage'], r['sans_ia'], r['total_app'], r['part_ia_approx'], r['rang_brut_F'], r['medium'])
print('--- mixte')
for i, r in enumerate(rows[:18], 1): print(i, r['personnage'], r['sexe'], r['sans_ia'])
