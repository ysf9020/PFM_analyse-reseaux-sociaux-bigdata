# Phase 6 – Visualisation & Dashboard (Streamlit)

## 🎯 Objectif de la phase

Cette phase vise à **présenter de manière interactive et lisible** les résultats obtenus lors des phases précédentes du projet Big Data d’analyse des réseaux sociaux.

Le dashboard permet de :

- visualiser les **sentiments** exprimés dans les commentaires,
- explorer les **thèmes dominants** (Topic Modeling),
- identifier les **utilisateurs influents**,
- analyser la **structure du réseau social** et les **communautés détectées**.

Cette étape répond directement aux exigences de la documentation du projet concernant la **visualisation des résultats analytiques**.

---

## 🛠️ Outils et technologies

- **Streamlit** : création du dashboard interactif
- **Pandas** : manipulation des données
- **Matplotlib** : visualisations graphiques
- **CSV** : sources de données issues des phases d’analyse

---

## 📂 Fichiers utilisés

Les visualisations s’appuient sur les fichiers générés dans les phases précédentes :

- `analyse/comments_sentiments.csv`
- `analyse/comments_topics.csv`
- `analyse/influenceurs.csv`
- `analyse/reseau_centralites.csv`
- `analyse/communities.csv`
- `analyse/dataset_final.csv`

---

## 📊 Contenu du Dashboard

### 1️⃣ Analyse des sentiments

- Distribution globale des sentiments :
  - positif
  - neutre
  - négatif
- Visualisation du nombre de commentaires par catégorie de sentiment.

---

### 2️⃣ Thèmes dominants (Topic Modeling)

- Répartition des commentaires par **topic** (LDA).
- Analyse croisée :
  - **Topic ↔ Sentiment**
- Permet de comprendre **sur quels sujets portent les débats** et leur tonalité dominante.

---

### 3️⃣ Influenceurs

- Tableau des **utilisateurs les plus influents**.
- Score d’influence basé sur :
  - nombre de commentaires,
  - nombre total de likes,
  - nombre de réponses.
- Graphique des **Top 10 influenceurs**.

---

### 4️⃣ Réseau social & communautés

- Indicateurs de centralité :
  - degree centrality
  - betweenness centrality
  - in-degree / out-degree
- Visualisation de la **taille des communautés détectées**
  (algorithme de détection de communautés).
- Analyse de la structure globale des interactions entre utilisateurs.

---

## 🎨 Interface et ergonomie

- Interface organisée en **onglets clairs** :
  - Sentiments
  - Topics
  - Influenceurs
  - Réseau & Communautés
- Amélioration de la lisibilité grâce à :
  - styles CSS personnalisés,
  - tailles de titres adaptées,
  - tableaux interactifs.

---

## ▶️ Lancement du dashboard

Depuis la racine du projet :

```bash
streamlit run visualisation/dashboard_streamlit.py


```
