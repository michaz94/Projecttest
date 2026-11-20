# Comparaison des 33 personnages féminins du top 100 des favoris MyAnimeList (25/10/2026)
# avec : rule34 (publications), Danbooru (images) et les votes TierMaker qui contiennent des personnages d'anime.
# Sources :
#  - MAL : app_tri/donnees_mal_2026-10-25.json (relevé du 25/10).
#  - rule34 / Danbooru : compteurs d'EdeniaList quand le personnage y est (sélection Rule34 auditée, Top Danbooru) ;
#    sinon relevés le 25/10 pour cette comparaison (rule34 : autocomplétion ou liste des tags, tag principal seul, doublons
#    non audités ; Danbooru : API tags.json). Pas de compteur rule34 demandé pour les collégiennes de 14 ans
#    (Yuno Gasai, Kaori Miyazono). Homura Akemi et Shinobu Oshino : compteurs déjà présents dans EdeniaList (Top Danbooru).
#  - TierMaker : top 100 « Average Vote » identifié de chaque vote (app_tiermaker/top100_tiermaker_rule34.html) ;
#    les images non identifiées et les rangs au-delà du top 100 ne sont pas connus.
import json, csv, statistics
from scipy.stats import spearmanr
B = '/home/user/outil_tags_r34/'
MAL = [o for o in json.load(open(B + 'app_tri/donnees_mal_2026-10-25.json', encoding='utf-8')) if o['s'] == 'F']
assert len(MAL) == 33
# rang MAL : (tag rule34, publications rule34 ou None, images Danbooru, remarque) pour les 13 absentes d'EdeniaList
NEW = {14: ('makise_kurisu', 1760, 4407, 'kurisu_makise : 8 (non additionné)'),
       27: ('senjougahara_hitagi', 1390, 3466, ''),
       29: ('sakurajima_mai', 2257, 1511, 'mai_sakurajima : 125 (non additionné)'),
       30: ('violet_evergarden_(character)', 890, 1227, "violet_evergarden : 1 002 (tag ambigu personnage / série, non additionné)"),
       45: ('aisaka_taiga', 499, 3510, 'taiga_aisaka : 91 (non additionné)'),
       54: ('gasai_yuno', None, 820, 'collégienne de 14 ans : pas de compteur rule34 demandé'),
       55: ('holo', 4443, 4557, 'holo_(spice_and_wolf) : 866 (non additionné)'),
       65: ('maomao_(kusuriya_no_hitorigoto)', 3488, 2210, ''),
       67: ('miyazono_kaori', None, 411, "collégienne de 14 ans : pas de compteur rule34 demandé ; Danbooru : miyazono_kaori est un alias de miyazono_kawori (411)"),
       77: ('yukinoshita_yukino', 1679, 2130, ''),
       80: ('tokisaki_kurumi', 3447, 2584, ''),
       81: ('revy', 4191, 1257, 'revy_(black_lagoon) : 638 (non additionné)'),
       100: ('takanashi_rikka', 608, 2440, '')}
h = open(B + 'app_tiermaker/top100_tiermaker_rule34.html', encoding='utf-8').read()
i = h.index('const D=') + 8
TD, _ = json.JSONDecoder().raw_decode(h[i:])
VOTES = [('99761754', 'Best Anime Waifus 2025', '311 images, 100 % anime'),
         ('30081640', 'The Anime Waifu Tier List', '2 050 images, anime/manga'),
         ('87784832', 'Ultimate Fictional Animated Women', '1 310 images, tous dessins animés'),
         ('80408816', 'Waifus Anime, Cartoon and Videogames', '381 images, tous médiums'),
         ('436045', 'Cartoon Hotties', '295 images, environ un tiers d\u2019anime')]
TM = {}
for L in TD['listes']:
    best = {}
    for r in L['rows']:
        if r['tag'] and not r.get('extra') and (r['tag'] not in best or r['tm'] < best[r['tag']]): best[r['tag']] = r['tm']
    TM[L['id']] = best
# alias de tags entre EdeniaList et les identifications TierMaker
ALIAS = {'violet_evergarden_(character)': 'violet_evergarden_(character)', 'sakurajima_mai': 'sakurajima_mai'}
rows = []
for o in MAL:
    if o['r'] in NEW:
        t, r34, db, rq = NEW[o['r']]; src = 'relevé du 25/10 (tag seul)' if r34 is not None else ''
    else:
        t, r34, db, rq = o['t'], o['r34'], o['db'], ''
        src = {'r': 'EdeniaList, sélection Rule34 (auditée)', 'd': 'EdeniaList, Top Danbooru (non audité)'}[o['lk']]
    x = dict(rang_mal=o['r'], rang_mal_filles=0, personnage=o['n'], oeuvre=o['u'], favoris_mal=o['f'], tag_rule34=t,
             rule34=r34, danbooru=db, danbooru_pour_100_rule34=round(db / r34 * 100, 1) if r34 and db else '', source=src, remarque=rq)
    for e, _, _ in VOTES: x['tm_' + e] = TM[e].get(t, '')
    rows.append(x)
for k, x in enumerate(rows, 1): x['rang_mal_filles'] = k
def rang(key):
    v = sorted([x for x in rows if isinstance(x[key], int) and x[key] > 0], key=lambda x: -x[key])
    for k, x in enumerate(v, 1): x['rang_' + key] = k
rang('rule34'); rang('danbooru')
cols = list(rows[0].keys()) + ['rang_rule34', 'rang_danbooru']
with open(B + 'myanimelist/comparaison_feminines_mal_r34_danbooru_tiermaker_2026-10-25.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, cols, restval=''); w.writeheader(); w.writerows(rows)
# corrélations (Spearman) entre favoris MAL et chaque mesure, sur les personnages qui ont la mesure
def sp(key, inv=False):
    v = [x for x in rows if isinstance(x[key], int) and x[key] > 0]
    if len(v) < 5: return None
    r = spearmanr([x['favoris_mal'] for x in v], [(-x[key] if inv else x[key]) for x in v])
    return round(r.statistic, 2), round(r.pvalue, 3), len(v)
res = {'rule34': sp('rule34'), 'danbooru': sp('danbooru')}
for e, _, _ in VOTES: res['tm_' + e] = sp('tm_' + e, inv=True)
print(res)
for x in rows:
    print(x['rang_mal_filles'], x['personnage'], x['favoris_mal'], x['rule34'], x.get('rang_rule34', ''), x['danbooru'], x.get('rang_danbooru', ''), x['danbooru_pour_100_rule34'], [x['tm_' + e] for e, _, _ in VOTES])
json.dump(dict(rows=rows, cor=res, votes=VOTES), open('/tmp/cmp_mal.json', 'w'), ensure_ascii=False)
