import menuData
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

myToken = #insert token

bot = telegram.Bot(token=myToken)
updater = Updater(token=myToken)
dispatcher = updater.dispatcher

def start(bot,update):
    keyboard = [[InlineKeyboardButton("Student", callback_data='student'),
                 InlineKeyboardButton("Public Servant", callback_data='publicservant')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose the price type for the menu:', reply_markup=reply_markup)

def menu(bot,update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id, text=menuData.displayMenu(query.data))

start_handler = CommandHandler('start', start)

dispatcher.add_handler(CallbackQueryHandler(menu))
dispatcher.add_handler(start_handler)
updater.start_polling()
