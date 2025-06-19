# utils/admin_session_store.py

import os
import json

SESSION_FILE = "storage/admin_sessions.json"

def set_admin_target(admin_id, target_user_id):
    if not os.path.exists("storage"):
        os.makedirs("storage")

    try:
        with open(SESSION_FILE, "r") as f:
            sessions = json.load(f)
    except:
        sessions = {}

    sessions[str(admin_id)] = target_user_id

    with open(SESSION_FILE, "w") as f:
        json.dump(sessions, f)

def get_admin_target(admin_id):
    if not os.path.exists(SESSION_FILE):
        return None

    try:
        with open(SESSION_FILE, "r") as f:
            sessions = json.load(f)
        return sessions.get(str(admin_id))
    except:
        return None

def clear_admin_target(admin_id):
    if not os.path.exists(SESSION_FILE):
        return

    try:
        with open(SESSION_FILE, "r") as f:
            sessions = json.load(f)
        sessions.pop(str(admin_id), None)
        with open(SESSION_FILE, "w") as f:
            json.dump(sessions, f)
    except:
        pass
