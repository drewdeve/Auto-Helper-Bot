import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from config import BOT_TOKEN, group_id_evacuator, group_id_payment, result
import keyboards as kb
from googleWorker import *
from utils import MenuState

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}! Напишите /menu, чтобы открыть его.'.format(message.from_user))

@dp.callback_query_handler(text='cancel_btn')   
async def process_callback_cancel(call: types.CallbackQuery):
    await call.message.answer('Вы вернулись назад в меню ↩️', reply_markup=kb.mainMenu)

@dp.message_handler(commands=['menu'])
async def process_menu_command(message: types.Message):
    await message.answer('📝 Вы открыли меню, выберите, что-то одно: ', reply_markup=kb.mainMenu)  
    
@dp.callback_query_handler(text='menu_btn_1')
async def process_callback_menu_1(call: types.CallbackQuery):
    await MenuState.menu_btn_1.set()
    await call.message.answer(kb.text_firtst_btn, reply_markup=kb.cancelMenu)

@dp.message_handler(state=MenuState.menu_btn_1)
async def process_menu_btn_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        i = 1
        for table in tables:
            i += 1
            try:
                row = table.find(message.text)
                table.row_values(row.row)
                msg = f'''
                - {table.row_values(row.row)[2]}
- {table.row_values(row.row)[5]}
- {table.row_values(row.row)[10]}
- {table.row_values(row.row)[6]}
- {table.row_values(row.row)[8]}
- {table.row_values(row.row)[1]}
                '''
                await message.answer(msg, reply_markup=kb.cancelMenu)
                break     
            except:
                continue                
        if i == 21:
            await message.answer('Извините, такого номера нету. Попробуйте, ещё раз!', reply_markup=kb.cancelMenu)          
    await state.finish()

@dp.callback_query_handler(text='menu_btn_2')
async def process_callback_menu_2(call: types.CallbackQuery):
    await MenuState.menu_btn_2.set()
    await call.message.answer(kb.text_second_btn, reply_markup=kb.cancelMenu)

@dp.message_handler(state=MenuState.menu_btn_2)
async def process_menu_btn_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        try:
            row = baza_table.find(message.text)
            baza_table.row_values(row.row)
            msg = f'''
            - {baza_table.row_values(row.row)[5]}
- {baza_table.row_values(row.row)[6]}
- {baza_table.row_values(row.row)[7]}
- {baza_table.row_values(row.row)[16]}
            '''
            await message.answer(msg, reply_markup=kb.cancelMenu)
        except:
            await message.answer('Извините, такого номера нету. Попробуйте, ещё раз!', reply_markup=kb.cancelMenu)  
    await state.finish()

@dp.callback_query_handler(text='menu_btn_3')
async def process_callback_menu_3(call: types.CallbackQuery):
    await call.message.answer(kb.text_third_btn, reply_markup=kb.menu_btn_wincode)

@dp.callback_query_handler(text='wincode_btn')
async def process_callback_wincode_btn(call: types.CallbackQuery):
    await MenuState.wincode.set()
    await call.message.answer('Пришлите винкод авто для идентификации.', reply_markup=kb.cancelMenu)

@dp.message_handler(state=MenuState.wincode)
async def process_menu_btn_wincode(message: types.Message, state: FSMContext):
    global wincode
    async with state.proxy() as data:
        data['text'] = message.text
        wincode = message.text
        await message.answer('Дальше пришлите фото.', reply_markup=kb.menu_btn_photo)
    await state.finish()  

@dp.callback_query_handler(text='photo_btn')
async def process_callback_photo_btn(call: types.CallbackQuery):
    await MenuState.photo.set()
    await call.message.answer('Пришлите фото.', reply_markup=kb.cancelMenu)

@dp.message_handler(content_types=['photo'], state=MenuState.photo)
async def process_menu_btn_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await bot.send_photo(group_id_payment, photo_id, caption=wincode)
   
    await message.answer('Спасибо, мы рассматриваем Вашу заявку.', reply_markup=kb.mainMenu)
    await state.finish()

@dp.callback_query_handler(text='menu_btn_4')
async def process_callback_menu_4(call: types.CallbackQuery):
    await call.message.answer(kb.text_fourth_btn, reply_markup=kb.menu_btn_driver)

@dp.callback_query_handler(text='full_name_driver_btn')
async def process_callback_driver_btn(call: types.CallbackQuery):
    await MenuState.full_name_driver.set()  
    await call.message.answer(kb.text_about_driver, reply_markup=kb.cancelMenu)

@dp.message_handler(state=MenuState.full_name_driver)
async def process_menu_btn_driver(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        full_name_driver = message.text
        result.append(full_name_driver)
        await message.answer('Дальше введите гос номер эвакуатора: машина / прицеп.', reply_markup=kb.menu_btn_license) 
    await state.finish()    

@dp.callback_query_handler(text='license_car_btn')
async def process_callback_driver_btn(call: types.CallbackQuery):
    await MenuState.license_car.set()  
    await call.message.answer(kb.text_about_license, reply_markup=kb.cancelMenu)

@dp.message_handler(state=MenuState.license_car)
async def process_menu_btn_license(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        license_car = message.text
        result.append(license_car)
        await message.answer('Дальше введите телефон водителя.', reply_markup=kb.menu_btn_phone) 
    await state.finish()    

@dp.callback_query_handler(text='phone_number_btn')
async def process_callback_driver_btn(call: types.CallbackQuery):
    await MenuState.phone_number.set()  
    await call.message.answer(kb.text_about_phone, reply_markup=kb.cancelMenu)    

@dp.message_handler(state=MenuState.phone_number)
async def process_menu_btn_driver(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        phone_number = message.text
        result.append(phone_number)
        await message.answer('Спасибо, мы рассматриваем Вашу заявку.', reply_markup=kb.mainMenu) 
    await state.finish()            
    
    msg = f'''
    - {result[0]}
- {result[1]}
- {result[2]}
    '''
    await bot.send_message(group_id_evacuator, msg) 
    result.clear()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)