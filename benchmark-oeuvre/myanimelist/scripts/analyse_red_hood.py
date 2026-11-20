import json,re
from collections import defaultdict
d=json.load(open('data.json'))

TH={
 "Rythme / lenteur":r"\b(pacing|paced|slow|slowly|drag(s|ged|ging)?|rushed|too long|dragging|filler)\b",
 "Examen comme détour":r"\b(exam|test(ing)?|tournament|arc)\b",
 "Protagoniste fade / générique":r"\b(generic|bland|boring|cliche|clich\u00e9|typical|standard|derivative|forgettable)\b",
 "Lisibilite de l'action":r"\b(confusing|confused|hard to follow|unclear|messy|cluttered|paneling|panel work|incoherent)\b",
 "Exposition / explications":r"\b(exposition|expositional|info ?dump|explaining|explains|over-?explain)\b",
 "Art / dessin (positif)":r"\b(art|artwork|gorgeous|beautiful|stunning|art style|visuals)\b",
 "Attachement / personnages":r"\b(attach(ed|ment)?|care about|invested|connect(ion)?|chemistry|develop(ment|ed)?)\b",
 "Peur de l'annulation":r"\b(axe[dn]?|cancel(l?ed|lation)?|getting axed|survive)\b",
 "Abandon declare":r"\b(drop(ping|ped)?|quit(ting)?|stopped reading|gave up)\b",
 "Monde / worldbuilding":r"\b(world ?building|setting|lore|world)\b",
 "Morale / predation":r"\b(moral(ity|s)?|ethic(s|al)?|kill(ing)? (them|people)|predation|genocide|extermin)\b",
 "Casting trop large":r"\b(too many characters|cast|side characters|new characters)\b",
}
TH={k:re.compile(v,re.I) for k,v in TH.items()}

def chnum(x):
    try: return int(x)
    except: return None

rows=defaultdict(lambda: defaultdict(int))
tot=defaultdict(int)
for p in d:
    s=p['serie']; ch=chnum(p['chapitre'])
    for c in p['comments']:
        b=c['body'] or ''
        tot[(s,ch)]+=1
        for t,rx in TH.items():
            if rx.search(b): rows[(s,ch)][t]+=1

# Red Hood overall
rh=[(ch,tot[(s,ch)]) for (s,ch) in tot if s=='Red Hood' and ch]
rh.sort()
N=sum(n for _,n in rh)
print(f"=== RED HOOD : {N} commentaires, 18 chapitres ===\n")
agg=defaultdict(int)
for (s,ch),v in rows.items():
    if s!='Red Hood': continue
    for t,n in v.items(): agg[t]+=n
print(f"{'Theme':34s} {'n':>5s} {'% comm.':>8s}")
for t,n in sorted(agg.items(),key=lambda x:-x[1]):
    print(f"{t:34s} {n:5d} {100*n/N:7.1f}%")

print("\n=== TRAJECTOIRE PAR CHAPITRE (% des commentaires du chapitre) ===")
key=["Rythme / lenteur","Protagoniste fade / générique","Lisibilite de l'action","Attachement / personnages","Peur de l'annulation","Abandon declare","Art / dessin (positif)"]
print(f"{'Ch':>3s} {'comm':>5s} " + " ".join(f"{k[:11]:>11s}" for k in key))
for ch,n in rh:
    v=rows[('Red Hood',ch)]
    print(f"{ch:3d} {n:5d} " + " ".join(f"{100*v[k]/n:10.1f}%" for k in key))
