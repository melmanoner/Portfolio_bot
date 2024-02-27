from bot import db

async def add_album(name):
    try:
        await db.pool.exectute(f'''INSERT INTO albums(name) VALUES ($1)''', name)
    except:
        print('Ошибка создания альбома')

async def add_photo(album, photo, date):
    try:
        await db.pool.exectute(f'''INSERT INTO photoportfolio(album, photo, date) VALUES ($1, $2, $3)''', album, photo, date)
    except:
        print('Ошибка добавления фото')

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
    except:
        print('Ошибка вывода фото по альбому ')

async def add_user(tg_id, username, name, registration_date):
    #try:
    default_role = 'user'
    await db.pool.exectute(f'''INSERT INTO users(tg_id, username, name, registration_date, role) VALUES ($1, $2, $3, $4, $5)''', tg_id, username, name, registration_date, default_role)
    #except:
    #    print('Ошибка добавления юзера')

async def get_user(tg_id):
    #try:
    user = await db.pool.fetchrow(f'''SELECT * FROM users WHERE tg_id={tg_id}''')
    return user
    #except:
    #    print('Юзер не зарегестрирован')


