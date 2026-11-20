-- Transcription du document 01_CONTEXTE_ET_SUITE (29/09/2026), sections 3, 4, 5, 7.
-- Rien n'est ajouté à la liste de l'auteur. Les « pièges » sont ses propres mises en garde.

INSERT INTO inspirations (nom, categorie, statut, ce_que_vous_en_dites, pieges_interpretation, reste_ouvert)
SELECT * FROM (VALUES
  ('Runeterra (League of Legends)', 'Worldbuilding', 'reference'::statut_inspiration,
   'Référence principale. Préférence nette, notamment pour les vêtements et des personnages jugés plus facilement identifiables et caractérisés. Perçu comme semi-réaliste stylisé, jugé plus compatible avec le manga shōnen.',
   'Cette perception est la vôtre, pas une classification objective des visuels de l''univers.', ''),
  ('Warcraft / World of Warcraft', 'Worldbuilding', 'reference',
   'Référence secondaire. Perçu comme davantage « hard rock » ou solennel.',
   'Même réserve : perception personnelle, pas une propriété de l''univers.', ''),
  ('Féodalisme', 'Organisation politique', 'reference',
   'Référence de structures politiques, juridiques et sociales.',
   'Ne pas fondre les inspirations médiévales, modernes et du XIXe siècle en un seul « Moyen Âge ».', 'Degré de différenciation des peuples et cultures.'),
  ('Philosophies et folklores gréco-romains et égyptiens', 'Folklore', 'reference',
   'Approche syncrétique assumée.',
   'La tripartition platonicienne (raison, thumos, appétits) n''équivaut pas à corps/esprit/âme.', ''),
  ('Europe occidentale, bas Moyen Âge à Renaissance', 'Folklore', 'reference',
   'Philosophies et folklores de la période.', '', ''),
  ('Dictionnaire infernal', 'Folklore', 'reference',
   'Démons, mais aussi hiérarchies et structures sociales.',
   'Ne pas le réduire à un bestiaire visuel. Toute affirmation d''influence directe sur des auteurs de manga doit être sourcée : une ressemblance visuelle ne suffit pas.', ''),
  ('Body, Mind and Soul', 'Non déterminé', 'indetermine',
   'Cité comme inspiration.',
   'Ne pas y attribuer un système de combat à trois branches avant clarification.', 'Sens précis et fonction dans l''œuvre entièrement à définir.'),
  ('Mélusine', 'Folklore', 'reference', '',
   'Le récit examiné distingue l''espionnage au bain de la révélation injurieuse ultérieure. Ne pas les fondre en une disparition immédiate.', ''),
  ('Petit Homme rouge des Tuileries', 'Folklore', 'reference', '',
   'Le compte à rebours évoqué par une autre IA n''est pas une décision de votre part.', ''),
  ('Chasse sauvage', 'Folklore', 'reference', '',
   'Ne pas présumer qu''il s''agit de la version de The Witcher.', ''),
  ('Esthétique de conte de fées (Shrek)', 'Esthétique', 'reference',
   'Référence esthétique.',
   'Une référence esthétique à Shrek n''emporte ni son humour ni son ton.', ''),
  ('The Hunters Guild: Red Hood', 'Esthétique', 'reference',
   'Référence esthétique de conte de fées ; objet par ailleurs d''une étude de réception.',
   'Ne pas en tirer la formule « conte puis examen = abandon ». Aucune obligation de révéler un système de pouvoirs dès la première page n''en découle.', ''),
  ('Harry Potter', 'Esthétique', 'indetermine', '', '', 'Aspects précis de l''inspiration encore à définir.'),
  ('Zone d''inspiration western', 'Zone envisagée', 'indetermine', 'Zone envisagée.', '', 'Répartition territoriale et importance narrative.'),
  ('Zone industrielle (BioShock Infinite)', 'Zone envisagée', 'indetermine', 'Zone envisagée.', '', 'Répartition territoriale et importance narrative.')
) AS v(nom, categorie, statut, ce_que_vous_en_dites, pieges_interpretation, reste_ouvert)
WHERE NOT EXISTS (SELECT 1 FROM inspirations);

INSERT INTO verifications (affirmation, nature, statut, constat, source)
SELECT * FROM (VALUES
  ('La tripartition de l''âme chez Platon équivaut à corps / esprit / âme.',
   'source'::nature_affirmation, 'refute'::statut_verif,
   'La République distingue raison, thumos et appétits. Ce n''est pas la même partition.',
   'https://plato.stanford.edu/entries/plato-ethics-politics/'),
  ('Dans le récit de Mélusine, l''épouse disparaît dès qu''elle est vue au bain.',
   'source', 'nuance',
   'Le récit examiné distingue l''espionnage au bain de la révélation injurieuse ultérieure. Les fondre en une disparition immédiate est une adaptation, pas la source.',
   'https://journals.openedition.org/peme/37379?lang=fr'),
  ('Glénat exige quatre pages d''action et rejette les passages explicatifs.',
   'marche', 'nuance',
   'Glénat demande au minimum quatre pages qui se suivent pour évaluer la fluidité de la narration. Pas obligatoirement de l''action ; aucun rejet automatique de l''explicatif n''est prévu.',
   'https://www.glenat.com/faq/comment-presenter-un-projet-de-manga/'),
  ('Le Dictionnaire infernal a directement influencé des auteurs de manga.',
   'interpretation', 'a_verifier',
   'À sourcer. Une ressemblance visuelle ne vaut pas preuve d''influence.', ''),
  ('Une note Goodreads d''au moins 4,27/5 au tome 1 distingue les futurs succès.',
   'marche', 'a_verifier',
   'Signalé par l''outil, non par vos documents. La comparaison porte sur 4 succès choisis parce qu''ils ont réussi, contre 5 séries axées totalisant 180 notes. La cellule manquante est : des séries bien notées au tome 1 qui ont malgré tout échoué. Sans elle, 4,27 décrit les cas retenus mais ne constitue pas un seuil prédictif.',
   'Vos fichiers Analyse_notes_tomes_1_2 et Percentiles')
) AS v(affirmation, nature, statut, constat, source)
WHERE NOT EXISTS (SELECT 1 FROM verifications);

