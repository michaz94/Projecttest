import sys,re,json
sys.path.insert(0,'/home/user/radiant_manga_analyse')
import sel2
from sel2 import COMB,POW,hits,sents,prep
D={r['id']:r for r in prep.R}
TR={'GR3-mSIVBw':"Malgré le même décor qu'au tome précédent, la grande bataille de Rumble Town montre des scènes inédites de la ville ; l'apparence des personnages en plein combat et les moments émotionnels les rapprochent encore du héros.",
'GR1-a4z6HA':"La magie et son système m'intriguent pas mal jusqu'ici.",
'GR2-0zKVSg':"Ainsi nous connaissons un peu plus à fond le système de magie appelé Fantasía.",
'GR3-LkpRTA':"Spectaculaires scènes de batailles qui inondent la rétine, puissants power-ups dignes de Goku, forte composante politico-sociale et une touche d'humour peu conventionnelle pour atténuer la violence.",
'GR1-4G_KGg':"J'aime beaucoup le système de magie, j'adore les personnages variés, je trouve le manga très bien dessiné et j'apprécie l'humour.",
'GR2-vdqJhA':"Au tome 2, des personnages assez intéressants s'ajoutent, surtout leur pouvoir magique."}
# (id, tag, [clés]) ; clés = sous-chaînes (insensibles à la casse) des phrases à citer
C=[('AS009','Mixte',['combat']),('AS010','Mixte',["l'action se fait attendre","vrai baston","scène d'action"]),('AS013','Éloge',['bastons sont','bataille/baston']),
('AS015','Réserve',['combats qui']),('AS016','Éloge',['combats épiques']),('AS021','Éloge',["scènes d'action"]),('AS022','Éloge',["action très nerveuse"]),
('AS029','Éloge',["de l'action"]),('AS041','Éloge',["de l'action"]),('AS042','Éloge',["action en permanence"]),('AS053','Éloge',["scènes d'actions"]),
('GR1-su2_RQ','Réserve',['fights were hard']),('GR1-4uyxZA','Réserve',['fight scenes']),('GR1-3091906853','Réserve',['fighting a demon']),
('GR1-2700378034','Réserve',['obnoxious young fighter']),('GR1-2545279294','Réserve',['fight scenes']),
('GR2-ddccda','Éloge',["scènes d’action sont","plus d’action"]),('GR2-Fg7aUg','Éloge',["l'action était"]),
('GR3-mSIVBw','Éloge',['масштабний бій']),('GR3-LkpRTA','Éloge',['escenas de batallas']),
('GR3-7GYKbA','Mixte',["beaucoup beaucoup d'action","lisibilité des scènes"]),('GR3-dc3a9e','Éloge',['gère à merveille']),
('GR3-KC86Zg','Réserve',['fight between Seth','fight felt really']),('MN3-04','Éloge',["beaucoup d'action"]),
('BB1-1729510','Éloge',["Il y a de l'action"]),('BB1-2309307','Éloge',['humour, combats']),('BB1-4901889','Réserve',['baston à tout-va']),
('BB1-471130','Éloge',["humour et d'action"]),('BB1-3124346','Éloge',["De l'action"]),('BB1-1274023','Réserve',["pas assez d'action"]),
('BB1-2204790','Éloge',['scènes de combats']),('BB2-1601574','Éloge',['combats hyper']),('BB2-3173176','Éloge',['combats très clairs']),
('BB2-3849592','Éloge',['gros combats']),('BB2-4023225','Éloge',["plus d'action"]),('BB2-4225150','Réserve',['en combat']),
('BB3-1204223','Éloge',['plus de combats']),('BB3-1214020','Réserve',['batailles et de destructions']),('BB3-1601576','Réserve',['Pas mal de combats']),
('BB3-3714444','Éloge',['gros combats']),('BB3-4969284','Éloge',['combats épiques','Combats, stratégie'])]
P=[('AS012','Neutre',["connaitre l'infection"]),('AS015','Réserve',['Aucun approfondissement','rapport à la magie']),
('AS021','Éloge',['pouvoirs genre le feu','contrôle ses sorts']),('AS022','Éloge',['capacité d'+"'"+'émettre du fantasia']),('AS029','Éloge',['pouvoirs intéressants']),
('AS040','Neutre',['énergie magique']),('AS051','Réserve',['uber-special powers']),('GR1-HlqQvA','Éloge',['magic system','fascinating magic']),
('GR1-4G_KGg','Éloge',['Magiesystem']),('GR1-a4z6HA','Éloge',['magia y su sistema']),('GR1-HYGgQA','Éloge',['Fantasia']),
('GR1-2364222311','Mixte',['bipolarité magique','sorciers, de la magie']),('GR1-6015687397','Neutre',['La magie dans cet univers']),
('GR1-4564513442','Réserve',['cast spells']),('GR1-8548861860','Éloge',['magic world']),('GR1-2545279294','Réserve',['USE MAGIC']),
('GR1-3261149369','Éloge',['interesting take on Wizards']),('GR2-0zKVSg','Éloge',['sistema de magia']),('GR2-ddccda','Mixte',['explosions de pouvoirs']),
('GR2-TxJkHQ','Éloge',['magic system']),('GR2-vdqJhA','Éloge',['kekuatan sihir']),('GR3-LkpRTA','Éloge',['power-ups']),
('BB1-892721','Mixte',['pouvoirs à la Naruto','tout sauf doué']),('BB1-2304803','Éloge',['héroïc-fantasy qui m']),('BB1-2204790','Éloge',['balance des pouvoirs','approche de la magie']),
('BB1-4109322','Réserve',['pas encore très bien']),('BB2-1601574','Éloge',['Fantasia comme incarnation'])]
NOTES_C={'AS002':"parle de la « baston » du shōnen en général",'GR1-5441728159':"« spækket med kamp » (danois : « truffé de combats ») — description"}
NOTES_P={}
EXCL_P={'AS050','GR2-r3iIaQ','GR3-P0SuYA','GR1-3945109126','BB3-1214020'}  # faux positifs : « infectious », « in power », Naruto, etc.
EXCL_C={'GR3-P0SuYA'}
def pick(r,keys,rx):
    ss=sents(r['txt']); out=[]
    for s in ss:
        if any(k.lower() in s.lower() for k in keys) and s not in out: out.append(s)
    assert out,(r['id'],keys)
    return out
