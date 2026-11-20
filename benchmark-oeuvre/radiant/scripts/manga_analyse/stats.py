import statistics as st,json,csv
from collections import Counter
from analyse import R,CATS,pct
def mean(x): return f"{st.mean(x):.1f}" if x else '—'
def med(x): return f"{st.median(x):g}" if x else '—'
def row(name,rs):
    n=len(rs); v=Counter(r['verdict'] for r in rs)
    pcts=[r['pct'] for r in rs if r['pct'] is not None]
    lk=[r['likes'] for r in rs if r['source'] in('Goodreads','SensCritique')]
    print(f"| {name} | {n} | {sum(r['mots'] for r in rs)} | {pct(v['Positif'],n)} | {pct(v['Mitigé'],n)} | {pct(v['Négatif'],n)} | {v['Non noté']} | {mean(pcts)} % ({len(pcts)}) | {sum(lk)} | {med(lk)} / {mean(lk)} |")
print('## 1.1')
for t in (1,2,3): row(f'Goodreads T{t}',[r for r in R if r['source']=='Goodreads' and r['tome']==t])
row('Goodreads total',[r for r in R if r['source']=='Goodreads'])
sc=[r for r in R if r['source']=='SensCritique']
row('SC T1',[r for r in sc if r['tome']==1]);row('SC T2',[r for r in sc if r['tome']==2]);row('SC T3',[r for r in sc if r['tome']==3]);row('SC série',[r for r in sc if r['tome'] is None])
row('SensCritique',sc)
mn=[r for r in R if r['source']=='Manga-News']
row('MN rédaction',[r for r in mn if r['author']=='Kiraa7']);row('MN lecteurs T1',[r for r in mn if r['author']!='Kiraa7'])
row('Presse/blogs',[r for r in R if r['source'] in('Otaku USA Magazine','TheOASG','Nerdbot','Askear')])
row('Autres sites',[r for r in R if r['groupe']!='Goodreads']); row('TOTAL',R)
print('## langues'); print(Counter(r['lang2'] for r in R if r['groupe']=='Goodreads'),Counter(r['lang2'] for r in R if r['groupe']!='Goodreads'))
print('## 1.2 verdict')
for v in ('Positif','Mitigé','Négatif','Non noté'):
    rs=[r for r in R if r['verdict']==v]; lk=[r for r in rs if r['source'] in('Goodreads','SensCritique')]
    pc=[r['pct'] for r in rs if r['pct'] is not None]
    print(v,len(rs),mean(pc),med([r['likes'] for r in lk]),mean([r['likes'] for r in lk]),max([r['likes'] for r in lk],default=0),[ (r['id'],r['author']) for r in lk if r['likes']==max([x['likes'] for x in lk],default=0)][:1])
print('## périodes')
for nm,f in [('2013-2017',lambda a:a<=2017),('2018-2020',lambda a:2018<=a<=2020),('2021-2026',lambda a:a>=2021)]:
    rs=[r for r in R if r['annee'] and f(r['annee'])]; v=Counter(r['verdict'] for r in rs); n=len(rs)
    rated=n-v['Non noté']
    print(nm,n,dict(v), 'Pos% sur notés',round(100*v['Positif']/rated,1),'Mix+Neg%',round(100*(v['Mitigé']+v['Négatif'])/rated,1))
    for g in ('Goodreads','Autres sites'):
        rr=[r for r in rs if r['groupe']==g]; vv=Counter(r['verdict'] for r in rr); print('   ',g,len(rr),dict(vv))
print('## notes GR distribution',Counter((r['tome'],r['note']) for r in R if r['source']=='Goodreads'))
print('## cats')
MX=[r for r in R if r['verdict'] in('Mitigé','Négatif')]
print('MixNeg N',len(MX),'avec cat',sum(1 for r in MX if r['codes']),'total avec cat',sum(1 for r in R if r['codes']),'Pos avec cat',sum(1 for r in R if r['verdict']=='Positif' and r['codes']), 'Pos N',sum(1 for r in R if r['verdict']=='Positif'))
for c in CATS:
    rs=[r for r in R if c in r['codes']]; mx=[r for r in rs if r['verdict'] in('Mitigé','Négatif')]
    pc=[r['pct'] for r in rs if r['pct'] is not None]; pcm=[r['pct'] for r in mx if r['pct'] is not None]
    lk=[r['likes'] for r in mx if r['source'] in('Goodreads','SensCritique')]
    g=sum(1 for r in rs if r['groupe']=='Goodreads')
    t=Counter(r['tome'] for r in rs)
    print(c,len(rs),f"GR{g}/AS{len(rs)-g}",'MixNeg',len(mx),mean(pc),mean(pcm),med(lk),mean(lk),'tomes',dict(t),'lang',dict(Counter(r['lang2'] for r in rs)),'Pos',sum(1 for r in rs if r['verdict']=='Positif'))
print('## par tome verdict')
for t in (1,2,3,None):
    rs=[r for r in R if r['tome']==t]; print(t,len(rs),dict(Counter(r['verdict'] for r in rs)),{c:sum(1 for r in rs if c in r['codes']) for c in CATS})
json.dump([{k:(sorted(v) if isinstance(v,set) else v) for k,v in r.items()} for r in R],open('/home/user/radiant_manga_analyse/codage_critiques_radiant_manga.json','w'),ensure_ascii=False,indent=1)
with open('/home/user/radiant_manga_analyse/codage_critiques_radiant_manga.csv','w',newline='',encoding='utf8') as f:
    w=csv.writer(f); w.writerow(['id','source','groupe','tome','auteur','langue','note','echelle','note_pct','verdict','date','likes','mots','categories_C','poles_lexique'])
    for r in R: w.writerow([r['id'],r['source'],r['groupe'],r['tome'],r['author'],r['lang2'],r['note'],r['echelle'],'' if r['pct'] is None else round(r['pct'],1),r['verdict'],r['date'],r['likes'],r['mots'],' '.join(r['codes']),' '.join(sorted(r['poles'])) if r['couvert'] else 'non couvert'])
