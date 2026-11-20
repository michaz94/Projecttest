# Compare le top 100 « Average Vote » du vote TierMaker 87784832 avec le top 100 féminin de rule34 (furry + espèces retenues).
import json,csv
from scipy.stats import spearmanr
import tm_top100 as T
from r34_top import liste
tm=json.load(open('classement_average_avec_incertitude.json')); TMR={x['rang_average']:x for x in tm}
L=liste(); BYTAG={x['tag']:x for x in L}
# rang TierMaker des personnages du top 100 rule34 absents du top 100 TierMaker (OCR des étiquettes + vérification visuelle)
TMRANG={"princess_peach":517,"rouge_the_bat":302,"hyuuga_hinata":328,"loona_(helluva_boss)":222,"amy_rose":1091,"gardevoir":265,"sakura_haruno":720,
"princess_zelda":470,"ochako_uraraka":234,"renamon":1226,"lara_croft":124,"widowmaker":182,"twilight_sparkle_(mlp)":1022,"android_18":255,"mercy":174,
"ahri":295,"frieren":122,"fluttershy_(mlp)":858,"judy_hopps":578,"raiden_shogun":117,"jill_valentine":319,"princess_rosalina":371,"tatsumaki":110,
"toriel":922,"lopunny":565,"rainbow_dash_(mlp)":920,"tracer":447,"hayase_nagatoro":654,"rarity_(mlp)":857,"bulma_briefs":612,"cynthia_(pokemon)":132,
"gwen_tennyson":538,"isabelle_(animal_crossing)":1128,"princess_daisy":812,"artoria_pendragon":273,"ciri":None,"boa_hancock":156,"krystal":1089,
"fern_(sousou_no_frieren)":220,"pinkie_pie_(mlp)":1111,"girlfriend_(friday_night_funkin)":None,"momo_yaoyorozu":125,"cammy_white":112,
"applejack_(mlp)":979,"lucy_heartfilia":215,"jinx_(league_of_legends)":445,"may_(pokemon)":926,"kasumi_(pokemon)":488,"vaporeon":None,
"yang_xiao_long":495,"mina_ashido":262,"ankha":696,"juri_han":216,"princess_celestia_(mlp)":1032,"princess_luna_(mlp)":854,"ganyu_(genshin_impact)":126,
"glaceon":None,"ino_yamanaka":309,"supergirl":111,"power_(chainsaw_man)":138,"aerith_gainsborough":411,"himiko_toga":242,"ruby_rose":610,
"rosa_(pokemon)":738,"hilda_(pokemon)":1017,"lumine_(genshin_impact)":603,"pharah":292,"megumin":320,"blaze_the_cat":900}
for k,(nom,fr,tag) in T.TM.items(): TMRANG.setdefault(tag,k)
f=lambda n:f"{n:,}".replace(","," ")
rows=[]
for k in range(1,101):
    nom,fr,tag=T.TM[k]; x=TMR[k]; s=BYTAG.get(tag)
    n=s['n'] if s else T.HORS[tag]
    rows.append(dict(rang_tiermaker=k,personnage=nom,franchise=fr,moyenne=x['moyenne'],votants=x['votants'],tag_r34=tag,r34=n,
        rang_r34=s['rang'] if s else "hors sélection (< 8 209)",top100_r34="oui" if s and s['rang']<=100 else "non",variantes_non_fusionnees=T.VARIANTES.get(tag,"")))
with open('top100_tiermaker_vs_r34_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as o:
    w=csv.DictWriter(o,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
rows2=[]
for x in L[:100]:
    k=TMRANG.get(x['tag']); t=TMR.get(k) if k else None
    rows2.append(dict(rang_r34=x['rang'],personnage=x['nom'],univers=x['univers'],tag_r34=x['tag'],r34=x['n'],espece_part_femelle=x['espece'],
        rang_tiermaker=k if k else "non trouvé dans le modèle",moyenne_tiermaker=t['moyenne'] if t else "",votants=t['votants'] if t else "",top100_tiermaker="oui" if k and k<=100 else "non"))
with open('top100_r34_vs_tiermaker_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as o:
    w=csv.DictWriter(o,fieldnames=rows2[0].keys()); w.writeheader(); w.writerows(rows2)
commun=[r for r in rows if r['top100_r34']=="oui"]
print('communs',len(commun))
rho=spearmanr([r['rang_tiermaker'] for r in rows],[-r['r34'] for r in rows]); print('TM top100 : rang TM vs r34',rho)
z=[r for r in rows2 if isinstance(r['rang_tiermaker'],int)]
print('r34 top100 présents dans modèle',len(z), spearmanr([r['rang_r34'] for r in z],[r['rang_tiermaker'] for r in z]))
import statistics
print('médiane rang TM des r34 top100 présents',statistics.median([r['rang_tiermaker'] for r in z]))
print('TM top100: hors sélection 217', sum(1 for r in rows if r['rang_r34']=="hors sélection (< 8 209)"))
print('médiane r34 TM top100', statistics.median([r['r34'] for r in rows]))
json.dump(dict(rows=rows,rows2=rows2),open('/tmp/cmp.json','w'),ensure_ascii=False)
