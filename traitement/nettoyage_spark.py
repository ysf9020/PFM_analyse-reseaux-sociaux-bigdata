import json
import pandas as pd
from pathlib import Path

# ===============================
# Chargement des données
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "collecte-donnees" / "youtube_data.json"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# ===============================
# Flatten des commentaires
# ===============================

rows = []

for video in data:
    for comment in video.get("comments", []):
        if comment.get("author") and comment.get("text"):
            rows.append({
                "video_id": video["video_id"],
                "keyword": video["keyword"],
                "comment_id": comment["comment_id"],
                "author": comment["author"],
                "text": comment["text"],
                "likes": comment["likes"],
                "published_at": comment["published_at"],
                "reply_to": comment["reply_to"]
            })

df = pd.DataFrame(rows)

# ===============================
# Sauvegarde propre
# ===============================

OUTPUT_PATH = BASE_DIR / "traitement" / "comments_clean.csv"
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print(f"Nettoyage terminé : {len(df)} commentaires sauvegardés")
