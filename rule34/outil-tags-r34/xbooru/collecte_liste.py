# Parcourt la liste des tags de Xbooru triée par nombre de publications (20 par page).
# Usage : python3 collecte_liste.py PAGE_MAX PAGE_DEBUT FICHIER_SORTIE SEUIL_ARRET
import re,json,time,urllib.request,sys,html
out=[];vus=set()
for p in range(int(sys.argv[2]),int(sys.argv[1])):
    u=f"https://xbooru.com/index.php?page=tags&s=list&tags=&sort=desc&order_by=index_count&pid={p*20}"
    for essai in range(3):
        try:
            t=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read().decode("utf-8","ignore");break
        except Exception as e: print("err",p,e,flush=True); time.sleep(3)
    rows=re.findall(r'<tr>\s*<td>(\d+)</td>.*?tags=([^"]*)">(.*?)</a>.*?<td>\s*(\w+)',t,re.S)
    for c,href,name,typ in rows:
        out.append({"count":int(c),"href":href,"name":html.unescape(name),"type":typ,"page":p})
    nch=sum(1 for x in out if x["type"]=="Character" and x["name"]==x["name"].strip())
    print(p,len(rows),rows[-1][0] if rows else None,"chars",nch,flush=True)
    json.dump(out,open(sys.argv[3],"w"),ensure_ascii=False)
    if not rows or int(rows[-1][0])<int(sys.argv[4]): break
    time.sleep(0.6)
print("FIN",flush=True)
