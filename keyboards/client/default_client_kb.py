from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_me_btn = KeyboardButton('Обо мне')
portfolio_btn = KeyboardButton('Моё портфолио')
appointment_btn = KeyboardButton('Запись')
contact_btn = KeyboardButton('Мои контакты')

client_kb = ReplyKeyboardMarkup()
client_kb.add(about_me_btn)
client_kb.add(portfolio_btn)
client_kb.add(appointment_btn)
client_kb.add(contact_btn)