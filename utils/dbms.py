from bot import db

async def add_album(name):
    try:
        await db.pool.execute(f'''INSERT INTO albums(name) VALUES ($1)''', name)
        return True
    except Exception as e:
        print(e)

async def add_photo(album, photo, date):
    try:
        await db.pool.execute(f'''INSERT INTO photoportfolio(album, photo, date) VALUES ($1, $2, $3)''', album, photo, date)
        return True
    except Exception as e:
        print(f'''Ошибка добавления фото {e}''')

async def get_all_album():
    try:
        all_albums = await db.pool.fetch(f'''SELECT * FROM albums''')
        return all_albums
    except:
        print('Ошибка вывода всех альбомов')

async def get_all_photos():
    try:
        all_photos = await db.pool.fetch(f'''SELECT * FROM photoportfolio''')
        return all_photos
    except:
        print('Ошибка вывода всех фото')

async def get_photo_by_album(album):
    try:
        photo = await db.pool.fetch(f'''SELECT * FROM photoportfolio WHERE album={album}''')
        return photo
    except Exception as e:
        print(f'''Ошибка вывода фото по альбому {e}''')

async def add_user(tg_id, username, name, registration_date):
    try:
        default_role = 'user'
        await db.pool.execute(f'''INSERT INTO p_users(tg_id, username, name, registration_date, role) VALUES ($1, $2, $3, $4, $5)''', tg_id, username, name, registration_date, default_role)
    except:
        print('Ошибка добавления юзера')

async def get_user(tg_id):
    try:
        user = await db.pool.fetchrow(f'''SELECT * FROM p_users WHERE tg_id={tg_id}''')
        return user
    except:
        print('Юзер не зарегестрирован')


async def get_all_users():
    try:
        users = await db.pool.fetch(f'''SELECT * FROM p_users''')
        return users
    except Exception as e:
        print(f'''Юзер не зарегестрирован {e}''')

async def edit_album(album_id, newname):
    try:
        await db.pool.execute(f'''UPDATE albums SET name='{newname}' WHERE id='{album_id}' ''')
        return True
    except Exception as e:
        print(e)
        return False

async def del_album(album_id):
    try:
        await db.pool.execute(f'''DELETE FROM albums WHERE id='{album_id}' ''')
        await db.pool.execute(f'''DELETE FROM photoportfolio WHERE album='{album_id}' ''')
        return True
    except Exception as e:
        print(e)
        return False

