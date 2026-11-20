import re,statistics as st,datetime
from collections import Counter
from analyse import R,CATS,POLES,SUB
from quotes import Q
def norm(t):
    t=t.replace('*','').replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('«','"').replace('»','"')
    t=re.sub(r'\[([^\]]+)\]\[\d+\]',r'\1',t); return re.sub(r'\s+',' ',t).strip()
byid={r['id']:r for r in R}
MOIS=['janv.','févr.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.']
def fdate(d):
    if not d: return 'date non indiquée'
    y,m,j=d.split('-'); return f"{int(j)} {MOIS[int(m)-1]} {y}"
def fnote(r):
    if r['note'] is None: return 'sans note'
    n=str(r['note']).replace('.',','); e=r['echelle'] or ''
    return f"{n}{e}" if e.startswith('/') else f"{n}"
def tome(r): return f"T{r['tome']}" if r['tome'] else 'série'
def head(r):
    lk=f", {r['likes']} like{'s' if r['likes']>1 else ''}" if r['source'] in('Goodreads','SensCritique') and r['likes'] else ''
    v=r['verdict']+(' (lu)' if r.get('verdict_lu') else '')
    return f"`{r['author'] or 'anonyme'}` ({r['source']} {tome(r)}, {v}, {fdate(r['date'])}, `{fnote(r)}`{lk})"
def quotes(key):
    out=[]
    for i,q in Q[key]:
        assert norm(q) in norm(byid[i]['txt']),(i,q)
        out.append(f"  * {head(byid[i])} : *« {q} »*")
    return '\n'.join(out)
def P(a,b): return f"{100*a/b:.1f}".replace('.',',')+' %' if b else '—'
def PC(a,b): return f"{a} ({P(a,b)})"
def mean(x): return f"{st.mean(x):.1f}".replace('.',',') if x else '—'
def med(x): return f"{st.median(x):g}".replace('.',',') if x else '—'
N=len(R); cov=[r for r in R if r['couvert']]; NC=len(cov); c50=[r for r in cov if r['mots']>=50]; N50=len(c50)
MX=[r for r in R if r['verdict'] in('Mitigé','Négatif')]; NM=len(MX)
vc=Counter(r['verdict'] for r in R)
GR=[r for r in R if r['groupe']=='Goodreads']; AS=[r for r in R if r['groupe']!='Goodreads']
def likes(rs): return [r['likes'] for r in rs if r['source'] in('Goodreads','SensCritique')]
def row11(name,rs,bold=False):
    bold=False
    n=len(rs); v=Counter(r['verdict'] for r in rs); pc=[r['pct'] for r in rs if r['pct'] is not None]; lk=likes(rs)
    b='**' if bold else ''
    lks=f"{sum(lk)} | {med(lk)} / {mean(lk)}" if lk else "— | —"
    return f"| {b}{name}{b} | {b}{n}{b} | {sum(r['mots'] for r in rs):,} | {PC(v['Positif'],n)} | {PC(v['Mitigé'],n)} | {PC(v['Négatif'],n)} | {v['Non noté']} | {mean(pc)} % (sur {len(pc)}) | {lks} |".replace(',',' ',0).replace('| '+f"{sum(r['mots'] for r in rs):,}",'| '+f"{sum(r['mots'] for r in rs):,}".replace(',',' '))
# ---------- tables
sc=[r for r in R if r['source']=='SensCritique']; mn=[r for r in R if r['source']=='Manga-News']
presse=[r for r in R if r['source'] in('Otaku USA Magazine','TheOASG','Nerdbot','Askear')]
bb=[r for r in R if r['source']=='Babelio']
T11=[row11('Goodreads T1',[r for r in GR if r['tome']==1]),row11('Goodreads T2',[r for r in GR if r['tome']==2]),row11('Goodreads T3',[r for r in GR if r['tome']==3]),row11('**Goodreads (total)**',GR,True),
 row11('Babelio T1',[r for r in bb if r['tome']==1]),row11('Babelio T2',[r for r in bb if r['tome']==2]),row11('Babelio T3',[r for r in bb if r['tome']==3]),
 row11('SensCritique T1',[r for r in sc if r['tome']==1]),row11('SensCritique T2',[r for r in sc if r['tome']==2]),row11('SensCritique T3',[r for r in sc if r['tome']==3]),row11('SensCritique série (tous tomes)',[r for r in sc if r['tome'] is None]),
 row11('Manga-News — rédaction (T1, T2)',[r for r in mn if r['author']=='Kiraa7']),row11('Manga-News — lecteurs T1',[r for r in mn if r['author']!='Kiraa7' and r['tome']==1]),row11('Manga-News — lecteurs T2',[r for r in mn if r['author']!='Kiraa7' and r['tome']==2]),row11('Manga-News — lecteurs T3',[r for r in mn if r['author']!='Kiraa7' and r['tome']==3]),
 row11('Presse / blogs (Otaku USA, TheOASG, Nerdbot, Askear)',presse),
 row11('**Autres sites (total)**',AS,True),row11('**TOTAL manga**',R,True)]
