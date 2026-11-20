# Raisonnements sur les données personnages (25 octobre 2026)

**Classements, nombres de publications et votes.** Rule34, Danbooru, Safebooru, Xbooru, e621, TierMaker et MyAnimeList. Sections 10 à 13 ajoutées le 25/10 : évolution par période, groupes de titres TierMaker, débat avec l'utilisateur, suites.

**Règle de lecture.** Chaque point donne :
- les **faits** utilisés, tous relevés et reproductibles, avec le fichier source ;
- le **type de raisonnement** ;
- la **force de la conclusion**.

Les hypothèses sont des propositions de l'IA. Ce ne sont pas des faits.

## 0. Base de faits

| Fait | Valeur | Source |
|---|---|---|
| Tags de personnages individuels rule34 ≥ ~5 000 publications (pages 1–390) | 388 féminins, 65 masculins, 17 de genre non défini | `selection_387…`, `autres_tags_personnages_270…` |
| Top féminin / top masculin rule34 | Nami 58 263 / Sonic 37 386 | `app_tri/donnees_app_2026-10-24.json` |
| Concentration dans les 388 féminines | top 10 = 9,6 % des publications ; Gini 0,34 ; pente log-rang/log-compte −0,57 (R² 0,95) | calcul du 25/10 |
| Rule34 vs Danbooru, 388 féminines | Spearman 0,29 | idem |
| Danbooru pour 100 rule34, médiane par médium | Animanga 21 ; Jeux vidéo 29 ; Cartoons 6,9 ; Comics 6,3 ; Furry 3,0 ; Autres 187 | idem |
| Recoupement top 388 rule34 / top 388 Danbooru | 81 personnages en commun (21 %) | idem |
| Top 388 Danbooru par médium | Jeux vidéo 264, Animanga 82, Autres 42, Comics / Cartoons / Furry 0 | `donnees_app_top_danbooru…` |
| 4 premières franchises | Danbooru : Touhou 75 + KanColle 40 + Blue Archive 32 + Hololive 31 = 178 / 388 (46 %). Rule34 : Pokémon 19 + Genshin 17 + LoL 16 + 11 = 63 / 388 (16 %) | idem |
| Ressemblance des classements, 195 personnages | Danbooru ~ Safebooru 0,90 ; rule34 ~ Xbooru 0,48 ; rule34 ~ Danbooru 0,23 ; rule34 ~ e621 0,25 ; Danbooru ~ e621 −0,15 | `comparaison_sites/RAPPORT…` |
| Accord entre deux listes TierMaker individuelles | médiane 0,12 (74 paires) | `tiermaker/RAPPORT_correlation…` |
| TierMaker vs rule34 (périmètre Comics / Cartoons / Furry, 10 votes) | Spearman de 0,30 à 0,48, toujours positif | `tiermaker_cartoons_vs_r34/…` |
| Favoris MAL vs rule34 / Danbooru (33 filles) | −0,08 / 0,20 | `myanimelist/comparaison_feminines…` |
| Top 100 MAL | 65 garçons, 33 filles, 2 indéterminés | `myanimelist/top100…` |
| Part d'images IA sur rule34 (9 personnages) | Marin 68 %, Frieren 65 %, Makima 63 %, Yor 61 %, Hinata 54 %, Nami 53 %, Tsunade 50 %, 2B 33 %, Tifa 29 % | `production_temps/ia_rule34…` |
| Volume du site rule34 | ≈ 6,19 M posts depuis fin nov. 2024, dont ≈ 4,67 M depuis mi-fév. 2026 | `frequence_magik/…` |
| Adaptation anime / film, Danbooru (12 mois avant → 12 mois après, rapporté au site) | Marin ×229, Nezuko ×150, Frieren ×115, Yor ×96, Black Widow ×13, Spider-Gwen ×10, Power ×4,4, Makima ×2,9, Wonder Woman ×2,5 | `effet_adaptation/…` |
| Entrée dans Marvel Rivals (sortie le 06/12/2024), Danbooru en part du site | Magik ×12 (12 mois avant → 12 mois après). Squirrel Girl : de 1 à 563 images, puis −78 % la 2e année | `magik_rivals/…`, `squirrel_girl_rivals/…` |

