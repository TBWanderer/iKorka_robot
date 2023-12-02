from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from messages import NON_PRIVATE_START_MESSAGE

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    if msg.chat.type != "private":
        await msg.answer("Yes, sir!")
    else:
        await msg.answer(NON_PRIVATE_START_MESSAGE)
