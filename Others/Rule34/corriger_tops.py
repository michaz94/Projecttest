# Réécrit les lignes rule34 des top 5 / top 8 selon la règle de l'audit (base = tag principal en autocomplétion
# + gain d'union réel > 150 mesuré par recherche négative). Lignes Danbooru inchangées. Nouveaux fichiers *_audit_*.
import csv
B='/home/user/outil_tags_r34/'
sel={r['personnage']:r for r in csv.DictReader(open(B+'doublons/selection_205_dedupliquee_audit_2026-10-24.csv',encoding='utf-8-sig'))}
def S(nom,label=None):
    r=sel[nom]; m='tag seul' if r['gain_dedup']=='0' else f"tag {int(r['tag_seul_24_10']):,} + gain d’union {r['gain_dedup']}".replace(',', ' ')
    return (label or nom, r['tag'], int(r['publications_dedup']), m+' (sélection auditée)')
def T(nom,tag,base,gain=0,req=''):
    m='tag seul' if gain<=150 else f'tag {base:,} + gain d’union {gain}'.replace(',', ' ')
    if req: m+=f' ({req})'
    return (nom,tag,base+(gain if gain>150 else 0),m)
TOP={
 ('top5_personnages_jjk_fma_hp','Jujutsu Kaisen'):[S('Nobara Kugisaki'),T("Maki Zen'in",'zenin_maki',7300,21,'maki_zenin -zenin_maki ≤ 42'),T('Satoru Gojo','satoru_gojo',5742,105,'alias sans tag principal ≈ 105'),T('Yuji Itadori','itadori_yuuji',4361,21,'alias ≤ 42'),T('Mei Mei','mei_mei_(jujutsu_kaisen)',3718)],
 ('top5_personnages_jjk_fma_hp','Harry Potter'):[T('Hermione Granger','hermione_granger',6943),T('Malfoid (Draco genderswap fan)','draco_malfoy_(redteneri)',3035,21,'malfoid -draco_malfoy_(redteneri) ≤ 42'),T('Harry Potter','harry_james_potter',2043,0,'harry_potter = Copyright'),T('Ginny Weasley','ginny_weasley',1445),T('Luna Lovegood','luna_lovegood',1134)],
 ('top5_personnages_kny_csm_naruto','Demon Slayer'):[S('Mitsuri Kanroji'),S('Shinobu Kocho'),S('Nezuko Kamado'),T('Tanjiro Kamado','kamado_tanjirou',3884,189,'tanjiro_kamado -kamado_tanjirou'),T('Giyu Tomioka','tomioka_giyuu',2614,21,'alias ≤ 42')],
 ('top5_personnages_kny_csm_naruto','Chainsaw Man'):[S('Makima'),T('Power','power_(chainsaw_man)',16185),T('Reze','reze_(chainsaw_man)',9300),S('Kobeni Higashiyama'),T('Denji','denji_(chainsaw_man)',7347)],
 ('top5_personnages_kny_csm_naruto','Naruto'):[S('Hinata Hyûga','Hinata Hyuga'),S('Tsunade'),S('Sakura Haruno'),T('Naruto Uzumaki','uzumaki_naruto',35637,0,'naruto_uzumaki -uzumaki_naruto = 0'),S('Ino Yamanaka')],
 ('top5_personnages_op_mha_lol','One Piece'):[S('Nami'),S('Nico Robin'),S('Boa Hancock'),T('Monkey D. Luffy','monkey_d_luffy',12703,357,'( monkey_d._luffy ~ luffy ) -monkey_d_luffy'),T('Yamato','yamato_(one_piece)',11696)],
 ('top5_personnages_op_mha_lol','My Hero Academia'):[S('Ochako Uraraka'),S('Miruko','Mirko (Miruko)'),T('Izuku Midoriya','izuku_midoriya',27847,651,'midoriya_izuku -izuku_midoriya'),S('Momo Yaoyorozu'),S('Mina Ashido')],
 ('top5_personnages_op_mha_lol','League of Legends'):[S('Ahri'),S('Jinx'),S('Akali'),S('Sona'),T('Lux','luxanna_crownguard',7669,21,'lux_(league_of_legends) -luxanna_crownguard ≤ 42')],
 ('top8_personnages_marvel_dc_nintendo','Marvel'):[T('Spider-Man (Peter Parker)','spider-man',20179,735,'peter_parker -spider-man'),S('Emma Frost'),S('Gwen Stacy','Gwen Stacy (dont Spider-Gwen)'),S('Black Cat (Felicia Hardy)'),T('Venom','venom_(marvel)',13138),S('Femme invisible (Sue Storm)'),S('Black Widow (Natasha Romanoff)'),S('Psylocke (Betsy Braddock / Kwannon)','Psylocke')],
 ('top8_personnages_marvel_dc_nintendo','DC'):[S('Raven'),S('Harley Quinn'),S('Wonder Woman'),S('Starfire'),S('Supergirl'),S('Power Girl'),S('Catwoman (Selina Kyle)'),T('Batman (Bruce Wayne)','batman',9505,113,'alias ≈ +113')],
 ('top8_personnages_marvel_dc_nintendo','Nintendo'):[S('Princesse Peach'),S('Princesse Zelda'),S('Samus Aran'),T('Link','link',32889),S('Harmonie (Rosalina)'),S('Cynthia'),T('Bowser','bowser',21352),S('Marie (Isabelle)')],
}
for fn in ['top5_personnages_jjk_fma_hp','top5_personnages_kny_csm_naruto','top5_personnages_op_mha_lol','top8_personnages_marvel_dc_nintendo']:
    rows=list(csv.DictReader(open(B+f'copyright/{fn}_2026-10-24.csv',encoding='utf-8-sig')))
    cols=list(rows[0].keys()); out=[]
    done=set()
    for r in rows:
        k=(fn,r['franchise'])
        if r['site']=='rule34' and k in TOP and r['rang']!='—':
            if k in done: continue
            done.add(k)
            lst=sorted(TOP[k],key=lambda t:-t[2])
            for i,(nom,tag,pub,m) in enumerate(lst,1):
                out.append({**{c:'' for c in cols},'site':'rule34','franchise':r['franchise'],'rang':str(i),'personnage':nom,'tags':tag,'publications':str(pub),'methode':m,'date':'2026-10-24'})
        else:
            out.append(r)
    if fn.startswith('top8'):
        out.append({**{c:'' for c in cols},'site':'rule34','franchise':'Nintendo','rang':'—','personnage':'Misty (Pokémon)','tags':'kasumi_(pokemon)','publications':'18082','methode':'sortie du top 8 : ancienne union abandonnée (misty_(pokemon) -kasumi_(pokemon) = 0). Recherche directe du 24/10 ≈ 23 163 : compteur de la liste des tags périmé','date':'2026-10-24'})
    with open(B+f'copyright/{fn}_audit_2026-10-24.csv','w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(out)
    print('==',fn)
    for r in out:
        if r['site']=='rule34': print(' ',r['franchise'],r['rang'],r['personnage'],r['publications'],'|',r['methode'][:70])
