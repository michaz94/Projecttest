# Tag de franchise retenu pour chaque franchise (rule34 : 110 ; Danbooru : 50) et son nombre total de publications (24/10/2026).
# rule34 : compteur de l'autocomplétion (api.rule34.xxx), sauf 2 unions mesurées par recherche OR (dernière page + 21).
# Danbooru : post_count de l'API (tags.json) ; le tag de franchise est celui des personnages (implications Danbooru = toutes les sous-séries).
import json, csv
S = json.load(open('sonde_autocomplete_r34_2026-10-24.json', encoding='utf-8'))
C = {}
for L in S['franchises'].values():
    if isinstance(L, list): C.update({a: b for a, b in L})
C.update({k: v for k, v in S['exacts'].items() if isinstance(v, int)})
C.update({'bishoujo_senshi_sailor_moon': 26100, 'dc': 172923, 'final_fantasy': 161402, 'avatar_legends': 34521})
# franchise → (tag retenu, autres tags concurrents notés)
T = {"Genshin Impact": "genshin_impact", "Pokémon": "pokemon", "Marvel": ("marvel", "marvel_comics"), "My Little Pony": "my_little_pony",
 "DC Comics": ("dc_comics", "dc"), "Sonic": ("sonic_(series)", "sonic_the_hedgehog_(series)"), "Naruto": ("naruto_(series)", "naruto"),
 "My Hero Academia": ("my_hero_academia", "boku_no_hero_academia"), "Overwatch": "overwatch", "Dragon Ball": "dragon_ball", "League of Legends": "league_of_legends",
 "Super Mario": ("mario_(series)", "super_mario_bros."), "Resident Evil": "resident_evil", "Fate": ("fate_(series)", "fate/grand_order"), "Zenless Zone Zero": "zenless_zone_zero",
 "One Piece": "one_piece", "Chainsaw Man": "chainsaw_man", "Five Nights at Freddy's": "five_nights_at_freddy's", "Bleach": "bleach", "RWBY": "rwby",
 "Undertale": ("undertale", "undertale_(series) (inclut probablement Deltarune)"), "Deltarune": "deltarune", "Fire Emblem": "fire_emblem",
 "The Legend of Zelda": "the_legend_of_zelda", "Final Fantasy VII": ("final_fantasy_vii", "final_fantasy (toute la série)"), "Street Fighter": "street_fighter",
 "Helluva Boss": "helluva_boss", "KonoSuba": ("kono_subarashii_sekai_ni_shukufuku_wo!", "konosuba"), "The Witcher": ("the_witcher_(series)", "the_witcher_3:_wild_hunt"),
 "Demon Slayer": ("demon_slayer", "kimetsu_no_yaiba"), "Doki Doki Literature Club": "doki_doki_literature_club", "Mass Effect": "mass_effect", "Adventure Time": "adventure_time",
 "NieR: Automata": ("nier:_automata", "nier"), "Frieren": ("sousou_no_frieren", "frieren_beyond_journey's_end"), "Zootopie": "zootopia", "One Punch Man": "one-punch_man",
 "Animal Crossing": "animal_crossing", "Fairy Tail": "fairy_tail", "Star Fox": "star_fox", "Evangelion": "neon_genesis_evangelion", "Friday Night Funkin'": "friday_night_funkin",
 "High School DxD": "high_school_dxd", "Xenoblade Chronicles 2": ("xenoblade_chronicles_2", "xenoblade_(series)"), "Les Indestructibles": "the_incredibles",
 "Kill la Kill": "kill_la_kill", "Jujutsu Kaisen": "jujutsu_kaisen", "Re:Zero": "re:zero_kara_hajimeru_isekai_seikatsu", "Kim Possible": "kim_possible",
 "Persona 5": ("persona_5", "persona (toute la série)"), "Blue Archive": "blue_archive", "Miss Kobayashi's Dragon Maid": ("miss_kobayashi's_dragon_maid", "kobayashi-san_chi_no_maidragon"),
 "Splatoon": ("splatoon", "splatoon_(series)"), "Dead or Alive": "dead_or_alive", "Vocaloid": "vocaloid", "Metroid": "metroid", "Tomb Raider": "tomb_raider",
 "Spy×Family": "spy_x_family", "My Dress-Up Darling": ("sono_bisque_doll_wa_koi_wo_suru", "my_dress_up_darling"), "Arrête de me chauffer, Nagatoro": "please_don't_bully_me,_nagatoro",
 "Ben 10": "ben_10", "Scooby-Doo": "scooby-doo", "La Reine des neiges": ("frozen_(film)", "frozen_2"), "Star Wars": "star_wars", "L'Attaque des Titans": ("attack_on_titan", "shingeki_no_kyojin"),
 "Hollow Knight": "hollow_knight", "The Amazing Digital Circus": "the_amazing_digital_circus", "Qui veut la peau de Roger Rabbit": "who_framed_roger_rabbit", "Shantae": "shantae",
 "BioShock Infinite": ("bioshock_infinite", "bioshock"), "Komi cherche ses mots": "komi-san_wa_komyushou_desu", "SCP Foundation": "scp_foundation",
 "La Route d'Eldorado (DreamWorks)": "the_road_to_el_dorado", "Dandadan": "dandadan", "Darkstalkers": "darkstalkers", "The Last of Us": ("the_last_of_us", "the_last_of_us_2"),
 "JoJo's Bizarre Adventure": "jojo's_bizarre_adventure", "Hazbin Hotel": "hazbin_hotel", "Overlord": "overlord_(maruyama)", "Touhou Project": "touhou", "Sword Art Online": "sword_art_online",
 "Baldur's Gate 3": "baldur's_gate_3", "Ring (roman et films)": ("the_ring", "ringu"), "Honkai: Star Rail": "honkai:_star_rail", "Cyberpunk: Edgerunners": "cyberpunk:_edgerunners",
 "Le Monde incroyable de Gumball": "the_amazing_world_of_gumball", "UTAU / Synthesizer V": ("utau", "synthesizer_v"), "Crash Bandicoot": ("crash_(series)", "crash_bandicoot_(series)"),
 "Uzaki-chan veut traîner !": "uzaki-chan_wa_asobitai!", "Looney Tunes": "looney_tunes", "Panty & Stocking with Garterbelt": "panty_&_stocking_with_garterbelt",
 "Hôtel Transylvanie": "hotel_transylvania", "Kid Icarus": "kid_icarus", "Stellar Blade": "stellar_blade", "Les Simpson": "the_simpsons", "Yu-Gi-Oh!": "yu-gi-oh!",
 "Hololive": "hololive", "Apex Legends": "apex_legends", "Sailor Moon": "bishoujo_senshi_sailor_moon", "Cyberpunk 2077": "cyberpunk_2077", "Black Clover": "black_clover",
 "Aladdin": ("aladdin_(1992_disney_film)", "aladdin (tag ambigu : film + personnage)"), "Darling in the Franxx": "darling_in_the_franxx", "Beastars": "beastars",
 "The Quintessential Quintuplets": "go-toubun_no_hanayome", "Brawl Stars": "brawl_stars", "Bocchi the Rock!": "bocchi_the_rock!", "Luz à Osville (The Owl House)": "the_owl_house"}
