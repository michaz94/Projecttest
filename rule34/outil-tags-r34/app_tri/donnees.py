# Assemble les données de l'application (24/10/2026 ; mises à jour du 25/10 : pages 331-340 et 5 masculins des pages 311-330, puis pages 341-360, puis pages 361-390 ;
# Danbooru des 29 nouvelles : releves/releve_pages_341-360_2026-10-25/danbooru_nouveaux.py ; des 52 suivantes : releves/releve_pages_361-390_2026-10-25/danbooru_nouveaux.py
# (sans tag Danbooru propre : la mère de Dexter (0) et V version féminine (v_(cyberpunk) commun aux deux versions) -> td vide, d = 0) ; Chara (version féminine) : tag Danbooru chara_(undertale), sans distinction de genre).
import csv,json
B='/home/user/outil_tags_r34/'
sel=list(csv.DictReader(open(B+'doublons/selection_388_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig')))
med={r['tag']:r for r in csv.DictReader(open(B+'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv',encoding='utf-8-sig'))}
cmp_=list(csv.DictReader(open(B+'comparaison_sites_195_personnages_2026-10-23.csv',encoding='utf-8-sig')))
D=json.load(open('danbooru_2026-10-24.json'))
R34M=json.load(open('r34_masculins_2026-10-24.json'))
MED_M={'Sonic':'Furry','Tails':'Furry','Shadow':'Furry','Nick Wilde':'Furry','Foxy':'Furry','Fox McCloud':'Furry','Ralsei':'Furry','Spike':'Furry',
 'Naruto Uzumaki':'Animanga','Izuku Midoriya':'Animanga','Monkey D. Luffy':'Animanga','Son Goku':'Animanga','Katsuki Bakugo':'Animanga','Jotaro Kujo':'Animanga','Astolfo':'Animanga',
 'Link':'Jeux vidéo','Aether':'Jeux vidéo','Bowser':'Jeux vidéo','Cloud Strife':'Jeux vidéo','Mario':'Jeux vidéo','Wise':'Jeux vidéo',
 'Spider-Man':'Comics','Venom':'Comics'}
GAIN_M={'monkey_d_luffy':(357,'( monkey_d._luffy ~ luffy ) -monkey_d_luffy'),'izuku_midoriya':(651,'midoriya_izuku -izuku_midoriya'),'spider-man':(735,'peter_parker -spider-man'),'uzumaki_naruto':(0,'naruto_uzumaki -uzumaki_naruto = 0')}
MED_SHORT={"Cartoons / films d'animation occidentaux":'Cartoons','Hors des 4 médiums':'Autres'}
out=[]
for x in sel:
    m=med[x['tag']]
    td=D['dtags'].get(x['tag']) or ''
    out.append(dict(n=x['personnage'],u=x['univers'],s='F',m=MED_SHORT.get(m['medium'],m['medium']),mo=m['note'],
        t=x['tag'],r=int(x['publications_dedup']),b=int(x['tag_seul_24_10']),g=int(x['gain_dedup']),q=x['mesure_gain'],a=1,
        td=td,d=D['res'][td][0] if td else 0))
for r in cmp_:
    if r['sexe']=='F': continue
    t=r['tag_r34']; base=R34M[t]; g,q=GAIN_M.get(t,(0,''))
    td=D['dtags'][t]
    out.append(dict(n=r['personnage'],u=r['univers'],s='M',m=MED_M[r['personnage']],mo='',t=t,r=base+(g if g>150 else 0),b=base,g=g if g>150 else 0,q=q,
        a=1 if t in GAIN_M else 0,td=td,d=D['res'][td][0]))
