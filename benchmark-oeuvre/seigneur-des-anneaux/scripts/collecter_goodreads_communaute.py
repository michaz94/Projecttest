"""Collecte des avis Goodreads (1 et 2 etoiles) de The Fellowship of the Ring.
Ecrit data/goodreads_communaute_1_2_raw.json. Ne modifie rien d'autre."""
import requests, json, re, time, sys
H0={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}
page=requests.get('https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring',headers=H0,timeout=30).text
nd=json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',page,re.S).group(1))
pp=nd['props']['pageProps']; st=pp['apolloState']
WID=[k for k in st if k.startswith('Work:')][0][5:]
EP='https://kxbwmqov6jgg3daaamb744ycu4.appsync-api.us-east-1.amazonaws.com/graphql'
H={'x-api-key':pp['apiKey'],'Content-Type':'application/json','User-Agent':'Mozilla/5.0','Origin':'https://www.goodreads.com','Referer':'https://www.goodreads.com/'}
Q='''query getReviews($filters: BookReviewsFilterInput!, $pagination: PaginationInput) {
 getReviews(filters: $filters, pagination: $pagination) { totalCount edges { node { id creator { name followersCount } text rating createdAt likeCount commentCount spoilerStatus } } pageInfo { nextPageToken } } }'''
def collect(rmin,rmax,maxpages=200):
    out=[];after=None;total=None
    for i in range(maxpages):
        pag={'limit':30}
        if after: pag['after']=after
        f={'resourceType':'WORK','resourceId':WID,'ratingMax':rmax}
        if rmin: f['ratingMin']=rmin
        r=requests.post(EP,headers=H,json={'query':Q,'variables':{'filters':f,'pagination':pag}},timeout=40).json()
        if r.get('errors'): print('ERR',r['errors'][0]['message'][:200]); break
        g=r['data']['getReviews']; total=g['totalCount']
        out+= [e['node'] for e in g['edges']]
        after=g['pageInfo']['nextPageToken']
        if not g['edges'] or not after or len(out)>=total: break
        time.sleep(0.4)
    return total,out
res={}
for key,(a,b) in {'1':(None,1),'2':(2,2)}.items():
    t,o=collect(a,b); res[key]={'totalCount':t,'collected':len(o),'reviews':o}
    print(key,t,len(o),len({x['id'] for x in o}),'ratings',sorted({x['rating'] for x in o}))
json.dump(res,open('data/goodreads_communaute_1_2_raw.json','w'),ensure_ascii=False)
