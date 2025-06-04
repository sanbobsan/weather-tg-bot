
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='7548618565:AAGA7z5My06S6egY9EcLT6dTIrdnxdCgCwM')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Бот запущен')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

