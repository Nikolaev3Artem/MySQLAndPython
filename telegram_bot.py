from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
from DataBase_Wrapper import DB

db = DB()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton("/help")
button_2 = KeyboardButton("/all_books")
button_3 = KeyboardButton("/search_for_name")
kb.add(button_1).insert(button_2).insert(button_3)

HELP_COMMAND = """  
/help - список команд
/all_books - вивід всіх книжок
/search_for_name - пошук книги по назві
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Добро пожаловать в наш Телеграмм бот!",
                            reply_markup=kb)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)

@dp.message_handler(commands=['all_books'])
async def all_books_command(message: types.Message):
    all_database = db.return_all_database()
    i = 0
    while i <= 10:
        tel_message = (f"Book name: {all_database[i][1]}\nBook author: {all_database[i][2]}\nBook price: {all_database[i][4]}{all_database[i][7]}\n{all_database[i][8]}")
        i += 1
        await message.answer(text=tel_message)


@dp.message_handler(commands=['search_for_name'])
async def search_for_name_command(message: types.Message):
    await message.answer(text="Пошук книги по назві!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)