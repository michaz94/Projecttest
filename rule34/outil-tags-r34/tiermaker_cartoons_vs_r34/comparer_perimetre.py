# Votes TierMaker « dessins animés » vs rule34, périmètre Comics + Cartoons / films d'animation occidentaux + Furry (24 oct. 2026).
import csv,sys,os,statistics
from scipy.stats import spearmanr
H=os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
sys.path.insert(0,'../tiermaker_87784832'); from r34_top import liste
import identifications as I
os.chdir('../tiermaker_87784832'); L=liste(); os.chdir(H)
V5={r['tag']:r['medium'] for r in csv.DictReader(open('../classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv',encoding='utf-8-sig'))}
CART="Cartoons / films d'animation occidentaux"
import collections; NB=collections.Counter(V5.values())
COURT={"Comics":"Comics",CART:"Cartoons","Furry":"Furry"}
def medium(t):
    if t in V5: return COURT.get(V5[t],"hors périmètre ("+V5[t]+")")
    if t in {"gardevoir","renamon","lopunny","vaporeon","glaceon"}: return "Furry"
    if t in I.JEUX: return "hors périmètre (Jeux vidéo)"
    if t in getattr(I,"ANIME",()): return "hors périmètre (Animanga)"
    if t in I.COMICS: return "Comics"
    if t in I.FURRY: return "Furry"
    return "Cartoons"
