from aiogram import types, Dispatcher
from bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.admin.default_admin_kb import admin_kb
from keyboards.client.default_client_kb import client_kb
from utils.misc.bot_filters import is_admin
from utils.dbms import *


async def command_start(message:types.Message):
    tg_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name
    registration_date = str(message.date.date())
    check_user = await get_user(tg_id)
    if check_user == None:
        await add_user(tg_id, username, name, registration_date)
        await bot.send_message(tg_id, f'''Добро пожаловать!''', reply_markup=client_kb)
    elif await is_admin(tg_id):
        await bot.send_message(tg_id, f'''Админ, с возвращением''', reply_markup=admin_kb)
    else:
        await bot.send_message(tg_id, f'''🔸 С возвращением, {name}!🫂\n🔸 Бот готов к использованию.''', reply_markup=client_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')