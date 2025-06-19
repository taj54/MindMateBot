from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from utils.logger import log_interaction  

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    step = context.user_data.get("step")

    if not step:
        await update.message.reply_text(
            "Hi! Use /checkin to start a quick mental wellness check-in 🌿"
        )
        return

    # Log this message with the current step
    log_interaction(user_id=user_id, step=step, message_text=text)

    # Step 1: Mood
    if step == "mood":
        context.user_data["mood"] = text
        await update.message.reply_text("2️⃣ Got it. What’s been on your mind lately?")
        context.user_data["step"] = "thoughts"

    # Step 2: Thoughts
    elif step == "thoughts":
        context.user_data["thoughts"] = text
        await update.message.reply_text("3️⃣ On a scale of 1 to 10, how stressed are you right now?")
        context.user_data["step"] = "stress"

    # Step 3: Stress level
    elif step == "stress":
        context.user_data["stress"] = text

        mood = context.user_data.get("mood", "N/A")
        thoughts = context.user_data.get("thoughts", "N/A")
        stress = context.user_data.get("stress", "N/A")

        await update.message.reply_text(
            "✅ Thanks for checking in with yourself.\n\n"
            f"🧠 Mood: {mood}\n"
            f"💭 Thoughts: {thoughts}\n"
            f"📈 Stress Level: {stress}/10\n\n"
            "You’ve done something good for your mind today. 🌿\n"
            "If you'd like, you can now try /tip for a helpful idea."
        )

        context.user_data.clear()

# Export handler
handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