P=[x for x in L if not medium(x['tag']).startswith("hors")]
for i,x in enumerate(P,1): x['rp']=i
BY={x['tag']:x for x in P}
f=lambda n:f"{n:,}".replace(","," ")
fr=lambda v,d=2:f"{v:.{d}f}".replace('.',',')
TITRES={"5058287":"« Definitive Cartoon Waifu Tier List » (601 images, 25/10/2025)","8447367":"« Cartoon Girls » (229 images, 03/10/2025)",
"88691896":"« Hottest Female Cartoon Characters » (200 images, 09/02/2025)","91860172":"« Hottest Animated Women Crushes Ranked » (214 images, 21/09/2025)",
"81614596":"« Some of Disney/Pixar's hottest women » (150 images, 13/06/2025 ; paliers S à D + Hard Pass)",
"30083716":"« Female Cartoon Characters » (1 087 images, 09/05/2026)",
"20899730":"« Penultimate Female Cartoon Character Tierlist » (324 images, 24/02/2026 ; paliers S à D + Ewwwwww + Who?)",
"73568440":"« Ranking Female Video Game Charecters » (617 images, 11-18/09/2025 ; modèle jeux vidéo : seules ses 24 images du périmètre — personnages de comics et Furry — sont comparées)",
"436045":"« Cartoon Hotties » (295 images, vote encore ouvert, relevé du 24/10/2026 ; malgré le titre, environ un tiers d'anime, retirés)",
"80408816":"« Waifus Anime, Cartoon and Videogames » (381 images, 17/08/2025 ; modèle tous médiums : animanga et jeux vidéo retirés, images du périmètre identifiées jusqu'au rang 274)"}
NOTE_INC={("5058287",106):"identification incertaine",("5058287",370):"identification incertaine"}
md=["# Votes TierMaker « dessins animés » vs rule34 — périmètre Comics, Cartoons occidentaux et Furry (24 octobre 2026)\n",
f"Liste rule34 du périmètre : les {len(P)-5} personnages féminins de la sélection 388 classés Comics ({NB['Comics']}), Cartoons / films d'animation occidentaux ({NB[CART]}) ou Furry ({NB['Furry']}) dans le classement par médium v12, plus les 5 espèces dessinées surtout en femelle (Gardevoir, Renamon, Lockpin, Aquali, Givrali), rangées en Furry. Tous ont au moins {f(P[-1]['n'])} publications (liste des tags, pages 1 à 390).\n",
"Côté TierMaker : top 100 Average Vote de chaque vote après retrait des personnages hors périmètre (jeux vidéo : Overwatch, Arcane/League of Legends, Castlevania, Peach du film Mario, Pokémon ; animanga : Naruto, One Piece, Pokémon (anime), Yu-Gi-Oh!, Dragon Ball). Les images non identifiées restent à leur place mais sont exclues des calculs.\n",
"Votes à paliers supplémentaires (81614596 : Hard Pass ; 20899730 : Ewwwwww et Who?) : Hard Pass et Ewwwwww comptent comme la note la plus basse (échelle 6 → 1) ; les votes « Who? » (je ne connais pas) sont retirés. Choix fait par toi le 24 oct.\n",
"## Synthèse\n","| Vote | Retirés (hors périmètre) | Identifiés | Distincts | Dans la liste r34 du périmètre | Liste r34 présente dans le modèle | Spearman rang TM / publications r34 |","|---|---:|---:|---:|---:|---:|---|"]
blocs=[]
for e,d in I.EV.items():
    if e in getattr(I,'ANIME_SEUL',()): continue  # vote 100 % animanga : pas de périmètre
    cl={int(r['rang_average']):r for r in csv.DictReader(open(f'../tiermaker_{e}/classement_average_avec_incertitude.csv',encoding='utf-8-sig'))}
    rows=[];best={};retires=[]
    for k in sorted(d):
        if len(rows)==100: break
        t=d[k]
        if t and medium(t).startswith("hors"): retires.append(f"{I.NOMS[t]} ({k})"); continue
        c=cl[k]; rp=len(rows)+1
        if t:
            n=BY[t]['n'] if t in BY else (I.HORS.get(t) if t in I.HORS else next(x['n'] for x in L if x['tag']==t))
            note=[]
            if (e,k) in I.INCERTAIN or (e,k) in NOTE_INC: note.append("identification incertaine")
            if t in I.AMBIGU: note.append("tag générique")
            if t not in BY and t in I.HORS: note.append("compte autocomplétion")
            if t in best: note.append(f"2e image (meilleure : {best[t][0]})")
            else: best[t]=(k,n)
            rows.append(dict(rang_perimetre=rp,rang_tiermaker=k,personnage=I.NOMS[t],medium=medium(t),votants=c['votants'],tag_r34=t,publications_r34=n,
                rang_r34_perimetre=BY[t]['rp'] if t in BY else "sous 5 011",remarque="; ".join(note)))
        elif (e,k) in getattr(I,"SANS_TAG",{}) and getattr(I,"SANS_TAG_MEDIUM",{}).get((e,k),"Cartoons") not in ("Cartoons","Comics","Furry"):
            retires.append(f"{I.SANS_TAG[(e,k)]} ({k})"); continue
        elif (e,k) in getattr(I,"SANS_TAG",{}):
            rows.append(dict(rang_perimetre=rp,rang_tiermaker=k,personnage=I.SANS_TAG[(e,k)],medium=getattr(I,"SANS_TAG_MEDIUM",{}).get((e,k),"Cartoons"),votants=c['votants'],tag_r34="",publications_r34="",rang_r34_perimetre="",remarque="pas de tag rule34 dédié (exclue des calculs)"))
        else:
            rows.append(dict(rang_perimetre=rp,rang_tiermaker=k,personnage="non identifiée",medium="",votants=c['votants'],tag_r34="",publications_r34="",rang_r34_perimetre="",remarque=""))
    assert len(rows)==100 or e in ('80408816','73568440'),(e,len(rows))  # 73568440 : modèle jeux vidéo, toutes ses images du périmètre  # 80408816 : modèle tous médiums, toutes ses images du périmètre
    with open(f'top100_perimetre_{e}_vs_r34_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as o:
        w=csv.DictWriter(o,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    ks=[v[0] for v in best.values()]; ns=[v[1] for v in best.values()]; rho=spearmanr(ks,[-n for n in ns])
    # présence de la liste r34 dans le modèle
    pres={}
    for k,t in d.items():
        if t in BY and (t not in pres or k<pres[t]): pres[t]=k
    for t,k in I.EXTRA[e].items():
        if t in BY and (t not in pres or k<pres[t]): pres[t]=k
    for t,k in I.R34_DANS_MODELE[e].items():
        if t in BY and (t not in pres or k<pres[t]): pres[t]=k
    ident=sum(1 for r in rows if r['tag_r34']); nin=sum(1 for t in best if t in BY)
    md.append(f"| {e} | {len(retires)} | {ident} | {len(best)} | {nin} | {len(pres)} / {len(P)} | {fr(rho.statistic)} ({'p = '+fr(rho.pvalue,4) if rho.pvalue>=0.001 else 'p < 0,001'}, n = {len(best)}) |")
    from collections import Counter
    cm=Counter(r['medium'] for r in rows if r['tag_r34'])
    b=[f"\n## Vote {e} — modèle {TITRES[e]}\n",
       f"Retirés : {', '.join(retires) if retires else 'aucun'}. Répartition des identifiés : Cartoons {cm['Cartoons']}, Comics {cm['Comics']}, Furry {cm['Furry']}. Votants par image : {min(int(r['votants']) for r in rows)} à {max(int(r['votants']) for r in rows)}.\n",
       "### Top 100 TierMaker (périmètre) → rule34\n","| # | Rang TM | Personnage | Médium | Votants | Publications r34 | Rang r34 (périmètre) | Remarque |","|---:|---:|---|---|---:|---:|---|---|"]
    for r in rows:
        b.append(f"| {r['rang_perimetre']} | {r['rang_tiermaker']} | {r['personnage']} | {r['medium']} | {r['votants']} | {f(r['publications_r34']) if r['publications_r34']!='' else ''} | {r['rang_r34_perimetre']} | {r['remarque']} |")
    b+=[f"\n### Liste rule34 du périmètre ({len(P)}) → rang dans ce modèle\n","| Rang r34 | Personnage | Médium | Publications | Rang TM | Votants |","|---:|---|---|---:|---|---:|"]
    for x in P:
        k=pres.get(x['tag'])
        b.append(f"| {x['rp']} | {I.NOMS.get(x['tag'],x['nom'])} | {medium(x['tag'])} | {f(x['n'])} | {(str(k)+(' (incertain)' if ((e,k) in NOTE_INC or (e,k) in I.INCERTAIN) else '')) if k else 'non trouvé'} | {cl[k]['votants'] if k else ''} |")
    blocs+=b
    print(e,len(retires),ident,len(best),nin,len(pres),round(rho.statistic,3),rho.pvalue)
md+=blocs
md+=["\n## Méthode et limites\n",
"- Médium : classement v5 pour les personnages de la sélection ; sinon médium de création (DC/Marvel/Invincible = Comics, Raven et Starfire en Cartoons à ta demande, Harley Quinn en Cartoons comme dans la v5). Les versions Equestria Girls (humaines) sont rattachées aux poneys MLP, donc en Furry.",
"- Identification visuelle sur planches contact (pas d'étiquettes sur ces images) ; cas douteux signalés. Recherche de la liste rule34 dans tout le modèle en miniatures : un personnage peu lisible a pu être manqué.",
"- Publications : sélection 388 dédupliquée (pages 1 à 390) ; sinon autocomplétion rule34 du 24 oct. 2026 (compteurs pouvant être en retard, variantes non fusionnées ; tags génériques signalés).",
"- Spearman sur les personnages distincts identifiés du top 100 du périmètre (meilleure image).",
"- Fichiers : `identifications.py`, `comparer_perimetre.py`, CSV `top100_perimetre_<id>_vs_r34_2026-10-24.csv` (UTF-8 avec BOM)."]
open('comparaison_perimetre_comics_cartoons_furry_2026-10-24.md','w').write("\n".join(md)+"\n")
