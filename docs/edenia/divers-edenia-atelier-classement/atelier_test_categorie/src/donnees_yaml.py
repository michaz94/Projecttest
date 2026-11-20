"""Pages Personnages, Folklore, Univers et Œuvres de référence, tirées du YAML du dépôt
(src/fiches_references_projet.yaml : version b1bffb0 + mise à jour du 22 oct. 2026) et des réponses de l'utilisateur
notées dans le rapport d'influences (12 oct.). Rien n'est ajouté : chaque phrase reprend une valeur
du YAML ou une réponse datée. Les pages Lieux restent dans template.html."""
import html, re, unicodedata, pathlib, yaml

D = pathlib.Path(__file__).resolve().parent
Y = yaml.safe_load(open(D / 'fiches_references_projet.yaml', encoding='utf-8'))
P = Y['projet']
ST = {'decide': 'Décidé', 'envisage': 'Envisagé', 'interet': 'Intérêt', 'non_precise': 'Non précisé', 'np': 'Non précisé', 'hc': 'Hors canon'}
CLS = {'decide': 's-decide', 'envisage': 's-envisage', 'interet': 's-interet', 'non_precise': 's-np', 'np': 's-np', 'hc': 's-hc'}


def e(s):
    return html.escape(str(s), quote=False)


def st_of(v):
    return {'non_precise': 'np', None: 'np'}.get(v, v)


def bd(st):
    st = st_of(st)
    return f'<span class="badge {CLS[st]}">{ST[st]}</span>'


def slug(s):
    s = unicodedata.normalize('NFD', s.lower().replace('×', 'x'))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def page(cat, t, sub, st, ex, lead, secs=(), src='', warn=None, rel=(), sl=None, **kw):
    d = dict(cat=cat, slug=sl or slug(t), t=t, sub=sub, st=st_of(st), ex=ex, lead=lead,
             secs=[[h, list(ps)] for h, ps in secs if ps], src=src, rel=list(rel))
    if warn:
        d['warn'] = warn
    d.update(kw)
    return d


PAGES = []
add = PAGES.append

# ------------------------------------------------------------------ PERSONNAGES
per = {p['nom']: p for p in P['personnages_edenia']}
c = per['Cosmo Dumas']
rv = [r for r in P['esthetique_vestimentaire']['references_visuelles'] if r['pour'] == 'Cosmo Dumas']
add(page('personnages', 'Cosmo Dumas', 'principaux', 'np',
         'Inspiré d\'Ekko, de Killua Zoldyck et de Shisui Uchiha.',
         '<b>Cosmo Dumas</b> est l\'un des trois personnages nommés d\'Edenia.',
         [('Inspiré de', [e(x) for x in c['inspire_de']]),
          ('Tenue', [f'{e(r["image"])} : {e(r["role"])} ({e(r["oeuvre"])}).' for r in rv])],
         src='YAML · personnages_edenia ; esthetique_vestimentaire.references_visuelles',
         rel=['oeuvres/runeterra-league-of-legends', 'oeuvres/hunter-x-hunter', 'oeuvres/naruto', 'univers/esthetique-vestimentaire']))

b = per['Brann']
rvb = [r for r in P['esthetique_vestimentaire']['references_visuelles'] if r['pour'] == 'Brann']
add(page('personnages', 'Brann', 'principaux', 'np',
         'Inspiré de Luffy, Yusuke, Edward Elric et Perceval. Goal en intérêt : devenir chevalier.',
         '<b>Brann</b> est l\'un des trois personnages nommés d\'Edenia. Son nom de famille est laissé vide.',
         [('Inspiré de', [e(x) for x in b['inspire_de']]),
          ('Goal', [f'« {e(b["goal"]["valeur"])} » {bd(b["goal"]["statut_decision"])} ({e(b["goal"]["source"])}).']),
          ('Nom', ['Nom de famille : « Pandragon » retiré, le nom est laissé vide (décidé, U, 9 oct. 2026).',
                   'Origine du prénom (tes réponses du 12 oct.) : Ben 10, puis Game of Thrones (« Bran »), puis Hearthstone (« Brann »). Pas encore dans le YAML.']),
          ('Tenue', [f'{e(r["image"])} : {e(r["role"])}' for r in rvb])],
         src='YAML · personnages_edenia ; arthurien.decide ; U 12 oct.',
         warn='L\'Atelier V7 crée encore une fiche « Brann Pandragon » (graine du tour 107-108), alors que ce nom de famille est retiré depuis le 9 oct.',
         rel=['oeuvres/one-piece', 'oeuvres/yu-yu-hakusho', 'oeuvres/fullmetal-alchemist', 'oeuvres/fabula-fantasia-tony-valente', 'personnages/inspirations-arthuriennes']))

