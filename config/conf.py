import psycopg2
import telebot
import os
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_TOKEN'))
conn = psycopg2.connect(dbname='buddy_coffee', user='postgres', password='', host='localhost')
