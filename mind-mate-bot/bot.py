import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes
from handlers import start, checkin, tip, help, messages, admin, admin_callback
from utils.logger import log_interaction


class MindMateBot:
    def __init__(self):
        # 🔐 Load environment and get token
        load_dotenv()
        self.token = os.getenv("TELEGRAM_TOKEN")
        if not self.token:
            raise RuntimeError("❌ TELEGRAM_TOKEN not found in .env file.")

        # 🏗️ Build the application
        self.app = ApplicationBuilder().token(self.token).build()

        # 🔧 Setup
        self.register_handlers()
        self.app.add_error_handler(self.error_handler)

    def register_handlers(self):
        """Attach all command and message handlers to the bot."""
        self.app.add_handler(start)
        self.app.add_handler(checkin)
        self.app.add_handler(tip)
        self.app.add_handler(help)
        self.app.add_handler(messages)

        # 🛡️ Admin
        self.app.add_handler(admin)
        self.app.add_handler(admin_callback)

    async def error_handler(self, update, context: ContextTypes.DEFAULT_TYPE):
        """Handle uncaught exceptions globally."""
        error_msg = f"⚠️ Exception: {context.error}"
        print(error_msg)

        if update and update.effective_user:
            await context.bot.send_message(
                chat_id=update.effective_user.id,
                text="⚠️ Something went wrong. Please try again."
            )

        log_interaction(
            user_id=update.effective_user.id if update and update.effective_user else 0,
            username=getattr(update.effective_user, "username", "unknown"),
            step="error",
            message_text=str(context.error),
            log_type="error"
        )

    def run(self):
        """Start polling for updates."""
        print("🤖 MindMateBot is running...")
        self.app.run_polling()


if __name__ == "__main__":
    bot = MindMateBot()
    bot.run()
