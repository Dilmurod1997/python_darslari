# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:12:02 2023

@author: Sharipov
"""
from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = '5931401380:AAGtScObHY3RyixDZGTA8djEc1Choa-Ra-0'

bot = telebot.TeleBot(TOKEN)


# Handle /start and /help
@bot.message_handler(commands=['start'])
def command_help(message):
    javob = "Assalomu alaykum botimizga xush kelibsiz!!!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda message: True)
def main_handler(message):
    msg = message.text
    if msg.isascii():  
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
        
    bot.reply_to(message,javob)
bot.polling()


