import re,json,time
from playwright.sync_api import sync_playwright
lists={'t1':'sc_t1','t2':'sc_t2','t3':'sc_t3','serie':'sc_s'}
items=[]
for scope,n in lists.items():
    h=open(f'pw_{n}.html',encoding='utf8').read()
    ap=json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S).group(1))['props']['pageProps']['__APOLLO_STATE__']
    for k,v in ap.items():
        if k.startswith('Review:'):
            au=ap.get(v['author']['__ref'],{})
            items.append(dict(scope=scope,review_id=v['id'],author=au.get('username') or au.get('name'),rating=v.get('rating'),date=v.get('dateCreation'),title=v.get('title'),likes=v.get('likeCount'),positive_likes=v.get('likePositiveCount'),comments=v.get('commentCount'),hits=v.get('hits'),url='https://www.senscritique.com'+v['url'],text_short=v.get('bodyShort'),text=None))
print(len(items))
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox']); ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='fr-FR')
    for it in items:
        pg=ctx.new_page()
        try:
            pg.goto(it['url'],wait_until='domcontentloaded',timeout=60000); time.sleep(1.5)
            h=pg.content()
            m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
            ap=json.loads(m.group(1))['props']['pageProps']['__APOLLO_STATE__']
            rv=[v for k,v in ap.items() if k.startswith('Review:') and v.get('id')==it['review_id']]
            body=(rv[0].get('body') or rv[0].get('bodyShort')) if rv else None
            it['text']=re.sub(r'<br\s*/?>','\n',re.sub(r'</p>','\n\n',body or ''))
            it['text']=re.sub(r'<[^>]+>','',it['text']).strip()
            if not rv: print('no review',it['url'],[k for k in ap][:6])
            it['author']=it['author']
        except Exception as e:
            print('ERR',it['url'],str(e)[:100])
        pg.close(); time.sleep(1)
    b.close()
json.dump(items,open('senscritique_raw.json','w'),ensure_ascii=False,indent=1)
print([ (i['scope'],i['author'],len((i['text'] or '').split()),len(i['text_short'].split())) for i in items])