def fmt(r):
    n=f"{r['note']}/{'5' if r['echelle']==5 else r['echelle']}" if r.get('note') is not None else 'sans note'
    return f"{r['author'] or 'anonyme'} · {r['source']} T{r['tome']}" if r['tome'] else f"{r['author']} · {r['source']} série"
def row(r,tag,keys,rx,i):
    ex=' […] '.join(x if len(x)<=330 else x[:327]+'…' for x in pick(r,keys,rx)[:3]).replace('|','/')
    if r['id'] in TR: ex+=f" — *trad. : « {TR[r['id']]} »*"
    note=r.get('note'); ech=r.get('echelle')
    ns=(str(note).replace('.0','').replace('.',',')+(ech if str(ech).startswith('/') else '/'+str(ech))) if note is not None and ech else 'sans note'
    if r['source']=='TheOASG': ns='note 2, échelle non précisée'
    src=f"{r['source']} T{r['tome']}" if r['tome'] else f"{r['source']} (série)"
    return f"| {i} | `{r['author'] or 'anonyme'}` | {src} | {r['verdict']} ({ns}) | **{tag}** | {ex} | `{r['id']}` |"
def table(L,rx):
    rows=["| # | Auteur | Source | Verdict dérivé (note) | Sens | Extrait | id |","| :-: | :--- | :--- | :--- | :--- | :--- | :--- |"]
    for i,(id_,tag,keys) in enumerate(L,1): rows.append(row(D[id_],tag,keys,rx,i))
    return '\n'.join(rows)
from collections import Counter
cA={i for i,_,_ in C}; pA={i for i,_,_ in P}
candC=[r for r in prep.R if hits(r['txt'],sel2.COMB) and r['id'] not in cA|EXCL_C]
candP=[r for r in prep.R if hits(r['txt'],sel2.POW) and r['id'] not in pA|EXCL_P]
def listB(cands,rx,NOTES):
    out=[]
    for r in cands:
        h=hits(r['txt'],rx)[0]; h=h if len(h)<=200 else h[:197]+'…'
        out.append(f"- `{r['author'] or 'anonyme'}` ({r['source']} T{r['tome']}, {r['verdict']}, {r['lang2']}, `{r['id']}`){' — '+NOTES[r['id']] if r['id'] in NOTES else ''} : « {h} »")
    return '\n'.join(out)
