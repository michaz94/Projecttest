"""Filtre les alias possibles trouvés par autocomplete_audit.py (revue manuelle ensuite)."""
import csv, json, re, html
B='/home/user/outil_tags_r34/'
sel=list(csv.DictReader(open(B+'doublons/selection_205_dedupliquee_2026-10-24.csv',encoding='utf-8-sig')))
ac=json.load(open(B+'audit_doublons/autocomplete_audit_2026-10-24.json'))
pairs=[l.split('\t')[0] for l in open(B+'doublons/pids_unions_2026-10-24.txt',encoding='utf-8') if not l.startswith('#') and l.strip()]
known={}
for q in pairs:
    ts=[t.strip() for t in q.split('~')]; known[ts[0]]=set(ts)
for r in sel:
    m=r['methode']
    if '∪' in m:
        ts=[t.strip() for t in re.sub(r'^union OU\s*','',m).split('(pages')[0].split('∪')]
        known.setdefault(r['tag'].split(' ∪ ')[0].strip(),set()).update(ts)
    if '∪' in r['tag']: known.setdefault(r['tag'].split(' ∪ ')[0].strip(),set()).update(t.strip() for t in r['tag'].split('∪'))
mains={r['tag'].split(' ∪ ')[0].strip() for r in sel}
allc={}
for q,v in ac.items():
    for d in v or []:
        n=html.unescape(d['value']); c=int(re.search(r'\((\d+)\)\s*$',d['label']).group(1)); allc[n]=c
out=[]
for r in sel:
    t=r['tag'].split(' ∪ ')[0].strip(); base=re.sub(r'_\(.*$','',t); toks=base.split('_')
    inv='_'.join(toks[::-1]) if len(toks)==2 else None
    ks=known.get(t,{t})|{t}
    for n,c in allc.items():
        if n in ks or c<150 or 'cosplay' in n or n in mains: continue
        nb=re.sub(r'_\(.*$','',n)
        ok = n.startswith(base+'_(') or nb==base or (inv and (nb==inv or n.startswith(inv+'_('))) \
             or (len(toks)>=2 and (nb==toks[0] and n.startswith(toks[0]+'_(')))
        if ok: out.append((r['personnage'],t,int(r['publications_dedup']),n,c))
with open(B+'audit_doublons/candidats_bruts_2026-10-24.tsv','w',encoding='utf-8') as f:
    for o in out: f.write('\t'.join(map(str,o))+'\n')
for o in out: print(*o,sep=' | ')
print(len(out))
