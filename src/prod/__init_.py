"""A simple module for production environment"""
import dotenv
from os import getenv


def main():
    """Entry point for the production environment"""
    dotenv.load_dotenv('./env/prod.env')
