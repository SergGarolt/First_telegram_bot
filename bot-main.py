from telegram.ext import Updater, MessageHandler, Filters, CommandHandler



TOKEN = '1501515491:AAGEsZn7RLqkgEzlM5wdjRBzh-CUUcOrvtk'

def main():
    updater = Updater(token=TOKEN)  # На этой строчке мы создали объект, который ловит сообщения из телеграмм

    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

def do_echo(update, context):

# Update - параметр, принимающий сообщения
# Context - параметр, запоминающий суть диалога с пользователем и реагирующий на основе предыдущих сообщений

    update.message.reply_text(text='AVE MARIA DEUS VOLT')

def do_start(update, context):


    update.message.reply_text(text='Приветствую! Как насчет похода на Иерусалим?')


main()