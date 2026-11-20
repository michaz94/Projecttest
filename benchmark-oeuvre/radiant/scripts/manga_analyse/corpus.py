import json,re,html,datetime,statistics
G=json.load(open('/home/user/goodreads_radiant_tomes_1_3.json'))
O=json.load(open('/home/user/critiques_manga_radiant_autres_sites.json'))['critiques']
def clean_html(t):
    t=re.sub(r'<br\s*/?>','\n',t or ''); t=re.sub(r'</?(i|b|em|strong|p|a)[^>]*>','',t); t=re.sub(r'<[^>]+>','',t)
    return html.unescape(t)
def verdict(pct):
    if pct is None: return 'Non noté'
    return 'Positif' if pct>=75 else ('Mitigé' if pct>40 else 'Négatif')
R=[]
for e in G:
    for r in e['reviews']:
        pct=None if not r['rating'] else r['rating']/5*100
        R.append(dict(id=f"GR{e['tome']}-{r['review_id'][-6:]}",source='Goodreads',groupe='Goodreads',tome=e['tome'],author=r['author'],lang='en',
          note=r['rating'] or None,echelle='/5',pct=pct,date=r['created_date'],likes=r['like_count'] or 0,txt=clean_html(r['text']).strip()))
for o in O:
    sc=o['rating_scale']; n=o['rating']
    mx={'/10':10,'/20':20,'/5':5}.get(sc)
    pct=None if (n is None or mx is None) else n/mx*100
    if o['source']=='TheOASG': pct=None
    R.append(dict(id=o['id'],source=o['source'],groupe='Autres sites',tome=o['tome'],author=o['author'],lang=o['language'],note=n,echelle=sc,pct=pct,
      date=o['date'],likes=o['likes'] or 0,txt=(o['text'] or '').strip()))
for r in R:
    r['annee']=int(r['date'][:4]) if r['date'] else None
    r['verdict']=verdict(r['pct']); r['mots']=len(re.findall(r"\w+",r['txt']))
if __name__=='__main__':
    from collections import Counter
    print(len(R),Counter(r['groupe'] for r in R),Counter((r['source'],r['verdict']) for r in R))
    print(sum(r['mots'] for r in R))
    print([ (r['id'],r['mots']) for r in R if r['mots']<5])
    print(Counter(r['annee'] for r in R))
