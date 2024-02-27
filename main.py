from bot import dp, bot
from aiogram.utils import executor
from config import BOT_ADMIN
from utils import create_tables


async def bot_start(_):
    await create_tables.run()
    bot_info = await bot.get_me()
    await bot.send_message(BOT_ADMIN, f'''Бот {bot_info['first_name']} запущен!▶''')

async def bot_stop(_):
    bot_info = await bot.get_me()
    await bot.send_message(BOT_ADMIN, f'''Бот {bot_info['first_name']} остановлен!🛑''')


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start, on_shutdown=bot_stop)
