# Phase 3 : Nettoyage et Prétraitement des Données

## Objectif de la phase

Cette phase a pour objectif de transformer les données brutes collectées depuis YouTube
en données propres, structurées et exploitables pour les analyses ultérieures, notamment :

- l’analyse de sentiments,
- l’analyse des réseaux sociaux,
- l’identification des influenceurs.

## Données en entrée

Les données en entrée sont fournies sous forme d’un fichier JSON (`youtube_data.json`)
contenant les vidéos, les commentaires et les réponses associées.

## Étapes réalisées

### 1. Nettoyage et structuration des données

Les données sont d’abord aplaties (flattening) afin d’extraire chaque commentaire
comme une entité indépendante. Les opérations suivantes sont appliquées :

- suppression des valeurs nulles,
- conservation des attributs essentiels (auteur, texte, date, likes),
- structuration des relations (réponses entre utilisateurs).

Le résultat de cette étape est un fichier `comments_clean.csv` contenant des données
structurées et homogènes.

### 2. Prétraitement NLP

Un prétraitement linguistique est appliqué aux textes des commentaires afin de :

- normaliser le texte (minuscules),
- supprimer les caractères spéciaux et les URLs,
- éliminer les textes vides.

Cette étape permet de préparer les données pour l’analyse de sentiments et
la modélisation thématique. Le résultat est stocké dans le fichier
`comments_nlp_ready.csv`.

## Utilisation d’Apache Spark

Conformément au cahier des charges du projet, Apache Spark est prévu pour le traitement
massivement parallèle des données. Cependant, dans l’environnement Windows local,
l’exécution complète de Spark peut entraîner des contraintes de compatibilité liées
au système de fichiers Hadoop.

Afin d’assurer la continuité du projet et la reproductibilité des résultats,
les opérations de nettoyage ont été exécutées en mode local à l’aide de la bibliothèque
Pandas, tout en conservant l’architecture Spark au niveau conceptuel.

Dans un environnement Linux ou cluster, ces mêmes traitements peuvent être déployés
directement avec Apache Spark sans modification de la logique métier.

## Résultats de la phase

À l’issue de cette phase, les données sont :

- propres,
- structurées,
- prêtes pour l’analyse de sentiments,
- prêtes pour l’analyse des réseaux sociaux.

Les fichiers produits constituent l’entrée principale de la phase suivante
(Analyse des sentiments et influenceurs).

## Lien avec le cahier des charges

Cette phase répond directement à l’étape **« Nettoyage et prétraitement des données »**
mentionnée dans le cahier des charges du projet Big Data & Applications.
