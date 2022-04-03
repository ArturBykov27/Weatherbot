import requests
import time
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5119795533:AAH7Q7lA7k_jK0982eUAEo5LDwY5qAEQVFA'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Теперь буду показывать вам погоду на сейчас. Слава Украине!")
params = {
    'appid':'f7740806204884a7c51613d937c21ae4',
    'units': 'metric',
    'q' : 'Dnipro',
    'lang' : 'ru'
}
wth = requests.get('https://api.openweathermap.org/data/2.5/weather',params)
result = wth.json()
lon = result['coord']['lon']
tempnow = int(result['main']['temp'])
a = ['погода','Погода','Погоде','погоде','погоду','Погоду']
if tempnow >=0:#подставляет градусов тепла/мороза
    tempword = '°С тепла'
else:
    tempword = '°С мороза'
tempmin = str (result['main']['temp_min'])
tempmax = str (result['main']['temp_max'])
windspd = result['wind']['speed']
if windspd >= 5:
    windrec = 'Лучше накинь капюшон'
else:
    windrec = 'Тебя не сдует.'
city = str(result['name'])
#date = str(result['dt'])
time=time.ctime()
@dp.message_handler()
async def send_weather(message: types.Message):
    for a1 in a:
        if a1 in message.text:
            await message.answer('Привет! \nСегодня ' +str(time)+' \nВ '+ city + 'е сейчас '+ str(tempnow)+tempword+'.\n'
                             +'Минимальная температура сегодня — ' + tempmin + '. Максимум — ' + tempmax + '.\n'+
                             'Скорость ветра — '+ str(windspd) +'м/с. ' + windrec + ".\n"+
                             "Всё давай, хорошего дня)")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