def tags(L): c=Counter(t for _,t,_ in L); return ', '.join(f"{k} {v}" for k,v in c.most_common())
def bytome(L): c=Counter(D[i]['tome'] for i,_,_ in L); return ', '.join(f"T{k} : {c[k]}" for k in (1,2,3) if c[k])
M=f"""# *Radiant* (manga) — avis qui parlent des combats et du système de pouvoir

**Source** : le corpus de {len(prep.R)} avis de `Analyse_critiques_recurrentes_Radiant_manga_Goodreads_et_autres_sites.md` (Goodreads, Babelio, Manga-News, SensCritique, presse). Extraits exacts, vérifiés par script ; seules les traductions (marquées *trad.*) sont de moi.

## Comment lire cette liste
- **Repérage par mots-clés** (combat, fight, baston, action, bataille, affronter… ; magie, fantasia, pouvoirs, sorts, magic system, infection…), anglais et français, plus quelques termes espagnols, ukrainiens, allemands, danois, indonésiens, bulgares et croates. **Un avis qui parle de ces sujets sans ces mots a pu m'échapper**, surtout dans les autres langues.
- **Deux niveaux** pour chaque sujet : **A** = l'avis *juge ou commente* (éloge, réserve, constat) ; **B** = l'avis *mentionne seulement* (résumé de l'intrigue, simple énumération). Ce classement A/B et la colonne « Sens » sont **ma lecture**, pas un codage mesuré ; les avis les plus brefs (« de l'action, de l'humour ») sont classés « Éloge » par défaut.
- « Verdict dérivé » = verdict calculé à partir de la note (≥ 75 % de l'échelle = Positif), pas une étiquette du site. Les sites donnent peu de détail sur le **système de pouvoir** : c'est un sujet nettement moins commenté que les combats.

## 1. Les combats

**{len(C)} avis jugent ou commentent les combats / l'action** ({tags(C)} ; {bytome(C)}) et {len(candC)} les mentionnent seulement.

### 1.A. Avis qui jugent ou commentent les combats

{table(C,COMB)}

### 1.B. Avis qui mentionnent les combats sans les juger ({len(candC)})

{listB(candC,COMB,NOTES_C)}

## 2. Le système de pouvoir (magie, Fantasia, infection)

**{len(P)} avis jugent ou commentent la magie / le système de pouvoir** ({tags(P)} ; {bytome(P)}) et {len(candP)} la mentionnent seulement (le plus souvent pour résumer le pitch : les infectés manient le « fantasia »).

### 2.A. Avis qui jugent ou commentent le système de pouvoir

{table(P,POW)}

### 2.B. Avis qui mentionnent la magie sans la juger ({len(candP)})

{listB(candP,POW,NOTES_P)}

## 3. Lecture rapide (observations, à ne pas prendre pour des mesures)

- **Combats** : surtout loués (lisibilité, dynamisme, intensité au tome 3). Les réserves portent sur trois choses distinctes : l'action qui se fait attendre (T2), la **lisibilité de certaines cases** de combat, et la longueur ou la place des combats au tome 3.
- **Système de pouvoir** : les éloges concernent l'originalité de l'infection / du Fantasia et la variété des pouvoirs. Les réserves visent surtout le **manque d'explications** ou d'approfondissement (« pas encore très bien détaillé », « aucun approfondissement de la magie »), ou un héros qui utilise la magie sans objet comme un « trope ». 
- **Tactique** : presque personne ne parle de stratégie de combat (cf. `E2` = 2,3 % dans l'analyse), contrairement à ce qu'on trouverait dans un corpus HxH.
"""
open('/home/user/Radiant_manga_avis_combats_et_systeme_de_pouvoir.md','w',encoding='utf8').write(M)
print(len(C),len(candC),len(P),len(candP),tags(C),tags(P))
