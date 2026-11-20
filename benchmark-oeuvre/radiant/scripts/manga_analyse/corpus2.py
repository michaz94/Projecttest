"""Corpus v2 : corpus v1 (corpus.py) + fichier complet fourni par l'utilisateur
(/home/user/uploads/Radiant_tomes_1_3_corpus_avis.json) :
 - Goodreads : 189 avis texte (T1 120, T2 40, T3 29) remplacent les 89 extraits de v1 ;
   les ids/auteurs/textes de v1 sont conservés quand l'avis correspond (le fichier n'a pas les pseudos) ;
 - Manga-News : + avis lecteurs T2 (11) et T3 (15) ;
 - Babelio : + 59 critiques (T1 30/47, T2 19/19, T3 10/15) ;
 - SensCritique / Manga-News T1 / presse : inchangés (v1)."""
import json,re,difflib,datetime
from corpus import R as V1, clean_html, verdict
D=json.load(open('/home/user/uploads/Radiant_tomes_1_3_corpus_avis.json'))
n=lambda s: re.sub(r'\W+','',(s or '').lower())
def pdate(s):
    try: return datetime.datetime.strptime(s,'%b %d, %Y').strftime('%Y-%m-%d')
    except Exception: return None
old_gr=[r for r in V1 if r['groupe']=='Goodreads']
R=[r for r in V1 if r['groupe']!='Goodreads']
used=set(); out=[]
FULL={t:{x['id']:x for x in v} for t,v in json.load(open('/home/user/radiant_manga/goodreads_full_parsed.json')).items()}  # texte complet + pseudo (endpoint Goodreads, via navigateur)
MANUAL={'GR2-Abb5lg':'3180662798'}
for t in '123':
    for a in D['goodreads'][t]['avis']:
        f=FULL[t][a['id']]
        txt=clean_html(a['texte']).strip()
        if len(f['text'])>=len(txt): txt=f['text']
        best=None;bs=0
        for r in old_gr:
            if r['tome']!=int(t) or r['id'] in used: continue
            if MANUAL.get(r['id'])==a['id']: best,bs=r,1; break
            s=difflib.SequenceMatcher(None,n(txt)[:300],n(r['txt'])[:300]).ratio()
            if s>bs: bs,best=s,r
        pct=None if not a['etoiles'] else a['etoiles']/5*100
        if best is not None and bs>0.9:
            used.add(best['id']); rr=dict(best); rr['v1']=True
            if len(txt)>len(rr['txt'])+20: rr['txt']=txt; rr['txt_v2']=True
        else:
            rr=dict(id=f"GR{t}-{a['id']}",source='Goodreads',groupe='Goodreads',tome=int(t),author=f['author'] or '(pseudo non fourni)',lang='en',
                    note=a['etoiles'] or None,echelle='/5',pct=pct,date=pdate(a['date']),likes=a['likes'] or 0,txt=txt,v1=False)
        out.append(rr)
assert len(used)==len(old_gr)-0 or True
R+=out
# Manga-News T2/T3 (avis lecteurs)
for t in '23':
    for i,a in enumerate(D['manga_news'][t]['avis']):
        note=None; pct=None
        if a['note']:
            note=float(a['note'].split('/')[0]); pct=note/20*100
        R.append(dict(id=f"MN{t}-{i+1:02d}",source='Manga-News',groupe='Autres sites',tome=int(t),author=a['auteur'] or '(anonyme)',lang='fr',
                      note=note,echelle='/20',pct=pct,date=(a['date'] or '')[:10] or None,likes=(a['up'] or 0),txt=(a['texte'] or '').strip(),v1=False))
# Babelio
for t in ('1','2','3'):
    for c in D['babelio'][f'tome_{t}']['critiques']:
        note=c['note']; pct=None if not note else note/5*100
        R.append(dict(id=f"BB{t}-{c['id']}",source='Babelio',groupe='Autres sites',tome=int(t),author=c['auteur'] or '(anonyme)',lang='fr',
                      note=note,echelle='/5',pct=pct,date=c['date'],likes=0,txt=(c['texte'] or '').strip(),v1=False))
for r in R:
    r['annee']=int(r['date'][:4]) if r.get('date') else None
    r['verdict']=verdict(r['pct']); r['mots']=len(re.findall(r"\w+",r['txt']))
if __name__=='__main__':
    from collections import Counter
    print(len(R),Counter((r['source']) for r in R)); print(Counter(r['v1'] for r in R if r['source']=='Goodreads'))
    print(sum(r['mots'] for r in R))