UNIONS = {"Avatar (Le Dernier Maître de l'air + La Légende de Korra)": ("avatar_the_last_airbender ~ the_legend_of_korra ~ avatar_legends", 61068 + 21),
          "Fatal Fury / King of Fighters": ("king_of_fighters ~ fatal_fury", 53970 + 21)}
fr = [r['franchise'] for r in csv.DictReader(open('../classement_franchises_tous_personnages_2026-10-24.csv', encoding='utf-8-sig'))]
assert set(fr) == set(T) | set(UNIONS), (set(fr) - set(T) - set(UNIONS), set(T) | set(UNIONS) - set(fr))
rows = []
for f in fr:
    if f in UNIONS:
        q, n = UNIONS[f]; rows.append(dict(site='rule34', franchise=f, tag=q, publications=n, methode='union OR mesurée (dernière page + 21)', autres_tags=''))
        continue
    v = T[f]; tag, alt = (v, '') if isinstance(v, str) else v
    def lab(a):
        t = a.split(' (')[0]; return f"{a} : {C[t]}" if t in C and t == a else (f"{t} : {C[t]} ({a.split(' (', 1)[1]}" if t in C else a)
    rows.append(dict(site='rule34', franchise=f, tag=tag, publications=C[tag], methode='autocomplétion (tag principal)', autres_tags=lab(alt) if alt else ''))
D = json.load(open('danbooru_tags_franchise_2026-10-24.json', encoding='utf-8'))
for r in csv.DictReader(open('../classement_franchises_danbooru_256_2026-10-24.csv', encoding='utf-8-sig')): pass
sel = {}
for r in csv.DictReader(open('../danbooru/selection_256_personnages_feminins_danbooru_2026-10-24.csv', encoding='utf-8-sig')):
    if r['retenu'] == 'oui': sel[r['franchise']] = r['franchise_tag']
for f, t in sel.items():
    rows.append(dict(site='danbooru', franchise=f, tag=t, publications=D[t][0], methode='API tags.json (post_count)', autres_tags=''))
with open('tags_franchise_2026-10-24.csv', 'w', encoding='utf-8-sig', newline='') as fo:
    w = csv.DictWriter(fo, list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), sum(r['site'] == 'rule34' for r in rows), sum(r['site'] == 'danbooru' for r in rows))
for r in sorted(rows, key=lambda r: -r['publications'])[:15]: print(r['site'], r['franchise'], r['tag'], r['publications'])
