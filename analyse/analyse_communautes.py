import pandas as pd
import networkx as nx
from pathlib import Path
import community as community_louvain

# ===============================
# Chargement des données
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "analyse" / "comments_sentiments.csv"
OUTPUT_PATH = BASE_DIR / "analyse" / "communities.csv"

df = pd.read_csv(INPUT_PATH)

# ===============================
# Construction du graphe
# ===============================

G = nx.Graph()

for _, row in df.iterrows():
    author = row["author"]
    reply_to = row["reply_to"]

    if pd.notna(reply_to):
        G.add_edge(author, reply_to)

# ===============================
# Détection des communautés (Louvain)
# ===============================

partition = community_louvain.best_partition(G)

# ===============================
# Sauvegarde des communautés
# ===============================

df_communities = pd.DataFrame({
    "author": list(partition.keys()),
    "community_id": list(partition.values())
})

df_communities.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("Détection des communautés terminée : fichier communities.csv généré")
