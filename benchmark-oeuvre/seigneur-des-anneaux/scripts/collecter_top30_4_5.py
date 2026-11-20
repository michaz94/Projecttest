"""Top 30 (tri par defaut de Goodreads = les plus apprecies) des avis a 5 et 4 etoiles.
Une seule requete par note ; au moindre echec (avis supprime), on abandonne cette note."""
import json,requests,time
KEY='da2-qadjawzt4vafhfci5we3sf65pe'
WID='kca://work/amzn1.gr.work.v1.9REDn-8i069k4tnkJOyIFA'
EP='https://kxbwmqov6jgg3daaamb744ycu4.appsync-api.us-east-1.amazonaws.com/graphql'
H={'x-api-key':KEY,'Content-Type':'application/json','User-Agent':'Mozilla/5.0','Origin':'https://www.goodreads.com','Referer':'https://www.goodreads.com/'}
Q='''query getReviews($filters: BookReviewsFilterInput!, $pagination: PaginationInput) {
 getReviews(filters: $filters, pagination: $pagination) { totalCount edges { node { id creator { name followersCount } text rating createdAt likeCount commentCount spoilerStatus } } } }'''
res={}
for N in (5,4):
    f={'resourceType':'WORK','resourceId':WID,'ratingMin':N,'ratingMax':N}
    r=requests.post(EP,headers=H,json={'query':Q,'variables':{'filters':f,'pagination':{'limit':30}}},timeout=30).json()
    if r.get('errors'):
        print(N,'ABANDON :',r['errors'][0]['message'][:90]); res[N]=None; continue
    g=r['data']['getReviews']; res[N]={'totalCount':g['totalCount'],'reviews':[e['node'] for e in g['edges']]}
    print(N,'ok',len(res[N]['reviews']),'sur',g['totalCount'])
    time.sleep(1)
json.dump({str(k):v for k,v in res.items()},open('data/goodreads_communaute_top30_4_5_raw.json','w'),ensure_ascii=False)
