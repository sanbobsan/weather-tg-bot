from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from bot import keyboards as kb
from bot.parser import build_weather_report

router = Router()


class Enter_location(StatesGroup):
    location = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("привет", reply_markup=kb.to_menu)


@router.message(F.text.lower() == "меню")
async def menu(message: Message, state: FSMContext):
    await message.answer("Это меню, выберите что хотите)", reply_markup=kb.menu)
    await state.clear()


@router.message(F.text.lower() == "узнать погоду")
async def find_weather(message: Message, state: FSMContext):
    await state.set_state(Enter_location.location)
    await message.answer("Выберите место", reply_markup=kb.to_menu)


@router.message(Enter_location.location)
async def weather(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    location = (await state.get_data())["location"]
    text = await build_weather_report(location)
    await state.clear()

    if not text:
        text = "❌ Ошибка, укажите правильное место"
        await state.set_state(Enter_location.location)
    await message.answer(text=text, reply_markup=kb.to_menu)
