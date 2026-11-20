import json,re,sys
from collections import Counter,defaultdict
from langdetect import detect, DetectorFactory
DetectorFactory.seed=0
B='/home/user/Others/workspace_1_benchmark_battle_shonen_et_corpus/benchmark_4_piliers/'
def isen(t):
    try: return detect(t)=='en' if len(t)>40 else bool(re.search(r"\b(the|and|is|this|it|but)\b",t,re.I))
    except: return False
C=defaultdict(list)
for b in json.load(open(B+'goodreads_tomes_1_2_5_series.json')):
    for r in b['reviews']:
        if r.get('rating') and isen(r['text']):
            C[b['serie']].append(dict(id=r['review_id'],t=b['tome'],n=r['rating'],txt=r['text']))
R=json.load(open('/home/user/radiant_manga_analyse/codage_critiques_radiant_manga.json'))
for r in R:
    if r['source']=='Goodreads' and r['lang2']=='en' and r['tome'] in(1,2) and r['note'] and r['echelle']=='2 /5'[:0] or False: pass
for r in R:
    if r['source']=='Goodreads' and r['lang2']=='en' and r['tome'] in(1,2) and isinstance(r['note'],(int,float)):
        C['Radiant'].append(dict(id=r['id'],t=r['tome'],n=r['note'],txt=r['txt']))
LEX={
'derive':r"\b(generic|derivative|clich\w+|unoriginal|formulaic|predictab\w+|nothing new|seen (it|this) (all )?before|same old|typical shonen|standard shonen|rip[- ]?off|knock[- ]?off|poor man|trope\w*|stereotyp\w+|run[- ]of[- ]the[- ]mill|cookie[- ]cutter|boilerplate)\b",
'lent':r"\b(slow|slowly|boring|bored|dull|drag\w*|tedious|pacing|paced|dry|meandering|uneventful)\b",
'bavard':r"\b(exposition|info[- ]?dump\w*|too (much|many) (talk\w*|dialogue|text|word\w*|explain\w*|exposition)|talk(s|ing)? (too much|a lot)|wordy|text[- ]heavy|dialogue[- ]heavy|explain\w* everything|walls? of text|dialogues?)\b",
'tension':r"\b(tension|stakes|suspense|no (danger|threat|risk)|lack of (danger|threat|risk)|toothless|harmless|low[- ]stakes)\b",
'combat':r"\b((fights?|battles?|action|combat)( scenes?)? (is|are|was|were|felt|feels|seems?|seemed) (\w+ ){0,2}(boring|simple|simplistic|basic|repetitive|lackluster|underwhelming|dull|meh|confusing|messy|weak|short|easy|bland)|(boring|simple|simplistic|repetitive|lackluster|underwhelming|dull|weak|bland|messy|confusing) (fights?|battles?|action|combat)|lack of action|not enough action|little action)\b",
'heros':r"\b(annoying|obnoxious|idiot\w*|stupid|dumb|irritating|insufferable|unlikeable|unlikable|cringe\w*)\b",
}
def stats(S,label):
    n=len(S); low=[r for r in S if r['n']<=3]
    print(f"\n{label}: N={n}, ≤3★={len(low)} ({100*len(low)/n:.0f}%), moy={sum(r['n'] for r in S)/n:.2f}")
    return low
if __name__=='__main__':
    for s in ['Radiant','Naruto','One Piece','Fullmetal Alchemist','Hunter x Hunter','Jujutsu Kaisen','Red Hood']:
        S=C[s]; low=stats(S,s)
        out=[]
        for k,rx in LEX.items():
            a=sum(bool(re.search(rx,r['txt'],re.I)) for r in S)
            b=sum(bool(re.search(rx,r['txt'],re.I)) for r in low)
            out.append(f"{k}: tous {a}/{len(S)} | ≤3★ {b}/{len(low)}")
        print(' ; '.join(out))
