# Produit le top 50 des personnages Xbooru (union des variantes de nom, relevé du 24/10/2026).
import json,csv
d=json.load(open("unions.json"))
L=sorted(d.items(),key=lambda x:-x[1]["union"])
date="2026-10-24"
f=lambda x:f"{x:,}".replace(","," ")
with open(f"top50_personnages_xbooru_{date}.csv","w",newline="",encoding="utf-8-sig") as o:
    w=csv.writer(o); w.writerow(["rang","personnage","franchise","sexe","publications","tag_principal","publications_tag_principal","gain_variantes","tags_fusionnes","date_releve"])
    for i,(k,v) in enumerate(L,1):
        w.writerow([i if i<=50 else "—",k,v["franchise"],v["sexe"],v["union"],v["tags"][0],v["principal"],v["union"]-v["principal"],"|".join(t for t,p in zip(v["tags"],v["parts"]) if p),date])
md=[f"# Top 50 des personnages sur Xbooru ({date})","","Relevé de l'IA. Compteurs en direct par l'API de Xbooru. Un personnage = son tag principal + les publications ajoutées par ses autres noms (calcul par négation, sans double compte).","",
"Exclus car ce ne sont pas des personnages individuels : original_character, humans_of_pokemon, inkling (espèce), character_request, anonymous, pokemon_(creature), fan_character, team_rocket.","",
"| Rang | Personnage | Franchise | Sexe | Publications | dont autres noms |","|---|---|---|---|---|---|"]
for i,(k,v) in enumerate(L[:50],1):
    g=v["union"]-v["principal"]
    md.append(f"| {i} | {k} | {v['franchise']} | {v['sexe']} | {f(v['union'])} | {f(g) if g else ''} |")
md+=["","Juste après : "+" ; ".join(f"{k} {f(v['union'])}" for k,v in L[50:60])]
open(f"top50_personnages_xbooru_{date}.md","w").write("\n".join(md)+"\n")
from collections import Counter
c=Counter(v["franchise"] for k,v in L[:50]); print(c.most_common(12)); print(Counter(v["sexe"] for k,v in L[:50]))
print(sum(v["union"] for k,v in L[:50]))
