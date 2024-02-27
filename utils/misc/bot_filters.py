from utils.dbms import *
from config import BOT_ADMIN



async def is_admin(tg_id):
    if int(tg_id) == int(BOT_ADMIN):
        return True
    else:
        return False
