from aiogram.utils.emoji import emoji
import os 
import pyautogui as pg
import aiogram
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import yt_download as yt 
import config 
from sqlighter import SQLighter
from time import sleep
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton  
from pyfiglet import Figlet
from aiogram.utils.emoji import emoji
import requests
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import folium
import aiogram
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from urllib.request import urlopen
from dataclasses import dataclass
import time
import pyautogui as pg
from aiogram.dispatcher.filters import Text
bot = Bot(token="2056524233:AAHpJ8L4lzRVobBLvo63aR6AV309_MwPko8")
dp = Dispatcher(bot)
db = SQLighter('db.db')

sube = db.get_subscriptions()
@dp.message_handler(commands=['s'])
async def subscribe(message: types.Message):
    await bot.send_message(995077290, sube)


@dp.message_handler(commands=['reset'])
async def functiscreen(message: types.Message):
    pg.click(x=1242, y=40)
@dp.message_handler(commands=['mute'])
async def functisd(message: types.Message):
    await message.reply("Ви включили або виключили мікрофон")
    pg.click(x=831, y=988)
@dp.message_handler(commands=['camera'])
async def functisa(message: types.Message):
    await message.reply("Ви включили або виключили камеру")
    pg.click(x=865, y=988)
    
@dp.message_handler(commands=['start'])
async def commands_start(message: types.message):
    
    kb =KeyboardButton("Bot ip")
    kb2 = KeyboardButton("YouTube donwload")
    kb3 = KeyboardButton("screanshoot")
    


    wda = ReplyKeyboardMarkup().add(kb).add(kb2).add(kb3)  	
    await message.reply("/f1 Пошук по ip /f2:Скачати відео з сайта  /f3:Зробити скриншот")   


@dp.message_handler(commands=["help"])
async def commands_help(message: types.message):
    await message.reply("Команди для гугл мита: \n /camera /mute скриншот екрана: /screen просмотр бази даних: ")

@dp.message_handler(commands=['next']) 
async def functisc(message: types.Message):
    for i in range(15): 
        #time.sleep(1)
        pg.click(x=693, y=571)
        pg.press('space')
        pg.press('down')
        pg.click(x=808, y=52)
        pg.hotkey('ctrl', 'c')
        pg.click(x= 663, y=1059)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')
        pg.click(x=376 , y=14)
"""""""""""""""""""""""""""""""""""""""""""""Скриншот""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""''"""
@dp.message_handler(commands=["f3"])
async def cmd_name(message: types.Message):
    await message.reply("Відправляю..")
    im1 = pg.screenshot('screenshot/screenshot.png')
    await message.reply_document(open('screenshot/screenshot.png', 'rb'))
"""""""""""""""""""""""""""""""""""""""""""""YouTube donwload"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@dp.message_handler(commands=["f2"])
async def cmd_name(message: types.Message):
    await bot.send_message(message.from_id,"Відправте силку на відео:")
    @dp.message_handler(content_types=['text'])
    async def echo_download_message(message: types.Message):

        lox2 = message.text
        print(lox2)
        
        try:
        



            echo_download=yt.Downloader(lox2)
            await message.reply("Побачила, починаю закачку...")         
            videonote = open(echo_download.download_video(), 'rb')
     
        except:
            await message.reply("На жаль, сталася помилка... Перевірте правильність посилання")
            print('Error :(')
            return
        await message.reply("Готово, видео зкачено на сервер.\nВідправляю...",)
        try:
            await bot.send_document(message.from_user.id, videonote)
         #await bot.send_message(message.from_user.id, "ok ")
        except:
            await bot.send_message(message.from_user.id, "На жаль, сталася помилка...")
            
        finally:
            videonote.close()
        return
"""""""""""""""""""""""""""""""""""""""""""""BOTIP""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""''"""
@dp.message_handler(commands=["f1"])
async def cmd_name(message: types.Message):
    await bot.send_message(message.from_id,"Скиньте ip:")
    @dp.message_handler(content_types=['text'])
    async def echo_download_message(message: types.Message):
        text = Figlet(font='slant')
        meme_text = Figlet(font='slant')

        print(text.renderText('BOT IP'))


        lox=message.text
        print(lox)
        ip = message.text
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
                    '[IP]': response.get('query'),
                    '                                                                                                '
        
                    '[Оператор]': response.get('isp'),
                    '                                                                                                '
        
                    '[Org]': response.get('org'),
                    '                                                                                                '
        
                    '[Страна]': response.get('country'),
                    '                                                                                                '
        
                    '[Область]': response.get('regionName'),
                    '                                                                                                '
        
                    '[Місто]': response.get('city'),
                    '                                                                                                            '
                    
                    '[Почтовий індекс]': response.get('zip'),           
                    '                                                                                                            '
                    
                    '[Ширина]': response.get('lat'),           
                    '                                                                                                            '
        
                    '[Довгота]': response.get('lon'),
                    }
        datacon = {
                    '[IP]': response.get('query'),
                    '[Оператор]': response.get('isp'),
                    '[Org]': response.get('org'),
                    '[Страна]': response.get('country'),
                    '[Область]': response.get('regionName'),
                    '[Місто]': response.get('city'),
                    '[Почтовий індекс]': response.get('zip'),           
                    '[Ширина]': response.get('lat'),                   
                    '[Довгота]': response.get('lon'),
                }
        for k, v in datacon.items():
            print(f'{k} : {v}')
    
    
        #await message.reply(data)
        await bot.send_message(message.from_user.id, '[IP]' + response.get('query') + "\n" +'[Оператор]' + response.get('isp') +'\n'+'[Org]'+ response.get('org')+'\n'+ '[Страна]'+ response.get('country')+'\n'+'[Область]'+ response.get('regionName')+'\n'+'[Місто]'+ response.get('city')+'\n'+'[Почтовий індекс]'+ response.get('zip')+'\n'+ '[Ширина]'+ str(response.get('lat'))+'\n'+ '[Довгота]'+ str(response.get('lon')))




        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'ip/map/{response.get("country")}_{response.get("city")}.html')
    

        i = response.get("country") +'_'+ response.get("city")
        print('Страна та город' +' ' + i)
    #await bot.send_message(message.from_user.id, "Місце положеня ip адреси на карті")
        lat = str(response.get('lat'))
        lot = str(response.get('lon'))
        await bot.send_location(message.from_user.id,lat ,lot)
    
    #await message.reply_document(open(f'{i}.html', 'rb'))

        return True


print("Оно живое !!!")
executor.start_polling(dp, skip_updates=True)