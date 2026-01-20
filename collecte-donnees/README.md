# Phase 2 : Collecte des données (YouTube API)

## Objectif

Cette phase a pour objectif de collecter des données issues de la plateforme YouTube
afin d’analyser les discussions en ligne liées à un sujet géopolitique donné.
La collecte constitue la première étape opérationnelle du pipeline Big Data.

## Source des données

Les données sont collectées à partir de l’API officielle **YouTube Data API v3**.
La collecte est orientée par sujet (topic-driven) à l’aide de mots-clés prédéfinis
en lien avec le thème étudié.

## Données collectées

Pour chaque mot-clé, le système récupère :

- Les vidéos correspondantes
- Les métadonnées des vidéos (titre, chaîne, date de publication)
- Les commentaires associés aux vidéos
- Les réponses aux commentaires
- Les indicateurs d’engagement (nombre de likes)
- Les informations temporelles (dates de publication et de collecte)

## Format des données

Les données sont stockées sous forme de documents **JSON** structurés.
Chaque document représente une vidéo et contient la liste des commentaires et réponses
associés, facilitant ainsi les étapes ultérieures de traitement et d’analyse.

## Gestion des cas particuliers

Certaines vidéos peuvent avoir les commentaires désactivés. Ces cas sont détectés
et gérés automatiquement afin d’assurer la continuité du processus de collecte,
sans interrompre le pipeline.

## Résultat de la phase

À l’issue de cette phase, un fichier `youtube_data.json` est généré.  
Il constitue un jeu de données brut (raw data) prêt pour :

- le streaming temps réel avec Apache Kafka,
- le nettoyage et le prétraitement avec Apache Spark,
- l’analyse des réseaux sociaux et des sentiments.

## Lien avec les objectifs du projet

Cette phase répond directement à l’étape **« Collecte et acquisition de données »**
définie dans le cahier des charges du projet. Les données collectées serviront de base
à l’analyse des interactions entre utilisateurs, à la détection de communautés et
à l’analyse de sentiments dans les phases suivantes.
