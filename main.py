import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

bot = Bot(token='7548618565:AAGA7z5My06S6egY9EcLT6dTIrdnxdCgCwM')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет')

@dp.message(Command('locality'))
async def cmd_start(message: Message):
    await message.answer('выберите населенный пункт')

async def main():
    await dp.start_polling(bot)
    print('Бот запущен')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

