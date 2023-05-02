
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware, BaseMiddleware

from configuration import strings
from bot.utils.constants import DEFAULT_LANGUAGE
from database.base import session
from database.models.user import User


class UserToContextMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self):
        super().__init__()

    async def pre_process(self, message: types.Message, data, *args):
        if not hasattr(message, "from_user") or message.from_user is None:
            data["user"] = None
        else:
            with session() as s:
                user = s.query(User).filter(User.telegram_id == message.chat.id).first()
                if user is None:
                    user = User(telegram_id=message.from_user.id, username=message.from_user.username)
                    s.add(user)
                    s.commit()
            data["user"] = user


class IgnoreWithoutUsernameMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        language = DEFAULT_LANGUAGE
        if isinstance(obj, types.CallbackQuery):
            chat_type = obj.message.chat.type
        elif isinstance(obj, types.InlineQuery):
            chat_type = obj.chat_type
        elif isinstance(obj, types.Message):
            chat_type = obj.chat.type
        else:
            return

        if chat_type != "private":
            return

        if obj.from_user.username is None:
            await obj.answer(text=strings[language].get('prompts', 'ignore_without_username'))
            raise CancelHandler()


class UpdateUsernameMiddleware(BaseMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        # requires UserToContextMiddleware before
        if not hasattr(message, "from_user"):
            return
        else:
            user = data['user']
            if user.username != message.from_user.username:
                user.username = message.from_user.username

                with session() as s:
                    res = s.query(User).filter(User.telegram_id == user.telegram_id).first()
                    res.username = user.username
