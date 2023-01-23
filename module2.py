from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
import re
import os
import random
from time import sleep
import time
import pyautogui as pg







import yt_download as yt
import config 

def random_id():
    return random.randint(0, 1000000)

def random_d():
    return random.choice(prank)


bot = Bot(config.TOKEN)
URL = "https://painmo.herokuapp.com/"
dp = Dispatcher(bot)
   

prank = ["kill @e", "Kick SweetDree", "kick MechanicCamp327"]

@dp.message_handler(commands=['startserver'])
async def process_he_command(message: types.Message):
    pg.typewrite(["winleft"])
    pg.typewrite("chrome\n")
    pg.typewrite(["enter"])
    time.sleep(2)
    pg.typewrite("https://aternos.org/server/")
    time.sleep(0.5)
    pg.typewrite(["enter"])
    time.sleep(2)
    pg.click(x=930, y=593)
    time.sleep(2)
    print("Сервер запущен!")


@dp.message_handler(commands=['t'])
async def process_help_command(message: types.Message):
    pg.click(x=224, y=376)
    pg.click(x=381, y=927)
    time.sleep(1)
    pg.typewrite(random_d())
    pg.typewrite(["enter"])



'''
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    


@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):   

'''





