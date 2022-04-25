from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

menu_btn_1 = InlineKeyboardButton('Статус контейнера 🏗', callback_data='menu_btn_1')
menu_btn_2 = InlineKeyboardButton('Статус авто 🚘', callback_data='menu_btn_2')
menu_btn_3 = InlineKeyboardButton('Загрузить платежку 💰', callback_data='menu_btn_3')
menu_btn_4 = InlineKeyboardButton('Загрузить данные эвакуатора 🚛', callback_data='menu_btn_4')
cancel_btn = InlineKeyboardButton('Назад ↩️', callback_data='cancel_btn')
full_name_driver_btn = InlineKeyboardButton('ФИО водителя 👨‍💼', callback_data='full_name_driver_btn')
license_car_btn = InlineKeyboardButton('Гос. номер эвакуатора: машина / прицеп 🔎', callback_data='license_car_btn')
phone_number_btn = InlineKeyboardButton('Телефон водителя 📱', callback_data='phone_number_btn')
photo_btn = InlineKeyboardButton('Фото 🖼', callback_data='photo_btn')
wincode_btn = InlineKeyboardButton('Винкод авто 💾', callback_data='wincode_btn')


mainMenu = InlineKeyboardMarkup(row_width=2).row(
    menu_btn_1, menu_btn_2).row(menu_btn_3, menu_btn_4)

cancelMenu = InlineKeyboardMarkup().add(cancel_btn)

# menu_btn_4Menu = InlineKeyboardMarkup(row_width=2).row(full_name_driver_btn, license_car_btn, phone_number_btn).row(cancel_btn)
menu_btn_driver = InlineKeyboardMarkup(row_width=2).row(full_name_driver_btn).row(cancel_btn)
menu_btn_license = InlineKeyboardMarkup(row_width=2).row(license_car_btn).row(cancel_btn)
menu_btn_phone = InlineKeyboardMarkup(row_width=2).row(phone_number_btn).row(cancel_btn)

# menu_btn_3Menu = InlineKeyboardMarkup(row_width=2).row(wincode_btn, photo_btn).row(cancel_btn)
menu_btn_wincode = InlineKeyboardMarkup(row_width=2).row(wincode_btn).row(cancel_btn)
menu_btn_photo = InlineKeyboardMarkup(row_width=2).row(photo_btn).row(cancel_btn)

text_firtst_btn = '''
Пришлите, номер контейнера.
Данные на выходе:
- номер контейнера (C)
- линия (I)
- судно (N)
- дата прихода конт. (J)
- дата передачи документов в порт (L)
- дата открытия  (B) 
'''

text_second_btn = '''
Пришлите, винкод автомобиля.
Данные на выходе:
- контейнер (F)
- марка авто (G)
- винкод автомобиля (H) 
- дата оформления гтд (Q)
'''

text_third_btn = '''
Загрузите изображение + винкод авто для идентификации.
'''

text_fourth_btn = '''
Подайте данные на эвакуатор, который нужно забирать.
Указать дату.

- ФИО водителя 
- гос номер эвакуатора: машина / прицеп
- телефон водителя  
'''

text_about_driver = '''
Напишите, Ваши данные:

- ФИО водителя
'''

text_about_license = '''
Напишите, Ваш гос номер:

- гос номер эвакуатора: машина / прицеп
'''

text_about_phone = '''
Напишите, Ваш номер телефона:

- телефон водителя
'''