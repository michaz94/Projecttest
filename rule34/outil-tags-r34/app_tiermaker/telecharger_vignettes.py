# Re-télécharge les images classées (rang Average) dans /tmp/tm4/<id>/NNNN.jpg (et /tmp/tmall pour 87784832), pour build.py.
# Usage : python3 telecharger_vignettes.py id:N [id:N ...]
import gzip,csv,json,sys,os,io,urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
B='/home/user/outil_tags_r34/'

def charger_json(p):
    # les fichiers live_event des votes ajoutés le 24 oct. (suite) sont compressés (.json.gz) pour la place
    import os
    return json.load(gzip.open(p + '.gz', 'rt')) if not os.path.exists(p) and os.path.exists(p + '.gz') else json.load(open(p))
def urls(e):
    p=B+('tiermaker/live_event_87784832_2026-10-23.json' if e=='87784832' else f'tiermaker_{e}/live_event_{e}.json')
    return {im['url'].rsplit('/',1)[1]:im['url'] for im in charger_json(p)['images']}
def get(a):
    u,dst=a
    if os.path.exists(dst): return 0
    try:
        b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Referer':'https://tiermaker.com/'}),timeout=30).read()
        im=Image.open(io.BytesIO(b)).convert('RGB'); im.thumbnail((400,400)); im.save(dst,quality=88); return 0
    except Exception as ex: print('ERR',dst,ex); return 1
for arg in sys.argv[1:]:
    e,N=arg.split(':'); N=int(N); U=urls(e)
    out='/tmp/tmall' if e=='87784832' else f'/tmp/tm4/{e}'; os.makedirs(out,exist_ok=True)
    rows=list(csv.DictReader(open(B+f'tiermaker_{e}/classement_average_avec_incertitude.csv',encoding='utf-8-sig')))[:N]
    jobs=[(U[r['image']],f"{out}/{int(r['rang_average']):04d}.jpg") for r in rows]
    with ThreadPoolExecutor(12) as ex: err=sum(ex.map(get,jobs))
    print(e,len(jobs),'erreurs',err)
