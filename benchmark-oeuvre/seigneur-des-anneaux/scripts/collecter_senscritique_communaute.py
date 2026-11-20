"""Collecte des critiques SensCritique de La Communaute de l'Anneau (produit 8957375).
Ecrit data/senscritique_communaute_raw.json."""
import requests, json
H={'Content-Type':'application/json','User-Agent':'Mozilla/5.0','Origin':'https://www.senscritique.com','Referer':'https://www.senscritique.com/'}
q='''query($id:Int!,$limit:Int!,$offset:Int!){product(id:$id){title stats{ratingCount reviewCount recommendCount}
 reviews(limit:$limit,offset:$offset,sortBy:LIKE_POSITIVE_COUNT,withTopReviews:false){total items{id title body rating dateCreation likeCount hits url author{username}}}}}'''
out=[];off=0
while True:
    r=requests.post('https://apollo.senscritique.com/',headers=H,json={'query':q,'variables':{'id':8957375,'limit':10,'offset':off}},timeout=40).json()
    if r.get('errors'): print(r['errors'][0]['message'][:300]); break
    p=r['data']['product']; items=p['reviews']['items']; tot=p['reviews']['total']
    out+=items; off+=10
    if not items or len(out)>=tot: break
print(p['stats'],tot,len(out))
json.dump({'stats':p['stats'],'reviews':out},open('data/senscritique_communaute_raw.json','w'),ensure_ascii=False)
