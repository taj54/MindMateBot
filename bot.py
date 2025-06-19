import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes
from handlers import  start, checkin, tip, help, messages,admin, admin_callback
from utils.logger import log_interaction

# 🔐 Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ TELEGRAM_TOKEN not found in environment variables.")

# ❗ Global error handler
async def error_handler(update, context: ContextTypes.DEFAULT_TYPE):
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

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # ✅ Core feature handlers
    app.add_handler(start)       
    app.add_handler(checkin)      
    app.add_handler(tip)          
    app.add_handler(help)         
    app.add_handler(messages)     

    # 🛡️ Admin tools
    app.add_handler(admin)           
    app.add_handler(admin_callback)  

    # ❗ Global error handler
    app.add_error_handler(error_handler)

    print("🤖 MindMateBot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