h = per['Harley Delphine']
add(page('personnages', 'Harley Delphine', 'principaux', 'np',
         'Nom provisoire. Personnage pas encore défini.',
         '<b>Harley Delphine</b> : nom provisoire, pas décidé (ta correction du 12 oct.). Harley n\'est pas définie pour l\'instant.',
         [('Inspirée de (YAML)', [e(x) for x in h['inspire_de']]),
          ('Tes réponses du 12 oct. (pas encore dans le YAML)',
           ['Personnalité visée : Shallan, Maka Albarn (Soul Eater), Luna Lovegood (Harry Potter).',
            'Apparence : « pour moi son apparence ressemble à Raiponce de Tangled ».',
            'Prénom : vient de Gwen Tennyson (Ben 10).'])],
         src='YAML · personnages_edenia ; U 12 oct.',
         rel=['oeuvres/the-stormlight-archive-sanderson', 'oeuvres/harry-potter-films', 'oeuvres/worm-wildbow']))

ar = P['arthurien']
add(page('personnages', 'Inspirations arthuriennes', 'inspirations', 'decide',
         'Des inspirations seulement, avec des noms différents.',
         'Règle décidée : les personnages arthuriens sont <b>des inspirations seulement</b>, avec des noms différents (aucun nom direct comme Arthur, Merlin, Lancelot).',
         [('Personnages qui inspirent', [e(x) for x in ar['personnages_arthuriens_inspirations']]),
          ('Écarté', [e(x) for x in ar['abandonne']] + [e(ar['note_merlin'])])],
         src='YAML · arthurien', rel=['univers/regles-arthuriennes', 'personnages/brann']))

# ------------------------------------------------------------------ FOLKLORE
fk = P['folklore']
DI_EXTRAIT = ('D\'après tes extraits du Dictionnaire infernal (Pdfmd, version 1818) : Henri Corneille Agrippa, '
              'né à Cologne en 1486, « mourut à l\'hôpital de Grenoble » ; accusé de sorcellerie, il est l\'auteur de la <i>Philosophie occulte</i>.')
for n in fk['decide']:
    add(page('folklore', 'Agrippa', 'figures', 'decide', 'Décidé. Figure du Dictionnaire infernal.',
             f'<b>{e(n)}</b> : seule entrée décidée du folklore.',
             [('Dans tes extraits', [DI_EXTRAIT]),
              ('Ta consigne', ['Ne pas se focaliser seulement sur la partie populaire (les 72 démons) : le dictionnaire traite énormément d\'autres sujets (brouillons, validé le 11 oct.).'])],
             src='YAML · folklore.decide ; Pdfmd/Dictionnaire_Infernal_Extraits.md', rel=['oeuvres/dictionnaire-infernal-collin-de-plancy-ed-1825']))
EXTRA = {
    'Barbegazi': dict(secs=[('Lieu', ['Créature locale de la région montagnarde enneigée (U, 9 oct.).'])],
                      warn='La fiche créatures du dépôt les dit « décidés » ; le YAML dit envisagé. Le YAML fait foi.',
                      rel=['lieux/region-montagnarde']),
    'Mélusine': dict(rel=['oeuvres/melusine']),
    'Le Petit Homme rouge': dict(rel=['oeuvres/petit-homme-rouge']),
}
for n in fk['envisage']:
    x = EXTRA.get(n, {})
    add(page('folklore', n, 'figures', 'envisage', 'Envisagé : possibilité réelle, pas validée.',
             f'<b>{e(n)}</b> est envisagé (possibilité réelle, pas validée).', x.get('secs', ()),
             src='YAML · folklore.envisage', warn=x.get('warn'), rel=x.get('rel', ())))
