# Lit le tableau « Analyse : les plus appréciés » de l'app TierMaker (tri par défaut) via Playwright
import os, json, sys
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/tmp/pw')
from playwright.sync_api import sync_playwright
p = '/home/user/outil_tags_r34/app_tiermaker/top100_tiermaker_rule34.html'
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + p); pg.wait_for_timeout(1500)
    pg.click('button.tab.an'); pg.wait_for_timeout(800)
    print('tri:', pg.eval_on_selector('#atri', 'e=>e.options[e.selectedIndex].text'))
    print('min:', pg.eval_on_selector('#amin', 'e=>e.options[e.selectedIndex].text'))
    rows = pg.eval_on_selector_all('#atb tr', 'rs=>rs.slice(0,20).map(r=>[...r.children].map(c=>c.innerText.replace(/\\s+/g," ").trim()).join(" | "))')
    for r in rows: print(r)
    b.close()
