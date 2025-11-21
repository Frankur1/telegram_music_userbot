import json
import os

DB = "database.json"

def load_posts():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as f:
        return json.load(f)

def save_posts(posts):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

def add_post(date_str):
    posts = load_posts()
    posts.append(date_str)
    save_posts(posts)
