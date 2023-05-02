from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class AnswerOnlyInPrivateChats(BaseMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        if not hasattr(message.chat, "type"):
            ignore_msg = True
        elif message.chat.type == "private":
            ignore_msg = False
        elif message.new_chat_members or message.left_chat_member:
            ignore_msg = False
        else:
            ignore_msg = True

        if ignore_msg:
            raise CancelHandler()