def prow(label,key,sets):
    cells=[]
    for rs in sets:
        n=len(rs); a=sum(1 for r in rs if key in r['poles']); cells.append(PC(a,n))
    return cells
RECALL={'D':('96,1 %','97,9 %'),'D1':('90,7 %','88,3 %'),'D2':('42,5 %','81,4 %'),'D3':('50,9 %','53,3 %'),'D4':('36,2 %','36,5 %'),'C':('61,4 %','77,7 %'),'B':('56,2 %','67,7 %'),'B1':('38,6 %','23,4 %'),'B2':('44,0 %','62,0 %'),'A':('59,6 %','56,4 %'),'A1':('57,5 %','54,5 %'),'A2':('3,5 %','2,7 %'),'A3':('9,9 %','10,8 %'),'E':('41,0 %','55,4 %'),'E1':('38,8 %','53,7 %'),'E2':('5,6 %','17,2 %')}
LABEL={'D':'**Pôle D — Narration, Scénario & Histoire**','D1':'↳ `D1` Intrigue, écriture, twists','D2':'↳ `D2` Rythme, arcs, exposition','D3':'↳ `D3` Dramaturgie, enjeux, ton','D4':'↳ `D4` Climax, fin d\'arc, résolution','C':'**Pôle C — Personnages & antagonistes**','B':'**Pôle B — Monde, morale & système**','B1':'↳ `B1` Philosophie, morale, discrimination','B2':'↳ `B2` Worldbuilding, magie, Inquisition','A':'**Pôle A — Visuel strict**','A1':'↳ `A1` Dessin, trait, planches, couleurs','A2':'↳ `A2` Effets de sorts et créatures','A3':'↳ `A3` Chara-design & physique','E':'**Pôle E — Action, chorégraphie & tactique**','E1':'↳ `E1` Intensité, combats','E2':'↳ `E2` Tactique, stratégie, créativité'}
grc=[r for r in cov if r['groupe']=='Goodreads']; asc=[r for r in cov if r['groupe']!='Goodreads']
T21=[]
for k in RECALL:
    a=prow(k,k,[grc,asc,cov,c50]); T21.append(f"| {LABEL[k]} | {a[0]} | {a[1]} | **{a[2]}** | {a[3]} | {RECALL[k][0]} | {RECALL[k][1]} |")
def cnt(rs,k): return sum(1 for r in rs if k in r['poles'])
def ratio(rs,a,b):
    x=cnt(rs,a)/len(rs); y=cnt(rs,b)/len(rs); return f"{x/y:.2f}".replace('.',',')+'×'
T21.append(f"| **Ratio Narration / Visuel (`D / A`)** | {ratio(grc,'D','A')} | {ratio(asc,'D','A')} | **{ratio(cov,'D','A')}** | {ratio(c50,'D','A')} | 1,61× | 1,74× |")
T21.append(f"| **Ratio Visuel / Monde (`A / B`)** | {ratio(grc,'A','B')} | {ratio(asc,'A','B')} | **{ratio(cov,'A','B')}** | {ratio(c50,'A','B')} | 1,06× | 0,83× |")
h=prow('h','HUM',[grc,asc,cov,c50]); T21.append(f"| *Hors grille (ajout de ma part)* : Humour | {h[0]} | {h[1]} | {h[2]} | {h[3]} | non mesuré | non mesuré |")
# categories
def catrow(c):
    rs=[r for r in R if c in r['codes']]; mx=[r for r in rs if r['verdict'] in('Mitigé','Négatif')]
    pc=[r['pct'] for r in rs if r['pct'] is not None]; pm=[r['pct'] for r in mx if r['pct'] is not None]; lk=likes(mx)
    g=sum(1 for r in rs if r['groupe']=='Goodreads')
    return len(rs),g,len(rs)-g,len(mx),mean(pc),mean(pm),med(lk),mean(lk)
