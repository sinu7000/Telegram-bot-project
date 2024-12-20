from telegram import Update

tasks = []

async def task_management(update: Update, context) -> None:
    try:
        
        command = context.args[0].lower()

        if command == "add":
            task = ' '.join(context.args[1:])
            tasks.append(task)
            await update.message.reply_text(f'Task added: {task}')
        
        elif command == "list":
            if tasks:
                task_list = '\n'.join([f"{idx+1}. {task}" for idx, task in enumerate(tasks)])
                await update.message.reply_text(f'Your tasks:\n{task_list}')
            else:
                await update.message.reply_text('No tasks available.')

        elif command == "remove":
            task_index = int(context.args[1]) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                await update.message.reply_text(f'Task removed: {removed_task}')
            else:
                await update.message.reply_text('Invalid task number.')
        
        else:
            await update.message.reply_text('Invalid command. Use /task add <task>, /task list, or /task remove <number>')

    except IndexError:
        await update.message.reply_text('Usage: /task add <task>, /task list, /task remove <number>')
