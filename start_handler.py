from telegram import Update

async def start(update: Update, context) -> None:
    await update.message.reply_text('Hello! Welcome to Persist Ventures Bot.')
