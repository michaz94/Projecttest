# Effet d'une adaptation : publications Danbooru 12 mois avant vs 12 mois après la sortie (date d'envoi), rapportées au volume total du site.
import json, time, urllib.request, urllib.parse, datetime as dt
UA={"User-Agent":"EdeniaResearch/1.0"}
def count(tags):
    u="https://danbooru.donmai.us/counts/posts.json?tags="+urllib.parse.quote(tags)
    for i in range(3):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); time.sleep(0.6)
            if d['counts']['posts'] is not None: return d['counts']['posts']
        except Exception as e: pass
        time.sleep(3)
    return None
def count_total(a,b):
    # le compteur global renvoie parfois null sur 12 mois : on additionne 4 trimestres
    n=count(f"date:{a}...{b}")
    if n is not None: return n
    A=dt.date.fromisoformat(a); B=dt.date.fromisoformat(b); step=(B-A)/4; tot=0
    for i in range(4):
        x=A+step*i; y=A+step*(i+1) if i<3 else B
        tot+=count(f"date:{x}...{y}")
    return tot
# (nom, tag, adaptation, date de sortie, début de l'œuvre d'origine)
C=[("Makima","makima_(chainsaw_man)","anime Chainsaw Man","2022-10-11","manga déc. 2018"),
   ("Power","power_(chainsaw_man)","anime Chainsaw Man","2022-10-11","manga déc. 2018"),
   ("Frieren","frieren","anime Frieren","2023-09-29","manga avr. 2020"),
   ("Marin Kitagawa","kitagawa_marin","anime My Dress-Up Darling","2022-01-09","manga janv. 2018"),
   ("Yor Forger","yor_briar","anime Spy×Family","2022-04-09","manga mars 2019"),
   ("Nezuko","kamado_nezuko","anime Demon Slayer","2019-04-06","manga févr. 2016"),
   ("Spider-Gwen","spider-gwen","film Spider-Man: New Generation","2018-12-14","comics 2014"),
   ("Wonder Woman","wonder_woman","film Wonder Woman","2017-06-02","comics 1941"),
   ("Black Widow","black_widow","film Avengers","2012-05-04","comics 1964")]
def shift(d,y): return d.replace(year=d.year+y)
res=[]
for n,t,a,d,o in C:
    D=dt.date.fromisoformat(d); av=f"{shift(D,-1)}...{D}"; ap=f"{D}...{shift(D,1)}"
    r=dict(personnage=n,tag=t,adaptation=a,sortie=d,origine=o,avant=count(f"{t} date:{av}"),apres=count(f"{t} date:{ap}"),
           total_site_avant=count_total(str(shift(D,-1)),d),total_site_apres=count_total(d,str(shift(D,1))),total_tag=count(t))
    r['par_M_avant']=round(r['avant']/r['total_site_avant']*1e6,1); r['par_M_apres']=round(r['apres']/r['total_site_apres']*1e6,1)
    r['multiplicateur']=round(r['par_M_apres']/r['par_M_avant'],1) if r['par_M_avant'] else None
    print(r,flush=True); res.append(r)
json.dump(res,open("danbooru_avant_apres_2026-10-24.json","w"),ensure_ascii=False,indent=1)
