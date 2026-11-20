-- Données transcrites des rapports lus le 29/09. Chiffres repris tels quels.

UPDATE inspirations SET medium = 'Jeu vidéo / univers transmédia', economie = 'Free-to-play, lore diffusé par cinématiques et skins'
  WHERE nom LIKE 'Runeterra%' AND medium = '';
UPDATE inspirations SET medium = 'Jeu vidéo / MMO', economie = 'Abonnement et extensions'
  WHERE nom LIKE 'Warcraft%' AND medium = '';
UPDATE inspirations SET medium = 'Manga hebdomadaire (WSJ)', economie = 'Prépublication hebdomadaire, ToC par questionnaires, puis volumes reliés'
  WHERE nom = 'The Hunters Guild: Red Hood' AND medium = '';
UPDATE inspirations SET medium = 'Film d''animation', economie = 'Sortie en salles'
  WHERE nom LIKE '%Shrek%' AND medium = '';
UPDATE inspirations SET medium = 'Roman', economie = 'Volumes, forte notoriété transmédia'
  WHERE nom = 'Harry Potter' AND medium = '';
UPDATE inspirations SET medium = 'Jeu vidéo', economie = 'Vente à l''unité'
  WHERE nom LIKE '%BioShock%' AND medium = '';

-- Références déclarées dans le message du 29/09. Statut « référence » : vous dites vouloir
-- les comprendre, pas les avoir retenues.
INSERT INTO inspirations (nom, categorie, statut, ce_que_vous_en_dites, pieges_interpretation, reste_ouvert, medium, economie)
SELECT * FROM (VALUES
  ('Hunter x Hunter', 'Référence à comprendre', 'reference'::statut_inspiration,
   'Référence citée comme restant à comprendre.',
   'Signalé par l''outil : le Nen est souvent cité comme modèle de système « bien expliqué ». Sa densité de règles est indissociable d''un auteur en position de force éditoriale, capable d''imposer des hiatus et des chapitres très verbaux. Ce n''est pas une position de départ.',
   'Ce que vous voulez en tirer : le système de pouvoir, la structure d''arc, le traitement des antagonistes ?',
   'Manga hebdomadaire (WSJ)', 'Prépublication hebdomadaire puis volumes ; hiatus fréquents et tolérés'),
  ('Stormlight Archive', 'Référence à comprendre', 'reference',
   'Référence citée comme restant à comprendre. Déjà couverte par un de vos rapports.',
   'Signalé par l''outil : premier du benchmark Goodreads (4,638 pondéré), mais la trajectoire par tome descend — 4,66 / 4,76 / 4,60 / 4,56 / 4,36. Même le cycle le mieux noté de votre corpus perd de l''altitude au fil des volumes.',
   'Ce que vous en visez : le hard magic, l''architecture d''un cycle long, la construction des personnages ?',
   'Roman (pavés de 1000+ pages)', 'Un volume tous les 3-4 ans ; lectorat de fantasy anglophone adulte'),
  ('Worm', 'Référence à comprendre', 'reference',
   'Référence citée comme restant à comprendre. Nouvelle : absente du document de contexte du 29/09.',
   'Signalé par l''outil : web serial d''environ 1,7 million de mots publié gratuitement à raison de plusieurs chapitres par semaine. Sa densité de pouvoirs et son escalade reposent sur un volume de texte qu''aucun manga en volumes ne peut égaler.',
   'Ce que vous en visez : la taxonomie de pouvoirs, l''escalade, la structure en arcs, le traitement du protagoniste ?',
   'Web serial (prose)', 'Gratuit, rythme très soutenu, financement par dons'),
  ('Progression fantasy', 'Référence à comprendre', 'reference',
   'Genre cité comme restant à comprendre.',
   'Signalé par l''outil : genre construit sur une progression visible et souvent quantifiée, avec un contrat de lecture explicite. Son fonctionnement est indissociable d''une parution très fréquente et d''un retour lecteur immédiat.',
   'Ce que vous en visez : le contrat de progression lui-même, ou seulement des techniques de rythme ?',
   'Web fiction (prose)', 'Royal Road, Kindle Unlimited, Patreon ; parution quasi quotidienne'),
  ('Web fiction', 'Référence à comprendre', 'reference',
   'Domaine cité comme restant à comprendre.',
   'Signalé par l''outil : c''est le seul domaine de vos références où la rétention est directement observable — abonnés, vues par chapitre, décrochage. Voir la proposition enregistrée dans les mécaniques.',
   'Rôle dans le projet non défini.',
   'Web serial (prose)', 'Publication libre, métriques de lecture publiques')
) AS v(nom, categorie, statut, ce_que_vous_en_dites, pieges_interpretation, reste_ouvert, medium, economie)
WHERE NOT EXISTS (SELECT 1 FROM inspirations WHERE nom = 'Worm');

