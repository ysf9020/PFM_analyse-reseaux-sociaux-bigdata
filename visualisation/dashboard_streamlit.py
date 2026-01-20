import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ===============================
# Configuration
# ===============================
st.set_page_config(
    page_title="Analyse des Réseaux Sociaux",
    layout="wide"
)

# Custom CSS for tabs
st.markdown(
    """
    <style>
    /* Tabs container */
    div[data-baseweb="tab-list"] {
        gap: 40px;
        border-bottom: 2px solid #e0e0e0;
    }

    /* Tab titles */
    button[data-baseweb="tab"] {
        font-size: 20px !important;
        font-weight: 600 !important;
        padding: 12px 20px !important;
        color: #444;
    }

    /* Selected tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0d6efd !important;
        border-bottom: 3px solid #0d6efd !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

BASE_DIR = Path(__file__).resolve().parent.parent / "analyse"

# ===============================
# Load data
# ===============================
df_sentiments = pd.read_csv(BASE_DIR / "comments_sentiments.csv")
df_topics = pd.read_csv(BASE_DIR / "comments_topics.csv")
df_influencers = pd.read_csv(BASE_DIR / "influenceurs.csv")
df_network = pd.read_csv(BASE_DIR / "reseau_centralites.csv")
df_communities = pd.read_csv(BASE_DIR / "communities.csv")

# ===============================
# Header
# ===============================
st.title("📊 Dashboard – Analyse des Réseaux Sociaux")
st.caption("Sentiments • Thèmes dominants • Influence • Réseau • Communautés")

# ===============================
# KPIs
# ===============================
col1, col2, col3, col4 = st.columns(4)

col1.metric("💬 Commentaires", len(df_sentiments))
col2.metric("👤 Utilisateurs", df_sentiments["author"].nunique())
col3.metric("🧩 Topics", df_topics["topic_id"].nunique())
col4.metric("👥 Communautés", df_communities["community_id"].nunique())

st.divider()

# ===============================
# Tabs
# ===============================
tab1, tab2, tab3, tab4 = st.tabs(
    ["🧠 Sentiments", "🧩 Topics", "⭐ Influenceurs", "🕸 Réseau & Communautés"]
)

# ===============================
# TAB 1 — Sentiments
# ===============================
with tab1:
    st.subheader("Distribution globale des sentiments")

    fig = px.histogram(
        df_sentiments,
        x="sentiment",
        color="sentiment",
        title="Répartition des sentiments",
        color_discrete_map={
            "positif": "green",
            "neutre": "gray",
            "negatif": "red"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# TAB 2 — Topics
# ===============================
with tab2:
    st.subheader("Thèmes dominants")

    topic_counts = df_topics["topic_id"].value_counts().reset_index()
    topic_counts.columns = ["topic_id", "nb_commentaires"]

    fig = px.bar(
        topic_counts,
        x="topic_id",
        y="nb_commentaires",
        title="Nombre de commentaires par topic",
        color="topic_id"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Sentiment par topic")

    df_topic_sentiment = pd.merge(
        df_topics[["comment_id", "topic_id"]],
        df_sentiments[["comment_id", "sentiment"]],
        on="comment_id"
    )

    fig = px.histogram(
        df_topic_sentiment,
        x="topic_id",
        color="sentiment",
        barmode="group",
        title="Distribution des sentiments par topic"
    )
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# TAB 3 — Influenceurs
# ===============================
with tab3:
    st.subheader("Top 10 influenceurs")

    top_inf = df_influencers.sort_values(
        "score_influence", ascending=False
    ).head(10)

    fig = px.bar(
        top_inf,
        x="score_influence",
        y="author",
        orientation="h",
        title="Top 10 influenceurs",
        color="score_influence"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(top_inf, use_container_width=True)

# ===============================
# TAB 4 — Réseau & Communautés
# ===============================
with tab4:
    st.subheader("Centralité du réseau")

    top_central = df_network.sort_values(
        "betweenness_centrality", ascending=False
    ).head(10)

    st.dataframe(top_central, use_container_width=True)

    st.subheader("Taille des communautés (Top 10)")

    community_sizes = (
        df_communities["community_id"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    community_sizes.columns = ["community_id", "nb_utilisateurs"]

    fig = px.bar(
        community_sizes,
        x="community_id",
        y="nb_utilisateurs",
        title="Top 10 communautés par taille"
    )
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# Footer
# ===============================
st.divider()
st.caption(
    "Projet Big Data – Analyse des Réseaux Sociaux | "
    "Sentiments • Topics • Influence • Réseau • Communautés"
)
