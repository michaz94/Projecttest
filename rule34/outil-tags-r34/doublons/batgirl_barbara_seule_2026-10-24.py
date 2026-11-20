# Batgirl = Barbara Gordon seule (décision de l'utilisateur, 24/10/2026). Modifie selection_256 sur place (idempotent) et re-classe.
# Mesure (recherche négative, dernier pid + 21) :
#  ( batgirl ~ barbara_gordon ~ batgirl_(barbara_gordon) ~ batgirl_(gotham_knights) ~ batgirl_(arkham_knight) ~ batgirl_(dcau)
#    ~ batgirl_(the_killing_joke) ~ batgirl_(the_new_batman_adventures) ~ batgirl_(the_batman) ~ barbara_gordon_(shg) ~ barbara_gordon_(gotham_knights) )
#    -cassandra_cain -stephanie_brown -batgirl_(cassandra_cain) -batgirl_(stephanie_brown)   → dernier pid 7854 → ≈ 7 875
#  même union sans les exclusions → dernier pid 9072 → ≈ 9 093 (donc ≈ 1 218 publications retirées car taguées Cassandra Cain ou Stephanie Brown)
import csv
B='/home/user/outil_tags_r34/doublons/'
f=B+'selection_256_dedupliquee_audit_2026-10-24.csv'
dd=list(csv.DictReader(open(f,encoding='utf-8-sig')))
TOT=7875
for r in dd:
    if r['tag']=='batgirl':
        r['personnage']='Batgirl (Barbara Gordon)'
        r['gain_dedup']=str(TOT-int(r['tag_seul_24_10'])); r['publications_dedup']=str(TOT)
        r['methode']='Barbara Gordon seule (décision du 24/10)'
        r['mesure_gain']=("( batgirl ~ barbara_gordon ~ 9 tags de version de Barbara ) -cassandra_cain -stephanie_brown -batgirl_(cassandra_cain) "
                          "-batgirl_(stephanie_brown) ≈ 7 875 ; les publications de batgirl sans nom restent comptées (surtout Barbara, non vérifiable)")
ts=sorted(dd,key=lambda r:-int(r['tag_seul_24_10'])); rts={id(r):i+1 for i,r in enumerate(ts)}
dd.sort(key=lambda r:-int(r['publications_dedup']))
for i,r in enumerate(dd):
    r['rang_dedup']=str(i+1)
    if r['effet_dedup']!='ajout': r['rang_tag_seul_24_10']=str(rts[id(r)]); r['effet_dedup']=str(rts[id(r)]-(i+1))
with open(f,'w',newline='',encoding='utf-8-sig') as o:
    w=csv.DictWriter(o,fieldnames=list(dd[0].keys())); w.writeheader(); w.writerows(dd)
print([(r['rang_dedup'],r['personnage'],r['publications_dedup']) for r in dd if r['tag']=='batgirl'])