-- Cas d'œuvres : chiffres repris de vos rapports du 22/09.
INSERT INTO cas_oeuvres (titre, marche, periode, resultat, facteurs, "analyse", source, fiabilite)
SELECT * FROM (VALUES
  ('The Hunters Guild: Red Hood', 'Japon (WSJ) + réception occidentale', '18 chapitres, 3 tomes', 'echec'::resultat,
   E'ToC : 1-8 pendant la phase protégée, puis 18-21 du chapitre 9 à la fin.\nAucune page couleur après le chapitre 2.\nProxy retardé du tome 1 : rang moyen 17,71 ; 6 positions sur 7 dans le dernier quart.\nGoodreads : 3,62 puis 3,48 puis 3,29 (851 notes cumulées).\nSensCritique série : 5,6/10 sur 15 notes. MAL : 6,41/10 sur 9 956 notateurs.',
   E'Série axée. Deuxième plus mal notée du corpus des cinq séries courtes sur Goodreads, devant Lock On! seulement.\nValeur du cas : la moyenne brute du tome 1 (8,40) semble correcte ; après décalage éditorial, la réception réelle tombe à 17,71. Illustration de l''écart entre position affichée et réception.\nLa matrice d''arguments recense des lectures divergentes sur le chapitre 5 et le tournant méta du chapitre 15, avec contre-exemples explicites dans les deux sens.',
   'Analyse_Red_Hood_notes_tomes_SensCritique_Goodreads_et_TOC_2026-09-22.md', 'source'::fiabilite),
  ('Naruto', 'International', 'Succès de référence', 'reussite',
   'Goodreads T1 4,41 (251 143 notes) ; T2 4,44. SensCritique T1 7,2/10 ; T2 7,3/10.',
   'Groupe témoin « succès » du corpus. Sélectionné parce qu''il a réussi : voir la vérification enregistrée sur le biais du survivant.',
   'Analyse_notes_tomes_1_2…2026-09-22.md', 'source'),
  ('Jujutsu Kaisen', 'International', 'Succès de référence', 'reussite',
   'Goodreads T1 4,49 (72 793 notes) ; T2 4,46. SensCritique T1 6,8 ; T2 7,1. Signal ToC contemporain du T1 : 14,86e place en fenêtre retardée.',
   'Contre-exemple interne le plus utile du corpus : meilleure note Goodreads actuelle des quatre succès, et pourtant le plus faible signal ToC d''époque. Les notes rétrospectives ne reproduisent pas le jugement hebdomadaire.',
   'Analyse_notes_tomes_1_2…2026-09-22.md', 'source'),
  ('Kagami no Kuni no Harisugawa', 'Japon (WSJ)', '28 chapitres', 'echec',
   'ToC : début à 6,8 de moyenne (ch. 9-14), puis effondrement à 16,67 (ch. 15-20). Goodreads T1 4,07 ; T2 4,20 (hausse).',
   'Le cas le moins évident des cinq axées. Sa note Goodreads monte alors que son ToC s''effondre : les communautés tardives peuvent valoriser une série rejetée en magazine.',
   'Jajanken_comparaison_complete_5_courtes_vs_hits_2026-09-22.md', 'source'),
  ('Tenmaku Cinema', 'Japon (WSJ)', '21 chapitres, 2023', 'echec',
   'Pire profil post-protection des cinq : 100 % des chapitres classables dans le dernier quart. Moyenne post-protection 18,08. Goodreads T1 3,81 ; T2 3,88.',
   'Cas le plus net de rejet hebdomadaire immédiat.',
   'Jajanken_comparaison_complete_5_courtes_vs_hits_2026-09-22.md', 'source'),
  ('Stormlight Archive', 'Anglophone (prose)', '5 tomes parus', 'reussite',
   E'Goodreads pondéré du cycle : 4,638 sur 2 083 194 notes — premier du benchmark fantasy.\nTrajectoire par tome : 4,66 / 4,76 / 4,60 / 4,56 / 4,36.\nThe Way of Kings : la moyenne monte avec le volume de notes (4,58 à 1 243 notes, 4,66 à 727 396).',
   E'Utile pour l''objectif « tenir sur la durée » : le cycle le mieux noté du corpus perd tout de même 0,40 point entre son pic (T2) et son dernier tome.\nDeuxième observation : la moyenne d''un même tome monte avec le temps et la notoriété. Une note actuelle n''est pas la note de lancement.',
   'Benchmark_fantasy_Goodreads_SensCritique_2026-09-20.md + Analyse_complete_Stormlight_Archive_2026-09-27.md', 'source')
) AS v(titre, marche, periode, resultat, facteurs, "analyse", source, fiabilite)
WHERE NOT EXISTS (SELECT 1 FROM cas_oeuvres);