for n in fk['interet']['creatures_de_la_carte']:
    add(page('folklore', n, 'carte', 'interet', 'Créature de la carte, en intérêt.',
             f'<b>{e(n)}</b> fait partie des créatures de la carte (intérêt : ça te plaît, ce n\'est pas une décision).',
             src='YAML · folklore.interet.creatures_de_la_carte'))
for n in fk['interet']['autres']:
    rel = ['oeuvres/chasse-sauvage'] if n == 'Chasse sauvage' else ['oeuvres/urban-rivals'] if n.startswith('Yétis') else []
    t = 'Yétis' if n.startswith('Yétis') else n
    lead = f'<b>{e(n)}</b> : piste en intérêt.'
    add(page('folklore', t, 'autres', 'interet', e(n) if t != n else 'Piste en intérêt.', lead,
             src='YAML · folklore.interet.autres', rel=rel))
add(page('folklore', 'Figures historiques du Dictionnaire infernal', 'historiques', 'np',
         'Attrait fort, statut individuel non précisé.',
         e(fk['non_precise']) + '.', src='YAML · folklore.non_precise',
         rel=['oeuvres/dictionnaire-infernal-collin-de-plancy-ed-1825']))

# ------------------------------------------------------------------ UNIVERS
def items(d, keys, lbls):
    out = []
    for k, l in zip(keys, lbls):
        v = d[k]
        s = f'<b>{e(l)}</b> : {e(v["texte"])} {bd(v.get("statut_decision"))}'
        if v.get('note'):
            s += f' <span class="sub">{e(v["note"])}</span>'
        out.append(s)
    return out

add(page('univers', 'Cadre validé', 'monde', 'decide', 'Les six points validés du cadre d\'Edenia.',
         '<b>Cadre validé</b> d\'Edenia, ' + e(P['genre']) + '.',
         [('Les six points', [e(x) for x in P['cadre_valide']])],
         src='YAML · projet.cadre_valide', rel=['univers/technologie', 'lieux/zone-western', 'lieux/zone-industrielle']))
t = P['technologie']
add(page('univers', 'Technologie', 'monde', 'mix', 'Armes à feu plafonnées à 1860 ; baisse du plafond à 1914 envisagée.',
         'Ce que tu as dit sur la <b>technologie</b> le 12 oct. 2026.',
         [('Points', items(t, ['plafond_armes_a_feu', 'baisse_plafond_general', 'inegalite_regionale'],
                           ['Armes à feu', 'Plafond général', 'Inégalité régionale']))],
         src='YAML · projet.technologie (12 oct.)', rel=['univers/cadre-valide', 'lieux/zone-industrielle', 'oeuvres/bioshock-infinite']))
sm = P['structure_du_monde']
add(page('univers', 'Structure du monde', 'monde', 'mix', 'Un royaume principal, des cités-États, des royaumes adjacents.',
         'Ce que tu as dit sur la <b>structure du monde</b> le 11 oct. 2026.',
         [('Points', items(sm, ['plan', 'regions', 'echelle', 'modele_de_monde', 'carte_du_monde'],
                           ['Plan', 'Régions', 'Échelle', 'Modèle de monde', 'Carte du monde']))],
         src='YAML · projet.structure_du_monde (11 oct.)',
         rel=['oeuvres/the-witcher-3-cd-projekt-red', 'oeuvres/runeterra-league-of-legends', 'oeuvres/fullmetal-alchemist', 'oeuvres/urban-rivals']))
