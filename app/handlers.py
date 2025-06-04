
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет', reply_markup=kb.to_menu)

@router.message(F.text.lower() == 'меню')
async def cmd_start(message: Message):
    await message.answer('Это меню, выберите что хотите)', reply_markup=kb.menu)

@router.message(F.text.lower() == 'ввести место')
async def cmd_start(message: Message):
    await message.answer('Выберите место', reply_markup=kb.menu)


