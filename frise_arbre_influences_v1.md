# Frise chronologique et réseau d’influences — version 1

**Périmètre :** les œuvres et liens nommés dans la demande, complétés seulement par les antécédents nécessaires pour vérifier ces liens.  
**Date de vérification :** 5 octobre 2026.  
**Important :** ce document synthétise des sources publiques ; il ne remplace pas tes données de lecteurs. Je n’ai pas consulté ni recopié ton dépôt. Pour intégrer précisément tes notes sur Gege Akutami, colle ici les extraits ciblés que tu veux utiliser. Les fichiers [relations_influences_v1.csv](relations_influences_v1.csv) (séparateur `;`) et [relations_influences_v1.json](relations_influences_v1.json) donnent les liens et leur niveau de preuve ; ce sont des cartes de recherche secondaire, pas un export de données de lecteurs.

## 1. Légende : ne pas confondre ressemblance et influence

- **══▶ Influence attestée** : déclaration d’auteur, d’éditeur ou description officielle suffisamment explicite. La portée peut être limitée à un élément (un dessin, un arc, une technique), pas à l’œuvre entière.
- **─[médiation]▶** : influence documentée, mais transmise par une décision éditoriale ou un contexte de travail.
- **···▶ Parenté de genre / contexte historique** : rapprochement utile, sans preuve que l’œuvre A a causé l’œuvre B.
- **?▶ Non vérifié** : lien proposé pour lequel je n’ai pas trouvé de source suffisante ; ce n’est pas une flèche d’influence.
- **[U]** : influence déclarée par toi pour ton projet. C’est un fait sur ta liste de références, pas une décision de conception ni une affirmation vérifiée sur le contenu de ton projet.

Les genres sont des étiquettes dominantes, non exclusives. Le « moteur narratif » ci-dessous est une lecture structurelle de ce qui fait avancer chaque récit, pas une formule officielle de l’auteur.

## 2. Verdicts rapides sur les liens à corriger

