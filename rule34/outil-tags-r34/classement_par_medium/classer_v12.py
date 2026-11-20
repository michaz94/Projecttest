# Classement par médium v12 (25/10/2026) : base = sélection dédupliquée 388 (pages 1-390, audit des doublons), compteurs du 24/10 (pages 1-330) et du 25/10 (pages 331-390).
import csv, json
from collections import defaultdict
B='/home/user/outil_tags_r34/'
src=open(B+'classement_par_medium/classer.py',encoding='utf-8').read()
# reprend U, EXC, NOTE, FURRY de la v2 sans relancer son calcul
ns={}; exec(src.split('out=[]')[0].replace("sel=list(","_sel=(").replace("cmp_={","_cmp={"),ns)
A,C,J,W,H,F=ns['A'],ns['C'],ns['J'],ns['W'],ns['H'],ns['F']
U=ns['U']; EXC=ns['EXC']; NOTE=ns['NOTE']; FURRY=set(ns['FURRY'])
cmp_={r['tag_r34']:r for r in csv.DictReader(open(B+'comparaison_sites_195_personnages_2026-10-23.csv',encoding='utf-8-sig'))}
U.update({"Sword Art Online":A,"Miss Kobayashi's Dragon Maid":A,"Cyberpunk: Edgerunners":A,"Honkai: Star Rail":J,"Deltarune":J,
          "Le Monde incroyable de Gumball":W,"Ring (roman et films)":H,"UTAU / Synthesizer V":H,"Dead or Alive":J,"Crash Bandicoot":J})
