import telebot
from telebot import apihelper
from telebot import types

from full_drum_rhytm import get_rhytm
from full_rudi_rhytm import get_rudiments
from full_snare_rudim import get_snare
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_help(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Рудименты")
        item2 = types.KeyboardButton("Акценты")
        item3 = types.KeyboardButton("Ритм")
        markup.add(item1, item2, item3) 
        bot.reply_to(message, "Привет\nВыбери, что тебе интересно", reply_markup=markup)

def rhythm_choose(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Длинный ритм")
        item2 = types.KeyboardButton("Короткий ритм")
        markup.add(item1, item2)
        bot.reply_to(message, "Выбери, что ты хочешь тренировать.", reply_markup=markup)

def return_long_rhythm(message):
    get_rhytm(4)
    with open(f'rhytm.png', 'rb') as d1:
        bot.send_photo(message.from_user.id, photo=d1)
def return_short_rhythm(message):
    get_rhytm(2)
    with open(f'rhytm.png', 'rb') as d1:
        bot.send_photo(message.from_user.id, photo=d1)

def return_snare(message):
    get_snare()
    with open(f'rhytm.png', 'rb') as d1:
        bot.send_photo(message.from_user.id, photo=d1)


def return_rudiments(message):
    get_rudiments()
    with open(f'rhytm.png', 'rb') as d1:
        bot.send_photo(message.from_user.id, photo=d1)

@bot.message_handler(content_types=['text'])
def choose(message):
    if message.text=='Ритм':
        rhythm_choose(message)
    elif message.text=='Акценты':
        return_snare(message)
    elif message.text=='Рудименты':
        return_rudiments(message)
    elif message.text=='Длинный ритм':
        return_long_rhythm(message)
    elif message.text=='Короткий ритм':
        return_short_rhythm(message)

bot.polling()
