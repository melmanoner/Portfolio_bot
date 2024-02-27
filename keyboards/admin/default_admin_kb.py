from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add_album_btn = KeyboardButton('Создать альбом')
edit_album_btn = KeyboardButton('Редактировать альбом')
delete_album_btn = KeyboardButton('Удалить альбо')
add_photo_btn = KeyboardButton('Добавить фото')
delete_photo = KeyboardButton('Удалить фото')
clients_btn = KeyboardButton('Клавиатура клиента')

admin_kb = ReplyKeyboardMarkup()
admin_kb.add(add_album_btn, edit_album_btn, delete_album_btn)
admin_kb.add(add_photo_btn, delete_photo)
admin_kb.add(clients_btn)