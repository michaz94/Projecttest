import json, time, urllib.request, urllib.parse
UA={"User-Agent":"EdeniaResearch/1.0"}
def count(tags):
    u="https://danbooru.donmai.us/counts/posts.json?tags="+urllib.parse.quote(tags)
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60)); time.sleep(0.6); return d['counts']['posts']
months=["2025-10-01","2025-11-01","2025-12-01","2026-01-01","2026-02-01","2026-03-01","2026-04-01","2026-05-01","2026-06-01","2026-07-01","2026-08-01","2026-09-01","2026-10-01","2026-10-24"]
out={}
for t in ["jubilee_(marvel)","black_cat_(marvel)"]:
    out[t]={months[i]:count(f"{t} date:{months[i]}...{months[i+1]}") for i in range(len(months)-1)}
    print(t,out[t],flush=True)
out["total_mensuel"]={months[i]:count(f"date:{months[i]}...{months[i+1]}") for i in range(len(months)-1)}
print(out["total_mensuel"])
json.dump(out,open("danbooru_mensuel_jubilee_blackcat_2026-10-24.json","w"),indent=1)
