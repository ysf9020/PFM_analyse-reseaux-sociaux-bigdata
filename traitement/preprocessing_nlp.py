import re
import pandas as pd
from pathlib import Path

# ===============================
# Chargement des données nettoyées
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "traitement" / "comments_clean.csv"

df = pd.read_csv(INPUT_PATH)

# ===============================
# Nettoyage du texte (NLP)
# ===============================

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["clean_text"] = df["text"].apply(clean_text)

# ===============================
# Suppression des textes vides
# ===============================

df = df[df["clean_text"] != ""]

# ===============================
# Sauvegarde finale
# ===============================

OUTPUT_PATH = BASE_DIR / "traitement" / "comments_nlp_ready.csv"
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("Prétraitement NLP terminé : fichier comments_nlp_ready.csv généré")
