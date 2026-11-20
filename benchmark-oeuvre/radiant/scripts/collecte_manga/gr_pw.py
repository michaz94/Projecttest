import re,json,sys,time
from playwright.sync_api import sync_playwright
URLS={1:"https://www.goodreads.com/book/show/18191523-radiant-tome-1",2:"https://www.goodreads.com/book/show/21991318-radiant-tome-2",3:"https://www.goodreads.com/book/show/25117448-radiant-tome-3"}
res={}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox'])
    ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='en-US')
    for t,u in URLS.items():
        pg=ctx.new_page()
        try:
            pg.goto(u,wait_until='domcontentloaded',timeout=60000)
            for _ in range(12):
                time.sleep(3)
                if pg.query_selector('script#__NEXT_DATA__'): break
            h=pg.content()
        except Exception as e:
            print(t,'ERR',e); h=''
        open(f'gr_t{t}.html','w',encoding='utf8').write(h)
        print(t,len(h),'__NEXT_DATA__' in h)
        pg.close(); time.sleep(4)
    b.close()
