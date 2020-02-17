import telebot
from telebot import apihelper

apihelper.proxy = {f'https':'http://51.158.119.88:8811'}

bot = telebot.TeleBot('1066091653:AAHjPIY4AADwIzVL41y2UEzOUhSuEGza50I')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text oneof:
        bot.reply_to(message, "Hello, I'm drum bot:3")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, "I was not born to talk((\nIf you need help, type /help\n or type /menu")


bot.polling()
