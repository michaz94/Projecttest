# Sonde l'autocomplétion rule34 pour trouver le tag de chaque franchise (24/10/2026)
import urllib.request, urllib.parse, json, time, html
Q = {"Genshin Impact":"genshin","Pokémon":"pokemon","Marvel":"marvel","My Little Pony":"my_little_pony","DC Comics":"dc_comics","Sonic":"sonic_",
"Naruto":"naruto","My Hero Academia":"my_hero_academia","Overwatch":"overwatch","Dragon Ball":"dragon_ball","League of Legends":"league_of_legends",
"Super Mario":"super_mario","Resident Evil":"resident_evil","Fate":"fate_","Zenless Zone Zero":"zenless","One Piece":"one_piece","Chainsaw Man":"chainsaw_man",
"Five Nights at Freddy's":"five_nights","Bleach":"bleach","RWBY":"rwby","Undertale":"undertale","Avatar (Le Dernier Maître de l'air + La Légende de Korra)":"avatar_",
"Deltarune":"deltarune","Fire Emblem":"fire_emblem","The Legend of Zelda":"the_legend_of_zelda","Final Fantasy VII":"final_fantasy_vii","Street Fighter":"street_fighter",
"Helluva Boss":"helluva","KonoSuba":"kono","The Witcher":"the_witcher","Demon Slayer":"demon_slayer","Doki Doki Literature Club":"doki_doki","Mass Effect":"mass_effect",
"Adventure Time":"adventure_time","NieR: Automata":"nier","Frieren":"frieren","Zootopie":"zootopia","One Punch Man":"one-punch","Animal Crossing":"animal_crossing",
"Fairy Tail":"fairy_tail","Star Fox":"star_fox","Evangelion":"neon_genesis","Friday Night Funkin'":"friday_night","High School DxD":"high_school_dxd",
"Xenoblade Chronicles 2":"xenoblade","Les Indestructibles":"the_incredibles","Kill la Kill":"kill_la_kill","Jujutsu Kaisen":"jujutsu","Re:Zero":"re:zero",
"Kim Possible":"kim_possible","Persona 5":"persona","Blue Archive":"blue_archive","Miss Kobayashi's Dragon Maid":"miss_kobayashi","Splatoon":"splatoon",
"Dead or Alive":"dead_or_alive","Vocaloid":"vocaloid","Metroid":"metroid","Tomb Raider":"tomb_raider","Spy×Family":"spy_x","My Dress-Up Darling":"my_dress",
"Arrête de me chauffer, Nagatoro":"please_don","Fatal Fury / King of Fighters":"king_of_fighters","Ben 10":"ben_10","Scooby-Doo":"scooby","La Reine des neiges":"frozen",
"Star Wars":"star_wars","L'Attaque des Titans":"attack_on","Hollow Knight":"hollow_knight","The Amazing Digital Circus":"the_amazing_digital","Qui veut la peau de Roger Rabbit":"who_framed",
"Shantae":"shantae","BioShock Infinite":"bioshock","Komi cherche ses mots":"komi","SCP Foundation":"scp_foundation","La Route d'Eldorado (DreamWorks)":"the_road_to",
"Dandadan":"dandadan","Darkstalkers":"darkstalkers","The Last of Us":"the_last_of_us","JoJo's Bizarre Adventure":"jojo","Hazbin Hotel":"hazbin","Overlord":"overlord",
"Touhou Project":"touhou","Sword Art Online":"sword_art","Baldur's Gate 3":"baldur","Ring (roman et films)":"the_ring","Honkai: Star Rail":"honkai","Cyberpunk: Edgerunners":"cyberpunk",
"Le Monde incroyable de Gumball":"the_amazing_world","UTAU / Synthesizer V":"utau","Crash Bandicoot":"crash_","Uzaki-chan veut traîner !":"uzaki","Looney Tunes":"looney",
"Panty & Stocking with Garterbelt":"panty_","Hôtel Transylvanie":"hotel_trans","Kid Icarus":"kid_icarus","Stellar Blade":"stellar_blade","Les Simpson":"the_simpsons",
"Yu-Gi-Oh!":"yu-gi-oh","Hololive":"hololive","Apex Legends":"apex_legends","Sailor Moon":"sailor_moon","Cyberpunk 2077":"cyberpunk_2077","Black Clover":"black_clover",
"Aladdin":"aladdin","Darling in the Franxx":"darling_in","Beastars":"beastars","The Quintessential Quintuplets":"go-toubun","Brawl Stars":"brawl_stars",
"Bocchi the Rock!":"bocchi","Luz à Osville (The Owl House)":"the_owl_house"}
EXTRA = ["marvel_comics","sonic_the_hedgehog_(series)","sonic_(series)","naruto_(series)","boku_no_hero_academia","mario_(series)","fate_(series)","fate/grand_order",
"kimetsu_no_yaiba","kono_subarashii_sekai_ni_shukufuku_wo!","sousou_no_frieren","shingeki_no_kyojin","nintendo","disney","pixar","dreamworks","persona_5",
"one_punch_man","fnaf","dragon_ball_z","avatar_the_last_airbender","the_legend_of_korra","neon_genesis_evangelion","evangelion","the_witcher_3","nier:_automata",
"komi-san_wa_komyushou_desu","sono_bisque_doll_wa_koi_wo_suru","ijiranaide_nagatoro-san","street_fighter_6","resident_evil_4","re:zero_kara_hajimeru_isekai_seikatsu",
"kobayashi-san_chi_no_maidragon","uzaki-chan_wa_asobitai!","darling_in_the_franxx","go-toubun_no_hanayome","bocchi_the_rock!","jojo's_bizarre_adventure","the_king_of_fighters","fatal_fury","snk",
"scp","ringu","synthesizer_v","hotel_transylvania","looney_tunes","the_road_to_el_dorado","who_framed_roger_rabbit","kim_possible","zootopia","frozen_(film)","star_wars","star_fox",
"the_incredibles","honkai:_star_rail","honkai_(series)","hollow_knight","one-punch_man","dandadan","dan_da_dan","cyberpunk:_edgerunners","black_clover","jujutsu_kaisen","spy_x_family"]
def ac(q):
    u = 'https://api.rule34.xxx/autocomplete.php?q=' + urllib.parse.quote(q)
    r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'EdeniaResearch/1.0'}), timeout=25).read().decode()
    return [(html.unescape(o['value']), int(o['label'].rsplit('(', 1)[1].rstrip(')'))) for o in json.loads(r)]
out = {}
for f, q in Q.items():
    try: out[f] = ac(q)[:8]
    except Exception as e: out[f] = str(e)
    time.sleep(0.4)
ex = {}
for t in EXTRA:
    try: ex[t] = dict(ac(t)).get(t)
    except Exception as e: ex[t] = str(e)
    time.sleep(0.4)
json.dump(dict(franchises=out, exacts=ex), open('sonde_autocomplete_r34_2026-10-24.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
for f, L in out.items(): print(f, '→', L if isinstance(L, str) else ', '.join(f'{a} {b}' for a, b in L[:6]))
print(ex)
