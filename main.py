import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Боттун токени (Render'ден Environment Variable катары берилет)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Салам! Оюндарга автоматикалык түрдө донат салуу ботуна кош келдиңиз! 🎮"
    )


async def main():
    print("Бот ишке киргизилди...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
