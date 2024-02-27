from bot import db
from asyncpg.exceptions import DuplicateTableError

async def create_table_albums():
    sql = 'CREATE TABLE albums(id serial PRIMARY KEY, name text)'
    await db.pool.execute(sql)

async def create_table_photoportfolio():
    sql = 'CREATE TABLE photoportfolio(id serial PRIMARY KEY,album text, photo text, date text)'
    await db.pool.execute(sql)


async def run():
    try:
        await create_table_photoportfolio()
        await create_table_albums()
    except DuplicateTableError as e:
        print(e)