ev = P['esthetique_vestimentaire']
add(page('univers', 'Esthétique vestimentaire', 'esthetique', 'mix', '« Archaïque mais pas trop » (décidé le 3 oct.), avec des anachronismes modernes (décidé le 15 oct.).',
         f'Esthétique vestimentaire : <b>« {e(ev["decide_depuis_le_3_oct"])} »</b> {bd("decide")} depuis le 3 oct., '
         f'avec des <b>éléments modernes anachroniques</b> {bd("decide")} depuis le 15 oct. (ta décision).',
         [('Définitions', [f'<b>Archaïque mais pas trop</b> : {e(ev["definitions"]["archaique_mais_pas_trop"])}.',
                           f'<b>Anachronisme</b> : {e(ev["definitions"]["anachronisme"]["texte"])}. {bd("decide")} '
                           'Décidé le 15 oct. (ta réponse : « Décidé »). '
                           '<span class="sub">Le YAML (commit b1bffb0) indique encore « non décidé ; a une part de vérité » : à mettre à jour dans le dépôt.</span>']),
          ('Inspirée de', [e(', '.join(ev['inspire_de'])) + ' ; cadre temporel flou comme ' + e(', '.join(ev['cadre_temporel_flou_comme'])) + '.']),
          ('Limite floue', [e(ev['limite_floue'])]),
          ('Tes précisions du 15 oct.', [
              'Tu veux une esthétique vestimentaire plus moderne et anachronique, « dans le style vestimentaire » des 7 images de la galerie ci-dessous.',
              'Les 12 tests visuels PixAI sont « Edenia compatible ».',
              'Tests 09 et 10 : ils doivent sonner légèrement moins moderne, à cause du jean.']),
          ('Ce que les 7 images ont en commun (lecture de l\'IA, à confirmer)', [
              '<b>Base ancienne</b> : robes, manteaux longs, tuniques à capuche, capes ; ceintures de cuir, bandoulières, fourreaux ; pièces d\'armure isolées, brassards dorés ; broderies et symboles (celtiques, alchimiques, religieux).',
              '<b>Coupes modernes</b> : tunique taillée comme un sweat à capuche (Barrier Mage), blazer d\'école avec cravate, pantalons amples resserrés à la cheville, crop top, chaussettes hautes.',
              '<b>Un ou deux objets modernes, pas plus</b> : baskets, casque audio, montre, sac à dos.',
              '<b>Chaussures solides</b> : bottes de combat à lacets ou à sangles sur presque toutes les images.',
              '<b>Asymétrie</b> : un seul bras en armure, un seul gant.',
              '<b>Fonction visible</b> : sacoches, sangles, outils et armes portés sur soi ; l\'habit dit le métier ou le statut, ce qui rejoint ta « limite floue ».',
              '<b>Couleurs</b> : base sombre (noir, bleu nuit) et une seule couleur d\'accent (jaune, vert, or, rouge).',
              '<b>Règle possible</b> : un élément moderne passe quand il est entouré de pièces anciennes. Une tenue entièrement contemporaine (jean droit et t-shirt imprimé, tests 09 et 10) sonne trop moderne. C\'est le même genre de détail que les lacets de Barrier Mage.']),
          ('Tenue d\'école ou d\'académie', [f'{e(ev["cadre_vestimentaire_ecole"]["texte"])} {bd("envisage")} Importance dans l\'histoire : inconnue.']),
          ('Difficulté', [e(ev['difficulte'])]),
          ('Références visuelles', [f'<b>{e(r["image"])}</b> (pour {e(r["pour"])}) : {e(r["role"])}' for r in ev['references_visuelles']] + [
              '<b>Duo en forêt : bras en armure, blazer d\'école et baskets</b> (ajouté le 15 oct.) : provenance non précisée.',
              '<b>Groupe sous un ciel étoilé : manteaux longs, sangles et bottes</b> (ajouté le 15 oct.) : générée avec Grok d\'après le nom du fichier.',
              '<b>Garçon à l\'auréole et au corbeau : robe brodée, brassards dorés, bottes de combat</b> (ajouté le 15 oct.) : provenance non précisée.',
              '<b>Vieil homme en fauteuil roulant à entrelacs celtiques</b> (ajouté le 15 oct.) : concept art, auteur non identifié.',
              '<b>Sorcière sur son balai</b> (ajouté le 15 oct.) : filigrane « YuumeiArt.com » visible.',
              '<span class="sub">Academy Ekko (concept art) et Barrier Mage, déjà listés plus haut, sont aussi dans la galerie. L\'une des nouvelles images est peut-être le « test HP + JJK dans un lieu shrekien » déjà noté : non confirmé.</span>'])],
         src='YAML · projet.esthetique_vestimentaire ; tes réponses et tes 7 images du 15 oct.',
         rel=['oeuvres/radiant-manga', 'oeuvres/runeterra-league-of-legends', 'personnages/cosmo-dumas', 'personnages/brann', 'tests/test-09', 'tests/test-10'],
         gal=['ten01', 'ten02', 'ten03', 'ten04', 'ten05', 'ten06', 'ten07'],
         galcap={'ten01': 'Duo en forêt : bras en armure, blazer et baskets',
                 'ten02': 'Groupe sous un ciel étoilé (Grok)',
                 'ten03': 'Garçon à l\'auréole et au corbeau',
                 'ten04': 'Academy Ekko, concept art (sunnykoda)',
                 'ten05': 'Vieil homme en fauteuil roulant celtique',
                 'ten06': 'Sorcière sur son balai (YuumeiArt.com)',
                 'ten07': 'Barrier Mage, couverture fictive (Grok)'},
         galvar=True))
