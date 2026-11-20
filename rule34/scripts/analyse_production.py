"""Production Danbooru par an : brute, et rapportée au volume total d'uploads du site (posts pour 10 000 uploads). 24 oct. 2026."""
import json,csv
d=json.load(open('danbooru_annuel_2026-10-24.json'))
T={int(y):v for y,v in d['_TOTAL']['annees'].items()}; T[2026]=738777+821976+326707   # 2026 : 1er jan. -> 24 oct. (3 requêtes)
F2026=297/365
MED={"2B":"JV","Raiden Shogun":"JV","Tifa":"JV","Samus":"JV","Chun-Li":"JV","Peach":"JV","Zelda":"JV","Lara Croft":"JV","Aerith":"JV","Hatsune Miku":"Autre"}
rows=[]
for n,v in d.items():
    if n in ('_TOTAL','Yor (variante)','Ai Hoshino'): continue
    a={int(y):(c or 0) for y,c in v['annees'].items()}
    mx=max(a.values()); S=min(y for y in a if a[y]>=0.1*mx)
    ys=[y for y in a if y>=S]; tot=sum(a[y] for y in ys); dur=sum(F2026 if y==2026 else 1 for y in ys)
    share=tot/sum(T[y]*(F2026 if False else 1) for y in ys)*1e4
    w=[2023,2024,2025]; win=sum(a[y] for y in w); wsh=win/sum(T[y] for y in w)*1e4
    pk=max(ys,key=lambda y:a[y]/T[y]); 
    rows.append(dict(personnage=n,medium=MED.get(n,"Animanga"),debut_danbooru=S,censure_gauche="oui" if S==2006 else "",total_2006_2026=tot,annees=round(dur,2),
        par_an=round(tot/dur),pour10k_uploads=round(share,2),posts_2023_2025=win,pour10k_2023_2025=round(wsh,2),annee_pic=pk,pic_pour10k=round(a[pk]/T[pk]*1e4,1)))
rows.sort(key=lambda r:-r['par_an'])
with open('production_danbooru_par_an_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as o:
    w=csv.DictWriter(o,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
for k in ['par_an','pour10k_uploads','pour10k_2023_2025']:
    print('==',k)
    for m in ['Animanga','JV']:
        R=sorted([r for r in rows if r['medium']==m],key=lambda r:-r[k])
        print(m,' | '.join(f"{i+1}.{r['personnage']} {r[k]}{'*' if r['censure_gauche'] else ''}" for i,r in enumerate(R)))
print('site: uploads/an', {y:T[y] for y in (2008,2012,2016,2018,2020,2022,2024,2025)})
