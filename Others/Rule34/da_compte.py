# Compte des œuvres d'un tag DeviantArt par recherche dichotomique sur l'offset de /browse/tags (pas de compteur fourni par l'API).
# Identifiants lus dans /tmp/da_cred.json (jamais écrits dans l'espace sauvegardé). Plafond de l'API : offset 50 000.
import json, sys, time, urllib.request, urllib.parse, gzip
UA = 'EdeniaResearch/1.0'
def token():
    c = json.load(open('/tmp/da_cred.json'))
    d = urllib.parse.urlencode(dict(grant_type='client_credentials', **c)).encode()
    r = urllib.request.Request('https://www.deviantart.com/oauth2/token', data=d, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip'})
    b = urllib.request.urlopen(r, timeout=30).read()
    try: b = gzip.decompress(b)
    except OSError: pass
    return json.loads(b)['access_token']
T = token()
def get(path, **p):
    u = 'https://www.deviantart.com/api/v1/oauth2/' + path + '?' + urllib.parse.urlencode(p)
    for i in range(5):
        try:
            r = urllib.request.Request(u, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip', 'Authorization': 'Bearer ' + T})
            b = urllib.request.urlopen(r, timeout=30).read()
            try: b = gzip.decompress(b)
            except OSError: pass
            time.sleep(0.4); return json.loads(b)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503): time.sleep(5 * (i + 1)); continue
            raise
    raise RuntimeError('429 persistant')
def n_at(tag, off, mature):
    d = get('browse/tags', tag=tag, offset=off, limit=50, mature_content='true' if mature else 'false')
    return len(d.get('results', [])), d.get('has_more')
def compte(tag, mature=True):
    k, more = n_at(tag, 0, mature)
    if not more: return k
    lo, hi = 0, 50000  # lo : offset avec résultats ; hi : offset vide
    k, _ = n_at(tag, 49950, mature)
    if k: return '≥50 000'
    while hi - lo > 50:
        mid = (lo + hi) // 2 // 50 * 50
        if mid == lo: break
        k, _ = n_at(tag, mid, mature)
        if k: lo = mid
        else: hi = mid
    k, _ = n_at(tag, lo, mature)
    return lo + k
if __name__ == '__main__':
    for t in sys.argv[1:]:
        print(t, 'avec adulte', compte(t, True), '| sans adulte', compte(t, False), flush=True)
