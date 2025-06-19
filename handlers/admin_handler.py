from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import ContextTypes
from services.admin_service import AdminService
from .base_handler import BaseHandler

admin_service = AdminService()

class AdminHandler(BaseHandler):
    async def admin_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if not admin_service.is_admin(user_id):
            await update.message.reply_text("❌ You are not authorized.")
            return

        await admin_service.show_user_selection(update, context)

    @property
    def handler(self):
        return CommandHandler("admin", self.admin_command)

class AdminCallbackHandler(BaseHandler):
    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await admin_service.handle_callback(update, context)

    @property
    def handler(self):
        return CallbackQueryHandler(self.callback, pattern=r"^admin_msg:")

# Export both handlers
handler = AdminHandler().handler
callback_handler = AdminCallbackHandler().handler