INSERT INTO mecaniques (nom, domaine, exemplifie_par, question, transposition, statut)
SELECT * FROM (VALUES
  ('Contrat de progression', 'Rythme', 'Progression fantasy, Worm',
   'Qu''est-ce qui fait qu''un lecteur revient au chapitre suivant, indépendamment de l''intrigue ?',
   'Vide : à vous de trancher. Le contrat de progression suppose une parution fréquente et un retour immédiat. Un volume tous les six mois chez un éditeur français ne procure ni l''un ni l''autre.',
   'a_verifier'::statut_verif),
  ('Système de pouvoir à règles denses', 'Système de pouvoir', 'Hunter x Hunter (Nen), Stormlight, Worm',
   'Quelle quantité de règles un lecteur accepte-t-il avant que l''explication ne devienne un coût ?',
   E'Vide. Point de friction signalé par l''outil : vos trois références de système viennent de médias à forte capacité d''exposition — prose longue, ou manga d''un auteur en position de force.\nVotre corpus Red Hood recense en sens inverse « l''examen peut différer les plaisirs attendus » et « la mise en scène peut freiner la compréhension ».',
   'a_verifier'),
  ('Escalade sur la durée', 'Structure d''arc', 'Worm, Hunter x Hunter, battle shōnen en général',
   'Comment monter l''enjeu sur des dizaines de tomes sans dévaluer ce qui précède ?',
   'Vide. C''est la mécanique la plus directement liée à votre objectif déclaré de plusieurs dizaines de tomes.',
   'a_verifier'),
  ('Fonctionnalité des personnages', 'Archétypes', 'Red Hood (duo), Runeterra (caractérisation immédiate)',
   'Distinguer reconnaissance visuelle, caractérisation immédiate, profondeur narrative et attachement — quatre choses que votre méthode demande déjà de séparer.',
   'Vide. Votre matrice Red Hood contient des éléments dans les deux sens : le duo est apprécié, et « le casting ne crée pas automatiquement les liens attendus ».',
   'a_verifier'),
  ('Observation directe de la rétention', 'Méthode', 'Royal Road, plateformes de web fiction',
   'Proposition de l''outil, non demandée : la web fiction est le seul domaine de vos références où le décrochage par chapitre est publiquement observable — abonnés, vues, abandons.',
   E'Proposition : puisque vous ne pouvez pas recruter de bêta-lecteurs et que tout votre corpus actuel mesure des notes rétrospectives, ces plateformes offrent la seule courbe d''attrition réelle à votre portée.\nRéserve à peser : lectorat, média et gratuité diffèrent de votre cible. Ce serait un substitut imparfait, pas une solution.',
   'a_verifier')
) AS v(nom, domaine, exemplifie_par, question, transposition, statut)
WHERE NOT EXISTS (SELECT 1 FROM mecaniques);

INSERT INTO verifications (affirmation, nature, statut, constat, source)
SELECT * FROM (VALUES
  ('Red Hood aide à comprendre ce qui plaît au public occidental.',
   'marche'::nature_affirmation, 'nuance'::statut_verif,
   E'Signalé par l''outil. Vos propres données : Goodreads 3,62 → 3,48 → 3,29 sur 851 notes occidentales, deuxième plus mauvaise note des cinq séries axées ; MAL 6,41.\nLe cas est instructif — votre rapport y consacre une section « pourquoi ce cas est particulièrement instructif » — mais il documente une réception occidentale défavorable et déclinante.\nÀ distinguer : référence esthétique (votre section 3), et cas d''étude d''un échec. Les deux sont légitimes, la fusion des deux ne l''est pas.',
   'Analyse_Red_Hood…2026-09-22.md ; Red Hood/matrice_arguments.csv'),
  ('Le plancher Goodreads de 4,10 constitue un seuil éditorial.',
   'marche', 'nuance',
   'Votre benchmark le qualifie de « très exigeant mais réaliste pour un cycle d''élite » : 25 œuvres sur 26 l''atteignent. Le corpus étant composé de cycles d''élite, le seuil décrit ce corpus. Il n''est pas établi comme critère prédictif hors de lui.',
   'Benchmark_fantasy_Goodreads_SensCritique_2026-09-20.md'),
  ('Les signaux ToC du Weekly Shōnen Jump valent pour une publication en volumes chez un éditeur français.',
   'marche', 'a_verifier',
   'Signalé par l''outil et non résolu. Le ToC mesure une rétention hebdomadaire par questionnaires. Ankama, Kana et Glénat n''ont pas ce dispositif. Tout votre appareil ToC dépend de cette question.',
   'À vérifier auprès des éditeurs eux-mêmes')
) AS v(affirmation, nature, statut, constat, source)
WHERE NOT EXISTS (SELECT 1 FROM verifications WHERE nature = 'marche' AND affirmation LIKE 'Red Hood%');

