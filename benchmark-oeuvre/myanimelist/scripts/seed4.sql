INSERT INTO constats (titre, corpus, mesure, lecture, limites, contre_epreuve)
SELECT * FROM (VALUES
  ('La discussion bascule sur l''annulation à partir du chapitre 9-10',
   '4 432 commentaires Reddit Red Hood, 18 chapitres, corpus intégral de votre dossier',
   E'Part des commentaires évoquant l''annulation (axed / cancel / hiatus) :\n  ch1-8   : 1,4 % à 7,4 %  (médiane ~3,9 %)\n  ch9     : 7,9 %\n  ch10    : 17,0 %\n  ch11-14 : 8,9 % à 15,9 %\n  ch15    : 22,3 %\n  ch16    : 22,0 %\n  ch17    : 22,7 %\n  ch18    : 18,3 %\n\nMentions de classements / ventes / questionnaires :\n  ch1-8 : 0,0 % à 1,8 %\n  ch9   : 11,2 %\n  ch10  : 12,6 %\n  ch11-13 : 6,5 % à 7,3 %',
   E'Les deux courbes basculent au même endroit, et cet endroit correspond exactement à l''effondrement du ToC que documente votre rapport Jajanken : chapitre 9 = rang 18, chapitre 10 = rang 21.\n\nLecture proposée : le lectorat occidental suivait les classements japonais. À partir du chapitre 9, près d''un commentaire sur quatre parle du sort éditorial de la série plutôt que de son contenu. La conversation cesse d''être une conversation de lecteurs pour devenir une veille de décès annoncé.\n\nC''est une hypothèse sur ce que la discussion devient, pas sur ce qui fait décrocher un lecteur.',
   E'Appariement lexical : le sens n''est pas évalué. Faux positifs vérifiés à la main sur ce thème (9/10 authentiques dans un tirage aléatoire de 10) ; non vérifiés sur les autres thèmes.\nLes commentateurs Reddit ne sont pas un échantillon du lectorat.\nUne corrélation temporelle entre deux courbes n''établit pas un lien causal.',
   'Refaire le même comptage sur une série au ToC également mauvais mais moins commentée, pour voir si la bascule est propre à Red Hood.'),

  ('Le volume de discussion occidental ne s''est PAS effondré',
   'Red Hood (4 432 comm.) vs Sakamoto Days (506), Ayashimon (4 047), Neru (372) — chapitres appariés 1, 3, 7, 14, 18',
   E'Commentaires par chapitre apparié :\n  Red Hood      : 446 / 179 / 315 / 135 / 349\n  Ayashimon     : 545 / 211 / 125 / 104 /  95\n  Sakamoto Days : 253 /  64 /  53 /  71 /  65\n  Neru          : 117 /  49 /  42 /  23 / 141\n\nRétention des commentateurs présents au chapitre 1 :\n  Red Hood  : 14,4 % (ch2) → 8,6 % (ch14) → 13,4 % (ch18)\n  Ayashimon : 28,3 % (ch2) → 9,0 % (ch14) →  6,9 % (ch21)',
   E'Red Hood génère plus de discussion que Sakamoto Days à CHAQUE point de comparaison : 1,8x au chapitre 1, 5,9x au chapitre 7, 5,4x au chapitre 18. Sakamoto Days a été un succès durable ; Red Hood a été axée.\n\nCela contredit frontalement la formulation « Red Hood n''a pas réussi à garder son public », si « public » désigne l''audience occidentale visible. Elle l''a gardée, et elle en a même regagné à la fin (135 commentaires au ch14, 349 au ch18).\n\nCe que la série n''a pas obtenu, c''est le classement dans les questionnaires japonais. Ce sont deux populations différentes, et votre corpus occidental ne mesure pas la seconde.',
   E'Le volume de discussion n''est ni la lecture, ni l''achat, ni la rétention — votre propre matrice le dit.\nLa remontée des chapitres 15-18 est très probablement due à l''annonce de l''annulation, pas à un regain d''intérêt narratif.\nLes séries témoins n''ont que 5 chapitres relevés contre 18 pour Red Hood.',
   'Comparer à une série occidentalement peu discutée mais japonaisement bien classée — le cas symétrique manque au corpus.'),

  ('Les griefs de métier sont minoritaires en fréquence, mais convergents dans les commentaires les plus votés',
   '4 432 commentaires Reddit Red Hood',
   E'Fréquence brute sur l''ensemble du corpus :\n  Rythme / lenteur              : 5,1 %  (224)\n  Protagoniste fade / générique : 2,4 %  (107)\n  Casting trop large            : 1,9 %  ( 82)\n  Attachement / personnages     : 1,8 %  ( 79)\n  Exposition                    : 1,3 %  ( 59)\n  Lisibilité de l''action        : 1,2 %  ( 54)\n  Abandon déclaré               : 0,9 %  ( 40)\n\nTrajectoire du thème « rythme » :\n  ch1 1,6 % → ch13 10,1 % → ch16 11,2 % → ch18 12,3 %',
   E'Deux choses distinctes.\n\n1. En fréquence brute, aucun grief de métier ne domine. Le thème le plus cité (rythme, 5,1 %) reste marginal devant l''annulation (11,4 %).\n\n2. En revanche, les commentaires critiques les plus votés convergent, et ils convergent sur une seule chose : la structure d''entrée. Technocity777 (315 points, ch18) : « 5 chapitres pour établir la motivation de Velou parce que les ch. 2-4 ont été gaspillés sur deux sbires sans conséquence, puis 10 chapitres de plus pour qu''il rejoigne l''organisation. On pourrait condenser les 15 premiers chapitres en 5 ou 6. » SolracXD (352 points, ch18) cite le manque de présence de Velou et le combat du hameau comme perte de temps. SaKaly (430 points, ch16) : « si une seule chose avait été ajustée, comme le rythme ».\n\nLe grief récurrent n''est donc pas « l''examen est trop long » mais : le temps de récit dépensé n''achète pas assez de progression. C''est cohérent avec le mécanisme 1 de votre synthèse, formulé autrement.',
   E'Le score d''un commentaire mesure l''accord de ceux qui votent, pas la fréquence d''une opinion.\nLes commentaires les mieux votés du ch18 sont des bilans rétrospectifs écrits en sachant la série annulée : ils rationalisent un échec connu.\nLa fréquence lexicale et la sélection par score mesurent deux choses différentes ; je les présente séparément pour cette raison.',
   'Coder à la main un échantillon aléatoire de 100 commentaires pour estimer le taux de faux positifs de chaque thème.')
) AS v(titre, corpus, mesure, lecture, limites, contre_epreuve)
WHERE NOT EXISTS (SELECT 1 FROM constats);

INSERT INTO ambiguites (projet_id, question, enjeu, consequences, statut)
SELECT p.id, a.question, a.enjeu, a.consequences, 'ouverte'::statut_ambiguite
FROM projets p
CROSS JOIN (VALUES
  ('« Red Hood n''a pas gardé son public » — de quel public parle-t-on ?',
   'Signalée par l''outil. La prémisse de votre question ne résiste pas au comptage.',
   E'Le public occidental visible n''a pas décroché : Red Hood a généré 5,4x plus de discussion que Sakamoto Days au chapitre 18, et sa rétention de commentateurs est comparable à celle d''Ayashimon.\nCe qui a manqué, ce sont les questionnaires japonais — un public que votre corpus occidental ne mesure pas du tout.\nSi votre cible est occidentale et votre voie de publication française, le mécanisme qui a tué Red Hood (le ToC hebdomadaire du Jump) n''existe pas sur votre chemin. Reste à savoir ce que vous voulez apprendre de ce cas.')
) AS a(question, enjeu, consequences)
WHERE NOT EXISTS (SELECT 1 FROM ambiguites WHERE question LIKE '%Red Hood%public%');
