from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "5517246931:AAEULC_CaVCXt9TekQIxpSKoiteodGeQyig"

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("Salom! Men Telegram botman! 😊")

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
