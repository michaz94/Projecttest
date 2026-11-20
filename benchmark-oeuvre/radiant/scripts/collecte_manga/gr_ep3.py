import json,re
from html import unescape
res=json.load(open('gr_ep_raw.json'))
def tx(s):
    s=re.sub(r'<br\s*/?>','\n',s); s=re.sub(r'<[^>]+>','',s); return unescape(s).strip()
out={}
for t,pages in res.items():
    L=[]
    for raw in pages:
        k=raw.index('Element.update("reviews", ')+len('Element.update("reviews", ')
        h,_=json.JSONDecoder().raw_decode(raw[k:])
        blocks=re.split(r'(?=<div id="review_\d+" class="review)',h)[1:]
        for b in blocks:
            rid=re.match(r'<div id="review_(\d+)"',b).group(1)
            au=re.search(r'<a title="([^"]*)" class="left imgcol"',b)
            st=re.search(r'class="staticStars[^"]*" title="([^"]*)"',b)
            dt=re.search(r'class="reviewDate[^>]*>([^<]*)<',b)
            lk=re.search(r'(\d+) likes?',b)
            rt=re.search(r'<div class="reviewText stacked">(.*?)<div class="reviewFooter',b,flags=re.S)
            body=rt.group(1) if rt else ''
            fts=re.findall(r'<span id="freeText(?:Container)?\d+"[^>]*>(.*?)</span>',body,flags=re.S)
            full=max((tx(x) for x in fts),key=len) if fts else tx(body)
            L.append(dict(id=rid,author=unescape(au.group(1)) if au else None,stars=st.group(1) if st else None,date=tx(dt.group(1)) if dt else None,likes=int(lk.group(1)) if lk else 0,text=full,n_free=len(fts)))
    out[t]=L
    print(t,len(L),sum(1 for x in L if x['author']),sum(1 for x in L if x['n_free']>1))
json.dump(out,open('goodreads_full_parsed.json','w'),ensure_ascii=False)
d=json.load(open('/home/user/uploads/Radiant_tomes_1_3_corpus_avis.json'))
for t in '123':
    mine={a['id']:a for a in d['goodreads'][t]['avis']}
    got={x['id']:x for x in out[t]}
    print(t,'ids ∩',len(set(mine)&set(got)),'user only',len(set(mine)-set(got)),'fetched only',len(set(got)-set(mine)))
    longer=sum(1 for i in set(mine)&set(got) if len(got[i]['text'])>len(mine[i]['texte'])+30)
    print(' longer than user:',longer)
