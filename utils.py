from aiogram.dispatcher.filters.state import State, StatesGroup

class MenuState(StatesGroup):
    menu_btn_1 = State()
    menu_btn_2 = State()
    photo = State()
    wincode = State()
    menu_btn_4 = State()
    full_name_driver = State()
    license_car = State()
    phone_number = State()

if __name__ == '__main__':
    print(MenuState.all())