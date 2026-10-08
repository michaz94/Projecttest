#!/usr/bin/env python3
"""Génère la vue Markdown lisible à partir de fiches_references_projet.yaml.

SENS UNIQUE : YAML -> MD. Le YAML est la source unique des statuts.
Ne jamais modifier la vue MD à la main : elle serait écrasée.

Usage :
    python3 generer_vue_md.py              # écrit VUE_references_projet.md
    python3 generer_vue_md.py --verifier   # échoue si la vue MD n'est pas à jour
Chemins par défaut : le YAML et la vue sont dans le dossier courant (ou passer
--yaml et --md).
"""
import argparse
import sys
import yaml

ETIQUETTES = [
    ("type_de_noeud", "Nature"), ("aspect_vise", "Aspect visé"),
    ("options_a_trancher", "Options à trancher"), ("niveau_de_detail", "Niveau de détail"),
    ("emprunt_ou_ecart", "Emprunt ou écart"), ("elements_confirmes", "Éléments qui ont confirmé mes choix"),
    ("elements_a_eviter", "Éléments à éviter"), ("distance_voulue", "Distance voulue"),
    ("elements_a_ne_pas_rapprocher", "Éléments à ne pas rapprocher"),
    ("trace_attendue_dans_le_texte", "Trace attendue dans le texte"), ("risque", "Risque"),
    ("contrainte_liee", "Contrainte liée"), ("role", "Rôle"),
    ("emprunts_ou_ecarts_par_aspect", "Emprunts ou écarts par aspect"), ("inventaire_non_fige", "Inventaire non figé"),
    ("limite_lecture", "Limite de lecture"), ("gimmick", "Gimmick"),
    ("type_de_gimmick", "Type de gimmick"), ("gimmick_detail", "Détail du gimmick"),
    ("gimmick_confiance", "Fiabilité du gimmick"), ("lien_avec", "Lié à"), ("oeuvres_liees", "Œuvres liées"), ("note", "Note"),
    ("note_utilisateur", "Note de l'utilisateur"), ("statut", "Statut (texte libre)"),
]
SOURCES = {"U": "utilisateur", "depot": "dépôt", "IA": "IA (à valider)"}
DECISIONS = {"": "—", "non_precise": "non précisé", "interet": "intérêt",
             "envisage": "envisagé", "decide": "décidé"}


def vide(v):
    return v in ("", None, [], {})


def fmt(v):
    if isinstance(v, list):
        return " ; ".join(str(x) for x in v)
    if isinstance(v, dict):
        return " ; ".join(f"{k} : {fmt(x)}" for k, x in v.items())
    return str(v)


def cell(v):
    return fmt(v).replace("|", "\\|").replace("\n", " ") if not vide(v) else "—"