iv = P['inspirations_visuelles_non_decidees']
add(page('univers', 'Inspirations visuelles non décidées', 'esthetique', 'mix', 'Personnages d\'inspiration asiatique ; objets bouddhiques japonais.',
         'Deux pistes visuelles, <b>non décidées</b>.',
         [('Pistes', [f'<b>{e(x["element"])}</b> {bd(x["statut_decision"])} <span class="sub">{e(x["note"])}</span>' for x in iv])],
         src='YAML · projet.inspirations_visuelles_non_decidees'))
oc = P['occultisme']
add(page('univers', 'Occultisme', 'esthetique', 'np', 'Volontairement non tranché ; penche vers l\'ambiance.',
         f'<b>Occultisme</b> : {e(oc["statut"])}.',
         [('Penche vers', [e(oc['penche_vers'])]), ('Livres de sorts', [e(oc['precision_livres'])])],
         src='YAML · projet.occultisme'))
hm = P['heritages_melanges']
add(page('univers', 'Héritages mélangés', 'monde', 'np', 'Deux façons retenues ; articulation non décidée.',
         f'<b>Héritages mélangés</b> : {e(hm["statut"])}.',
         [('Façons retenues', [e(x) for x in hm['facons_retenues']])], src='YAML · projet.heritages_melanges'))
ib = P['inspirations_issues_des_brouillons']
add(page('univers', 'Inspirations des brouillons', 'brouillons', 'interet', 'Bibliothèque bleue, Renaissance, Moyen Âge, fantasy épique.',
         f'Éléments de tes brouillons de worldbuilding ({e(ib["source"])}).',
         [('Éléments', [e(x) for x in ib['elements']]),
          ('Exclusion', [f'{e(ib["exclusion"]["texte"])} <span class="sub">{e(ib["exclusion"]["note"])}</span>'])],
         src='YAML · projet.inspirations_issues_des_brouillons'))
vb = P['vocabulaire_des_brouillons']
add(page('univers', 'Vocabulaire des brouillons', 'brouillons', 'interet', 'Titres et fonctions, événements : vocabulaire, pas décision.',
         f'Vocabulaire tiré de tes brouillons : {e(vb["note"])}.',
         [('Titres et fonctions', [e(', '.join(vb['titres_et_fonctions']))]), ('Événements', [e(', '.join(vb['evenements']))])],
         src='YAML · projet.vocabulaire_des_brouillons', rel=['oeuvres/feodalisme-dictionnaire-feodal-1820']))
add(page('univers', 'Règles arthuriennes', 'regles', 'decide', 'Noms de lieux français ; personnages en inspirations seulement.',
         'Règles <b>décidées</b> sur la matière arthurienne.',
         [('Décidé', [e(x) for x in ar['decide']]), ('Lieux', [e(ar['note_lieux']), e(ar['exception_lieux'])])],
         src='YAML · projet.arthurien', rel=['personnages/inspirations-arthuriennes', 'lieux/broceliande', 'lieux/le-lac']))
