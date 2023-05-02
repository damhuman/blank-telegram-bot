from datetime import datetime
import re

from aiogram.utils.markdown import text, bold, escape_md
from configuration import DATE_FORMAT, strings


def datetime_json_encoder(dt):
    if isinstance(dt, datetime):
        return dt.strftime(DATE_FORMAT)
    return None


def is_valid_email(email):
    # Make a regular expression
    # for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # pass the regular expression
    # and the string in search() method
    return re.search(regex, email)


def text_to_tag(text):
    return text.replace(" ", "")


def prepare_for_markdown(text):
    markdown_symbols = ['-', '.', ',', '?', '_', '*', '@', '"', '\'', '$', '(', ')', '!']
    for ch in markdown_symbols:
        text = text.replace(ch, '\\' + ch)
    return text


def prepare_from_discord_to_telegram(text):
    markdown_symbols = ['-', '.', ',', '?', '_', '@', '"', '\'', '$', '(', ')', '!', '#', '|', '=', '{', '}', '>',
                        '[', ']', '+', '~']
    for ch in markdown_symbols:
        text = text.replace(ch, '\\' + ch)
        text = text.replace('**', '*')
        text = text.replace('```', ' ``` ')
    return text


def faq_to_msg_text(questions):
    result_content = []
    for q in questions:
        result_content.append(bold(f"{q.question}"))
        result_content.append(escape_md(q.answer))
        result_content.append("\n")

    return text(*result_content, sep="\n")


def is_photo_file(filename):
    file_type = filename.split('.')[-1]
    photo_types = ['jpg', 'png', 'jpeg', 'gif']
    return file_type in photo_types


def verify_text(section, key, text):
    for localization in strings.values():
        if localization.get(section, key) == text:
            return True
    return False

