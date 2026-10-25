# Relevé DeviantArt (25/10/2026) : comptes par tag pour le top 15 féminin rule34 sans IA.
# Compte = recherche dichotomique sur l'offset de /browse/tags (mature_content=true), ± ~100, plafond 50 000.
import json, sys, os
sys.argv = ['x']; sys.path.insert(0, os.path.dirname(__file__))
import da_compte as D
V = {'Rouge the Bat': ['rougethebat', 'rouge_the_bat'],
     'Tifa Lockhart': ['tifalockhart', 'tifa_lockhart', 'tifa'],
     'Amy Rose': ['amyrose', 'amy_rose', 'amyrosethehedgehog'],
     'Princesse Peach': ['princesspeach', 'princess_peach'],
     'Loona': ['loonahelluvaboss', 'loona_helluvaboss'],
     'Chun-Li': ['chunli', 'chun_li', 'chunlistreetfighter'],
     '2B': ['2b', 'yorha2b', '2bnierautomata'],
     'Twilight Sparkle': ['twilightsparkle', 'twilight_sparkle'],
     'Hatsune Miku': ['hatsunemiku', 'hatsune_miku'],
     'Nami': ['namionepiece', 'nami'],
     'Lara Croft': ['laracroft', 'lara_croft'],
     'Raven': ['raventeentitans', 'ravendc', 'raven'],
     'Samus Aran': ['samusaran', 'samus_aran', 'samus'],
     'Princesse Zelda': ['princesszelda', 'princess_zelda', 'zelda'],
     'D.Va': ['dva', 'dvaoverwatch', 'dva_overwatch']}
OUT = os.path.join(os.path.dirname(__file__), 'brut_top15_tags_2026-10-25.json')
R = json.load(open(OUT)) if os.path.exists(OUT) else {}
for n in V:
    for t in V[n]:
        k = n + '|' + t
        if k in R: continue
        R[k] = D.compte(t, True); print(n, t, R[k], flush=True)
        json.dump(R, open(OUT, 'w'), ensure_ascii=False, indent=0)
