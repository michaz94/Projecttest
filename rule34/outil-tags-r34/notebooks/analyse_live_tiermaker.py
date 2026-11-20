"""Analyse d'un vote en direct TierMaker (fichier JSON de server.tiermaker.com/v1/live-event/{id}).
Usage : python3 analyse_live_tiermaker.py chemin.json dossier_sortie
Sorties : classement_average_avec_incertitude.json/.csv + apercu/topN.jpg
Moyenne S=5..D=1 ; marge 95 % = 1,96 x écart-type / racine(n) ;
simulation : 2000 rejeux multinomiaux -> P(n°1) et fourchette de rang 95 % ;
rang pondéré : moyenne bayésienne (prior = moyenne globale, poids = nb médian de votants)."""
import json,sys,csv,io,urllib.request,os,numpy as np
from scipy.stats import spearmanr
from PIL import Image, ImageDraw
src,out=sys.argv[1],sys.argv[2]; N=int(sys.argv[3]) if len(sys.argv)>3 else 24
d=json.load(open(src)); W=np.array([5,4,3,2,1])
# paliers dans l'ordre affiché (du meilleur au pire) ; gère les libellés personnalisés
_L=lambda x: json.loads(x) if isinstance(x,str) else x
KEYS=[_L(x)['labelKey'] for x in d['images'][0]['rawLabels']]
assert len(KEYS)==5, KEYS
print('paliers (5 -> 1) :',KEYS)
names=[];C=[];pos=[];urls=[]
for im in d['images']:
    labs={_L(x)['labelKey']:_L(x)['totalVotes'] for x in im['rawLabels']}
    C.append([labs.get(k,0) for k in KEYS]); urls.append(im['url']); names.append(im['url'].rsplit('/',1)[1]); pos.append(im['originalPosition'])
C=np.array(C); n=C.sum(1); mean=(C*W).sum(1)/n
sd=np.sqrt((C*(W-mean[:,None])**2).sum(1)/(n-1)); se=sd/np.sqrt(n)
print('images',len(n),'votants min/med/max',n.min(),int(np.median(n)),n.max(),'| rho position~votants',round(spearmanr(pos,n)[0],2),'| rho position~moyenne',round(spearmanr(pos,mean)[0],2))
rng=np.random.default_rng(0);B=2000;P=C/n[:,None];ranks=np.zeros((B,len(n)),int)
for b in range(B):
    m=np.array([rng.multinomial(n[i],P[i]) for i in range(len(n))]).dot(W)/n
    ranks[b]=(-m).argsort().argsort()+1
p1=(ranks==1).mean(0);lo=np.percentile(ranks,2.5,0);hi=np.percentile(ranks,97.5,0)
gm=(C*W).sum()/n.sum();mp=np.median(n);bay=(n*mean+mp*gm)/(n+mp);br=np.empty(len(n),int);br[np.argsort(-bay)]=np.arange(1,len(n)+1)
order=np.argsort(-mean)
rows=[dict(rang_average=k+1,personnage='',image=names[i],position=int(pos[i]),votants=int(n[i]),S=int(C[i,0]),A=int(C[i,1]),B=int(C[i,2]),C=int(C[i,3]),D=int(C[i,4]),moyenne=round(float(mean[i]),3),marge95=round(float(1.96*se[i]),3),p_numero1=round(float(p1[i]),3),rang_min95=int(lo[i]),rang_max95=int(hi[i]),rang_bayesien=int(br[i])) for k,i in enumerate(order)]
os.makedirs(out+'/apercu',exist_ok=True)
json.dump(rows,open(out+'/classement_average_avec_incertitude.json','w'),indent=0,ensure_ascii=False)
w=csv.DictWriter(open(out+'/classement_average_avec_incertitude.csv','w',newline='',encoding='utf-8'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
for r in rows[:N]: print(r['rang_average'],r['image'][:40],r['moyenne'],'±',r['marge95'],r['votants'],f"P1={r['p_numero1']:.0%}",f"[{r['rang_min95']}-{r['rang_max95']}]",'b',r['rang_bayesien'])
tiles=[]
for r,i in zip(rows[:N],order[:N]):
    try:
        b=urllib.request.urlopen(urllib.request.Request(urls[i],headers={'User-Agent':'Mozilla/5.0','Referer':'https://tiermaker.com/'}),timeout=20).read();im=Image.open(io.BytesIO(b)).convert('RGB')
    except Exception as e: im=Image.new('RGB',(200,200),'grey')
    im.thumbnail((220,220));t=Image.new('RGB',(230,250),'white');t.paste(im,(5,5));ImageDraw.Draw(t).text((5,232),f"#{r['rang_average']}",fill='black');tiles.append(t)
cols=6;sheet=Image.new('RGB',(230*cols,250*((len(tiles)+cols-1)//cols)),'white')
for k,t in enumerate(tiles): sheet.paste(t,((k%cols)*230,(k//cols)*250))
sheet.save(out+f'/apercu/top{N}.jpg',quality=85)
