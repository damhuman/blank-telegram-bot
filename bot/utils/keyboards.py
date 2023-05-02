from aiogram.dispatcher.handler import ctx_data
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from configuration import strings
from bot.utils.constants import GUEST, USER, DEFAULT_LANGUAGE
from database.models.user import User


class MainKeyboards:

    @staticmethod
    def default_keyboard(language=DEFAULT_LANGUAGE, ignore_admin=False):
        """
        :param: ignore_admin - if True returns user keyboard for Admins and SuperAdmins
        """
        role = ctx_data.get().get("role")
        if role == GUEST:
            return MainKeyboards.guest_keyboard(language)
        if role == USER or ignore_admin:
            return MainKeyboards.guest_keyboard(language)

        return MainKeyboards.admin_keyboard()

    @staticmethod
    def guest_keyboard(language=DEFAULT_LANGUAGE):
        faq = KeyboardButton(strings[language].get('buttons', 'profile'))
        lang = KeyboardButton(strings[language].get('buttons', 'set_lang'))
        profile = KeyboardButton(strings[language].get('buttons', 'faq'))
        return ReplyKeyboardMarkup(resize_keyboard=True).add(profile, lang)

    @staticmethod
    def admin_keyboard(language=DEFAULT_LANGUAGE):
        result_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        admin = KeyboardButton(strings[language].get('buttons', 'admin'))
        profile = KeyboardButton(strings[language].get('buttons', 'faq'))
        result_kb.add(profile, admin)
        return result_kb


class ProfileKeyboards:
    @staticmethod
    def profile_keyboard(user: User, language=DEFAULT_LANGUAGE):
        keyboard = InlineKeyboardMarkup(row_width=1)
        close = InlineKeyboardButton(strings[language].get('buttons', 'close'), callback_data='close')
        keyboard.add(close)
        return keyboard


class BasicKeyboards:
    @staticmethod
    def close_button(language=DEFAULT_LANGUAGE):
        return InlineKeyboardButton(strings[language].get('buttons', 'close'), callback_data="close")

    @staticmethod
    def back_keyboard(language=DEFAULT_LANGUAGE):
        result_kb = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(strings[language].get('buttons', 'back'), callback_data='back')
        result_kb.row(back)
        return result_kb
