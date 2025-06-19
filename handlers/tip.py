from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.tips import get_tip

# /tip command handler
async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tip_text = get_tip()
    await update.message.reply_text(f"💡 Tip for you:\n\n{tip_text}")

# Export handler
handler = CommandHandler("tip", tip)
