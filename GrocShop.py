import telebot 
import time
from telebot import types


TOKEN = '5970658595:AAHgZ_aUyFw-urXX2IZWx3pRfadQ6DNjS7M'
bot = telebot.TeleBot(TOKEN)

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
        total = ''
        for type in position_types:
            total += f'{type.name}:\n'
            for position in positions:
                if position.positiontype == type:
                    total += f'{position.name}\nЦена: {position.price} грн\n'
            total += '\n\n'
        bot.send_message(message.chat.id, total)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'Нова позиція':
        bot.send_message(call.message.chat.id, 'Введіть: Класс, назву, ціну, додайте фото')
    elif call.data == 'Змінити позицію':
        bot.send_message(call.message.chat.id, 'Послідовно введіть нові данні:Класс, назву, ціну, додайте фото')
    elif call.data == 'Видалити позицію':
        bot.send_message(call.message.chat.id, 'Виберіть позицію, яку бажаете видалити')

    







class Position:
    def __init__(self, name, price, photo, possitiontype:'PositionType'):
        self.name = name
        self.price = price
        self.photo = photo
        self.positiontype = possitiontype

class PositionType:
    def __init__(self, name):
        self.name = name

# drinks = PositionType('Напитки')
# laptops = PositionType('Ноутбуки')
position_types = []
position_types.append(PositionType('Нпитки'))
position_types.append(PositionType('Ноутбуки'))
positions = []

positions.append(Position('Coca-cola', 10, None, position_types[0]))
positions.append(Position('sprite', 8, None, position_types[0]))
positions.append(Position('ASUS',10000,None, position_types[1]))






bot.polling(none_stop=True)