## 1. Déductions

Une déduction est certaine si ses prémisses sont vraies.

1. **EdeniaList ne dit rien des personnages sous le seuil.** La sélection ne contient que les tags rule34 au-dessus d'environ 5 000 publications. Donc :
   - toute absence d'EdeniaList signifie « moins de ~5 000 sur rule34 » ou « tag non féminin / non individuel » ;
   - elle ne signifie jamais « impopulaire ».

   C'est pour cette raison que Kurisu (1 760) ou Senjougahara (1 390) n'y étaient pas.
2. **« Absente du top 100 TierMaker » ne veut pas dire « mal classée ».** On n'a identifié que le top 100 de chaque vote. Une absence peut venir de trois causes :
   - un rang au-delà de 100 ;
   - une image non identifiée ;
   - un personnage absent du modèle.

   On ne peut donc rien déduire d'une absence, seulement d'une présence.
3. **Les compteurs rule34 sont dominés par le récent.** Environ 4,67 M posts sur les ≈ 6,19 M mis en ligne depuis fin novembre 2024 datent de mi-février 2026 ou après. Donc :
   - une grande partie du stock actuel a moins d'un an ;
   - un compteur total mesure surtout l'activité récente, pas une popularité ancienne cumulée.
4. **Les compteurs bruts rule34 ne mesurent pas que des dessins humains.** Chez les 9 personnages mesurés, 29 à 68 % des publications sont taguées `ai_generated`. Pour Marin, Frieren, Makima et Yor, la majorité du compteur est donc de l'image générée.
5. **Les mesures sont asymétriques.**
   - 17 des 33 filles du top 100 MAL sont dans la sélection rule34 (52 %).
   - À l'inverse, seules 17 des 388 féminines rule34 sont dans le top 100 MAL (4,4 %).

   Ce n'est pas une contradiction. Le top MAL est très petit et très sélectif, alors que la liste rule34 est large.
6. **Le top Danbooru ne contient ni Comics, ni Cartoons, ni Furry.** Un classement « tous médiums » fondé sur Danbooru exclut donc de fait l'animation occidentale. Le comparer à un vote TierMaker « dessins animés » serait biaisé dès le départ.

## 2. Inductions

Une induction généralise à partir de cas observés. Sa conclusion est probable, pas certaine.

1. **Chaque site a son public et son style.** Les observations :
   - Danbooru et Safebooru donnent presque le même ordre (0,90) ;
   - rule34 ressemble surtout à Xbooru (0,48) ;
   - e621 est dominé par MLP, Zootopie et Sonic ;
   - la médiane Danbooru/rule34 va de 3 (Furry) à 187 (Autres, dont Miku et Touhou).

   Généralisation : le nombre de publications mesure **la production d'une communauté précise**, pas une popularité « universelle ». Force : élevée (5 sites, 195 personnages).
2. **Le contenu explicite pèse peu dans le classement Danbooru.** Danbooru accepte aussi des images explicites. Pourtant son ordre est presque celui de Safebooru, qui est tout public (0,90). Généralisation : le classement Danbooru est porté par le fan art non explicite. Force : élevée.
3. **Le goût individuel est très dispersé ; le consensus n'apparaît qu'en agrégeant.**
   - Deux listes TierMaker individuelles s'accordent à 0,12 en médiane.
   - Les classements moyens de 10 votes sont tous corrélés positivement à rule34 (0,30–0,48).

   Généralisation : un vote isolé ne vaut presque rien ; une moyenne de milliers de votants révèle une tendance stable mais modérée. Force : moyenne à élevée.
4. **Une adaptation animée multiplie la production, surtout si le personnage partait de presque rien.**
   - Gros multiplicateurs pour Marin, Frieren, Yor et Nezuko (×96 à ×229, avec 7 à 48 images l'année d'avant).
   - Multiplicateurs plus faibles pour Makima et Power (×2,9 et ×4,4, déjà 512–965 images avant), comme pour Wonder Woman (×2,5).

   Généralisation : l'effet relatif d'une adaptation est d'autant plus fort que la base de départ est petite. Force : moyenne (9 cas, choisis parce qu'ils ont été adaptés, donc biais de sélection).
