import os
import random
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# 1. Настройки
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 2. Список предсказаний
predictions = [
    "Не сегодня, приляг",
    "Да, действуй!",
    "Кофе поможет тебе",
    "Передохни 10 мин",
    "О нет, я тебе не помощник",
    "Магия уже действует!",
]


# 3. Клавиатура
def get_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Узнать судьбу!"))
    return builder.as_markup(resize_keyboard=True)


# 4. Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\nНажми на кнопку, чтобы погадать!",
        reply_markup=get_keyboard(),
    )


# 5. Обработчик кнопки гадания
@dp.message(F.text == "Узнать судьбу!")
async def send_prediction(message: types.Message):
    prediction = random.choice(predictions)
    await message.answer(f"🔮 Твое предсказание: {prediction}")


# 6. Запуск бота
async def main():
    print("🔮 Бот-гадалка запущен и готов предсказывать! (Февраль 2026)")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот выключен")