EXC["sally_acorn"]=(W,"créée pour la série animée Sonic le Rebelle (SatAM, 1993) et les comics Archie, absente des jeux d'origine")
# 24/10 : déplacées en dessins animés occidentaux à la demande de l'utilisateur (popularité rule34 surtout liée à la série 2003)
EXC["raven_(dc)"]=(W,"créée dans les comics (1980) ; déplacée ici à ta demande car sa popularité vient surtout de la série Teen Titans (2003) : 52 % de ses publications ont le tag purple_hair (look de la série), 2,5 % black_hair sans purple_hair")
EXC["starfire"]=(W,"créée dans les comics (1980) ; déplacée ici à ta demande comme Raven (série Teen Titans, 2003) ; tags de version : starfire_(teen_titans) 2 442, starfire_(comics) 1 773")
NOTE["rebecca_(edgerunners)"]="créée pour l'anime Cyberpunk: Edgerunners (2022), univers du jeu Cyberpunk 2077"
NOTE["bowsette"]="création de fans (2018) à partir de Super Mario ; indice e621 1,33 (bowsette_meme), personnage humanoïde"
NOTE["yamamura_sadako"]="roman de Kōji Suzuki (1991) puis films"
NOTE["kasane_teto"]="voix de synthèse UTAU (2008), comme Hatsune Miku pour Vocaloid"
# e621 des nouvelles candidates furry (24/10/2026, API tags.json) ; référence = 743 132 / 3 721 392
REF=743132/3721392
E621_NEW={"sally_acorn":7447,"nicole_watterson":8221,"susie_(deltarune)":9305,"coco_bandicoot":7078,"millie_(helluva_boss)":5190}
U.update({"Uzaki-chan veut traîner !":A,"Panty & Stocking with Garterbelt":A,"Looney Tunes":W,"Hôtel Transylvanie":W,"Kid Icarus":J,"Stellar Blade":J})
EXC["android_21"]=(J,"créée pour le jeu de combat Dragon Ball FighterZ (2018), absente du manga et des anime")
NOTE["tohsaka_rin"]="Fate/stay night est un visual novel (2004), donc classé jeu vidéo"
NOTE["minamoto_no_raikou_(fate/grand_order)"]="créée pour le jeu mobile Fate/Grand Order (2015)"
NOTE["rogue_(x-men)"]="créée dans les comics (1981), aussi très connue par la série X-Men (1992)"
NOTE["mavis_dracula"]="créée pour le film d'animation Hôtel Transylvanie (2012, Sony Pictures Animation)"
E621_NEW["lola_bunny"]=5877
FURRY|=set(E621_NEW)|{"lamb_(league_of_legends)"}
# v6 : nouvelles œuvres des pages 281-290
U.update({"Les Simpson":W,"Yu-Gi-Oh!":A,"Hololive":H,"Apex Legends":J,"Cyberpunk 2077":J})
NOTE["dark_magician_girl"]="apparaît dans le manga Yu-Gi-Oh! (1996) et le jeu de cartes, classée en animanga"
NOTE["ouro_kronii"]="VTuber de l'agence hololive (2021) : personnage-avatar incarné par une personne réelle"
NOTE["marie_rose"]="Dead or Alive 5 (2012) ; 18 ans selon le jeu"
NOTE["panam_palmer"]="jeu Cyberpunk 2077 (2020)"
NOTE["batgirl"]="Barbara Gordon seule (décision du 24/10) : publications taguées Cassandra Cain ou Stephanie Brown retirées"
# v7 : nouvelles œuvres des pages 291-300
U.update({"Black Clover":A})
NOTE["femshep"]="version féminine du Commandant Shepard (héros au choix du joueur, Mass Effect) ; le tag ne désigne que la version féminine"
NOTE["kefla"]="fusion de Kale et Caulifla, créée pour Dragon Ball Super (2017)"
NOTE["violet_parr"]="14 ans dans le film (2004)"
NOTE["noelle_silva"]="15 ans au début de la série"
NOTE["kyoka_jiro"]="lycéenne (15-16 ans), comme Ochaco et Momo"
# v8 : nouvelles œuvres des pages 301-310
U.update({"Darling in the Franxx":A,"The Quintessential Quintuplets":A,"Brawl Stars":J,"Aladdin":W,"Sailor Moon":A,"Bocchi the Rock!":A,"Luz à Osville (The Owl House)":W})
E621_NEW.update({"queen_chrysalis_(mlp)":9521,"noelle_holiday":7082}); FURRY|={"queen_chrysalis_(mlp)","noelle_holiday"}
NOTE["poison_ivy"]="créée dans les comics Batman (1966)"
NOTE["zero_two_(darling_in_the_franxx)"]="anime original (2018, Trigger / A-1 Pictures)"
NOTE["princess_jasmine"]="film d'animation Disney Aladdin (1992)"
NOTE["colette_(brawl_stars)"]="jeu mobile Brawl Stars (Supercell)"
NOTE["usagi_tsukino"]="14 ans au début de la série ; union avec le tag sailor_moon (son identité de guerrière)"
NOTE["gotou_hitori"]="lycéenne (15-16 ans)"
NOTE["luz_noceda"]="14 ans au début de la série (2020)"
NOTE["zenin_maki"]="élève de 2e année de l'école d'exorcisme (16 ans)"
# v9 : nouvelles œuvres et notes des pages 311-330
U.update({"Mortal Kombat":J,"Les Bad Guys":W,"Steven Universe":W,"Harry Potter":H,"WarioWare":J,"Ma vie de robot ado":W,"Gurren Lagann":A,
          "Bayonetta":J,"Foster, la maison des amis imaginaires":W,"Fortnite":J})
