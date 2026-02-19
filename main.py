import asyncio
from asyncio import CancelledError

from aiogram import Bot, Dispatcher

from bot.handlers import router
from config import config
from in_terminal import start_in_terminal


async def start_bot() -> None:
    try:
        print("!!! Бот запущен !!!")
        bot = Bot(token=config.TOKEN)
        dp = Dispatcher()
        dp.include_router(router)
        await dp.start_polling(bot)

    except (KeyboardInterrupt, CancelledError):
        print("!!! Бот выключен !!!")

    except Exception as e:
        print(f"!!! Ошибка !!! \n{e}")


def main() -> None:
    if not config.RUN_IN_TERMINAL:
        asyncio.run(start_bot())
    else:
        asyncio.run(start_in_terminal())


if __name__ == "__main__":
    main()
