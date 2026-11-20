# Spider-Gwen sur Danbooru : fenêtres annuelles alignées sur la sortie de Spider-Man: New Generation (14/12/2018)
# + 6 mois avant / 6 mois après Spider-Man: Across the Spider-Verse (02/06/2023). Date = date d'envoi.
import json, time, urllib.request, urllib.parse, datetime as dt
UA={"User-Agent":"EdeniaResearch/1.0"}
def count(tags):
    u="https://danbooru.donmai.us/counts/posts.json?tags="+urllib.parse.quote(tags)
    for i in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); time.sleep(0.6)
            if d['counts']['posts'] is not None: return d['counts']['posts']
        except Exception: pass
        time.sleep(3)
    return None
def total(a,b):
    n=count(f"date:{a}...{b}")
    if n is not None: return n
    A=dt.date.fromisoformat(a); B=dt.date.fromisoformat(b); s=(B-A)/4; t=0
    for i in range(4):
        x=A+s*i; y=A+s*(i+1) if i<3 else B; t+=count(f"date:{x}...{y}")
    return t
W=[(f"{y}-12-14",f"{y+1}-12-14") for y in range(2014,2025)]+[("2025-12-14","2026-10-24")]
W+= [("2022-12-02","2023-06-02"),("2023-06-02","2023-12-02")]
T={"spider-gwen":"spider-gwen","union gwen_stacy|spider-gwen":"~gwen_stacy ~spider-gwen"}
res=[]
for a,b in W:
    tot=total(a,b); r={"debut":a,"fin":b,"total_site":tot}
    for k,q in T.items():
        n=count(f"{q} date:{a}...{b}"); r[k]=n; r[k+"_par_M"]=round(n/tot*1e6,1) if n is not None and tot else None
    print(r,flush=True); res.append(r)
res2={"fenetres":res,"totaux_tags":{k:count(q) for k,q in T.items()},"gwen_stacy":count("gwen_stacy")}
print(res2["totaux_tags"],res2["gwen_stacy"])
json.dump(res2,open("danbooru_spider_gwen_2026-10-24.json","w"),ensure_ascii=False,indent=1)
