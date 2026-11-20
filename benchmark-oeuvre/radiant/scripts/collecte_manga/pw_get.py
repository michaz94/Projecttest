import sys,time
from playwright.sync_api import sync_playwright
def get(urls,wait=3,ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='fr-FR'):
    out={}
    with sync_playwright() as p:
        b=p.chromium.launch(args=['--no-sandbox'])
        ctx=b.new_context(user_agent=ua,locale=locale)
        for name,u in urls.items():
            pg=ctx.new_page()
            try:
                r=pg.goto(u,wait_until='domcontentloaded',timeout=60000); time.sleep(wait)
                out[name]=(r.status if r else None,pg.url,pg.content())
            except Exception as e:
                out[name]=(None,u,'ERR '+str(e)[:200])
            pg.close()
        b.close()
    return out
if __name__=='__main__':
    import json
    urls=json.loads(sys.argv[1]); res=get(urls)
    for n,(st,u,h) in res.items():
        open(f'pw_{n}.html','w',encoding='utf8').write(h); print(n,st,u,len(h))
