"""A simple module for development environment"""
from os import getenv
from asyncio import run

import dotenv

from bot.main import start


def main():
    """Entry point for the development environment"""
    dotenv.load_dotenv('.env/dev.env')
    print("Hello from dev!")
    bot_token = getenv("BOT_TOKEN")
    print(f"Bot token: {bot_token}")
    run(start(bot_token))
