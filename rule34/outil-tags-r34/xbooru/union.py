# Union par négation : tag1 + (tag2 -tag1) + (tag3 -tag1 -tag2)...
import json,time,sys
from compter import n
from groupes import G
res=json.load(open("unions.json")) if __import__("os").path.exists("unions.json") else {}
for nom,fr,sx,tags in G:
    if nom in res: continue
    parts=[]
    for i,t in enumerate(tags):
        q=t+"".join(" -"+u for u in tags[:i]); parts.append(n(q)); time.sleep(0.35)
    res[nom]={"franchise":fr,"sexe":sx,"tags":tags,"parts":parts,"principal":parts[0],"union":sum(p or 0 for p in parts)}
    json.dump(res,open("unions.json","w"),ensure_ascii=False,indent=0)
    print(nom,parts,flush=True)
print("FIN",flush=True)
