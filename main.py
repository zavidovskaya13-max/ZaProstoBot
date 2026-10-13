import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router

load_dotenv()

async def main():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        print("Ошибка: BOT_TOKEN не найден в .env!")
        return

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)

    print("Бот успешно запущен на Python 3.14 и ожидает сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
