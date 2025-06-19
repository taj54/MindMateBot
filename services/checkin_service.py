from utils.logger import log_interaction

class CheckinService:
    async def handle_checkin(self, update, context):
        user_id = update.effective_user.id
        text = update.message.text
        step = context.user_data.get("step")

        if not step:
            await update.message.reply_text("Hi! Use /checkin to begin 🌿")
            return

        log_interaction(user_id=user_id, step=step, message_text=text)

        if step == "mood":
            context.user_data["mood"] = text
            context.user_data["step"] = "thoughts"
            await update.message.reply_text("2️⃣ What’s on your mind?")
        elif step == "thoughts":
            context.user_data["thoughts"] = text
            context.user_data["step"] = "stress"
            await update.message.reply_text("3️⃣ On a scale of 1–10, how stressed are you?")
        elif step == "stress":
            context.user_data["stress"] = text
            await self._summarize(update, context)
            context.user_data.clear()

    async def _summarize(self, update, context):
        mood = context.user_data.get("mood", "N/A")
        thoughts = context.user_data.get("thoughts", "N/A")
        stress = context.user_data.get("stress", "N/A")

        await update.message.reply_text(
            f"✅ Check-in complete:\n\n"
            f"🧠 Mood: {mood}\n"
            f"💭 Thoughts: {thoughts}\n"
            f"📈 Stress: {stress}/10\n\n"
            f"Try /tip for a wellness idea!"
        )
