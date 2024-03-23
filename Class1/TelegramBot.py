import os
# https://pypi.org/project/pyTelegramBotAPI/

import telebot

BOT_TOKEN = "7033144207:AAEtDk9ejFyKcVYulfT6inA6REkAVlciWQg"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    print(message.text)


bot.infinity_polling()
