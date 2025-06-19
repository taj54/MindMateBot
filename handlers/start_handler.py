from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.logger import log_interaction
from utils.user_store import add_user
from .base_handler import BaseHandler  

class StartHandler(BaseHandler):
    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handles the /start command. Marks the user as 'logged in' and sends a welcome message.
        """
        user = update.effective_user
        user_id = user.id
        username = user.username or user.first_name or "Anonymous"

        # Set user as logged in
        context.user_data["logged_in"] = True

        # Save to known user store
        add_user(user_id=user_id, username=username)

        # Log interaction
        log_interaction(
            user_id=user_id,
            username=username,
            step="login",
            message_text="/start",
            log_type="event"
        )

        # Welcome message
        await update.message.reply_text(
            f"👋 Welcome {username}!\nYou're now logged in to MindMateBot 🌿\n"
            "Use /checkin to start a wellness check or /help for guidance."
        )

    @property
    def handler(self):
        return CommandHandler("start", self.callback)

# Export instance
handler = StartHandler().handler
