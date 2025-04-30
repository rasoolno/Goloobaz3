from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات GolooBaz خوش اومدی!")

app = ApplicationBuilder().token("7993730901:AAH5WoKtXYKbQLi08lGJRwBgcFFEOpOtJZ0").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
