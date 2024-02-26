import asyncio
from aiogram import Bot, Dispatcher
from src.config import TG_BOT_TOKEN
from src.database import async_session_maker
from src.chat_support.commands import chat_support_router
from src.middlewares.db import DataBaseSession

bot = Bot(token=TG_BOT_TOKEN)

ALLOWED_UPDATES = ['edited_messages, messages']
dp = Dispatcher()

dp.include_router(chat_support_router)


async def main():

    dp.update.middleware(DataBaseSession(session_pool=async_session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
