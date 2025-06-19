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
        # 1️⃣ Admin replying to user
        if await self.admin.try_handle_admin(update, context):
            return

        # 2️⃣ User replying to admin
        if await self.admin.try_handle_user(update, context):
            return

        # 3️⃣ Default fallback to check-in system
        await self.checkin.handle_checkin(update, context)

    @property
    def handler(self):
        return MessageHandler(filters.TEXT & ~filters.COMMAND, self.callback)


# Export instance
handler = CustomMessageHandler().handler
