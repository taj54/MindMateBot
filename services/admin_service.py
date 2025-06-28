import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from dotenv import load_dotenv

from utils.admin_session_store import (
    set_admin_target,
    get_admin_target,
    clear_admin_target,
    get_admin_for_user,  # 🔁 for two-way chat
)
from utils.user_store import get_all_users
from utils.logger import log_interaction

# 🔐 Load admin IDs from .env
load_dotenv()
ADMIN_IDS = [
    int(uid.strip())
    for uid in os.getenv("ADMIN_IDS", "").split(",")
    if uid.strip().isdigit()
]

class AdminService:
    def __init__(self):
        pass

    def is_admin(self, user_id: int) -> bool:
        return user_id in ADMIN_IDS

    async def show_user_selection(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        if update.callback_query:
            sender = update.callback_query.from_user
        elif update.message:
            sender = update.message.from_user
        else:
            return

        sender_id = sender.id

        if not self.is_admin(sender_id):
            if update.callback_query:
                await update.callback_query.answer()
                await update.callback_query.edit_message_text(
                    "❌ You are not authorized."
                )
            else:
                await update.message.reply_text("❌ You are not authorized.")
            return

        # 1️⃣ Admin replying to user
        users = get_all_users()
        if not users:
            await update.message.reply_text("⚠️ No users found.")
            return

        buttons = [
            [
                InlineKeyboardButton(
                    f"✉️ {u['username']} ({u['user_id']})",
                    callback_data=f"admin_msg:{u['user_id']}",
                )
            ]
            for u in users
        ]
        markup = InlineKeyboardMarkup(buttons)

        await update.message.reply_text(
            "Select a user to message:", reply_markup=markup
        )

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle user selection or stop chat callback"""
        query = update.callback_query
        sender_id = query.from_user.id

        if not self.is_admin(sender_id):
            await query.answer()
            await query.edit_message_text("❌ You are not authorized.")
            return

        data = query.data

        if data.startswith("admin_msg:"):
            # ✅ Start chat session
            target_user_id = int(data.split(":")[1])
            set_admin_target(sender_id, target_user_id)

            stop_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🛑 Stop Chat", callback_data="admin_stop")]]
            )

            await query.answer()
            await query.edit_message_text(
                f"✅ You selected user <code>{target_user_id}</code>.\nNow type your message.",
                parse_mode="HTML",
                reply_markup=stop_markup,
            )

        elif data == "admin_stop":
            clear_admin_target(sender_id)
            await query.answer()
            await query.edit_message_text("🛑 Chat session stopped.")

    async def try_handle_admin(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> bool:
        """If admin is replying to a selected user, forward message and return True"""
        admin_id = update.effective_user.id
        if not self.is_admin(admin_id):
            return False

        target_user_id = get_admin_target(admin_id)
        if not target_user_id:
            return False

        message_text = update.message.text

        await context.bot.send_message(
            chat_id=target_user_id,
            text=f"📬 Message from MindMate Admin:\n\n{message_text}",
        )
        await update.message.reply_text("✅ Message sent to user.")

        log_interaction(
            user_id=admin_id,
            username=update.effective_user.username or update.effective_user.first_name,
            step="admin_msg",
            message_text=f"To {target_user_id}: {message_text}",
            log_type="admin",
        )

        return True

    async def try_handle_user(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> bool:
        """If a user is in active admin chat, forward message to admin"""
        user_id = update.effective_user.id
        admin_id = get_admin_for_user(user_id)

        if not admin_id:
            return False

        message_text = update.message.text
        username = update.effective_user.username or update.effective_user.first_name

        await context.bot.send_message(
            chat_id=admin_id,
            text=f"📨 Reply from {username} (`{user_id}`):\n\n{message_text}",
            parse_mode="Markdown",
        )

        log_interaction(
            user_id=user_id,
            username=username,
            step="user_reply",
            message_text=message_text,
            log_type="admin_chat",
        )

        return True
