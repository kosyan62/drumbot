import telebot
from telebot import apihelper
from full_drum_rhytm import get_rhytm

apihelper.proxy = {f'https':'http://51.158.119.88:8811'}

bot = telebot.TeleBot('1066091653:AAHjPIY4AADwIzVL41y2UEzOUhSuEGza50I')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
        bot.reply_to(message, "Hello, this is help message, it will help you make things")

@bot.message_handler(commands=['rhytm'])
def handle_start_rhytm_choose(message):
    bot.reply_to(message, "Please, choose long or short rhytm")

@bot.message_handler(commands=['longrhytm'])
def return_long_rhytm(message):
    get_rhytm(2)
    image = open('rhytm.png', 'rb')
    bot.send_photo(message.from_user.id, photo=image)

@bot.message_handler(commands=['shortrhytm'])
def return_short_rhytm(message):
    get_rhytm(1)
    image = bot.send_photo(message.from_user.id, photo=image)
    
bot.polling()
