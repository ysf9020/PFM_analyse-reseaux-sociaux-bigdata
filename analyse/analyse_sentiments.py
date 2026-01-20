import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pathlib import Path

# ===============================
# Chargement des données NLP ready
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "traitement" / "comments_nlp_ready.csv"

df = pd.read_csv(INPUT_PATH)

# ===============================
# Initialisation VADER
# ===============================

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positif"
    elif score <= -0.05:
        return "negatif"
    else:
        return "neutre"

# ===============================
# Application de l’analyse
# ===============================

df["sentiment"] = df["clean_text"].apply(get_sentiment)

# ===============================
# Sauvegarde des résultats
# ===============================

OUTPUT_PATH = BASE_DIR / "analyse" / "comments_sentiments.csv"
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("Analyse des sentiments terminée : fichier comments_sentiments.csv généré")
