"""Module for creating keyboards for the bot"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_payment_keyboard() -> InlineKeyboardMarkup:
    """Function to create a payment keyboard"""
    button = InlineKeyboardButton(text="Оплатить", callback_data="pay", style="bg_primary")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard
