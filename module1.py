from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from time import sleep
import time
import yt_download as yt
import config 



bot = Bot(config.TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):
    try:
        
        echo_download=yt.Downloader(message.text)
        await message.reply("Побачила, починаю закачку...")
        time.sleep(2)
        '''await message.reply("Генерирую id...")
        time.sleep(4)
        await message.reply(random_id())
        '''
        
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






