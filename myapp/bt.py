from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
import argparse

# Объявление переменной бота
bot = TeleBot('5441210926:AAEIEO-xBalcs5XlUZD1gOVKav3HbdqjlTo')


# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#   bot.reply_to(message, "3ch support bot")

def send_msg(text):
  bot.send_message(-440766444,text)

def send_img(path):
  bot.send_photo(-440766444,path)
# bot.infinity_polling()
def send_audio(path):
  bot.send_audio(-440766444,path)