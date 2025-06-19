from telegram import ReplyKeyboardMarkup

# Mood emoji choices
MOOD_CHOICES = ["😊", "😔", "😠", "😰", "😴", "😇", "😕"]
MOOD_KEYBOARD = ReplyKeyboardMarkup(
    [[emoji for emoji in MOOD_CHOICES[:5]], [emoji for emoji in MOOD_CHOICES[5:]]],
    one_time_keyboard=True,
    resize_keyboard=True
)

# Stress scale as emoji
STRESS_SCALE = [str(i) for i in range(1, 11)]

# Quick reply keyboards
STRESS_KEYBOARD = ReplyKeyboardMarkup(
    [STRESS_SCALE[i:i+5] for i in range(0, 10, 5)],
    one_time_keyboard=True,
    resize_keyboard=True
)

# Generic messages
PRIVACY_NOTICE = (
    "🔒 Your responses are private and not stored.\n"
    "This check-in is just for your self-awareness. ❤️"
)

CHECKIN_START_MSG = (
    "🧠 Let’s begin your mental wellness check-in.\n"
    "Just three small steps — take your time."
)

THANK_YOU_MSG = (
    "✅ Thank you for taking a moment to reflect.\n"
    "Your mental well-being matters. 🌿"
)

HELP_FOOTER = (
    "Use /checkin anytime to reflect, or /tip for calming suggestions."
)
