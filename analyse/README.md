# Phase 4 : Analyse des Sentiments et des Influenceurs

## Objectif de la phase

Cette phase vise à analyser le contenu textuel des commentaires collectés afin de :

- déterminer le sentiment exprimé (positif, neutre ou négatif),
- identifier les utilisateurs les plus influents au sein des discussions.

## Analyse des sentiments

L’analyse des sentiments est réalisée à l’aide de la bibliothèque **VADER (Valence Aware Dictionary and Sentiment Reasoner)**,
particulièrement adaptée aux textes courts issus des réseaux sociaux.

Chaque commentaire est classé selon trois catégories :

- positif,
- neutre,
- négatif.

Les résultats sont stockés dans le fichier `comments_sentiments.csv`.

## Analyse des influenceurs

L’identification des influenceurs repose sur des indicateurs d’engagement simples :

- nombre de commentaires publiés,
- nombre total de likes reçus,
- nombre de réponses générées.

Un score d’influence composite est calculé afin de classer les utilisateurs selon
leur niveau d’impact dans les discussions. Les résultats sont enregistrés dans le
fichier `influenceurs.csv`.

## Résultats de la phase

À l’issue de cette phase :

- les sentiments des commentaires sont identifiés,
- les utilisateurs influents sont détectés,
- les données sont prêtes pour l’analyse des réseaux sociaux.

## Lien avec le cahier des charges

Cette phase répond aux exigences d’**analyse des sentiments**, d’**analyse de l’engagement**
et d’**identification des influenceurs** définies dans le cahier des charges du projet.

---

# Phase 5 : Analyse des Réseaux Sociaux (Graph)

## Objectif de la phase

Cette phase vise à analyser la structure des interactions entre les utilisateurs
à travers la construction d’un graphe social. L’objectif principal est de mettre
en évidence les relations entre les acteurs, ainsi que les positions structurales
les plus importantes au sein du réseau.

## Modélisation du réseau

Le réseau social est modélisé sous forme d’un graphe orienté :

- les nœuds représentent les utilisateurs,
- les arêtes représentent les réponses entre utilisateurs.

Une arête est créée lorsqu’un utilisateur répond à un commentaire publié par un autre.

## Mesures de centralité

Plusieurs indicateurs de centralité sont calculés afin d’analyser la structure du réseau :

- **degree centrality** : mesure l’activité globale d’un utilisateur,
- **in-degree** : indique le nombre de réponses reçues,
- **out-degree** : indique le nombre de réponses émises,
- **betweenness centrality** : identifie les utilisateurs jouant un rôle de médiateur
  entre différentes parties du réseau.

Ces indicateurs permettent d’identifier les utilisateurs ayant une influence
structurelle, indépendamment de leur popularité directe.

## Résultats de la phase

Les résultats de l’analyse du réseau sont stockés dans le fichier
`reseau_centralites.csv`. Ce fichier contient, pour chaque utilisateur,
les différentes mesures de centralité calculées.

## Lien avec le cahier des charges

Cette phase répond aux exigences d’**analyse des réseaux sociaux**, de
**modélisation des relations entre utilisateurs** et d’**identification des
acteurs centraux**, telles que définies dans le cahier des charges du projet.
-------------
