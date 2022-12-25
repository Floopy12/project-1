import telebot 
import time
from telebot import types


TOKEN = '5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA'
bot = telebot.TeleBot('5961836068:AAGuMNBmcP7TAQnJLjB0vLq0PsgcQypqMiA')

ADMIN = [662765024]




@bot.message_handler(commands = ['start'])
def start(message):
    if  message.from_user.id in ADMIN:
        keybord = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton('Додати', callback_data = 'Нова позиція')
        button2 = telebot.types.InlineKeyboardButton('Змінити', callback_data = 'Змінити позицію')
        button3 = telebot.types.InlineKeyboardButton('Видалити', callback_data = 'Видалити позицію')
        keybord.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Що будемо робити?', reply_markup = keybord)
    else:
        bot.send_message(message.chat.id, 'Перечень товаров')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'Нова позиція':
        bot.send_message(call.message.chat.id, 'Введіть: Класс, назву, ціну, додайте фото')
    elif call.data == 'Змінити позицію':
        bot.send_message(call.message.chat.id, 'Послідовно введіть нові данні:Класс, назву, ціну, додайте фото')
    elif call.data == 'Видалити позицію':
        bot.send_message(call.message.chat.id, 'Виберіть позицію, яку бажаете видалити')

    







class Positions:
    def __init__(self, name, price, photo):
        self.name = name
        self.price = price
        self.photo = photo

class Drinks(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)

drink = []

class Cheeses(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)


chees = []


class Sausages(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)


class Milk(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)


sauseg = []

class Milks(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)

milk = []

class Fruits(Positions):
    def __init__(self, name, price, photo):
        super().__init__(name, price, photo)


fruit = []








bot.polling(none_stop=True)


