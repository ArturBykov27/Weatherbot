import datetime
import requests
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5234216216:AAHKIEW_U5kvmDLhT-e6pHpdJWTXPKbL4qs'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Теперь буду показывать вам погоду на сейчас. Слава Украине!")

@dp.message_handler()
async def weatherresponse(message):
    params = {
        'appid':'f7740806204884a7c51613d937c21ae4',
        'units': 'metric',
        'q' : 'Dnipro',
        'lang' : 'ru'
    }
    wth = requests.get('https://api.openweathermap.org/data/2.5/weather',params)
    result = wth.json()
    tempnow = (result['main']['temp'])
    a = ['погода','Погода','Погоде','погоде','погоду','Погоду','gjujlf','Gjujlf']
    if tempnow >=0:#подставляет градусов тепла/мороза
        tempword = '°С тепла'
    else:
        tempword = '°С мороза'

    windspd = result['wind']['speed']
    if windspd >= 5:
        windrec = 'Лучше накинь капюшон'
    else:
        windrec = 'Тебя не сдует.'
    city = str(result['name'])
    time=str(datetime.datetime.now().rfc822())
    for a1 in a:
        if a1 in message.text:
            await message.answer('Привет! \nСегодня ' +time+' \nВ '+ city + 'е сейчас '+ str(tempnow)+tempword+'.\n'+
                             'Скорость ветра — '+ str(windspd) +'м/с. ' + windrec + ".\n"+
                             "Всё давай, хорошего дня)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)