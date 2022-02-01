import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWords import checkWord

API_TOKEN = '2113530155:AAG6E9Uf4hyIvZ8MTt6Uc_vEOM7ylmdvOyw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):

    await message.reply("Assalomu Alaykum So'z tekshirish botiga hush kelibsiz")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):

    await message.reply("Botdan foydalanish uchun so'z yuboring")


@dp.message_handler()
async def echo(message: types.Message):
    word=message.text
    result=checkWord(word)

    if result['available']:
        response = f" ☑{word.capitalize()} "
    else:
        response = f"✖{word.capitalize()}"
        for text in result['matches']:
            response+=f"so'z to'g'ri {word.capitalize()}\n"

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)