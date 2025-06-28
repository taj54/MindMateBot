import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes
from handlers import start, checkin, tip, help, messages, admin, admin_callback
from utils.logger import log_interaction


class MindMateBot:
    def __init__(self):
        # 🔐 Load environment variables
        load_dotenv()
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.webhook_url = os.getenv("WEBHOOK_URL")  # Optional for webhook deployments
        self.port = int(os.getenv("PORT", 8443))     # Default Render port

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

        user = getattr(update, "effective_user", None)
        username = getattr(user, "username", "unknown")
        user_id = user.id if user else 0

        # Notify user
        if user_id:
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text="⚠️ Something went wrong. Please try again."
                )
            except Exception:
                pass  # Fail silently if unable to send message

        log_interaction(
            user_id=user_id,
            username=username,
            step="error",
            message_text=str(context.error),
            log_type="error"
        )

    def run(self):
        """Start the bot using polling or webhook depending on environment."""
        print("🤖 MindMateBot is running...")

        if self.webhook_url:
            # Production mode: Use webhook (e.g. on Render)
            self.app.run_webhook(
                listen="0.0.0.0",
                port=self.port,
                webhook_url=self.webhook_url
            )
        else:
            # Development mode: Use polling
            self.app.run_polling()


def run_main():
    bot = MindMateBot()
    bot.run()
