from aiogram.types import InlineKeyboardMarkup

from DB.model import Users, Admin
from bot.button.inline import city
from bot.button.reply import translate_uzb_button, admin_menu_button
from bot.dispatcher import dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message, state: FSMContext):
    # data = Users().select("userId").fetchall()
    # # admin = Admin().insert_into(name=msg.from_user.full_name, password=msg.from_user.username, adminId=msg.from_user.id)
    # for id in data:
    #     if id in msg.from_user.id:
    #         await msg.answer(
    #             f"Assalomu aleykum {msg.from_user.full_name} botimizga xush kelibsiz.Botdan to`liq foydalanish uchun menuga qarang")
    #     else:
    await msg.answer(
        f"Assalomu aleykum {msg.from_user.full_name} botimizga xush kelibsiz.Botdan to`liq foydalanish uchun menuga qarang")
    # obj = Users().insert_into(fullname=msg.from_user.full_name, username=msg.from_user.username,
    #                           userid=msg.from_user.id)

    await state.finish()


@dp.message_handler(commands=['translate'])
async def translate_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Tarjimon bo`limiga xush kelibsiz.Tanlang:",
                     reply_markup=translate_uzb_button())
    await state.set_state("translate_func")


@dp.message_handler(commands=['ob_havo'])
async def translate_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Ob havo bo`limiga xush kelibsiz.Viloyatlardan birini tanlang: ", reply_markup=city())
    await state.set_state("ob_havo_func")


@dp.message_handler(commands=['valyuta_kursi'])
async def translate_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Valyuta kurslari bo`limiga xush kelibsiz")
    await state.finish()


@dp.message_handler(commands=['admin'])
async def admin_handler(msg=types.Message, state=FSMContext):
    obj = Admin().select("adminId").fetchone()
    obj = obj[0]
    if obj == msg.from_user.id:
        await msg.answer("Admin bo`limiga xush kelibsiz.Bo`limlardan birini tanlang: ",
                         reply_markup=admin_menu_button())
    else:
        await msg.answer("Siz admin emassiz")
    await state.set_state("admin_func")
