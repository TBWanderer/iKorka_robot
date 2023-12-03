from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from messages import *

router = Router()


@router.message()
async def textHandler(msg: Message):
    if msg.reply_to_message:
        reputationAdding = False
        for word in REPUTATION_ADD_MESSAGES:
            if word in str(msg.text):
                reputationAdding = True
                break
        if reputationAdding:
            add_rep_to_id = int(msg.reply_to_message.from_user.id)
            await msg.answer(add_rep_to_id)
