import json,re,statistics,collections
d=json.load(open('/home/user/radiant_anime_mal_saisons_1_2.json'))
HDR=re.compile(r'^\s*\[?(story|characters?|sounds?|art|art, animation|animation( and fights)?|enjoyment|overall|direction|plot|screenplay|music)\]?\s*(\(\s*\d+(\.\d+)?\s*/\s*10\s*\)|-?\s*\d+(\.\d+)?\s*/\s*10|\s*-|\s*:|\s*\d+)*\s*[-:]?\s*',re.I)
def clean(t):
    t=t.split('---------\nEspañol')[0]            # doublon espagnol (S1-15)
    out=[]
    for l in t.split('\n'):
        l=HDR.sub('',l,count=1) if re.match(r'^\s*\[?(story|characters?|sounds?|art|art, animation|animation( and fights)?|enjoyment|overall|direction|plot|screenplay|music)\]?\s*(\(|-|:|\d|\[|$)',l,re.I) else l
        if re.fullmatch(r'\s*(spoilers?|this review may contain some spoilers\.?|season [12] review\.?|\(spoiler free\)|tl;dr)\s*',l,re.I): continue
        out.append(l)
    return '\n'.join(out).strip()
LEX={
'D1':r"\bstor(y|ies|ytelling)\b|\bplots?\b|\bwrit(ing|ten)\b|screenplay|twists?|narrative|premise|script|dialogues?|foreshadow|mysteries|mystery",
'D2':r"\bpac(e|ing|ed)\b|\bslow\w*|sluggish|\bdrag(s|ging|ged)?\b|\barcs?\b|exposition|\bexplain\w*|first (half|\d+|few|ten) ?(ep|episodes)?|\beps? ?\d+|stretch|rushed|runtime|slow burner|beginning|\bintros?\b|introduction",
'D3':r"stakes|consequences?|tragic|tragedy|\bdark\b|serious\w*|emotion\w*|\btone\b|mature|maturity|\bdeaths?\b|betray\w*|intens\w*|angst|drama\w*|heart-?felt|moving|\bdepth\b|sense of (risk|urgency)|\bgrim\b",
'D4':r"climax|\bending\b|finale|conclusion|resolution|cliff ?hanger|payoff|epilogue|final (arc|episode|battle)|last (episode|ep|arc|2 eps)|end of the (season|series)|escalation|de-?escalation",
'C':r"\bcharacters?\b|protagonist|\bmc\b|villains?|antagonists?|\bseth\b|\bm[eé]lie\b|\bdoc\b|\bgrimm?\b|\balma\b|dragunov|konrad|\bcast\b|\bhero\b|sidekicks?|companions?|supporting|\bbrat\b|personalit\w+",
'B1':r"discriminat\w*|racis\w*|xenophob\w*|bigot\w*|persecut\w*|outcasts?|oppress\w*|minority|prejudice|stigma\w*|infected|moral\w*|\bgr[ae]y\b|ostraci\w*|equality|acceptance|social commentary|political|injustice|immigrant\w*|\bhated\b|hate speech\w*|humans? vs",
'B2':r"\bworld\b|world-?building|worldbuild\w*|magic system|power system|\bsetting\b|\blore\b|inquisition|inquisitors?|hierarchy|universe|mechanics|\bspells?\b|\bcurses?\b|\bnemesis\b.*\bmystery|\bfaction",
'A1':r"\bart\b|artwork|art style|animation|animated|visuals?|colou?rs?\b|palette|lerche|\bcgi\b|\bdrawn\b|drawing|colou?ring|backgrounds?|\bframes\b",
'A2':r"spell effects?|sparkles?|particles?|\baura|\bgore\b|creature design|monster design|spells? look|green or blue|blobs? of colou?r|magic effects?|lightsabers?",
'A3':r"character designs?|\bdesigns?\b|silhouette|costumes?|outfits?|clothes|fashion|\bhair\w*|appearance|\bhorns?\b|\bhaired",
'E1':r"\bfights?\b|fighting|\bbattles?\b|combat|\baction\b|choreograph\w*|\bpunch\w*|\bwar\b|clash",
'E2':r"tactic\w*|strateg\w*|bluff|outsmart\w*|clever\w*|creative\w*|inventive|ingenious",
}
EXTRA={'SON':r"\bsound\b|\bmusic\b|\bost\b|\bosts\b|opening|\bop\b|\bed\b|\bending song|\bbgm\b|voice|seiyuu|\bva\b|soundtrack|jazz",
       'HUM':r"humou?r|comed\w+|\bjokes?\b|funny|gags?|punchlines?|slapstick"}
def pole_union(codes,sub): return any(c in codes for c in sub)
reviews=[]
for si,s in enumerate(d['saisons']):
    for i,r in enumerate(s['critiques']):
        txt=clean(r['texte_filtre'])
        codes=set()
        for k,p in {**LEX,**EXTRA}.items():
            if re.search(p,txt,re.I): codes.add(k)
        reviews.append(dict(id=f"S{si+1}-{i}",saison=si+1,auteur=r['auteur'],date=r['date'],annee=int(re.search(r'(\d{4})',r['date']).group(1)),
            note=r['note'],tag=r['recommandation'],react=r['votes_utiles'] or 0,mots=len(re.findall(r"\w+",txt)),codes=codes,txt=txt))
