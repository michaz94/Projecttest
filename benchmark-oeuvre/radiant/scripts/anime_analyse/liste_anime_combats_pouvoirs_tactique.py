import sys,re
sys.path.insert(0,'/home/user/radiant_analyse')
from scan_anime import R,sents,TAC,COMB,POW
D={r['id']:r for r in R}
MASK="*(extrait masqué : il dévoile des événements de la fin de la saison 2)*"
OVR={'S2-0':MASK,
 'S2-11':"Too much talk […] than action, plot = decent, dont feel really hype for the next episode"}
LOV={('S1-35','h'):"an utterly detestable and braindead protagonist that blindly runs around and screams nonstop like a crying toddle[r]",
 ('S1-35','c'):"cheap animation, cheap fight scenes, bland art and sound",
 ('S1-23','p'):"it isn't the whole I'm a over powered mc that has too much magic off the bat",
 ('S1-19','p'):"the curses are unique and inventive",
 ('S1-19','c'):"Grimm has excellent style, a cool aesthetic and badass combat abilities."}
CUR=['c']
def ex(i,keys,n=3):
    if (i,CUR[0]) in LOV: return LOV[(i,CUR[0])]
    if i in OVR: return OVR[i]
    out=[s for s in sents(D[i]['txt']) if any(k.lower() in s.lower() for k in keys)]
    assert out,(i,keys)
    return ' […] '.join(x if len(x)<=300 else x[:297]+'…' for x in out[:n]).replace('|','/')
def row(n,i,tag,keys):
    r=D[i]
    return f"| {n} | `{r['auteur']}` | Saison {r['saison']} | {r['reco']} ({r['note']}/10) | **{tag}** | {ex(i,keys)} | `{i}` |"
def table(L,k):
    CUR[0]=k
    rows=["| # | Auteur | Saison | Verdict MAL (note) | Sens | Extrait | id |","| :-: | :--- | :--- | :--- | :--- | :--- | :--- |"]
    rows+=[row(n,*x) for n,x in enumerate(L,1)]
    return '\n'.join(rows)
TACT=[('S1-19','Mixte (style de combat)',['defense and offense bipolarity']),
 ('S1-12','Réserve (règles du pouvoir)',['power ups','God powers randomly','plot dictates']),
 ('S1-1','Réserve (variété des combats)',['Titan Punch','seen the first fight','choreography']),
 ('S1-26','Réserve (créativité)',['isn\'t very creative']),
 ('S2-6','Mixte (comparaison à HxH)',['HxH'])]
HERO=[('S1-1','Réserve',['recklessness and daredevil']),('S1-3','Réserve',['reckless, childish']),('S1-35','Réserve',['blindly runs around'])]
COMBA=[('S1-1','Réserve',['choreography','seen the first fight']),('S1-2','Éloge',['fight scenes are so']),('S1-10','Mixte',['The best fight','lacks the intensity','filled to the brim']),
 ('S1-13','Mixte',['not the best fighting scenes']),('S1-14','Mixte',['spell effects are nice']),('S1-19','Éloge',['badass combat abilities']),
 ('S1-20','Éloge',['decent fight scenes']),('S1-24','Éloge',['great fighting scenes']),('S1-26','Éloge',['Action scenes are decently']),
 ('S1-27','Réserve',['not enough action']),('S1-32','Réserve',['action picks up']),('S1-35','Réserve',['cheap fight scenes']),
 ('S2-0','Éloge',['battle of epic']),('S2-2','Éloge',['battles continue to amp up']),('S2-4','Mixte',['had better action scenes']),
 ('S2-6','Mixte',['fights on the level']),('S2-7','Éloge',['fight scenes were not half bad']),('S2-9','Éloge',['decent fight scenes']),('S2-11','Réserve',['talk'])]
POWA=[('S1-1','Neutre',['not very talented in the art of magic','defensive abilities']),('S1-3','Réserve',['bland all the spells']),('S1-12','Réserve',['power ups','God powers randomly','plot dictates','imperial army employ']),
 ('S1-13','Éloge',['solid magic system']),('S1-14','Éloge',['spell effects are nice']),('S1-19','Éloge',['curses are unique']),('S1-23','Éloge',['over powered mc']),
 ('S1-26','Réserve',['power isn\'t very creative']),('S1-31','Éloge',['magic system']),('S1-33','Réserve',['also have weird powers']),
 ('S1-34','Réserve',['magic macguffins']),('S1-35','Réserve',['overpowered MC']),('S2-6','Mixte',['varied powers','spells are usually'])]
