"""Doublons r34 : effectif dédupliqué par recherche OU ( a ~ b ), relevé 24/10/2026.
Effectif union = dernier pid + 21 (la dernière page contient 1 à 42 posts → ±21).
Tag principal = autocomplete du même jour (api.rule34.xxx/autocomplete.php).
Usage : python3 unions.py   (depuis outil_tags_r34/doublons/)"""
import csv
ac = dict(l.rstrip('\n').split('\t') for l in open('autocomplete_2026-10-24.tsv', encoding='utf-8'))
pid = {}
for l in open('pids_unions_2026-10-24.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    q, p = l.rstrip('\n').split('\t'); pid[q] = int(p)

sel = list(csv.DictReader(open('../selection_172_personnages_feminins_2026-10-23.csv', encoding='utf-8-sig')))
by_tag = {r['tag']: r for r in sel}
rows = []
for q, p in pid.items():
    tags = [t.strip() for t in q.split('~')]
    main = tags[0]
    union = p + 21
    m = int(ac[main])
    others = {t: int(ac[t]) for t in tags[1:]}
    somme = m + sum(others.values())
    gain = union - m
    r = by_tag.get(main)
    rows.append(dict(
        personnage=r['personnage'] if r else ('Psylocke' if main == 'psylocke' else main),
        univers=r['univers'] if r else 'Marvel',
        rang_ancien=r['rang'] if r else 'hors sélection',
        tags=' ∪ '.join(tags),
        tag_principal_seul=m,
        tags_secondaires_seuls='; '.join(f'{t}={c}' for t, c in others.items()),
        somme_brute=somme,
        union_dedupliquee=union,
        gain=gain,
        gain_pct=round(100 * gain / m, 1),
        recouvrement_pct=round(100 * (somme - union) / sum(others.values()), 0),
    ))
rows.sort(key=lambda x: -x['gain'])
with open('doublons_unions_2026-10-24.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

# Re-classement de la sélection 172 : tout au 24/10 (autocomplete du jour ; union OU pour les doublons)
ac172 = dict(l.rstrip('\n').split('\t') for l in open('autocomplete_172_2026-10-24.tsv', encoding='utf-8'))
uni = {r['tags'].split(' ∪ ')[0]: r['union_dedupliquee'] for r in rows}
new = []
for r in sel:
    today = int(ac172[r['tag']]) if ac172.get(r['tag'], 'NA') != 'NA' else int(r['publications'])
    c = uni.get(r['tag'], today)
    new.append(dict(r, tag_seul_24_10=today, publications_dedup=c,
                    methode='union OU' if r['tag'] in uni else ('tag seul' if ac172.get(r['tag'], 'NA') != 'NA' else 'tag seul (valeur du relevé, autocomplete muet)')))
for i, r in enumerate(sorted(new, key=lambda x: -x['tag_seul_24_10']), 1):  # 172 d'origine seulement
    r['rang_tag_seul_24_10'] = i
# Ajout : Psylocke (aucun de ses deux tags n'atteint seul le seuil du relevé ~9 640, l'union oui)
new.append(dict(rang='—', personnage='Psylocke (Betsy Braddock / Kwannon)', univers='Marvel', tag='psylocke ∪ psylocke_(kwannon)',
                publications='', tag_seul_24_10=int(ac['psylocke']), publications_dedup=uni['psylocke'],
                methode='union OU (ajout : absente du relevé par tag seul)', date_releve='2026-10-24', source='recherche OU'))
new.sort(key=lambda x: -x['publications_dedup'])
for i, r in enumerate(new, 1):
    r['rang_dedup'] = i
    r['effet_dedup'] = (r['rang_tag_seul_24_10'] - i) if 'rang_tag_seul_24_10' in r else 'ajout'
cols = ['rang_dedup', 'effet_dedup', 'rang_tag_seul_24_10', 'rang', 'personnage', 'univers', 'tag',
        'publications', 'tag_seul_24_10', 'publications_dedup', 'methode', 'date_releve', 'source']
with open('selection_173_dedupliquee_2026-10-24.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); w.writeheader(); w.writerows(new)
for r in rows:
    print(f"{r['personnage'][:22]:22} {r['tag_principal_seul']:>6} → {r['union_dedupliquee']:>6}  {r['gain']:+6} ({r['gain_pct']:>5}%)  recouvr {r['recouvrement_pct']}%")
print()
for r in new:
    if r['effet_dedup']:
        print(r['rang_dedup'], f"(dedup {r['effet_dedup']}; ancien rang {r['rang']})", r['personnage'], r['tag_seul_24_10'], '→', r['publications_dedup'])
