# Critique 2 — Worm, le dépôt `Projecttest`, et ce que les données supportent réellement

*Rédigé le 2026-10-04. Dépôt cloné et lu : 174 fichiers. Sources en §10.*

---

## Verdict en cinq lignes

1. **Le socle factuel du texte Worm est exact** — et même mieux sourcé que ce qu'il cite : 306 chapitres, 30 arcs et 1 682 400 mots sont confirmés par les sources primaires.
2. **Deux chiffres financiers sont faux ou non établis** : les « 20 000 $/mois de dons » sont contredits par l'auteur lui-même (≈ 4 500 CAD dans les bons mois, 1 000–2 000 typiques), et le « million de dollars de Patreon cumulés » ne repose que sur une source dont les autres chiffres sont faux.
3. **« Du bouche-à-oreille pur » est incomplet** : l'auteur attribue explicitement à une recommandation d'Eliezer Yudkowsky (HPMOR) le doublement de son lectorat à la fin — et HPMOR est déjà une note de bas de page de ton propre dépôt.
4. **Le dépôt contredit le texte sur Red Hood**, et c'est le point important : par tes propres données, le décrochage de Red Hood est *la norme* de son groupe de pairs, et la mesure « le public est venu » (313) n'est même pas la plus élevée du groupe (Ayashimon : 371 après dédoublonnage, chez toi).
5. **« Worm est le groupe témoin de ton corpus » ne tient pas méthodologiquement** : c'est un groupe de n = 1, avec une variable (M3) constante — et ton corpus ne mesure ni la portée ni le revenu.

---

## 1. Ce que j'ai lu, et ce qui n'y est pas

**Lu intégralement ou en détail :** `01_CONTEXTE_ET_SUITE (1).md`, `Red Hood/synthese_red_hood.md`, `Red Hood/scores_reddit_archives.csv`, `Red Hood/matrice_arguments.csv`, `red_hood_classements_chapitres_et_volumes_2026-09-22.csv`, `red_hood_notes_3_tomes_*`, `Jajanken_comparaison_complete_5_courtes_vs_hits_*.md`, `percentiles_tous_corpus_principaux_*.csv/json`, `percentiles_avec_nombre_votes_*.csv`, `LISEZMOI_commit_*.md`, `Note_retrait_One_Piece_116_*.md`, `REPARTITION_DEUX_OEUVRES_README.md`, `Myanimelist/catalogue_mal_shonen.json` (2 951 œuvres), `Influence-Atelier/influences-atelier.md`.

**Ce qui n'est PAS dans le dépôt** — et qu'il faut donc considérer comme venant de la conversation seulement :

