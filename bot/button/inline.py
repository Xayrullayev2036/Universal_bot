from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.button.text import send, edit


def city():
    design = [
        [InlineKeyboardButton("Toshkent", callback_data=f"01"), InlineKeyboardButton("Farg`ona", callback_data="02")],
        [InlineKeyboardButton("Andijon", callback_data=f"03"), InlineKeyboardButton("Namangan", callback_data="04")],
        [InlineKeyboardButton("Xorazm", callback_data=f"05"), InlineKeyboardButton("Buxoro", callback_data="06")],
        [InlineKeyboardButton("Samarqand", callback_data=f"07"),
         InlineKeyboardButton("Qashqadaryo", callback_data="08")],
        [InlineKeyboardButton("Jizzax", callback_data=f"09"), InlineKeyboardButton("Navoiy", callback_data="10")],
        [InlineKeyboardButton("Surxondaryo", callback_data=f"11"),
         InlineKeyboardButton("Sirdaryo", callback_data="12")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design, row_width=2)


def back():
    design = [
        [InlineKeyboardButton("Orqaga", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


def send_button():
    design = [
        [InlineKeyboardButton(send, callback_data="send"),InlineKeyboardButton(edit,callback_data="edit")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)
