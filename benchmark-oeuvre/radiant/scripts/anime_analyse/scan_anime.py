import json,re
d=json.load(open('/home/user/radiant_anime_mal_saisons_1_2.json'))
R=[]
for s in d['saisons']:
    for i,c in enumerate(s['critiques']):
        R.append(dict(id=f"S{s['saison']}-{i}",saison=s['saison'],auteur=c['auteur'],date=c['date'],note=c['note'],reco=c['recommandation'],txt=c['texte_filtre']))
def sents(t):
    t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[.!?…])\s+(?=[A-Z0-9"“(\[*])',t)
TAC=re.compile(r"\b(tactic\w*|strateg\w*|outsmart\w*|outwit\w*|cunning|clever\w*|ruses?|chess|mind[- ]?games?|brains?|intelligen\w*|smart\w*|plan(s|ning|ned)?|calculat\w*|creativ\w*|inventive|ingenious|improvis\w*|think(s|ing)? (it )?through|without thinking|reckless\w*|brute|bluff\w*|puzzle|lazy fight|predictab\w*|choreograph\w*|power[- ]?scal\w*|stakes|tension)\b",re.I)
COMB=re.compile(r"\b(fights?|fighting|fighters?|battles?|combat\w*|duels?|action|fight scenes?|choreograph\w*|brawl\w*|clash\w*|tournament|beat\w* up|punch\w*|kicks?)\b",re.I)
POW=re.compile(r"\b(magic\w*|spells?|fantasia|power system|magic system|powers?|abilit\w+|techniques?|wizards?|sorcer\w*|witch\w*|infect\w*|nemes\w+)\b",re.I)
if __name__=='__main__':
    import sys
    rx={'t':TAC,'c':COMB,'p':POW}[sys.argv[1]]
    for r in R:
        h=[s for s in sents(r['txt']) if rx.search(s)]
        if h: print(f"## {r['id']}|{r['auteur']}|{r['reco']}|{r['note']}\n"+'\n'.join('  - '+x[:300] for x in h[:6]))
