import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# الحصول على التوكن من متغير البيئة في Render
TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = f"https://telegram-bot-oj6w.onrender.com/{TOKEN}"  # عدل هذا حسب رابط Render الخاص بك

# إنشاء تطبيق Flask
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# دالة الرد على /start
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

# إضافة معالج الأمر /start
application.add_handler(CommandHandler("start", start))

# صفحة الفحص
@app.route("/")
def index():
    return "Bot is alive!"

# ربط Webhook
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)

    if not application.running:
        await application.initialize()
        await application.start()

    await application.process_update(update)
    return "OK"

# تشغيل التطبيق
if __name__ == "__main__":
    async def main():
        await application.initialize()
        await application.bot.set_webhook(url=WEBHOOK_URL)
        await application.start()
        app.run(host="0.0.0.0", port=10000)

    asyncio.run(main())
