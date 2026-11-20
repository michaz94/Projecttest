import sys,re
sys.path.insert(0,'/home/user/radiant_manga_analyse')
from sel2 import prep,sents
D={r['id']:r for r in prep.R}
TR={'BB3-4969284':None,
'GR3-mSIVBw':"Mais comme il doit jongler entre le combat contre le méchant, qui emploie une tactique odieuse, le sauvetage de ses amis et des habitants de cette ville volante, il devient évident que sauver Rumble Town ne sera pas une tâche facile.",
'GR1-4BOmcQ':"Seth est impulsif, ce qui n'est pas toujours une bonne qualité au combat."}
T1=[('BB3-4969284','Éloge (bref)',['stratégie']),('GR3-mSIVBw','Neutre (tactique du méchant, dans un résumé)',['тактику']),('GR1-4BOmcQ','Réserve légère',['impulsiv'])]
T2=[('AS004','Neutre/réserve',['gros bourrin']),('AS021','Neutre',['caractère bourrin']),('AS051','Réserve',['very good at doing anything']),
('AS052','Neutre',['brute strength']),('GR1-HlqQvA','Neutre',['not too bright']),('GR1-rwG-nA','Réserve',['powerful but incompetent']),
('GR1-4uyxZA','Réserve',['overconfident']),('GR1-4564513442','Réserve',['cannot differentiate','recklessness']),
('GR1-6015687397','Neutre (humour)',['maladroit et bourrin']),('GR2-jxS83w','Neutre (humour)',['bourrins']),
('BB1-905930','Neutre (humour)',['confond de paisibles','impulsivité']),('BB1-1729510','Mixte',['fonce souvent','un tour dans son sac']),
('BB1-2309307','Neutre',['fonce tête baissée']),('BB1-2417233','Neutre (humour)',['tape sur tout'])]
T3=[('AS009','Mixte',['combat']),('GR2-ddccda','Mixte',['explosions de pouvoirs'])]
def pick(r,keys):
    out=[s for s in sents(r['txt']) if any(k.lower() in s.lower() for k in keys)]
    assert out,(r['id'],keys); return out
def row(r,tag,keys,i):
    ex=' […] '.join(x if len(x)<=330 else x[:327]+'…' for x in pick(r,keys)[:2]).replace('|','/')
    if TR.get(r['id']): ex+=f" — *trad. : « {TR[r['id']]} »*"
    note,ech=r.get('note'),r.get('echelle')
    ns=(str(note).replace('.0','').replace('.',',')+(ech if str(ech).startswith('/') else '/'+str(ech))) if note is not None and ech else 'sans note'
    if r['source']=='TheOASG': ns='note 2, échelle non précisée'
    src=f"{r['source']} T{r['tome']}" if r['tome'] else f"{r['source']} (série)"
    return f"| {i} | `{r['author'] or 'anonyme'}` | {src} | {r['verdict']} ({ns}) | **{tag}** | {ex} | `{r['id']}` |"
def table(L):
    rows=["| # | Auteur | Source | Verdict dérivé (note) | Sens | Extrait | id |","| :-: | :--- | :--- | :--- | :--- | :--- | :--- |"]
    rows+= [row(D[a],t,k,i) for i,(a,t,k) in enumerate(L,1)]
    return '\n'.join(rows)
M=f"""# *Radiant* (manga) — avis qui parlent des tactiques de combat

**Source** : le corpus de {len(prep.R)} avis de l'analyse manga (Goodreads, Babelio, Manga-News, SensCritique, presse). Extraits exacts ; les traductions sont de moi (*trad.*).

## Réponse courte
**Presque aucun avis ne parle de tactique de combat.** Un seul avis évoque explicitement la **stratégie** dans les combats (`Tmor`, Babelio T3 : une phrase de huit mots). Un avis ukrainien parle de la **tactique du méchant** dans un résumé, et un avis suédois dit que l'impulsivité de Seth n'est pas une qualité au combat. Les autres avis ci-dessous touchent le sujet **de biais** : ils décrivent un héros qui fonce sans réfléchir, ou jugent les combats « pas innovants ».

**Précision sur mon analyse précédente** : dans le MD d'analyse, le sous-pôle `E2` (tactique, stratégie, créativité) sort à 2,3 % (5 avis). C'est **un repérage par mots-clés qui contient 4 faux positifs** (« bluffé » ×2, « cleverly » à propos d'un titre de chapitre, « pas très intelligent » à propos du héros). Au sens strict, **un seul avis** parle de stratégie de combat : le MD corrigé en tient compte.

**Méthode et limites** : repérage par mots-clés (tactique, stratégie, ruse, astucieux, intelligent, réfléchir, plan, bourrin, impulsif, sans réfléchir…) en anglais, français et quelques autres langues, puis lecture de chaque résultat. Un avis qui évoque la tactique avec d'autres mots, ou dans une langue non couverte, a pu m'échapper. Le classement en trois niveaux et la colonne « Sens » sont ma lecture.

## 1. Avis qui parlent de stratégie ou de tactique en combat ({len(T1)})
{table(T1)}

## 2. Avis sur la façon dont Seth se bat : foncer sans réfléchir ({len(T2)})
*Ce n'est pas de la tactique au sens strict : ces avis décrivent un héros puissant mais impulsif, ce qui indique indirectement l'absence d'approche réfléchie du combat dans les premiers chapitres. Le plus souvent, c'est un trait de personnalité ou une source d'humour, pas un jugement sur les combats.*

{table(T2)}

## 3. Avis qui jugent l'originalité ou la créativité des combats ({len(T3)})
{table(T3)}

## 4. Lecture rapide (observations)
- **Les combats sont jugés surtout sur le rythme, la lisibilité et l'intensité** (voir `Radiant_manga_avis_combats_et_systeme_de_pouvoir.md`), pas sur leur logique ni sur l'intelligence des affrontements.
- **Les avis du niveau 2 viennent presque tous du tome 1** : le héros y est décrit comme « bourrin », « impulsif » ou « puissant mais incompétent ». Un seul avis du tome 2 (`Sunread26`, « bourrins ») et aucun du tome 3 en parlent. Aucun avis ne dit que les combats deviennent plus tactiques, ni le contraire : c'est une absence de commentaire, pas une preuve.
- **Comparaison** : dans le corpus HxH analysé précédemment, la tactique/stratégie (`E2`) ressortait à 17,2 % (repérage par mots-clés). Ici, ce sujet n'existe pour ainsi dire pas dans la réception de *Radiant*.
"""
open('/home/user/Radiant_manga_avis_tactique_de_combat.md','w',encoding='utf8').write(M)
print(len(T1),len(T2),len(T3))
