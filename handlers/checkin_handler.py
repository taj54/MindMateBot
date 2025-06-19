from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.constants import CHECKIN_START_MSG, MOOD_KEYBOARD
from .base_handler import BaseHandler

class CheckinHandler(BaseHandler):
    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🧠 Let’s do a quick check-in.")
        await update.message.reply_text(CHECKIN_START_MSG, reply_markup=MOOD_KEYBOARD)
        context.user_data["step"] = "mood"

    @property
    def handler(self):
        return CommandHandler("checkin", self.callback)

handler = CheckinHandler().handler
