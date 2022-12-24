from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
import argparse

# Объявление переменной бота
bot = TeleBot('5441210926:AAEIEO-xBalcs5XlUZD1gOVKav3HbdqjlTo')




# Название класса обязательно - "Command"
class Command(BaseCommand):
  
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
      # @bot.message_handler(commands=['help', 'start'])
      # def send_welcome(message):
      #     bot.reply_to(message, "3ch support bot")
      pass
      
      
        

