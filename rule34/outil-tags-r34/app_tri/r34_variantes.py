import json,time,urllib.request,urllib.parse,re,html
B='/home/user/outil_tags_r34/app_tri/'
A=json.load(open(B+'r34_top_danbooru_autocomplete_2026-10-24.json'))
def ac(q):
    u='https://api.rule34.xxx/autocomplete.php?q='+urllib.parse.quote(q)
    for k in range(3):
        try: return [(html.unescape(x['value']),int(re.search(r'\((\d+)\)$',x['label']).group(1))) for x in json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))]
        except Exception: time.sleep(3)
    return []
V={}
for t in A:
    m=re.match(r'^(.*?)_\((.*)\)$',t)
    qs=[]
    if m: qs=[m.group(1)+'_(' ]
    else:
        w=t.split('_')
        if len(w)>=2: qs=['_'.join(w[1:]+w[:1]), t+'_(']
    res=[]
    for q in qs: res+=ac(q); time.sleep(0.35)
    V[t]=[x for x in res if 'cosplay' not in x[0]][:10]
json.dump(V,open(B+'r34_top_danbooru_variantes_2026-10-24.json','w'),ensure_ascii=False,indent=0)
for t,v in V.items():
    ex=A[t]['exact'] or 0
    big=[x for x in v if x[1]>max(150,0.1*ex) and x[0]!=t]
    if big: print(t,ex,big[:5])
