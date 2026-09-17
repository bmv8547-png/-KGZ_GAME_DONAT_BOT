import asyncio
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start командасы жана меню кнопкалары
@dp.message(Command("start"))
async def start_cmd(message: Message):
    kb = [
        [
            InlineKeyboardButton(
                text="💎 Баалар / Прейскурант", callback_data="price"
            )
        ],
        [InlineKeyboardButton(text="🎮 Донат кылуу", callback_data="donat")],
        [
            InlineKeyboardButton(
                text="👨‍💻 Админ менен байланышуу",
                url="https://t.me/your_admin_username",
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(
        "Салам! Оюндарга автоматикалык түрдө донат салуу ботуна кош келдиңиз! 🎮\n\n"
        "Керектүү бөлүмдү тандаңыз:",
        reply_markup=keyboard,
    )


# Баалар (Прейскурант) баскычы басылганда
@dp.callback_query(F.data == "price")
async def show_price(callback: types.CallbackQuery):
    text = (
        "💎 **Оюндардын донат баалары:**\n\n"
        "🔥 **Free Fire:**\n"
        "• 100+10 алма — 80 сом\n"
        "• 310+31 алма — 250 сом\n"
        "• 520+52 алма — 400 сом\n\n"
        "• 1166 алма - 780сом\n\n"
        "• 6150 алма - 3800сом\n\n"
        "• недельный ваучер - 165сом\n\n"
        "• недельный лайт - 40сом\n\n"
        "• месячный ваучер - 600сом\n\n"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()


# Донат кылуу баскычы басылганда
@dp.callback_query(F.data == "donat")
async def process_donat(callback: types.CallbackQuery):
    text = (
        "💳 **Төлөм реквизиттери:**\n\n"
        "OBANK / BAKAIBANK: `0705341671`\n\n"
        "Төлөгөндөн кийин чекти жана оюндагы ID'ңизди админге жөнөтүңүз!"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    