INSERT INTO ambiguites (projet_id, question, enjeu, consequences, statut)
SELECT p.id, a.question, a.enjeu, a.consequences, 'ouverte'::statut_ambiguite
FROM projets p
CROSS JOIN (VALUES
  ('La phase « comprendre le public occidental » est-elle close ou non ?',
   'Signalée par l''outil. Vous l''avez fermée puis rouverte dans le même message.',
   E'Vous écrivez « Je pense avoir assez compris ce qui plaît au public occidental », puis « Mmm finalement j''ai peut-être pas complètement fini ».\nLa réponse commande la suite : si la phase est close, le worldbuilding avance sur une base figée ; si elle est ouverte, il avance sur une base révisable et une partie sera à refaire.\nAucune des deux options n''est mauvaise. Les traiter comme équivalentes, si.'),
  ('Vos références de système viennent de médias à forte capacité d''exposition. Que faites-vous de cet écart ?',
   'Signalée par l''outil. Touche directement le worldbuilding en cours.',
   E'Worm : ~1,7 M de mots. Stormlight : pavés de 1000+ pages. Hunter x Hunter : auteur en position d''imposer des chapitres très verbaux.\nVotre cible : manga en volumes, premier projet, éditeur à convaincre. La densité de règles que ces références rendent possible n''est pas disponible au même coût en pages dessinées.\nTrois voies au moins : réduire la densité, la déployer très progressivement, ou changer de cible de publication. Je n''en choisis aucune.'),
  ('Une étude supplémentaire rapprochera-t-elle de la rétention, ou élargira-t-elle seulement le corpus ?',
   'Signalée par l''outil. Question de rendement du travail de recherche.',
   E'Votre matrice d''arguments conclut elle-même : « aucune de ces mesures ne remplace un suivi de lecteurs », « ni rétention calculable par ratios de notateurs, ni causalité éditoriale ».\nÉtudier Worm, HxH et la progression fantasy par le même appareil produira davantage de données de réception, pas des données de rétention. L''écart que vous avez identifié resterait entier.\nCela ne condamne pas ces études : comprendre des mécaniques est un objectif distinct de mesurer une rétention. Mais les deux ne doivent pas être comptés comme le même progrès.')
) AS a(question, enjeu, consequences)
WHERE NOT EXISTS (SELECT 1 FROM ambiguites WHERE question LIKE 'La phase%');

INSERT INTO documents (titre, url, nature, etabli, non_etabli)
SELECT * FROM (VALUES
  ('Red Hood — matrice d''arguments', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Red%20Hood/matrice_arguments.csv',
   'Matrice proposition / appui / objection / limite',
   'Dix-sept propositions de réception, chacune avec ses sources d''appui, une objection et une limite explicites. Méthodologiquement la pièce la plus solide du dossier.',
   'Sa dernière ligne le dit : discussion, notes et ToC restent distincts ; aucune de ces mesures ne remplace un suivi de lecteurs. Ni rétention calculable, ni causalité éditoriale.'),
  ('Jajanken — 5 séries courtes vs 4 hits', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Jajanken_comparaison_complete_5_courtes_vs_hits_2026-09-22.md',
   'Analyse ToC avec correction du décalage éditorial',
   'Six indicateurs distincts, dont les proxys retardés qui corrigent la protection éditoriale des premiers chapitres. Explique quatre arrêts sur cinq.',
   'Jajanken prévient que ses données donnent une tendance, pas un classement officiel. Le ToC est un dispositif de prépublication hebdomadaire japonaise.'),
  ('Benchmark fantasy — 5 cycles modernes', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Benchmark_fantasy_Goodreads_SensCritique_2026-09-20.md',
   'Agrégats Goodreads / SensCritique',
   'Classement pondéré de cinq cycles, trajectoires par tome, séparation principal/annexes, déduplication documentée.',
   'Corpus de cycles d''élite : le « plancher 4,10 » décrit ce corpus, il n''est pas validé comme prédicteur. Biais de survivants et attrition signalés par le document lui-même.'),
  ('Stormlight — évolution historique Goodreads', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Analyse_complete_Stormlight_Archive_Goodreads_2026-09-27.md',
   'Série historique reconstruite via Internet Archive',
   'Évolution de la moyenne d''un même tome sur 16 ans, avec histogrammes recalculés. Montre qu''une moyenne monte avec la notoriété.',
   'Goodreads ne publie pas de série historique officielle. Décalages entre histogramme et compteur signalés ; reconstructions très proches, pas une série officielle.')
) AS v(titre, url, nature, etabli, non_etabli)
WHERE NOT EXISTS (SELECT 1 FROM documents WHERE titre LIKE 'Red Hood — matrice%');
