from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from bot.utils.utils import verify_text
from configuration import strings
from bot.utils.constants import DEFAULT_LANGUAGE, Language
from bot.utils.keyboards import MainKeyboards
from database.base import session
from database.models.user import User


async def process_help_command(m: types.Message, state: FSMContext):
    await state.finish()
    await m.reply(strings[DEFAULT_LANGUAGE].get('prompts', 'help_message'), parse_mode=ParseMode.MARKDOWN_V2,
                  reply_markup=MainKeyboards.default_keyboard())


async def process_start_command(m: types.Message, state: FSMContext):
    with session() as s:
        user = s.query(User).filter(User.telegram_id == m.chat.id).first()
    # if start param exists => handle it
    start_params = m.text.split()
    if len(start_params) > 1:
        # add handlers for start params
        pass
    await m.reply(strings[user.language.value].get('prompts', 'start_message').format(username=m.from_user.username),
                  reply_markup=MainKeyboards.default_keyboard(ignore_admin=False))
    await state.finish()


async def process_change_language(m: types.Message, state: FSMContext):
    with session() as s:
        user = s.query(User).filter(User.telegram_id == m.chat.id).first()

    if user.language == Language.ua:
        user.language = Language.en
    else:
        user.language = Language.ua

    with session() as s:
        res = s.query(User).filter(User.telegram_id == user.telegram_id).first()
        res.language = user.language

    await m.bot.send_message(chat_id=m.chat.id,
                             text=strings[user.language.value].get('prompts', 'start_message').format(
                                 username=m.chat.username),
                             reply_markup=MainKeyboards.default_keyboard(language=user.language.value)
                             )
    await state.finish()


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_help_command, commands=["help"], state="*")
    dp.register_message_handler(process_start_command, commands=["start"], state="*")
    dp.register_message_handler(process_change_language, lambda m: verify_text('buttons', 'set_lang', m.text), state='*')
