# Interroge e621 (par lots), Safebooru et Xbooru (un tag à la fois) pour les tags exacts.
import json,time,urllib.request,urllib.parse,sys
import xml.etree.ElementTree as ET
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
def get(url):
    for k in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":UA}),timeout=20).read().decode()
        except Exception as e:
            time.sleep(2)
    return None
def gelb(base,tag):
    t=get(base+"/index.php?page=dapi&s=tag&q=index&name="+urllib.parse.quote(tag))
    if t is None: return None
    try:
        for x in ET.fromstring(t).findall("tag"):
            if x.get("name")==tag: return int(x.get("count"))
    except Exception: return None
    return 0
def e621(tags):
    out={}
    for i in range(0,len(tags),40):
        b=tags[i:i+40]
        t=get("https://e621.net/tags.json?limit=100&search%5Bname%5D="+urllib.parse.quote(",".join(b)))
        for x in json.loads(t or "[]"): out[x["name"]]=x["post_count"]
        time.sleep(1.1)
    return out
if __name__=="__main__":
    tags=sys.argv[2].split("|") if len(sys.argv)>2 else [x["tag"] for x in json.load(open("liste_195.json"))]
    mode=sys.argv[1]
    res={}
    if mode=="e621": res=e621(tags)
    else:
        base={"safebooru":"https://safebooru.org","xbooru":"https://xbooru.com"}[mode]
        for t in tags: res[t]=gelb(base,t); time.sleep(0.3)
    print(json.dumps(res,ensure_ascii=False))
