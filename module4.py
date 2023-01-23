from email import message
from sqlite3 import dbapi2
from traceback import print_tb
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
import re
import os 
from sql import SQLighter
from time import sleep
import yt_download as yt
import config 
import time 
import random
import pyautogui as pg
'''***********************************************Фунции***************************************************************'''








'''***********************************************Конвази*************************************************************'''





bot = Bot(token="2056524233:AAHpJ8L4lzRVobBLvo63aR6AV309_MwPko8")
dp = Dispatcher(bot)
db = SQLighter('bd.db')

# инициализируем соединение с БД

'''**************************************Админская часть****************************************************'''




sube = db.get_subscriptions() 



@dp.message_handler(commands=['s'])
async def subscribe(message: types.Message):
    await bot.send_message(995077290, sube)





'''*****************************Клиенская часть***************************************'''

@dp.message_handler(commands=['dr'])
async def functiscreen(message: types.Message):
  await bot.send_message(177061121, "Дивитесь футбол ?")
  






@dp.message_handler(commands=['screen'])
async def functiscreen(message: types.Message):
    im4 = pg.screenshot('my_screenshot.png')    
    await message.reply("Відправляю..")
    await message.reply_document(open('my_screenshot.png', 'rb'))









	
	
@dp.message_handler(commands=['start'])
async def commands_start(message: types.message):
    
    
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, True)
	

    


	await message.reply("Привіт я багато функціональний телеграм бот\n Та звати мене Паймон")    
    



@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):
    await bot.send_message(995077290, message.text)  
    print(message.text)
    '''
    
    
    try:
        
        echo_download=yt.Downloader(message.text)
        await message.reply("Побачила, починаю закачку...")        
        videonote = open(echo_download.download_video(), 'rb')
     
    except:
        await message.reply("На жаль, сталася помилка... Перевірте правильність посилання")
        print('Error :(')
        return
    await message.reply("Готово, видео зкачено на сервер.\nВідправляю...",)
    try:
        await bot.send_document(message.from_user.id, videonote)
    except:
        await bot.send_message(message.from_user.id, "На жаль, сталася помилка...")
    finally:
        videonote.close()





'''
if __name__ == '__main__':
    print("Оно живое !!!")
    executor.start_polling(dp, skip_updates=True)