add(page('univers', 'Gimmicks des grands succès', 'regles', 'np', 'Pirate, Ninja, Shinigami… : le gimmick de chaque grand succès.',
         'Liste des <b>gimmicks des grands succès</b> notée dans le YAML. Aucun statut : c\'est un repère, pas un choix pour Edenia.',
         [('Liste', [e(g['gimmick']) + (f' ({e(g["oeuvre"])})' if g.get('oeuvre') else '') for g in P['gimmicks_des_grands_succes']])],
         src='YAML · projet.gimmicks_des_grands_succes'))

# ------------------------------------------------------------------ ŒUVRES DE RÉFÉRENCE
REL = {'influence': ('influences', 'Influence (ce qui t\'a façonné)'),
       'reference': ('references', 'Référence (point de comparaison ou éléments piochés)'),
       'influence+reference': ('influences', 'Influence et référence'),
       'source_documentaire': ('sources', 'Source documentaire'),
       'corpus_de_traditions': ('traditions', 'Corpus de traditions')}
LIENS = {
    'Runeterra (League of Legends)': ['personnages/cosmo-dumas', 'univers/structure-du-monde', 'univers/esthetique-vestimentaire'],
    'The Witcher 3 (CD Projekt Red)': ['univers/structure-du-monde', 'lieux/marais'],
    'Urban Rivals': ['univers/structure-du-monde', 'folklore/yetis'],
    'BioShock Infinite': ['lieux/zone-industrielle', 'univers/technologie'],
    'Dictionnaire infernal (Collin de Plancy, éd. 1825)': ['folklore/agrippa', 'folklore/figures-historiques-du-dictionnaire-infernal'],
    'Mélusine': ['folklore/melusine'], 'Petit Homme rouge': ['folklore/le-petit-homme-rouge'], 'Chasse sauvage': ['folklore/chasse-sauvage'],
    'Shrek': ['lieux/marais', 'lieux/foret-de-conte'],
    'Radiant (manga)': ['oeuvres/fabula-fantasia-tony-valente', 'univers/esthetique-vestimentaire'],
    'Fabula Fantasia (Tony Valente)': ['oeuvres/radiant-manga', 'personnages/brann'],
    'Hunter × Hunter': ['personnages/cosmo-dumas'], 'Naruto': ['personnages/cosmo-dumas'],
    'Yu Yu Hakusho': ['personnages/brann'], 'One Piece': ['personnages/brann'],
    'Fullmetal Alchemist': ['personnages/brann', 'univers/structure-du-monde'],
    'Harry Potter (films)': ['personnages/harley-delphine', 'oeuvres/harry-potter-livres'],
    'Harry Potter (livres)': ['personnages/harley-delphine', 'oeuvres/harry-potter-films'],
    'Worm (Wildbow)': ['personnages/harley-delphine'], 'The Stormlight Archive (Sanderson)': ['personnages/harley-delphine'],
    'Féodalisme (Dictionnaire féodal 1820)': ['univers/vocabulaire-des-brouillons'],
}
VAL = {'emprunt': 'emprunt', 'distance_a_maintenir': 'distance à maintenir'}
for r in Y['references']:
    n = r['reference']
    sub, rl = REL.get(r.get('statut_relation'), ('autres', None))
    secs = []
    secs.append(('Relation', [f'{e(rl) if rl else "Non précisée dans le YAML"} · source : {"toi" if r.get("source") == "U" else "ton dépôt"}.']))
    if r.get('aspect_vise'):
        secs.append(('Aspect visé', [e(r['aspect_vise'])]))
    if r.get('emprunts_ou_ecarts_par_aspect'):
        secs.append(('Emprunts et écarts', [f'<b>{e(x["aspect"])}</b> : {VAL.get(x["valeur"], e(x["valeur"]))}'
                                            + (f' ({e(x["date"])})' if x.get('date') else '')
                                            + (f', {e(x["reserve"])}' if x.get('reserve') else '')
                                            + (f' <span class="sub">{e(x["note"])}</span>' if x.get('note') else '')
                                            for x in r['emprunts_ou_ecarts_par_aspect']]))
    notes = []
    for k in ('role', 'note', 'note_utilisateur', 'voir_aussi', 'contrainte_liee', 'lien_avec'):
        if r.get(k):
            notes.append(e(r[k]))
    if r.get('structure_du_monde'):
        notes.append(e(r['structure_du_monde']['texte']) + ' ' + bd(r['structure_du_monde']['statut_decision']))
    if r.get('oeuvres_liees'):
        notes.append('Œuvres liées : ' + e(', '.join(r['oeuvres_liees'])))
    if r.get('inventaire_non_fige'):
        inv = r['inventaire_non_fige']
        notes.append('Inventaire non figé : ' + '; '.join(f'{e(k)} : {e(", ".join(v))}' for k, v in inv.items()))
    if notes:
        secs.append(('Notes', notes))
    lim = r.get('limite_lecture')
    if lim:
        secs.append(('Limite de lecture (anti-spoil)', [e(lim)] + ([e(r['note_limite'])] if r.get('note_limite') else [])))
    ex = r.get('aspect_vise') or r.get('note_utilisateur') or r.get('note') or (rl or 'Relation non précisée')
    ex = re.sub(r'^\(.*?\)\s*', '', str(ex))
    add(page('oeuvres', n, sub, r.get('statut_decision'), e(ex),
             f'<b>{e(n)}</b> : {e(rl.split(" (")[0].lower()) if rl else "relation non précisée"}.',
             secs, src='YAML · references',
             warn=None if rl else 'Le YAML ne donne pas de statut_relation à cette œuvre.',
             rel=LIENS.get(n, [])))

