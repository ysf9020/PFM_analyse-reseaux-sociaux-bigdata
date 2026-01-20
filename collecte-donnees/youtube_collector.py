from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yaml
import json
from datetime import datetime, timezone
from pathlib import Path

# ===============================
# Chargement de la configuration
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "config_api.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

API_KEY = config["youtube"]["api_key"]
MAX_VIDEOS = config["youtube"]["max_videos"]
MAX_COMMENTS = config["youtube"]["max_comments_per_video"]

# ===============================
# Initialisation API YouTube
# ===============================

youtube = build("youtube", "v3", developerKey=API_KEY)

KEYWORDS = [
    "Western Sahara Morocco",
    "Sahara conflict Morocco",
    "Morocco Polisario",
    "Polisario Front"
]

# ===============================
# Recherche des vidéos
# ===============================

def search_videos(query):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=MAX_VIDEOS
    )
    response = request.execute()
    return response.get("items", [])

# ===============================
# Récupération des commentaires
# ===============================

def get_comments(video_id):
    comments = []

    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=MAX_COMMENTS,
            textFormat="plainText"
        )

        response = request.execute()

        for item in response.get("items", []):
            top = item["snippet"]["topLevelComment"]["snippet"]

            comments.append({
                "comment_id": item["id"],
                "author": top.get("authorDisplayName"),
                "text": top.get("textDisplay"),
                "likes": top.get("likeCount"),
                "published_at": top.get("publishedAt"),
                "reply_to": None
            })

            if item["snippet"]["totalReplyCount"] > 0:
                replies_request = youtube.comments().list(
                    part="snippet",
                    parentId=item["id"],
                    maxResults=MAX_COMMENTS
                )
                replies_response = replies_request.execute()

                for reply in replies_response.get("items", []):
                    snippet = reply["snippet"]
                    comments.append({
                        "comment_id": reply["id"],
                        "author": snippet.get("authorDisplayName"),
                        "text": snippet.get("textDisplay"),
                        "likes": snippet.get("likeCount"),
                        "published_at": snippet.get("publishedAt"),
                        "reply_to": item["id"]
                    })

    except HttpError as e:
        # Cas normal : commentaires désactivés
        print(f"[INFO] Commentaires désactivés pour la vidéo {video_id}")

    return comments

# ===============================
# Collecte globale
# ===============================

def collect_data():
    dataset = []

    for keyword in KEYWORDS:
        videos = search_videos(keyword)

        for video in videos:
            video_id = video["id"]["videoId"]

            dataset.append({
                "video_id": video_id,
                "title": video["snippet"]["title"],
                "channel": video["snippet"]["channelTitle"],
                "published_at": video["snippet"]["publishedAt"],
                "keyword": keyword,
                "comments": get_comments(video_id),
                "collected_at": datetime.now(timezone.utc).isoformat()
            })

    return dataset

# ===============================
# Main
# ===============================

if __name__ == "__main__":
    data = collect_data()

    output_path = Path(__file__).parent / "youtube_data.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Collecte terminée : {len(data)} vidéos")
