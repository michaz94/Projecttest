import csv
SP=[("Gardevoir","Pokémon (espèce)","gardevoir",41237,"87 %"),("Renamon","Digimon (espèce)","renamon",33274,"87 %"),
    ("Lockpin (Lopunny)","Pokémon (espèce)","lopunny",23999,"92 %"),("Aquali (Vaporeon)","Pokémon (espèce)","vaporeon",18056,"67 %"),
    ("Givrali (Glaceon)","Pokémon (espèce)","glaceon",16462,"69 %")]
def liste():
    r=list(csv.DictReader(open('../doublons/selection_388_dedupliquee_audit_2026-10-25.csv',encoding='utf-8-sig')))
    L=[dict(nom=x['personnage'],univers=x['univers'],tag=x['tag'],n=int(x['publications_dedup']),espece='') for x in r]
    L+=[dict(nom=a,univers=b,tag=c,n=d,espece=e) for a,b,c,d,e in SP]
    L.sort(key=lambda x:-x['n'])
    for i,x in enumerate(L,1): x['rang']=i
    return L
