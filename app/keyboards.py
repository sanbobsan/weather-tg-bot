
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

to_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Меню')]],
                           resize_keyboard = True,)

menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Узнать погоду')]],
                           resize_keyboard = True,)

choose_weather = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Погода на сегодня'),
                                                KeyboardButton(text='Погода на вчера'),
                                                KeyboardButton(text='Погода на неделю')]],
                                                resize_keyboard = True,)