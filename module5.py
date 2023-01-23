import schedule
from aiogram.utils.emoji import emoji
import os 
import pyautogui as pg
import aiogram
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from sqlighter import SQLighter
from time import sleep
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton  



bot = Bot(token="2056524233:AAHpJ8L4lzRVobBLvo63aR6AV309_MwPko8")
dp = Dispatcher(bot)
db = SQLighter('db.db')


async def commands_start(message: types.message):
    await message.reply("Привіт")   

def greeting():
    """Greeting function"""
    
    todos_dict = {
        '08:00': 'Drink coffee',
        '11:00': 'Work meeting',
        '23:59': 'Hack the Planet!'
    }
    
    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')
        

    

schedule.every().day.at('01:25').do(greeting)

    
  
while True:
    schedule.run_pending()
    break







        

    


if __name__ == '__main__':
    print("Оно живое !!!")
    executor.start_polling(dp, skip_updates=True)
    
 