5. **Un jeu à grande audience fait le même effet qu'une adaptation, mais l'effet retombe.**
   - Magik : ×12 sur Danbooru.
   - Squirrel Girl : de 1 à 563 images, puis −78 % la 2e année.

   Généralisation : une entrée dans un jeu populaire crée un pic, puis un plateau plus bas. Force : faible (2 cas, un seul jeu).
6. **Le rapport filles/garçons s'inverse selon la mesure.**
   - Rule34 : 388 féminines pour 65 masculins au-dessus du seuil.
   - MAL : 65 garçons pour 33 filles dans le top 100.

   Généralisation : les sites d'images (surtout explicites) mesurent l'attrait visuel et sexualisé, alors que les favoris mesurent l'attachement au personnage. Force : moyenne (2 sources, mais écart très net).
7. **La popularité sur rule34 est inégale, mais moins extrême qu'on pourrait le croire au sommet.** Dans les 388 féminines, les 10 premières ne font que 9,6 % du total. La courbe rang/compte suit bien une loi de puissance de pente −0,57.

   Attention : la liste est **tronquée** au seuil. On ne voit que la tête de la distribution, donc la loi complète n'est pas connue.

## 3. Abductions

L'abduction cherche la meilleure explication d'un fait surprenant. Pour chacune : les explications concurrentes, et un moyen de trancher.

### A1. Pourquoi Kurisu est 1re fille sur MAL mais faible sur rule34 et absente des tier lists ?
- **H1 (préférée) : les favoris MAL récompensent l'écriture et l'œuvre**, ici Steins;Gate, très bien notée. Les sites d'images récompensent le design et l'attrait visuel. Le même profil se retrouve chez Senjougahara, Taiga, Violet et Rikka.
- **H2 : un effet d'ancienneté.** L'anime est ancien. Or rule34 est dominé par les 12 derniers mois (déduction 3) et par l'IA, qui vise les personnages récents (voir A3).
- **H3 : peu de fan service officiel**, donc moins de matière pour l'image sexualisée.
- **Pour trancher :** comparer des personnages MAL de même ancienneté mais au design plus sexualisé, comme Rias (2012), qui est forte sur rule34. Si l'ancienneté seule ne suffit pas à faire baisser le compteur, H1 et H3 l'emportent. Indice déjà disponible : Danbooru, qui est surtout tout public, ne place pas non plus Kurisu très haut (4 407). Cela affaiblit H3 et renforce H2.

### A2. Pourquoi Homura (Danbooru 30 350) et Touhou dominent Danbooru, mais pas rule34 ?
- **H1 (préférée) :** Danbooru est alimenté surtout par des illustrateurs japonais, et Touhou comme Madoka y ont une très forte tradition de fan art.
- **H2 :** les personnages très jeunes d'apparence sont filtrés ou moins postés sur rule34.
- **Pour trancher :** regarder Danbooru en notation explicite seulement, ou utiliser le rapport Safebooru/Danbooru. Si Touhou reste aussi haut en explicite, H2 tombe.

### A3. Pourquoi les héroïnes d'anime récentes ont-elles autant de publications rule34 ?
Exemples : Frieren, Marin, Makima, Yor.
- **Fait testé :** chez les 9 personnages mesurés, la part d'IA augmente avec l'année d'apparition sur Danbooru (Spearman 0,71, p = 0,03, n = 9).
- **H1 (préférée) :** la génération par IA gonfle surtout les personnages populaires au moment où cette génération a explosé (2023–2026).
- **H2 :** ces personnages sont simplement plus populaires aujourd'hui.
- **Les deux se combinent probablement.** Une fois l'IA retirée, Marin passe de 29 857 à 9 676 et Tifa de 54 505 à 38 818. L'écart réel entre récentes et anciennes est donc bien plus petit que le compteur brut ne le montre.
- **Limite :** n = 9, et l'année de départ Danbooru est une approximation grossière (2006 est tronqué à gauche).

