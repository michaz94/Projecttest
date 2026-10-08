#!/usr/bin/env python3
"""Tests de cohérence de fiches_references_projet.yaml et de sa vue MD.

Usage (depuis le dossier qui contient le YAML, la vue et generer_vue_md.py) :
    python3 tester_fiches.py
Code de sortie 0 si tout passe, 1 sinon. Ne modifie aucun fichier.
"""
import os
import re
import subprocess
import sys
import tempfile
import shutil
import yaml

YAML = "fiches_references_projet.yaml"
VUE = "VUE_references_projet.md"
GEN = "generer_vue_md.py"

OK = []
KO = []


def check(nom, cond, detail=""):
    (OK if cond else KO).append(nom + (f" : {detail}" if detail and not cond else ""))


d = yaml.safe_load(open(YAML, encoding="utf-8"))
p, refs = d["projet"], d["references"]

# 1. Structure ----------------------------------------------------------
noms = [r["reference"] for r in refs]
check("noms de fiches uniques", len(noms) == len(set(noms)), str([n for n in noms if noms.count(n) > 1]))
for r in refs:
    check(f"champs de base présents : {r['reference']}", all(k in r for k in ("statut_relation", "source", "statut", "statut_decision")))

# 2. Valeurs autorisées -------------------------------------------------
REL = {"", "influence", "reference", "influence+reference", "reference_de_comparaison",
       "source_documentaire", "famille_de_conventions", "corpus_de_traditions"}
DEC = {"", "non_precise", "interet", "envisage", "decide"}
SRC = {"U", "depot", "IA"}
EMP = {"", "emprunt", "ecart_delibere", "hommage_ponctuel", "distance_a_maintenir", "confirmation"}
GIM = {"", "identite", "discipline", "statut_institutionnel", "mixte"}
CONF = {"", "verifie_web", "memoire_IA"}
for r in refs:
    n = r["reference"]
    check(f"statut_relation valide : {n}", r.get("statut_relation", "") in REL, r.get("statut_relation"))
    check(f"statut_decision valide : {n}", r.get("statut_decision", "") in DEC, r.get("statut_decision"))
    check(f"source valide : {n}", r.get("source") in SRC, r.get("source"))
    check(f"emprunt_ou_ecart valide : {n}", r.get("emprunt_ou_ecart", "") in EMP, r.get("emprunt_ou_ecart"))
    check(f"type_de_gimmick valide : {n}", r.get("type_de_gimmick", "") in GIM, r.get("type_de_gimmick"))
    check(f"gimmick_confiance valide : {n}", r.get("gimmick_confiance", "") in CONF, r.get("gimmick_confiance"))
    for x in r.get("emprunts_ou_ecarts_par_aspect", []):
        check(f"valeur par aspect valide : {n} / {x.get('aspect')}", x.get("valeur") in EMP, x.get("valeur"))
for h in p["systeme_de_pouvoirs"]["hypotheses"]:
    check("hypothèse : statut valide", h["statut"] in {"a_reexaminer", "validee", "refutee"}, h["statut"])
for k in ("decide", "envisage"):
    check(f"folklore.{k} est une liste", isinstance(p["folklore"][k], list))
for x in p["inspirations_visuelles_non_decidees"]:
    check(f"inspiration visuelle : statut valide ({x['element'][:30]})", x["statut_decision"] in DEC)
for v in p["esthetique_vestimentaire"]["references_visuelles"]:
    check(f"image : statut valide ({v['image'][:30]})", v["statut_decision"] in DEC)
    check(f"image : aucun nom de fichier ({v['image'][:30]})", not re.search(r"\.(png|jpe?g|webp)\b", yaml.safe_dump(v, allow_unicode=True)))

