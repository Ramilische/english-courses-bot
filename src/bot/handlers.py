"""Handlers for the bot"""
from os import getenv

from dotenv import load_dotenv
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, LabeledPrice, SuccessfulPayment

from bot.keyboards import get_payment_keyboard
from bot.generate_link import generate_link

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message):
    """Handler for the /start command"""
    if message.from_user is None:
        await message.answer("Привет! Бот не предназначен для использования в каналах, пишите напрямую.")
        return

    text = (
        f"Привет, {message.from_user.first_name}!\n\n"
        f"Здесь можно купить курс английского языка. Цена: {getenv('PRICE')} рублей.\n\n"
        "Чтобы оплатить, нажмите на кнопку ниже."
    )
    await message.answer(text, reply_markup=get_payment_keyboard())

@router.message(Command(commands=["pay"]))
async def pay(message: Message):
    """Handler for the /pay command"""
    await message.answer("Оплата")

@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    """Handler for the pre-checkout query"""
    await pre_checkout_query.answer(ok=True)


@router.callback_query(lambda c: c.data == "pay")
async def process_payment_callback(callback_query: CallbackQuery):
    """Handler for the payment callback"""
    if callback_query.message is None:
        await callback_query.answer('Это откуда вообще прилетело')
        return
    if getenv('PROVIDER_TOKEN') is None:
        await callback_query.answer('Токен провайдера отсутствует, напиши @ramilische')
        return

    price_string = getenv('PRICE')
    price = 100
    if price_string:
        price = int(price_string)

    await callback_query.answer("Вы нажали на кнопку оплаты!")
    prices = [LabeledPrice(label='Оплата курса английского языка', amount=price * 100)]
    await callback_query.message.answer_invoice(
        title="Курс английского языка",
        description="Оплата курса английского языка",
        payload="course1",
        provider_token=getenv('PROVIDER_TOKEN'),
        prices=prices,
        currency='RUB'
    )


@router.message(F.successful_payment)
async def process_successful_payment(message: Message):
    """Sending a link after payment"""
    print('Вроде успешная оплата')
    link = generate_link()
    await message.answer(f'Оплата прошла успешно, ссылка на курс: {link}')

@router.message(lambda c: True)
async def check_if_payment_is_successful(message: Message):
    """Checks if message is successful payment"""
    payment = message.successful_payment
    if payment is None:
        await message.answer('Не понимаю')
        return

    print('Вроде успешная оплата')
    link = generate_link()
    await message.answer(f'Оплата прошла успешно, ссылка на курс: {link}')
