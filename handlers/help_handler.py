from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from .base_handler import BaseHandler 

class HelpHandler(BaseHandler):
    """
    Handles the /help command.
    Displays mental health resources and bot usage tips.
    """

    async def callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "🆘 *You’re not alone. Here are some resources that might help:*\n\n"
            "📞 *Mental Health Helplines:*\n"
            "• India: iCall – 9152987821 (Mon–Sat, 10am–8pm)\n"
            "• US: 988 (24/7 Suicide & Crisis Lifeline)\n"
            "• UK: Samaritans – 116 123\n\n"
            "🌐 *Find a Therapist:*\n"
            # "• [BetterHelp](https://www.betterhelp.com/)\n"
            # "• [Psychology Today](https://www.psychologytoday.com/)\n\n"
            "💬 *Self-help Tools:*\n"
            "• Use /checkin to reflect on your day\n"
            "• Try /tip for a calming suggestion\n\n"
            "🔒 *This bot does not store personal data. Your privacy is respected.*"
        )

        await update.message.reply_text(help_text, parse_mode="Markdown")

    @property
    def handler(self) -> CommandHandler:
        return CommandHandler("help", self.callback)

# 🎯 Export handler instance
handler = HelpHandler().handler
