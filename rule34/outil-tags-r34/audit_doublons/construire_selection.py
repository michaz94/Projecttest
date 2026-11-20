# Construit doublons/selection_205_dedupliquee_audit_2026-10-24.csv (audit complet des doublons, 24/10/2026).
# Base commune = compteur « tag seul » de la liste des tags / autocomplétion (tag_seul_24_10), comme le relevé.
# On n'ajoute que le GAIN réel d'union : posts portant un alias/une version SANS le tag principal,
# mesuré par recherche négative rule34.xxx (gain ≈ dernier pid + 21) ou par union − tag principal
# mesurés tous deux par recherche. Union retenue si gain > 150 ; sinon « tag seul ».
# Toutes les requêtes et pids : audit_doublons/pids_audit_2026-10-24.txt
import csv
B='/home/user/outil_tags_r34/'
src=B+'doublons/selection_205_dedupliquee_2026-10-24.csv'
out=B+'doublons/selection_205_dedupliquee_audit_2026-10-24.csv'
rows=list(csv.DictReader(open(src,encoding='utf-8-sig')))

# tag principal -> (gain, requête/mesure)
G={
 'ochako_uraraka':(1491,'uraraka_ochako -ochako_uraraka'),
 'yor_briar':(1743,'yor_forger -yor_briar'),
 'miruko':(4389,'( rumi_usagiyama ~ mirko ) -miruko'),
 'supergirl':(1953,'kara_zor-el -supergirl ; versions (injustice, maws, dcau, sasha_calle) : ≤ 42'),
 'princess_zelda':(231,'( zelda_(tears_of_the_kingdom) ~ zelda_(breath_of_the_wild) ) -princess_zelda'),
 'power_girl':(231,'karen_starr -power_girl ; versions injustice : ≤ 42'),
 'yuuki_asuna':(693,'( asuna_(sao) ~ asuna_yuuki ) -yuuki_asuna'),
 'akali':(1029,'( akali_jhomen_tethi ~ akali_(league_of_legends) ) -akali'),
 'kamado_nezuko':(777,'( nezuko_kamado ~ nezuko_(demon_form) ) -kamado_nezuko'),
 'yamamura_sadako':(441,'sadako_yamamura -yamamura_sadako'),
 'ilulu_(dragon_maid)':(273,'( ilulu_(maidragon) ~ ilulu ) -ilulu_(dragon_maid)'),
 'higashiyama_kobeni':(357,'kobeni_higashiyama -higashiyama_kobeni'),
 'sona_buvelle':(357,'sona_(league_of_legends) -sona_buvelle'),
 'emma_frost':(189,'( emma_frost_(marvel_rivals) ~ emma_frost_(x-revolution) ~ emma_frost_(white_wave_queen) ) -emma_frost'),
 'gwen_stacy':(399,'( gwen_stacy_(spider-verse) ~ gwen_stacy_(classic) ~ spider-gwen ) -gwen_stacy'),
 'harley_quinn':(588,'union 26 334 − tag 25 746 (pids, recherche)'),
 'tsunade':(420,'union 41 118 − tag 40 698 (pids, recherche)'),
 'kitagawa_marin':(924,'union 29 862 − tag 28 938 (pids, recherche)'),
 'reimu_hakurei':(588,'union 10 542 − tag 9 954 (pids, recherche)'),
 'mina_ashido':(420,'union 17 766 − tag 17 346 (pids, recherche)'),
 'uzumaki_kushina':(378,'union 10 752 − tag 10 374 (pids, recherche)'),
 'tsuyu_asui':(336,'union 13 272 − tag 12 936 (pids, recherche)'),
 'momo_yaoyorozu':(168,'union 18 942 − tag 18 774 (pids, recherche)'),
 'kugisaki_nobara':(168,'union 15 162 − tag 14 994 (pids, recherche)'),
 'akeno_himejima':(168,'union 11 214 − tag 11 046 (pids, recherche)'),
 'rei_ayanami':(168,'union 10 122 − tag 9 954 (pids, recherche)'),
 'kanroji_mitsuri':(903,'mitsuri_kanroji -kanroji_mitsuri'),
 'kochou_shinobu':(231,'shinobu_kocho -kochou_shinobu'),
 'charlie_morningstar_(hazbin_hotel)':(273,'charlie_morningstar -charlie_morningstar_(hazbin_hotel)'),
 'himiko_toga':(441,'toga_himiko -himiko_toga'),
 'bulma_briefs':(231,'( bulma_(dragon_ball) ~ bulma_briefs_(frieza_saga) ~ bulma_(bunny) ) -bulma_briefs'),
 'mythra':(945,'mythra_(xenoblade) -mythra'),
 'pyra':(735,'pyra_(xenoblade) -pyra'),
 'chel':(525,'chel_(the_road_to_el_dorado) -chel'),
 'krystal':(399,'( krystal_(star_fox) ~ krystal_(assault_outfit) ) -krystal'),
 'artoria_pendragon':(1323,'artoria_pendragon_(fate) -artoria_pendragon (versions Lancer/Alter non comptées : autres Servants)'),
}
PSY_GAIN=2499  # psylocke_(kwannon) -psylocke ; versions Marvel Rivals/Sai : ≤ 42

