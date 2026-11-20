# App « Top 100 TierMaker + publications Rule34 » (24 oct. 2026).
# Usage : python3 build.py  (vignettes lues dans /tmp/tmall et /tmp/tm4 ; à re-télécharger si /tmp a été vidé)
import gzip, csv, json, sys, os, io, base64
from PIL import Image
B = '/home/user/outil_tags_r34/'
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B + 'tiermaker_87784832'); sys.path.insert(0, B + 'tiermaker_cartoons_vs_r34')
import tm_top100 as T
import identifications as I
from r34_top import liste
os.chdir(B + 'tiermaker_87784832'); L = liste(); os.chdir(H)
GEN = {x['tag']: x for x in L}
V5 = {r['tag']: r['medium'] for r in csv.DictReader(open(B + 'classement_par_medium/classement_r34_par_medium_v12_2026-10-25.csv', encoding='utf-8-sig'))}
CART = "Cartoons / films d'animation occidentaux"
COURT = {"Comics": "Comics", CART: "Cartoons", "Furry": "Furry", "Animanga": "Animanga", "Jeux vidéo": "Jeux vidéo", "Hors des 4 médiums": "Autre"}
SPECIES = {"gardevoir", "renamon", "lopunny", "vaporeon", "glaceon"}
FR_MED = {"Marvel": "Comics", "DC": "Comics", "Kim Possible": "Cartoons", "La Route d'Eldorado": "Cartoons", "Hôtel Transylvanie": "Cartoons",
          "Les Indestructibles": "Cartoons", "Les Nouveaux Héros": "Cartoons", "Total Drama": "Cartoons", "Lilo & Stitch": "Cartoons",
          "Cyberpunk: Edgerunners": "Animanga", "Vocaloid": "Autre"}
JEUX_FR = {"Zenless Zone Zero", "Nikke", "Genshin Impact", "NieR:Automata", "NieR", "Fatal Fury / KOF", "Resident Evil", "Azur Lane", "Final Fantasy VII",
           "Street Fighter", "Blue Archive", "Pokémon", "Honkai: Star Rail", "Overwatch", "Bayonetta", "Metroid", "Stellar Blade", "Persona 3",
           "Fire Emblem", "Wuthering Waves", "Halo", "Dispatch"}

def medium(tag, franchise=None):
    if tag in V5: return COURT[V5[tag]]
    if tag in SPECIES: return "Furry"
    if franchise is not None:
        if franchise in FR_MED: return FR_MED[franchise]
        if franchise in JEUX_FR: return "Jeux vidéo"
        return "Animanga"
    if tag in I.JEUX: return "Jeux vidéo"
    if tag in getattr(I, "ANIME", ()): return "Animanga"
    if tag in I.COMICS: return "Comics"
    if tag in I.FURRY: return "Furry"
    return "Cartoons"

PERIM = {"Comics", "Cartoons", "Furry"}
P = [x for x in L if medium(x['tag']) in PERIM]
RP = {x['tag']: i for i, x in enumerate(P, 1)}

# repli : vignettes déjà intégrées dans l'app précédente (extraites dans /tmp/vcache.json) si /tmp/tmall et /tmp/tm4 ont été vidés
try: VCACHE = json.load(open('/tmp/vcache.json'))
except Exception: VCACHE = {}
def vignette(path):
    try:
        im = Image.open(path).convert('RGB')
    except Exception:
        q = path.split('/'); k = int(q[-1].split('.')[0])
        return VCACHE.get(('87784832' if q[2] == 'tmall' else q[3]) + ':' + str(k), '')
    im.thumbnail((72, 72)); b = io.BytesIO(); im.save(b, 'JPEG', quality=68)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def classement(path):
    return {int(r['rang_average']): r for r in csv.DictReader(open(path, encoding='utf-8-sig'))}


def charger_json(p):
    # les fichiers live_event des votes ajoutés le 24 oct. (suite) sont compressés (.json.gz) pour la place
    import os
    return json.load(gzip.open(p + '.gz', 'rt')) if not os.path.exists(p) and os.path.exists(p + '.gz') else json.load(open(p))

def ev_info(path):
    d = charger_json(path)
    return dict(participants=d.get('participantsCount'), votes=d.get('totalVotesCount'), debut=(d.get('startAt') or d.get('createdAt') or '')[:10], fin=(d.get('endAt') or '')[:10], titre=d['title'])

LISTES = []
# --- 87784832 ---
cl = classement(B + 'tiermaker_87784832/classement_average_avec_incertitude.csv')
info = ev_info(B + 'tiermaker/live_event_87784832_2026-10-23.json')
rows = []
for k in range(1, 101):
    nom, fr, tag = T.TM[k]; c = cl[k]
    if tag in GEN: n, src = GEN[tag]['n'], 'sel'
    else: n, src = T.HORS[tag], 'ac'
    notes = []
    v = T.VARIANTES.get(tag)
    if v and v != '—': notes.append('variantes non fusionnées : ' + v)
    rows.append(dict(tm=k, nom=nom, univers=fr, medium=medium(tag, fr), votants=int(c['votants']), moyenne=float(c['moyenne']), tag=tag, n=n, src=src,
                     rg=GEN[tag]['rang'] if tag in GEN else None, rp=RP.get(tag), notes='; '.join(notes), extra=False, img=vignette('/tmp/tmall/%04d.jpg' % k)))