CATS_EXTRA = {
    'personnages': {'principaux': 'Personnages d\'Edenia', 'inspirations': 'Inspirations'},
    'folklore': {'figures': 'Figures et créatures', 'carte': 'Créatures de la carte', 'autres': 'Autres pistes', 'historiques': 'Figures historiques'},
    'univers': {'monde': 'Monde', 'esthetique': 'Esthétique', 'brouillons': 'Brouillons', 'regles': 'Règles et repères'},
    'oeuvres': {'influences': 'Influences', 'references': 'Références', 'sources': 'Sources documentaires', 'traditions': 'Corpus de traditions', 'autres': 'Relation non précisée'},
}

if __name__ == '__main__':
    from collections import Counter
    print(len(PAGES), Counter(p['cat'] for p in PAGES))
    slugs = {f"{p['cat']}/{p['slug']}" for p in PAGES}
    for p in PAGES:
        for r in p['rel']:
            if r not in slugs and not r.startswith('lieux/'):
                print('lien cassé', p['slug'], r)


# ------------------------------------------------------------------ ACCUEIL IMMERSIF (textes du YAML uniquement)
def _home():
    cv = P['cadre_valide']; t = P['technologie']; sm = P['structure_du_monde']
    ib = P['inspirations_issues_des_brouillons']; vb = P['vocabulaire_des_brouillons']
    am = P['ambiance_des_lieux']; hm = P['heritages_melanges']; ev = P['esthetique_vestimentaire']
    st = lambda v: st_of(v)
    return {
        'nom': P['nom_provisoire'], 'genre': P['genre'],
        'ambiance': {'texte': am['ambiance']['texte'], 'st': st(am['statut_decision']), 'images': am['statut_des_images']},
        'piliers': [
            {'titre': 'Un seul monde, une seule époque', 'st': 'decide', 'txt': 'Cadre validé, avec « ' + cv[1] + ' ».', 'go': 'univers/cadre-valide'},
            {'titre': 'Fantasy multi-héritages', 'st': 'decide',
             'txt': 'Cadre validé : « ' + cv[0] + ' ». Façons de mélanger les héritages : ' + ' ; '.join(hm['facons_retenues']) + '. ' + hm['statut'][0].upper() + hm['statut'][1:] + '.',
             'go': 'univers/heritages-melanges'},
            {'titre': '« Archaïque mais pas trop »', 'st': 'decide',
             'txt': 'Esthétique décidée depuis le 3 oct. : ' + ev['definitions']['archaique_mais_pas_trop'] + '.', 'go': 'univers/esthetique-vestimentaire'},
        ],
        'brouillons': {'elements': ib['elements'], 'st': st(ib['statut_decision']), 'exclusion': ib['exclusion']['texte']},
        'frise': [
            {'an': 'Moyen Âge', 'lbl': 'bas et milieu Moyen Âge', 'st': 'interet', 'txt': 'Inspiration de tes brouillons.', 'go': 'univers/inspirations-des-brouillons'},
            {'an': 'Renaissance', 'lbl': 'la science, le folklore, les superstitions, les croyances et la magie', 'st': 'interet', 'txt': 'Inspiration de tes brouillons.', 'go': 'univers/inspirations-des-brouillons'},
            {'an': '1860', 'lbl': 'plafond des armes à feu', 'st': st(t['plafond_armes_a_feu']['statut_decision']), 'txt': t['plafond_armes_a_feu']['texte'] + '.', 'go': 'univers/technologie'},
            {'an': '1914', 'lbl': 'plafond général abaissé ?', 'st': st(t['baisse_plafond_general']['statut_decision']), 'txt': t['baisse_plafond_general']['texte'] + '.', 'go': 'univers/technologie'},
            {'an': '1950', 'lbl': 'plafond technologique théorique', 'st': 'decide', 'txt': 'Cadre validé : ' + cv[3] + '.', 'go': 'univers/cadre-valide'},
        ],
        'inegalite': {'txt': t['inegalite_regionale']['texte'], 'st': st(t['inegalite_regionale']['statut_decision'])},
        'monde': [{'k': k, 'lbl': l, 'txt': sm[k]['texte'], 'st': st(sm[k]['statut_decision'])}
                  for k, l in [('plan', 'Plan'), ('regions', 'Régions'), ('modele_de_monde', 'Modèle de monde'), ('echelle', 'Échelle'), ('carte_du_monde', 'Carte')]],
        'vocab': {'titres': vb['titres_et_fonctions'], 'evenements': vb['evenements'], 'note': vb['note'], 'st': st(vb['statut_decision'])},
        'arthurien': P['arthurien']['decide'],
    }
