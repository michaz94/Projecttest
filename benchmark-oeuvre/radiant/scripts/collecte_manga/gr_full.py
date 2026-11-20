import re,json,sys,time
from playwright.sync_api import sync_playwright
URLS={1:"https://www.goodreads.com/book/show/18191523-radiant-tome-1",2:"https://www.goodreads.com/book/show/21991318-radiant-tome-2",3:"https://www.goodreads.com/book/show/25117448-radiant-tome-3"}
t=int(sys.argv[1]); out={}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox'])
    ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='en-US',viewport={'width':1300,'height':2000})
    pg=ctx.new_page()
    pg.goto(URLS[t],wait_until='domcontentloaded',timeout=60000)
    time.sleep(6)
    # dismiss modals
    try: pg.keyboard.press('Escape')
    except: pass
    prev=-1
    for i in range(40):
        n=pg.locator('article.ReviewCard').count()
        print('cards',n,flush=True)
        if n==prev: break
        prev=n
        btn=pg.locator('button:has-text("Show more reviews")')
        if btn.count()==0: break
        try:
            btn.first.scroll_into_view_if_needed(); btn.first.click(timeout=5000)
        except Exception as e: print('click err',str(e)[:100]); break
        time.sleep(4)
    html=pg.content()
    open(f'gr_full_t{t}.html','w',encoding='utf8').write(html)
    b.close()
