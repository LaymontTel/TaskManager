from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Создаем экземпляры бота и диспетчера
bot = Bot(token="6228916578:AAGH0nF6U9RX-egPePLpzer8RPfe126Yfxk")
dp = Dispatcher(bot)

# Обработчик команды /mono
@dp.message_handler(commands=['mono'])
async def send_mono_text(message: types.Message):
    mono_text = "<code>Моноширинный текст</code>"

    await message.reply(mono_text, parse_mode='HTML')

print('work')

if __name__ == '__main__':
    executor.start_polling(dp)
