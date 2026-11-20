# Compte les publications Xbooru pour une liste de requêtes (API dapi, limit=0).
import urllib.request,urllib.parse,re,time,json,sys
def n(q):
    for e in range(4):
        try:
            u="https://xbooru.com/index.php?page=dapi&s=post&q=index&limit=0&tags="+urllib.parse.quote(q)
            t=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read().decode()
            return int(re.search(r'count="(\d+)"',t).group(1))
        except Exception as ex: time.sleep(3)
    return None
if __name__=="__main__":
    for q in sys.argv[1].split("|"):
        print(q,n(q),flush=True); time.sleep(0.4)
