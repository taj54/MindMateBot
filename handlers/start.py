from telegram.ext import CommandHandler

async def start(update, context):
    await update.message.reply_text(
        "👋 Hi! I’m MindMate. Use /checkin to reflect on your day 🌿"
    )

handler = CommandHandler("start", start)
    