import os
import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import main_message


API_TOKEN = os.getenv("TOKEN")
bot = Bot(token=API_TOKEN)

async def main():
    dp = Dispatcher()

    dp.include_router(main_message.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
