from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.button.text import uzb_lang, other_lang, rus, eng, reklama, users


def translate_uzb_button():
    design = [
        [uzb_lang], [other_lang]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def other_lang_button():
    design = [
        [rus], [eng]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def admin_menu_button():
    design = [
        [reklama, users],
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
