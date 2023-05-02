from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class IgnoreBlockedUsersMiddleware(BaseMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        # requires UserToContextMiddleware before

        if not hasattr(message, "from_user"):
            data["is_banned"] = None
        else:
            user = data['user']
            data["is_banned"] = user.is_banned

        if data["is_banned"]:
            raise CancelHandler()