### A4. Pourquoi les personnages Furry / MLP sont énormes sur rule34 mais mal classés sur TierMaker ?
Exemples : Loona 222e, Judy 578e, poneys entre 854 et 1 111 (vote 87784832).
- **H1 (préférée) :** une communauté de niche très productive. Peu de personnes, mais beaucoup d'images par personne. e621 montre que ces personnages dominent un site spécialisé, mais le nombre d'images par artiste n'est pas mesuré.
- **H2 :** les votants TierMaker grand public sanctionnent les personnages non humains.
- **Pour trancher :** comparer le nombre d'artistes distincts par tag avec le nombre d'images. Ce n'est pas relevé ; il faudrait les tags d'artistes.

### A5. Pourquoi la corrélation TierMaker–rule34 est-elle positive mais seulement modérée ?
- **H1 :** un facteur commun, le design attirant et la notoriété, explique la partie partagée.
- **H2 :** les différences de public expliquent le reste : niches productives (A4), effets de mode, IA.
- La corrélation modérée est exactement ce qu'on attend si les deux mesures partagent un facteur sans s'y réduire.

## 4. Inférences causales

On ne dispose ici que d'observations, pas d'expériences.
- **Adaptations et Marvel Rivals = quasi-expériences.** La date de l'événement est connue de l'extérieur et la hausse arrive juste après. La production est rapportée au volume du site, ce qui neutralise la croissance générale. C'est l'argument causal le plus solide du corpus.
- **Ce qui manque :** un groupe témoin. Il faudrait des personnages comparables non adaptés sur la même période, par exemple d'autres héroïnes Marvel non jouables (She-Hulk ou MJ, absentes du jeu).
- **Piège à éviter :** conclure qu'un personnage est populaire « parce qu'il est attirant » à partir de corrélations seules. Le sens peut être inverse : un personnage populaire est davantage dessiné de façon sexualisée.

## 5. Analogies

Une analogie est probable si les structures se ressemblent.
- **Squirrel Girl → futurs personnages ajoutés à un jeu populaire :** on peut s'attendre à un pic la 1re année, puis à une forte retombée. Force faible tant qu'il n'y a que 2 cas.
- **Rule34 ↔ Xbooru et Danbooru ↔ Safebooru :** des sites au contenu semblable donnent des classements semblables. On peut donc prévoir, sans le mesurer, qu'un site tout public de style japonais classera comme Danbooru.

## 6. Hypothèses réfutées par les données

Il s'agit de falsification : une hypothèse est rejetée quand les données la contredisent.
- **« Les personnages les plus aimés sont les plus dessinés. »** Rejetée pour MAL. ρ = −0,08 avec rule34 et 0,20 avec Danbooru, non significatif.
- **« Un seul classement de popularité existe. »** Rejetée. Danbooru et e621 sont même légèrement opposés (−0,15).
- **« Les votes TierMaker ne sont que du hasard. »** Rejetée. Les 10 votes sont tous corrélés positivement avec rule34.
- **« Un compteur rule34 = des dessins faits par des fans. »** Rejetée. Jusqu'à 68 % des publications sont de l'IA chez les personnages mesurés.

## 7. Raisonnements fautifs à éviter

- **Biais du survivant :** ne regarder que le top 388, alors que la queue n'est pas observée.
- **Erreur écologique :** passer de « Furry est mal classé sur TierMaker » à « chaque votant déteste le Furry ». C'est faux à l'échelle individuelle (accord médian 0,12).
- **Absence de preuve = preuve d'absence :** les absences dans le top 100 TierMaker et les « — » ne valent pas 0.
- **Comparer des compteurs bruts entre époques** sans les rapporter au volume du site.

## 8. Pistes pour Edenia

