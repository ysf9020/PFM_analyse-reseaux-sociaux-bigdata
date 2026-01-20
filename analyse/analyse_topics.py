import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# ===============================
# Configuration
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "traitement" / "comments_nlp_ready.csv"
OUTPUT_PATH = BASE_DIR / "analyse" / "topics.csv"

N_TOPICS = 5
N_TOP_WORDS = 8

# ===============================
# Chargement des données
# ===============================

df = pd.read_csv(INPUT_PATH)

texts = df["clean_text"].dropna().astype(str)

# ===============================
# Vectorisation TF-IDF
# ===============================

vectorizer = TfidfVectorizer(
    max_df=0.9,
    min_df=5,
    stop_words="english"
)

X = vectorizer.fit_transform(texts)

# ===============================
# Topic Modeling avec LDA
# ===============================

lda = LatentDirichletAllocation(
    n_components=N_TOPICS,
    random_state=42
)

lda.fit(X)

# ===============================
# Extraction des mots-clés par topic
# ===============================

feature_names = vectorizer.get_feature_names_out()

topics = []

for topic_idx, topic in enumerate(lda.components_):
    top_words = [
        feature_names[i]
        for i in topic.argsort()[:-N_TOP_WORDS - 1:-1]
    ]
    topics.append({
        "topic_id": topic_idx,
        "mots_cles": ", ".join(top_words)
    })

df_topics = pd.DataFrame(topics)

# ===============================
# Attribution d'un topic à chaque commentaire
# ===============================

topic_distribution = lda.transform(X)
dominant_topics = topic_distribution.argmax(axis=1)

df_topics_comments = df.loc[texts.index].copy()
df_topics_comments["topic_id"] = dominant_topics

# ===============================
# Sauvegardes
# ===============================

df_topics.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
df_topics_comments.to_csv(
    BASE_DIR / "analyse" / "comments_topics.csv",
    index=False,
    encoding="utf-8"
)

print("Topic modeling terminé : fichiers topics.csv et comments_topics.csv générés")
