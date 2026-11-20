import sys,json,statistics,collections
sys.path.insert(0,'/home/user/radiant_analyse')
from codage import *
# --- codage manuel des critiques récurrentes (après lecture des 48 textes) ---
K={
'K1':("Démarrage lent / rythme inégal (≈10 premiers épisodes ou 1re moitié de S1 ; lenteur de S2)",
  {1:[0,1,2,3,4,5,7,8,9,10,12,13,14,16,18,19,20,21,25,26,32,35],2:[9,10]}),
'K2':("Héros (Seth) et/ou casting jugés génériques, bêtes, irritants ou peu profonds",
  {1:[0,1,3,5,6,7,8,9,12,13,14,16,18,19,21,25,26,30,31,35],2:[6,8,11]}),
'K3':("Dérivatif / « shōnen standard » (Naruto, One Piece, Black Clover, Fairy Tail)",
  {1:[0,1,3,5,9,11,12,15,16,18,19,22,26,30,33,34,35],2:[6,8]}),
'K4':("Ton enfantin et/ou humour qui casse la tension ou tombe à plat",
  {1:[1,11,12,14,16,18,19,35],2:[6]}),
'K5':("Surexplication, bavardage, répétition de l'objectif (« beaucoup de paroles, peu d'action »)",
  {1:[0,9,18,27,31,35],2:[11]}),
'K6':("Adaptation jugée appauvrie par rapport au manga (ton, personnages, couleurs, rythme)",
  {1:[13,16,19,25],2:[0]}),
'K7':("Enjeux faibles, incohérences ou logique du monde (humains « tous racistes », pas de conséquences)",
  {1:[6,11,12,18,33,35],2:[6]}),
'K8':("Animation / visuel jugé moyen, plat ou paresseux",
  {1:[1,3,10,19,25,32,35],2:[6]}),
}
P={'P1':("« Ça décolle » après ≈ ép. 10-11 (arc Rumble Town) / 2e moitié de S1",{1:[1,3,5,7,8,9,10,13,14,18,19,20,21,22,32],2:[]}),
   'P2':("La saison 2 est jugée meilleure que la saison 1",{1:[19,28],2:[0,1,2,3,4,5,6,7]}) }
# P2 S1-28 (Elyshion) et S1-19, S1-29 mentionnent aussi S2 meilleure : on ne compte que S2 + S1 listés après vérification
for r in reviews:
    n=int(r['id'].split('-')[1]); r['K']=[k for k,(l,m) in K.items() if n in m[r['saison']]]
    r['P']=[k for k,(l,m) in P.items() if n in m[r['saison']]]
def med(x): return statistics.median(x) if x else None
def mean(x): return statistics.mean(x) if x else None
def pct(a,b): return f"{a} ({100*a/b:.1f} %)".replace('.',',')
REN={'K1':'C1','K2':'C2','K3':'C3','K4':'C4','K8':'C5','K5':'C6','K7':'C7','K6':'C8'}
json.dump([{**{k:(sorted(v) if isinstance(v,set) else v) for k,v in r.items() if k not in ('txt','K')},'C':sorted(REN[k] for k in r['K'])} for r in reviews],open('/home/user/radiant_analyse/codage_critiques_radiant_anime_MAL.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    groups={'S1':[r for r in reviews if r['saison']==1],'S2':[r for r in reviews if r['saison']==2],'T':reviews}
    print("== tab 1.1")
    for g,R in groups.items():
        c=collections.Counter(r['tag'] for r in R); n=len(R)
        print(g,n,sum(r['mots'] for r in R),c['Recommended'],c['Mixed Feelings'],c['Not Recommended'],round(mean([r['note'] for r in R]),2),med([r['note'] for r in R]),sum(r['react'] for r in R),med([r['react'] for r in R]),round(mean([r['react'] for r in R]),1))
    print("== 1.2")
    for t in ['Recommended','Mixed Feelings','Not Recommended']:
        R=[r for r in reviews if r['tag']==t]; print(t,len(R),round(mean([r['note'] for r in R]),2),med([r['note'] for r in R]),med([r['react'] for r in R]),round(mean([r['react'] for r in R]),1),max(R,key=lambda r:r['react'])['auteur'],max(r['react'] for r in R))
    for lab,f in [('2018-2020',lambda r:r['annee']<=2020),('2021-2026',lambda r:r['annee']>=2021)]:
        R=[r for r in reviews if f(r)]; c=collections.Counter(r['tag'] for r in R); print(lab,len(R),c)
    print("== 2.1 poles")
    poles={'D':['D1','D2','D3','D4'],'C':['C'],'B':['B1','B2'],'A':['A1','A2','A3'],'E':['E1','E2']}
    def cnt(R,codes): return sum(1 for r in R if any(c in r['codes'] for c in codes))
    for name,codes in list(poles.items())+[(c,[c]) for c in ['D1','D2','D3','D4','B1','B2','A1','A2','A3','E1','E2','SON','HUM']]:
        print(name,[cnt(groups[g],codes) for g in ('S1','S2','T')],[round(100*cnt(groups[g],codes)/len(groups[g]),1) for g in ('S1','S2','T')])
    D=cnt(reviews,poles['D']);A=cnt(reviews,poles['A']);B=cnt(reviews,poles['B']); print('D/A',D/A,'A/B',A/B)
    for g in ('S1','S2'):
        R=groups[g]; print(g,'D/A',cnt(R,poles['D'])/cnt(R,poles['A']),'A/B',cnt(R,poles['A'])/cnt(R,poles['B']))
    print("== 2.2 criticisms")
    MN=[r for r in reviews if r['tag']!='Recommended']; print('MN',len(MN))
    for k,(lab,m) in K.items():
        R=[r for r in reviews if k in r['K']]; M=[r for r in R if r['tag']!='Recommended']
        print(k,len(R),[sum(1 for r in R if r['saison']==s) for s in (1,2)],len(M),round(100*len(M)/len(MN),1),round(mean([r['note'] for r in R]),2),round(mean([r['note'] for r in M]),2) if M else None,med([r['react'] for r in M]),round(mean([r['react'] for r in M]),1) if M else None, lab[:50])
    cov=[r for r in MN if r['K']]; print('couverture MN',len(cov),len(MN))
    allcov=sum(1 for r in reviews if r['K']); print('reviews avec >=1 K',allcov)
    for p,(lab,m) in P.items():
        R=[r for r in reviews if p in r['P']]; print(p,len(R),[sum(1 for r in R if r['saison']==s) for s in (1,2)])
    # nb de K par avis recommandé
    print('Recommended avec ≥1 K',sum(1 for r in reviews if r['tag']=='Recommended' and r['K']),sum(1 for r in reviews if r['tag']=='Recommended'))
