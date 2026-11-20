import sys,time,json,re
from playwright.sync_api import sync_playwright
BOOK={1:(18191523,"radiant-tome-1",5),2:(21991318,"radiant-tome-2",2),3:(25117448,"radiant-tome-3",2)}
res={}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox'])
    ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='en-US')
    for t,(i,slug,np_) in BOOK.items():
        pg=ctx.new_page()
        pg.goto(f"https://www.goodreads.com/book/show/{i}-{slug}",wait_until='domcontentloaded',timeout=60000); time.sleep(5)
        res[t]=[]
        for page in range(1,np_+1):
            r=pg.evaluate("""async (u)=>{const r=await fetch(u,{headers:{'X-Requested-With':'XMLHttpRequest'}});return [r.status,await r.text()]}""",f"/book/reviews/{i}?text_only=true&page={page}")
            print(t,page,r[0],len(r[1]),flush=True); res[t].append(r[1]); time.sleep(2)
        pg.close()
    b.close()
json.dump(res,open('gr_ep_raw.json','w'))