LISTES.append(dict(id='87784832', modele='Ultimate Fictional Animated Women (1 310 images)', **info, rows=rows,
                   remarque="Images portant le nom écrit : identification par lecture des étiquettes. Beaucoup d'images de la 2e vague ont moins de 300 votants."))
# --- 4 votes dessins animés ---
MOD = {"5058287": "Definitive Cartoon Waifu Tier List (601 images)", "8447367": "Cartoon Girls (229 images)",
       "88691896": "Hottest Female Cartoon Characters (200 images)", "91860172": "Hottest Animated Women Crushes Ranked (214 images)",
       "81614596": "Some of Disney/Pixar's hottest women (150 images)", "30083716": "Female Cartoon Characters (1 087 images)",
       "20899730": "Penultimate Female Cartoon Character Tierlist (324 images)",
       "80408816": "Waifus Anime, Cartoon and Videogames (381 images, tous médiums)",
       "30081640": "The Anime Waifu Tier List (2 050 images, anime/manga)",
       "436045": "Cartoon Hotties (295 images, vote encore ouvert)",
       "73568440": "Most Popular Female Video Game Characters (617 images, jeux vidéo)",
       "99761754": "Best Anime Waifus 2025 (311 images, anime)"}
REM = {"81614596": " Paliers S, A, B, C, D + Hard Pass : Hard Pass = note la plus basse, moyenne sur 6.",
       "20899730": " Paliers S, A, B, C, D + Ewwwwww + Who? : Ewwwwww = note la plus basse, moyenne sur 6 ; votes « Who? » retirés.",
       "80408816": " Modèle tous médiums (anime, cartoons, jeux vidéo). Au-delà du rang 130, seules les images du périmètre Comics + Cartoons + Furry ont été rattachées à un tag (affichées en mode périmètre).",
       "30081640": " Modèle anime/manga (quelques personnages de jeux vidéo : 2B, A2, Tifa, Aerith, Bayonetta...). Aucun personnage du périmètre Comics + Cartoons + Furry : mode périmètre sans objet. Attention : 3 530 participants pour 2 050 images, donc peu de votants par image (18 à 1 094 dans le top 100, moins de 100 pour 46 images) ; les moyennes sur peu de votants sont fragiles.",
       "436045": " Vote encore ouvert : chiffres du relevé du 24 oct. 2026 (7 894 participants, 441 695 votes), ils bougeront. La date affichée est la création de l'événement (21/10/2025). Malgré le titre « Cartoon Hotties », le modèle contient beaucoup d'anime (36 du top 100 : One Piece, Naruto, My Hero Academia, Evangelion, Demon Slayer...). Au-delà du rang 100, seules les images du périmètre Comics + Cartoons + Furry ont été rattachées (jusqu'au rang 175). Image n° 18 = Makio, Suma et Hinatsuru ensemble (Demon Slayer) : pas de tag unique. Image n° 89 = Gwen Stacy version Spectacular Spider-Man : le tag gwen_stacy regroupe toutes les versions. Images n° 74 (Ellen Yin), 107 (Wilhamena) et 116 (Cleopatra de Clone High, sans tag dédié) : identification par nom de fichier, à confirmer.",
       "73568440": " Modèle jeux vidéo à 7 paliers (I love you, Ma gurl, AMAZING, Good, Mid, Ew, GET OUT ; notés de 7 à 1, moyenne sur 7). Attention : 4 126 participants pour 617 images, 113 à 1 624 votants par image (médiane 204) ; le nombre de votants baisse fortement avec la position de l'image dans le modèle (corrélation -0,94), les premières images ont été vues par bien plus de monde. Les personnages de comics présents dans des jeux (Black Cat, Femme invisible, Psylocke, Catwoman, Emma Frost, Magik…) restent rangés en Comics, Harley Quinn en Cartoons, et les personnages animaliers (Amy Rose, Toriel, Ankha…) en Furry, selon les règles du classement par médium ; Luna Snow, créée pour un jeu, reste en Jeux vidéo. Au-delà du rang 100, seules les images du périmètre ont été rattachées (24 images en tout, repérées sur les 617). Image n° 443 = Blanche-Neige de The Wolf Among Us, personnage des comics Fables : pas de tag rule34 dédié.",
       "99761754": " Modèle 100 % anime : aucun personnage du périmètre Comics + Cartoons + Furry, mode périmètre sans objet. L'événement était réglé en « Most Votes » ; comme pour les autres votes, il est relu ici en moyenne (Average Vote) à partir des votes par palier. 19 274 participants, 1 253 à 6 382 votants par image (médiane 1 813). Images sans nom écrit (noms de fichier = codes) : 67 images du top 100 identifiées visuellement, 33 laissées « non identifiées » faute de certitude ; Yunyun (47) et Maki Oze (57) sont à confirmer ; n° 9 = Nico Robin (corrigé par l'utilisateur, d'abord prise pour Boa Hancock).",
       "30083716": " Beaucoup d'images en double dans ce modèle : les doublons ont souvent moins de 100 votants."}
