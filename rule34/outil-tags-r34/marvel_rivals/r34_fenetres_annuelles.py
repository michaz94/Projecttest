# -*- coding: utf-8 -*-
"""Rule34.xxx : posts par fenêtre annuelle, reconstruits à partir des ID (chronologiques).
Relevé manuel 24/10/2026 via index.php?page=post&s=list&tags=<tag>+id:<B (42 posts/page).
Valeur relevée = pid de la dernière page ("»") ; effectif réel = pid + 1..42 -> on prend pid+21 (±21).
Psylocke : avant le jeu, le tag principal était psylocke_(kwannon) ; tag nu psylocke = ~105 posts avant le 06/12/2024
(63 / 105 / 4305 / 7497 aux 4 bornes) -> on utilise l'union OR des deux tags (syntaxe r34 "( a ~ b )")."""
import csv
# Bornes ID <-> date (voir README des ancres)
BORNES = {"2023-12-06": 9_122_000, "2024-12-06": 11_927_000, "2025-12-06": 15_730_000,
          "2026-07-10": 18_057_000, "2026-10-24": 19_130_000}
# dernier pid relevé : (<9.122M, <11.927M, <15.73M, total)   None = page unique (<42 posts)
PID = {
 "emma_frost":              (3108, 4620, 13944, 19992),
 "magik_(illyana_rasputin)":( 504,  630,  3150,  5586),
 "luna_snow":               (None, None,  3360,  5460),
 "invisible_woman":         (1092, 1218,  7518, 10710),
 "jubilee":                 ( 756,  924,  1134,  2940),
 "psylocke ∪ psylocke_(kwannon)": (1512, 1890, 6762, 9954),  # requête ( psylocke ~ psylocke_(kwannon) )
 "spider-gwen (témoin)":    (6300, 9534, 12726, 15414),
}
JUB_18057 = 1302  # jubilee id:<18057000 (sortie de Jubilee dans le jeu, 10/07/2026)
LUNA_PETIT = (30, 40)  # 1 seule page : ~30 posts <9.0M (relevé antérieur), <42 avant 11.927M
def n(p, petit): return petit if p is None else p + 21
ids = {"W3": (11_927_000-9_122_000)/1e6, "W4": (15_730_000-11_927_000)/1e6, "W5": (19_130_000-15_730_000)/1e6}
rows=[]
for tag,(a,b,c,t) in PID.items():
    pa = n(a, LUNA_PETIT[0]); pb = n(b, LUNA_PETIT[1]); pc = n(c,0); pt = n(t,0)
    w3, w4, w5 = pb-pa, pc-pb, pt-pc
    r3, r4, r5 = w3/ids["W3"], w4/ids["W4"], w5/ids["W5"]
    rows.append({"tag":tag, "avant_dec2023":pa, "dec23_dec24":w3, "dec24_dec25":w4, "dec25_24oct26":w5, "total":pt,
                 "par_M_ID_W3":round(r3), "par_M_ID_W4":round(r4), "par_M_ID_W5":round(r5),
                 "mult_W4_vs_W3":round(r4/r3,1) if r3 else "", "mult_W5_vs_W3":round(r5/r3,1) if r3 else "",
                 "part_postee_apres_lancement_6dec24_%":round(100*(pt-pb)/pt)})
with open("r34_fenetres_annuelles_2026-10-24.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
j_av = (JUB_18057+21)-(1134+21); j_ap = (2940+21)-(JUB_18057+21)
print("Jubilee déc25->10 juil:", j_av, round(j_av/((18_057_000-15_730_000)/1e6)),"/M ;  10 juil->24 oct:", j_ap, round(j_ap/((19_130_000-18_057_000)/1e6)),"/M")
