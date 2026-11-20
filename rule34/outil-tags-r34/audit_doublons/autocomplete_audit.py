"""Audit systématique des doublons de la sélection 205 (24/10/2026).
Pour chaque personnage : autocomplete rule34 (api.rule34.xxx) sur le tag principal, sa base (avant « _( »),
l'ordre inversé des noms (a_b -> b_a) et le premier mot + « _ ». Résultat brut : autocomplete_audit_2026-10-24.json"""
import csv, json, time, urllib.parse, urllib.request, re, os
B = '/home/user/outil_tags_r34/'
sel = list(csv.DictReader(open(B + 'doublons/selection_205_dedupliquee_2026-10-24.csv', encoding='utf-8-sig')))
OUT = B + 'audit_doublons/autocomplete_audit_2026-10-24.json'
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
def ac(q):
    u = 'https://api.rule34.xxx/autocomplete.php?q=' + urllib.parse.quote(q)
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    for _ in range(3):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=20).read().decode())
        except Exception as e:
            time.sleep(2)
    return None
qs = set()
for r in sel:
    t = r['tag'].split(' ∪ ')[0].strip()
    base = re.sub(r'_\(.*$', '', t)
    toks = base.split('_')
    qs |= {t, base}
    if len(toks) == 2: qs.add(toks[1] + '_' + toks[0])
    if len(toks) >= 2 and len(toks[0]) >= 3: qs.add(toks[0] + '_')
    if len(toks) >= 2 and len(toks[-1]) >= 4: qs.add(toks[-1] + '_')
qs = sorted(qs)
print(len(qs), 'requêtes', flush=True)
for i, q in enumerate(qs):
    if q in res and res[q] is not None: continue
    res[q] = ac(q); time.sleep(0.3)
    if i % 50 == 0:
        json.dump(res, open(OUT, 'w'), ensure_ascii=False); print(i, flush=True)
json.dump(res, open(OUT, 'w'), ensure_ascii=False); print('fini', flush=True)
