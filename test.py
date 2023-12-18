#
#
#
# import requests
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
#
# API_TOKEN = '6572410065:AAEJb7XbS04YrCSHC6fawvodaF0SK1k7WBE'
# OPENEXCHANGERATES_API_KEY = '0fafdc003588203731efbad6a5e11e8f'
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# def get_exchange_rate(base_currency, target_currency):
#     url = f'https://data.fixer.io/api/latest/{base_currency}?apikey={OPENEXCHANGERATES_API_KEY}'
#     response = requests.get(url)
#     data = response.json()
#     if 'error' in data:
#         return None
#     rate = data['rates'].get(target_currency)
#     return rate
#
# @dp.message_handler(commands=['get_rate'])
# async def get_rate(message: types.Message):
#     base_currency = 'USD'  # Asosiy valyuta (masalan, AQSh dollari)
#     target_currency = 'UZS'  # O'zbekiston so'mi
#
#     rate = get_exchange_rate(base_currency, target_currency)
#
#     if rate is not None:
#         await message.reply(f"Hozirgi vaqtdagi kurs: 1 {base_currency} = {rate} {target_currency}")
#     else:
#         await message.reply("Kurs olishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '6572410065:AAEJb7XbS04YrCSHC6fawvodaF0SK1k7WBE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# OpenWeatherMap API ma'lumotlari
OWM_API_KEY = '9fc4456aae1a6dfedc30da229ebb48a6'

# Viloyat nomlarini va kodlarini saqlash uchun lug'at
viloyatlar = {
    'Toshkent': 'Tashkent',
    'Namangan': 'Namangan',
    'Andijon': 'Andijan',
    # Qo'shimcha viloyatlar...
}


def get_weather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': OWM_API_KEY,
        'units': 'metric',  # Metric tizimda olish
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

@dp.message_handler(commands=['weather'])
async def get_weather_command(message: types.Message):
    # /weather komandasiga javob
    command_parts = message.text.split(' ', 1)
    if len(command_parts) == 2:
        city_name = command_parts[1]
        if city_name in viloyatlar:
            city_name = viloyatlar[city_name]

        weather_data = get_weather(city_name)

        print("Weather data:", weather_data)  # Qo'shimcha: ma'lumotlarni ekranga chiqaring

        if 'main' in weather_data and 'temp' in weather_data['main']:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            response_text = f"Hozirgi ob-havo: {description.capitalize()}\nTemperature: {temperature}°C"
            await message.reply(response_text)
        else:
            await message.reply("Ob-havo ma'lumotlari topilmadi.")
    else:
        await message.reply("Iltimos, viloyat nomini kiritishni unutmang, masalan: /weather Toshkent")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
