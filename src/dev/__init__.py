"""A simple module for development environment"""
from os import getenv
from asyncio import run

import dotenv

from bot.main import main as start_bot


def main():
    """Entry point for the development environment"""
    dotenv.load_dotenv('.env/dev.env')
    dotenv.load_dotenv('.env/token.env')
    print("Hello from dev!")
    bot_token = getenv("TOKEN")
    print(f"Bot token: {bot_token}")
    run(start_bot(bot_token))
