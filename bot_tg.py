import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Услуги", callback_data="services")],
        [InlineKeyboardButton(text="💬 Связаться", callback_data="contact")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
    ])

    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я бот-помощник. Выбери что тебя интересует:",
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

@dp.callback_query()
async def handle_buttons(callback: types.CallbackQuery):
    if callback.data == "services":
        await callback.message.answer(
            "🛠 Наши услуги:\n\n"
            "🤖 Telegram-бот для бизнеса — от 3500р\n"
            "🧠 AI-консалтинг — от 10000р\n\n"
            "Напиши чтобы обсудить детали!"
        )

    elif callback.data == "contact":
        await callback.message.answer(
            "📞 Напиши мне напрямую: @bobr_q\n"
            "Отвечу в течение часа!"
        )

    elif callback.data == "help":
        await callback.message.answer(
            "📌 Доступные команды:\n\n"
            "/start — главное меню\n"
            "/help — список команд\n"
            "/contact — контакты"
        )

    await callback.answer()
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