import telebot
from telebot import apihelper
from full_drum_rhytm import get_rhytm
import config
from telebot import types

apihelper.proxy = {'https':'socks5h://54.38.195.161:55919'}

bot = telebot.TeleBot('1066091653:AAHjPIY4AADwIzVL41y2UEzOUhSuEGza50I')


@bot.message_handler(commands=['start'])
def handle_start_help(message):
        bot.reply_to(message, "Привет\nВыбери, что тебе интересно")
        markup = ReplyKeyboardMarkup(reszize_keyboard=True)
        item1 = types.KeyboardButton("Рудименты")
        item2 = types.KeyboardButton("Акценты")
        item3 = types.KeyboardButton("Ритм")
        markup.add(item1, item2, item3) 

def rhythm_choose(message):
        bot.reply_to(message, "Привет\nВыбери, что ты хочешь тренировать.")
        markup = ReplyKeyboardMarkup(reszize_keyboard=True)
        item1 = types.KeyboardButton("Длинный ритм")
        item2 = types.KeyboardButton("Короткий ритм")
        markup.add(item1, item2)

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
def choose(mesage):
    if message.text=='Ритм':
        rhythm_choose()
    elif message.text=='Акценты':
        return_snare(message)
    elif message.text=='Рудименты':
        return_rudimeents(message)
    elif message.text=='Длинный ритм':
        return_long_rhythm(message)
    elif message.text=='Короткий ритм':
        return_short_rhythm(message)

bot.polling()
