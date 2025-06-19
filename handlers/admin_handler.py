from telegram.ext import CommandHandler, CallbackQueryHandler
from .base_handler import BaseHandler
from services.admin_service import AdminService

admin_service = AdminService()

class AdminUserSelectHandler(BaseHandler):
    async def callback(self, update, context):
        await admin_service.show_user_selection(update, context)

    @property
    def handler(self):
        return CommandHandler("admin", self.callback)


class AdminUserCallbackHandler(BaseHandler):
    async def callback(self, update, context):
        await admin_service.handle_callback(update, context)

    @property
    def handler(self):
        return CallbackQueryHandler(self.callback, pattern="^admin_msg:|^admin_stop$")


# Export handlers
handler = AdminUserSelectHandler().handler
callback_handler = AdminUserCallbackHandler().handler
