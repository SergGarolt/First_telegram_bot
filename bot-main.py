from telegram.ext import Updater, MessageHandler, Filters, CommandHandler



TOKEN = '1501515491:AAGEsZn7RLqkgEzlM5wdjRBzh-CUUcOrvtk'

def main():
    updater = Updater(token=TOKEN)  # На этой строчке мы создали объект, который ловит сообщения из телеграмм

    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help) # Это второй шаг создания команды

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler) # Это третий, самый важный этап создания команды - регистрация.
    # Важно регистрировать команды в правильном порядке - если поставить эту регистрацию после той, что реагирует на все незарегестрированные команды - эта команда обработается как незарегестрированная
    # Диспетчер бота прогоняет команду по функциям и "скармливает" ее первой подошедшей для команды
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()  # Эти две строки запускают бота

def do_echo(update, context):

# Update - параметр, принимающий сообщения
# Context - параметр, запоминающий суть диалога с пользователем и реагирующий на основе предыдущих сообщений

    update.message.reply_text(text='AVE MARIA DEUS VOLT')

def do_start(update, context):


    update.message.reply_text(text='Приветствую! Как насчет похода на Иерусалим?')
    # Сама суть функции - принять два параметра и среагировать на что-то, дальше по коду.
    # Создание функции - первый шаг к созданию обрабатываемой команды


def do_help(update, context):


    update.message.reply_text(text='Я пока не умею тебе отвечать нормально, только шутки про крестовые походы :)')


main()