"""Collecte les avis Goodreads de The Fellowship of the Ring pour UNE note (ex. 3).
Usage : python3 collecter_goodreads_note.py 3
Ecrit data/goodreads_communaute_<note>_raw.json (sauvegarde reguliere).
Jeton de pagination = '<score>,<createdAt ms>'. Un avis supprime fait echouer la page
('Unable to find resource') : on divise alors la taille de page par 2 jusqu'a 1 ; si l'avis
fautif est seul, on abaisse le score du jeton de 1 (les avis du meme score situes apres
l'obstacle peuvent etre perdus : on compte les sauts)."""
import json,sys,time,requests,base64
N=int(sys.argv[1])
KEY='da2-qadjawzt4vafhfci5we3sf65pe'   # cle publique de la page Goodreads
WID='kca://work/amzn1.gr.work.v1.9REDn-8i069k4tnkJOyIFA'
EP='https://kxbwmqov6jgg3daaamb744ycu4.appsync-api.us-east-1.amazonaws.com/graphql'
H={'x-api-key':KEY,'Content-Type':'application/json','User-Agent':'Mozilla/5.0','Origin':'https://www.goodreads.com','Referer':'https://www.goodreads.com/'}
Q='''query getReviews($filters: BookReviewsFilterInput!, $pagination: PaginationInput) {
 getReviews(filters: $filters, pagination: $pagination) { totalCount edges { node { id creator { name followersCount } text rating createdAt likeCount commentCount spoilerStatus } } pageInfo { nextPageToken } } }'''
SORT=sys.argv[2] if len(sys.argv)>2 else 'NEWEST'   # NEWEST | OLDEST (le tri par defaut casse sur des avis supprimes)
F={'resourceType':'WORK','resourceId':WID,'ratingMin':N,'ratingMax':N,'sort':SORT}
OUT=f'data/goodreads_communaute_{N}_raw.json'  # une note par fichier
def post(tok,limit):
    for k in range(4):
        try:
            return requests.post(EP,headers=H,json={'query':Q,'variables':{'filters':F,'pagination':{'limit':limit,**({'after':tok} if tok else {})}}},timeout=20).json()
        except Exception: time.sleep(3)
    return {'errors':[{'message':'reseau'}]}
out=[];seen=set();tok=None;skips=[];pages=0;total=None;limit=30;errs=0
import os
if os.path.exists(OUT) and 'reprendre' in sys.argv:       # reprise apres interruption (tri NEWEST/OLDEST)
    prev=json.load(open(OUT)); out=prev['reviews']; seen={x['id'] for x in out}; total=prev['totalCount']
    edge=min if SORT=='NEWEST' else max
    tok=base64.b64encode(str(int(edge(float(x['createdAt']) for x in out))).encode()).decode().rstrip('=')
    print('reprise avec',len(out),'avis, jeton',base64.b64decode(tok+'==').decode(),flush=True)
def save():
    json.dump({'note':N,'totalCount':total,'collected':len(out),'sauts_de_jeton':len(skips),'reviews':out},open(OUT,'w'),ensure_ascii=False)
trans=0;esc=0;DELTAS=[1000,60000,3600000,86400000,7*86400000]
while True:
    r=post(tok,limit); pages+=1
    if r.get('errors'):
        m=r['errors'][0]['message']
        if m.startswith('resource not found') or 'Unable to find' in m:   # avis supprime dans le lot (ou erreur intermittente)
            if limit>1: limit=max(1,limit//2); continue
            trans+=1
            if trans<3: time.sleep(0.5); continue
            # limit=1 et echec repete : l'avis suivant est casse. On saute en reculant le jeton (tri par date).
            d=base64.b64decode(tok+'==').decode().split(',')
            if len(d)!=1: print('jeton inattendu',d); break
            skips.append((d[0],len(out)))
            if len(skips)>400 or esc>=len(DELTAS): print('arret sauts'); break
            tok=base64.b64encode(str(int(d[0])-DELTAS[esc]).encode()).decode().rstrip('=')
            esc+=1; trans=0; continue
        errs+=1
        if errs<=8: time.sleep(3); continue
        print('ERR',m[:100]); break
    trans=0; esc=0
    g=r['data']['getReviews']; total=g['totalCount']
    for e in g['edges']:
        x=e['node']
        if x['id'] not in seen: seen.add(x['id']); out.append(x)
    tok=g['pageInfo']['nextPageToken']
    limit=min(30,limit*2)
    save()
    if pages%5==0: print(pages,len(out),'sauts',len(skips),flush=True)
    if not g['edges'] or not tok: break
    time.sleep(0.4)
save()
print(f'{N} etoiles : {len(out)} collectes sur {total} | pages {pages} | sauts {len(skips)}')
