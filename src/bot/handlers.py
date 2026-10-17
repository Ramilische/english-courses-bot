"""Handlers for the bot"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards import get_payment_keyboard


router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message):
    """Handler for the /start command"""
    if message.from_user is None:
        await message.answer("Привет! Бот не предназначен для использования в каналах, пишите напрямую.")
        return
    price = 1000
    text = (
        f"Привет, {message.from_user.first_name}!\n\n"
        f"Здесь можно купить курс английского языка. Цена: {price} рублей.\n\n"
        "Чтобы оплатить, нажмите на кнопку ниже."
    )
    await message.answer(text, reply_markup=get_payment_keyboard())

@router.message(Command(commands=["pay"]))
async def pay(message: Message):
    """Handler for the /pay command"""
    await message.answer("Оплата")
