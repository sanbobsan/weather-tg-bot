
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Find_weather(StatesGroup):
    place = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет', reply_markup=kb.to_menu)

@router.message(F.text.lower() == 'меню')
async def cmd_menu(message: Message, state: FSMContext):
    await message.answer('Это меню, выберите что хотите)', reply_markup=kb.menu)
    await state.clear()

@router.message(F.text.lower() == 'узнать погоду')
async def find_weather(message: Message, state: FSMContext):
    await state.set_state(Find_weather.place)
    await message.answer('Выберите место', reply_markup=kb.to_menu)

@router.message(Find_weather.place)
async def place(message: Message, state: FSMContext):
    await state.update_data(place=message.text)
    data = await state.get_data()
    await message.answer(f'Ваше место: {data['place']}', reply_markup=kb.to_menu)
    await state.clear()
    

