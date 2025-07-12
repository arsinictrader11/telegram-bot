import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = f"https://telegram-bot-oj6w.onrender.com/{TOKEN}"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "بقدملك في القناة..\n\n"
        "_ اولا وأهم حاجه محتوي تعليمي قادر يحولك من مبتدأ لشخص قادر يعتمد علي نفسه وياخد صفقات❤️_\n\n"
        "_ جلسات تحليل يوميا مع صفقات مدروسة بعناية👌❤️_\n\n"
        "_ لايفات اسبوعيه مع الفريق لشرح استراتيجيات جديدة❤️_\n\n"
        "_ خطط مخصصة لكل شخص لأدارة رأس ماله بطريقة صحيحة👌❤️_\n\n"
        "_ متابعه بشكل يومي مع كامل اعضاء الفريق لتحقيق نتائج ممتازة👌❤️_\n\n"
        "*رابط القناة تفضل للانضمام:*\n"
        "[اضغط هنا للانضمام](https://t.me/Arsenic_Trader0)"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل /start لتجربة البوت.")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# هذه فقط لتأكيد أن السيرفر يعمل لـ Render
@app.route("/")
def home():
    return "✅ Bot is alive!"

# استقبال الرسائل من Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)

    if not application.running:
        await application.initialize()
        await application.start()

    await application.process_update(update)
    return "OK"

# إعداد الـ Webhook
if __name__ == "__main__":
    async def main():
        await application.initialize()
        await application.bot.set_webhook(url=WEBHOOK_URL)
        await application.start()
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

    asyncio.run(main())
