from telegram import Update
from telegram.ext import ContextTypes

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("plan activated!")