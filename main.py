
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('!!! Бот запущен !!!')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('!!! Бот выключен !!!')
    except Exception as e:
        print(f"!!! Ошибка !!! \n{e}")

