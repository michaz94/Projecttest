"""Catégorie « Recherches » (21 oct.) : articles de RECHERCHE, de brouillon et d'exploration de concepts.
Demande de l'utilisateur : ces pages sont des pages d'influence ou de référence ; elles ne doivent pas être
confondues avec les pages canon, semi-canon ou directement liées à l'univers d'Edenia.
- statut propre « hc » (Hors canon) : ce n'est pas un statut du YAML, qui reste la seule source des statuts ;
- bandeau « Page de recherche · hors canon » en tête de chaque article (corps.html) ;
- chaque affirmation renvoie à une source numérotée ; les sources faibles sont signalées.
Contenu : recherches du 21 oct. (Terre Gaste, puis Terre Déserte)."""
from donnees_yaml import e, bd
from donnees_articles import art, L, ALL

# Clés utilisées pour les liens croisés (les lieux arthuriens envisagés sont générés dans template.html)
ALL.update({'recherches/terre-gaste': {'t': 'Terre Gaste'}, 'recherches/terre-deserte': {'t': 'Terre Déserte'},
            'lieux/la-terre-deserte': {'t': 'La Terre Déserte'}, 'lieux/benoic': {'t': 'Bénoïc'},
            'lieux/gaunes': {'t': 'Gaunes'}, 'lieux/trebes': {'t': 'Trèbes'}})


def refs(lst):
    """lst : (clé, titre, url, faible). Renvoie (r, html) : r('a', 'b') -> « [1][4] »."""
    idx = {k: i + 1 for i, (k, *_ ) in enumerate(lst)}
    def r(*ks):
        return '<sup class="ref">' + ''.join(f'[{idx[k]}]' for k in ks) + '</sup>'
    lis = ''.join(f'<li>{t}{" <span class=\"ref-faible\">source faible</span>" if f else ""}<br>'
                  f'<a class="ref-url" href="{u}" target="_blank" rel="noopener">{e(u)}</a></li>' for k, t, u, f in lst)
    return r, f'<ol class="refs">{lis}</ol>'


def tab(head, rows):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="rtab-w"><table class="rtab"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


RECHERCHES = []

