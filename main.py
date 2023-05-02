import asyncio
import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from bot.filters.role import RoleFilter, PermissionsFilter

from bot.handlers.user.base_user import register_user_handlers

from bot.middlewares.blocked import IgnoreBlockedUsersMiddleware
from bot.middlewares.only_private import AnswerOnlyInPrivateChats
from bot.middlewares.roles import RoleMiddleware
from bot.middlewares.user_base import UserToContextMiddleware, IgnoreWithoutUsernameMiddleware, UpdateUsernameMiddleware
from configuration import TOKEN, USE_REDIS, LOGGING_FILE_PATH


logger = logging.getLogger(__name__)


async def main():
    if LOGGING_FILE_PATH is not None:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )
    logger.error("Starting bot")

    if USE_REDIS:
        storage = RedisStorage(host='redis')
    else:
        storage = MemoryStorage()

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=storage)

    dp.filters_factory.bind(RoleFilter)
    dp.filters_factory.bind(PermissionsFilter)

    dp.middleware.setup(UserToContextMiddleware())
    dp.middleware.setup(IgnoreWithoutUsernameMiddleware())
    dp.middleware.setup(AnswerOnlyInPrivateChats())
    dp.middleware.setup(UpdateUsernameMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(RoleMiddleware())
    dp.middleware.setup(IgnoreBlockedUsersMiddleware())

    # Warning! registration order is important (base user commands at last step)
    register_user_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
