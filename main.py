import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1. Функция для создания Главного Меню (Reply-кнопки)
def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="📁 Мои проекты"))
    builder.add(types.KeyboardButton(text="🛠 Мой стек"))
    builder.add(types.KeyboardButton(text="🐧 Обо мне"))
    return builder.as_markup(resize_keyboard=True)

# 2. Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет! Рад видеть тебя здесь. Я — бот-визитка начинающего Python-разработчика.\n\n"
        f"Используй меню ниже, чтобы узнать обо мне больше! 👇",
        reply_markup=get_main_menu()
    )

# 3. Обработчик кнопки "📁 Мои проекты"
@dp.message(F.text == "📁 Мои проекты")
async def show_projects(message: types.Message):
    inline_builder = InlineKeyboardBuilder()
    inline_builder.add(types.InlineKeyboardButton(
        text="🌐 Открыть мой GitHub", 
        url="https://github.com/buslikbus-cmd"
    ))
    
    await message.answer(
        "🚀 **Мои проекты:**\n\n"
        "1. **Этот самый бот-визитка** — написан на Python 3 с использованием асинхронного фреймворка aiogram 3. Работает на ОС Arch Linux, скрывает секреты через `.env` и бережно хранится в Git.\n\n"
        "Все исходники и новые эксперименты я выкладываю в свой профиль:",
        reply_markup=inline_builder.as_markup()
    )

# 4. Обработчик кнопки "🛠 Мой стек"
@dp.message(F.text == "🛠 Мой стек")
async def show_stack(message: types.Message):
    await message.answer(
        "🛠 **Технологии, которые я использую:**\n\n"
        "• **Язык:** Python 3 (Пишу чистый асинхронный код)\n"
        "• **Библиотеки:** aiogram 3, python-dotenv\n"
        "• **Инструменты:** Git, VS Code\n"
        "• **Окружение:** Arch Linux 🐧 (минимализм и полный контроль)"
    )

# 5. Обработчик кнопки "🐧 Обо мне"
@dp.message(F.text == "🐧 Обо мне")
async def show_about(message: types.Message):
    await message.answer(
        "👋 **Пара слов обо мне:**\n\n"
        "Я изучаю программирование, автоматизирую рутину и создаю полезные инструменты.\n"
        "Не боюсь терминала, собираю окружение руками в Arch Linux и стремлюсь писать красивый, оптимизированный код.\n\n"
        "Спасибо, что заглянул в моего бота! Задавай любые вопросы прямо сюда."
    )

# Запуск опроса
async def main():
    print("Бот-визитка успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