used_c={i for i,_,_ in COMBA}; used_p={i for i,_,_ in POWA}
def other(rx,used):
    out=[]
    for r in R:
        if r['id'] in used: continue
        h=[s for s in sents(r['txt']) if rx.search(s)]
        if h: out.append(r['id'])
    return out
M=f"""# *Radiant* (anime, MAL) — avis sur les tactiques de combat, les combats et le système de pouvoir

**Source** : les 48 critiques MAL de l'anime (saison 1 : 36 ; saison 2 : 12), texte déjà filtré (phrases sur les épisodes filler du début de la saison 1 retirées). Extraits en anglais exacts. **Rien n'est quoté qui dévoile la fin de la saison 2** : un avis est listé avec son extrait masqué, un autre est coupé.

## Réponse courte
- **Tactique de combat : aucun des 48 avis ne parle de stratégie ou de tactique dans les combats.** Mon repérage par mots-clés (tactic, strategy, outsmart, clever, plan, intelligent, reckless, choreography, stakes…) ne ressort que des faux positifs et des remarques indirectes (tableau 1).
- Les avis parlent des combats surtout pour juger **la chorégraphie, la fluidité et l'animation** (tableau 3). Le système de pouvoir est commenté en peu de mots (tableau 4).
- Je ne peux pas dire *pourquoi* les critiques n'en parlent pas : tu as lu l'œuvre, pas moi.

**Limites** : 48 avis MAL, pas un échantillon représentatif. Un avis qui parle de tactique sans ces mots a pu m'échapper. Le classement « Sens » est ma lecture.

## 1. Avis proches de la question « tactique » ({len(TACT)})
*Aucun ne parle de stratégie de combat au sens strict. Ils portent sur le style de combat de l'équipe, la logique des pouvoirs, la variété des combats ou la comparaison avec HxH.*

{table(TACT,'t')}

## 2. Seth qui se bat sans réfléchir ({len(HERO)})
*Le style « bullheaded brawler » de Seth est aussi relevé dans le tableau 1 (`S1-19`).*

{table(HERO,'h')}

## 3. Les combats : jugés ou commentés ({len(COMBA)} avis)
{table(COMBA,'c')}

**Mentionnent les combats sans les juger ({len(other(COMB,used_c))})** : {', '.join('`'+D[i]['auteur']+'` (`'+i+'`)' for i in other(COMB,used_c))}.

## 4. Le système de pouvoir : jugé ou commenté ({len(POWA)} avis)
{table(POWA,'p')}

**Mentionnent la magie, les sorciers ou l'infection sans les juger ({len(other(POW,used_p))})** : surtout des résumés du pitch (`{'`, `'.join(D[i]['auteur'] for i in other(POW,used_p)[:12])}`…).

## 5. Lecture rapide (observations)
- **Combats** : l'animation est le sujet principal (fluidité, chorégraphie « correcte mais pas spectaculaire », images sautées). Les éloges portent sur les scènes de combat en général, avec plus de nuances sur l'intensité. Les deux saisons sont citées ; un avis de la saison 2 trouve que la saison 1 (arc de Rumble Town) avait de meilleures scènes d'action.
- **Système de pouvoir** : les éloges sont brefs (« solid magic system », « curses are unique and inventive », héros pas surpuissant d'entrée) ; les réserves visent les règles jugées arbitraires, le manque de créativité du pouvoir de Seth et la ressemblance avec d'autres shōnens. **Un point propre à l'anime** : la couleur et le rendu des sorts (« green sparkles », « blobs of color »).
- **Tactique** : même constat que pour le manga, mais avec 48 avis seulement, donc encore moins de matière.
"""
open('/home/user/Radiant_anime_avis_tactique_combats_et_systeme_de_pouvoir.md','w',encoding='utf8').write(M)
print(len(TACT),len(HERO),len(COMBA),len(POWA),len(other(COMB,used_c)),len(other(POW,used_p)))
