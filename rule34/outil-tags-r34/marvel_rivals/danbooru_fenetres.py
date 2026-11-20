import json, time, urllib.request, urllib.parse
UA={"User-Agent":"EdeniaResearch/1.0"}
def count(tags):
    u="https://danbooru.donmai.us/counts/posts.json?tags="+urllib.parse.quote(tags)
    for i in range(3):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); time.sleep(0.6); return d['counts']['posts']
        except Exception as e: err=e; time.sleep(3)
    return None
chars={"Magik":"magik_(x-men)","Femme invisible":"sue_storm","Psylocke":"psylocke","Emma Frost":"emma_frost","Luna Snow":"luna_snow","Jubilee":"jubilee_(marvel)",
"She-Hulk (témoin, absente du jeu)":"she-hulk","Spider-Gwen (témoin, absente du jeu)":"spider-gwen","Wonder Woman (témoin DC)":"wonder_woman","Harley Quinn (témoin DC)":"harley_quinn",
"Black Cat (ajoutée avril 2026)":"black_cat_(marvel)","Rogue (ajoutée déc. 2025)":"rogue_(x-men)","Storm (lancement)":"storm_(x-men)","Scarlet Witch (lancement)":"scarlet_witch"}
# fenêtres annuelles alignées sur le lancement du jeu (6 déc. 2024)
W=[("2021-12-06","2022-12-06"),("2022-12-06","2023-12-06"),("2023-12-06","2024-12-06"),("2024-12-06","2025-12-06"),("2025-12-06","2026-10-24")]
res={"fenetres":W,"total":{},"perso":{}}
for a,b in W:
    res["total"][a]=count(f"date:{a}...{b}")
for n,t in chars.items():
    r={"tag":t,"total":count(t),"avec_marvel_rivals":count(f"{t} marvel_rivals"),"fen":{}}
    for a,b in W: r["fen"][a]=count(f"{t} date:{a}...{b}")
    res["perso"][n]=r; print(n,r,flush=True)
print(res["total"])
json.dump(res,open("danbooru_fenetres_2026-10-24.json","w"),ensure_ascii=False,indent=1)