# 23 personnages masculins des relevés de pages (18 le 24/10/2026, 5 le 25/10) : compteur = liste des tags ; gain d'union mesuré par recherche négative (retenu si > 150)
# (nom, œuvre, médium, tag rule34, compteur, gain mesuré ≈, recherche, tag Danbooru, images Danbooru, note)
EXTRA_M=[
('Batman','DC Comics','Comics','batman',9505,147,'( batman_(bruce_wayne) ~ bruce_wayne ~ bruce_wayne_(injustice_2) ) -batman ≈ 147 (≤ 150)','batman',1888,''),
('Ritsuka Fujimaru (version masculine)','Fate','Jeux vidéo','fujimaru_ritsuka_(male)',9338,63,'( gudao ~ ritsuka_fujimaru_(male) ~ 4 tenues ) -fujimaru_ritsuka_(male) ≈ 63 (≤ 150)','fujimaru_ritsuka_(male)',19322,"protagoniste de Fate/Grand Order (avatar au choix ; le tag ne désigne que la version masculine)"),
('Boyfriend',"Friday Night Funkin'",'Jeux vidéo','boyfriend_(friday_night_funkin)',9298,21,"( boyfriend_(fnf) ~ boyfriend_(friday_night_funkin') ) -boyfriend_(friday_night_funkin) ≈ 21 (≤ 150)","boyfriend_(friday_night_funkin')",240,''),
('Asriel Dreemurr','Undertale','Furry','asriel_dreemurr',9224,105,'( asriel_dreemurr_(god_form) ~ asriel ) -asriel_dreemurr ≈ 105 (≤ 150)','asriel_dreemurr',986,"médium d'origine : Jeux vidéo"),
('Moxxie','Helluva Boss','Furry','moxxie_(helluva_boss)',8599,0,'non mesuré (pas d’alias trouvé)','moxxie_(helluva_boss)',71,"médium d'origine : Cartoons ; diablotin (imp), rangé en Furry comme Millie, à confirmer"),
('Sasuke Uchiha','Naruto','Animanga','sasuke_uchiha',8584,189,'uchiha_sasuke -sasuke_uchiha','uchiha_sasuke',4720,''),
('Freddy Fazbear',"Five Nights at Freddy's",'Furry','freddy_(fnaf)',8525,21,'freddy_fazbear -freddy_(fnaf) ≈ 21 (≤ 150)','freddy_fazbear',313,"médium d'origine : Jeux vidéo"),
('Beast Boy','DC Comics','Cartoons','beast_boy',8422,63,'( garfield_logan ~ 7 versions ) -beast_boy ≈ 63 (≤ 150)','beast_boy_(dc)',378,"créé dans les comics (1965) ; déplacé en Cartoons à ta demande, comme Raven et Starfire (série Teen Titans, 2003)"),
('Leon S. Kennedy','Resident Evil','Jeux vidéo','leon_scott_kennedy',8377,21,'( leon_s._kennedy ~ leon_kennedy ) -leon_scott_kennedy ≈ 21 (≤ 150)','leon_s._kennedy',5487,''),
('Bonnie',"Five Nights at Freddy's",'Furry','bonnie_(fnaf)',8339,0,'non mesuré (les autres tags bonnie_ sont d’autres personnages ou des versions d’artistes)','bonnie_(fnaf)',153,"médium d'origine : Jeux vidéo"),
('Venti','Genshin Impact','Jeux vidéo','venti_(genshin_impact)',8243,21,'( venti ~ venti_(archon)_(genshin_impact) ) -venti_(genshin_impact) ≈ 21 (≤ 150)','venti_(genshin_impact)',8594,''),
('Knuckles','Sonic','Furry','knuckles_the_echidna',8228,63,'( knuckles_(boom) ~ knuckles ) -knuckles_the_echidna ≈ 63 (≤ 150)','knuckles_the_echidna',1349,"médium d'origine : Jeux vidéo"),
('Legoshi','Beastars','Furry','legoshi_(beastars)',7379,0,'non mesuré (legosi_(beastars) 10)','legoshi',287,"médium d'origine : Animanga"),
('Denji','Chainsaw Man','Animanga','denji_(chainsaw_man)',7348,21,'denji_(hybrid_form) -denji_(chainsaw_man) ≈ 21 (≤ 150)','denji_(chainsaw_man)',8437,''),
('Big Macintosh','My Little Pony','Furry','big_macintosh_(mlp)',7346,21,'( big_macintosh ~ big_macintosh_(eg) ) -big_macintosh_(mlp) ≈ 21 (≤ 150)','big_macintosh',21,"médium d'origine : Cartoons"),
('Finn','Adventure Time','Cartoons','finn_the_human',7259,0,'non mesuré (les tags finn_(…) sont d’autres personnages)','finn_the_human',552,''),
('Raikage (A)','Naruto','Animanga','raikage',7255,0,'non mesuré ; environ 820 de ces publications portent aussi le tag d’artiste raikage_art','a_(naruto)',175,"tag du titre de Raikage, surtout le Quatrième (A) ; tag Danbooru a_(naruto)"),
('9S','NieR: Automata','Jeux vidéo','yorha_9s',7235,105,'( 9s_(nier:automata) ~ yorha_no._9_type_s ) -yorha_9s ≈ 105 (≤ 150)','9s_(nier:automata)',2803,''),
# 5 masculins des pages 311-330, ajoutés le 25/10/2026 (gains mesurés le 25/10 ; Danbooru : releves/releve_pages_331-340_2026-10-25/danbooru_nouveaux.py ;
# e621 API tags.json 25/10 : jax_(tadc) 4 725, shining_armor_(mlp) 7 918)
('Dick Grayson (Robin / Nightwing)','DC Comics','Comics','dick_grayson',7003,189,'( nightwing ~ robin_(dick_grayson) ~ nightwing_(series) ) -dick_grayson','dick_grayson',1088,"premier Robin, puis Nightwing ; nightwing_(wof) (Les Royaumes de feu, 701) exclu"),
('Jax','The Amazing Digital Circus','Furry','jax_(the_amazing_digital_circus)',6977,231,'( jax_(tadc) ~ jax_(dancer_outfit) ) -jax_(the_amazing_digital_circus)','jax_(the_amazing_digital_circus)',1402,"médium d'origine : Cartoons ; lapin anthropomorphe, e621 4 725 publications (jax_(tadc)), indice e621 3,39"),
('Shining Armor','My Little Pony','Furry','shining_armor_(mlp)',6848,0,'non mesuré (variante shining_armor : 128 au plus, sous le seuil de 150)','shining_armor',24,"médium d'origine : Cartoons ; e621 7 918 publications, indice e621 5,79"),
('Ichigo Kurosaki','Bleach','Animanga','ichigo_kurosaki',6610,189,'kurosaki_ichigo -ichigo_kurosaki','kurosaki_ichigo',3309,''),
('Ash Ketchum (Sacha en VF)','Pokémon','Animanga','ash_ketchum',6576,0,'satoshi_(pokemon) -ash_ketchum = 0','ash_ketchum',6468,"héros de l'anime Pokémon (1997), inspiré de Red des jeux : rangé en Animanga"),
]
for n,u,m,t,b,g,q,td,d,note in EXTRA_M:
    gg=g if g>150 else 0
    out.append(dict(n=n,u=u,s='M',m=m,mo=note,t=t,r=b+gg,b=b,g=gg,q=q,a=0 if q.startswith('non mesuré') else 1,td=td,d=d))
json.dump(out,open('donnees_app_2026-10-24.json','w'),ensure_ascii=False)
print(len(out),sum(1 for o in out if o['s']=='M'))
