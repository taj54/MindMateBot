import json
import os
from datetime import datetime

LOG_DIR = "storage"
LOG_FILE = os.path.join(LOG_DIR, "logs.json")


def ensure_log_file():
    """Ensure the log directory and file exist and are properly initialized."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)


def load_logs():
    """Load existing log data or return an empty list if the file is empty or corrupted."""
    try:
        with open(LOG_FILE, "r") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Warning: logs.json is empty or corrupted. Starting fresh.")
        return []


def save_logs(data):
    """Write the log data back to the file."""
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


def log_interaction(user_id, step, message_text, log_type="interaction", username=None):
    """
    Log a user action with optional username and log_type.
    
    Parameters:
        user_id (int): Telegram user ID
        username (str): Telegram username or fallback
        step (str): Step or context of the action
        message_text (str): What the user sent
        log_type (str): Type of log event ('login', 'checkin', etc.)
    """
    ensure_log_file()

    log_entry = {
        "user_id": user_id,
        "username": username or "Anonymous",
        "timestamp": datetime.now().isoformat(),
        "step": step,
        "message": message_text,
        "type": log_type
    }

    logs = load_logs()
    logs.append(log_entry)
    save_logs(logs)