Ce sont des hypothèses de l'IA, non canon, à valider par toi.
- **Deux leviers distincts.** Les données séparent l'attachement (MAL : écriture, rôle dans l'histoire) de la visibilité visuelle (Danbooru / rule34 / TierMaker : design). Pour une série, ce sont deux objectifs différents ; l'un n'entraîne pas l'autre.
- **Un design très lisible et facile à dessiner** favorise sans doute le fan art. C'est une hypothèse : la lisibilité n'a pas été mesurée ici.
- **Une adaptation ou une apparition dans un jeu** est le déclencheur de production le mieux attesté du corpus.

## 9. Test ajouté : le temps et la part d'IA

Données : `sans_ia/stock_avant_ia_2026-10-25.csv` (script `sans_ia/stock_avant_ia.py`), 25 personnages.

**Méthode.**
- Coupure au post 7 000 000, mis en ligne le 18/11/2022 (ancre vérifiée). Avant cette date, rule34 ne compte qu'environ 8 757 posts tagués `ai_generated` au total.
- Pour chaque personnage : part de son stock publiée avant cette date, et part d'IA dans sa production publiée depuis.

**Résultats.**
- **Plus le stock ancien est grand, plus la part d'IA est faible :** Spearman −0,78 (p < 0,0001). Une partie de ce lien est mécanique : un grand stock humain d'avant 2022 dilue la part d'IA.
- **Le lien tient aussi sur la production récente seule :** −0,62 (p = 0,001). Les personnages « anciens » restent davantage dessinés par des humains aujourd'hui.
- **Le médium joue en plus du temps.** Furry et Jeux vidéo ont la même médiane de stock ancien (41 % et 39 %). Pourtant, depuis novembre 2022, la part d'IA est de 27,5 % en Furry contre 45 % en Jeux vidéo. L'Animanga a le stock ancien le plus faible (23 %) et la part d'IA la plus forte (64,5 %).
- **Cas appariés à stock égal :** Rouge (39 % de stock ancien, 14 % d'IA depuis) contre Tifa (40 % et 48 %). Sakura (40 %) a 64 % d'IA depuis.

**Hypothèses (non testées ici).**
- Les modèles d'IA les plus répandus sont surtout entraînés sur de l'illustration de style anime.
- Les normes de la communauté furry vont contre l'IA, et cette production a un débouché séparé. Exemples : e621 interdit l'IA depuis février 2025 et l'envoie sur e6ai ; r/mylittlepony l'a interdite en décembre 2022.

## 10. Test ajouté : évolution par période sur rule34 (top 20 général TierMaker)

Données : `temporalite/releve_bornes_id.txt` (relevé brut), script `temporalite/parts_par_periode.py`, résultat `temporalite/top20_general_parts_par_periode_2026-10-25.csv`. Ce test répond à l'objection de l'utilisateur : les données cumulées ignorent les pics d'activité, la temporalité et l'évolution.

**Méthode.**
- Les ID de post rule34 sont attribués dans l'ordre chronologique. On compte les posts de chaque personnage sous trois bornes d'ID (`id:<N`), puis on prend le total.
- Ancres :
  - post 2 000 000 = 29/03/2016 et post 4 000 000 = 12/08/2020 (dates lues dans les premiers commentaires des posts « milestone ») ;
  - post 7 000 000 = 18/11/2022 et post 11 927 000 = 06/12/2024 (ancres vérifiées, voir `marvel_rivals/r34_ancres_id_dates_2026-10-24.md`) ;
  - ID max ≈ 19 130 000 le 24/10/2026.
- Périodes : P1 jusqu'à mars 2016 ; P2 avril 2016 – novembre 2022 ; P3 novembre 2022 – décembre 2024 ; P4 décembre 2024 – octobre 2026.
- **Taux** = posts du personnage pour 1 million d'ID attribués pendant la période. Ce taux corrige la croissance du site. C'est une approximation : les posts supprimés gardent leur ID.
- Effectif = pid de la dernière page + 21 (± 21). Total = compteur EdeniaList (relevés du 23 au 25/10).
- P4 a aussi été mesurée sans IA (`-ai_generated`). Mirko, Yor et Marin n'existaient pas avant 2016 : leur effectif P1 est fixé à 0.

**Rang parmi les 20, par période.** « — » = le personnage n'existait pas encore ou presque.

| Personnage | Origine | P1 | P2 | P3 | P4 | P4 sans IA | Part d'IA en P4 |
|---|---|---|---|---|---|---|---|
| Raven | Occident | 6 | 5 | 4 | 9 | 6 | 62 % |
| D.Va | Occident | — | 3 | 10 | 10 | 7 | 60 % |
| Starfire | Occident | 9 | 10 | 13 | 14 | 12 | 66 % |
| Hélène Parr | Occident | 12 | 12 | 15 | 16 | 15 | 63 % |
| Chel | Occident | 14 | 19 | 17 | 17 | 16 | 74 % |
| Jessica Rabbit | Occident | 8 | 17 | 19 | 18 | 18 | 79 % |
| Kim Possible | Occident | 4 | 18 | 18 | 19 | 19 | 82 % |
| Shego | Occident | 10 | 20 | 20 | 20 | 20 | 81 % |
| Tifa | Japon | 2 | 1 | 2 | 4 | 1 | 60 % |
| Chun-Li | Japon | 1 | 8 | 5 | 8 | 2 | 52 % |
| Ada Wong | Japon | 13 | 11 | 11 | 13 | 3 | 36 % |
| 2B | Japon | — | 2 | 3 | 7 | 4 | 62 % |
| Nami | Japon | 3 | 7 | 1 | 1 | 5 | 79 % |
| Samus | Japon | 5 | 4 | 9 | 11 | 8 | 60 % |
| Mirko | Japon | — | 9 | 8 | 6 | 9 | 73 % |
| Tsunade | Japon | 7 | 6 | 6 | 5 | 10 | 82 % |
| Marin | Japon | — | 14 | 12 | 2 | 11 | 85 % |
| Yor | Japon | — | 13 | 7 | 3 | 13 | 86 % |
| Yoruichi | Japon | 11 | 16 | 14 | 12 | 14 | 79 % |
| Fubuki | Japon | 15 | 15 | 16 | 15 | 17 | 82 % |

D.Va est classée « Occident » (studio Blizzard), alors que le personnage est coréen.

**Résultats (faits mesurés).**
- **Le déclin des cartoons occidentaux des années 2000 est réel.**
  - Kim Possible (4e en P1), Jessica Rabbit (8e) et Shego (10e) sont aujourd'hui 18e à 20e.
  - L'IA n'explique pas ce déclin : le classement sans IA donne le même résultat.
- **La part des 8 personnages occidentaux dans la production du top 20 baisse à chaque période :** 35 %, 31 %, 27 %, 24 % (26 % sans IA en P4).
- **Exceptions occidentales.** Raven et D.Va restent dans le top 10. Chel est la seule à monter (taux de 116, puis 328, 622 et 896), mais avec 74 % d'IA en P4.
- **La forte hausse des héroïnes d'anime récentes vient surtout de l'IA.** Marin passe 2e et Yor 3e en P4, mais avec 85–86 % d'IA. Sans IA, elles ne sont que 11e et 13e.
- **Ada Wong a la plus faible part d'IA (36 %)** et elle est 3e en production humaine récente.
- **Les personnages les plus dessinés par des humains aujourd'hui** sont Tifa, Chun-Li, Ada Wong et 2B.
- **Aucun lien avec l'indice TierMaker.** Spearman entre l'indice de consensus et le taux : de −0,25 à +0,07 selon la période, et −0,11 en P4 sans IA, rien de significatif. Le test ne porte que sur le top 20, donc sur une plage de valeurs restreinte.

**Interprétations (hypothèses de l'IA).**
- **TierMaker mesure plutôt la mémoire des votants, et la production rule34 l'activité actuelle.** La forte place de Kim Possible, Shego ou Jessica Rabbit dans les votes viendrait en partie de la nostalgie d'une génération : leurs dessins ont culminé avant 2016.
- **La stabilité de Raven et Starfire** pourrait venir de leur exposition continue, notamment avec *Teen Titans Go!*, diffusé depuis 2013. C'est non vérifié.
- **Ada Wong** est cohérente avec le seul facteur causal bien établi du corpus : une adaptation ou une nouvelle entrée de jeu. Ici, il s'agit du remake de Resident Evil 4 (2023).

**Limites.**
- La découpe par période ne vaut que pour rule34. DeviantArt n'a pas de filtre par date, et les favoris MyAnimeList sont un stock sans date.
- rule34 est un site pour adultes. Il ne dit rien des goûts d'un public de 11–16 ans.

## 11. Test ajouté : classement TierMaker par groupe de titres

Données : script `tiermaker_titres/classer_par_titre.py`. Il réutilise la fonction `agreg()` de l'app, donc le même indice de consensus que l'onglet Analyse. Résultats : `tiermaker_titres/classement_par_groupe_de_titres_2026-10-25.csv`, données brutes dans `brut_groupes_titres_2026-10-25.json`. Ce test répond à l'objection de l'utilisateur : les titres et les choix des votants peuvent vouloir dire plusieurs choses.

**Correction.** Le classement général de l'onglet Analyse porte sur **13 votes**, pas 10 comme annoncé dans la conversation.

**Groupes, selon le titre de l'événement vu par les votants.**

| Groupe | Votes | Titres |
|---|---|---|
| Attirance (8) | 87784832, 5058287, 8447367, 88691896, 91860172, 30083716, 20899730, 436045 | « HOTTEST WOMEN IN FICTION? », « Hottest Cartoon Characters » (×4), « Hottest Female Cartoon Characters », « Hottest animated girls », « Cartoon Hotties » |
| Waifu (4) | 81614596, 80408816, 30081640, 99761754 | « Disney/PIXAR Waifus », « Waifu anime and cartoon », « Biggest Waifu List », « Top Tier Waifu » |
| Neutre (1) | 73568440 | « Ranking Female Video Game Charecters » |
| Design | aucun | — |

**Résultats (faits mesurés).**
- **Top 8 par groupe :**

| Groupe | Top 8 |
|---|---|
| Attirance | Chel, Shego, Hélène Parr, Starfire, Raven, Jessica Rabbit, Tsunade, Kim Possible |
| Waifu | 2B, Yor, Mirko, Marin, Yoruichi, Tsunade, Hinata, Makima |
| Neutre | 2B, Tifa, Samus, Chun-Li, Zelda, Cynthia, Lara Croft, Ada Wong |

- **L'accord entre les groupes n'est que modéré.** Attirance contre waifu : Spearman 0,42 sur 131 personnages communs.
- **Seule paire au même périmètre.** On compare 87784832 (« HOTTEST WOMEN IN FICTION? », tous médiums) et 80408816 (« Waifu anime and cartoon », tous médiums). Sur les 36 personnages présents dans les deux top 100, le Spearman est de 0,43 (p = 0,008).
  - **Mieux classés en « hottest » :** Mai Shiranui (4e contre 78e), Poison Ivy (18e contre 82e), Shego (6e contre 35e), Chel (12e contre 41e), Ada Wong (16e contre 54e), GoGo Tomago (56e contre 92e).
  - **Mieux classés en « waifu » :** Raven (21e contre 1re), Starfire (19e contre 3e), Chun-Li (40e contre 4e), D.Va (50e contre 7e), Mirko (31e contre 8e), Samus (59e contre 11e), Tsunade (44e contre 10e), Nami (60e contre 14e).
- **Biais de structure.**
  - Six votes « attirance » ne contiennent que des cartoons, et l'indice compare chaque personnage aux autres personnages présents dans les mêmes votes.
  - « Chel 2e au général » signifie donc « la mieux classée dans les votes hottest de cartoons », pas « devant Tifa ».
  - Le classement général mélange donc des questions différentes (attirance, waifu, popularité) et des médiums différents.
- **Le vote neutre** (jeux vidéo) est proche de la production humaine récente sur rule34 (§10) : Tifa, Chun-Li, 2B et Ada Wong sont dans le haut des deux classements.

**Interprétations (hypothèses de l'IA).**
- **Les deux types de votes ne récompensent pas les mêmes personnages.** Les titres « hottest » favoriseraient les designs de femme fatale (Mai Shiranui, Poison Ivy, Shego, Ada). Les titres « waifu » favoriseraient les personnages auxquels on s'attache (Raven, Starfire, D.Va, Mirko).
- Cette conclusion ne repose que sur deux votes, avec des publics, des animateurs, des dates et des modèles différents. Une absence du top 100 ne veut pas dire un mauvais classement : le personnage n'était peut-être pas dans le modèle.

**Conséquence de méthode.** Ne plus présenter TierMaker comme une mesure de l'« attrait visuel » général. Il faut toujours préciser le groupe de titres et le médium couvert.

## 12. Débat avec l'utilisateur : points retenus

**Position de l'utilisateur.** S'inspirer de personnages occidentaux largement appréciés en Occident est un bon moyen d'augmenter l'attractivité du manga.

**Ce que les données appuient.**
- 8 des 20 premiers du classement général sont occidentaux.
- Runeterra est déjà la première influence d'Edenia.

**Nuances.**
- **« Apprécié en Occident » n'est pas « occidental ».** 12 des 20 premiers viennent d'œuvres japonaises, comme la plupart du top rule34 sans IA (Rouge, Tifa, Amy, Peach, Chun-Li, Zelda).
- **Les personnages occidentaux du top viennent presque tous de la même époque :** Jessica Rabbit (1988), Chel (2000), Kim Possible (2002), Teen Titans (2003), Les Indestructibles (2004). Le §10 confirme que leur production est en déclin. Une partie de leur score vient sans doute de la nostalgie, qu'on ne reproduit pas en s'en inspirant.
- **Ce qui plaît serait plutôt l'archétype que l'origine :** la rivale méchante, la princesse solaire face à la gothique, la femme fatale. Ces archétypes existent aussi dans le manga.

**Ajout de l'utilisateur.** Si un design plaît aux 11–16 ans, c'est déjà un bon point. Aucune source du corpus ne mesure ce public : rule34 est réservé aux adultes, et l'âge des votants TierMaker est inconnu.

**Les super-héroïnes ressortent souvent.** Dans le top 20 : Starfire, Raven, Hélène Parr, Mirko, Fubuki, Kim Possible, et Shego, ancienne héroïne. Explications possibles (hypothèses, non testées) :
1. **Le costume comme signature visuelle :** silhouette, 2–3 couleurs, emblème. On le reconnaît en miniature et on peut le redessiner. Le costume moulant joue aussi dans les votes d'attirance.
2. **Attirance et compétence réunies :** une héroïne puissante peut gagner dans les deux types de votes.
3. **Exposition :** les franchises de super-héros sont très souvent adaptées, et l'adaptation est le facteur causal le mieux établi.
4. **Biais de sélection possible :** les super-héroïnes sont peut-être surreprésentées dans les modèles TierMaker eux-mêmes. À mesurer avant de conclure.

**Piste la plus utile.** *My Hero Academia* et *One-Punch Man* reprennent un archétype occidental (le super-héros) avec les codes du manga, et Mirko comme Fubuki sont dans le top. C'est une version plus précise de la position de l'utilisateur.

**Archétype + gimmick (intuition de l'utilisateur).** Plusieurs personnages du top reposent sur un contraste, ce que les Japonais appellent le *gap moe* :
- Yor : tueuse et maladroite ;
- Marin : gyaru et otaku ;
- Raven : gothique qui contient ses émotions ;
- Starfire : naïve et guerrière.

Ce n'est pas encore mesuré : il faudrait un codage du top 50.

## 13. Suites proposées (non faites)
- **(a) Évolution des favoris MyAnimeList,** à partir des captures annuelles de la page de classement sur la Wayback Machine. Leur existence n'est pas encore vérifiée.
- **(b) Codage archétype + gimmick sur le top 50,** puis comparaison avec les votes et la production.
- **(c) Boutons « Attirance / Waifu / Neutre » dans l'onglet Analyse** de l'app TierMaker. Les cases à cocher existantes permettent déjà de le faire à la main.
- **Mesurer la part de super-héroïnes dans les modèles TierMaker,** pour tester le biais de sélection (point 4 du §12).
