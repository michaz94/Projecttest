import json
d=open('donnees_app_2026-10-24.json',encoding='utf-8').read()
s=open('modele.html',encoding='utf-8').read()
assert '/*DATA*/[]' in s
s=s.replace('/*DATA*/[]',d.replace('</','<\\/'))
d2=open('donnees_app_top_danbooru_2026-10-24.json',encoding='utf-8').read()
assert '/*DATA_D*/[]' in s
s=s.replace('/*DATA_D*/[]',d2.replace('</','<\\/'))
d3=open('donnees_franchises_2026-10-24.json',encoding='utf-8').read()
assert '/*DATA_F*/{}' in s
s=s.replace('/*DATA_F*/{}',d3.replace('</','<\\/'))
d5=open('donnees_especes_2026-10-25.json',encoding='utf-8').read()
assert '/*DATA_E*/[]' in s
s=s.replace('/*DATA_E*/[]',d5.replace('</','<\\/'))
d4=open('donnees_copyright_2026-10-25.json',encoding='utf-8').read()
assert '/*DATA_C*/{}' in s
s=s.replace('/*DATA_C*/{}',d4.replace('</','<\\/'))
d6=open('donnees_mal_2026-10-25.json',encoding='utf-8').read()
assert '/*DATA_M*/[]' in s
s=s.replace('/*DATA_M*/[]',d6.replace('</','<\\/'))
open('classement_rule34_danbooru.html','w',encoding='utf-8').write(s)
print(len(s))
