# Analyse Big Data des Réseaux Sociaux

## Sentiments – Thèmes – Influence – Communautés

---

## 📌 Présentation du projet

Ce projet consiste à développer une application **Big Data d’analyse des réseaux sociaux**
permettant de collecter, traiter et analyser des discussions en ligne autour d’un sujet
géopolitique sensible : **le conflit Maroc – Polisario autour du Sahara**.

L’objectif est **exclusivement analytique et technique** :  
comprendre comment les utilisateurs interagissent, quels sujets émergent,
quelles communautés se forment et quels acteurs influencent les conversations.

Le projet a été réalisé en **mode batch / quasi temps réel**, avec une architecture
préparée pour une extension future vers le **temps réel**.

---

## 🎯 Objectifs principaux

- Collecter automatiquement des commentaires depuis un réseau social
- Nettoyer et prétraiter les données textuelles
- Analyser la **tonalité des opinions** (sentiment analysis)
- Extraire les **thèmes dominants** (topic modeling)
- Identifier les **utilisateurs influents**
- Modéliser les **relations entre utilisateurs**
- Détecter les **communautés** au sein du réseau
- Présenter les résultats via un **dashboard interactif**

---

## 🧠 Tâches réalisées (conformité à la documentation)

### 1️⃣ Analyse des réseaux sociaux

- Modélisation du réseau utilisateurs (graphes)
- Calcul des centralités :
  - degree centrality
  - betweenness centrality
- Identification des influenceurs
- Détection des communautés (algorithme de Louvain)

### 2️⃣ Analyse des posts et commentaires

- Nettoyage et prétraitement NLP
- **Topic Modeling (LDA)** pour extraire les thèmes dominants
- Analyse de sentiments (positif / neutre / négatif)
- Analyse de l’engagement utilisateur :
  - nombre de commentaires
  - likes
  - réponses

### 3️⃣ Analyse des sentiments

- Réalisée à l’aide de la bibliothèque **VADER**
- Résultats exploités dans les analyses et le dashboard

### 4️⃣ Visualisation et dashboard

- Dashboard interactif développé avec **Streamlit**
- Visualisation :
  - des sentiments
  - des thèmes dominants
  - des influenceurs
  - du réseau social
  - des communautés détectées

---

## 🛠️ Technologies utilisées

- **Python**
- **YouTube Data API** (source de données)
- **Pandas** / **NumPy**
- **Scikit-learn** (TF-IDF, LDA)
- **NetworkX** (analyse de graphes)
- **VADER Sentiment Analysis**
- **Matplotlib**
- **Streamlit**

### Outils Big Data (préparés dans l’architecture)

- Apache Kafka (streaming)
- Apache Spark / Spark Streaming
- MongoDB (NoSQL)
- Apache Airflow (orchestration)

---

## 🗂️ Structure du projet

PFM_analyse-reseaux-sociaux-bigdata/
│
├─ collecte-donnees/ # Collecte des données
├─ traitement/ # Nettoyage et prétraitement
├─ analyse/ # Analyses NLP, réseau, topics, communautés
├─ visualisation/ # Dashboard Streamlit
├─ streaming/ # Kafka (préparé)
├─ orchestration/ # Airflow (préparé)
├─ stockage/ # MongoDB (préparé)
├─ docs/ # Documentation
├─ requirements.txt
└─ README.md

---

## ▶️ Lancement du dashboard

Depuis la racine du projet :

```bash
streamlit run visualisation/dashboard_streamlit.py

```

---

## 📌 Documentation

### 📄 Analyse des réseaux sociaux

- [Analyse des réseaux sociaux](docs/analyse-reseaux-sociaux.md)

### 📄 Analyse des posts et commentaires

- [Analyse des posts et commentaires](docs/analyse-posts.md)

### 📄 Analyse des sentiments

- [Analyse des sentiments](docs/analyse-sentiments.md)

### 📄 Visualisation et dashboard

- [Visualisation et dashboard](docs/visualisation-dashboard.md)

---

## 📌 Contact

## ⚠️ Limitations du projet

L’analyse est réalisée en mode batch (quasi temps réel).

Les modules Kafka, Spark Streaming, MongoDB et Airflow sont présents
au niveau de l’architecture mais non activés.

L’entraînement d’un modèle de Machine Learning personnalisé pour les sentiments
n’a pas été réalisé ; un modèle préentraîné (VADER) a été utilisé.

Ces choix sont justifiés par :

les contraintes de temps,

les ressources matérielles disponibles,

le cadre académique du projet.

## 🚀 Perspectives d’amélioration

Intégration du streaming temps réel avec Kafka et Spark Streaming

Stockage distribué des données avec MongoDB

Orchestration complète du pipeline avec Airflow

Entraînement d’un modèle ML personnalisé pour l’analyse des sentiments

Visualisation dynamique des graphes de réseau

## 🎓 Conclusion

Le projet répond aux exigences académiques du module Big Data & Social Network Analysis.
Il couvre l’ensemble des analyses demandées :
sentiments, thèmes dominants, influence, réseau et communautés,
et propose une architecture extensible vers des solutions Big Data complètes.

---

---

## ▶️ Lancement du dashboard

Depuis la racine du projet :

```bash
streamlit run visualisation/dashboard_streamlit.py
```
