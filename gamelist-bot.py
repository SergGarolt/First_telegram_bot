from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook


TOKEN = '1799218775:AAGOCz4CnagUDahkyAx9QdXbv_dKJIdrcG8'
book = load_workbook('Game List.xlsx')
sheet_1 = book['list1']


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)
    keybord_handler = MessageHandler(Filters.text, do_something)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(keybord_handler)
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

def do_echo(update, context):


    update.message.reply_text(text='ОШИБКА! Бот еще далек от завершения...')

def do_start(update, context):
    keybord = [
        ['Apex Legends', 'Star Wars Battlefront 2', 'Minecraft Windows 10 edition'],
    ]

    update.message.reply_text(
        text='Ваш список игр:',
        reply_markup=ReplyKeyboardMarkup(keybord, one_time_keyboard=True, resize_keyboard=True)
    )

def do_something(update: Update, context):
    text = update.message.text

   # if text == 'Конечно!':
    #    update.message.reply_text('AVE MARIA DEUS VOLT', reply_markup=ReplyKeyboardRemove())
    #elif text == '2':
    #    update.message.reply_text('Вы нажали кнопку 2', reply_markup=ReplyKeyboardRemove())
    #elif text == '3':
    #    update.message.reply_text('Вы нажали кнопку 3', reply_markup=ReplyKeyboardRemove())
    #else:
    #    update.message.reply_text('Ошибочка')
#доделать клавиатуру

main()