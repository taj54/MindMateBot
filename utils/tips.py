import random

TIPS = [
    "Take a deep breath. You're doing okay.",
    "Step outside and get some sunlight ☀️",
    "Stretch for a few minutes.",
    "Write down a worry and let it go."
]

def get_tip():
    return random.choice(TIPS)