# ================================================================== TERRE GASTE
RG = [
    ('wikt', 'Wiktionnaire, « gast » (ancien français).', 'https://fr.wiktionary.org/wiki/gast', False),
    ('deaf', 'DEAF (Dictionnaire étymologique de l\'ancien français), lemme « gast ».', 'https://deaf.hadw-bw.de/lemme/gast', False),
    ('dect', 'DÉCT (Dictionnaire électronique de Chrétien de Troyes, ATILF), « gast ».', 'http://atilf.atilf.fr/scripts/dect.exe?BASE_LEXIQUE%3BSANS_MENU%3BAFFICHAGE=2%3BVED%3Dgast1', False),
    ('gast', 'Wikipédia (fr), « Le Gast ».', 'https://fr.wikipedia.org/wiki/Le_Gast', False),
    ('gatine', 'Wikipédia (fr), « Gâtine ».', 'https://fr.wikipedia.org/wiki/G%C3%A2tine', False),
    ('etym', 'Online Etymology Dictionary, « waste ».', 'https://www.etymonline.com/word/waste', False),
    ('mela', 'M.-P. Suárez, « Tierras baldías y otros espacios », revue CEMyR (Univ. de La Laguna), 2025.', 'https://www.ull.es/revistas/index.php/cemyr/article/download/2025-10-B/4874/', False),
    ('percen', 'Wikipédia (en), « Perceval, the Story of the Grail ».', 'https://en.wikipedia.org/wiki/Perceval,_the_Story_of_the_Grail', False),
    ('bnfimg', 'BnF Essentiels, « Arrivée de Perceval au château du Graal et Cortège du Graal » (Français 12577).', 'https://essentiels.bnf.fr/fr/image/894c83dc-e167-4bb1-83ae-2fe21121fca2-arrivee-perceval-chateau-graal-et-cortege-graal', False),
    ('ws', 'Chrétien de Troyes, <i>Perceval ou le conte du Graal</i>, texte établi par G. Baist (1911), Wikisource.', 'https://fr.wikisource.org/wiki/Perceval_ou_le_conte_du_Graal', False),
    ('bfm', 'Base de français médiéval (ENS de Lyon), <i>Conte du Graal</i>, éd. Kunstmann (vers numérotés).', 'http://txm.ish-lyon.cnrs.fr/bfm/pdf/PercevalKu.pdf', False),
    ('frperc', 'Wikipédia (fr), « Perceval ».', 'https://fr.wikipedia.org/wiki/Perceval', False),
    ('univ', 'Encyclopædia Universalis, « Perceval ».', 'https://www.universalis.fr/encyclopedie/perceval/', False),
    ('mathey', 'L. Mathey-Maille, « Le Roi Pêcheur dans quelques récits médiévaux » (Univ. du Havre, PDF).', 'https://gric.univ-lehavre.fr/IMG/pdf/mathey-2.pdf', False),
    ('roipe', 'Wikipédia (fr), « Roi pêcheur ».', 'https://fr.wikipedia.org/wiki/Roi_p%C3%AAcheur', False),
    ('waste', 'Wikipédia (en), « Wasteland (mythology) ».', 'https://en.wikipedia.org/wiki/Wasteland_(mythology)', False),
    ('eluc', 'Wikipédia (en), « Elucidation (poem) ».', 'https://en.wikipedia.org/wiki/Elucidation_(poem)', False),
    ('pur', 'OpenEdition Books (Presses universitaires de Rennes), chapitre citant l\'<i>Élucidation</i>.', 'https://books.openedition.org/pur/29237', False),
    ('perlfr', 'Wikipédia (fr), « Perlesvaus ».', 'https://fr.wikipedia.org/wiki/Perlesvaus_ou_Haut_livre_du_Graal', False),
    ('rlr', '« Repenser le Perlesvaus : le sens de l\'équivoque », <i>Revue des langues romanes</i>.', 'https://journals.openedition.org/rlr/2611', False),
    ('queste', 'Wikipédia (de), « Queste del Saint Graal ».', 'https://de.wikipedia.org/wiki/Queste_del_Saint_Graal', False),
    ('gallica', '<i>The Romanic Review</i> (Gallica), passage sur Brulans et Lambor.', 'https://gallica.bnf.fr/ark:/12148/bpt6k11822x', False),
    ('bnfq', 'BnF Essentiels, « La Quête du Saint Graal » (Français 343, fol. 23v).', 'https://essentiels.bnf.fr/fr/litterature/moyen-age-1/ed6c3713-b2d5-4b94-8cac-a35fbd9471b1-mythe-arthurien/livre-feuilleter/27628493-70d1-4511-be19-00f0984b2b90-quete-saint-graal', False),
    ('fisher', 'Wikipédia (en), « Fisher King ».', 'https://en.wikipedia.org/wiki/Fisher_King', False),
    ('dolo', 'Wikipédia (en), « Dolorous Stroke ».', 'https://en.wikipedia.org/wiki/Dolorous_Stroke', False),
    ('malory', 'Thomas Malory, <i>Le Morte d\'Arthur</i>, vol. 1, livre II, ch. XV–XVI (Project Gutenberg).', 'https://www.gutenberg.org/ebooks/1251', False),
    ('parsifal', 'Wikipédia (en), « Parsifal ».', 'https://en.wikipedia.org/wiki/Parsifal', False),
    ('bnf5', 'BnF Essentiels, « Cinq chevaliers emblématiques de la Table ronde ».', 'https://essentiels.bnf.fr/fr/litterature/moyen-age-1/ed6c3713-b2d5-4b94-8cac-a35fbd9471b1-mythe-arthurien/article/b43c7b77-7269-4231-b8fd-c793127007da-cinq-chevaliers-emblematiques-la-table-ronde', False),
    ('percfr', 'Wikipédia (fr), « Perceval ou le Conte du Graal ».', 'https://fr.wikipedia.org/wiki/Perceval_ou_le_Conte_du_Graal', False),
    ('zrp', '<i>Zeitschrift für romanische Philologie</i>, 2019 (De Gruyter), article zrp-2019-0055.', 'https://www.degruyter.com/document/doi/10.1515/zrp-2019-0055/html', False),
    ('eliot', 'Wikipédia (en), « The Waste Land ».', 'https://en.wikipedia.org/wiki/The_Waste_Land', False),
    ('vaine', 'Wikipédia (fr), « La Terre vaine ».', 'https://fr.wikipedia.org/wiki/La_Terre_vaine', False),
    ('exc', 'Wikipédia (en), « Excalibur (film) ».', 'https://en.wikipedia.org/wiki/Excalibur_(film)', False),
    ('rio', 'Wikipédia (fr), « Michel Rio (écrivain) ».', 'https://fr.wikipedia.org/wiki/Michel_Rio_(%C3%A9crivain)', False),
    ('route', 'Wikipédia (fr), « La Route (roman) ».', 'https://fr.wikipedia.org/wiki/La_Route_(roman)', False),
    ('tdfr', 'Wikipédia (fr), « Terre Déserte ».', 'https://fr.wikipedia.org/wiki/Terre_D%C3%A9serte', False),
]
r, REFS_G = refs(RG)