# anciennes unions abandonnées (gain réel ≤ 150) -> note
NOTE_TAG_SEUL={
 'hyuuga_hinata':'ancienne union abandonnée : ( uzumaki_hinata ~ hinata_hyuuga ) -hyuuga_hinata ≤ 42 ; l’écart venait du compteur périmé',
 'sakura_haruno':'ancienne union abandonnée : haruno_sakura -sakura_haruno = 0',
 'shihouin_yoruichi':'ancienne union abandonnée : yoruichi_shihouin -shihouin_yoruichi = 0',
 'kasumi_(pokemon)':'ancienne union abandonnée : misty_(pokemon) -kasumi_(pokemon) = 0',
 'matsumoto_rangiku':'rangiku_matsumoto -matsumoto_rangiku = 0',
 'makima_(chainsaw_man)':'makima -makima_(chainsaw_man) ≈ 147 (≤ 150)',
 'mercy':'( mercy_(overwatch) ~ mercy_(overwatch_2_suit) ) -mercy ≈ 147 (≤ 150)',
 'catwoman':'versions + selina_kyle -catwoman ≈ 147 (≤ 150)',
 'starfire':'( starfire_(teen_titans) ~ starfire_(comics) ~ koriand\'r ) -starfire ≈ 147 (≤ 150)',
 'chun-li':'union − tag = 42 (recherche)',
 'hayase_nagatoro':'union − tag = 84 (recherche)',
}
for t in ['raven_(dc)','samus_aran','lara_croft','jill_valentine','wonder_woman','ankha','helen_parr','black_cat_(marvel)','midna','invisible_woman','ellie_(the_last_of_us)']:
    NOTE_TAG_SEUL[t]='ancienne union abandonnée : union (recherche) − tag ≤ 150, donc gain ≤ 150'

res=[]
for x in rows:
    t=x['tag']; base=int(x['tag_seul_24_10'])
    y=dict(x)
    if t.startswith('psylocke'):
        y['gain_dedup']=str(PSY_GAIN); y['publications_dedup']=str(base+PSY_GAIN)
        y['methode']='tag + gain d’union (ajout : absente du relevé par tag seul)'
        y['mesure_gain']='psylocke_(kwannon) -psylocke ; versions Marvel Rivals/Sai ≤ 42'
    elif t in G:
        g,q=G[t]
        y['gain_dedup']=str(g); y['publications_dedup']=str(base+g)
        y['methode']='tag + gain d’union (> 150)'; y['mesure_gain']=q
        y['date_releve']='2026-10-24'
    else:
        y['gain_dedup']='0'; y['publications_dedup']=str(base)
        y['methode']='tag seul'; y['mesure_gain']=NOTE_TAG_SEUL.get(t,'')
    res.append(y)

res.sort(key=lambda y:-int(y['publications_dedup']))
for i,y in enumerate(res,1):
    y['rang_dedup']=str(i)
    y['effet_dedup']='ajout' if not y['rang_tag_seul_24_10'] else str(int(y['rang_tag_seul_24_10'])-i)
cols=['rang_dedup','effet_dedup','rang_tag_seul_24_10','rang','personnage','univers','tag','publications','tag_seul_24_10','gain_dedup','publications_dedup','methode','mesure_gain','date_releve','source']
with open(out,'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore'); w.writeheader(); w.writerows(res)
print(len(res),'lignes ; unions',sum(1 for y in res if y['gain_dedup']!='0'),'; min',res[-1]['personnage'],res[-1]['publications_dedup'])
missing=[t for t in G if t not in {x['tag'] for x in rows}]
print('tags G absents :',missing)
missing2=[t for t in NOTE_TAG_SEUL if t not in {x['tag'] for x in rows}]
print('tags notes absents :',missing2)
for y in res[:60]:
    print(y['rang_dedup'],y['effet_dedup'],y['personnage'],y['publications_dedup'],y['gain_dedup'])
