import re,json,html
from bs4 import BeautifulSoup
MOIS={'Janvier':1,'Février':2,'Mars':3,'Avril':4,'Mai':5,'Juin':6,'Juillet':7,'Août':8,'Septembre':9,'Octobre':10,'Novembre':11,'Décembre':12}
def soup(f):
    s=BeautifulSoup(open(f,encoding='utf8').read(),'html.parser')
    for t in s(['script','style']): t.decompose()
    return s
def clean(t): return re.sub(r'\s+',' ',t).strip()
out=[]
# ---- SensCritique
sc=json.load(open('senscritique_raw.json'))
tomes={'t1':1,'t2':2,'t3':3,'serie':None}
for r in sc:
    out.append(dict(source='SensCritique',type='lecteur',tome=tomes[r['scope']],niveau='tome' if r['scope']!='serie' else 'série',
      url=r['url'],review_id=r['review_id'],author=r['author'],rating=r['rating'],rating_scale='/10',
      date=(r['date'] or '')[:10],title=r['title'],likes=r['likes'],comments=r['comments'],language='fr',note=None,
      text=html.unescape(r['text'] or ''),text_complete=bool(r['text']) and len(r['text'])>=len(re.sub(r'…$','',r['text_short'] or ''))-5))
# ---- Manga-News critique rédac
def mn_crit(f,tome,url):
    t=soup(f).get_text('\n',strip=True)
    i=t.find('Critique du volume manga'); j=t.find("Critique 1 : L'avis du chroniqueur")
    blk=t[i:j].split('\n'); date=blk[1].replace('Publiée le ','')
    m=re.search(r'(\d+) (\w+) (\d{4})',date); d=f"{m.group(3)}-{MOIS[m.group(2)]:02d}-{int(m.group(1)):02d}"
    body='\n'.join(blk[2:])
    k=t[j:].split('\n'); author=k[1]; note=int(k[2])
    return dict(source='Manga-News',type='rédaction',tome=tome,niveau='tome',url=url,review_id=None,author=author,rating=note,rating_scale='/20',date=d,title=None,likes=None,comments=None,language='fr',text=body,text_complete=True)
out.append(mn_crit('pw_mn1.html',1,'https://www.manga-news.com/index.php/manga/critique/Radiant/vol-1'))
out.append(mn_crit('pw_mn2.html',2,'https://www.manga-news.com/index.php/manga/critique/Radiant/vol-2'))
# ---- Manga-News avis lecteurs T1
t=soup('pw_mna1.html').get_text('\n',strip=True)
t=t[t.find('- populaires')+len('- populaires'):]
t=t[:t.rfind('Répondre')+len('Répondre')]
blocks=[b for b in re.split(r'\nRépondre\n?',t+'\n') if b.strip()]
ents=[]
for b in blocks:
    b=b.strip()
    m=re.match(r'De\n(.+?)\n(?:\[\n(\d+) Pts\n\])?, le (\d+) (\w+) (\d{4}) à (\d+)h(\d+)\n?(.*)',b,re.S)
    if not m: print('NOPARSE',b[:80]); continue
    au,pts,dd,mo,yy,hh,mm,rest=m.groups()
    rest=rest.strip(); rating=None
    rm=re.match(r'(\d+)/20\n?',rest)
    if rm: rating=int(rm.group(1)); rest=rest[rm.end():].strip()
    # note de fin éventuelle
    rm2=re.search(r'\n(\d+)/20$',rest)
    if rm2 and rating is None: rating=int(rm2.group(1)); rest=rest[:rm2.start()].strip()
    ents.append(dict(author=au,date=f"{yy}-{MOIS[mo]:02d}-{int(dd):02d}",time=f"{int(hh):02d}:{mm}",rating=rating,text=rest.replace('\n',' ') if False else rest,pts=pts))
# fusion note + texte (même auteur, même horodatage)
merged=[]
for e in ents:
    key=(e['author'],e['date'],e['time'])
    if merged and merged[-1]['key']==key:
        p=merged[-1]
        if e['rating'] is not None and p['rating'] is None: p['rating']=e['rating']
        if e['text'] and not p['text']: p['text']=e['text']
        elif e['text'] and p['text'] and e['text']!=p['text']: p['text']+='\n'+e['text']
    else: merged.append(dict(key=key,**{k:e[k] for k in ['author','date','time','rating','text']}))
