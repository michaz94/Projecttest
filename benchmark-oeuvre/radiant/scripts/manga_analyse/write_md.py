import re,json
src=open('build_md.py').read().split("tables=dict(")[0]
exec(src)
def pp(rs,k): return P(cnt(rs,k),len(rs))
def share(cat):
    n=catrow(cat)[0]; return f"{n} ({P(n,N)})"
def mm(cat):
    m=catrow(cat)[3]; return f"{m} / {NM} ({P(m,NM)})"
def langs(cat):
    c=Counter(r['lang2'] for r in R if cat in r['codes']); names={'en':'anglais','fr':'français','es':'espagnol','uk':'ukrainien','bg':'bulgare','id':'indonésien','hr':'croate','sv':'suédois','de':'allemand','da':'danois','cs':'tchèque','it':'italien','pt':'portugais','ca':'catalan'}
    return ', '.join(f"{names.get(k,k)} {v}" for k,v in c.most_common())
def tomes(cat):
    c=Counter(tome(r) for r in R if cat in r['codes']); return ', '.join(f"{k} : {c[k]}" for k in ['T1','T2','T3','série'] if c[k])
def nT(t): return len([r for r in R if r['tome']==t])
def cT(cat,t): return sum(1 for r in R if r['tome']==t and cat in r['codes'])
for i in ['GR2-gsZYnQ','GR3-VQPFug','GR3-adBWOw','GR2-qtz0lw','GR2-cyAB_A','GR2-ddccda','GR3-dc3a9e','AS010']: assert i in byid,i
mn13=[r for r in R if r['annee']==2013]; n13mn=sum(1 for r in mn13 if r['source']=='Manga-News')
half=6
d_a=ratio(cov,'D','A'); a_b=ratio(cov,'A','B')
T=json.load(open('/tmp/tables.json'))
nGR_dec=11
words=sum(r['mots'] for r in R)
words_s=f'{words:,}'.replace(',',' ')
anime_mentions=sum(1 for r in R if re.search(r'\banime\b',r['txt'],re.I))
fr_mentions=sum(1 for r in R if re.search(r'fran[cç]ais|french|france|manfra|franga|made in france|gaijin|euromanga',r['txt'],re.I))

from corpus2 import D as UD, FULL
import statistics as _st
gl=Counter(r['lang2'] for r in GR)
GL_MAIN=['en','fr','es','uk','id','de','bg']
n_other_gr=sum(v for k,v in gl.items() if k not in GL_MAIN and k!='short'); k_other_gr=len([k for k in gl if k not in GL_MAIN and k!='short'])
nonc_short=sum(1 for r in R if r['lang2']=='short'); nonc_oth=N-NC-nonc_short
n_trunc=sum(1 for t in '123' for a in UD['goodreads'][t]['avis'] if len(FULL[t][a['id']]['text'])>len(a['texte'])+30)
as_lang=Counter(r['lang2'] for r in AS)
_pat=re.compile(r"(?<![\d.,])([1-5])[.,](25|75|5|2)(?!\d)\s*(?:/\s*5|★|⭐|\*|stars?|étoiles?|estrellas?|🌟|\s*$)",re.I)
dec=[]
for r in GR:
    m=_pat.search(r['txt'][:120])
    if m and r['note']: dec.append((r['id'],float(m.group(1)+'.'+m.group(2)),r['note'],r['verdict']))
n_dec=len(dec); n_dec_down=sum(1 for d in dec if d[1]>d[2]); n_dec_down_mit=sum(1 for d in dec if d[1]>d[2] and d[3]=='Mitigé')
n_gr_mit=sum(1 for r in GR if r['verdict']=='Mitigé')
def gpos(f):
    g=[r for r in GR if r['annee'] and f(r['annee']) and r['verdict']!='Non noté']; p=sum(1 for r in g if r['verdict']=='Positif'); return p,len(g)
