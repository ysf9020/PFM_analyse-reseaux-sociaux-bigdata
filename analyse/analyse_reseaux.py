import pandas as pd
import networkx as nx
from pathlib import Path

# ===============================
# Chargement des données
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "analyse" / "comments_sentiments.csv"

df = pd.read_csv(INPUT_PATH)

# ===============================
# Création du graphe orienté
# ===============================

G = nx.DiGraph()

for _, row in df.iterrows():
    author = row["author"]
    reply_to = row["reply_to"]

    if pd.notna(reply_to):
        G.add_edge(author, reply_to)

# ===============================
# Mesures de centralité
# ===============================

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
in_degree = dict(G.in_degree())
out_degree = dict(G.out_degree())

# ===============================
# Construction du DataFrame résultats
# ===============================

results = pd.DataFrame({
    "author": list(G.nodes()),
    "degree_centrality": [degree_centrality.get(n, 0) for n in G.nodes()],
    "betweenness_centrality": [betweenness_centrality.get(n, 0) for n in G.nodes()],
    "in_degree": [in_degree.get(n, 0) for n in G.nodes()],
    "out_degree": [out_degree.get(n, 0) for n in G.nodes()]
})

# ===============================
# Sauvegarde
# ===============================

OUTPUT_PATH = BASE_DIR / "analyse" / "reseau_centralites.csv"
results.sort_values("betweenness_centrality", ascending=False).to_csv(
    OUTPUT_PATH, index=False, encoding="utf-8"
)

print("Analyse du réseau terminée : fichier reseau_centralites.csv généré")
