import re,json
class prep: R=json.load(open("/home/user/radiant_manga_analyse/codage_critiques_radiant_manga.json"))
from collections import Counter
COMB=re.compile(r"\b(fights?|fighting|fighters?|battles?|battling|combats?|combat\w*|duels?|action[- ]packed|action scenes?|fight scenes?|battle scenes?|brawl\w*)\b|scènes? d['’]action|l['’]action|de l['’]action|d['’]action|bataille|bagarre|affrontements?|baston|castagne|combattre|combattent|se battre|\bcombates?\b|\bpelea\w*|\blucha\w*|\bbatalla\w*|\bдуел\w*|\bбитв\w*|\bбій\w*|\bбої\b|\bбою\b|\bбо[їй]\w*|\bбитк\w*|\bсхватк\w*|\bбой\b|\bpertarung\w*|\bbertarung\w*|\bpertempur\w*|\bkampf\w*|\bkämpf\w*|\bkamp\b|\bkæmp\w*|\bborb\w*|\bboj\w*|\bbitk\w*|affront\w+|\btacti\w+|\bstratég\w+|\bstrateg\w+|\bтактик\w*|\bстратег\w*|\bcombati\w*|\bpelear\w*|\bsc[eè]ne[s]? de coups",re.I)
POW=re.compile(r"\b(magic\w*|spells?|spellcast\w*|fantasia|power system|magic system|powers?|abilities|ability|techniques?|jutsu|wizardry|sorcery|casting)\b|\bmagie\b|\bmagiques?\b|\bpouvoirs\b|système (de|des|d['’])\s*(magie|pouvoirs?)|\bsorts\b|\bsortilèges?\b|\bfantasia\b|\bmagia\b|\bhechizos?\b|\bpoderes\b|\bmagi\w*|\bмагі\w*|\bзакляття\w*|\bчаклу\w*|\bмагия\w*|\bмагическ\w*|\bспособност\w*|\bsihir\w*|\bkekuatan\w*|\bkräfte\b|\bzauber\w*|\bmagisk\w*|\bkræfter\b|\bčaro\w*|\bsnag\w*|\binfect\w*|\binfection\w*|\bsystème\b|\bsystem\b|\bsistema\w*|\bсистем\w*|\bсила\w*|\bсили\b|\bенерг\w*|\bподібн\w*|\bpower[- ]?ups?",re.I)
def sents(t):
    t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[.!?…])\s+(?=[A-ZÀ-ÖØ-ÝА-ЯІЇЄҐ¿¡«"“(\[*])',t)
def hits(t,rx):
    return [s for s in sents(t) if rx.search(s)]
if __name__=='__main__':
    c=[r for r in prep.R if hits(r['txt'],COMB)]
    p=[r for r in prep.R if hits(r['txt'],POW)]
    print(len(c),len(p),len({r['id'] for r in c}&{r['id'] for r in p}))
    print(Counter(r['lang2'] for r in c)); print(Counter(r['lang2'] for r in p))
    # keyword frequency for power
    kw=Counter(m.group(0).lower() for r in p for s in hits(r['txt'],POW) for m in POW.finditer(s)); print(kw.most_common(40))
    kc=Counter(m.group(0).lower() for r in c for s in hits(r['txt'],COMB) for m in COMB.finditer(s)); print(kc.most_common(40))
