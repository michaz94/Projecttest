"""Ajoute (ou met à jour) la visionneuse d'images dans un fichier HTML. Usage : python3 inject.py fichier.html [...]"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).parent
def block():
    css = (HERE/'lightbox.css').read_text(encoding='utf-8')
    js = (HERE/'lightbox.js').read_text(encoding='utf-8')
    return f'<!--FLB-START--><style>{css}</style><script>{js}</script><!--FLB-END-->'
def inject_str(s):
    s = re.sub(r'<!--FLB-START-->.*?<!--FLB-END-->', '', s, flags=re.S)
    i = s.rfind('</body>')
    b = block()
    return s[:i] + b + s[i:] if i >= 0 else s + b
if __name__ == '__main__':
    for f in sys.argv[1:]:
        p = pathlib.Path(f); p.write_text(inject_str(p.read_text(encoding='utf-8')), encoding='utf-8'); print('ok', f)
