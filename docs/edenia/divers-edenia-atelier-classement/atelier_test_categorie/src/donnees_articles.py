"""Articles de worldbuilding (19 oct.), sur le modèle du wiki Hunter × Hunter :
le menu mène à des ARTICLES (Media → « Hunter × Hunter », Characters → « List of Characters »,
World → « World of Hunter × Hunter ») ; les catégories ne sont que des pages de navigation.
Ici : « Edenia » (= Media), « Liste des personnages » (= Characters), « Monde d'Edenia » (= World).
Pas d'équivalent du Nen : le système de pouvoirs est mis de côté dans le YAML.
Rien n'est ajouté : chaque phrase reprend le YAML, une réponse datée de l'utilisateur ou une fiche existante.
Les sections sans données (intrigue, langues, monnaies, calendrier…) ne sont pas créées."""
import re, pathlib
from collections import Counter
from donnees_yaml import P, PAGES as PY, e, bd, items, page
from donnees_tests import TESTS

D = pathlib.Path(__file__).resolve().parent
_t = (D / 'template.html').read_text()
_l = _t[_t.index('const LIEUX = ['):_t.index('\n];', _t.index('const LIEUX = ['))]
LIEUX = [dict(slug=a, t=b, sub=c, st=d) for a, b, c, d in
         re.findall(r'\{slug:"([^"]+)", t:"([^"]+)", sub:"([^"]+)", st:"([^"]+)"', _l)]
ALL = {f"{p['cat']}/{p['slug']}": p for p in PY + TESTS}
ALL.update({f"lieux/{l['slug']}": l for l in LIEUX})
ALL.update({'univers/edenia': {'t': 'Edenia'}, 'univers/monde-d-edenia': {'t': 'Monde d\'Edenia'},
            'personnages/liste-des-personnages': {'t': 'Liste des personnages'}})


def L(k, lbl=None):
    """Lien interne vers une fiche (vérifié) ou une catégorie (« cat:lieux »)."""
    if k.startswith('cat:'):
        return f'<a href="#/{k[4:]}">{e(lbl)}</a>'
    assert k in ALL, k
    return f'<a href="#/{k}">{e(lbl or ALL[k]["t"])}</a>'


def gosub(cat, sub, lbl, n):
    return f'<button class="fx-link" data-gosub="{cat}:{sub}">{e(lbl)}</button> ({n})'


def art(cat, t, sub, st, ex, lead, secs, src, sl, **kw):
    """Comme page(), mais chaque section peut avoir un 3e élément : ses « Article principal »."""
    d = page(cat, t, sub, st, ex, lead, (), src=src, sl=sl, **kw)
    d['secs'] = []
    for sec in secs:
        h, ps, m = sec[0], list(sec[1]), list(sec[2]) if len(sec) > 2 else []
        for k in m:
            assert k.startswith('cat:') or k in ALL, k
        if ps:
            d['secs'].append([h, ps] + ([m] if m else []))
    return d


cv = P['cadre_valide']; tech = P['technologie']; sm = P['structure_du_monde']; ev = P['esthetique_vestimentaire']
fk = P['folklore']; hm = P['heritages_melanges']; am = P['ambiance_des_lieux']; ar = P['arthurien']
genre, edition = [x.strip() for x in P['genre'].split(',')]
n_oe = Counter(p['sub'] for p in PY if p['cat'] == 'oeuvres')
OE_SUBS = [('influences', 'Influences'), ('references', 'Références'), ('sources', 'Sources documentaires'),
           ('traditions', 'Corpus de traditions'), ('autres', 'Relation non précisée')]
n_tests = sum(1 for p in TESTS if p['slug'].startswith('test-'))
PERSOS = ['personnages/brann', 'personnages/cosmo-dumas', 'personnages/harley-delphine']
LIEUX_SUBS = [('cadre', 'Cadre validé'), ('naturelles', 'Zones naturelles'), ('arthurien', 'Lieux arthuriens'),
              ('brouillon', 'Zones de brouillon')]
ARTICLES = []

