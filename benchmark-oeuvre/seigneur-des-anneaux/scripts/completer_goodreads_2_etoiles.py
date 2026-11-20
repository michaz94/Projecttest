"""Complete data/goodreads_communaute_1_2_raw.json (cle '2') : avis Goodreads a 2 etoiles.
Le jeton de pagination est '<score>,<createdAt ms>'. Quand un avis supprime casse le jeton
(erreur 'Unable to find resource'), on abaisse le score de 1 pour sauter l'obstacle.
Les avis du meme score situes apres l'obstacle peuvent etre perdus : on compte les sauts."""
import json,time,requests,base64
KEY='da2-qadjawzt4vafhfci5we3sf65pe'   # cle publique de la page Goodreads
WID='kca://work/amzn1.gr.work.v1.9REDn-8i069k4tnkJOyIFA'
EP='https://kxbwmqov6jgg3daaamb744ycu4.appsync-api.us-east-1.amazonaws.com/graphql'
H={'x-api-key':KEY,'Content-Type':'application/json','User-Agent':'Mozilla/5.0','Origin':'https://www.goodreads.com','Referer':'https://www.goodreads.com/'}
Q='''query getReviews($filters: BookReviewsFilterInput!, $pagination: PaginationInput) {
 getReviews(filters: $filters, pagination: $pagination) { totalCount edges { node { id creator { name followersCount } text rating createdAt likeCount commentCount spoilerStatus } } pageInfo { nextPageToken } } }'''
F={'resourceType':'WORK','resourceId':WID,'ratingMin':2,'ratingMax':2}
P='data/goodreads_communaute_1_2_raw.json'
res=json.load(open(P)); out=res['2']['reviews']; seen={x['id'] for x in out}
def post(tok):
    for k in range(4):
        try:
            return requests.post(EP,headers=H,json={'query':Q,'variables':{'filters':F,'pagination':{'limit':30,**({'after':tok} if tok else {})}}},timeout=40).json()
        except Exception as e: time.sleep(3)
    return {'errors':[{'message':'reseau'}]}
last=out[-1]; score=59
tok=base64.b64encode(f"{score},{int(last['createdAt'])}".encode()).decode().rstrip('=')
skips=[];pages=0
while True:
    r=post(tok); pages+=1
    if r.get('errors'):
        m=r['errors'][0]['message']
        if 'Unable to find' in m or 'not found' in m:
            d=base64.b64decode(tok+'==').decode().split(','); s=int(d[0])-1; skips.append((d[0],len(out)))
            if s<0: break
            tok=base64.b64encode(f"{s},{d[1]}".encode()).decode().rstrip('=')
            if len(skips)>60: print('trop de sauts'); break
            continue
        print('ERR',m[:100]); break
    g=r['data']['getReviews']
    for e in g['edges']:
        x=e['node']
        if x['id'] not in seen: seen.add(x['id']); out.append(x)
    tok=g['pageInfo']['nextPageToken']
    if not g['edges'] or not tok: break
    time.sleep(0.4)
res['2']['reviews']=out; res['2']['collected']=len(out); res['2']['sauts_de_jeton']=len(skips)
json.dump(res,open(P,'w'),ensure_ascii=False)
print('2 etoiles collectes',len(out),'sur',res['2']['totalCount'],'| pages',pages,'| sauts',len(skips), skips[:10])
