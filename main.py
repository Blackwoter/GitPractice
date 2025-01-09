import telebot
import os
from telebot import types
from PIL import ImageGrab

bot = telebot.TeleBot("7597921187:AAGMGKrSSJ8f4ofggI_BRBpaIKQ8J8mtCgs")


Button_1 = types.InlineKeyboardButton(text = 'Снимок экрана', callback_data = 'screen')
Button_2 = types.InlineKeyboardButton(text = 'Выключить компьютер.', callback_data = 'pc_off')
  
@bot.message_handler(commands=['start'])
def send_welcome(message):
    mark = types.InlineKeyboardMarkup()
    mark.add(Button_1, Button_2)
    bot.send_message(message.chat.id, "Компьютер запущен.", reply_markup = mark)

def back_welcome(call):
    mark = types.InlineKeyboardMarkup()
    mark.add(Button_1, Button_2)
    bot.send_message(call.message.chat.id, "Компьютер запущен.", reply_markup = mark)


def pc_off(call):
    os.system("shutdown /s /t 0")
    bot.reply_to(call.message, "Успех!")

@bot.callback_query_handler(func = lambda call: True)
def bot_sistem(call):
    global user_choise
    user_choise = ''
    if call.data == 'list':
        list(call)
    elif call.data == 'pc_off':    
        pc_off(call)

    
bot.infinity_polling()