print('MN avis',len(ents),'->',len(merged))
for e in merged:
    out.append(dict(source='Manga-News',type='lecteur',tome=1,niveau='tome',url='https://www.manga-news.com/index.php/manga/avis/Radiant/vol-1',review_id=None,author=e['author'],rating=e['rating'],rating_scale='/20',date=e['date'],title=None,likes=None,comments=None,language='fr',text=e['text'],text_complete=True,
        note='commentaire avant la sortie du tome 1 (juin 2013)' if e['date']<'2013-06-30' else None))
# ---- presse anglophone / blogs
def body(f,start,end):
    x=clean(soup(f).get_text(' ',strip=True)); start=clean(start); i=x.find(start); j=x.find(end,i); assert i>=0 and j>i,(f,i,j); return x[i:j].replace(' , ',', ').replace(' .','.').replace(' ,',',')
ot=body('pw_otaku.html','Depending on what generation','Publisher:')
out.append(dict(source='Otaku USA Magazine',type='presse',tome=1,niveau='tome',url='https://otakuusamagazine.com/radiant-review/',review_id=None,author='David Estrella',rating=None,rating_scale=None,date='2018-11-02',title='Radiant [Review]',likes=None,comments=None,language='en',text=ot,text_complete=True,note='édition Viz ; pas de note chiffrée ; classement âge « T »'))
oa=body('pw_oasg.html',"It’s been a while since I’ve seen",'Like this:')
intro=body('pw_oasg.html',"In a strange world where people live",'It’s been a while')
out.append(dict(source='TheOASG',type='presse',tome=1,niveau='tome',url='https://www.theoasg.com/reviews/manga/radiant-volume-1-review/10867',review_id=None,author='Helen',rating=2,rating_scale='non précisée sur la page (« OVERALL SCORE 2 »)',date='2018-11-08',title='Radiant Volume 1 Review',likes=None,comments=None,language='en',text=intro+' '+oa,text_complete=True,note='édition Viz ; exemplaire de presse fourni par Viz'))
nb=body('pw_nerdbot.html','Radiant is a 2013 manga','Do You Want to Know More?')
out.append(dict(source='Nerdbot',type='presse',tome=1,niveau='tome',url='https://nerdbot.com/2018/08/30/nerdbot-manga-review-radiant-by-tony-valente/',review_id=None,author=None,rating=3.5,rating_scale='/5',date='2018-08-30',title='Nerdbot Manga Review: Radiant by Tony Valente',likes=None,comments=None,language='en',text=nb,text_complete=True,note='édition Viz ; exemplaire de presse'))
x=soup('pw_askear.html').get_text('\n',strip=True); i=x.find('Encore un shonen'); j=x.find('REDACTEUR')
out.append(dict(source='Askear',type='presse',tome=1,niveau='tome',url='https://www.askear.com/radiant.php',review_id=None,author='Cocopanzer',rating=3.8,rating_scale='/5',date=None,title=None,likes=None,comments=None,language='fr',text=clean(x[i:j]).replace(' Tony Valente ',' Tony Valente '),text_complete=True,note='date non indiquée sur la page ; critique après lecture du tome 1'))
for o in out:
    if o['source']=='SensCritique' and o['text'].startswith('Chronique complète'):
        m=re.match(r'Chronique complète :\s*\"\"\"\s*\[(https?://[^\]]+)\]\[1\]\s*\"\"\"\s*Extrait :\s*',o['text'])
        assert m
        o['note']='extrait d\'un article de blog repris sur SensCritique : '+m.group(1)
        t=o['text'][m.end():]
        t=re.sub(r'\s*\[1\]:\s*\S+\s*$','',t).strip()
        o['text']=t
for n,o in enumerate(out,1):
    o['id']=f"AS{n:03d}"; o['words']=len(o['text'].split()) if o['text'] else 0
json.dump(out,open('critiques_manga_autres_sites_raw.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(out),Counter((o['source'],o['tome']) for o in out),sum(o['words'] for o in out))
print([ (o['id'],o['source'],o['author'],o['words']) for o in out if o['words']<8])