# 3. Décisions connues --------------------------------------------------
check("Edenia : nom provisoire + source U", p["nom_provisoire"] == "Edenia" and p.get("source_nom_provisoire") == "U")
check("plafond technologique 1950 théorique, hors magie", any("1950" in c and "théorique" in c and "magique" in c for c in p["cadre_valide"]))
check("plus aucune trace du plafond 1930 dans le cadre", not any("1930" in c for c in p["cadre_valide"]))
bs = [r for r in refs if r["reference"] == "BioShock Infinite"][0]
check("BioShock : contrainte 1950", "1950" in bs["contrainte_liee"] and "1930" not in bs["contrainte_liee"])
check("BioShock : zone industrielle décidée", bs["statut_decision"] == "decide")
check("technologie magique non tranchée", any("technologie magique" in s for s in p["non_tranche"]))
check("Body, Mind and Soul : sans précision négative", "Body, Mind and Soul" in p["non_tranche"] and "trois branches" not in yaml.safe_dump(d, allow_unicode=True))
check("Harry Potter scindé en films / livres", {"Harry Potter (films)", "Harry Potter (livres)"} <= set(noms) and "Harry Potter" not in noms)
hpf = [r for r in refs if r["reference"] == "Harry Potter (films)"][0]
check("HP films : envisagé", hpf["statut_decision"] == "envisage")
rad = [r for r in refs if r["reference"].startswith("Radiant")][0]
check("Radiant : reference (pas influence)", rad["statut_relation"] == "reference")
rh = [r for r in refs if "Red Hood" in r["reference"]][0]
check("Red Hood : influence+reference", rh["statut_relation"] == "influence+reference")
fma = [r for r in refs if r["reference"] == "Fullmetal Alchemist"][0]
check("FMA : pas d'écart déclaré sur le ton", not any(x["aspect"] == "ton" for x in fma["emprunts_ou_ecarts_par_aspect"]))
check("FMA : cadre militaire = distance_a_maintenir", any(x["aspect"] == "cadre militaire" and x["valeur"] == "distance_a_maintenir" for x in fma["emprunts_ou_ecarts_par_aspect"]))
pers = {c["nom"]: c for c in p["personnages_edenia"]}
check("3 personnages d'Edenia", set(pers) == {"Cosmo Dumas", "Brann Pandragon", "Harley Delphine"})
check("Perceval le Gallois présent", "Perceval le Gallois" in pers["Brann Pandragon"]["inspire_de"])
check("Fabula Fantasia : fiche + lien Radiant", any(r["reference"].startswith("Fabula Fantasia") and "Radiant" in r.get("lien_avec", "") for r in refs))
al = p["ambiance_des_lieux"]
check("ambiance des lieux : envisagé", al["statut_decision"] == "envisage")
check("ambiance des lieux : procédés = source IA", all(x["source"] == "IA" for x in al["procedes_visuels"]))
check("ambiance des lieux : aucun nom de fichier", not re.search(r"\.(png|jpe?g|webp)\b|shr00|n252E0Z", yaml.safe_dump(al, allow_unicode=True)))
check("« univers vaste » non reporté (abandonné par U)", "univers vaste" not in yaml.safe_dump(d, allow_unicode=True).lower())
check("occultisme non tranché", p["occultisme"]["statut_decision"] == "")
check("couleur / rouge non reportés (demande de l'utilisateur)", "rouge" not in yaml.safe_dump(d, allow_unicode=True).lower().replace("rouge »", "").replace("petit homme rouge", ""), "mot « rouge » trouvé")

# 4. Limites anti-spoil -------------------------------------------------
LIM = {
    "Radiant (manga)": "tome 6",
    "Worm (Wildbow)": "arc 9",
    "Jujutsu Kaisen (anime)": "59",
    "One Piece": "97",
    "Yu Yu Hakusho": "129",
}
for n, motif in LIM.items():
    r = [x for x in refs if x["reference"] == n][0]
    check(f"limite de lecture présente : {n}", motif in r.get("limite_lecture", ""), r.get("limite_lecture"))
for r in refs:
    if any(k in r["reference"] for k in ("Stormlight", "Kingkiller", "Horde", "Game of Thrones", "Seigneur des Anneaux")):
        check(f"limite de lecture renseignée : {r['reference']}", bool(r.get("limite_lecture")))
