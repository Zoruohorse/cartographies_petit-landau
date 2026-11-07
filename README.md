# Cartographie des acteurs — Microsoft Petit-Landau / Hombourg

Site statique autonome à publier sur GitHub Pages. Le moteur physique et le rendu sont repris **sans modification de formule ni des fichiers CSS** du modèle Fouju, tel que réemployé dans les livrables précédents.

## Deux vues / trois onglets

- `apps/cards/` : cartes acteurs et preuves, synthèse des oppositions, points de vigilance et sources.
- `apps/network/` : nuage relationnel avec la même physique, les mêmes couleurs, sélections, zooms et panneaux que Fouju.
- `data/*.json` et `config/taxonomy.json` : référentiel commun aux deux vues.

## Données issues des deux blocs du code initial

- **24 nœuds réseau initiaux**, **24 relations d’origine**, tous conservés.
- **31 nœuds finaux**, **31 relations**, y compris **7 rattachements contextuels supplémentaires**, explicitement signalés comme tels et déjà étayés par les fiches sources.
- **28 fiches acteurs**, **25 éléments de preuve**, **11 sujets de synthèse**, **16 points de vigilance** et **7 références documentaires**.
- Les appellations génériques « Communes Favourables » et « Commune Défavorable » du réseau original sont conservées et reliées à leurs dénominations précises dans les fiches par une relation d’équivalence explicite.
- Les trois fiches comportant la preuve `N/A` affichent « Aucune preuve structurée » au lieu d’une fausse preuve.

## Fiabilité et provenance

Les positions, chiffres, formulations et degrés de certitude proviennent du code utilisateur, sans vérification factuelle extérieure. Les éléments de preuve peuvent être des verbatims ou des reformulations : aucun statut de citation littérale n’est prétendu. Les liens d’article individuels ne sont pas attribués fictivement à des déclarations. Toute URL de référence non fournie reste `null` dans `data/sources.json`. Les relations reprises du nuage d’origine et les liens contextuels ajoutés sont séparés par leur champ `status`.

## Publication GitHub Pages

1. Décompresser l’archive puis transférer **tout son contenu** (et pas le ZIP) à la racine du dépôt GitHub.
2. `Settings → Pages → Deploy from a branch → main / (root)`.
3. Ouvrir le site Pages puis choisir « Vue en cartes » ou « Vue réseau ».

## Contrôles locaux

```bash
python3 validate.py
python3 -m http.server 8000
```

Ouvrir `http://localhost:8000/`. L'application charge des JSON via `fetch`, donc ouvrir directement `index.html` en `file://` ne suffit pas.

## Actualisation 7 novembre 2026
Quatre onglets, preuves URL et audit de 54 ressources. Voir [AUDIT_QUALIFICATION_2026-11-07.md](AUDIT_QUALIFICATION_2026-11-07.md).

## Cinquième onglet : Évolution des acteurs (2026-11-07)
Histogramme mensuel empilé, en mode **cumulé par défaut** et **nouveaux acteurs** sur option, par typologie et avec renvoi vers les premières mentions documentaires. La série comporte 60 jalons sourcés pour 60 fiches. Voir [METHODE_EVOLUTION_2026-11-07.md](METHODE_EVOLUTION_2026-11-07.md).
