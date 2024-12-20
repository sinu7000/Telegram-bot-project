from telegram import Update
import asyncio

async def remind(update: Update, context) -> None:
    try:
        seconds = int(context.args[0])
        await update.message.reply_text(f'Reminder set for {seconds} seconds.')
        await asyncio.sleep(seconds)
        await update.message.reply_text('Time is up! This is your reminder.')
    except (IndexError, ValueError):
        await update.message.reply_text('Usage: /remind <seconds>')
