import telebot 
import time



TOKEN = '5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA'
bot = telebot.TeleBot('5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA')


@bot.message_handler(commands = ['start'])
def start(message):
    keybord = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('Додати', callback_data = 'Нова позиція')
    button2 = telebot.types.InlineKeyboardButton('Змінити', callback_data = 'Змінити позицію')
    button3 = telebot.types.InlineKeyboardButton('Видалити', callback_data = 'Видалити позицію')
    keybord.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Що будемо робити?', reply_markup = keybord)
    















bot.infinity_polling()


