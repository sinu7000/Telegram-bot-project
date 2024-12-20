from telegram.ext import Application, CommandHandler
from handlers.start_handler import start
from handlers.remind_handler import remind
from handlers.forward_handler import forward_message
from handlers.task_handler import task_management

def main():
   
    application = Application.builder().token("7770142037:AAFpMXXk4Ygz3VBWQRzwELHMjydvBwp30I8").build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("remind", remind))
    application.add_handler(CommandHandler("forward", forward_message))
    application.add_handler(CommandHandler("task", task_management))

    
    application.run_polling()

if __name__ == '__main__':
    main()
