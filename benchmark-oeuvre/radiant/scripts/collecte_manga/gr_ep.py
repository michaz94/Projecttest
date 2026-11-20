import sys,time,json
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox'])
    ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",locale='en-US')
    pg=ctx.new_page()
    pg.goto("https://www.goodreads.com/book/show/21991318-radiant-tome-2",wait_until='domcontentloaded',timeout=60000); time.sleep(5)
    for u in ["/book/reviews/21991318?text_only=true&page=2","/book/reviews/21991318?text_only=true&page=1"]:
        r=pg.evaluate("""async (u)=>{const r=await fetch(u,{headers:{'X-Requested-With':'XMLHttpRequest'}});return [r.status,await r.text()]}""",u)
        print(u,r[0],len(r[1])); open('ep_'+u.split('page=')[1]+'.html','w').write(r[1])
    b.close()