for e, d in I.EV.items():
    cl = classement(B + f'tiermaker_{e}/classement_average_avec_incertitude.csv')
    info = ev_info(B + f'tiermaker_{e}/live_event_{e}.json')
    rows = []; vus = set(); horsp = 0
    for k in sorted(d):
        t = d[k]; c = cl[k]
        extra = k > 100
        if t:
            if t in GEN: n, src = GEN[t]['n'], 'sel'
            else: n, src = I.HORS[t], 'ac'
            notes = []
            if (e, k) in I.INCERTAIN: notes.append('identification incertaine')
            if t in I.AMBIGU: notes.append('tag générique (peut mêler plusieurs personnages)')
            if t in vus: notes.append('2e image du même personnage')
            if t in getattr(I, "VARIANTES_EV", {}): notes.append("variantes non fusionnées : " + I.VARIANTES_EV[t])
            if t.endswith('_(mlp)'): notes.append('version Equestria Girls, comptée avec le tag du poney')
            vus.add(t)
            m = medium(t)
            rows.append(dict(tm=k, nom=I.NOMS[t], univers='', medium=m, votants=int(c['votants']), moyenne=float(c['moyenne']), tag=t, n=n, src=src,
                             rg=GEN[t]['rang'] if t in GEN else None, rp=RP.get(t), notes='; '.join(notes), extra=extra,
                             img=vignette(f'/tmp/tm4/{e}/{k:04d}.jpg')))
        elif (e, k) in getattr(I, 'SANS_TAG', {}):
            enf = (e, k) in getattr(I, 'SANS_R34_ENFANT', set())
            rows.append(dict(tm=k, nom=I.SANS_TAG[(e, k)], univers='', medium='Animanga' if e in getattr(I, 'ANIME_SEUL', set()) else getattr(I, 'SANS_TAG_MEDIUM', {}).get((e, k), 'Cartoons'), votants=int(c['votants']), moyenne=float(c['moyenne']), tag='', n=None, src='',
                             rg=None, rp=None, notes='personnage enfant : aucun compte Rule34 relevé' if enf else 'pas de tag rule34 dédié', extra=extra, img=vignette(f'/tmp/tm4/{e}/{k:04d}.jpg')))
        else:
            rows.append(dict(tm=k, nom='non identifiée', univers='', medium='', votants=int(c['votants']), moyenne=float(c['moyenne']), tag='', n=None, src='',
                             rg=None, rp=None, notes='', extra=extra, img=vignette(f'/tmp/tm4/{e}/{k:04d}.jpg')))
    LISTES.append(dict(id=e, modele=MOD[e], **info, rows=rows, perimetre=e not in getattr(I, 'ANIME_SEUL', set()),
                       remarque=(("Images portant le nom écrit : identification par lecture des étiquettes (OCR vérifié sur planches)." if e == "80408816" else "Identification par le nom de fichier et l'étiquette « personnage / série » écrite sur l'image, vérifiées sur planches." if e in ("30081640", "73568440") else "Identification par le nom de fichier de l'image, vérifiée sur planches ; cas douteux signalés." if e in ("81614596", "20899730", "436045") else "Images sans nom écrit : identification visuelle, cas douteux signalés ; « non identifiée » = pas reconnue avec assez de certitude.") + REM.get(e, ""))))

# statistiques de chaque vote sur TOUTES les images (pour l'écart à la moyenne du vote, page Analyse)
import statistics
for l in LISTES:
    ms = [float(r['moyenne']) for r in csv.DictReader(open(B + f"tiermaker_{l['id']}/classement_average_avec_incertitude.csv", encoding='utf-8-sig'))]
    l['stats'] = dict(nimg=len(ms), moy=round(statistics.mean(ms), 4), et=round(statistics.pstdev(ms), 4))
# autres sites (relevé du 23 oct. 2026, 195 personnages les plus publiés sur Rule34)
SITES = {}
for r in csv.DictReader(open(B + 'comparaison_sites_195_personnages_2026-10-23.csv', encoding='utf-8-sig')):
    f = lambda k: int(r[k]) if r[k] not in ('', None) else None
    SITES[r['tag_r34']] = dict(danbooru=f('danbooru'), e621=f('e621'), xbooru=f('xbooru'))
DATA = dict(listes=LISTES, sites=SITES, perim=[dict(r=RP[x['tag']], nom=x['nom'], tag=x['tag'], n=x['n'], medium=medium(x['tag'])) for x in P],
            seuil=7228, date='24 octobre 2026')
html = open(H + '/template.html', encoding='utf-8').read().replace('/*DATA*/null', json.dumps(DATA, ensure_ascii=False))
open(H + '/top100_tiermaker_rule34.html', 'w', encoding='utf-8').write(html)
print('ok', [(l['id'], len(l['rows'])) for l in LISTES], round(len(html) / 1e6, 2), 'Mo')