brut = open(YAML, encoding="utf-8").read() + open(VUE, encoding="utf-8").read()
for motif, nom in [(r"\btomes? (7|8|9|10|11|12)\b", "Radiant tomes 7+"), (r"\barc 1[0-9]\b", "Worm arc 10+"),
                   (r"\bS8\b|saison 8", "GoT S8")]:
    trouves = re.findall(motif, brut, flags=re.I)
    check(f"aucune mention interdite : {nom}", not trouves, str(trouves))
check("Radiant : aucun contenu d'intrigue des tomes 7+ (limite écrite)", "rien au-delà" in rad["limite_lecture"])
fab = [r for r in refs if r["reference"].startswith("Fabula")][0]
check("Fabula Fantasia : risque de spoil Radiant signalé", "tome 6" in fab.get("risque", ""))

# 5. Folklore vs fiche créatures (si le fichier est là) ------------------
FICHE = os.path.join("uploads", "Fiche_creatures_et_figures_folkloriques_statuts.md")
if os.path.exists(FICHE):
    md = open(FICHE, encoding="utf-8").read()
    f = p["folklore"]
    crea = f["interet"]["creatures_de_la_carte"]
    check("24 créatures en intérêt", len(crea) == 24, str(len(crea)))
    for n in crea + [e for e in f["envisage"]]:
        base = n.split("/")[0].split(" (")[0]
        base = re.sub(r"^(Le|La|Les) ", "", base)
        check(f"présent dans la fiche créatures : {n}", base.lower() in md.lower() or n.split("/")[-1].lower() in md.lower())
    check("décidé = Agrippa ; Barbegazi envisagé", [x.split(" (")[0] for x in f["decide"]] == ["Agrippa"] and "Barbegazi" in f["envisage"])
else:
    OK.append("(fiche créatures absente : section 5 ignorée)")

# 6. Vue MD à jour + génération depuis un dossier vierge ------------------
r = subprocess.run([sys.executable, GEN, "--verifier"], capture_output=True, text=True)
check("vue MD à jour (--verifier)", r.returncode == 0, r.stderr.strip())
vue = open(VUE, encoding="utf-8").read()
for n in noms:
    check(f"fiche dans la vue : {n}", f"### {n}" in vue)
for n in p["folklore"]["decide"] + p["folklore"]["envisage"]:
    check(f"folklore dans la vue : {n}", n in vue)
tmp = tempfile.mkdtemp()
try:
    shutil.copy(YAML, tmp)
    shutil.copy(GEN, tmp)
    g = subprocess.run([sys.executable, GEN], cwd=tmp, capture_output=True, text=True)
    check("génération dans un dossier vierge", g.returncode == 0, g.stderr.strip())
    check("vue générée identique à la vue du dépôt", open(os.path.join(tmp, VUE), encoding="utf-8").read() == vue)
    # la vérification doit détecter une modification manuelle
    with open(os.path.join(tmp, VUE), "a", encoding="utf-8") as fh:
        fh.write("\nmodification manuelle\n")
    v = subprocess.run([sys.executable, GEN, "--verifier"], cwd=tmp, capture_output=True, text=True)
    check("--verifier détecte une modification manuelle", v.returncode != 0)
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# 7. Fichier de décisions : chiffres cités -------------------------------
DEC_MD = "DECISIONS_RECENTES_2026-10-07.md"
if os.path.exists(DEC_MD):
    dm = open(DEC_MD, encoding="utf-8").read()
    for m in re.finditer(r"(\d+) fiches", dm):
        check(f"nombre de fiches cité dans {DEC_MD} ({m.group(0)})", int(m.group(1)) == len(refs), f"réel : {len(refs)}")

print(f"\n{len(OK)} contrôles réussis, {len(KO)} échecs.")
for k in KO:
    print("ÉCHEC :", k)
sys.exit(1 if KO else 0)
