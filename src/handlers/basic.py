from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from messages import *

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    if msg.chat.type != "private":
        await msg.answer(NON_PRIVATE_START_MESSAGE)
    else:
        await msg.answer(PRIVATE_START_MESSAGE)


@router.message(Command("faq"))
async def faq_handler(msg: Message):
    await msg.answer(FAQ_MESSAGE)
