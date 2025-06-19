import json
import os

SESSIONS_FILE = "storage/admin_sessions.json"

def _load():
    if not os.path.exists(SESSIONS_FILE):
        return {}
    with open(SESSIONS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def _save(data):
    os.makedirs(os.path.dirname(SESSIONS_FILE), exist_ok=True)
    with open(SESSIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_admin_target(admin_id: int, user_id: int):
    """Assign a user to an admin for direct messaging"""
    data = _load()
    data[str(admin_id)] = user_id
    _save(data)

def get_admin_target(admin_id: int):
    """Get the user ID that this admin is currently messaging"""
    return _load().get(str(admin_id))

def clear_admin_target(admin_id: int):
    """Remove the messaging target for the given admin"""
    data = _load()
    data.pop(str(admin_id), None)
    _save(data)

def get_admin_for_user(user_id: int):
    """Check if any admin is in a messaging session with the given user"""
    data = _load()
    for admin_id_str, target_id in data.items():
        if target_id == user_id:
            return int(admin_id_str)
    return None