| Élément | Présent dans le dépôt ? |
| :--- | :--- |
| Le modèle M1 / M2 / M3, « audience empruntée », « la vague » | **Non** (aucune occurrence) |
| Radiant (l'œuvre) | **Non** — les seules occurrences de « radiant » sont le pseudo d'un commentateur Reddit (`Radiant_eagle573`) et la mention d'un manga homonyme de 2002 (*Soul Gadget Radiant*) dans le catalogue MAL |
| La table des 5 appariements (Mashle/HP, Red Hood, Radiant, JJK, 2011) | **Non** |
| Narou, webnovels, Wuxiaworld | **Non** |

Conséquence de méthode : ta base de données et ta théorie sont deux objets distincts. Le dépôt documente **un cas (Red Hood) + un corpus de réception (notes, ToC, percentiles) + un catalogue MAL**. Il ne contient pas la thèse. Toute évaluation de la thèse doit donc dire *quel* fichier la soutient — et pour l'essentiel, aucun ne porte M1, M2 ou M3.

---

## 2. Worm — vérification ligne à ligne

### 2.1 Ce qui est confirmé (sources primaires)

| Affirmation du texte | Vérification | Statut |
| :--- | :--- | :--- |
| 1,68 M de mots | 1 682 400 mots (Wikipedia, cité sur sources) | ✅ |
| **306 chapitres** | Recompté sur le sommaire officiel : « As of E.4, there are 304 chapters. With E.5 and the final interlude, the total will be 306 » (commentaire daté de nov. 2013 sur la page ToC officielle de parahumans.wordpress.com) | ✅ |
| **30 arcs** | Le sommaire officiel montre **Arc 30** puis **Epilogue: Teneral E.1 → E.x**. Ta formulation correspond mieux à la source primaire que celle de Wikipedia (« 31 arcs », qui compte l'épilogue) | ✅ (mieux que la source secondaire) |
| Juin 2011 → novembre 2013 | ✅ Wikipedia + ToC officiel | ✅ |
| Deux chapitres par semaine | Mardi + samedi, avec un chapitre bonus le jeudi **en récompense de dons** | ✅ |
| Courbe de vues (13 → 26 844 → 207 833 → 1 390 648 → 693 675) | Reproduction exacte et chiffre pour chiffre des données citées par Wikipedia | ✅ (mais ce sont ses chiffres, pas une mesure directe) |
| Pic daté : novembre 2013 | ✅ | ✅ |
| Gratuit, sans éditeur, sans adaptation | Au 10/2025 : aucune édition imprimée ou ebook commerciale officielle, aucune adaptation TV/cinéma produite ni annoncée, Wildbow déclaré réticent | ✅ |
| M3 = 0 | ✅ — **une seule nuance** : il existe un audiobook intégral *fan-made* (podcast « Worm: The Full-Cast Audiobook »), non officiel et gratuit. Cela renforce ton point : production sans droits ni revenus, donc M3 = 0 au sens économique | ✅ |
| ~10 000 fanfics | Ordre de grandeur **juste** : AO3 (tag Parahumans Series – Wildbow) = **6 872 œuvres** ; FFN (catégorie Worm) = **929 histoires** ; + SpaceBattles / SufficientVelocity / QuestionableQuesting = plusieurs milliers de fils. Total ≈ 8 000–12 000 selon les plateformes comptées | ✅ sous réserve de préciser la période et les plateformes |
| « de-worm the forum » / sous-forum dédié | Témoignage communautaire direct et concordant (r/WormFanfic) : les modérateurs ont déplacé les fics Worm dans une section dédiée parce qu'elles « noyaient » Creative Writing ; Worm est aussi le seul fandoms à avoir sa section sur SV | ✅ (témoignage, pas annonce officielle) |
| BCF plus long que l'œuvre source | **Confirmé, et sous-estimé** : *Brockton's Celestial Forge* = **201 chapitres / 2 904 170 mots** sur FFN (mise à jour du 1er octobre 2026) > 1 682 400 | ✅ (ton 2,6 M est périmé) |
| Narou, génération dorée 2012-2013 | *Mushoku Tensei* : web novel démarré le **22 novembre 2012** ; *KonoSuba* : **décembre 2012** ; *Tensei Shitara Slime* : **20 février 2013** ; *Re:Zero* : 2012 (tous sur 小説家になろう) | ✅ |

### 2.2 Ce qui est faux ou non établi

| Affirmation | Problème | Correction |
| :--- | :--- | :--- |
| **« Les dons dépassaient 20 000 $/mois à la fin de la sérialisation »** | **Contredit par l'auteur.** Wildbow, 4 janvier 2014, sur sa propre page de soutien : *« For the last stretch, on the really good months, I've made ~4500 CAD. On the bad months, I've made ~600. The typical month? Maybe $1000-2000. »* | Écart d'un facteur 4 à 20. Il visait ~4 500 CAD **dans ses meilleurs mois**, avec une médiane à 1 000–2 000 CAD, et ajoutait que les mois de fin de *Worm* étaient gonflés par des pourboires « congratulatoires » |
| **« Le Patreon de Wildbow a dépassé 1 million de dollars cumulés »** | **Non établi.** La seule source trouvée qui l'affirme est un article de blog qui donne par ailleurs « 2 000 à 4 000 patrons, 15 000–30 000 $/mois » — contredit par Graphtreon (**983 patrons, 4 528 $/mois** aujourd'hui ; Patreon lancé le **10 février 2014** ; 2 236 $/mois en 2016). Wildbow déclare par ailleurs « un confortable six chiffres » annuels (rapporté via un fil r/Parahumans qui cite son commentaire) | Réécrire : « revenu de plusieurs dizaines de milliers de dollars par an, majoritairement des dons directs, suffisant pour vivre » — vérifiable — et **retirer** le « million cumulé » ou le marquer « non vérifié » |
| **« Aucune campagne […] du bouche-à-oreille pur »** | **Incomplet, et la pièce manquante est dans ton dépôt.** Wildbow, interview 2015 : *« Au moment où Worm se terminait, Eliezer Yudkowsky, l'auteur de Harry Potter and the Methods of Rationality, a recommandé Worm, beaucoup de gens ont commencé l'histoire […] Mon lectorat a doublé dans les derniers mois. »* Or **HPMOR est déjà la note 10 de ton fichier `influences-atelier.md`** | Ce n'est pas du bouche-à-oreille pur : c'est un **canal de découverte daté et attribuable** — exactement le type de mécanisme que ta propre étude Red Hood avait isolé (« la recommandation extérieure constitue aussi un canal ») |
| « 30 arcs » vs Wikipedia 31 | Faux problème | Aucune correction à faire, mais à signaler : ta version suit la source primaire |
| « Taylor Varga : 1,9 M de mots » | Non vérifié dans le temps imparti | À recouper sur FFN/SpaceBattles avant de citer |

### 2.3 Le point le plus intéressant du texte, et ce qu'il rate

Le texte dit : *« Worm est le seul élément où M3 = 0 »*. C'est exact, et c'est une observation juste et utile.

**Mais il en tire la mauvaise conclusion analytique, dans les deux sens :**

**(a) Worm n'est pas un cas pur de M1 = 0 — c'est peut-être un cas d'audience empruntée.** Le pic de novembre 2013 (1 390 648 vues, contre 207 833 cinq mois plus tôt) **coïncide avec la recommandation de Yudkowsky et avec la fin de la sérialisation**. Autrement dit : même le « groupe témoin » hérite d'un public adjacent préexistant — celui d'une autre web-série gratuite anglophone. Si ta thèse de l'audience empruntée vaut quelque chose, **Worm en est une confirmation de plus, pas une exception**. Et le mécanisme est datable : c'est un événement de découverte, pas une vague de goût.

**(b) « M3 = 0 » n'identifie pas l'effet de M3.** Une variable qui ne varie jamais n'explique rien. Un seul cas avec M3 = 0 te dit *qu'on peut atteindre des centaines de milliers de lecteurs sans écran* — c'est une borne supérieure de ce que M1 + M2 permettent. Pour estimer l'effet de M3, il faut de la variation, et tu l'as dans tes propres données externes : Jujutsu Kaisen passe de 6,8 M (09/2020) à 60 M (12/2021) autour de l'anime. **C'est de la portée payante multipliée par ~9, pas seulement du revenu.** La formule « M3 n'est pas un multiplicateur de portée, c'est un multiplicateur de revenu » est élégante mais fausse en l'état : M3 multiplie le **nombre d'acheteurs**, donc la portée au sens commercial. Ce que Worm montre, c'est autre chose : qu'on peut avoir de la portée *non payante* à grande échelle — mais Wildbow en vit quand même (six chiffres annuels, ~1 $ par lecteur mensuel et par an). « Presque aucun » est trop fort : c'est peu par lecteur, pas nul.

---

## 3. Ce que ton dépôt dit vraiment sur Red Hood

C'est la partie où le texte Worm se trompe le plus gravement — parce qu'il utilise deux de tes chiffres contre leur propre avertissement.

### 3.1 « Le public est venu (313 comptes) » n'est pas ce que ton CSV mesure

Ton fichier `scores_reddit_archives.csv` a une colonne justement nommée `comptes_7j_du_fil` : **313 = nombre de comptes distincts ayant commenté dans les 7 jours**, sur r/manga — pas des lecteurs, pas des acheteurs, pas des Occidentaux. Ta propre synthèse le redit à trois endroits, ex. ligne 172 : *« Forte activité de lancement dans le corpus étudié ; pas mesure du lectorat occidental total »*.

Et surtout : **par ton propre dédoublonnage, Red Hood n'est pas le premier de son groupe.** Ta synthèse (l. 162) donne : *Red Hood 313 ; **Ayashimon 371** (deux fils réunis et dédoublonnés) ; Sakamoto Days 179 ; Neru 98*. Si 313 prouvait « le public est venu », alors Ayashimon – arrêté lui aussi – avait un public encore plus présent. **Le chiffre ne discrimine rien.**

### 3.2 La décroissance de Red Hood est identique à celle de ses pairs

En prenant le même instrument (comptes à J+7), du chapitre 1 au chapitre 14 :

| Série | Ch.1 | Ch.14 | Variation | Sort |
| :--- | ---: | ---: | ---: | :--- |
| Red Hood | 313 | 96 | **−69,3 %** | arrêtée au ch.18 |
| Sakamoto Days | 179 | 56 | **−68,7 %** | toujours en cours |
| Ayashimon | 240 (371 dédoubl.) | 74 | **−69,2 %** | arrêtée au ch.25 |
| Neru | 98 | 19 | −80,6 % | arrêtée |

Trois séries sur quatre décrochent **exactement du même ordre**. Cette forme est une propriété de l'instrument (r/manga) et du format hebdomadaire, pas du titre. Un chiffre qui vaut pour un succès et pour un échec ne peut servir à expliquer ni l'un ni l'autre — c'est la définition d'une mesure non informative. Ton doc le dit déjà (« Cela ne compare pas des cohortes de lecteurs ») ; le texte Worm l'a oublié.

### 3.3 Ton ToC — la meilleure donnée du dossier — dit autre chose, et plus tôt

Ta règle, écrite noir sur blanc dans `Jajanken_comparaison_complete_5_courtes_vs_hits_2026-09-22.md` (l. 240) :

> *« les premiers chapitres sont placés promotionnellement. Avec un décalage approximatif de sept à huit semaines, les positions des chapitres publiés 8 à 14 constituent le meilleur proxy de la réception du premier tome. »*

Applique-la à ton propre CSV Red Hood :

| Chapitre publié | Rang / entrées | Fenêtre informative |
| ---: | :--- | :--- |
| 1 | 1 / 20 (**couleur + lancement** → placement éditorial) | aucune |
| 2 | 6 / 19 (**couleur** → placement éditorial) | aucune |
| 3 → 8 | 8/19, 5/20, 9/21, 8/21, 12/21, 8/21 | non informatif (antérieur à la fenêtre de 7–8 semaines) |
| **9** | **18 / 21** | reflète ~ch. 2–4 |
| **10** | **21 / 21 (dernier)** | reflète ~ch. 3–5 |
| 11 | 18 / 19 | |
| **12** | **21 / 21 (dernier)** | |
| 13 | 18 / 19 | |
| 14 | 20 / 20 | |
| 15 → 18 | 19/20, 20/20, 17/20, 20/21 | |

**Conclusion, avec ta méthode et tes données** : la réception mesurée par le magazine place Red Hood dans le dernier quart **dès le chapitre imprimé 9**, c'est-à-dire pour des chapitres **2 à 6** — **le prologue**, avant l'arc d'examen (ch. 9+). Autrement dit : si l'on veut une explication temporellement valide de l'arrêt, elle se situe dans les tout premiers chapitres, pas dans le virage « conte → examen ». Toute lecture qui fait de l'examen la cause du décrochage se heurte à ce décalage — et c'est cohérent avec ton propre avertissement de contexte : *« Ne pas transformer le cas Red Hood en formule "conte puis examen = abandon" »*.

Deux pièges de lecture à signaler dans ton CSV :
- le **chapitre 1 est au rang 1** parce qu'il a la page couleur de lancement (colonne `couleur = True`) : ce n'est pas un vote de lecteurs. Idem ch. 2 (rang 6, couleur). Si ces lignes entrent dans une moyenne de rang, elles biaisent la série vers le haut.
- le rebond des chapitres 15 → 18 (242, 235, 210, 230 comptes, contre 94–142 sur les chapitres 9–14) n'est pas une reconquête : **ta synthèse l'explique déjà** (discussion sur la « hache », métanarration, annonce de fin) et conclut qu'« un rebond de commentaires ne mesure pas une reconquête de lecteurs ». Le texte Worm réintroduit exactement l'erreur que ton dossier avait corrigée en v2/v3.

### 3.4 Worm dans ton corpus : la ligne la moins fiable du fichier

Dans `percentiles_tous_corpus_principaux_2026-09-22.csv`, la famille « Web-serial » contient **un seul élément : Parahumans**. Et la ligne SensCritique affiche **11 notations**.

Or ton propre document l'a déjà signalé : *« Un percentile très élevé sur peu de votes peut être instable : Worm atteint par exemple le sommet SensCritique avec seulement 11 notations »* (fichiers du 20/09, l. 51) — et ton score ajusté, dans la version du 20/09, ramène Worm d'un percentile brut de 99,9 à une note ajustée de **7,24** et un percentile ajusté de **58,6**. **Ta propre méthode refuse déjà de lire cette ligne comme un sommet.** Le texte Worm fait comme si de rien n'était.

---

## 4. Ce que le corpus ne peut pas porter

| Affirmation du texte Worm | Problème |
| :--- | :--- |
| « Worm est le meilleur point de ta liste » | C'est le **seul** point mesuré dans une famille de taille 1. « Meilleur » suppose une comparaison |
| « C'est le groupe témoin de ton corpus » | Un témoin suppose des comparanda **mesurés de la même façon**. Ici : vues mensuelles et comptage de fanfics pour Worm, notes et percentiles pour les 19 autres séries. Aucun dénominateur commun dans le dépôt |
| « Sur les vues et les fanfics, Worm écrase Radiant » | **Il n'y a aucun Radiant dans le corpus.** La comparaison n'est pas dans tes données ; elle est faite avec des chiffres extérieurs, non appariés (vues mensuelles d'un WordPress contre exemplaires vendus d'un manfra : > 1 M en France, 19 tomes, premier manfra publié au Japon, anime NHK/Lerche 2018-2020). Sur l'attention, ton verdict est plausible ; sur l'argent, il s'inverse |
| « M3 = 0 rend M1 et M2 lisibles » | Ton corpus ne mesure ni M1, ni M2, ni M3 : il mesure des **notes** (réception) et des **rangs de sommaire** (réception éditoriale). Ni portée, ni revenu. La phrase est un argument conceptuel, pas un résultat |
| « La générativité est une métrique que ton corpus ne mesure nulle part » | **Exact** — et c'est la remarque la plus productive du texte. Voir §5 |

---

## 5. La générativité : les vrais chiffres, et comment la rendre utilisable

Les chiffres accessibles aujourd'hui :

| Œuvre | Plateforme | Volume |
| :--- | :--- | ---: |
| Worm (Parahumans) | AO3 (tag officiel) | **6 872 œuvres** |
| Worm | FanFiction.net | **929 histoires** |
| Worm | SpaceBattles / SV / QQ | plusieurs milliers de fils (non compté finement ici) |
| *Brockton's Celestial Forge* | FFN | **2 904 170 mots / 201 chapitres** |
| Worm (source) | — | 1 682 400 mots |
| **Harry Potter** | **FFN** | **638 000 histoires** |

Ce dernier chiffre est le contre-argument décisif : sur **la même plateforme**, Harry Potter a ~687 fois plus de fics que Worm. Donc « 10 000 fanfics » n'est pas, en soi, une preuve de solidité de worldbuilding : **le comptage de fanfics mesure d'abord la taille et l'âge du fandom, puis l'effet de plateforme** (SpaceBattles/SV produisent des fics longues que FFN/AO3 mesurent mal).

Trois façons de rendre la métrique utile dans ton cadre :

1. **Part de fics longues** (≥ 100 k mots) plutôt que le nombre total : mesure l'engagement, pas la taille du fandom.
2. **Fics par lecteur** (normalisée par la portée) : Worm ≈ 8 000–10 000 œuvres pour quelques centaines de milliers de lecteurs mensuels — ratio vraisemblablement très supérieur à HP. C'est *ce* ratio qui serait un indicateur de monde « habitable », et il serait comparable entre tes cas.
3. **Croissance post-fin** : Worm garde 693 675 vues mensuelles **cinq ans après la fin**, sans adaptation ni réédition commerciale. C'est la mesure la plus propre que tu possèdes — et elle est compatible avec ta contrainte de corpus (une seule grandeur par œuvre, datée).

Et la limite, à écrire dans le dossier : la générativité est un proxy d'**attachement**, pas de revenus ni d'achat. Deux personnes qui écrivent 300 k mots de fanfic ne sont pas deux acheteurs.

---

## 6. Le point narratif : « escalade tenue » et corpus

Le texte affirme que Worm est « le seul cas occidental long-format ayant soutenu une escalade sur 1,68 M de mots », et propose la générativité comme indicateur de solidité du worldbuilding. Deux réserves :

- **« Le seul » est une affirmation forte sans relevé.** Le dépôt ne contient aucun corpus occidental long-format de web-séries : ni *Ward* (la suite, 2017-2020), ni *Pact*, ni *Twig*, ni *Pale*, ni les autres piliers du genre (Wandering Inn, Mother of Learning…). Comparer Worm à un « seul » suppose une liste exhaustive qui n'existe pas encore chez toi.
- **La fanfic n'est pas une mesure de worldbuilding** mais d'attachement aux **personnages et aux relations** : les fandoms dominants sont très majoritairement centrés sur les personnages (slash et relationnel en tête). Un monde solide sans personnages aimables génère peu. Si l'objectif est de tester la robustesse du monde, il faudrait des fics centrées sur le monde (OC, exploration, factions) — un codage que ton pipeline sait déjà faire (tu codes déjà les arguments par thèmes dans `matrice_arguments.csv`), mais qu'il faudrait appliquer aux textes de fanfics, pas aux discussions de chapitres.

---

## 7. Sur la réconciliation « 2014 »

Ton texte dit : *« Ta date de 2014 était trop tardive de deux ans. »* Les deux affirmations peuvent être vraies, et il faut les séparer :

| Ce que date « 2014 » | Exactitude |
| :--- | :--- |
| Le début de la traduction anglaise des webnovels chinois (*Coiling Dragon*) et la fondation de Wuxiaworld (22/12/2014) | ✅ 2014 est exact |
| Le démarrage du marché du light novel en France (Ofelbe) | ✅ 2014 est exact |
| L'écriture gratuite massive côté japonais (Narou) et anglophone (Worm, HPMOR) | ❌ c'est **2010-2013** |

Donc : **2014 date la mise en marché et la traduction, 2011-2013 date la production gratuite.** La formulation « webnovel » empruntée telle quelle à Radiant reste fausse pour l'œuvre (2013, shōnen papier, éditeur, inspirations *Fairy Tail/Naruto/One Piece*) — la correction de la critique 1 tient.

---

## 8. Ce qui tient, solidement, dans ce texte

À conserver tel quel :

- **La correction du dénominateur.** Comparer 10 769 notes Goodreads à 11,8 M (qui est le compte Goodreads du seul tome 1 de HP dans ton corpus : 11 816 633) est une erreur de calibrage : Worm n'a pas de tunnel achat → fiche. Ce raisonnement est juste et important, et il s'applique à **toute** ton étude (tes corpus Goodreads/SC ne mesurent que les lecteurs qui cataloguent).
- **M3 = 0, et le pic daté de novembre 2013.** Utile, propre, vérifiable.
- **L'idée que la générativité soit une métrique de solidité non mesurée par ton corpus.** C'est une addition réelle à ton dispositif — à condition de la normaliser (§5).
- **Le parallèle Worm (2011) / Narou (2012-2013).** Exact, et c'est une bonne observation de simultanéité. Nuance : côté anglophone, *HPMOR* (2010-2015) précède Worm de deux ans — Worm amplifie un modèle déjà vivant, il ne le fonde pas seul.

---

## 9. Les six corrections à faire

| # | Où | Correction |
| :--- | :--- | :--- |
| 1 | Texte Worm | « 20 000 $/mois » → « ~4 500 CAD les meilleurs mois, 1 000–2 000 typiques » (source : l'auteur) |
| 2 | Texte Worm | « Patreon > 1 M$ cumulés » → retirer ou marquer non vérifié |
| 3 | Texte Worm | « bouche-à-oreille pur » → ajouter la recommandation Yudkowsky/HPMOR (déjà dans ton dépôt) |
| 4 | Texte Worm | « le public est venu (313) » → « 313 comptes commentant à J+7 ; Ayashimon 371 ; ne discrimine pas » |
| 5 | Texte Worm | « Worm écrase Radiant » → préciser la métrique, ou retirer (aucun Radiant dans le corpus) |
| 6 | Dépôt | Dans `scores_reddit_archives.csv` et le ToC : exclure explicitement ch. 1 et 2 de toute moyenne de rang (pages couleur), et documenter la fenêtre informative 7–8 semaines pour Red Hood comme tu le fais déjà pour Naruto/Bleach/JJK/MHA |

Et deux ajouts recommandés : un **ratio de générativité normalisé** (§5) et un **test M3 intra-série** (évaluer, pour chaque série de ton corpus dotée d'un anime, la variation de portée payante autour de la diffusion — tu as déjà le matériel temporel : Jajanken, MAL, Reddit).

---

## 10. Sources

**Sources primaires**
1. Wildbow, page « Support » (commentaire du 4 janvier 2014) — revenus réels de fin de *Worm* : https://pactwebserial.wordpress.com/support/
2. Interview de Wildbow, juillet 2015 (recommandation de Yudkowsky, doublement du lectorat, premier don de 1 000 $, rythme de publication) : https://t4nky.wordpress.com/2015/07/02/interview-with-wildbow/
3. Sommaire officiel de *Worm* (Arc 30 + Epilogue E.1–E.x ; commentaire du 14/11/2013 donnant 304 → 306 chapitres) : https://parahumans.wordpress.com/table-of-contents/
4. Catalogue FFN — Worm : **929** histoires ; *Brockton's Celestial Forge* : **201 chapitres / 2 904 170 mots** (maj 01/10/2026) : https://www.fanfiction.net/book/Worm/
5. Catalogue FFN — Harry Potter : **638 000** histoires : https://www.fanfiction.net/book/Harry-Potter/
6. AO3, tag *Parahumans Series – Wildbow* : **6 872 œuvres** : https://archiveofourown.org/tags/Parahumans%20Series%20-%20Wildbow/works
7. Graphtreon — Wildbow : 983 patrons, 4 528 $/mois, Patreon lancé le 10/02/2014 : https://graphtreon.com/creator/Wildbow

**Sources secondaires (à recouper)**
8. Wikipedia (EN), *Worm (web serial)* — 1 682 400 mots, courbe de vues, absence d'édition commerciale au 10/2025 : https://en.wikipedia.org/wiki/Worm_(web_serial)
9. r/WormFanfic — « de-worm the forum », sous-forum dédié, section propre sur SV : https://www.reddit.com/r/WormFanfic/comments/c9iqcc/
10. r/Parahumans (sept. 2024) — 5 315 $/mois, et citation du commentaire Reddit de Wildbow évoquant « six figures » : https://www.reddit.com/r/Parahumans/comments/1faivho/
11. Blog « eternal-lib » — source unique du « > 1 M$ cumulés », chiffres de patrons contradictoires avec [7] : https://eternal-lib.com/story/digital-ink/chapter-2-patreon-serial-fiction/
12. Elysian Press — interview « 7 600 $/mois » : https://www.elysian.press/p/wildbow
13. Kadokawa, page commémorative de fin de *Mushoku Tensei* — web novel démarré le 22/11/2012 : https://promo.kadokawa.co.jp/mfbooks/title/mushoku/
14. Wikipedia (JA), *転生したらスライムだった件* — web novel du 20/02/2013 au 30/10/2015 : https://ja.wikipedia.org/wiki/転生したらスライムだった件

**Ton dépôt (fichiers utilisés)**
15. `Benchmark Oeuvre/Red Hood/scores_reddit_archives.csv`, `red_hood_classements_chapitres_et_volumes_2026-09-22.csv`, `Red Hood/synthese_red_hood.md`, `Red Hood/matrice_arguments.csv`
16. `Benchmark Oeuvre/Jajanken_comparaison_complete_5_courtes_vs_hits_2026-09-22.md` (règle des 7–8 semaines, l. 240)
17. `Benchmark Oeuvre/percentiles_tous_corpus_principaux_2026-09-22.csv`, `percentiles_avec_nombre_votes_2026-09-20.csv`, `Percentiles_tous_corpus_principaux_2026-09-20.md` (l. 51)
18. `Benchmark Oeuvre/01_CONTEXTE_ET_SUITE (1).md`, `Benchmark Oeuvre/Myanimelist/catalogue_mal_shonen.json`, `Atelier App/Export 1/Influence-Atelier/influences-atelier.md` (note 10 : HPMOR)

### Fiabilité
- **Solide :** [1], [2], [3], [4], [5], [6], [7], [8], [13], [14] et tes propres CSV (données datées, récoltées avec méthode et limites déclarées).
- **Correct mais secondaire :** [9], [12], [16]-[18].
- **Faible / à ne pas citer :** [11].
- **Non établi :** « > 1 M$ de Patreon cumulés », « 1,9 M de mots pour *Taylor Varga* », « vues = lecteurs » (une vue mensuelle n'est pas une personne), « sans publicité » (non vérifié).
