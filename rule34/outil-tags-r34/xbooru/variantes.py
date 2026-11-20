# Cherche les variantes de nom d'un personnage sur Xbooru (recherche par motif, tags de type personnage, >= 100 publications).
import re,json,time,urllib.request,urllib.parse,html,sys
motifs=sys.argv[1].split("|")
res=json.load(open("variantes.json")) if __import__("os").path.exists("variantes.json") else {}
for m in motifs:
    if m in res: continue
    u="https://xbooru.com/index.php?page=tags&s=list&sort=desc&order_by=index_count&tags="+urllib.parse.quote(m)
    t=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read().decode("utf-8","ignore")
    rows=re.findall(r'<td>(\d+)</td>\s*<td>\s*<span class="tag-type-(\w+)">\s*<a[^>]*>(.*?)</a>',t,re.S)
    res[m]=[(int(c),typ,html.unescape(n)) for c,typ,n in rows if int(c)>=100 and n==n.strip() and typ in("character","general")]
    json.dump(res,open("variantes.json","w"),ensure_ascii=False,indent=0)
    time.sleep(0.6)
for m in motifs: print(m,res[m])