RECHERCHES.append(art('recherches', 'Terre Gaste', 'arthurien', 'hc',
    'Le pays stérile du Roi Pêcheur : origine du mot, textes, causes, remèdes, interprétations, postérité.',
    'La <b>Terre Gaste</b> (« terre dévastée », aussi appelée <b>Terre désolée</b> ; en anglais <i>Waste Land</i>) est, dans la '
    'légende arthurienne, le pays devenu stérile qui entoure le château du Graal. Son sort est lié à la blessure du '
    '<b>Roi Pêcheur</b> (le Roi Méhaigné, « infirme ») : la terre ne retrouvera sa fertilité qu\'à la fin de la quête du Graal, '
    'qui guérira le roi en même temps que son royaume.' + r('gatine', 'roipe'),
    [('Nom et origine du mot', [
        '<i>Gaste</i> est le féminin de l\'ancien français <i>gast</i> : « dévasté, ruiné, désert, vide ».' + r('wikt') +
        ' Le mot vient du latin <i>vastus</i>, croisé avec le francique <i>*wōst-</i> (« désert »), ce qui explique le <i>g-</i> du début.' + r('deaf', 'gast'),
        'La même famille donne <i>gâter</i>, <i>dégât</i> et <i>gâtine</i>, qui désignait un « terrain inculte, inhabité », mais aussi « le pillage, la ruine ».' + r('gatine') +
        ' On la retrouve dans des noms de lieux comme Le Gast, attesté <i>Guastum</i> en 1175.' + r('gast') +
        ' L\'anglais <i>waste</i> a la même origine.' + r('etym'),
        'Chez Chrétien de Troyes, le dictionnaire du DÉCT range <i>gaste</i> au sens de « désolé, désert », en parlant d\'un lieu.' + r('dect') +
        ' Charles Méla, dans son adaptation en français moderne du manuscrit de Berne (1990), traduit <i>terre gaste</i> par « désert ».' + r('mela')]),
     ('Chez Chrétien de Troyes', [
        '<i>Perceval ou le Conte du Graal</i> date des années 1180 ou 1190 ; il est inachevé, peut-être à cause de la mort de son '
        'commanditaire, Philippe de Flandre, en 1191.' + r('percen') + ' La BnF donne « vers 1181-1185 ».' + r('bnfimg'),
        '<b>La Gaste Forêt.</b> Le mot apparaît dès le début : Perceval est « li filz a la veve dame / de la Gaste Forest soutainne ».' + r('ws') +
        ' Sa mère l\'a élevé dans un manoir isolé au milieu de cette forêt « gaste » (stérile) pour l\'éloigner de la chevalerie.' + r('frperc'),
        '<b>Beaurepaire.</b> Autour du château de Blancheflor, assiégé et affamé, Perceval ne voit « fors mer et eve et terre gaste » '
        '(v. 1707 dans l\'édition Kunstmann) ; à l\'intérieur, les rues sont vides et les maisons en ruine, « que home ne fame n\'i avoit ».' + r('bfm', 'dect'),
        '<b>Le château du Roi Pêcheur.</b> Perceval voit passer le cortège du Graal mais n\'ose pas demander qui l\'on sert. Ces questions '
        'auraient guéri le roi infirme et rendu la prospérité à la Terre Gaste.' + r('bnfimg') + ' Sa cousine le lui reproche : s\'il avait '
        'demandé, le roi « fust ores gariz de sa plaie / et si tenist sa terre an pes, / dom il ne tanra point jamés ».' + r('ws'),
        'Selon le texte, ce silence vient du péché de Perceval envers sa mère, morte de chagrin à son départ.' + r('univ', 'mathey') +
        ' Chrétien n\'explique pas la blessure du roi.' + r('roipe') + ' Pour Laurence Mathey-Maille, les terres dévastées, les jeunes '
        'filles abandonnées et les chevaliers morts évoqués par la Demoiselle hideuse « préfigurent » le motif de la Terre Gaste.' + r('mathey')]),
     ('Continuations et Élucidation', [
        '<b>Première Continuation</b> (anonyme) : Gauvain guérit la terre en partie, mais il n\'est pas destiné à achever sa restauration.' + r('waste'),
        '<b>Élucidation</b> : poème anonyme du début du XIIIᵉ siècle (484 vers), écrit comme prologue du <i>Perceval</i> et conservé dans un seul '
        'manuscrit, à Mons.' + r('eluc') + ' Il donne une autre cause : les demoiselles des puits offraient à boire et à manger aux voyageurs, '
        'jusqu\'à ce que le roi Amangon les viole et emporte leurs coupes d\'or. Le pays devient stérile, et le château du Roi Pêcheur '
        'reste longtemps introuvable.' + r('eluc') + ' « Li roiaume si agasti / K\'ains puis n\'i ot arbre fueilli. »' + r('pur')]),
     ('Perlesvaus', [
        'Roman anonyme de la première moitié du XIIIᵉ siècle.' + r('perlfr') + ' Il s\'ouvre sur le silence du héros, rendu responsable du '
        'malheur du Roi Pêcheur. La Demoiselle Chauve explique que, parce qu\'il n\'a pas demandé « qui on servoit », « totes les terres '
        'en furent commeües de guerre ».' + r('rlr'),
        'Mais dans la branche VIII, le Roi Pêcheur meurt avant que Perlesvaus ait pu lui parler : ici, la question n\'est pas indispensable.' + r('rlr')]),
     ('Cycle Vulgate (Lancelot-Graal)', [
        'Dans la <i>Queste del Saint Graal</i>, la sœur de Perceval raconte l\'origine du nom. Pendant une guerre entre le roi Lambar, père '
        'du Roi Méhaigné, et le roi Varlan, Varlan frappe Lambar avec l\'épée trouvée sur la nef ; tout le pays est dévasté et prend le nom '
        'de Terre Gaste.' + r('queste'),
        'Dans un passage cité par <i>The Romanic Review</i>, les noms sont Brulans et Lambor : la terre de Galles ne donne plus ni blé, ni '
        'fruits, ni poissons, « por ce fu elle puis apelee la terre gaste ».' + r('gallica'),
        'Dans la <i>Queste</i>, la tante de Perceval, devenue recluse, est l\'ancienne « reine de la Terre Gaste ».' + r('bnfq') +
        ' Dans ce cycle, le lien entre la terre dévastée et le roi blessé n\'est plus absolu.' + r('waste')]),
     ('Post-Vulgate et Malory : le coup douloureux', [
        'Le roi blessé s\'appelle Pellehan (Pellam chez Malory). Balin, privé d\'arme, saisit une lance pour se défendre et frappe le roi. '
        'C\'est la lance de Longin, qui a percé le flanc du Christ : Pellam et sa terre en souffriront jusqu\'à la venue de Galaad.' + r('fisher') +
        ' Balin a ignoré une voix qui le mettait en garde.' + r('dolo'),
        'Chez Malory (vers 1470), le coup détruit trois pays (« three countries »).' + r('malory', 'roipe') +
        ' Le Post-Vulgate insiste davantage sur la blessure de Pellehan que sur la dévastation de son royaume.' + r('waste')]),
     ('Wolfram von Eschenbach', [
        'Dans <i>Parzival</i> (vers 1205), le roi s\'appelle Anfortas. Sa blessure, explicitement aux parties génitales, punit un amour pour '
        'une femme qui ne lui était pas destinée.' + r('fisher', 'dolo') + ' Wagner reprend cette histoire dans son opéra <i>Parsifal</i> (1882).' + r('parsifal')]),
     ('Tableau récapitulatif', [tab(['Texte', 'Date', 'Roi', 'Cause', 'Remède'], [
        ['Chrétien, <i>Perceval</i>', 'v. 1180–1190', 'Roi Pêcheur (sans nom)', 'Blessure inexpliquée ; silence de Perceval', 'Poser la question'],
        ['Première Continuation', 'v. 1190–1200', 'Roi Pêcheur', '—', 'Gauvain guérit la terre en partie'],
        ['<i>Élucidation</i>', 'début XIIIᵉ s.', 'Roi Pêcheur', 'Viol des demoiselles des puits par Amangon', 'Quête des chevaliers d\'Arthur'],
        ['<i>Perlesvaus</i>', '1ʳᵉ moitié XIIIᵉ s.', 'Roi Pêcheur', 'Silence de Perlesvaus', 'Aucun : le roi meurt avant'],
        ['<i>Queste</i> (Vulgate)', 'début XIIIᵉ s.', 'Lambar, père du Roi Méhaigné', 'Coup d\'épée de Varlan', 'Galaad'],
        ['Post-Vulgate ; Malory', '— ; v. 1470', 'Pellehan / Pellam', 'Coup douloureux de Balin', 'Galaad'],
        ['Wolfram, <i>Parzival</i>', 'v. 1205', 'Anfortas', 'Amour interdit', 'La question de Parzival'],
     ]) + '<p class="rtab-note">Dates : ' + r('fisher', 'percen', 'eluc', 'perlfr', 'roipe') + '. Remède de la Vulgate : Galaad « ramènera à la vie la Terre désolée ».' + r('roipe') + '</p>']),
     ('Interprétations', [
        '<b>Un motif celtique.</b> Une terre stérile, liée à une malédiction qu\'un héros doit lever : on le trouve dans la mythologie '
        'irlandaise. Dans l\'<i>Echtrae Airt meic Cuinn</i>, la terre du roi Conn devient stérile quand il épouse la mauvaise Bé Chuma.' + r('waste'),
        '<b>Le roi et la souveraineté.</b> « Le roi est blessé et la souveraineté de son royaume est anéantie » (BnF).' + r('bnf5') +
        ' Wikipédia rapproche le Roi Pêcheur du Dagda irlandais et voit dans la Terre Gaste « la désolation des anciens temps, voués au paganisme ».' + r('roipe') +
        ' Selon Philippe Jouët, le roi méhaigné représenterait un cycle temporel et politique à son déclin.' + r('percfr'),
        '<b>Une lecture chrétienne.</b> Chez Chrétien, c\'est le péché de Perceval envers sa mère qui l\'empêche de parler.' + r('univ') +
        ' Chez Robert de Boron, le Roi Pêcheur peut être assimilé au Christ souffrant, le « pêcheur d\'hommes ».' + r('mathey') +
        ' Un article de 2019 lit les causes de la dévastation selon un schéma du péché originel.' + r('zrp'),
        '<b>La thèse de Jessie Weston</b> (<i>From Ritual to Romance</i>, 1920) : le motif viendrait d\'un culte païen de la fertilité, '
        'jamais attesté. Le livre est aujourd\'hui largement écarté.' + r('waste')]),
     ('Postérité', [
        '<b>T. S. Eliot</b>, <i>The Waste Land</i> (1922, 433 vers). Dans sa première note, il attribue le titre au livre de Weston ; en 1956, '
        'il désavoue cette piste, qui aurait encouragé une « fausse érudition » (« bogus scholarship »).' + r('eliot') +
        ' En français : <i>La Terre vaine</i>, parfois <i>La Terre Gaste</i>.' + r('vaine'),
        '<b>John Boorman</b>, <i>Excalibur</i> (1981) : Arthur devient le roi blessé, et son royaume une terre gaste. Perceval obtient le Graal '
        'en répondant à l\'énigme : le roi et la terre ne font qu\'un.' + r('waste', 'exc'),
        '<b>En français</b> : <i>La Terre Gaste</i>, dialogue philosophique de Michel Rio ;' + r('rio') + ' « Le jardin de la Terre gaste », '
        'parcelle du Festival des jardins de Chaumont-sur-Loire imaginée par Jean-Pierre Le Dantec pour illustrer <i>La Route</i> de Cormac McCarthy.' + r('route')]),
     ('À ne pas confondre', [
        f'{L("recherches/terre-deserte")} : le royaume du roi Claudas, ravagé par une guerre d\'Uterpendragon. Wikipédia précise qu\'il ne faut '
        'pas le confondre avec la Terre Gaste, domaine du Roi Pêcheur.' + r('tdfr')]),
     ('Références', [REFS_G])],
    'Recherches du 21 oct. 2026 (web) : encyclopédies, dictionnaires, textes médiévaux, articles universitaires. Voir la section Références.',
    'terre-gaste', prose=True,
    ib=[['Autres noms', 'Terre désolée ; <i>Waste Land</i> (anglais)'], ['Type', 'Motif littéraire, royaume légendaire'],
        ['Souverain', 'Le Roi Pêcheur (Roi Méhaigné) ; selon les textes : Lambar, Pellehan/Pellam, Anfortas'],
        ['Première mention', 'Chrétien de Troyes, <i>Perceval</i> (v. 1180–1190)'],
        ['Cause', 'Blessure du roi, coup douloureux, faute, silence du héros (selon les textes)'],
        ['Remède', 'La question du Graal ; Galaad (Vulgate)']],
    rel=['recherches/terre-deserte']))

