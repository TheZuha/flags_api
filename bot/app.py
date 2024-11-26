from aiogram import Dispatcher, Bot, types, executor
from keyboards import flags_button
import requests

TOKEN = '7064960495:AAHXuiUWiG4UTCdXuH6iR5gxist8vDevpXM'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

flags = requests.get('http://127.0.0.1:8000/api/').json()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hello' ,reply_markup=flags_button)

@dp.message_handler()
async def flag(message: types.Message):
    davlat = message.text
    bayroq_url = ""

    for flag in flags:
        if davlat == flag['country_name']:
            bayroq_url = flag['image']
            bayroq_url = bayroq_url[21:]


    try:
        bayroq = types.InputFile(f"..{bayroq_url}")
        await message.answer_photo(photo=bayroq, caption=davlat)
    except Exception as e:
        await message.reply(f"Rasmni yuborishda xatolik yuz berdi: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)