-- Amorçage volontairement pauvre.
-- On ne crée que des coquilles vides : aucun contenu de corpus n'est inventé.
-- Les seuls noms d'éditeurs insérés sont ceux cités par l'auteur lui-même.

INSERT INTO projets (titre, pitch, note_perimetre)
SELECT
  'Projet shonen (à renommer)',
  '',
  'Ce module ne tient que la couche éditoriale. Le worldbuilding reste dans l''app mobile.'
WHERE NOT EXISTS (SELECT 1 FROM projets);

INSERT INTO editeurs (nom, fiabilite)
SELECT v.nom, 'squelette'::fiabilite
FROM (VALUES ('Glénat'), ('Ankama'), ('Kana'), ('Pika')) AS v(nom)
WHERE NOT EXISTS (SELECT 1 FROM editeurs);

INSERT INTO segments_publics (nom, fiabilite)
SELECT 'Lectorat occidental (découpage à préciser)', 'squelette'::fiabilite
WHERE NOT EXISTS (SELECT 1 FROM segments_publics);

-- Trois propositions, enregistrées comme telles : statut « proposition », origine « outil ».
-- Elles n'engagent rien et peuvent être supprimées sans conséquence.
INSERT INTO decisions (projet_id, axe, intitule, contenu, statut, origine, justification)
SELECT
  p.id, d.axe, d.intitule, d.contenu, 'proposition'::statut_decision, 'outil'::origine, d.justification
FROM projets p
CROSS JOIN (VALUES
  (
    'Positionnement marché',
    'Fixer la maison visée avant de figer le format',
    'Arrêter une ou deux maisons cibles, puis dériver format et pagination de leurs contraintes.',
    'Proposition de l''outil, pas une règle. L''ordre inverse — écrire d''abord, chercher ensuite la maison qui correspond — est parfaitement défendable et souvent pratiqué.'
  ),
  (
    'Format & pagination',
    'Trancher tôt entre série longue et récit borné',
    'Le choix engage la structure d''arc, le rythme des révélations et l''argumentaire de présentation.',
    'Proposition de l''outil. Je ne sais pas ce que vous visez ; ce n''est peut-être pas prioritaire à ce stade.'
  ),
  (
    'Ton',
    'Expliciter la part de codes shonen japonais conservée',
    'Nommer ce qui est repris tel quel, ce qui est adapté, ce qui est écarté pour un lectorat occidental.',
    'Proposition de l''outil, issue du seul fait que vous ciblez un public occidental. Vous n''avez formulé aucune intention d''adaptation.'
  )
) AS d(axe, intitule, contenu, justification)
WHERE NOT EXISTS (SELECT 1 FROM decisions);
