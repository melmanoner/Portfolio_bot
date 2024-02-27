from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.dbms import get_all_album

cancel_btn = InlineKeyboardButton('Отмена', callback_data='cancel')
cancel_btn = InlineKeyboardMarkup.add(cancel_btn)

async def get_albums_kb():
    all_albums = await get_all_album()
    all_albums_kb = InlineKeyboardMarkup()
    for album in all_albums:
        btn = InlineKeyboardButton(f'''{album[1]}''', callback_data=f'''album_{album[0]}''')
        all_albums_kb.add(btn)
    all_albums_kb.add(cancel_btn)
    return all_albums_kb