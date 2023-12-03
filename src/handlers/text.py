from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from messages import *

router = Router()


@router.message()
async def textHandler(msg: Message):
    await msg.answer("OK")
