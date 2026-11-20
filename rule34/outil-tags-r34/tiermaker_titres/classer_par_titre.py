# Classement TierMaker refait par groupe de titres (titre de l'événement live vu par les votants).
# Utilise la fonction agreg() de l'app (même indice de consensus que l'onglet Analyse), via Playwright.
import os, json, csv
from scipy.stats import spearmanr
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/tmp/pw')
from playwright.sync_api import sync_playwright
APP = '/home/user/outil_tags_r34/app_tiermaker/top100_tiermaker_rule34.html'
G = {
 'attirance': ['87784832','5058287','8447367','88691896','91860172','30083716','20899730','436045'],  # « Hottest… », « Hotties »
 'waifu':     ['81614596','80408816','30081640','99761754'],                                          # « …Waifu… »
 'neutre':    ['73568440'],                                                                           # « Ranking Female Video Game Characters »
}
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(); pg.goto('file://' + APP); pg.wait_for_timeout(1500)
    titres = pg.evaluate("D.listes.map(l=>[l.id,l.titre,l.modele,l.participants])")
    res = {k: pg.evaluate("ids=>agreg(false,ids).map(c=>({nom:c.nom,tag:c.tag,medium:c.medium,ix:c.ix,rc:c.rc,pres:c.pres,nel:c.nel,rk:c.rk}))", v) for k, v in G.items()}
    res['tous'] = pg.evaluate("ids=>agreg(false,ids).map(c=>({nom:c.nom,tag:c.tag,medium:c.medium,ix:c.ix,rc:c.rc,pres:c.pres,nel:c.nel,rk:c.rk}))", sum(G.values(), []))
    b.close()
for t in titres: print(t)
out = '/home/user/outil_tags_r34/tiermaker_titres/'
json.dump(res, open(out + 'brut_groupes_titres_2026-10-25.json', 'w'), ensure_ascii=False)
for k, C in res.items():
    print(f'\n== {k} : {len(C)} personnages ; top 20')
    for c in C[:20]: print(f"  {c['rc']:3d} {c['nom'][:28]:28s} {c['medium']:10s} ix {c['ix']:.1f}  {c['pres']}/{c['nel']}")
# comparaison attirance vs waifu sur les personnages éligibles dans les deux groupes (nel>=1 de chaque côté et présents au moins une fois)
A = {c['tag'] or c['nom']: c for c in res['attirance']}; W = {c['tag'] or c['nom']: c for c in res['waifu']}
com = [k for k in A if k in W and (A[k]['pres'] or W[k]['pres'])]
print('\nCommuns attirance/waifu :', len(com), 'ρ indices', spearmanr([A[k]['ix'] for k in com], [W[k]['ix'] for k in com]))
# paire au même périmètre (tous médiums) : 87784832 « HOTTEST WOMEN IN FICTION? » vs 80408816 « Waifu anime and cartoon »
T = res['tous']
both = [c for c in T if '87784832' in c['rk'] and '80408816' in c['rk'] and c['rk']['87784832'] is not None and c['rk']['80408816'] is not None]
print('Présents dans les 2 top 100 tous médiums :', len(both), spearmanr([c['rk']['87784832'] for c in both], [c['rk']['80408816'] for c in both]))
for c in sorted(both, key=lambda c: c['rk']['87784832']): print('   ', c['nom'][:26], c['rk']['87784832'], c['rk']['80408816'])
only87 = [c['nom'] for c in T if (c['rk'].get('87784832') or 999) <= 30 and c['rk'].get('80408816') is None]
only80 = [c['nom'] for c in T if (c['rk'].get('80408816') or 999) <= 30 and c['rk'].get('87784832') is None]
print('Top 30 « hottest » absents du top 100 « waifu » :', only87)
print('Top 30 « waifu » absents du top 100 « hottest » :', only80)
# CSV : rang par groupe
keys = list({(c['tag'] or c['nom']) for C in res.values() for c in C})
idx = {k: {(c['tag'] or c['nom']): c for c in C} for k, C in res.items()}
rows = []
for key in keys:
    base = next(idx[g][key] for g in ['tous','attirance','waifu','neutre'] if key in idx[g])
    r = dict(personnage=base['nom'], tag=base['tag'], medium=base['medium'])
    for g in ['tous','attirance','waifu','neutre']:
        c = idx[g].get(key); r[f'rang_{g}'] = c['rc'] if c else ''; r[f'indice_{g}'] = round(c['ix'], 1) if c else ''; r[f'presence_{g}'] = f"{c['pres']}/{c['nel']}" if c else ''
    rows.append(r)
rows.sort(key=lambda r: r['rang_tous'] if r['rang_tous'] != '' else 9999)
with open(out + 'classement_par_groupe_de_titres_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