# e621 (API tags.json, 24/10/2026) : princess_cadance_(mlp) 8 104 ; diane_foxington 7 994 ; chica_(fnaf) 4 304 ; meow_skulls 5 773 ; poppy_(lol) 3 606 (non furry : yordle humanoïde, comme Midna) ; callie 1 527 ; jenny_wakeman 2 198
E621_NEW.update({"princess_cadance_(mlp)":8104,"diane_foxington":7994,"chica_(fnaf)":4304,"meow_skulls_(fortnite)":5773})
FURRY|={"princess_cadance_(mlp)","diane_foxington","chica_(fnaf)","meow_skulls_(fortnite)"}
NOTE["poppy"]="yordle (League of Legends) ; indice e621 2,60 (poppy_(lol) 3 606) mais personnage humanoïde, laissée en jeux vidéo comme Midna"
NOTE["hermione_granger"]="romans de J. K. Rowling (1997) puis films : ni manga, ni jeu, ni comics, ni dessin animé ; élève de Poudlard (11 à 18 ans selon les tomes)"
NOTE["diane_foxington"]="film d'animation DreamWorks Les Bad Guys (2022), d'après les livres d'Aaron Blabey"
NOTE["mori_calliope"]="VTuber de l'agence hololive (2020) : personnage-avatar incarné par une personne réelle"
NOTE["houshou_marine"]="VTuber de l'agence hololive (2019) : personnage-avatar incarné par une personne réelle"
NOTE["ashley_graves"]="jeune sorcière de WarioWare (2005) ; âge non précisé, apparence d'enfant"
NOTE["nemona_(pokemon)"]="élève de l'académie (Pokémon Écarlate et Violet, 2022), adolescente"
NOTE["jenny_wakeman"]="robot (XJ-9), série Nickelodeon (2003)"
NOTE["caitlyn_kiramman"]="championne de League of Legends (2011), aussi dans la série Arcane (2021)"
NOTE["bayonetta_(character)"]="le tag de licence bayonetta (7 435) n'est pas additionné"
NOTE["uzaki_tsuki"]="mère de Hana Uzaki"
# v10 : nouvelles œuvres et notes des pages 331-340 (25/10/2026) ; aucune nouvelle candidate furry (Amity : sorcière humaine ; Ragatha : poupée de chiffon ; Tristana : yordle humanoïde comme Poppy)
U.update({"Miraculous":W,"Les Griffin (Family Guy)":W,"Guilty Gear":J,"Elden Ring":J})
NOTE["bridget"]="Guilty Gear XX (2002) ; présentée comme une femme trans depuis Guilty Gear Strive (2022)"
NOTE["tristana"]="yordle (League of Legends) : personnage humanoïde, laissée en jeux vidéo comme Poppy"
NOTE["anna_(frozen)"]="film d'animation Disney La Reine des neiges (2013)"
NOTE["marinette_dupain-cheng"]="série animée française Miraculous (2015) ; collégienne puis lycéenne (13-15 ans)"
NOTE["amity_blight"]="14 ans au début de la série (2020), comme Luz"
NOTE["sakura_futaba"]="lycéenne (15-16 ans)"
NOTE["hyuuga_hanabi"]="petite sœur de Hinata : enfant dans Naruto, adolescente dans The Last et Boruto"
NOTE["ragatha_(the_amazing_digital_circus)"]="série web animée Glitch Productions (2023)"
# v11 : nouvelles œuvres et notes des pages 341-360 (25/10/2026)
U.update({"Soulcalibur":J,"DanMachi":A,"Life is Strange":J,"Code Geass":A,"Azur Lane":J,"Mushoku Tensei":A,"Star vs. les forces du mal":W,"Gameoverse":W})
# e621 (API tags.json, 25/10/2026) : kit_bodega 4 216 ; raven_team_leader 3 182 ; trixie_(mlp) 8 055 ; felicia_(darkstalkers) 2 781 (indice 2,28, femme-chat humanoïde : reste en jeux vidéo comme Midna)
E621_NEW.update({"kit_(gameoverse)":4216,"raven_team_leader":3182,"trixie_(mlp)":8055}); FURRY|={"kit_(gameoverse)","raven_team_leader","trixie_(mlp)"}
NOTE["felicia_(darkstalkers)"]="femme-chat de Darkstalkers (1994) ; indice e621 2,28 (felicia_(darkstalkers) 2 781) mais personnage humanoïde, laissée en jeux vidéo comme Midna"
NOTE["gawr_gura"]="VTuber de l'agence hololive (2020) : personnage-avatar incarné par une personne réelle"
NOTE["vi"]="championne de League of Legends (2012), surtout connue par la série Arcane (2021)"
NOTE["lucyna_kushinada"]="créée pour l'anime Cyberpunk: Edgerunners (2022), univers du jeu Cyberpunk 2077"
NOTE["female_chara"]="version féminine de Chara (personnage au genre non défini d'Undertale) ; le tag chara (genre au choix) n'est pas additionné"
NOTE["komi_shuuko"]="mère de Shouko Komi"
NOTE["mitsuki_bakugou"]="mère de Katsuki Bakugo"
NOTE["star_butterfly"]="14 ans au début de la série (2015)"
NOTE["sayori_(doki_doki_literature_club)"]="visual novel Doki Doki Literature Club! (2017), lycéenne"
NOTE["hestia_(danmachi)"]="déesse du light novel DanMachi (2013), connue surtout par l'anime"
NOTE["ghislaine_dedoldia"]="light novel Mushoku Tensei (web novel 2012), connue surtout par l'anime"
NOTE["kit_(gameoverse)"]="série web animée Gameoverse (Glitch Productions)"
NOTE["lapis_lazuli_(steven_universe)"]="Gemme de Steven Universe (2013)"
NOTE["tenten"]="adolescente dans Naruto, adulte dans Boruto"
# v12 : nouvelles œuvres et notes des pages 361-390 (25/10/2026)
U.update({"Kaguya-sama: Love is War":A,"Warcraft":J,"Les Tortues Ninja":C,"Raiponce (Disney)":W,"Le Laboratoire de Dexter":W,"Akame ga Kill!":A,
          "Trials of Mana (Seiken Densetsu 3)":J,"Final Fight":J,"JoJo's Bizarre Adventure":A,"Ranma ½":A,"Kung Fu Panda":W,"Roshidere":A,
          "Dragons (DreamWorks)":W,"La Petite Sirène (Disney)":W,"Gravity Falls":W,"Haydee":J})
