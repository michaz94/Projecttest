import re,json,statistics as st,csv
from collections import Counter,defaultdict
from prep import R
CODES={
'GR1-UP2RsQ':['C4','C8'],'GR1-HlqQvA':['C2','C6'],'GR1-Dck3Xw':['C1'],'GR1-7swWkg':['C2'],'GR1-4BOmcQ':['C3'],
'GR1-rGep_g':['C1','C3','C4'],'GR1-LgLErA':['C1','C3'],'GR1-BhObyw':['C5'],'GR1-su2_RQ':['C1','C2'],'GR1-IWnyyA':['C4','C8'],
'GR1-rwG-nA':['C1','C3','C6'],'GR1-4uyxZA':['C1','C3'],'GR1-niTJVA':['C2','C3','C4'],'GR1-HAYWYg':['C1','C4'],
'GR2-pNCs_w':['C2','C5'],'GR2-r3iIaQ':['C1','C3','C4','C5','C7'],'GR2-ddccda':['C2','C4'],'GR2-TN0RuQ':['C7'],
'GR2-X7PQZg':['C2','C8'],'GR2-Abb5lg':['C1','C4'],'GR2-a62a3e':['C2','C4'],'GR2-0zKVSg':['C2'],'GR2-gsZYnQ':['C4'],'GR2-2GWfeQ':['C2'],
'GR3-KC86Zg':['C5'],'GR3-P0SuYA':['C4'],'GR3-LkpRTA':['C5'],'GR3-VQPFug':['C5'],'GR3-mSIVBw':['C5'],'GR3-HvpRZw':['C6'],
'AS001':['C1'],'AS003':['C1'],'AS004':['C1'],'AS005':['C1'],'AS007':['C1'],'AS009':['C1','C3','C4'],'AS010':['C5'],'AS013':['C4'],
'AS015':['C1','C3','C6','C7','C8'],'AS016':['C1','C4','C6'],'AS017':['C1','C8'],'AS020':['C1'],'AS021':['C1','C8'],'AS022':['C1'],
'AS035':['C4'],'AS039':['C1'],'AS051':['C1','C3','C5','C6','C7'],'AS052':['C2','C5'],'AS053':['C2']}
CATS={'C1':'Dérivatif / déjà-vu (Fairy Tail, Naruto, One Piece…)','C2':'Surcharge de texte, exposition, planches denses ou illisibles',
'C3':'Seth et/ou casting jugés irritants ou archétypaux','C4':'Humour lourd, répétitif, mal dosé ; ton ou public jugé jeune',
'C5':'Rythme : démarrage lent, flashbacks ou combats étirés, action qui se fait attendre','C6':'Logique du monde, explications absentes ou confuses ; récit brouillon',
'C7':'Propos sur la discrimination jugé appuyé, maladroit ou problématique','C8':'Dessin jugé moyen, impersonnel ou trop jeune'}
MAP={'C4':'C2','C2':'C3','C3':'C4','C8':'C7','C7':'C8'}   # renumérotation par rang de fréquence
CATS={MAP.get(k,k):v for k,v in CATS.items()}
from codes_v2 import CODES2
FINAL={'C2':'C4','C4':'C2'}   # 2e renumérotation (corpus v2) : Seth/casting = C2, humour = C4
CATS={FINAL.get(k,k):v for k,v in CATS.items()}
for r in R: r['codes']=[FINAL.get(MAP.get(c,c),MAP.get(c,c)) for c in CODES.get(r['id'],[])]+CODES2.get(r['id'],[])
POLES={
'D1':r"\bstor(y|ies|ytelling)\b|\bplots?\b|\bwrit(ing|ten)\b|twists?|narrative|premise|dialogues?|mysteries|mystery|histoire|sc[ée]nario|intrigue|r[ée]cit|[ée]criture|narration|rebondissement|trame|suspense|cliffhangers?|mystère",
'D2':r"\bpac(e|ing|ed)\b|\bslow\w*|\bdrag\w*|\barcs?\b|exposition|explain\w*|info[- ]?dump|first (half|\d+|few|chapter|volume)|rushed|rythme|\blent\w*|longuet|tra[îi]ne|d[ée]marr\w+|explications?|flash-?backs?|flashbacks?|chapitres?|\bchapters?|50 premi[èe]res|trop de texte|\bdense",
'D3':r"stakes|consequences?|tragic|tragedy|\bdark\b|serious\w*|emotion\w*|\btone\b|mature|\bdeaths?\b|betray\w*|intens\w*|drama\w*|heart-?felt|moving|enjeux|tragique|drame|sombre|s[ée]rieux|[ée]motion\w*|\bmort\w*|trahi\w*|intense|grave|dur\b|profond\w*",
'D4':r"climax|\bending\b|finale?|conclusion|resolution|cliff ?hangers?|payoff|epilogue|last page|d[ée]nouement|r[ée]solution|[ée]pilogue|derni[èe]re page|\bfin\b|derni[èe]re? (chapitre|case)|twist de fin",
'C':r"\bcharacters?\b|protagonist|villains?|antagonists?|\bseth\b|\bm[eé]lie\b|\bmelie\b|\bdoc\b|\bgrimm?\b|\balma\b|dragunov|konrad|\bcast\b|\bhero\b|sidekicks?|personalit\w+|personnages?|h[ée]ros|protagoniste|m[ée]chants?|antagonistes?|casting|personnalit[ée]|attachants?|arch[ée]typ\w+|ma[iî]tre|\bhameline?\b|\byaga\b",
'B1':r"discriminat\w*|racis\w*|xenophob\w*|bigot\w*|persecut\w*|outcasts?|oppress\w*|minorit\w+|prejudice|infected|moral\w*|\bgr[ae]y\b|ostraci\w*|social|political|injustice|immigra\w*|islamophob\w*|racisme|discrimin\w+|x[ée]nophob\w*|persécut\w*|exclu\w*|minorit[ée]|pr[ée]jug[ée]s?|morale|engag[ée]\w*|politique|propos (politique|engag\w+|fort|social)|th[ée]matiques?|message|tol[ée]rance|bouc[- ]?[ée]missaire|infect[ée]s?|ethnique|ratonnade|ma[iî]tres? du",
'B2':r"\bworld\b|world-?building|worldbuild\w*|magic system|power system|\bsetting\b|\blore\b|inquisition|inquisitors?|hierarchy|universe|\bspells?\b|\bmagic\b|fantasia|univers|\bmonde\b|\bmagie\b|syst[èe]me|sorciers?|wizards?|h[ié]rarchie|n[ée]mesis|nemes[ie]s|background|mythologie|folklore|\bcontes?\b|hamelin",
'A1':r"\bart\b|artwork|art style|visuals?|colou?rs?\b|palette|\bdrawn\b|drawings?|backgrounds?|\bpanels?\b|layout|illustrations?|\bdessin\w*|graphi\w+|\btrait\b|planches?|d[ée]cors?|couleurs?|colorisation|visuel\w*|mise en page|d[ée]coupage|encrage|crayonn[ée]|illustrations?|illustrat\w+",
'A2':r"spell effects?|power-?ups?|explosions?|creature design|monster design|magic effects?|effets? (de|des) (magie|sorts|pouvoirs)|design des (sorts|cr[ée]atures|monstres)|attaques? explosives?|explosions? de pouvoirs",
'A3':r"character designs?|chara-?design|\bdesigns?\b|silhouette|costumes?|outfits?|\bhorns?\b|tenues?|apparence|\bcornes?\b|\blook\b|\bhaired|design des personnages|bonnes gueules",
'E1':r"\bfights?\b|fighting|\bbattles?\b|combat\w*|\baction\b|choreograph\w*|affrontements?|bastons?|bataille|sc[èe]nes? d'action|\bbaston",
'E2':r"tactic\w*|strateg\w*|bluff|outsmart\w*|clever\w*|inventive|ingenious|tactique|strat[ée]gi\w+|\bruse\b|astuce|intelligen\w+",
'HUM':r"humou?r|comed\w+|\bjokes?\b|funny|gags?|punchlines?|slapstick|drôle|\brire\b|\brires?\b|rigol\w+|blagues?|comique|\bmarr(ant|ée?|é)\w*|hilar\w+|d[ée]sternill\w+|gloussé|laugh\w*|humor|cómic|graciosos?",
}
SUB={'D':['D1','D2','D3','D4'],'B':['B1','B2'],'A':['A1','A2','A3'],'E':['E1','E2']}
for r in R:
    s=set()
    if r['couvert']:
        for k,p in POLES.items():
            if re.search(p,r['txt'],re.I): s.add(k)
        for P,subs in SUB.items():
            if any(x in s for x in subs): s.add(P)
        if 'C' in s: pass
    r['poles']=s
def sub(f): return [r for r in R if f(r)]
def pct(a,b): return f"{a} ({100*a/b:.1f} %)" if b else '—'
if __name__=='__main__':
    cov=sub(lambda r:r['couvert']); print('N total',len(R),'couvert',len(cov),'≥50 mots',len([r for r in cov if r['mots']>=50]))
    groups={'Goodreads':lambda r:r['groupe']=='Goodreads','Autres':lambda r:r['groupe']!='Goodreads','Total':lambda r:True}
    order=['D','D1','D2','D3','D4','C','B','B1','B2','A','A1','A2','A3','E','E1','E2','HUM']
    for nm,f in groups.items():
        cc=[r for r in cov if f(r)]; n=len(cc)
        print(nm,n,{k:round(100*sum(1 for r in cc if k in r['poles'])/n,1) for k in order})
        c5=[r for r in cc if r['mots']>=50]; n5=len(c5)
        print(nm,'>=50',n5,{k:round(100*sum(1 for r in c5 if k in r['poles'])/n5,1) for k in order})
