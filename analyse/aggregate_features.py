import pandas as pd
from pathlib import Path

# =========================
# Base directory
# =========================
BASE_DIR = Path(__file__).resolve().parents[1] / "analyse"

# =========================
# Input files
# =========================
COMMENTS_TOPICS = BASE_DIR / "comments_topics.csv"
COMMENTS_SENTIMENTS = BASE_DIR / "comments_sentiments.csv"
COMMUNITIES = BASE_DIR / "communities.csv"
INFLUENCERS = BASE_DIR / "influenceurs.csv"
CENTRALITIES = BASE_DIR / "reseau_centralites.csv"

# =========================
# Output file
# =========================
OUTPUT_PATH = BASE_DIR / "dataset_final.csv"

# =========================
# Load datasets
# =========================
df_topics = pd.read_csv(COMMENTS_TOPICS)
df_sentiments = pd.read_csv(COMMENTS_SENTIMENTS)
df_communities = pd.read_csv(COMMUNITIES)
df_influencers = pd.read_csv(INFLUENCERS)
df_centralities = pd.read_csv(CENTRALITIES)

# =========================
# Merge Topics + Sentiments
# =========================
df = pd.merge(
    df_topics,
    df_sentiments[["comment_id", "sentiment"]],
    on="comment_id",
    how="left"
)

# =========================
# Add community info (author → community)
# =========================
df = pd.merge(
    df,
    df_communities,
    on="author",
    how="left"
)

# =========================
# Add influencer metrics
# =========================
df = pd.merge(
    df,
    df_influencers,
    on="author",
    how="left"
)

# =========================
# Add network centrality metrics
# =========================
df = pd.merge(
    df,
    df_centralities,
    on="author",
    how="left"
)

# =========================
# Fill missing values (users with no interactions)
# =========================
numeric_cols = [
    "nb_commentaires",
    "total_likes",
    "nb_reponses",
    "score_influence",
    "degree_centrality",
    "betweenness_centrality",
    "in_degree",
    "out_degree"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)

df["community_id"] = df["community_id"].fillna(-1)

# =========================
# Save final dataset
# =========================
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("Agrégation terminée : fichier dataset_final.csv généré")
