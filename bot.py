import requests
import sqlite3
import json
from telebot import *
import time
from time import sleep
import os
bot = telebot.TeleBot("8181801599:AAFI0g5XWxkyNp4Kii9lG49GwI1FXl4Kq5k")
@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,parse_mode='HTML',text = (f"<b>Hello -> </b><i>{message.from_user.first_name}</i> ðŸ˜€\n<b>USER ID -> </b><i>{message.from_user.id} ðŸ¤–</i>\n<b>TO CHECK MY MENU SEND -> </b><i>/cmds</i>"))