# e621 (API tags.json, 25/10/2026) : muffet 3 774 ; surge_the_tenrec 4 342 ; master_tigress 5 263 ; tawna_bandicoot 2 640 ; undyne 6 331 ;
# non furry : tohru_(dragon_maid) 470 (indice 0,44), reisen_udongein_inaba 319, xayah 1, vex_(league_of_legends) 6 (vastaya et yordle humanoïdes, comme Poppy)
E621_NEW.update({"muffet":3774,"surge_the_tenrec":4342,"master_tigress":5263,"tawna_bandicoot":2640,"undyne":6331})
FURRY|={"muffet","surge_the_tenrec","master_tigress","tawna_bandicoot","undyne"}
EXC["luna_snow"]=(J,"créée pour le jeu mobile Marvel Future Fight (2019, Netmarble), puis reprise dans les comics et Marvel Rivals")
EXC["surge_the_tenrec"]=(C,"créée pour les comics IDW Sonic the Hedgehog (Imposter Syndrome, 2021), absente des jeux principaux")
EXC["rey"]=(H,"film en prises de vues réelles Star Wars : Le Réveil de la Force (2015) ; le tag rey est ambigu (rey_(star_wars) : 540)")
NOTE["magik_(illyana_rasputin)"]="créée dans les comics X-Men (1975), personnage jouable de Marvel Rivals (2024)"
NOTE["april_o'neil"]="créée dans les comics Mirage (1984) ; 72 % de ses publications ont aussi le tag de la série animée de 1987 (april_o'neil_(tmnt_1987) : 3 952)"
NOTE["rapunzel"]="film d'animation Disney Raiponce (2010) ; le tag rapunzel est ambigu (aussi Rapunzel de NIKKE, 347, et le conte) ; union avec rapunzel_(tangled)"
NOTE["ariel"]="film d'animation Disney La Petite Sirène (1989) ; le tag ariel est ambigu ; union avec ariel_(the_little_mermaid)"
NOTE["astrid_hofferson"]="film d'animation DreamWorks Dragons (2010), d'après les livres de Cressida Cowell"
NOTE["master_tigress"]="film d'animation DreamWorks Kung Fu Panda (2008)"
NOTE["dexter's_mom"]="série Cartoon Network Le Laboratoire de Dexter (1996)"
NOTE["ranma-chan"]="forme féminine de Ranma Saotome (manga de Rumiko Takahashi, 1987) ; le tag ranma_saotome (genre non défini) n'est pas additionné"
NOTE["corrin_(fire_emblem)_(female)"]="version féminine de Corrin (héros au choix du joueur, Fire Emblem Fates, 2015)"
NOTE["valerie_(cyberpunk_2077)"]="version féminine de V (héros au choix du joueur, Cyberpunk 2077, 2020), comme Femshep"
NOTE["poison_(final_fight)"]="Final Fight (1989) ; genre présenté différemment selon les versions de Capcom (femme trans selon certaines sources officielles japonaises), classée en féminin comme Bridget"
NOTE["purah"]="The Legend of Zelda: Breath of the Wild (2017) : apparence d'enfant dans BotW (rajeunie), adulte dans Tears of the Kingdom (2023)"
NOTE["tohru_(dragon_maid)"]="dragonne sous forme humaine ; indice e621 0,44 (470), non furry"
NOTE["ty_lee"]="14 ans dans la série (2005)"
NOTE["gloria_(pokemon)"]="héroïne de Pokémon Épée et Bouclier (2019), adolescente"
NOTE["wendy_corduroy"]="15 ans dans la série (2012)"
NOTE["kirigaya_suguha"]="union avec leafa (son avatar dans ALfheim Online) ; collégienne puis lycéenne (15 ans)"
NOTE["fujiwara_chika"]="lycéenne"
NOTE["shinomiya_kaguya"]="lycéenne"
NOTE["nakano_miku"]="lycéenne"
NOTE["alisa_mikhailovna_kujou"]="lycéenne ; light novel Roshidere (2021), connue surtout par l'anime"
NOTE["haru_okumura"]="lycéenne"
NOTE["ayase_seiko"]="grand-mère de Momo Ayase"
NOTE["annie_leonhardt"]="15 ans au début de la série"
NOTE["fionna_the_human_girl"]="version féminine de Finn créée dans l'épisode Fionna et Cake (2011)"
NOTE["haydee"]="jeu vidéo Haydee (2016) ; le tag de licence haydee_(game) n'est pas additionné"
NOTE["riesz"]="Seiken Densetsu 3 (1995), refait sous le nom Trials of Mana (2020)"
NOTE["marisa_kirisame"]="série de jeux Touhou Project (1997)"
sel=list(csv.DictReader(open(B+'doublons/selection_388_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig')))
out=[]
for r in sel:
    t=r['tag']; uni=r['univers']
    m=U[uni]; note=NOTE.get(t,'')
    if t in EXC: m,note=EXC[t]
    if uni=='Vocaloid': note="logiciel de synthèse vocale (mascotte), ni jeu ni anime à l'origine"
    if uni=='The Witcher': note="personnage des romans d'Andrzej Sapkowski ; classé en jeux vidéo à ta demande"
    mo=m; pub=int(r['publications_dedup'])
    if t in FURRY:
        m=F
        if t in cmp_: note=f"médium d'origine : {mo} ; e621 {int(cmp_[t]['e621'])} publications, indice e621 {cmp_[t]['indice_e621']}"
        elif t in E621_NEW:
            e=E621_NEW[t]; note=f"médium d'origine : {mo} ; e621 {e} publications, indice e621 {e/int(r['tag_seul_24_10'])/REF:.2f}"
        else: note=f"médium d'origine : {mo} ; pas de tag séparé sur e621, indice estimé à 3,08 via le tag commun kindred_(lol) (5 730)"
        if t=="millie_(helluva_boss)": note+=" ; diablotine (imp) et non animal : rangée en Furry comme Toriel, à confirmer"
    if r['methode'].startswith('tag + gain'): note=(note+' ; ' if note else '')+'tag + gain d’union mesuré (doublons, audit 24/10)'
    out.append(dict(medium=m,medium_origine=mo,personnage=r['personnage'],univers=uni,tag=t,publications=pub,note=note,date_releve=r['date_releve']))
