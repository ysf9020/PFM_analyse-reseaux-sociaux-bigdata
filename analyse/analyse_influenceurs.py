import pandas as pd
from pathlib import Path

# ===============================
# Chargement des données enrichies
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "analyse" / "comments_sentiments.csv"

df = pd.read_csv(INPUT_PATH)

# ===============================
# Calcul des indicateurs d’influence
# ===============================

influence = df.groupby("author").agg(
    nb_commentaires=("comment_id", "count"),
    total_likes=("likes", "sum"),
    nb_reponses=("reply_to", lambda x: x.notna().sum())
).reset_index()

# Score d’influence simple
influence["score_influence"] = (
    influence["nb_commentaires"] * 1 +
    influence["total_likes"] * 2 +
    influence["nb_reponses"] * 3
)

# ===============================
# Sauvegarde
# ===============================

OUTPUT_PATH = BASE_DIR / "analyse" / "influenceurs.csv"
influence.sort_values("score_influence", ascending=False).to_csv(
    OUTPUT_PATH, index=False, encoding="utf-8"
)

print("Analyse des influenceurs terminée : fichier influenceurs.csv généré")