# ------------------------------------------------------------------ EDENIA (= article « Hunter × Hunter », relié à Media)
ARTICLES.append(art('univers', 'Edenia', 'articles', 'mix',
    'Article général sur le projet : genre, cadre, personnages, influences, tests.',
    f'<b>Edenia</b> (nom provisoire) est un projet de <b>{e(genre)}</b>, pensé pour l\'<b>{e(edition)}</b>. '
    f'Son monde est un « {e(cv[0])} » : {e(cv[2])}.',
    [('Cadre', [f'{e(x[0].upper() + x[1:])}. {bd("decide")}' for x in cv],
      ['univers/monde-d-edenia', 'univers/cadre-valide']),
     ('Personnages', [f'Trois personnages sont nommés : {", ".join(L(k) for k in PERSOS)}. '
                      'Harley Delphine est un nom provisoire, et le personnage n\'est pas encore défini (12 oct.).'],
      ['personnages/liste-des-personnages']),
     ('Influences', [f'{L("oeuvres/runeterra-league-of-legends", "Runeterra")} est noté comme la <b>référence principale du monde</b> '
                     '(« Edenia en est proche », note du dépôt).',
                     'Pour la structure du monde, tu cites un mélange de The Witcher 3, de Runeterra et de Fullmetal Alchemist, dosage non précisé (11 oct.).',
                     'Œuvres notées : ' + ' · '.join(gosub('oeuvres', k, l, n_oe[k]) for k, l in OE_SUBS if n_oe[k]) + '.',
                     'Pages de recherche (hors canon, pour explorer des concepts) : ' + gosub('recherches', 'arthurien', 'Légende arthurienne', 2) + '.'],
      ['cat:oeuvres', 'cat:recherches']),
     ('Esthétique', [f'« {e(ev["decide_depuis_le_3_oct"])} » {bd("decide")} depuis le 3 oct. : {e(ev["definitions"]["archaique_mais_pas_trop"])}.',
                     f'Éléments modernes anachroniques dans les tenues {bd("decide")} (15 oct.).'],
      ['univers/esthetique-vestimentaire']),
     ('Tests visuels', [f'{n_tests} images générées avec PixAI pour tester des styles et des designs. <b>Rien n\'est canon</b>, '
                        'et aucune ne représente Brann, Cosmo ou Harley.',
                        f'Outils : {L("tests/outils-pixai", "modèles et LoRA PixAI")} · {L("tests/tier-liste-personnages", "tier liste des tags de personnages")}.'],
      ['cat:tests']),
     ('Pas encore défini', ['<b>Intrigue</b> : rien n\'est noté dans le YAML.',
                            '<b>Système de pouvoirs</b> : mis de côté pour l\'instant (YAML).',
                            f'<b>Harley</b> : personnage pas encore défini ({L("personnages/harley-delphine", "fiche")}).'])],
    'YAML · projet.genre, cadre_valide, esthetique_vestimentaire, references ; tes réponses du 11, 12 et 15 oct.',
    'edenia',
    ib=[['Nom', 'Edenia <small>(nom provisoire)</small>'], ['Genre', e(genre)], ['Édition', e(edition)],
        ['Monde', e(cv[0])], ['Personnages nommés', '3']],
    rel=['univers/monde-d-edenia', 'personnages/liste-des-personnages', 'oeuvres/runeterra-league-of-legends']))

# ------------------------------------------------------------------ MONDE D'EDENIA (= « World of Hunter × Hunter », relié à World)
lieux_items = []
for s, lbl in LIEUX_SUBS:
    ls = [l for l in LIEUX if l['sub'] == s]
    lieux_items.append(f'<b>{e(lbl)}</b> : ' + ', '.join(f'{L("lieux/" + l["slug"])} {bd(l["st"])}' for l in ls) + '.')
