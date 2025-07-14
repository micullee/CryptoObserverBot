from config import BOT_TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import start, plan, exitplan, chifoi

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("plan", plan))
app.add_handler(CommandHandler("exitplan", exitplan))
app.add_handler(CommandHandler("chifoi", chifoi))

if __name__ == '__main__':
    app.run_polling()