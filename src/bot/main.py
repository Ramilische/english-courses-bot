"""Main module for the bot"""
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def start(message: Message):
    """Handler for the /start command"""
    await message.reply("Старт")


async def main(bot_token: str | None):
    """Function to start the bot"""
    if bot_token is None:
        raise ValueError("Bot token is not set. Please set the TOKEN environment variable.")
    await dp.start_polling(Bot(token=bot_token))
