from corpus2 import R as RAW
from langdetect import detect, DetectorFactory
DetectorFactory.seed=0
DROP={'GR2-jQatvQ','GR3-bd_6Qw',   # copies identiques (même auteur, même texte) postées sur T2 et T3
      'AS011','AS014',              # SensCritique : copies à 100 % de deux avis Goodreads de Sunread26 (T2 et T3)
      # --- v2 (fichier complet fourni) : même avis publié sur plusieurs sites -> une seule copie (la plus longue ; à égalité, Goodreads/déjà codée)
      'MN3-09','MN3-10',                     # « triplon » eques (Manga-News T3) : MN3-08 gardé
      'AS006','BB1-3554313',                  # Sunread26 T1 : copie Goodreads GR1-6015687397 gardée
      'BB2-3706680','BB3-3757193',           # Sunread26 T2/T3 : copies Goodreads gardées
      'BB2-2068127',                         # Zutto T2 : copie Goodreads (plus longue) gardée
      'BB3-3742609','BB2-3742466',           # Tachan T3/T2 : copies Goodreads gardées
      'GR1-3638042226','GR2-2GWfeQ','GR3-rSqXAw',
      # Manga-News T2/T3 : commentaires d'annonce (date de sortie, nombre de tomes) sans avis sur l'œuvre
      'MN2-08','MN2-09','MN2-10','MN2-11','MN3-12','MN3-13','MN3-14'}  # Drine Psylook / LeManegeDePsy… : copies Babelio (plus longues) gardées
AUTHOR={'BB1-2417233':'Drine Psylook (Babelio : LeManegeDePsy…)','BB2-3173176':'Drine Psylook (Babelio : LeManegeDePsy…)','BB3-3269430':'Drine Psylook (Babelio : LeManegeDePsy…)'}
LANG_FIX={'GR1-4862245087':'en','GR1-8582776166':'es','GR1-3729033343':'es','GR1-8693534366':'ca','GR1-5157575441':'en'}
EXCL_ANIME={'AS019'}               # Shigeo (SensCritique, page série) : parle de « cet anime », pas du manga
R=[]
for r in RAW:
    if r['id'] in DROP or r['id'] in EXCL_ANIME: continue
    if r['id'] in AUTHOR: r['author']=AUTHOR[r['id']]
    try: r['lang2']=detect(r['txt']) if r['mots']>=4 else 'short'
    except: r['lang2']='short'
    if r['source'] in ('Manga-News','SensCritique','Askear','Babelio') : r['lang2']='fr'
    if r['source'] in ('Nerdbot','TheOASG','Otaku USA Magazine'): r['lang2']='en'
    if r['id'] in ('AS024','AS028'): r['lang2']='fr'
    if r['id'] in LANG_FIX: r['lang2']=LANG_FIX[r['id']]
    r['couvert']= r['lang2'] in ('en','fr')   # langues couvertes par les lexiques
    if r['id']=='AS051': r['verdict']='Négatif'; r['verdict_lu']=True   # TheOASG : note « 2 » sans échelle ; texte négatif
    if r['id']=='AS050': r['verdict']='Positif'; r['verdict_lu']=True  # Otaku USA : pas de note ; texte positif
    R.append(r)
if __name__=='__main__':
    from collections import Counter
    print(len(R),Counter(r['groupe'] for r in R),Counter(r['lang2'] for r in R),Counter(r['verdict'] for r in R))