INSERT INTO documents (titre, url, nature, etabli, non_etabli)
SELECT * FROM (VALUES
  ('01_CONTEXTE_ET_SUITE', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/01_CONTEXTE_ET_SUITE%20(1).md',
   'Document de contexte à maintenir',
   'Objectif, règle de collaboration, inspirations, méthode de crash-test, travail restant.',
   'Ni transcription intégrale, ni étude factuelle nouvelle. Les références citées ne sont pas des décisions de conception.'),
  ('Synthèse de réception — Red Hood', 'https://github.com/michaz94/Projecttest/tree/main/Benchmark%20Oeuvre/Red%20Hood',
   'Étude de réception (corpus Reddit, Goodreads)',
   'Relecture des témoignages sur les chapitres 1, 5 et 15, rôle du one-shot, explications concurrentes.',
   'Pas une lecture directe des planches des 18 chapitres ni du one-shot. Ne mesure pas des préférences occidentales représentatives. L''activité de discussion n''est ni la rétention ni l''achat.'),
  ('Analyse notes tomes 1 et 2 — succès vs séries axées', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Analyse_notes_tomes_1_2_SensCritique_Goodreads_succes_vs_series_axees_2026-09-22.md',
   'Relevé comparatif Goodreads / SensCritique',
   'Écart net de notes entre 4 succès du Jump et 5 séries axées, au tome 1 comme au tome 2.',
   'Réception rétrospective et auto-sélectionnée, influencée par la notoriété et les adaptations animées. Échantillons des séries axées minuscules (11 à 72 notes). Ne reproduit pas le ToC de l''époque.'),
  ('Percentiles tous corpus principaux', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Percentiles_tous_corpus_principaux_2026-09-22.md',
   'Percentiles et scores robustes',
   '602 entrées Goodreads et 599 SensCritique après correction ; score robuste réestimé (C = 4,40151 ; m = 5 892,5).',
   'Des notes agrégées ne sont pas des ventes. La position en percentile ne dit rien de la rétention entre tomes.'),
  ('Étude ventes et notes 2000-2012', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Etude_ventes_et_notes_2000_2012.md',
   'Étude ventes / notes',
   'À compléter après lecture : je n''ai pas ouvert ce fichier.',
   'Non lu par l''assistant à ce stade.'),
  ('Note de retrait One Piece 116', 'https://github.com/michaz94/Projecttest/blob/main/Benchmark%20Oeuvre/Note_retrait_One_Piece_116_2026-09-27.md',
   'Note de correction méthodologique',
   'Retrait d''une entrée qui était un chapitre et non un tome relié ; recalcul des percentiles.',
   'Non lu intégralement par l''assistant.')
) AS v(titre, url, nature, etabli, non_etabli)
WHERE NOT EXISTS (SELECT 1 FROM documents);

-- Ambiguïtés signalées par l'outil, pas par vous. À écarter si elles ne vous parlent pas.
INSERT INTO ambiguites (projet_id, question, enjeu, consequences, statut)
SELECT p.id, a.question, a.enjeu, a.consequences, 'ouverte'::statut_ambiguite
FROM projets p
CROSS JOIN (VALUES
  ('Les signaux tirés du Weekly Shōnen Jump valent-ils pour une création originale chez un éditeur français ?',
   'Signalée par l''outil. Conditionne la validité de tout votre corpus quantitatif comme base de décision.',
   'Le ToC mesure la rétention hebdomadaire d''un magazine de prépublication. Ankama, Kana et Glénat publient en volumes, sans ce mécanisme. Si le transfert ne tient pas, le benchmark reste intéressant mais cesse d''être un guide de conception pour votre voie de publication.'),
  ('Que mesure votre corpus par rapport à ce que vous visez ?',
   'Signalée par l''outil. Écart entre l''instrument et l''objectif.',
   'Vos relevés mesurent l''appréciation rétrospective de lecteurs auto-sélectionnés. Votre objectif est la stabilité commerciale et la rétention sur des dizaines de tomes. Vos propres notes le disent. La question ouverte est ce qui comble l''écart, faute de pouvoir recruter des bêta-lecteurs.'),
  ('Quel rapport entre vos inspirations de fantasy occidentale et la forme battle shōnen ?',
   'Signalée par l''outil. Structurante et non tranchée.',
   'Runeterra, Warcraft, Tolkien et Stormlight sont des références de worldbuilding. Le battle shōnen est une forme de sérialisation. L''un peut servir de décor à l''autre, ou l''autre être plié au premier. Les deux voies existent ; je ne choisis pas.')
) AS a(question, enjeu, consequences)
WHERE NOT EXISTS (SELECT 1 FROM ambiguites);
