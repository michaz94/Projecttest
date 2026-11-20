"""Analyse d'un vote TierMaker en direct, paliers personnalisés (25 oct. 2026 ; v1 = analyse_live_tiermaker.py, 5 paliers S-D).
Usage : python3 analyse_live_tiermaker_v2.py live.json dossier_sortie [paliers exclus séparés par |]
Règle choisie par l'utilisateur (24 oct.) : les paliers sous D (« Hard Pass », « Ewwwwww ») sont la note la plus basse d'une échelle continue
(6 paliers notés -> 6 à 1) ; « Who? » (= je ne connais pas) est retiré : ces votes ne comptent ni dans la moyenne ni dans les votants.
Sorties : classement_average_avec_incertitude.csv/.json (mêmes colonnes que la v1 + palier_bas, exclus, moyenne_sur_5).
moyenne_sur_5 = 1 + (moyenne-1)*4/(k-1) : simple changement d'échelle pour comparer aux votes S-D (même ordre)."""
import json,sys,csv,os,numpy as np
from scipy.stats import spearmanr
src,out=sys.argv[1],sys.argv[2]; EXCL=set(sys.argv[3].split('|')) if len(sys.argv)>3 and sys.argv[3] else set()
import gzip; d=json.load(gzip.open(src,'rt') if src.endswith('.gz') else open(src)); _L=lambda x: json.loads(x) if isinstance(x,str) else x
KEYS=[_L(x)['labelKey'] for x in d['images'][0]['rawLabels']]; G=[k for k in KEYS if k not in EXCL]; k=len(G)
W=np.arange(k,0,-1).astype(float); print('paliers notés',dict(zip(G,W)),'| exclus',[x for x in KEYS if x in EXCL])
names=[];C=[];X=[];pos=[]
for im in d['images']:
    labs={_L(x)['labelKey']:_L(x)['totalVotes'] for x in im['rawLabels']}
    C.append([labs.get(g,0) for g in G]); X.append(sum(labs.get(e,0) for e in EXCL)); names.append(im['url'].rsplit('/',1)[1]); pos.append(im['originalPosition'] if im.get('originalPosition') is not None else len(pos)+1)  # vote en cours : position absente -> ordre du fichier
C=np.array(C); X=np.array(X); n=C.sum(1); mean=(C*W).sum(1)/n
sd=np.sqrt((C*(W-mean[:,None])**2).sum(1)/(n-1)); se=sd/np.sqrt(n)
print('images',len(n),'votants min/med/max',n.min(),int(np.median(n)),n.max(),'| rho position~votants',round(spearmanr(pos,n)[0],2))
rng=np.random.default_rng(0);B=2000;P=C/n[:,None];ranks=np.zeros((B,len(n)),int)
for b in range(B):
    m=rng.multinomial(n,P).dot(W)/n; ranks[b]=(-m).argsort().argsort()+1
p1=(ranks==1).mean(0);lo=np.percentile(ranks,2.5,0);hi=np.percentile(ranks,97.5,0)
gm=(C*W).sum()/n.sum();mp=np.median(n);bay=(n*mean+mp*gm)/(n+mp);br=np.empty(len(n),int);br[np.argsort(-bay)]=np.arange(1,len(n)+1)
order=np.argsort(-mean,kind='stable')
rows=[]
for r,i in enumerate(order):
    row=dict(rang_average=r+1,personnage='',image=names[i],position=int(pos[i]),votants=int(n[i]))
    for j,lab in enumerate(['S','A','B','C','D']): row[lab]=int(C[i,j])
    row['palier_bas']=int(C[i,5]) if k>5 else ''
    if k>6: row['palier_bas2']=int(C[i,6])  # 7 paliers (ex. 73568440 : I love you, Ma gurl, AMAZING, Good, Mid, Ew, GET OUT)
    assert k<=7
    row['exclus']=int(X[i]) if EXCL else ''
    row.update(moyenne=round(float(mean[i]),3),moyenne_sur_5=round(float(1+(mean[i]-1)*4/(k-1)),3),marge95=round(float(1.96*se[i]),3),
               p_numero1=round(float(p1[i]),3),rang_min95=int(lo[i]),rang_max95=int(hi[i]),rang_bayesien=int(br[i]))
    rows.append(row)
os.makedirs(out,exist_ok=True)
json.dump(rows,open(out+'/classement_average_avec_incertitude.json','w'),indent=0,ensure_ascii=False)
with open(out+'/classement_average_avec_incertitude.csv','w',newline='',encoding='utf-8') as o:
    w=csv.DictWriter(o,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
for r in rows[:12]: print(r['rang_average'],r['image'][:50],r['moyenne'],'±',r['marge95'],r['votants'],f"[{r['rang_min95']}-{r['rang_max95']}]")
