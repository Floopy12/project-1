import telebot 
import time



TOKEN = '5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA'
bot = telebot.TeleBot('5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA')


@bot.message_handler(commands = ['start'])
def start(message):
    keybord = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('Add new', callback_data = 'New position')
    button2 = telebot.types.InlineKeyboardButton('Change', callback_data = 'Change position')
    button3 = telebot.types.InlineKeyboardButton('Delete', callback_data = 'Delete position')
    keybord.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Что делаем?', reply_markup = keybord)
    















bot.infinity_polling()