HOME = _home()


def _persos():
    per = {p['nom']: p for p in P['personnages_edenia']}
    rv = {r['pour']: r for r in P['esthetique_vestimentaire']['references_visuelles']}
    b = per['Brann']['goal']
    return [
        {'nom': 'Cosmo Dumas', 'go': 'personnages/cosmo-dumas', 'insp': per['Cosmo Dumas']['inspire_de'],
         'ligne': 'Tenue : ' + rv['Cosmo Dumas']['image'] + ', ' + rv['Cosmo Dumas']['role'] + '.', 'st': None},
        {'nom': 'Brann', 'go': 'personnages/brann', 'insp': per['Brann']['inspire_de'],
         'ligne': 'Goal : « ' + b['valeur'] + ' ».', 'st': st_of(b['statut_decision'])},
        {'nom': 'Harley Delphine', 'go': 'personnages/harley-delphine', 'insp': per['Harley Delphine']['inspire_de'],
         'ligne': 'Nom provisoire. Personnage pas encore défini.', 'st': None},
    ]
HOME['persos'] = _persos()


def _ouverts():
    sm = P['structure_du_monde']; oc = P['occultisme']; hm = P['heritages_melanges']; am = P['ambiance_des_lieux']
    cap = lambda s: s[0].upper() + s[1:]
    return [
        {'t': 'Échelle du monde', 'txt': cap(sm['echelle']['texte']) + '.', 'go': 'univers/structure-du-monde'},
        {'t': 'Modèle de monde', 'txt': cap(sm['modele_de_monde']['texte']) + '.', 'go': 'univers/structure-du-monde'},
        {'t': 'Héritages mélangés', 'txt': cap(hm['statut']) + '.', 'go': 'univers/heritages-melanges'},
        {'t': 'Occultisme', 'txt': cap(oc['statut']) + '.', 'go': 'univers/occultisme'},
        {'t': 'Vocabulaire des paysages', 'txt': cap(am['a_preciser']) + '.', 'go': 'lieux/foret-de-conte'},
        {'t': 'Harley', 'txt': 'Nom provisoire ; personnage pas encore défini (12 oct.).', 'go': 'personnages/harley-delphine'},
    ]
HOME['ouverts'] = _ouverts()