| Lien / hypothèse | Verdict | Formulation plus juste |
|---|---|---|
| Jackie Chan → *Dragon Ball* | **Attesté** | Toriyama dit avoir regardé *Drunken Master* de nombreuses fois ; son intérêt pour les films de kung-fu a conduit son éditeur à lui suggérer un manga de kung-fu, d’abord expérimenté avec *Dragon Boy*. Toriyama cite aussi Bruce Lee. [7](https://www.kanzenshuu.com/translations/seg-story-volume-truth-about-dragon-ball/) [5](https://www.forbes.com/sites/olliebarder/2016/10/15/kazuhiko-torishima-on-shaping-the-success-of-dragon-ball-and-the-origins-of-dragon-quest/) |
| *Journey to the West* → *Dragon Ball* | **Attesté** | C’est le classique chinois qui fournit à Toriyama une base d’aventure, de personnages et d’images. Le projet initial se transforme ensuite : *Dragon Ball* n’est pas une simple adaptation. À ne pas confondre avec le « Voyage du héros » de Campbell. [7](https://www.kanzenshuu.com/translations/seg-story-volume-truth-about-dragon-ball/) [8](https://www.kanzenshuu.com/translations/dr-mashiritos-ultimate-manga-technique-ultimate-interview-vol-1/) |
| « Voyage du héros » → *Dragon Ball* | **Non attesté comme influence directe** | On peut lire certains passages avec le modèle du voyage initiatique, mais je n’ai pas trouvé de déclaration de Toriyama citant Campbell. À représenter comme **grille d’analyse**, pas comme flèche causale. |
| *Kinnikuman* → *Dragon Ball* | **Attesté, portée modeste** | Toriyama écrit qu’il consulte *Kinnikuman* comme référence pour dessiner son propre manga. Cela ne prouve pas que chaque trope ou arc de *Dragon Ball* en dérive. [2](https://www.kanzenshuu.com/translations/akira-toriyama-tankobon-ask-me-anything/) |
| *Ring ni Kakero* → *Dragon Ball* | **Non vérifié directement** | C’est une série antérieure de boxe/action avec championnats et adversaires successifs ; je n’ai pas trouvé d’attribution directe de Toriyama. Garder la série comme repère historique, pas comme une flèche solide. |
| *Hokuto no Ken* → évolution de *Dragon Ball* | **Documenté, mais par l’éditeur** | Kazuhiko Torishima dit avoir étudié *Hokuto no Ken* quand la popularité de *Dragon Ball* baissait, puis avoir ajusté la direction éditoriale de *Dragon Ball*. Ce n’est pas la même chose que dire que Toriyama a conçu le manga à l’origine sous l’influence de *Hokuto*. La source disponible est une traduction d’entretien publiée secondairement. [1](https://thedaoofdragonball.com/blog/interviews/akira-toriyama-editor-says-there-is-nothing-to-learn-from-dragon-ball/) |
| *Hokuto no Ken* → premiers *JoJo* | **Attesté / bien étayé** | Le rapprochement porte surtout sur la musculature, la violence visuelle et l’esthétique des premiers épisodes de *JoJo*, pas sur toutes les parties de la série. [1](https://screenrant.com/fist-north-star-jojo-berserk-influence-manga/) |
| *Saint Seiya* → *Yu Yu Hakusho* | **Non vérifié** | Même voisinage éditorial et même grande famille de shōnen d’action, mais pas de déclaration directe retrouvée. Ne pas dessiner de flèche causale. |
| *JoJo* → *Yu Yu Hakusho* / *Hunter × Hunter* | **Lien spécifique, pas généalogie globale** | Les pouvoirs de « territoire » de l’arc Sensui de *Yu Yu Hakusho* sont rapportés comme inspirés des Stands ; *JoJo* est aussi cité comme modèle pour l’élaboration du Nen. Cela ne veut pas dire que *Yu Yu Hakusho* entier vient de *JoJo*. La formulation repose sur des comptes rendus secondaires/fan de déclarations et doit rester circonscrite. [4](https://jojowiki.com/List_of_References_to_JoJo) [1](https://www.cbr.com/jojos-bizarre-adventure-part-4-yu-yu-hakusho/) |
| *Yu Yu Hakusho* → *Naruto* | **Attesté pour des éléments précis** | Kishimoto cite la technique de Suzaku comme modèle du Kage Bunshin et Hiei comme inspiration de Sasuke. Ce n’est pas une filiation totale entre les deux œuvres. Source : traduction de l’entretien Togashi–Kishimoto, diffusée par une page de fans. [1](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Yoshihiro_Togashi_x_Masashi_Kishimoto_interview) |
| *Hunter × Hunter* → *Naruto* | **Attesté pour un aspect précis** | Kishimoto cite *Hunter × Hunter* pour l’étude des expressions des personnages lors des révélations de puissance ou de danger. Là encore, pas une dérivation générale de *Naruto*. [1](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Yoshihiro_Togashi_x_Masashi_Kishimoto_interview) |
| *Yu Yu Hakusho* → *Bleach* | **Non attesté par les sources consultées** | Kubo nomme plutôt *GeGeGe no Kitarō* et *Saint Seiya* comme influences de jeunesse, et l’entretien lui fait reconnaître leur présence dans *Bleach*. La parenté de ton surnaturel ne suffit pas à établir une flèche *Yu Yu* → *Bleach*. [2](https://www.liveabout.com/interview-tite-kubo-2282834) |
| *One Piece* → *Fairy Tail* | **Non vérifié** | Mashima parle de *Dragon Ball*, de *Dragon Quest*, de *Rave Master* et de l’ambiance de groupe qu’il voulait créer ; cela ne confirme pas *One Piece* comme source directe de *Fairy Tail*. [1](https://www.animenewsnetwork.com/interview/2008-08-17/hiro-mashima) |
| *Fairy Tail* → *Radiant* | **Influence majeure non établie** | Valente rapporte qu’il avait lu deux tomes de *Fairy Tail* et qu’il a modifié des éléments après qu’on lui a signalé des ressemblances. Il cite séparément *Dragon Ball*, *Naruto* et *One Piece* comme influences de lecture/création. La relation avec *Fairy Tail* est donc surtout une **ressemblance remarquée puis corrigée**, pas une filiation principale. [1](https://www.bodoi.info/tony-valente-on-a-le-droit-de-dessiner-du-manga-en-france/) [3](https://asiapacificarts.org/2018/11/28/nycc-interview-radiant-manga-creator-tony-valente/) |
| *Naruto* → *My Hero Academia* | **Attesté pour le découpage / la mise en scène de cases** | Horikoshi dit avoir consulté *Naruto* pour le cadrage de certaines scènes. Éviter d’en faire une influence sur toute la conception de *MHA*. La source accessible est une traduction de l’entretien Horikoshi–Kishimoto, relayée secondairement. [2](https://www.resetera.com/threads/interview-between-horikoshi-my-hero-academia-and-kishimoto-naruto.238057/) |
| *Watchmen* → *Worm* | **Influence directe non confirmée** | *Watchmen* est un repère historique de la révision du super-héros, mais Wildbow ne le confirme pas comme influence directe dans l’entretien retrouvé. Il dit qu’il est difficile de réduire *Worm* à quelques influences ; il attribue explicitement à *Legion of Nothing* et *Tales of MU* le fait de lui avoir donné confiance dans le format web-serial. La question de l’intervieweur propose *Watchmen* ; la réponse de Wildbow ne valide pas cette flèche. [1](https://t4nky.wordpress.com/2015/07/02/interview-with-wildbow/) |
| *Harry Potter and the Methods of Rationality* → *Mother of Learning* | **Non vérifié** | *Mother of Learning* a commencé sur FictionPress en 2011 ; son auteur cite les fandoms *Harry Potter* et *Naruto* parmi des inspirations mineures, mais je n’ai pas trouvé de déclaration citant spécifiquement *HPMOR*. L’ordre chronologique ne prouve pas le lien. [2](https://www.royalroad.com/fiction/21220/mother-of-learning) [3](https://www.fictionpress.com/~nobody103) |

## 3. Frise chronologique — œuvres, genres et moteurs

Les dates indiquent la première publication/sérialisation repérée, pas la date de traduction française ; lorsqu’une plage est donnée, elle correspond à la parution originale, pas à l’arrivée dans une autre langue. Certaines dates de manga varient selon que la source retient le numéro daté du magazine ou sa date de mise en vente.

| Date / période | Œuvre ou tradition | Genre dominant | Moteur narratif | Place dans le réseau / preuve |
|---|---|---|---|---|
| XVIᵉ siècle (source littéraire) | *Journey to the West* (*La Pérégrination vers l’Ouest*) | Roman classique chinois d’aventure fantastique | Pèlerinage, étapes, épreuves et rencontres surnaturelles | Source explicitement utilisée par Toriyama pour la base de *Dragon Ball*. [8](https://www.kanzenshuu.com/translations/dr-mashiritos-ultimate-manga-technique-ultimate-interview-vol-1/) |
| 1949, comme cadre théorique — pas comme source attestée | Joseph Campbell, *The Hero with a Thousand Faces* (« voyage du héros ») | Modèle de mythologie comparée, pas un genre | Séparation, épreuves, transformation/retour dans ses formulations usuelles | **Pas de preuve** que Toriyama l’ait utilisé. Le distinguer du roman chinois ci-dessus. [1](https://en.wikipedia.org/wiki/The_Hero_with_a_Thousand_Faces) |
| 1977–1981 | *Ring ni Kakero* | Shōnen sportif, boxe et action | Entraînement, adversaires de plus en plus forts, championnats et combats d’équipe | Antécédent de manga de combat/tournoi ; influence directe sur *Dragon Ball* non vérifiée. [4](https://tv.apple.com/be/show/ring-ni-kakero/umc.cmc.1fqvwy18hx1ctd86f7mc437ep) |
| 1978 | *Drunken Master* et films de Jackie Chan cités par Toriyama | Action de kung-fu, souvent teintée de comédie | Chorégraphie, improvisation et résolution physique des affrontements | Influence directe sur l’impulsion kung-fu de Toriyama et *Dragon Boy* / *Dragon Ball*. [7](https://www.kanzenshuu.com/translations/seg-story-volume-truth-about-dragon-ball/) |
| 1979–1987 | *Kinnikuman* | Action-comédie, catch, sport fantastique | Tournois, défis, rivalités et changements d’échelle | Toriyama l’utilisait comme référence graphique ; Togashi le cite aussi comme modèle de transition vers le combat. [2](https://www.kanzenshuu.com/translations/akira-toriyama-tankobon-ask-me-anything/) [2](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Jump_Ryu_Vol.21:_Yoshihiro_Togashi) |
| 1983–1988 | *Hokuto no Ken* | Action post-apocalyptique, arts martiaux | Survie dans les terres désolées, protection des victimes, duels contre des oppresseurs | Hara cite notamment *Mad Max 2*, Bruce Lee et le cinéma d’action ; Torishima l’étudie plus tard pour réorienter *Dragon Ball*. [10](https://geekculture.co/fist-of-the-north-star-creator-tetsuo-hara-mad-max-furiosa-george-miller/) [5](https://www.viz.com/blog/posts/exclusive-q-a-with-legendary-creator-tetsuo-hara) [1](https://thedaoofdragonball.com/blog/interviews/akira-toriyama-editor-says-there-is-nothing-to-learn-from-dragon-ball/) |
| 1984–1995 | *Dragon Ball* | Aventure fantastique, arts martiaux, shōnen de combat | D’abord quête des Dragon Balls et exploration ; puis entraînement, tournois et affrontements à escalade croissante | Sources directes : films de kung-fu, *Journey to the West*, référence graphique à *Kinnikuman* ; évolution éditoriale influencée par l’étude de *Hokuto*. [2](https://www.kanzenshuu.com/manga/weekly-jump/) [7](https://www.kanzenshuu.com/translations/seg-story-volume-truth-about-dragon-ball/) |
| 1986–1990 | *Saint Seiya* | Fantasy mythologique, action et combat shōnen | Chevaliers, armures, entraînement, missions et duels pour défendre Athéna | Kubo cite *Saint Seiya* comme influence de jeunesse et reconnaît une empreinte sur l’armement et les scènes de bataille de *Bleach*. Pas de flèche attestée vers *Yu Yu Hakusho*. [3](https://ultimatepopculture.fandom.com/wiki/Saint_Seiya) [2](https://www.liveabout.com/interview-tite-kubo-2282834) |
| 1986–1987 | *Watchmen* | Fiction super-héroïque, thriller politique et critique du genre | Enquête, conspiration et confrontation de visions politiques et morales | Jalons de la révision du super-héros ; contexte historique pour lire *Worm*, pas influence directe démontrée. [9](https://en.wikipedia.org/wiki/Watchmen) |
| 1987– | *JoJo’s Bizarre Adventure* | Aventure surnaturelle, action, fantastique/gothique selon les parties | Affrontements successifs résolus par capacités, observation et ruse ; protagonistes et périodes renouvelés | Influence visuelle de *Hokuto* surtout au début ; Stands → territoires de *Yu Yu* et, selon les comptes rendus consultés, Nen de *HxH*. [1](https://en.wikipedia.org/wiki/JoJo%27s_Bizarre_Adventure) [1](https://screenrant.com/fist-north-star-jojo-berserk-influence-manga/) [4](https://jojowiki.com/List_of_References_to_JoJo) |
| 1990–1994 | *Yu Yu Hakusho* | Surnaturel, enquête occulte puis action/combat | Cas de détective spirituel au début, puis tournois et conflits d’arts martiaux | Togashi cite *Kinnikuman* comme modèle de bascule d’une forme plus comique/épisodique vers le combat ; influences ponctuelles de *JoJo* rapportées pour les pouvoirs de territoire. [4](https://en.wikipedia.org/wiki/YuYu_Hakusho) [2](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Jump_Ryu_Vol.21:_Yoshihiro_Togashi) |
| 1994 (manga) ; 1995–1996 (TV) ; 1997 (*The End of Evangelion*) | *Neon Genesis Evangelion* | Science-fiction apocalyptique, mecha et drame psychologique | Défense contre les Anges, fonctionnement de l’institution et crise intérieure des personnages | Akutami cite *Evangelion* comme influence de jeunesse, notamment pour son imagerie mythologique ; il dit avoir choisi un registre bouddhiste différent. La série TV n’a donc pas commencé en 1998. [1](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion_(manga)) [2](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion) [1](https://en.wikipedia.org/wiki/The_End_of_Evangelion) [1](https://edomonogatari.wordpress.com/2021/03/14/akutami-kubo/) |
| 1997 (R.-U.) ; 1998 (États-Unis) | *Harry Potter à l’école des sorciers* | Fantasy jeunesse, école de magie, récit d’apprentissage | Année scolaire, apprentissage, mystères et quête | Première publication britannique en 1997 ; 1998 est la première édition américaine, pas la première parution mondiale. [1](https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone) |
| 1997– | *One Piece* | Aventure de pirates, fantasy et récit d’équipage | Exploration, recrutement d’alliés et quête du One Piece | Oda attribue à *Vicky le Viking* son intérêt d’enfant pour les pirates ; il reconnaît aussi l’importance de *Dragon Ball* pour son parcours et son œuvre. [5](https://www.thegrandline.com/odaaeraint.htm) [3](https://animehunch.com/oda-reveals-he-was-influenced-by-dragon-balls-art-style/) |
| 1998– | *Hunter × Hunter* | Aventure fantastique et manga de combat stratégique | Examen, chasse, missions et conflits où l’information et les règles de pouvoir comptent | Autre œuvre de Togashi, donc une continuité d’auteur ; JoJo est rapporté comme une influence pour le Nen. Ne pas la présenter comme une œuvre dérivée de *Yu Yu Hakusho*. [5](https://en.wikipedia.org/wiki/Yoshihiro_Togashi) [1](https://www.cbr.com/jojos-bizarre-adventure-part-4-yu-yu-hakusho/) |
| 1999–2014 | *Naruto* | Aventure ninja, coming-of-age et action | Missions d’équipe, entraînement, rivalité et recherche de reconnaissance | Emprunts déclarés et ciblés à *Yu Yu Hakusho* et *Hunter × Hunter*. [1](https://en.wikipedia.org/wiki/Naruto) [1](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Yoshihiro_Togashi_x_Masashi_Kishimoto_interview) |
| 2001–2016 | *Bleach* | Action surnaturelle, shōnen de combat | Missions de Shinigami, protection et sauvetage dans des conflits avec des esprits/ennemis | Kubo cite *GeGeGe no Kitarō* et *Saint Seiya* ; il ne confirme pas ici *Yu Yu Hakusho* comme source directe. [1](https://en.wikipedia.org/wiki/Bleach_(manga)) [2](https://www.liveabout.com/interview-tite-kubo-2282834) |
| 2006–2017 | *Fairy Tail* | Fantasy d’action, magie, comédie et aventure de groupe | Quêtes de guilde, combats et dynamique de communauté/famille choisie | Mashima dit que l’ambiance de bar et de groupe, ainsi que la communauté, ont inspiré le cœur de la guilde ; *Dragon Ball* est son manga favori d’enfance, sans être à lui seul le pitch de *Fairy Tail*. Pas de source directe solide pour *One Piece* → *Fairy Tail*. [1](https://www.animenewsnetwork.com/interview/2008-08-17/hiro-mashima) [2](https://en.wikipedia.org/wiki/Fairy_Tail) |
| 2010–2015 | *Harry Potter and the Methods of Rationality* (HPMOR) | Fanfiction de *Harry Potter*, fantasy spéculative/rationaliste | Réinterprétation des règles du monde par l’expérimentation, l’argumentation et la résolution de problèmes | Dérive explicitement de *Harry Potter* ; aucune preuve que ce texte influence *Mother of Learning*. [2](https://www.fanfiction.net/s/5782108/1/Harry-Potter-and-the-Methods-of-Rationality) [1](https://en.wikipedia.org/wiki/Harry_Potter_and_the_Methods_of_Rationality) |
| 2011 (première publication sur FictionPress) | *Mother of Learning* | Fantasy d’école de magie, boucle temporelle et progression | Répéter une période, conserver les acquis, augmenter connaissances et compétences, puis résoudre le problème de fond | L’auteur cite notamment les jeux *Exile/Avernum*, D&D et *Fullmetal Alchemist* ; les fandoms *Harry Potter* et *Naruto* sont des inspirations mineures. Le récit a commencé sur FictionPress, puis a été mis sur Royal Road : ne pas confondre origine de l’œuvre et plateforme ultérieure. [3](https://www.fictionpress.com/~nobody103) [2](https://www.royalroad.com/fiction/21220/mother-of-learning) |
| 2011–2013 | *Worm* | Fiction super-héroïque spéculative, web-serial | Conflits de pouvoirs, décisions tactiques, institutions et conséquences sociales | Wildbow cite *Legion of Nothing* et *Tales of MU* comme ayant rendu le format web-serial plus envisageable pour lui ; il refuse une généalogie simple. **Aucun élément narratif au-delà de l’arc 10 n’est détaillé ici.** [5](https://balloondaycreative.wordpress.com/2017/02/18/today-i-asked-wildbow/) [1](https://t4nky.wordpress.com/2015/07/02/interview-with-wildbow/) |
| 2013– | *Radiant* | Fantasy d’aventure, « manfra »/shōnen | Chasse aux Némésis, quête de Seth pour les vaincre et progression de sorcier | Valente cite *Dragon Ball*, *Naruto* et *One Piece* ; les ressemblances avec *Fairy Tail* ont entraîné des modifications conscientes. [3](https://www.europecomics.com/author/tony-valente/) [1](https://www.bodoi.info/tony-valente-on-a-le-droit-de-dessiner-du-manga-en-france/) [3](https://asiapacificarts.org/2018/11/28/nycc-interview-radiant-manga-creator-tony-valente/) |
| 2014–2024 | *My Hero Academia* | Super-héros, école et action | Formation à Yuei, exercices, stages et missions de héros | Influence déclarée de *Naruto* sur la mise en scène de certaines cases ; ne pas étendre cette flèche à toute l’histoire. [2](https://www.anniversaryjump.com/debuts?lang=en) [2](https://www.resetera.com/threads/interview-between-horikoshi-my-hero-academia-and-kishimoto-naruto.238057/) |
| 2015–2023 | *Black Clover* | Fantasy magique et action shōnen | Équipes de chevaliers-mages, rivalité et ambition de devenir Empereur-Mage | Tabata cite *Berserk* comme modèle pour les décors, combats et histoire, en visant un manga dans cet esprit mais en style shōnen ; *Dragon Ball* l’a inspiré à devenir mangaka et est rapporté comme référence de mise en scène des combats. *Bleach* est rapporté comme influence/favori avec une portée moins précise ; pas de flèche forte vers *Fairy Tail* ou *Naruto*. [2](https://www.anniversaryjump.com/debuts?lang=en) [10](https://en.wikipedia.org/wiki/Black_Clover) [11](https://www.lepoint.fr/pop-culture/black-clover-le-meilleur-manga-de-fantasy-explique-par-son-auteur-07-07-2018-2233981_2920.php) [12](https://blog.francetvinfo.fr/popup/2018/09/18/dragon-ball-ma-donne-envie-de-faire-ce-metier-entretien-avec-yuki-tabata-lauteur-du-shonen-manga-black-clover.html) |
| 2016 | *Demon Slayer* | Fantasy historique, chasse aux démons et action | Protéger sa sœur, chercher un remède et progresser dans le Corps des pourfendeurs | Gotouge cite trois influences majeures : *JoJo*, *Naruto* et *Bleach*, et non *Bleach* seul. [2](https://otakuusamagazine.com/koyoharu-gotoge-reveals-manga-inspired-demon-slayer/) [2](https://www.anniversaryjump.com/debuts?lang=en) |
| 2018–2024 | *Jujutsu Kaisen* | Fantasy urbaine occulte, horreur et shōnen de combat | Missions/exorcismes de fléaux, règles de pouvoirs et affrontements | Akutami cite explicitement *Bleach*, *Hunter × Hunter* et *Evangelion* ; l’imagerie mythologique d’*Evangelion* l’a poussé à choisir une autre voie, notamment bouddhiste. [1](https://edomonogatari.wordpress.com/2021/03/14/akutami-kubo/) [2](https://www.anniversaryjump.com/debuts?lang=en) [3](https://en.wikipedia.org/wiki/Jujutsu_Kaisen) |
| 2020 (one-shot) ; 2021 (sérialisation) | *The Hunters Guild: Red Hood* | Fantasy d’action surnaturelle, chasse aux monstres et contes sombres | Menace locale, contrat de guilde, chasse, épreuves et formation | VIZ présente l’œuvre comme une relecture sombre des contes de Grimm et précise que Kawaguchi a été assistant de Horikoshi. C’est une donnée de parcours professionnel, **pas** une preuve de copie ou d’influence graphique précise. [1](https://www.viz.com/hunters-guild-red-hood) |

## 4. Arbre / réseau d’influences corrigé

### A. Arts martiaux, aventure et premières formes du manga de combat

```text
Journey to the West ──[Toriyama le cite]─────────────────────┐
Films de kung-fu, dont Jackie Chan / Drunken Master ─────────┼──▶ Dragon Ball
Kinnikuman ──[Toriyama l’utilise comme référence graphique]──┘

Ring ni Kakero ············································> contexte historique du manga de combat
                                                              (pas de flèche directe attestée vers Dragon Ball)

Mad Max 2 + Bruce Lee + cinéma d’action ──[Hara]──────────────▶ Hokuto no Ken
Hokuto no Ken ──[étude de Torishima, éditeur]─────────────────▶ réorientation éditoriale de Dragon Ball
Hokuto no Ken ──[surtout style des premiers épisodes]────────▶ JoJo
```

Le lien *Hokuto no Ken* → *Dragon Ball* est donc bien réel au niveau de l’histoire éditoriale, mais il est **médié par Torishima**. Toriyama, lui, attribue les bases initiales à ses films de kung-fu et à *Journey to the West*. [5](https://www.forbes.com/sites/olliebarder/2016/10/15/kazuhiko-torishima-on-shaping-the-success-of-dragon-ball-and-the-origins-of-dragon-quest/) [1](https://thedaoofdragonball.com/blog/interviews/akira-toriyama-editor-says-there-is-nothing-to-learn-from-dragon-ball/)

### B. Shōnen d’action : flèches courtes et précises

```text
Kinnikuman ──[modèle de bascule comédie → combat]─────────────▶ Yu Yu Hakusho
JoJo / Stands ──[pouvoirs de territoire, arc Sensui]─────────▶ Yu Yu Hakusho
JoJo / Stands ──[modèle rapporté pour les capacités]─────────▶ Hunter × Hunter / Nen

Yu Yu Hakusho / Suzaku ──[technique]─────────────────────────▶ Naruto / Kage Bunshin
Yu Yu Hakusho / Hiei ────[personnage et traits]──────────────▶ Naruto / Sasuke
Hunter × Hunter ─────────[expressions en scènes de danger]──▶ Naruto

Saint Seiya ─────────────[armes et scènes de combat]────────▶ Bleach
GeGeGe no Kitarō ────────[yōkai et dessin de personnages]──▶ Bleach
Bleach ──────────────────┐
Hunter × Hunter ─────────┼──[Akutami les nomme]─────────────▶ Jujutsu Kaisen
Evangelion ──────────────┘  [mythologie, puis choix d’un registre distinct]

JoJo ────────────────┐
Naruto ──────────────┼──[Gotouge cite ces trois séries]────▶ Demon Slayer
Bleach ──────────────┘

Naruto ──[cadrage/paneling de scènes précises]──────────────▶ My Hero Academia
```

Les cases marquées par une précision d’arc/personnage ne doivent pas être généralisées à toute l’œuvre. En particulier : **pas de flèche attestée *Saint Seiya* → *Yu Yu Hakusho* ; pas de flèche directe *Yu Yu Hakusho* → *Bleach*.**

### C. Aventure, guildes et fantasy shōnen

```text
Vicky le Viking ──[intérêt d’Oda pour les pirates]────────────▶ One Piece
Dragon Ball ──────[admiration/influence reconnue par Oda]────▶ One Piece

Dragon Ball ──────[manga favori / formation de Mashima]──────▶ Fairy Tail (contexte d’auteur)
Rave Master ──────[expérience et idée de la communauté]──────▶ Fairy Tail
Ambiance de bar + groupe d’amis ──[Mashima]─────────────────▶ Fairy Tail

Dragon Ball ──────┐
Naruto ────────────┼──[Valente les cite]────────────────────▶ Radiant
One Piece ────────┘
Fairy Tail ·········[ressemblances signalées, éléments changés]···> Radiant

Dragon Ball ──────[mouvement et dynamique des combats]───────▶ Black Clover
Berserk ──────────[ambition de fantasy plus sombre en shōnen]▶ Black Clover
Bleach ───────────[influence rapportée, portée à préciser]───▶ Black Clover

Contes de Grimm ──[relecture explicitement présentée par VIZ]▶ The Hunters Guild: Red Hood
Horikoshi ────────[assistanat de Kawaguchi]─────────────────▶ contexte professionnel de Red Hood
                              (ne prouve pas une influence graphique précise)
```

### D. Super-héros et *Worm* : contexte, non filiation inventée

```text
Bronze Age des comics US (périodisation informelle)
                 ···▶ révision du super-héros des années 1980
Watchmen (1986–87) ···▶ contexte historique / comparaison critique
                 ···▶ famille de récits à laquelle on peut comparer Worm

Legion of Nothing ──[Wildbow : a rendu le web-serial envisageable]──▶ Worm / format
Tales of MU ────────[Wildbow : a rendu le web-serial envisageable]──▶ Worm / format
```

Le « Bronze Age » est généralement placé autour de 1970–1985, mais les bornes sont informelles et désignent une **périodisation des comics américains**, pas des mangas. Il résulte d’une évolution graduelle vers des récits plus sociaux, adultes et parfois plus sombres ; il n’a pas été déclenché par un seul titre. *Watchmen* et *The Dark Knight Returns* sont des jalons emblématiques de la transition vers le « Modern Age » autour du milieu des années 1980, mais ils n’inventent pas à eux seuls la critique du super-héros. « Dark Age » est une appellation courante mais discutée, pas une période universellement définie. Éviter donc le récit causal simpliste « Bronze Age → *Watchmen* → âge sombre → *Worm* ». [1](https://en.wikipedia.org/wiki/Bronze_Age_of_Comic_Books) [8](https://en.wikipedia.org/wiki/Events_from_the_Modern_Age_of_Comic_Books) [9](https://en.wikipedia.org/wiki/Watchmen)

Dans cette carte, « déconstruction du super-héros » est une **lecture critique possible**, pas une déclaration de Wildbow. L’influence directe de format la mieux documentée est celle des web-serials qu’il nomme. La description de *Worm* reste volontairement sans révélations au-delà de l’arc 10.

### E. Fanfiction, boucle temporelle et progression

```text
Harry Potter ──[univers source]──────────────────────────────▶ HPMOR
Harry Potter / Naruto (fandoms, influence mineure déclarée)──▶ Mother of Learning
HPMOR ···················································?▶ Mother of Learning
                         (aucune influence directe vérifiée)
```

*Mother of Learning* est une fantasy de progression et de boucle temporelle ; son moteur est l’accumulation de savoir et de compétences au fil des répétitions. Cela ne la transforme pas automatiquement en xianxia/cultivation : il faut distinguer **moteur de progression** et **tradition de genre**.

## 5. Wuxia, xianxia/cultivation et progression fantasy

| Terme | Ce que le genre met au centre | Moteur fréquent | Comment le relier à la carte |
|---|---|---|---|
| **Wuxia** | Héros martiaux, monde du *jianghu*, loyauté, justice, honneur, rivalités et techniques | Errance, vengeance, duel, protection d’autrui ou conflit entre écoles/clans | Tradition chinoise d’arts martiaux et de chevalerie ; ce n’est pas simplement « tout manga où l’on s’entraîne ». |
| **Xianxia / cultivation** | Fantasy chinoise liée à la culture du *qi*, à des pratiques de cultivation et souvent à la quête d’immortalité | Entraînement, percées de niveau, sectes, épreuves et ascension | Développement fantastique apparenté au wuxia, mais distinct par le poids du surnaturel et de l’ascension. |
| **Progression fantasy** | Catégorie anglophone centrée sur une progression lisible des capacités, du savoir ou du rang | Apprentissage, entraînement, répétition, défis de niveau | Peut recouvrir des récits de cultivation ou des œuvres occidentales comme *Mother of Learning* ; ce n’est pas une origine culturelle unique. |

Ces traditions ont des continuités, mais ne sont pas synonymes. L’étude sur la fiction chinoise en ligne décrit le xianxia comme un développement fantastique de traditions martiales, avec cultivation du *qi* et aspiration à l’immortalité ; elle ne justifie pas de tracer une flèche directe vers les mangas japonais cités ici. [1](https://www.nature.com/articles/s41599-024-04256-y)

**À retenir :** *Dragon Ball* a des racines chinoises et cinématographiques documentées, mais le classer comme « wuxia » au sens strict effacerait son identité de shōnen japonais de fantasy/action. De même, entraînement, tournoi et niveaux de puissance sont des moteurs qu’on retrouve dans plusieurs traditions sans prouver une influence directe entre toutes les œuvres concernées.

## 6. Ton projet : registre des influences que tu as déclarées

Ce tableau **classe les références**, mais ne décide pas ce que ton projet doit en faire.

| Référence déclarée [U] | Type de nœud | Genre / moteur attribuable sans extrapolation | Ce qu’il manque pour préciser la relation |
|---|---|---|---|
| *Worm* / Wildbow | Œuvre + auteur | Super-héros spéculatif, web-serial ; conflits de pouvoirs et rapports entre personnages/institutions | Quel aspect précis tu veux suivre ; pour *Worm*, rester dans la limite de lecture fixée (arc 10). |
| Tarantino | Auteur/réalisateur, pas une œuvre unique | Impossible d’attribuer un seul genre ou moteur à toute sa filmographie | Film(s) et élément(s) concernés ; je ne déduis pas « dialogues », « violence » ou « non-linéarité » sans ta précision. |
| SCP | Corpus collaboratif / univers de fiction | Horreur et fiction spéculative, mais moteur variable selon le récit ou le dossier | Article(s), branche(s) ou format(s) précis. |
| Brandon Sanderson | Auteur, pas une œuvre unique | Fantasy, mais le système et le moteur varient selon le livre | Titre(s) concerné(s) ; ne pas attribuer une technique à tout l’auteur. |
| Togashi | Auteur ; nœuds disponibles dans la carte : *Yu Yu Hakusho*, *Hunter × Hunter* | Combat stratégique, enquête/aventure selon l’œuvre | Quelle œuvre et quel aspect de Togashi tu vises. |
| *One Piece* | Œuvre | Aventure de pirates ; exploration et quête de l’équipage | Aspect précis non indiqué. |
| *Naruto* | Œuvre | Aventure ninja ; missions, formation, équipe et rivalité | Aspect précis non indiqué. |
| Gege Akutami / *Jujutsu Kaisen* | Auteur + œuvre | Fantasy urbaine occulte ; enquêtes/missions d’exorcisme et affrontements à règles | Pour le dépôt, il faut les extraits ciblés que tu souhaites intégrer ; dépôt non consulté ici. |
| *The Hunters Guild: Red Hood* | Œuvre | Fantasy de contes sombres et chasse aux monstres ; contrats, épreuves et guilde | Aspect précis non indiqué. |
| Occultisme | Corpus de pratiques et de textes | Pas un genre ou un moteur unique | Traditions, périodes et sources précises. |
| Colin de Plancy | Auteur / source documentaire | *Dictionnaire infernal* : ouvrage de démonologie, pas fiction à moteur narratif | Entrées ou éditions que tu mobilises. |
| Runeterra | Univers fictionnel de *League of Legends* | Monde partagé ; moteurs variables selon le récit, la région ou le personnage | Région, époque et textes/lore précis. |
| Super-héros | Famille de genres/conventions | Les moteurs varient : identité, mission, responsabilité, institutions, etc. | Tradition ou œuvres de référence. |
| Folklore et légendes | Corpus de traditions | Moteur variable : quête, tabou, épreuve, métamorphose, dette, etc. | Récits et cultures précis. |

Tous les liens de ces références vers ton projet sont enregistrés en **[U] déclaration utilisateur** : ils ne sont pas présentés comme des décisions de conception déjà validées. Le dépôt GitHub demeure ta source primaire pour les données de lecteurs ; la carte ci-dessus est une couche de recherche secondaire distincte.

## 7. Incertitudes à garder visibles

1. **Pas de preuve directe retrouvée** pour *Ring ni Kakero* → *Dragon Ball* ; on garde l’antécédent de genre, pas la causalité.
2. **Pas de preuve retrouvée** pour *Saint Seiya* → *Yu Yu Hakusho* ou *Yu Yu Hakusho* → *Bleach*.
3. *JoJo* → *Yu Yu Hakusho/Hunter × Hunter* est limité à des pouvoirs et des arcs précis ; la base consultée inclut des traductions et des synthèses secondaires.
4. *Black Clover* : *Berserk* et *Dragon Ball* sont les liens les mieux étayés ici ; *Bleach* est rapporté comme influence mais sa portée précise reste moins claire. Pas de preuve solide pour *Fairy Tail* ou *Naruto* comme sources directes déterminantes.
5. *The Hunters Guild: Red Hood* : Grimm est attesté par la présentation éditeur ; l’assistanat auprès de Horikoshi est attesté, mais ne prouve pas à lui seul une influence graphique directe.
6. *Worm* : contexte historique de déconstruction/révision du super-héros, oui ; influence directe de *Watchmen*, non établie par la source consultée.
7. *Mother of Learning* : influence mineure de fandom *Harry Potter* mentionnée par l’auteur ; influence de *HPMOR* non établie.
8. **Dates corrigées :** *Evangelion* = manga en 1994, série TV en 1995–1996, *The End of Evangelion* en 1997 ; *Harry Potter* = première parution UK en 1997, édition US en 1998 ; *Mother of Learning* commence sur FictionPress en 2011 avant son transfert ultérieur sur Royal Road.

## Sources principales utilisées

- Toriyama, propos sur *Dragon Ball*, Jackie Chan, Bruce Lee et *Journey to the West* : traduction de matériel d’entretien par Kanzenshuu [7](https://www.kanzenshuu.com/translations/seg-story-volume-truth-about-dragon-ball/) [8](https://www.kanzenshuu.com/translations/dr-mashiritos-ultimate-manga-technique-ultimate-interview-vol-1/).
- Toriyama sur sa référence à *Kinnikuman* : [2](https://www.kanzenshuu.com/translations/akira-toriyama-tankobon-ask-me-anything/).
- Torishima sur son étude de *Hokuto no Ken* : transcription/traduction secondaire de l’entretien [1](https://thedaoofdragonball.com/blog/interviews/akira-toriyama-editor-says-there-is-nothing-to-learn-from-dragon-ball/).
- Togashi–Kishimoto : traduction fan de l’entretien [1](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Yoshihiro_Togashi_x_Masashi_Kishimoto_interview) ; résumé de l’entretien *Jump Ryu* sur le rôle de *Kinnikuman* [2](https://hunterxhunter.fandom.com/wiki/User_blog:MrGenial11/Jump_Ryu_Vol.21:_Yoshihiro_Togashi).
- Kubo–Akutami : traduction de l’entretien spécial [1](https://edomonogatari.wordpress.com/2021/03/14/akutami-kubo/). Kubo sur *Saint Seiya* et *GeGeGe no Kitarō* : [2](https://www.liveabout.com/interview-tite-kubo-2282834).
- Mashima : entretien Anime News Network [1](https://www.animenewsnetwork.com/interview/2008-08-17/hiro-mashima).
- Tabata : entretien *Le Point* sur *Berserk* et le souhait d’en transposer l’esprit en shōnen [11](https://www.lepoint.fr/pop-culture/black-clover-le-meilleur-manga-de-fantasy-explique-par-son-auteur-07-07-2018-2233981_2920.php) ; entretien Franceinfo sur *Dragon Ball* comme déclencheur de vocation [12](https://blog.francetvinfo.fr/popup/2018/09/18/dragon-ball-ma-donne-envie-de-faire-ce-metier-entretien-avec-yuki-tabata-lauteur-du-shonen-manga-black-clover.html).
- Valente : entretiens BoDoï [1](https://www.bodoi.info/tony-valente-on-a-le-droit-de-dessiner-du-manga-en-france/), Anime News Network [2](https://www.animenewsnetwork.com/feature/2018-10-16/new-york-comic-con-2018-interview-tony-valente-creator-of-radiant/.138241) et Asia Pacific Arts [3](https://asiapacificarts.org/2018/11/28/nycc-interview-radiant-manga-creator-tony-valente/).
- Wildbow : entretien [1](https://t4nky.wordpress.com/2015/07/02/interview-with-wildbow/) ; entretien sur le démarrage de *Worm* [5](https://balloondaycreative.wordpress.com/2017/02/18/today-i-asked-wildbow/).
- Wuxia/xianxia : étude académique publiée par *Humanities and Social Sciences Communications* [1](https://www.nature.com/articles/s41599-024-04256-y).
- *The Hunters Guild: Red Hood* : présentation officielle VIZ [1](https://www.viz.com/hunters-guild-red-hood).
