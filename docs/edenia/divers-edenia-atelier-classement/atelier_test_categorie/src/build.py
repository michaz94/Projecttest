"""Assemble Edenia.html (brouillon du wiki d'Edenia dans l'Atelier).
- template.html : CSS d'origine + fiches Lieux écrites à la main (LIEUX, MOOD) + icônes
- css_edenia.css, corps.html : ajouts Edenia (accueil, catégories, routeur)
- donnees_yaml.py : pages Personnages, Folklore, Univers, Œuvres tirées du YAML
Lancer depuis le dossier atelier_test_categorie : python3 src/build.py"""
import json, pathlib, re, sys
D = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(D))
from donnees_yaml import PAGES, CATS_EXTRA, HOME
from donnees_tests import TESTS, SUBS_TESTS
PAGES = PAGES + TESTS
CATS_EXTRA = {**CATS_EXTRA, 'tests': SUBS_TESTS}
from donnees_articles import ARTICLES, SUBS_ARTICLES
PAGES = ARTICLES + PAGES
CATS_EXTRA = {k: {**SUBS_ARTICLES.get(k, {}), **v} for k, v in CATS_EXTRA.items()}
from donnees_recherches import RECHERCHES, SUBS_RECHERCHES   # pages de recherche, hors canon (21 oct.)
PAGES = PAGES + RECHERCHES
CATS_EXTRA['recherches'] = SUBS_RECHERCHES

def bloc(s, debut, fin_txt):
    a = s.index(debut); b = s.index(fin_txt, a) + len(fin_txt)
    return s[a:b]

t = (D/'template.html').read_text()
css = t[t.index('<style>')+7:t.index('</style>')] + (D/'css_edenia.css').read_text()
import base64 as _b64
_LAT='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
_EXT='U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF'
_faces=''
_RUB=json.load(open(D/'polices_rubik.json'))
for _pre,_rng in (('',_LAT),('x',_EXT)):
    for _it,_w in (('',300),('',400),('',700),('i',300),('i',700)):
        _d=_RUB[f'{_pre}{_it}{_w}']
        _faces+=("@font-face{font-family:rubik;font-style:%s;font-weight:%d;font-display:swap;"
                 "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s}\n") % ('italic' if _it else 'normal',_w,_d,_rng)
css += (D/'css_police_fandom.css').read_text().replace('__RUBIK_FACES__', _faces)
head = t[:t.index('<style>')]
head = re.sub(r'<title>.*?</title>', '<title>Edenia — Atelier (brouillon)</title>', head, flags=re.S)
lieux = bloc(t, 'const LIEUX = [', '\n];')
mood = bloc(t, 'const MOOD = [', '\n];')
icon = bloc(t, 'const ICON = {', '};')
J = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
corps = (D/'corps.html').read_text()
corps = (corps.replace('__IMGS__', J({**json.load(open(D/'imgs.json')), **json.load(open(D/'imgs_tests.json')), **json.load(open(D/'imgs_tenues.json'))}))
              .replace('__ICON__', icon).replace('__LIEUX__', lieux).replace('__MOOD__', mood)
              .replace('__SUBS__', J(CATS_EXTRA)).replace('__PAGES__', J(PAGES)).replace('__HOME__', J(HOME)))
out = head + '<style>' + css + '</style>\n</head>\n' + corps
out = out.replace('__ICON_CASTLE__', (D/'icon_castle.svg').read_text())
(D.parent/'Edenia.html').write_text(out)
print('Edenia.html', len(out), 'octets,', len(PAGES), 'pages générées')
