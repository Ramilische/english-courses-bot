"""A simple module for production environment"""
from os import getenv
from asyncio import run

import dotenv

from bot.main import start


def main():
    """Entry point for the production environment"""
    dotenv.load_dotenv('./env/prod.env')
    bot_token = getenv("BOT_TOKEN")
    print(f"Bot token: {bot_token}")
    run(start(bot_token))
