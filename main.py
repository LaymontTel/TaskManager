import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import filters
from aiogram import executor
import random
import string

API_TOKEN = '6228916578:AAGH0nF6U9RX-egPePLpzer8RPfe126Yfxk'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Для регистрации нажми на кнопку ниже:", reply_markup=create_inline_keyboard())


def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")
    keyboard.add(button)
    return keyboard


def is_button_pressed(callback_query: types.CallbackQuery):
    return callback_query.data == 'button_pressed'


@dp.callback_query_handler(is_button_pressed)
async def button_pressed_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer("Аккаунт создан")

    def generate_random_code(length):
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code


    code_id = generate_random_code(46)
    mono_text = f"<code>{code_id}c</code>"
    await bot.send_message(callback_query.message.chat.id, f"Спасибо за регистрацию, ваш id для авторизации - {mono_text}", parse_mode='HTML')

print("work")

if __name__ == '__main__':
    dp.register_message_handler(start, Command("start"))
    dp.register_callback_query_handler(button_pressed_callback)
    executor.start_polling(dp, skip_updates=True)
