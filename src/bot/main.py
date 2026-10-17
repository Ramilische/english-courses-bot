"""Main module for the bot"""
from aiogram import Bot, Dispatcher

from bot.handlers import router

dp = Dispatcher()


async def start(bot_token: str | None):
    """Function to start the bot"""
    if bot_token is None:
        raise ValueError("Bot token is not set. Please set the TOKEN environment variable.")
    bot = Bot(token=bot_token)

    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    await dp.start_polling(bot)
