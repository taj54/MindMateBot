import os
import json
from datetime import datetime

USERS_FILE = "storage/users.json"

def ensure_user_file():
    if not os.path.exists("storage"):
        os.makedirs("storage")
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([], f)

def add_user(user_id, username):
    ensure_user_file()
    with open(USERS_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    if not any(user["user_id"] == user_id for user in data):
        data.append({
            "user_id": user_id,
            "username": username or "Anonymous",
            "joined": datetime.now().isoformat()
        })

        with open(USERS_FILE, "w") as f:
            json.dump(data, f, indent=2)

def get_all_users():
    ensure_user_file()
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