T22=[]
order=sorted(CATS,key=lambda c:(-catrow(c)[0],c))
RANK={c:i+1 for i,c in enumerate(order)}
for c in order:
    n,g,a,m,pc,pm,ml,mm=catrow(c)
    T22.append(f"| **{c}. {CATS[c]}** | **{PC(n,N)}** | {g} / {a} | {m} / {NM} ({P(m,NM)}) | {pc} % | {pm} % | {ml} / {mm} |")
withc=sum(1 for r in R if r['codes']); mxc=sum(1 for r in MX if r['codes']); posc=sum(1 for r in R if r['verdict']=='Positif' and r['codes']); npos=vc['Positif']
nnote=sum(1 for r in R if r['verdict']=='Non noté' and r['codes'])
TT=[]
for t,lab in [(1,'T1'),(2,'T2'),(3,'T3'),(None,'Série')]:
    rs=[r for r in R if r['tome']==t]; v=Counter(r['verdict'] for r in rs); n=len(rs)
    TT.append(f"| {lab} | {n} | {v['Positif']} / {v['Mitigé']} / {v['Négatif']} / {v['Non noté']} | "+' | '.join(str(sum(1 for r in rs if c in r['codes'])) for c in ['C1','C2','C3','C4','C5','C6','C7','C8'])+" |")
# periods
PER=[]
for nm,f in [('2013–2017',lambda a:a<=2017),('2018–2020',lambda a:2018<=a<=2020),('2021–2026',lambda a:a>=2021)]:
    rs=[r for r in R if r['annee'] and f(r['annee'])]; v=Counter(r['verdict'] for r in rs); rated=len(rs)-v['Non noté']
    g=[r for r in rs if r['groupe']=='Goodreads']; vg=Counter(r['verdict'] for r in g); rg=len(g)-vg['Non noté']
    PER.append(f"| **{nm}** | {len(rs)} | {PC(v['Positif'],rated) if rated else '—'} | {PC(v['Mitigé'],rated)} | {PC(v['Négatif'],rated)} | {len(g)} | {PC(vg['Positif'],rg) if rg else '—'} | {PC(vg['Mitigé']+vg['Négatif'],rg) if rg else '—'} |")
VER=[]
for v in ('Positif','Mitigé','Négatif','Non noté'):
    rs=[r for r in R if r['verdict']==v]; pc=[r['pct'] for r in rs if r['pct'] is not None]; lk=likes(rs)
    mx=max(lk) if lk else 0; top=[r for r in rs if r['source'] in('Goodreads','SensCritique') and r['likes']==mx][0]
    VER.append(f"| ***{v}*** | {len(rs)} | **{P(len(rs),N)}** | {mean(pc)} % | {med(lk)} | {mean(lk)} | {mx} (`{top['author']}`) |")
# praise among positives
pos_cov=[r for r in cov if r['verdict']=='Positif']; npc=len(pos_cov)
PR={k:cnt(pos_cov,k) for k in ['A1','HUM','C','B2','B1','E1','D1']}
# langues
lg=Counter(r['lang2'] for r in R if r['groupe']=='Goodreads')
ncov_gr=len(grc); nonc=[r for r in R if not r['couvert']]
open('/tmp/vars.txt','w').write(repr(dict(N=N,NC=NC,N50=N50,NM=NM,vc=dict(vc),withc=withc,mxc=mxc,posc=posc,npos=npos,nnote=nnote,PR=PR,npc=npc,lg=dict(lg),nonc=len(nonc),RANK=RANK)))
tables=dict(T11='\n'.join(T11),T21='\n'.join(T21),T22='\n'.join(T22),TT='\n'.join(TT),PER='\n'.join(PER),VER='\n'.join(VER))
import json; json.dump(tables,open('/tmp/tables.json','w'),ensure_ascii=False)
print('\n\n'.join(f"### {k}\n{v}" for k,v in tables.items()))
print(open('/tmp/vars.txt').read())