def vue(d):
    p, refs = d["projet"], d["references"]
    o = []
    a = o.append
    a("# Vue des fiches de références (générée)\n")
    a("> **Fichier généré automatiquement** par `generer_vue_md.py` à partir de `fiches_references_projet.yaml`.")
    a("> **Ne pas modifier à la main** : toute modification ici sera écrasée. Pour changer un statut, modifier le YAML puis régénérer.")
    a("> Règle : « — » = non tranché (champ vide dans le YAML). Rien n'est inventé.\n")

    a(f"## 1. Projet : {p.get('nom_provisoire','')} (nom provisoire)\n")
    src = f" (source : {p['source_nom_provisoire']})" if p.get("source_nom_provisoire") else ""
    a(f"**Nom provisoire :** {p.get('nom_provisoire','')}{src}\n")
    a(f"**Genre :** {p.get('genre','')}\n")
    a("**Cadre validé (décisions du 3 oct. 2026, plafond technologique modifié le 7 oct.) :**\n")
    for c in p.get("cadre_valide", []):
        a(f"- {c}")
    a("")
    a("**Gimmick d'Edenia :** " + (cell(p.get("gimmick_edenia")) if not vide(p.get("gimmick_edenia")) else "non tranché")
      + " (type : " + (cell(p.get("type_gimmick_edenia")) if not vide(p.get("type_gimmick_edenia")) else "non tranché") + ")\n")

    a("### Gimmicks des grands succès (liste de l'utilisateur ; type proposé par l'IA)\n")
    a("| Gimmick | Œuvre | Type |\n|---|---|---|")
    for g in p.get("gimmicks_des_grands_succes", []):
        a(f"| {cell(g.get('gimmick'))} | {cell(g.get('oeuvre'))} | {cell(g.get('type_de_gimmick'))} |")
    a("")

    a("### Personnages d'Edenia (noms et inspirations seulement)\n")
    a("| Personnage | Inspiré de | Tenue (inspiration) |\n|---|---|---|")
    for c in p.get("personnages_edenia", []):
        a(f"| {cell(c.get('nom'))} | {cell(c.get('inspire_de'))} | {cell(c.get('tenue_inspiration'))} |")
    a("")

    f = p.get("folklore", {})
    a("### Folklore : statuts sur l'échelle décisionnelle\n")
    a(f"- **Décidé :** {cell(f.get('decide'))}")
    a(f"- **Envisagé :** {cell(f.get('envisage'))}")
    it = f.get("interet", {})
    if isinstance(it, dict):
        a(f"- **Intérêt (créatures de la carte) :** {cell(it.get('creatures_de_la_carte'))}")
        a(f"- **Intérêt (autres) :** {cell(it.get('autres'))}")
    else:
        a(f"- **Intérêt :** {cell(it)}")
    a(f"- **Non précisé :** {cell(f.get('non_precise'))}\n")

    s = p.get("systeme_de_pouvoirs")
    if s:
        a("### Système de pouvoirs (précisions de l'utilisateur ; rien n'est une règle fixée sauf mention)\n")
        a(f"- **Critère :** {cell(s['critere'].get('texte'))} ({cell(s['critere'].get('statut'))})")
        L = s["limites_affirmees"]
        a(f"- **Limites affirmées :** {cell(L.get('liste'))} ({cell(L.get('statut'))}). Non précisé : {cell(L.get('non_precise'))}")
        O = s["option_a_trancher"]
        a(f"- **Option à trancher :** {cell(O.get('texte'))} ({cell(O.get('statut'))}). Recoupe : {cell(O.get('recoupe'))}")
        a(f"- **Position de méthode :** {cell(s['position_de_methode'].get('texte'))}")
        for h in s.get("hypotheses", []):
            a(f"- **Hypothèse :** {cell(h.get('texte'))} : {cell(h.get('statut'))}")
        a("")

    e = p.get("esthetique_vestimentaire")
    if e:
        a("### Esthétique vestimentaire\n")
        a(f"- **Décidé (cadre du 3 oct.) :** « {cell(e.get('decide_depuis_le_3_oct'))} »")
        d = e.get("definitions", {})
        a(f"- **« Archaïque mais pas trop » :** {cell(d.get('archaique_mais_pas_trop'))}")
        an = d.get("anachronisme", {})
        a(f"- **Anachronisme :** {cell(an.get('texte'))} ({cell(an.get('statut'))})")
        a(f"- **Style copié ou inspiré de :** {cell(e.get('inspire_de'))}")
        a(f"- **Cadre temporel flou comme :** {cell(e.get('cadre_temporel_flou_comme'))}")
        a(f"- **Difficulté :** {cell(e.get('difficulte'))}")
        if e.get("limite_floue"):
            a(f"- **Limite floue :** {cell(e.get('limite_floue'))}")
        ce = e.get("cadre_vestimentaire_ecole")
        if ce:
            a(f"- **Cadre vestimentaire d'école ({DECISIONS.get(ce.get('statut_decision',''), ce.get('statut_decision'))}) :** {cell(ce.get('texte'))} ; importance dans l'histoire : {cell(ce.get('importance_dans_l_histoire'))}")
        a(f"- **Source documentaire :** {cell(e.get('source_documentaire'))}\n")
        a("| Image | Pour | Œuvre | Rôle | Décision |\n|---|---|---|---|---|")
        for v in e.get("references_visuelles", []):
            a(f"| {cell(v.get('image'))} | {cell(v.get('pour'))} | {cell(v.get('oeuvre'))} | {cell(v.get('role'))} | {DECISIONS.get(v.get('statut_decision',''), v.get('statut_decision'))} |")
        a("")

    oc, he, iv = p.get("occultisme"), p.get("heritages_melanges"), p.get("inspirations_visuelles_non_decidees")
    if oc or he or iv:
        a("### Occultisme, héritages mélangés, inspirations visuelles\n")
        if oc:
            a(f"- **Occultisme :** penche vers {cell(oc.get('penche_vers'))}. Niveaux possibles : {cell(oc.get('niveaux_possibles'))}. {cell(oc.get('statut'))}")
            if oc.get("precision_livres"):
                a(f"- **Occultisme, livres :** {cell(oc.get('precision_livres'))}")
        if he:
            a(f"- **Héritages mélangés :** {cell(he.get('facons_retenues'))}. {cell(he.get('statut'))}")
        for x in iv or []:
            a(f"- **{cell(x.get('element'))} :** {DECISIONS.get(x.get('statut_decision',''), x.get('statut_decision'))} ({cell(x.get('note'))})")
        a("")

    al = p.get("ambiance_des_lieux")
    if al:
        a("### Ambiance des lieux (décors naturels)\n")
        a(f"- **Statut :** {DECISIONS.get(al.get('statut_decision',''), al.get('statut_decision'))}")
        a(f"- **Sources visuelles :** {cell(al.get('sources_visuelles'))}")
        a(f"- **Ambiance ({al['ambiance']['source']}) :** {cell(al['ambiance']['texte'])}")
        a(f"- **Usage des images ({al['usage_des_images']['source']}) :** {cell(al['usage_des_images']['texte'])}")
        for x in al.get("procedes_visuels", []):
            a(f"- **Procédé visuel ({x['source']}, avis U : {cell(x.get('avis_U'))}) :** {cell(x['texte'])}")
        a(f"- **Pierres levées :** {cell(al.get('pierres_levees'))}")
        for x in al.get("reponses_de_U", []):
            st = f" [{DECISIONS.get(x['statut_decision'], x['statut_decision'])}]" if x.get("statut_decision") else ""
            a(f"- **Réponse de U : {cell(x['point'])} :** {cell(x['reponse'])}{st}")
        a(f"- **À préciser :** {cell(al.get('a_preciser'))}\n")

    a("### Points non tranchés du projet\n")
    a(cell(p.get("non_tranche")) + "\n")

    a("## 2. Échelle décisionnelle\n")
    a("| Barreau | Sens |\n|---|---|")
    a("| non précisé | élément cité, statut non dit |")
    a("| intérêt | ce qui t'intéresse ou te plaît ; pas une décision pour l'œuvre |")
    a("| envisagé | possibilité réelle à laquelle tu as réfléchi (« où et comment l'utiliser ? »), non validée, abandonnable |")
    a("| décidé | choisi pour l'œuvre |\n")
    cnt = {}
    for r in refs:
        k = r.get("statut_decision", "")
        cnt[k] = cnt.get(k, 0) + 1
    a("Fiches par `statut_decision` : " + ", ".join(f"{DECISIONS.get(k,k)} : {n}" for k, n in sorted(cnt.items())) + ".\n")

    a(f"## 3. Les {len(refs)} fiches (tableau)\n")
    a("| Référence | Relation | Décision | Source | Limite de lecture |\n|---|---|---|---|---|")
    for r in refs:
        a(f"| {cell(r.get('reference'))} | {cell(r.get('statut_relation'))} | "
          f"{DECISIONS.get(r.get('statut_decision',''), r.get('statut_decision'))} | "
          f"{SOURCES.get(r.get('source'), cell(r.get('source')))} | {cell(r.get('limite_lecture'))} |")
    a("")

    a("## 4. Détail des fiches (champs renseignés uniquement)\n")
    for r in refs:
        a(f"### {r.get('reference')}\n")
        a(f"- **Relation :** {cell(r.get('statut_relation'))} ; **décision :** "
          f"{DECISIONS.get(r.get('statut_decision',''), r.get('statut_decision'))} ; "
          f"**source :** {SOURCES.get(r.get('source'), cell(r.get('source')))}")
        for cle, lab in ETIQUETTES:
            v = r.get(cle)
            if vide(v):
                continue
            if isinstance(v, dict) or (isinstance(v, list) and v and isinstance(v[0], dict)):
                a(f"- **{lab} :**")
                for x in (v if isinstance(v, list) else [v]):
                    a(f"  - {fmt(x)}")
            else:
                a(f"- **{lab} :** {fmt(v)}")
        a("")
    return "\n".join(o).rstrip() + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml", default="fiches_references_projet.yaml")
    ap.add_argument("--md", default="VUE_references_projet.md")
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args()
    texte = vue(yaml.safe_load(open(a.yaml, encoding="utf-8")))
    if a.verifier:
        try:
            actuel = open(a.md, encoding="utf-8").read()
        except FileNotFoundError:
            sys.exit("Vue absente : lancer sans --verifier.")
        if actuel != texte:
            sys.exit("La vue MD n'est pas à jour (ou a été modifiée à la main). Relancer sans --verifier.")
        print("OK : la vue MD correspond au YAML.")
    else:
        open(a.md, "w", encoding="utf-8").write(texte)
        print(f"Écrit : {a.md}")
