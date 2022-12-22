# importing libs
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
from DataBase_Wrapper import DB

# initializing database
db = DB()

# adding our keyboards
kb = ReplyKeyboardMarkup(resize_keyboard=True)
books = ReplyKeyboardMarkup(resize_keyboard=True)
search_kb = ReplyKeyboardMarkup(resize_keyboard=True)

# buttons for our keyboards
button_1 = KeyboardButton("/help")
button_2 = KeyboardButton("/all_books")
button_3 = KeyboardButton("/search_for_name")
button_left = KeyboardButton("/page_back")
button_right = KeyboardButton("/page_forward")
find_button = KeyboardButton("/find")
exit_button = KeyboardButton("/exit")
# from variables constructing our keabord
kb.add(button_1).insert(button_2)
kb.add(button_3)
books.add(button_left).insert(button_right)
books.add(exit_button)
search_kb.add(find_button)
search_kb.add(exit_button)
# list of our help command
HELP_COMMAND = """  
/help - список команд
/all_books - вивід всіх книжок
/search_for_name - пошук книги по назві
"""

# initializing our bot 
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# initializing all database in one variable
all_database = db.return_all_database()

# function for start command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Добро пожаловать в наш Телеграмм бот!",
                            reply_markup=kb)

# function for help command
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)

# function for all_books command
@dp.message_handler(commands=['all_books'])
async def all_books_command(message: types.Message):
    i = 0
    while i <= 10:
        tel_message = (f"Book name: {all_database[i][1]}\nBook author: {all_database[i][2]}\nBook price: {all_database[i][4]}{all_database[i][7]}\n{all_database[i][8]}")
        i += 1
        await message.answer(text=tel_message,
                             reply_markup=books)

# function for page_back command
@dp.message_handler(commands=['page_back'])
async def page_back_command(message: types.Message):
    await message.answer(text="Page -10 books",
                         reply_markup=books)

# function for page_forward command
@dp.message_handler(commands=['page_forward'])
async def page_forward_command(message: types.Message):
        await message.answer(text="Page +10 books",
                         reply_markup=books)

# function for search_for_name command
@dp.message_handler(commands=['search_for_name'])
async def search_for_name_command(message: types.Message):
    await message.answer(text="Пошук книги по назві!", reply_markup=search_kb)

# function for search_for_name command
@dp.message_handler(commands=['exit'])
async def exit_command(message: types.Message):
    await message.answer(text="На головну сторінку", reply_markup=kb)

# starting our bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)