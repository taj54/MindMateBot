from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.constants import MOOD_KEYBOARD, CHECKIN_START_MSG

async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Initiates a 3-step mental health check-in starting with the user's mood.
    Stores 'mood' as the first step in context.user_data.
    """
    await update.message.reply_text("🧠 Let’s do a quick check-in.")
    await update.message.reply_text(
        CHECKIN_START_MSG,
        reply_markup=MOOD_KEYBOARD
    )

    # Set step for message routing
    context.user_data["step"] = "mood"

# Export as handler for main bot registration
handler = CommandHandler("checkin", checkin)
