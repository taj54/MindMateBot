from telegram.ext import ApplicationBuilder
from handlers import start, checkin, tip, help, messages
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(start.handler)
    app.add_handler(checkin.handler)
    app.add_handler(tip.handler)
    app.add_handler(help.handler)
    app.add_handler(messages.handler)

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