# ================================================================== TERRE DÉSERTE
RD = [
    ('pleiade', '<i>Le Livre du Graal</i>, t. II, <i>Lancelot</i>, « La Marche de Gaule », Bibliothèque de la Pléiade (Gallimard), extrait PDF.', 'https://media.electre-ng.com/extraits/extrait-id/4e1d0ec2b3e182eeb27368bceb6cb16de15ddef188f475fb721afb0928fcc3d2.pdf', False),
    ('pp', 'Paulin Paris, <i>Les Romans de la Table ronde</i>, vol. 3 (adaptation du XIXᵉ s.), Project Gutenberg.', 'https://www.gutenberg.org/cache/epub/45212/pg45212-images.html', False),
    ('ppws', 'Paulin Paris, <i>Les Romans de la Table ronde</i>, vol. 3, Wikisource.', 'https://fr.wikisource.org/wiki/Les_Romans_de_la_Table_ronde_(Paulin_Paris)/Texte_entier/Volume3', False),
    ('jaq', 'L. Jaquiery, « Esthétique de l\'entremêlement dans les portraits du jeune Lancelot et de Claudas de la Terre Déserte », <i>Médiévales</i> 66, 2014.', 'https://journals.openedition.org/medievales/7228', False),
    ('claen', 'Wikipédia (en), « Claudas » (article signalé comme manquant de sources).', 'https://en.wikipedia.org/wiki/Claudas', False),
    ('tdfr', 'Wikipédia (fr), « Terre Déserte ».', 'https://fr.wikipedia.org/wiki/Terre_D%C3%A9serte', False),
    ('liste', 'Wikipédia (fr), « Liste des personnages du cycle arthurien », section Claudas.', 'https://fr.wikipedia.org/wiki/Liste_des_personnages_du_cycle_arthurien', False),
    ('ban', 'Wikipédia (en), « King Ban ».', 'https://en.wikipedia.org/wiki/King_Ban', False),
    ('banfr', 'Wikipédia (fr), « Ban de Bénoïc ».', 'https://fr.wikipedia.org/wiki/Ban_de_B%C3%A9no%C3%AFc', False),
    ('morris', 'William Morris Archive, transcription de « Lancelot of the Lake » (traduction anglaise).', 'http://morrisarchive.lib.uiowa.edu/transcription-lancelot', False),
    ('lg', 'Wikipédia (fr), « Lancelot-Graal ».', 'https://fr.wikipedia.org/wiki/Lancelot-Graal', False),
    ('bnfl', 'BnF Essentiels, « Roman de Lancelot » (Français 113, fol. 150v).', 'https://essentiels.bnf.fr/fr/litterature/moyen-age-1/ed6c3713-b2d5-4b94-8cac-a35fbd9471b1-mythe-arthurien/livre-feuilleter/ca9ee60b-3be5-4929-9aaf-ed2c7f1a4cda-roman-lancelot', False),
    ('kiwix', 'Ancienne version de l\'article Wikipédia « Terre Déserte » (copie hors ligne Kiwix), sans source.', 'https://zims-lfr.kiwix.campusafrica.gos.orange.com/wikipedia_fr_all_maxi/A/Terre_D%C3%A9serte', True),
    ('lafr', 'Wikipédia (fr), « Légende arthurienne ».', 'https://fr.wikipedia.org/wiki/L%C3%A9gende_arthurienne', False),
    ('night', 'Nightbringer.se, « Claudas of the Land Laid Waste » (site d\'amateur).', 'https://nightbringer.se/the-legend-of-king-arthur/arthurian-characters/c-arthurian-persons/claudas-of-the-land-laid-waste/', True),
    ('mela', 'M.-P. Suárez, « Tierras baldías y otros espacios », revue CEMyR (Univ. de La Laguna), 2025.', 'https://www.ull.es/revistas/index.php/cemyr/article/download/2025-10-B/4874/', False),
]
r, REFS_D = refs(RD)

