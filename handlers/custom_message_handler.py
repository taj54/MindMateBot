from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from services.checkin_service import CheckinService
from services.admin_service import AdminService
from .base_handler import BaseHandler

class CustomMessageHandler(BaseHandler):
    def __init__(self):
        self.checkin = CheckinService()
        self.admin = AdminService()

    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if await self.admin.try_handle_admin(update, context):
            return
        await self.checkin.handle_checkin(update, context)

    @property
    def handler(self):
        return MessageHandler(filters.TEXT & ~filters.COMMAND, self.callback)

handler = CustomMessageHandler().handler
