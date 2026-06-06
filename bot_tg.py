import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛠 Услуги")],
            [KeyboardButton(text="💬 Связаться"), KeyboardButton(text="❓ Помощь")],
            [KeyboardButton(text="🔴 Не нажимать")],
        ],
        resize_keyboard=True
    )

    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\nЯ бот-помощник. Выбери что тебя интересует:",
        reply_markup=keyboard
    )

    await message.answer(
        caption=f"Привет, {message.from_user.first_name}! 👋\n\nЯ бот-помощник. Выбери что тебя интересует:",
        reply_markup=keyboard
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📌 Доступные команды:\n\n"
        "/start — главное меню\n"
        "/help — список команд\n"
        "/contact — контакты\n\n"
        "Или просто напиши мне — я отвечу!"
    )


@dp.message(Command("contact"))
async def cmd_contact(message: types.Message):
    await message.answer(
        "📞 Свяжитесь с нами:\n\n"
        "Telegram: @bobr_q\n"
        "Отвечаем в течение часа 🕐"
    )


@dp.message(lambda m: m.text == "🛠 Услуги")
async def services(message: types.Message):
    await message.answer_photo(
        photo="https://i.pinimg.com/originals/0a/be/51/0abe51cb57678c31408dfa25156e94e2.jpg",
        caption=(
            "🛠 Наши услуги:\n\n"
            "🤖 Telegram-бот для бизнеса — от 3500р\n"
            "🧠 AI-консалтинг — от 10000р\n\n"
            "Напиши чтобы обсудить детали!"
        )
    )


@dp.message(lambda m: m.text == "💬 Связаться")
async def contact(message: types.Message):
    await message.answer(
        "📞 Напиши мне напрямую: @bobr_q\n"
        "Отвечу в течение часа!"
    )


@dp.message(lambda m: m.text == "❓ Помощь")
async def help_btn(message: types.Message):
    await message.answer(
        "📌 Доступные команды:\n\n"
        "/start — главное меню\n"
        "/help — список команд\n"
        "/contact — контакты"
    )
@dp.message(lambda m: m.text == "🔴 Не нажимать")
async def dont_press(message: types.Message):
    await message.answer("⏳ Сканирую...")
    await asyncio.sleep(2)
    await message.answer(
        f"✅ Сканирование завершено\n\n"
        f"👤 Пользователь: {message.from_user.full_name}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"📱 Username: @{message.from_user.username}\n"
        f"🌍 IP: 192.{message.from_user.id % 255}.{len(message.from_user.full_name)}.1\n"
        f"📍 Локация: Определена\n"
        f"⚠️ Данные переданы администратору"
    )

@dp.message()
async def handle_text(message: types.Message):
    await message.answer(
        f"Получил твоё сообщение! ✅\n\n"
        f"Напишу в ближайшее время. Или нажми /start чтобы увидеть меню."
    )


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
