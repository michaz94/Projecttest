import json,sys,time
from interroger_sites import gelb
site=sys.argv[1]; base={"safebooru":"https://safebooru.org","xbooru":"https://xbooru.com"}[site]
L=json.load(open("liste_195.json")); DR=json.load(open("danbooru_resolution.json")); ER=json.load(open("e621_resolution.json"))
ex=json.load(open(f"brut_{site}_exact.json"))
out={}
for x in L:
    t=x["tag"]; c={t:ex.get(t)}
    for alt in {DR.get(t,[t])[0], ER.get(t,t)}:
        if alt not in c: c[alt]=gelb(base,alt); time.sleep(0.25)
    if not c[t]: c[t]=gelb(base,t); time.sleep(0.25)
    out[t]=c
json.dump(out,open(f"brut_{site}_candidats.json","w"),ensure_ascii=False,indent=0)
print("fini",site)