RECHERCHES.append(art('recherches', 'Terre Déserte', 'arthurien', 'hc',
    'Le royaume du roi Claudas, au Berry, ravagé par Uterpendragon : origine du nom, histoire, Claudas, localisation.',
    'La <b>Terre Déserte</b> (ou <b>la Déserte</b>) est, dans la légende arthurienne, le royaume du <b>roi Claudas</b>, seigneur de Bourges. '
    'Le <i>Lancelot en prose</i> la place « du côté du Berry », à côté des royaumes de Ban de Bénoïc et de Bohort de Gaunes. Son nom vient '
    'd\'une guerre : Uterpendragon, le père d\'Arthur, l\'a ravagée.' + r('pleiade') + ' Il ne faut pas la confondre avec la Terre Gaste, '
    'domaine du Roi Pêcheur.' + r('tdfr'),
    [('Nom', [
        'En ancien français : « la terre del regne Claudas, qui estoit apelee deserte, estoit toute desertie par le roi Uterpandragon et par '
        'Arramont ». La traduction de la Pléiade rend <i>desertie</i> par « dévastée ».' + r('pleiade') + ' Il ne s\'agit donc pas d\'un désert '
        'de sable, mais d\'une terre vidée par la guerre. Le sens est proche de <i>gaste</i> : Charles Méla traduit d\'ailleurs <i>terre gaste</i> '
        'par « désert ».' + r('mela'),
        'Selon l\'adaptation de Paulin Paris, le Berry fut si dévasté « qu\'elle perdit son nom pour prendre celui de <i>la Déserte</i> ».' + r('pp') +
        ' En anglais : « Land Laid Waste ».' + r('claen')]),
     ('Le texte source', [
        'La Terre Déserte apparaît surtout au début du <i>Lancelot en prose</i>, dans la partie appelée « La Marche de Gaule ».' + r('pleiade') +
        ' Ce roman fait partie du <i>Lancelot-Graal</i> (ou cycle Vulgate), dont les textes remontent pour l\'essentiel au début du XIIIᵉ siècle.' + r('lg'),
        'Le récit présente Ban comme ayant « un voisin dont les terres, qui jouxtaient les siennes du côté du Berry, se nommaient alors la '
        'Terre Déserte. Ce voisin s\'appelait Claudas, et il était roi de Bourges et du pays environnant ».' + r('pleiade')]),
     ('Origine : la guerre d\'Uterpendragon', [
        '<b>Le refus d\'hommage.</b> Arramont, surnommé Hoël, seigneur de Petite-Bretagne, était le suzerain de Gaunes, de Bénoïc et de tout '
        'le territoire jusqu\'à la marche d\'Auvergne et de Gascogne ; il aurait dû l\'être aussi du royaume de Bourges. Mais Claudas a fait '
        'hommage au roi de Gaule, « que l\'on appelle désormais France ». La Gaule payait alors tribut à Rome, et « tous les rois étaient par élection ».' + r('pleiade'),
        '<b>L\'appel à Uterpendragon.</b> Soutenu par le roi de Gaule, Claudas tient tête à Arramont dans une guerre qui n\'en finit pas. '
        'Arramont se fait alors l\'homme d\'Uterpendragon, roi de Grande-Bretagne, à condition qu\'il l\'aide. Uterpendragon traverse la mer avec son armée.' + r('pleiade'),
        '<b>La dévastation.</b> Les Bretons battent Claudas, lui prennent sa terre et l\'en chassent, après l\'avoir si bien dévastée « qu\'il '
        'n\'y resta pierre sur pierre de ses forteresses ». <b>Seule Bourges est épargnée</b>, sur ordre d\'Uterpendragon, « lequel se '
        'souvenait d\'y avoir passé son enfance » (« norris des s\'enfance »).' + r('pleiade') +
        ' La traduction anglaise de William Morris dit « born therein », « qu\'il y était né ».' + r('morris'),
        'Ensuite, la Petite-Bretagne est soumise à la Grande.' + r('pleiade')]),
     ('La revanche de Claudas', [
        'Après la mort d\'Arramont et d\'Uterpendragon, Arthur doit affronter la révolte de ses barons. Claudas, qui a reconstruit sa terre, '
        'en profite pour attaquer Ban de Bénoïc, son voisin et vassal d\'Arthur. Un grand seigneur venu de Rome, Ponce Antoine, l\'aide avec '
        'les forces de Gaule.' + r('pleiade'),
        'Claudas achète le sénéchal de Ban en lui promettant des terres, s\'empare de Bénoïc et la brûle. Ban, qui fuit avec sa femme et son '
        'fils, meurt de chagrin en voyant sa ville en flammes. La Dame du Lac enlève alors le bébé Lancelot.' + r('jaq') +
        ' D\'autres résumés parlent du château de Ban, Trèbe, situé au milieu d\'un marais réputé imprenable, que Claudas parvient à incendier.' + r('ban', 'banfr'),
        'Claudas écrase aussi Bohort de Gaunes, frère de Ban. Il enferme ses deux fils, Lionel et Bohort, dans une tour.' + r('jaq') +
        ' Il tient ensuite en paix les trois royaumes de Bourges, de Gaunes et de Bénoïc.' + r('ppws')]),
     ('La fin de Claudas', [
        'Devenus grands, Lionel et Bohort tuent Dorin, le fils de Claudas, puis rejoignent Lancelot chez la Dame du Lac. Des années plus tard, '
        'Claudas emprisonne un cousin de Guenièvre : Arthur, Bohort et Lionel le battent et reprennent les terres de Ban, de Bohort et toutes '
        'celles que Claudas avait conquises. Le vieux roi part à Rome, en disgrâce.' + r('claen'),
        'Un autre fils, Claudin, devient un chevalier vertueux et fait partie des rares chevaliers qui voient le Graal.' + r('claen')]),
     ('Claudas, le personnage', [
        '<b>Caractère.</b> « Un très bon chevalier, très avisé, mais félon ».' + r('pleiade'),
        '<b>Portrait.</b> Le texte oppose une tête laide à un corps parfait : visage et yeux noirs, yeux écartés, cheveux roux et noirs, grande '
        'bouche, dents acérées, pilosité. Pour Ludivine Jaquiery, tout évoque « l\'homme sauvage » ; Claudas est « mi-beau, mi-monstrueux », '
        'une sorte de « patchwork », construit en miroir du jeune Lancelot.' + r('jaq'),
        '<b>Une visite incognito.</b> Après son portrait, Claudas se rend incognito à la cour d\'Arthur pour juger si sa réputation est méritée.' + r('jaq'),
        '<b>Apparitions.</b> D\'abord dans le <i>Perlesvaus</i> et la Seconde Continuation du <i>Perceval</i>, puis surtout dans le '
        '<i>Lancelot-Graal</i> et le <i>Merlin</i> de la Vulgate.' + r('liste') + ' Aussi dans le Post-Vulgate et chez Malory.' + r('claen') +
        ' Dans le <i>Perlesvaus</i>, il se serait allié à Brian des Îles pour envahir l\'Écosse.' + r('night'),
        '<b>Un modèle historique ?</b> Claudas pourrait s\'inspirer des rois francs Clodion et Clovis ; ses conquêtes ressemblent à celles de '
        'Clovis.' + r('claen') + ' C\'est une hypothèse, rapportée sans source précise.']),
     ('Localisation', [
        '<b>Le Berry</b> : c\'est la lecture dominante. Le texte parle de Bourges et de terres « devers Berri », et Claudas est dit seigneur '
        'de Bourges et de « la Berrie ».' + r('pleiade', 'tdfr'),
        '<b>Autres hypothèses, sans source solide</b> : une ancienne version de l\'article Wikipédia proposait le sud de l\'embouchure de la '
        'Loire (Vendée, Pays de la Loire) ou le Gâtinais, « car ce nom signifie terrain inculte ».' + r('kiwix') + ' L\'article « Légende '
        'arthurienne » relève des villages « du Désert » autour de la forêt d\'Andaine, en Normandie.' + r('lafr')]),
     ('Terre Déserte et Terre Gaste', [tab(['', 'Terre Gaste', 'Terre Déserte'], [
        ['Souverain', 'Roi Pêcheur, blessé', 'Claudas, usurpateur'],
        ['Cause', 'Blessure sacrée, faute, coup douloureux', 'Guerre d\'Uterpendragon (punition politique)'],
        ['Nature', 'Stérilité magique liée au corps du roi', 'Dévastation militaire, puis reconstruction'],
        ['Remède', 'La question, le Graal', 'La reconquête par les armes'],
        ['Rôle dans le récit', 'Cœur de la quête du Graal', 'Décor de l\'enfance de Lancelot'],
     ]) + f'<p class="rtab-note">Voir {L("recherches/terre-gaste")}. Tableau de synthèse rédigé par l\'IA à partir des deux articles.</p>']),
     ('Noms repris dans les lieux d\'Edenia (pour information)', [
        f'Le YAML range {L("lieux/la-terre-deserte")}, {L("lieux/benoic")} et {L("lieux/gaunes")} parmi les six lieux arthuriens '
        f'envisagés {bd("envisage")} : tu les as acceptés sans les connaître tous (11 oct.). <b>Cette page ne change pas ce statut</b> et '
        'ne dit rien de ce que ces lieux seront dans Edenia.',
        f'Le château de Ban s\'appelle Trèbe dans ces résumés ; je n\'ai pas vérifié s\'il s\'agit du même nom que {L("lieux/trebes")}.']),
     ('Références', [REFS_D])],
    'Recherches du 21 oct. 2026 (web) : traductions du Lancelot en prose, articles universitaires, encyclopédies. Voir la section Références.',
    'terre-deserte', prose=True,
    ib=[['Autres noms', 'La Déserte ; <i>Land Laid Waste</i> (anglais)'], ['Type', 'Royaume légendaire'],
        ['Souverain', 'Claudas, roi de Bourges'], ['Capitale', 'Bourges (seule cité épargnée)'],
        ['Localisation', 'Le Berry (lecture dominante)'], ['Suzerain', 'Le roi de Gaule (Claudas refuse Arramont)'],
        ['Voisins', 'Bénoïc (Ban), Gaunes (Bohort)'], ['Texte principal', '<i>Lancelot en prose</i> (début XIIIᵉ s.)']],
    rel=['recherches/terre-gaste', 'lieux/la-terre-deserte']))

SUBS_RECHERCHES = {'arthurien': 'Légende arthurienne'}