g1=gpos(lambda a:2018<=a<=2020); g2=gpos(lambda a:a>=2021); gold=gpos(lambda a:a<=2017)
def moe(n): return round(196*((0.25/n)**0.5)) if n else 0
first30=[a['etoiles'] for a in UD['goodreads']['1']['avis'] if a['etoiles']]
f30=f"{_st.mean(first30[:30]):.2f}".replace('.',','); fall=f"{_st.mean(first30):.2f}".replace('.',',')
def gtxt(t): g=UD['goodreads'][str(t)]; return (f"{g['moyenne_sous_corpus_texte']:.2f}".replace('.',','), g['n_notes_dans_avis_texte'], f"{g['moyenne_toutes_editions']:.2f}".replace('.',','), g['n_notes'])
UB=UD['babelio']
def wc(p): return sum(1 for r in R if re.search(p,r['txt'],re.I))
DISC_IDS=['GR2-ddccda','GR3-dc3a9e','AS010','GR2-cyAB_A','GR2-gsZYnQ','GR3-VQPFug','GR3-adBWOw','GR2-qtz0lw','GR1-ZGU3zg','BB2-1211463','BB2-1895675','BB2-4965238','BB2-4023225','BB2-4225150','BB2-3714301','BB1-2033061']
for i in DISC_IDS: assert i in byid,i
disc_auth={byid[i]['author'] for i in DISC_IDS}; c8_auth={r['author'] for r in R if 'C8' in r['codes']}
assert not (disc_auth&c8_auth),(disc_auth&c8_auth)
ac=Counter(r['author'] for r in R if r['author'] not in('(anonyme)','(pseudo non fourni)'))
rep3=[a for a,n in ac.most_common() if n>=3]; n_rep=sum(1 for a,n in ac.items() if n>=2)
for i in ('GR1-4256903234','GR1-8346979712'): assert not byid[i]['codes'],i
for i in ['GR2-gsZYnQ','GR1-5936052743','BB2-2164941','MN3-02']: assert 'C4' in byid[i]['codes'],i
nonfr_share={c:sum(1 for r in R if c in r['codes'] and r['lang2'] not in('en','fr'))/max(1,catrow(c)[0]) for c in CATS}
assert max(nonfr_share,key=nonfr_share.get)=='C3',nonfr_share
n_c3_nonfr=sum(1 for r in R if 'C3' in r['codes'] and r['lang2'] not in('en','fr'))
n_c7_pos=sum(1 for r in R if 'C7' in r['codes'] and r['verdict']=='Positif')
nd_ratio_sc=sum(1 for r in R if r['source']=='SensCritique' and 'C1' in r['codes']); n_sc=len(sc)
n_noterated=N-vc['Non noté']
mn_nonote=sum(1 for r in mn if r['note'] is None)
assert {r['id'] for r in cov if 'E2' in r['poles']}=={'AS018','AS036','GR1-HlqQvA','BB1-424069','BB3-4969284'}
noncodes=[r for r in MX if not r['codes']]
M=f"""# Analyse des critiques récurrentes et des 5 pôles — *Radiant* (manga, tomes 1 à 3 : Goodreads + autres sites)

**Date de l'étude** : 5 octobre 2026
**Méthode reprise de** : `Analyse_critiques_recurrentes_FMA_hors_2003.md` et `Analyse_critiques_recurrentes_HxH_hors_1999.md`, et de l'analyse de l'anime *Radiant* faite au tour précédent (même plan : périmètre → verdicts → 5 pôles → table des critiques récurrentes → détail avec citations datées et contre-voix → comparaison).
**Corpus** : **{N} avis du manga** (≈ {words_s} mots), après dédoublonnage (24 avis retirés sur 327 ; voir § 0).
- **Goodreads** : {len(GR)} avis (T1 : {len([r for r in GR if r['tome']==1])}, T2 : {len([r for r in GR if r['tome']==2])}, T3 : {len([r for r in GR if r['tome']==3])}) : **tous les avis avec texte** des trois pages du site (120 + 40 + 29 = 189 avant dédoublonnage). Source : ton fichier `Radiant_tomes_1_3_corpus_avis.json`, dont j'ai complété les textes (coupés à environ 500 caractères) et les pseudos.
- **Autres sites** : {len(AS)} avis (Babelio {len(bb)}, Manga-News {len(mn)}, SensCritique {len(sc)}, presse {len(presse)} : Otaku USA, TheOASG, Nerdbot, Askear).
**Exclusions et dédoublonnage** : voir § 0. Aucun filtre « filler » : il ne concernait que l'anime.

---

## 0. Ce qui est identique à FMA/HxH, ce qui est différent, et ce que je n'ai pas pu reproduire

**Identique** : les 5 pôles et leurs sous-pôles (D1–D4, C, B1–B2, A1–A3, E1–E2), la table des critiques récurrentes (total, part dans les avis mitigés/négatifs, note moyenne, réactions), les citations datées avec réactions, la contre-voix, le tableau comparatif final. Les citations de ce document ont été vérifiées par script contre les textes du corpus ({sum(len(v) for v in Q.values())}/{sum(len(v) for v in Q.values())}).

**Différent** :
- **Pas d'étiquette *Recommended / Mixed / Not Recommended*.** Goodreads et les autres sites donnent seulement une note, sur des échelles différentes (`/5`, `/10`, `/20`). J'ai donc **dérivé un verdict de la note** (annexe B) : *Positif* si la note vaut au moins 75 % de l'échelle, *Mitigé* entre 41 % et 74 %, *Négatif* à 40 % ou moins, *Non noté* sans note. **Ces seuils sont mon choix**, pas une donnée du site. Deux avis de presse sans note exploitable ont reçu un verdict lu à la main (`TheOASG` : négatif ; `Otaku USA` : positif), signalés « (lu) ».
- **Goodreads : tous les avis texte, pas un échantillon de 30.** FMA/HxH étaient plafonnés à 30 avis par tome ; ici le corpus est complet pour Goodreads (T1 120 avis, T2 40, T3 29 avant dédoublonnage). **Le fichier fourni coupait {n_trunc} avis à environ 500 caractères et n'avait pas de pseudos** : j'ai rechargé chaque avis (mêmes identifiants Goodreads, tous retrouvés) pour récupérer le texte complet et l'auteur.
- **Corpus multilingue.** Goodreads mélange les langues : anglais {gl['en']}, français {gl['fr']}, espagnol {gl['es']}, ukrainien {gl['uk']}, indonésien {gl['id']}, allemand {gl['de']}, bulgare {gl['bg']}, {n_other_gr} avis dans {k_other_gr} autres langues (croate, danois, suédois, grec, etc.), et {gl['short']} avis de moins de 4 mots (une note comme « 3.5 », un emoji, « Excellent tome »). Les autres sites sont en français, sauf trois avis de presse en anglais (Otaku USA, TheOASG, Nerdbot).
- **Pôles : seulement {NC} avis sur {N}.** Mes listes de mots-clés couvrent l'anglais et le français ; les {N-NC} autres avis ({nonc_oth} dans une autre langue, {nonc_short} de moins de 4 mots) sont **exclus des pourcentages de pôles** mais **inclus dans les verdicts et dans C1–C8**, que j'ai codés à la main après lecture (les avis de moins de 25 mots dans d'autres langues ont été lus en aperçu seulement).
- **Dédoublonnage (24 avis retirés sur 327)** : le même avis est souvent publié sur plusieurs sites ou plusieurs tomes ; je garde une seule copie (la plus longue). Retirés : 6 copies de `Sunread26` (extraits de blog repris sur SensCritique et Babelio ; la copie Goodreads est gardée), 3 copies Goodreads de `Drine Psylook` (copies Babelio, plus longues, gardées), 2 copies Babelio de `Tachan`, 1 de `Zutto`, 2 avis identiques de `Ivan Jovanovic` publiés sur les tomes 2 et 3 (gardé au T1), 2 doublons de `eques` sur Manga-News, **7 commentaires Manga-News d'annonce** (date de sortie, nombre de tomes) sans avis sur l'œuvre, et 1 avis SensCritique (`Shigeo`) qui parle de « cet anime ». Les pseudos identiques sur plusieurs sites peuvent être des homonymes ; je ne les ai pas fusionnés au-delà de ces copies exactes.
- **Anime mentionné** dans {anime_mentions} avis : conservés (ils parlent du manga).

**Je n'ai pas pu reproduire / pas pu collecter** :
- Les listes de mots-clés de FMA/HxH n'ont pas été retrouvées : mes listes sont à moi (annexe A). **Les pourcentages de pôles ne sont comparables à ceux de FMA/HxH qu'en ordre de grandeur.** FMA/HxH reposaient sur des critiques MAL longues ; ici beaucoup d'avis sont des phrases isolées (voir la colonne « avis de 50 mots ou plus »).
- **Babelio est incomplet** : 59 critiques collectées sur 81 annoncées (T1 30/47, pages 4 et 5 manquantes ; T2 19/19 ; T3 10/15, page 2 manquante). Les notes globales Babelio viennent de la page (T1 3,97 sur 41 notes ; T2 4,11 sur 18 ; T3 4,25 sur 14).
- **Manga-News** : avis lecteurs collectés pour les trois tomes ; **il n'existe pas de critique de la rédaction pour le tome 3** (la page répond sans bloc de critique).
- **SensCritique** : première page de chaque liste seulement.
- **Booknode** (écarté, sur ta demande) et **Reddit r/manga** (accès refusé) : non collectés.

---

## 1. Périmètre et répartition globale

### 1.1. Structure du corpus *Radiant* (manga, `N = {N}`)

| Sous-corpus | Avis (`N`) | Mots | *Positif* | *Mitigé* | *Négatif* | Non noté | Note moyenne (% de l'échelle) | Réactions cumulées | Réactions (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{T['T11'].replace('| **Goodreads (total)**','| **Goodreads (total)**')}

Notes agrégées affichées par les sites (relevé du 5 oct. 2026) : **Goodreads** T1 **3,80** (1 058 notes), T2 **4,00** (557), T3 **4,19** (434) ; **Babelio** T1 3,97 (41 notes), T2 4,11 (18), T3 4,25 (14) ; **SensCritique** T1 7,0 / T2 7,2 / T3 7,4 / série 7,0 (sur 10) ; **Manga-News** rédaction T1 15 / T2 16 (sur 20), lecteurs T1 19 / T2 19 / T3 17 ; **Askear** 3,8/5 ; **Nerdbot** 3,5/5 ; **TheOASG** « 2 » (échelle non précisée).

**Sur Goodreads, les lecteurs qui écrivent notent moins bien que l'ensemble des lecteurs** : T1 {gtxt(1)[0]} sur {gtxt(1)[1]} avis notés contre {gtxt(1)[2]} sur {str(gtxt(1)[3]).replace(',',' ')} notes ; T2 {gtxt(2)[0]} ({gtxt(2)[1]}) contre {gtxt(2)[2]} ({gtxt(2)[3]}) ; T3 {gtxt(3)[0]} ({gtxt(3)[1]}) contre {gtxt(3)[2]} ({gtxt(3)[3]}). L'écart est le plus grand au tome 1. Le corpus d'avis texte est donc un peu plus sévère que l'opinion globale (à lire avec le § 5).

Notes de méthode : (a) les « réactions » sont les *likes* Goodreads et SensCritique ; Manga-News, Babelio et la presse n'en ont pas dans mon relevé ; (b) dans Goodreads, **{n_dec} avis annoncent une note décimale** dans le texte (ex. « 3.5 ★ ») alors que le site n'accepte que des entiers : **{n_dec_down_mit} des {n_gr_mit} avis *Mitigé* de Goodreads** ({P(n_dec_down_mit,n_gr_mit)}) sont des « 3,5/5 » arrondis à 3. Le verdict ne change pas (3,5/5 = 70 % = *Mitigé* dans ma règle), mais la note Goodreads moyenne de ces avis est un peu sous-estimée ; sur Babelio, les demi-notes existent ; (c) l'avis de `Sunread26` conservé est un extrait de blog ; (d) {len(mn13)} avis datent de 2013, dont {n13mn} de Manga-News, souvent écrits **avant la sortie du tome 1** (juin 2013) ; (e) {mn_nonote} commentaires Manga-News sont sans note.

### 1.2. Distribution par verdict et par période

| Verdict | Avis (`N`) | Part | Note moyenne (% échelle) | Réactions médianes | Réactions moyennes | Max réactions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{T['VER']}

| Période | Avis (`N`) | *Positif* (sur notés) | *Mitigé* | *Négatif* | dont Goodreads | Goodreads *Positif* | Goodreads *Mitigé+Négatif* |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{T['PER']}

La baisse apparente entre 2013–2017 et 2018+ vient surtout de la **composition** : en 2013–2017, l'essentiel des avis vient de Manga-News (lecteurs enthousiastes, certains avant la sortie) ; Goodreads n'y compte que {gold[1]} avis, tous positifs. **À l'intérieur de Goodreads**, la part de positifs passe de {P(g1[0],g1[1])} en 2018–2020 (`N = {g1[1]}`, marge ± {moe(g1[1])} points) à {P(g2[0],g2[1])} en 2021–2026 (`N = {g2[1]}`, ± {moe(g2[1])}) : un écart de {round(100*g2[0]/g2[1]-100*g1[0]/g1[1])} points, **dans la marge d'erreur**. Je n'en tire pas de tendance.

---

## 2. Les 5 pôles et la table des critiques récurrentes

### 2.1. Les 5 pôles (texte nettoyé, part des avis qui mentionnent le pôle ; avis en anglais et français seulement)

| Pôle | Goodreads (`N = {len(grc)}`) | Autres sites (`N = {len(asc)}`) | ***Radiant* manga (`N = {NC}`)** | dont avis de 50 mots ou plus (`N = {N50}`) | Rappel FMA (`N = 1 097`) | Rappel HxH (`N = 897`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{T['T21']}

**Ce que montre le tableau** (observations ; la comparaison avec FMA/HxH est indicative, voir § 0) :
1. **La narration (`D = {pp(cov,'D')}`) et les personnages (`C = {pp(cov,'C')}`) sont les pôles les plus cités**, comme dans FMA et HxH. Dans le détail, l'intrigue (`D1 = {pp(cov,'D1')}`) est le premier sous-pôle. Les parts sont plus basses que pour FMA/HxH parce que {sum(1 for r in cov if r['mots']<25)} des {NC} avis ont moins de 25 mots. Sur les avis de 50 mots ou plus, `D = {pp(c50,'D')}` et `C = {pp(c50,'C')}`.
2. **Le visuel pèse plus que dans FMA/HxH par rapport à la narration** : `D / A = {d_a}` (contre 1,61× pour FMA et 1,74× pour HxH) et `A / B = {a_b}`. Les deux sous-corpus sont proches sur ce ratio (Goodreads `{ratio(grc,'D','A')}`, autres sites `{ratio(asc,'D','A')}`), mais le dessin est plus souvent cité sur les autres sites (`A1 = {pp(asc,'A1')}`) que sur Goodreads (`A1 = {pp(grc,'A1')}`). L'art est surtout loué (voir § 3.7 et 3.9).
3. **La tactique de combat est quasi absente** (`E2 = {pp(cov,'E2')}`), comme dans FMA (`5,6 %`), loin de HxH (`17,2 %`). Les combats sont cités (`E1 = {pp(cov,'E1')}`) sans que leur logique soit discutée. **Lecture des {cnt(cov,'E2')} avis repérés en `E2` : 4 sont des faux positifs** (« bluffé » ×2, « cleverly » à propos d'un titre de chapitre, « pas très intelligent » à propos du héros) ; **un seul avis parle de stratégie de combat** (`Tmor`, Babelio T3). Liste détaillée : `Radiant_manga_avis_tactique_de_combat.md`.
4. **Rythme et dramaturgie sont peu cités** (`D2 = {pp(cov,'D2')}`, `D3 = {pp(cov,'D3')}`), très en dessous de HxH pour `D2` (`81,4 %`). Avec des avis courts, je ne conclus pas que le rythme ne pose pas question : voir C5.
5. **Le chara-design (`A3 = {pp(cov,'A3')}`)** est un peu plus cité que dans FMA (`9,9 %`) et HxH (`10,8 %`), mais bien moins que dans l'anime (`29,2 %`). Mes listes ne sont pas celles de FMA/HxH : l'écart est faible et peut être en partie artificiel.
6. **La discrimination (`B1 = {pp(cov,'B1')}`, {pp(c50,'B1')} sur les avis de 50 mots ou plus)** est du même ordre que HxH (`23,4 %`) et sous FMA (`38,6 %`).
7. **L'humour est mentionné par {pp(cov,'HUM')} des avis** ({pp(c50,'HUM')} sur les avis de 50 mots ou plus), nettement plus sur les autres sites ({pp(asc,'HUM')}) que sur Goodreads ({pp(grc,'HUM')}). Ce pôle n'existe pas dans la grille FMA/HxH.

### 2.2. Table de codage des critiques récurrentes

*Couverture : ces 8 catégories couvrent **{mxc} des {NM}** avis mitigés ou négatifs ({P(mxc,NM)}). Les {len(noncodes)} autres ne relèvent d'aucune de ces catégories : avis sans motif précis (ex. `Isak+Even` : *« That was fun! »*, `Lindsay` : *« DNF. Not interesting enough to keep my attention. »*, `Anna Wallman` : *« Too weird for me. »*, plusieurs notes seules comme « 3.5 ») ou avis surtout favorables notés 3 (ex. `Tachan` T3). Elles couvrent aussi des réserves dans **{posc} des {npos}** avis *Positif* ({P(posc,npos)}). **Méthode** : j'ai lu tous les avis *Mitigé* et *Négatif* ; pour les avis *Positif*, j'ai repéré les phrases à réserve par mots-clés (« mais », « but », « however », « un peu trop », etc.) : **des réserves discrètes dans des avis positifs ont pu m'échapper**, donc ces catégories sont plutôt sous-estimées chez les *Positif*. Les catégories sont construites à partir de ces {N} textes : la couverture est en partie circulaire.*

| Rang & catégorie | Total (`N = {N}`) | Goodreads / Autres | Part dans les *Mitigé / Négatif* (`N = {NM}`) | Note moyenne (tous, % échelle) | Note moyenne (*Mit/Nég*) | Réactions *Mit/Nég* (médiane / moyenne) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{T['T22']}

**Répartition par tome** (nombre d'avis qui portent la réserve) :

| Tome | Avis | Positif / Mitigé / Négatif / Non noté | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{T['TT']}

Lecture (observation) : **le déjà-vu (C1), Seth (C2), le texte (C3) et la logique du monde (C6) se concentrent sur le tome 1** (C1 : {cT('C1',1)} avis sur {nT(1)} ; T2 : {cT('C1',2)} sur {nT(2)} ; T3 : {cT('C1',3)} sur {nT(3)} ; C2 : {cT('C2',1)} / {cT('C2',2)} / {cT('C2',3)} ; C3 : {cT('C3',1)} / {cT('C3',2)} / {cT('C3',3)} ; C6 : {cT('C6',1)} / {cT('C6',2)} / {cT('C6',3)}). **L'humour (C4) est la seule catégorie plus fréquente au tome 2 qu'au tome 1** ({cT('C4',2)} sur {nT(2)} contre {cT('C4',1)} sur {nT(1)}). **Au tome 3, il reste surtout le rythme (C5 : {cT('C5',3)} avis), l'humour (C4 : {cT('C4',3)}) et la discrimination appuyée (C8 : {cT('C8',3)})**, soit des réserves plus rares mais d'un autre type. Cela va avec la hausse des notes des sites (Goodreads 3,80 → 4,00 → 4,19). **Attention au biais** : le tome 1 compte {nT(1)} avis, le tome 3 {nT(3)} ; les lecteurs du tome 3 ont déjà aimé les deux premiers ; ce ne sont pas les mêmes personnes qui jugent chaque tome. Les avis « série » ({nT(None)}) portent surtout C1 ({cT('C1',None)} sur {nT(None)}).

---

## 3. Analyse détaillée des critiques récurrentes

*Citations en langue originale (français ou anglais). Format : pseudo (source et tome, verdict, date, note, réactions). Les avis dans d'autres langues sont comptés mais non cités.*

### 3.1. Critique n°1 — Dérivatif, déjà-vu (`{share('C1')}` du corpus ; `{mm('C1')}` des *Mitigé/Négatif*)

* **Ce qui est reproché** : *Radiant* serait un assemblage d'ingrédients de shōnen déjà vus. Œuvres citées dans l'ensemble du corpus (réserves et éloges confondus) : *Naruto* ({wc(r'naruto')} avis), *One Piece* ({wc(r'one\s*piece')}), *Fairy Tail* ({wc(r'fairy\s*tail')}), *Dragon Ball* / Toriyama ({wc(r'dragon\s*ball|toriyama|dbz')}), puis *Blue Exorcist* ({wc(r'blue\s*exorcist')}), *Bleach* ({wc(r'bleach')}), *Black Clover* ({wc(r'black\s*clover')}), *Evangelion* ({wc(r'evangelion')}). **Mentionner une influence n'est pas toujours un reproche** (voir contre-voix). C'est sur SensCritique que la réserve est la plus fréquente ({nd_ratio_sc} avis sur {n_sc}). Répartition : {tomes('C1')} ; langues : {langs('C1')}.
* **Citations** :
{quotes('C1')}
* **Contre-voix** : plusieurs avis reconnaissent la parenté et la jugent assumée ou dépassée.
{quotes('C1c')}

### 3.2. Critique n°2 — Seth et/ou casting irritants ou archétypaux (`{share('C2')}` ; `{mm('C2')}`)

* **Ce qui est reproché** : héros bruyant, impulsif, « bête », typique du shōnen ; casting jugé archétypal. C'est la catégorie dont les avis sont répartis sur le plus grand nombre de langues ({len(set(r['lang2'] for r in R if 'C2' in r['codes']))}). Répartition : {tomes('C2')} ; langues : {langs('C2')}. Dans deux avis (croate, ukrainien), le héros agace au départ puis le jugement s'adoucit ; dans l'avis suédois, il reste agaçant.
* **Citations** :
{quotes('C2')}
* **Contre-voix** : les avis qui commentent les personnages en bien sont plus nombreux : {PR['C']} avis *Positif* sur {npc} mentionnent les personnages (mention, pas forcément louange).
{quotes('C2c')}

### 3.3. Critique n°3 — Surcharge de texte, exposition, planches denses (`{share('C3')}` ; `{mm('C3')}`)

* **Ce qui est reproché** : trop de texte dans les bulles, explications en dialogues (« info dump »), cases très chargées, parfois difficiles à lire (combats compris). **C'est la critique la plus partagée entre langues** : {langs('C3')} ; {n_c3_nonfr} des {catrow('C3')[0]} avis ne sont ni en anglais ni en français, la part la plus élevée des huit catégories. Elle apparaît surtout aux tomes 1 et 2 ({tomes('C3')}). Deux avis du tome 3 (`Tachan` et un avis ukrainien) trouvent la narration plus épurée ou plus dynamique.
* **Citations** :
{quotes('C3')}
* **Contre-voix** : d'autres jugent la lecture fluide et les combats clairs.
{quotes('C3c')}

### 3.4. Critique n°4 — Humour lourd, répétitif, mal dosé ; ton ou public jugé jeune (`{share('C4')}` ; `{mm('C4')}`)

* **Ce qui est reproché** : blagues scatologiques (« pee, poop », « pipi-caca-prout », « en dessous de la ceinture »), répétition des gags, humour « enfantin », sentiment que l'œuvre vise un public plus jeune. Plusieurs avis (espagnol, français, anglais) relèvent aussi des gags ou des remarques jugés sexistes ou ecchi. Répartition : {tomes('C4')} ; langues : {langs('C4')}. **Cette catégorie apparaît à tous les tomes, y compris le tome 3.**
* **Citations** :
{quotes('C4')}
* **Contre-voix** : l'humour est aussi l'un des points forts les plus cités par les avis *Positif* ({PR['HUM']} sur {npc}) ; plusieurs lecteurs francophones l'associent au fait que l'œuvre est française.
{quotes('C4c')}

### 3.5. Critique n°5 — Rythme : démarrage lent, flashbacks ou combats étirés (`{share('C5')}` ; `{mm('C5')}`)

* **Ce qui est reproché** : trois formes différentes. (1) **Démarrage** : le tome 1 / les premières pages jugés lents ou trop longs. (2) **Tome 3 plus long ou plus lent** : cinq avis (anglais, espagnol ×2, ukrainien, français) trouvent le flashback de Hameline ou le combat contre Konrad trop long, ou le tome « longuet ». (3) **Action qui se fait attendre** au tome 2 (SensCritique). Répartition : {tomes('C5')} ; langues : {langs('C5')}. **Contrairement à l'anime** (démarrage lent n°1 avec 50 % des avis), le manga n'a pas de plainte dominante sur le début.
* **Citations** :
{quotes('C5')}
* **Contre-voix** : le tome 1 est jugé introductif mais « prometteur » par plusieurs avis, et au moins trois lecteurs disent que la série s'améliore au fil des tomes.
{quotes('C5c')}

### 3.6. Critique n°6 — Logique du monde, explications absentes ou confuses ; récit brouillon (`{share('C6')}` ; `{mm('C6')}`)

* **Ce qui est reproché** : l'Inquisition « mal expliquée », la logique des infections et des Némésis, la profondeur de la magie, des éléments « introduits de façon brouillonne ». **Une incohérence revient dans plusieurs avis du tome 1** : si les sorciers sont les seuls à pouvoir tuer les Némésis, pourquoi sont-ils craints et sans soutien de l'État (`Albs` en espagnol, `Andre` en anglais ; `The Book Dragon` relève une logique voisine : des villageois qui lancent des pierres à des sorciers puissants). Répartition : {tomes('C6')}. Petit effectif ({catrow('C6')[0]} avis).
* **Citations** :
{quotes('C6')}
* **Contre-voix** : le worldbuilding est l'un des points les plus cités en positif (`B2` mentionné par {PR['B2']} avis *Positif* sur {npc}) ; plusieurs lecteurs aiment justement l'ampleur de l'univers.

### 3.7. Critique n°7 — Dessin jugé moyen, impersonnel ou trop jeune (`{share('C7')}` ; `{mm('C7')}`)

* **Ce qui est reproché** : dessin « sans personnalité » (comparé à d'autres shōnen), « bon sans être excellent », orienté public jeune, absence de décors dans certaines cases. Répartition : {tomes('C7')}. **Elle est presque absente des avis *Positif* ({n_c7_pos} seul)**, et l'art est très loué ailleurs ; c'est la catégorie dont la note moyenne est la plus basse ({catrow('C7')[4]} % de l'échelle), sur {catrow('C7')[0]} avis seulement.
* **Citations** :
{quotes('C7')}
* **Contre-voix** :
{quotes('C7c')}

### 3.8. Critique n°8 — Propos sur la discrimination jugé appuyé, maladroit ou problématique (`{share('C8')}` ; `{mm('C8')}`)

* **Ce qui est reproché** : la métaphore du racisme jugée peu convaincante ou « preachy » ; un avis (T2) trouve que le traitement de l'islamophobie pose problème ; un autre (série) juge le manichéisme « patent » ; trois avis du tome 3 (dont un commentaire Manga-News sans note : « Beaucoup trop manichéen ») jugent le thème de l'exclusion appuyé, gratuit ou trop manichéen. **Effectif très petit ({catrow('C8')[0]} avis)** : {tomes('C8')}. Cinq des {catrow('C8')[0]} avis portent sur les tomes 2 et 3, ceux de l'arc de Rumble Town, où le thème est le plus visible.
* **Citations** :
{quotes('C8')}
* **Contre-voix** : **{len(DISC_IDS)} avis ({len(disc_auth)} auteurs) louent explicitement ce propos** ({', '.join(f"{k} {v}" for k,v in Counter(('Goodreads' if byid[i]['groupe']=='Goodreads' else byid[i]['source']) for i in DISC_IDS).most_common())} ; langues : {', '.join(f"{k} {v}" for k,v in Counter(byid[i]['lang2'] for i in DISC_IDS).most_common())}). C'est un sujet qui **polarise** : aucun des {len(c8_auth)} auteurs de réserves n'en fait partie. Les éloges portent presque tous sur le tome 2 ({Counter(byid[i]['tome'] for i in DISC_IDS)[2]} sur {len(DISC_IDS)}), celui où le thème s'installe.
{quotes('C8c')}

### 3.9. Ce qui est loué le plus souvent (contre-voix d'ensemble)

*Comptage par mots-clés dans les {npc} avis *Positif* en anglais ou français ; une mention n'est pas toujours une louange.*

* **Les personnages** : mentionnés par {PR['C']} avis sur {npc}. **L'humour** : {PR['HUM']}. **Le dessin** : {PR['A1']}. **L'intrigue** : {PR['D1']}. **L'univers / la magie** : {PR['B2']}. **Les combats** : {PR['E1']}. **La discrimination** : {PR['B1']} seulement par mots-clés, mais {len(DISC_IDS)} avis la louent explicitement (§ 3.8).
* **Le fait que ce soit un manga français** : {fr_mentions} avis sur {N} mentionnent la France, le français ou le « manfra ». Plusieurs y voient un plus (humour qui ne sent pas la traduction, dessin à hauteur des mangas japonais).
{quotes('PRAISE')}
* **La série s'améliore avec les tomes** (trois lecteurs ; voir aussi le tableau par tome, § 2.2) :
{quotes('PRAISE2')}

---

## 4. Tableau comparatif : FMA (hors 2003) vs HxH (hors 1999) vs *Radiant* (anime) vs *Radiant* (manga)

| Dimension | *Fullmetal Alchemist* (`N = 1 097`) | *Hunter × Hunter* (`N = 897`) | *Radiant* anime (`N = 48`) | *Radiant* manga (`N = {N}`) |
| :--- | :--- | :--- | :--- | :--- |
| **Verdicts favorables** | **91,0 %** — note moy. **9,02 / 10** | **88,4 %** — note moy. **8,83 / 10** | **64,6 %** — note moy. **6,81 / 10** | **{P(vc['Positif'],N)}** *Positif* ({P(vc['Positif'],n_noterated)} des avis notés ; seuil à 75 % de l'échelle) — note moy. **{mean([r['pct'] for r in R if r['pct'] is not None])} %** de l'échelle |
| **Pôle D — Narration** | **96,1 %** (D2 `42,5 %`) | **97,9 %** (D2 `81,4 %`) | **100 %** (D2 `66,7 %`) | **{pp(cov,'D')}** (D2 `{pp(cov,'D2')}`) ; {pp(c50,'D')} (≥ 50 mots) |
| **Pôle C — Personnages** | **61,4 %** | **77,7 %** | **95,8 %** | **{pp(cov,'C')}** ; {pp(c50,'C')} (≥ 50 mots) |
| **Pôle B — Monde / système** | **56,2 %** | **67,7 %** | **60,4 %** | **{pp(cov,'B')}** ; {pp(c50,'B')} (≥ 50 mots) |
| **Pôle A — Visuel** | **59,6 %** | **56,4 %** | **70,8 %** | **{pp(cov,'A')}** ; {pp(c50,'A')} (≥ 50 mots) |
| **Pôle E — Action** | **41,0 %** (E2 `5,6 %`) | **55,4 %** (E2 `17,2 %`) | **52,1 %** (E2 `4,2 %`) | **{pp(cov,'E')}** (E2 `{pp(cov,'E2')}`) ; {pp(c50,'E')} (≥ 50 mots) |
| **Ratios `D/A` et `A/B`** | `1,61×` ; `1,06×` | `1,74×` ; `0,83×` | `1,41×` ; `1,17×` | `{d_a}` ; `{a_b}` |
| **Critique n°1 (tous avis)** | Rythme début/Briggs (`31,0 %`) | Lenteur/narrateur de *Chimera Ant* (`27,4 %`) | Démarrage lent (`50,0 %`) | **Dérivatif / déjà-vu (`{P(catrow('C1')[0],N)}`)** |
| **Critique n°1 chez les mitigés/négatifs** | Rythme (`37,0 %`) | Lenteur/narrateur (`58,5 %`) | **Héros/casting générique (`82,4 %`)** | **Dérivatif / déjà-vu (`{P(catrow('C1')[3],NM)}`)** |
| **Critique de « classicisme »** | `7,9 %` | `6,1 %` | **`39,6 %`** | **`{P(catrow('C1')[0],N)}`** |

**Lecture (mienne, à ne pas prendre pour un fait)** :
- **Le reproche de déjà-vu (C1) est le plus fréquent dans le manga comme dans l'anime** (`C3` de l'anime : 39,6 % ; ici `{P(catrow('C1')[0],N)}`), très au-dessus des reproches de « classicisme » de FMA et HxH (`7,9 %` et `6,1 %`). Il pèse moins dans le manga, mais les bases diffèrent (anime : 48 avis MAL longs ; manga : {N} avis dont beaucoup sont très courts).
- **Les plaintes sur le héros générique sont bien plus rares dans le manga** : `C2 = {P(catrow('C2')[0],N)}` du corpus, `{P(catrow('C2')[3],NM)}` des mitigés/négatifs, contre `47,9 %` et `82,4 %` pour l'anime. **Le démarrage lent**, premier défaut de l'anime (`50,0 %`), n'est pas dominant chez les lecteurs du manga (`C5 = {P(catrow('C5')[0],N)}`). Je ne tire pas de cause de ces écarts.
- **Un défaut propre au manga : le texte à la page** (C3, {P(catrow('C3')[0],N)}), absent de l'anime. Il est proche, par le thème, de la « surexplication » de l'anime (14,6 %), sans être la même mesure.
- **Écarts à garder en tête** : taille et nature des corpus ({N} avis multilingues, beaucoup d'avis courts, contre 897 et 1 097 critiques MAL), verdicts dérivés de la note et non étiquetés par les sites, listes de mots-clés différentes pour les pôles.

---

## 5. Limites et marges d'erreur

- **Taille** : avec `N = {N}`, une part de 50 % a une marge d'environ ±{moe(N)} points (IC à 95 %) ; avec `N = {NC}` (pôles), ±{moe(NC)} points ; avec `N = {NM}` (mitigés/négatifs), ±{moe(NM)} points. Les écarts entre tomes ou entre catégories rares (C7, C8 : 7 avis chacune ; C6 : {catrow('C6')[0]}) ne sont pas interprétables.
- **Corpus complet pour Goodreads, mais pas représentatif des lecteurs** : seuls les lecteurs qui écrivent un texte sont dans le corpus ({gtxt(1)[1]} avis notés pour {gtxt(1)[3]} notes au tome 1), et ils notent moins bien que l'ensemble (§ 1.1). Pas de conclusion sur « ce que pensent les lecteurs » en général.
- **Autres sites incomplets** : Babelio 59 critiques sur 81 annoncées ; SensCritique limité à la première page ; Booknode et Reddit absents ; pas de critique de rédaction Manga-News pour le tome 3 (elle n'existe pas). Les commentaires Manga-News datent en partie d'avant la sortie. Le corpus francophone est donc plus fragmentaire que le corpus anglophone.
- **Échelles hétérogènes** : un 4/5 Goodreads, un 8/10 SensCritique et un 15/20 Manga-News ne signifient pas la même chose ; les seuils de verdict sont les miens (annexe B). Avec un seuil à 70 % au lieu de 75 %, les `7/10` de SensCritique et les « 3,5/5 » passeraient en *Positif*.
- **Biais de survie par tome** : les lecteurs du tome 3 sont ceux qui ont continué ; le tome 1 compte {nT(1)} avis, le tome 3 {nT(3)}.
- **Notes entières sur Goodreads** : {n_dec} avis annoncent une note décimale ; {n_dec_down_mit} avis *Mitigé* sont des 3,5/5 arrondis à 3 (sans effet sur le verdict).
- **Auteurs répétés** : {n_rep} pseudos apparaissent plus d'une fois ; trois avis ou plus pour {len(rep3)} d'entre eux, dont {', '.join(f"`{a}` ({ac[a]})" for a in rep3[:6])}. Ces pseudos peuvent être des homonymes (« Daniel », « Jessica »). Les auteurs à plusieurs avis pèsent plusieurs fois dans les comptages.
- **Pôles** : codés par mots-clés (annexe A) sur {NC} avis seulement ; une mention n'indique ni un jugement positif ni négatif. Les comptages d'œuvres citées (§ 3.1) et de mentions de la France (§ 3.9) sont aussi faits par mots-clés.
- **C1–C8** : codées à la main (fichier de codage joint). Tous les avis *Mitigé* et *Négatif* ont été lus ; les réserves dans les avis *Positif* ont été repérées par mots-clés et ont pu m'échapper (§ 2.2). Ces catégories sont tirées du corpus lui-même : elles décrivent ces avis, pas un lexique indépendant comme celui de FMA/HxH.
- **Langues** : les avis ukrainiens, espagnols, bulgares, allemands, indonésiens, croates, danois et autres sont codés sur C1–C8 par ma lecture ; je ne suis pas locuteur natif de ces langues, la lecture est donc moins fine que pour l'anglais et le français.
- **Pas de lecture de l'œuvre** : ces chiffres décrivent des avis, pas la qualité du manga.

---

## Annexe A — Listes de mots-clés des pôles (anglais et français, insensibles à la casse)

Voir `/home/user/radiant_manga_analyse/analyse.py` (dictionnaire `POLES`) : une expression régulière par sous-pôle, avec les termes anglais de l'analyse de l'anime et leurs équivalents français (ex. `D2` : *rythme, lent, longuet, traîne, démarr…, explications, flash-back, chapitre*, `A1` : *dessin, graphi…, trait, planches, décors, couleurs, mise en page, découpage*, `B1` : *racisme, discrimin…, xénophob…, préjugés, immigr…, morale, thématiques, bouc émissaire*, `HUM` : *humour, drôle, blagues, gags…*). Retirés par rapport à l'anime : les termes liés à l'animation (*Lerche, CGI, animation*) et à la musique.

## Annexe B — Règle de verdict (note normalisée)

| Échelle | *Positif* (≥ 75 %) | *Mitigé* (41–74 %) | *Négatif* (≤ 40 %) |
| :--- | :--- | :--- | :--- |
| Goodreads `/5` | 4–5 | 3 | 1–2 |
| SensCritique `/10` | 8–10 | 5–7 | 1–4 |
| Manga-News `/20` | 15–20 | 9–14 | 1–8 |
| Askear `/5` ; Nerdbot `/5` | 3,8 → *Positif* | 3,5 → *Mitigé* | — |

Sans note : *Non noté* ; exceptions lues à la main : `TheOASG` (négatif), `Otaku USA` (positif).

Numérotation des catégories C1–C8 : par rang de fréquence dans ce corpus (elle ne correspond donc pas à celle du MD de l'anime).

## Annexe C — Fichiers

- `Radiant_tomes_1_3_corpus_avis.json` (ton fichier) : source des avis Goodreads (textes coupés à environ 500 caractères, sans pseudo), Babelio, Manga-News et SensCritique. `radiant_manga/goodreads_full_parsed.json` : textes complets et pseudos Goodreads que j'ai récupérés.
- `radiant_manga_analyse/codage_critiques_radiant_manga.csv` et `.json` : une ligne par avis ({N}), avec verdict, catégories C1–C8, pôles (anglais/français) et langue détectée.
- `goodreads_radiant_tomes_1_3_complet.json` et `critiques_manga_radiant_autres_sites_complet.json` : le corpus de {N} avis après dédoublonnage (textes complets, pseudos, notes). Les deux anciens JSON (version partielle) sont conservés tels quels.
- Scripts : `radiant_manga_analyse/corpus2.py` (fusion des sources), `prep.py` (dédoublonnage, langues), `analyse.py` (pôles), `codes_v2.py` (codage C1–C8), `stats.py`, `build_md.py` / `write_md.py` (tableaux et citations vérifiées).
"""
open('/home/user/Analyse_critiques_recurrentes_Radiant_manga_Goodreads_et_autres_sites.md','w',encoding='utf8').write(M)
print(len(M))
