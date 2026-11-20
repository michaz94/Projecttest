import csv, json
from collections import defaultdict
B='/home/user/outil_tags_r34/'
sel=list(csv.DictReader(open(B+'selection_172_personnages_feminins_2026-10-23.csv',encoding='utf-8-sig')))
cmp_={r['tag_r34']:r for r in csv.DictReader(open(B+'comparaison_sites_195_personnages_2026-10-23.csv',encoding='utf-8-sig'))}
A,C,J,W,H='Animanga','Comics','Jeux vidéo','Cartoons / films d\'animation occidentaux','Hors des 4 médiums'
U={
# Animanga (manga, anime, light novels)
"Arrête de me chauffer, Nagatoro":A,"Bleach":A,"Chainsaw Man":A,"Dandadan":A,"Demon Slayer":A,"Dragon Ball":A,"Evangelion":A,"Neon Genesis Evangelion":A,"Fairy Tail":A,"Frieren":A,"High School DxD":A,"Jujutsu Kaisen":A,"Kill la Kill":A,"Komi cherche ses mots":A,"KonoSuba":A,"Konosuba":A,"L'Attaque des Titans":A,"My Dress-Up Darling":A,"My Hero Academia":A,"Naruto":A,"Naruto / Boruto":A,"One Piece":A,"One Punch Man":A,"One-Punch Man":A,"Overlord":A,"Re:Zero":A,"Spy×Family":A,
# Comics
"DC Comics":C,"Marvel":C,"Marvel (Les 4 Fantastiques)":C,
# Jeux vidéo
"Animal Crossing":J,"Baldur's Gate 3":J,"BioShock Infinite":J,"Blue Archive":J,"Darkstalkers":J,"Doki Doki Literature Club":J,"Fatal Fury / King of Fighters":J,"Fate":J,"Final Fantasy VII":J,"Fire Emblem":J,"Five Nights at Freddy's":J,"Friday Night Funkin'":J,"Genshin Impact":J,"Hollow Knight":J,"League of Legends":J,"League of Legends / Arcane":J,"Mass Effect":J,"Metroid":J,"NieR: Automata":J,"Overwatch":J,"Persona 5":J,"Pokémon":J,"Resident Evil":J,"Resident Evil 4":J,"Resident Evil Village":J,"Shantae":J,"Sonic":J,"Sonic the Hedgehog":J,"Splatoon":J,"Star Fox":J,"Street Fighter":J,"Super Mario":J,"The Last of Us":J,"The Legend of Zelda":J,"Tomb Raider":J,"Touhou Project":J,"Undertale":J,"Xenoblade Chronicles 2":J,"Zenless Zone Zero":J,
# Occident animé
"Adventure Time":W,"Avatar, le dernier maître de l'air":W,"Ben 10":W,"Hazbin Hotel":W,"Helluva Boss":W,"Kim Possible":W,"La Légende de Korra":W,"La Reine des neiges":W,"La Route d'Eldorado (DreamWorks)":W,"Les Indestructibles":W,"My Little Pony":W,"Qui veut la peau de Roger Rabbit":W,"RWBY":W,"Scooby-Doo":W,"The Amazing Digital Circus":W,"Zootopie":W,"Star Wars":W,
# hors
"Vocaloid":H,"The Witcher":J,
}
# exceptions : medium de création du personnage différent de celui de la franchise
EXC={"jessie_(pokemon)":(A,"créée dans l'anime Pokémon (1997), absente des jeux d'origine"),
     "harley_quinn":(W,"créée dans Batman : la série animée (1992), intégrée aux comics ensuite"),
     "ahsoka_tano":(W,"créée pour le film d'animation The Clone Wars (2008)")}
NOTE={"artoria_pendragon":"Fate/stay night est un visual novel (2004), donc classé jeu vidéo",
      "raven_(dc)":"créée dans les comics (1980), très popularisée par la série Teen Titans",
      "starfire":"créée dans les comics (1980), très popularisée par la série Teen Titans",
      "jinx_(league_of_legends)":"personnage du jeu (2013), repris dans la série Arcane",
      "jessica_rabbit":"apparaît d'abord dans un roman (1981), rendue célèbre par le film de 1988",
      "kasumi_(pokemon)":"personnage des jeux Pokémon Rouge/Vert (1996), aussi héroïne de l'anime",
      "yang_xiao_long":"RWBY : websérie américaine (Rooster Teeth) au style anime"}
F='Furry'
FURRY={"judy_hopps","pinkie_pie_(mlp)","twilight_sparkle_(mlp)","princess_celestia_(mlp)","rainbow_dash_(mlp)","princess_luna_(mlp)","applejack_(mlp)","fluttershy_(mlp)","rarity_(mlp)","krystal","toriel","cream_the_rabbit","isabelle_(animal_crossing)","blaze_the_cat","loona_(helluva_boss)","rouge_the_bat","roxanne_wolf_(fnaf)","vanilla_the_rabbit","hornet_(hollow_knight)","ankha","amy_rose","toy_chica_(fnaf)"}
NOTE["midna"]="indice e621 2,74 mais personnage non animal (Twili) : laissée en jeux vidéo"
out=[]
for r in sel:
    c=cmp_.get(r['tag']); assert c, r['tag']
    m=U[r['univers']]; note=NOTE.get(r['tag'],'')
    if r['tag'] in EXC: m,note=EXC[r['tag']]
    if r['univers']=='Vocaloid': note="logiciel de synthèse vocale (mascotte), ni jeu ni anime à l'origine"
    if r['univers']=='The Witcher': note="personnage des romans d'Andrzej Sapkowski ; classé en jeux vidéo à ta demande"
    medium_origine=m
    if r['tag'] in FURRY:
        m=F; note=f"médium d'origine : {medium_origine} ; e621 {int(c['e621'])} publications, indice e621 {c['indice_e621']}"
    out.append(dict(medium=m,medium_origine=medium_origine,personnage=r['personnage'],univers=r['univers'],tag=r['tag'],publications=int(c['r34']),rang_general=int(c['rang_r34']),date_releve=c['date_releve'],note=note))
assert len(out)==172
# rang général parmi les 172 filles
out.sort(key=lambda x:-x['publications'])
for i,o in enumerate(out,1): o['rang_general_172']=i
G=defaultdict(list)
for o in out: G[o['medium']].append(o)
rows=[]
for m in [A,J,C,W,F,H]:
    for i,o in enumerate(G[m],1):
        o['rang_medium']=i; rows.append(o)
cols=['medium','medium_origine','rang_medium','rang_general_172','personnage','univers','tag','publications','note','date_releve']
with open(B+'classement_par_medium/classement_r34_par_medium_2026-10-23.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,cols,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
json.dump({m:len(G[m]) for m in G},open('/tmp/cnt.json','w'))
for m in [A,J,C,W,F,H]:
    t=sum(o['publications'] for o in G[m])
    print(f"## {m} : {len(G[m])} personnages, {t} publications")
    for o in G[m]: print(o['rang_medium'],o['rang_general_172'],o['personnage'],'|',o['univers'],o['publications'],'*' if o['note'] else '')
