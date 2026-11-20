"""Compte des themes de reproches dans les avis collectes (data/*.json). Ne modifie rien."""
import json,re,html
from collections import Counter
gr=json.load(open('data/goodreads_communaute_1_2_raw.json'))
sc=json.load(open('data/senscritique_communaute_raw.json'))
gr['3']=json.load(open('data/goodreads_communaute_3_raw.json'))
def clean(t): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t or '')))
# Avis qui franchissent la limite anti-spoil (tomes suivants) : non affiches
SPOIL=re.compile(r'two towers|return of the king|deux tours|retour du roi|\bfaramir|th[eé]oden|\bsaruman.{0,40}(fall|defeat)|shelob|mount doom|mont du destin|boromir.{0,40}(die|death|dead|mort|meurt)|gandalf.{0,30}(die|death|dead|returns|white)|\bsmeagol|gollum.{0,40}(fall|bit|ring)|\bspoiler',re.I)
THEMES={
 'lent / ennui / dull':r'\bslow|boring|bored|dull|tedious|slog|plodding|drag|lent|ennuy|laborieu|longueur|interminable',
 'Tom Bombadil':r'bombadil|bombadilo',
 'chansons / poèmes':r'\bsongs?\b|poems?\b|poetry|singing|chansons?|po[eè]mes?|\bsing\b',
 'descriptions / détails':r'descriptions?|describ|detail|geograph|scenery|d[eé]tail',
 'marche / voyage':r'walking|\bwalk|marche|\btravel|journey|trek',
 'personnages plats / indistincts':r'flat|interchangeable|one-dimensional|characters? (?:are|were|lack)|personnages? (?:plat|peu)|psycholog',
 'prologue / exposition':r'prologue|exposition|infodump|info-dump|backstory|history lesson|\bgenealog',
 'langue / style / lourd':r'prose|writing style|style|archaic|verbose|wordy|lourd|syntax',
 'film mieux / après film':r'\bmovies?\b|\bfilms?\b|jackson|film|adaptation',
 "pas d'action / rien ne se passe":r'nothing happen|no action|little action|where is the action|rien ne se passe|peu d.action|nothing much',
 'manichéisme / morale':r'manich|black and white|good vs\.? evil|good and evil|moral',
 'fin / non conclusif':r'ending|no ending|cliffhanger|\bend of\b|abrupt|sans fin|inachev',
 'Fondcombe/Conseil/Moria (partie jugée meilleure)':r'rivendell|council|moria|lothl|fondcombe|conseil|lorien',
 'Bree / Strider / Grands-Pas (moment où ça démarre)':r'\bbree\b|strider|aragorn|grands-pas',
 'abandon (DNF)':r'\bdnf\b|did not finish|didn.t finish|couldn.t finish|gave up|abandon|stopped reading|never finished',
}
def rows():
    for k in ('1','2','3'):
        for r in gr[k]['reviews']:
            yield 'GR'+k,clean(r['text']),r
    for r in sc['reviews']:
        yield 'SC',clean((r.get('title') or '')+' . '+(r.get('body') or '')),r
if __name__=='__main__':
    data=list(rows())
    grp=Counter(g for g,_,_ in data); print('effectifs',dict(grp))
    for g in ('GR1','GR2','GR3','SC'):
        sub=[(t,r) for gg,t,r in data if gg==g]
        n=len(sub); empty=sum(1 for t,_ in sub if len(t)<20)
        sp=sum(1 for t,_ in sub if SPOIL.search(t))
        print(f'\n== {g}: {n} avis (texte < 20 car. : {empty}; signalés spoiler/au-delà de la limite : {sp}) ==')
        for th,pat in THEMES.items():
            c=sum(1 for t,_ in sub if re.search(pat,t,re.I))
            print(f'  {th:55s} {c:4d} ({100*c/max(n,1):.0f} %)')