lieux_items.append(f'<b>Carte du monde</b> : {e(sm["carte_du_monde"]["texte"])} {bd(sm["carte_du_monde"]["statut_decision"])}')
env = [p for p in PY if p['cat'] == 'folklore' and p['st'] == 'envisage']
ARTICLES.append(art('univers', 'Monde d\'Edenia', 'articles', 'mix',
    'Vue d\'ensemble du monde : structure, lieux, technologie, créatures, cultures.',
    f'Le <b>monde d\'Edenia</b> est un « {e(cv[0])} » : {e(cv[2])} {bd("decide")}.',
    [('Présentation', [f'{e(cv[0][0].upper() + cv[0][1:])} ; {e(cv[2])} {bd("decide")}.',
                       f'{e(cv[1][0].upper() + cv[1][1:])} {bd("decide")}.',
                       f'Esthétique « {e(ev["decide_depuis_le_3_oct"])} » {bd("decide")}.'],
      ['univers/cadre-valide']),
     ('Structure politique', items(sm, ['plan', 'regions', 'echelle', 'modele_de_monde'],
                                   ['Plan', 'Régions', 'Échelle', 'Modèle de monde']),
      ['univers/structure-du-monde']),
     ('Lieux', lieux_items, ['cat:lieux']),
     ('Paysages et ambiance', [f'<b>Ambiance</b> : {e(am["ambiance"]["texte"])} {bd(am["statut_decision"])}',
                               f'<b>Usage des images</b> : {e(am["usage_des_images"]["texte"])}.',
                               f'<b>À préciser</b> : {e(am["a_preciser"])}.',
                               f'<b>Images</b> : {e(am["statut_des_images"])}.']),
     ('Technologie et ressources', [f'<b>Plafond théorique</b> : {e(cv[3])} {bd("decide")}'] +
      items(tech, ['plafond_armes_a_feu', 'baisse_plafond_general', 'inegalite_regionale'],
            ['Armes à feu', 'Plafond général', 'Inégalité régionale']),
      ['univers/technologie']),
     ('Créatures et folklore', [f'<b>Décidé</b> : {L("folklore/agrippa", "Agrippa")}, figure du Dictionnaire infernal {bd("decide")}',
                                f'<b>Envisagés</b> {bd("envisage")} : ' + ', '.join(L(f"folklore/{p['slug']}", p['t']) for p in env) + '.',
                                f'<b>Créature locale</b> : les {L("folklore/barbegazi", "Barbegazi")} pour la {L("lieux/region-montagnarde")} (envisagé, 9 oct.).',
                                f'<b>En intérêt</b> {bd("interet")} : ' + gosub('folklore', 'carte', 'créatures de la carte', len(fk['interet']['creatures_de_la_carte'])) +
                                ' · ' + gosub('folklore', 'autres', 'autres pistes', len(fk['interet']['autres'])) + '.'],
      ['cat:folklore']),
     ('Cultures et héritages', [f'<b>Héritages mélangés</b> : {e(" ; ".join(hm["facons_retenues"]))} ; {e(hm["statut"])} {bd("np")}',
                                '<b>Matière arthurienne</b> : ' + ' ; '.join(e(x) for x in ar['decide']) + f' {bd("decide")}',
                                f'<b>Brouillons</b> : {L("univers/inspirations-des-brouillons")} et {L("univers/vocabulaire-des-brouillons")} {bd("interet")}'],
      ['univers/heritages-melanges', 'univers/regles-arthuriennes']),
     ('Esthétique', [f'« {e(ev["decide_depuis_le_3_oct"])} » {bd("decide")} : {e(ev["definitions"]["archaique_mais_pas_trop"])}.',
                     f'Éléments modernes anachroniques {bd("decide")} (15 oct.).',
                     f'<b>Occultisme</b> : {e(P["occultisme"]["statut"])} {bd("np")}'],
      ['univers/esthetique-vestimentaire', 'univers/occultisme'])],
    'YAML · projet.cadre_valide, structure_du_monde, technologie, ambiance_des_lieux, folklore, heritages_melanges, arthurien, esthetique_vestimentaire, occultisme ; fiches Lieux',
    'monde-d-edenia',
    ib=[['Type', f'Un seul monde, une seule époque {bd("decide")}'], ['Héritages', e(cv[0])],
        ['Plafond technologique', f'1950 {bd("decide")}<br>1914 {bd("envisage")}'], ['Armes à feu', f'1860 {bd("decide")}'],
        ['Lieux', f'{len(LIEUX)} fiches']],
    rel=['univers/structure-du-monde', 'univers/technologie', 'univers/cadre-valide', 'oeuvres/runeterra-league-of-legends']))

# ------------------------------------------------------------------ LISTE DES PERSONNAGES (= « List of Characters », relié à Characters)
def _ini(t):
    return ''.join(w[0] for w in t.split()[:2]).upper()


cells = ''.join(f'<a class="roster__c" href="#/{k}"><span class="roster__img"><b>{e(_ini(ALL[k]["t"]))}</b></span>'
                f'<span class="roster__n">{e(ALL[k]["t"])}</span></a>' for k in PERSOS)
roster = (f'<span class="roster"><span class="roster__h">Personnages principaux</span>'
          f'<span class="roster__g">{cells}</span></span>')
ARTICLES.append(art('personnages', 'Liste des personnages', 'listes', 'np',
    'Tableau des personnages nommés, rangés par groupe.',
    'Liste des personnages nommés d\'<b>Edenia</b>, rangés par groupe. Harley Delphine est un nom provisoire.',
    [('Personnages principaux', [roster]),
     ('Voir aussi', [f'{L("personnages/inspirations-arthuriennes")} : les personnages arthuriens sont des inspirations seulement, avec des noms différents {bd("decide")}.'])],
    'YAML · projet.personnages_edenia ; ta correction du 12 oct. (Harley)',
    'liste-des-personnages', noib=True,
    rel=PERSOS))

SUBS_ARTICLES = {'univers': {'articles': 'Articles généraux'}, 'personnages': {'listes': 'Listes'}}
