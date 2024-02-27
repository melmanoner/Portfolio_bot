import asyncio
import asyncpg
from config import DB_USER, DB_NAME, DB_PASSWORD

class Database:
    def __init__(self, loop:asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database = DB_NAME,
                user = DB_USER,
                password = DB_PASSWORD,
                host = '127.0.0.1',
                port = '5432',
            )
        )