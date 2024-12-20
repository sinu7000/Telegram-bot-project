from telegram import Update

async def forward_message(update: Update, context) -> None:
    try:
        
        target_chat_id = int(context.args[0])  
        message_id = update.message.message_id
        

        await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.message.chat_id, message_id=message_id)
        await update.message.reply_text('Message forwarded successfully.')
    except (IndexError, ValueError):
        await update.message.reply_text('Usage: /forward <chat_id>')
