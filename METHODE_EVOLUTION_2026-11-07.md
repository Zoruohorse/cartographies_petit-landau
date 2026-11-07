# Suivi chronologique de l'évolution des acteurs — Petit-Landau / Hombourg
Date de construction : 2026-11-07

## Principe
Le cinquième onglet reproduit l'histogramme interactif de Châteauroux, avec le mode « Cumulés » sélectionné par défaut. Une fiche d'acteur compte **une seule fois**, à la date de sa première **mention ou intervention datable dans les sources du corpus**. Il ne s'agit ni de la date réelle d'arrivée d'un acteur dans le projet, ni du nombre de citoyens mobilisés, ni d'un indicateur de soutien/opposition à une date passée.

Les fonctions, personnes, entreprises, collectifs et institutions sont comptés ensemble sous leur propre typologie. Les positions non établies sont incluses, **en tant que présence documentaire seulement** ; le cumul ne transforme pas leur rôle en opinion. Chaque ligne renvoie à son article ou document public.

## Périmètre vérifié
- 60 acteurs visibles, 60 jalons univoques dans `data/timeline.json`.
- Aucun projet central compté comme un acteur.
- Les sources datent soit une prise de parole (réunion du 3 juin, décisions des 22 juin/12 octobre, etc.), soit la publication où l'acteur apparaît. Le champ `date_basis` précise chaque méthode.
- La série débute en juillet 2025 avec les premières sources locales retenues et s'arrête le 1er novembre 2026 pour les témoignages diffusés par RTS. Les découvertes ultérieures seront des deltas documentaires et **non des créations rétroactives fictives**.
- La diffusion RTS du 1er novembre 2026 a été recoupée avec le descriptif de l'émission (podcast Apple).
- Catégories exclusives : élus ; associations/collectifs ; entreprises ; institutions ; collectivités ; habitants et experts.
- Les deux modes « Nouveaux » et « Cumulés » sont interactifs et filtrables ; ils ne modifient jamais la position actuelle conservée dans `data/claims.json`.

## Notes d'interprétation
1. Les articles payants peuvent avoir été lus par le texte du classeur ; leurs URLs restent fournies.
2. Une délibération administrative ne donne pas une opinion personnelle au préfet, à la MRAe, au CODERST, au commissaire ou à RTE.
3. La première mention *dans ce corpus* peut être postérieure à la première expression de l'acteur dans la réalité.
4. Les occurrences mensuelles à forte concentration peuvent refléter la couverture d'une manifestation collective, et non une hausse équivalente de personnes nouvellement mobilisées.
5. Le 27 octobre 2026 est la date d'octroi des permis ; elle ne réécrit pas rétroactivement la première opinion publique de Thierry Engasser, documentée dès juillet 2025.

## Répartition documentaire par catégorie
- Élus et responsables politiques : 18 fiches
- Associations et collectifs : 15 fiches
- Entreprises et porteurs : 5 fiches
- Institutions et autorités techniques : 6 fiches
- Collectivités et conseils : 6 fiches
- Habitants, experts et autres : 10 fiches

## Contrôles
Un acteur, un premier événement. Une URL de source au minimum par événement. Dates ISO sans jalon futur et association valide aux acteurs existants. Graphique rendu depuis `data/timeline.json` et jamais depuis des compteurs saisis manuellement.
