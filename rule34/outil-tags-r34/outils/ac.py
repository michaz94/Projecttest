# Autocomplétion rule34 (api.rule34.xxx) : affiche les 8 premières propositions (tag (compteur)) pour chaque préfixe.
import sys,json,urllib.request,urllib.parse,html
for q in sys.argv[1:]:
    u='https://api.rule34.xxx/autocomplete.php?q='+urllib.parse.quote(q)
    r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
    print(q,'->',[html.unescape(x['label']) for x in r[:8]])
