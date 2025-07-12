import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد التوكن
TOKEN = os.environ.get("BOT_TOKEN")

# إعداد سجل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ البوت يعمل الآن... (Polling mode)")

    app.run_polling()

if __name__ == "__main__":
    main()
