from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from utils.db import Database

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage)
loop = asyncio.get_event_loop()
db = Database(loop)