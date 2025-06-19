from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.tips import get_tip
from .base_handler import BaseHandler  # ensure this exists

class TipHandler(BaseHandler):
    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        tip_text = get_tip()
        await update.message.reply_text(f"💡 Tip for you:\n\n{tip_text}")

    @property
    def handler(self):
        return CommandHandler("tip", self.callback)

# Export handler instance
handler = TipHandler().handler