assert len(out)==388
out.sort(key=lambda x:-x['publications'])
for i,o in enumerate(out,1): o['rang_general_388']=i
G=defaultdict(list)
for o in out: G[o['medium']].append(o)
rows=[]
for m in [A,J,C,W,F,H]:
    for i,o in enumerate(G[m],1): o['rang_medium']=i; rows.append(o)
cols=['medium','medium_origine','rang_medium','rang_general_388','personnage','univers','tag','publications','note','date_releve']
with open(B+'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,cols,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
# Markdown
fmt=lambda n:f"{n:,}".replace(',',' ')
order=[A,J,C,W,F,H]; tot=sum(o['publications'] for o in out)
L=["# Classement rule34 par médium : personnages féminins (v12, audit des doublons, pages 1-390)","",
"*Relevés des 24 et 25 octobre 2026. Base : les 388 personnages féminins de `doublons/selection_388_dedupliquee_audit_2026-10-25.csv` (liste des tags rule34.xxx, pages 1 à 390, soit environ 5 000 publications au minimum). Compteurs du 24/10 pour les pages 1 à 330, du 25/10 pour les pages 331 à 390 ; audit complet des doublons : base = compteur du tag principal (liste des tags), plus le gain réel d’union (posts portant un alias ou une version sans le tag principal, mesurés par recherche négative) quand il dépasse 150.*","",
"**Règle de classement :** chaque personnage est rangé selon le médium où il a été créé (exceptions indiquées en Note ; Raven et Starfire, créées dans les comics, sont rangées en dessins animés occidentaux à ta demande, pour la série Teen Titans de 2003). L'Animanga regroupe le manga, l'anime et les light novels.","",
"**Furry :** classement séparé ; ses personnages sont retirés de leur médium d'origine (indiqué en Note). Critères : (1) animal anthropomorphe ou créature animale ; (2) indice e621 d'au moins 2 (part sur e621 rapportée à la part sur rule34). Midna (2,74), Poppy (2,60, yordle humanoïde), Felicia (2,28, femme-chat humanoïde) et Bowsette restent hors Furry (personnages humanoïdes).","",
"## Synthèse","","| Médium | Personnages | Publications cumulées | Part | Moyenne par personnage |","|---|---|---|---|---|"]
for m in order:
    g=G[m]; s=sum(o['publications'] for o in g)
    L.append(f"| {m} | {len(g)} | {fmt(s)} | {s/tot*100:.1f} % | {fmt(round(s/len(g)))} |")
L.append(f"| **Total** | **{len(out)}** | **{fmt(tot)}** | 100 % | |")
for m in order:
    L+=["",f"## {m} ({len(G[m])})","","| # | Rang général (sur 388) | Personnage | Œuvre | Publications | Note |","|---|---|---|---|---|---|"]
    for o in G[m]: L.append(f"| {o['rang_medium']} | {o['rang_general_388']} | {o['personnage']} | {o['univers']} | {fmt(o['publications'])} | {o['note']} |")
open(B+'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
for m in order:
    s=sum(o['publications'] for o in G[m]); print(f"## {m} : {len(G[m])} / {s}")
    for o in G[m][:12]: print(o['rang_medium'],o['rang_general_388'],o['personnage'],'|',o['univers'],o['publications'])
