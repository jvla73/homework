from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# записываем ключ
api = 'YOUR_KEY'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# обработка сообщений хендлеры
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Твой возраст')
    await UserState.age.set()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button1 = KeyboardButton(text = 'Информация')
#добавляем в клавиатуру
kb.add(button)
kb.add(button1)

menu = InlineKeyboardMarkup()
button2 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button3 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
menu.add(button2)
menu.add(button3)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выбери опцию', reply_markup=menu)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Расчёт по формуле: 10 * вес в кг + 6,25 * рост в см – (5 * возраст в г – 161)')
    await call.answer()

@dp.message_handler(commands = ['start'])
async def Start_message(message):
    #reply_markup=kb показываем клавиатуру
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=kb)

#обрабатываем кнопку
@dp.message_handler(text = 'Рассчитать')
async def inform(message):
    await message.answer('Рассчитать')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Твой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Твой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    value_data = (v for v in data.values())
    value_list = []
    for v in value_data:
        value_list.append(round(float(v),2))
    norma = 10 * value_list[2] + 6.25 * value_list[1] - (5 * value_list[0] - 161)
    await message.answer(f'Твоя норма калорий {norma}')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)