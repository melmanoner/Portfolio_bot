from bot import db
from asyncpg.exceptions import DuplicateTableError

async def create_table_users():
    sql = 'CREATE TABLE p_users(id serial PRIMARY KEY, tg_id bigint, username text, name text, registration_date text, role text)'
    try:
        await db.pool.execute(sql)
    except:
        print('Ошибка создания таблицы users')

async def create_table_albums():
    sql = 'CREATE TABLE albums(id serial PRIMARY KEY, name text)'
    try:
        await db.pool.execute(sql)
    except:
        print('Ошибка создания таблицы albums')

async def create_table_photoportfolio():
    sql = 'CREATE TABLE photoportfolio(id serial PRIMARY KEY,album integer, photo text, date text)'
    try:
        await db.pool.execute(sql)
    except Exception as e:
        print(f'''Ошибка создания таблицы photoportfolio {e}''')
        return False


async def run():
    try:
        await create_table_users()
        await create_table_photoportfolio()
        await create_table_albums()
    except DuplicateTableError as e:
        print(e)