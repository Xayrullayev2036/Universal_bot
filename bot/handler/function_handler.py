import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from deep_translator import GoogleTranslator
import os
from DB.model import Users
from bot.button.inline import back, city, send_button
from bot.button.reply import other_lang_button, admin_menu_button
from bot.button.text import uzb_lang, other_lang, rus, eng, reklama, users, send
from bot.dispatcher import dp, bot
from bs4 import BeautifulSoup as BS


@dp.message_handler(state='translate_func')
async def translate_functions(msg: types.Message, state: FSMContext):
    if msg.text == uzb_lang:
        await msg.answer("Tarjima qilinadigan so`zni kiriting: ")
        await state.set_state("translate_uzb_functions")
    if msg.text == other_lang:
        await msg.answer("Tillardan birini tanlang: ", reply_markup=other_lang_button())
        await state.set_state("translate_other_functions")


@dp.message_handler(state="translate_uzb_functions")
async def translate_uzb(msg=types.Message, state=FSMContext):
    await msg.answer(
        f"Bu so`zning o`zbek tiliga tarjimasi: {GoogleTranslator(source='auto', target='uz').translate(f'{msg.text}')}")
    await state.finish()


@dp.message_handler(state="translate_other_functions")
async def translate_other(msg=types.Message, state=FSMContext):
    if msg.text == rus:
        await msg.answer("So`zni kiriting: ")
        await state.set_state(state="translate_rus")
    if msg.text == eng:
        await msg.answer("So`zni kiriting: ")
        await state.set_state(state="translate_eng")


@dp.message_handler(state="translate_rus")
async def translate_russia(msg=types.Message, state=FSMContext):
    await msg.answer(
        f"Bu so`zning rus tiliga tarjimasi: {GoogleTranslator(source='auto', target='ru').translate(f'{msg.text}')}")
    await state.finish()


@dp.message_handler(state="translate_eng")
async def translate_english(msg=types.Message, state=FSMContext):
    await msg.answer(
        f"Bu so`zning ingliz tiliga tarjimasi: {GoogleTranslator(source='auto', target='en').translate(f'{msg.text}')}")
    await state.finish()


# =============================================Weather=======================================================================

@dp.callback_query_handler(state="ob_havo_func")
async def ob_havo(call=types.CallbackQuery,state = FSMContext):
    if call.data == "back":
        await call.message.answer('Tanlang', reply_markup=city())
        await call.message.delete()
        await state.finish()


    if call.data == "01":
        data = weather('погода-ташкент')
        await call.message.answer(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "02":
        data = weather('погода-фергана')
        await call.message.answer(f"Bugun Farg`ona shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "03":
        data = weather('погода-андижан')
        await call.message.answer(f"Bugun Andijon shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "04":
        data = weather('погода-наманган')
        await call.message.answer(f"Bugun Namangan shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "05":
        data = weather('погода-ургенч')
        await call.message.answer(f"Bugun Xorazm,Urganch shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "06":
        data = weather('погода-бухара')
        await call.message.answer(f"Bugun Buxoro shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "07":
        data = weather('погода-самарканд')
        await call.message.answer(f"Bugun Samarqand shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "08":
        data = weather('погода-карши')
        await call.message.answer(f"Bugun Qashqadaryo,Qarshi shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "09":
        data = weather('погода-джизак')
        await call.message.answer(f"Bugun Jizzax shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "10":
        data = weather('погода-навои')
        await call.message.answer(f"Bugun Navoiy shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "11":
        data = weather('погода-термез')
        await call.message.answer(f"Bugun Surxondaryo,Termiz shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()

    if call.data == "12":
        data = weather('погода-гулистан')
        await call.message.answer(f"Bugun Sirdaryo,Guliston shaxrida havo o`zgarib turadi\nmin {data[0]}\nmax "
                                  f"{data[1]} \nbo`lishi kutilmoqda ⛅",
                                  reply_markup=back())
        await call.message.delete()
        await state.finish()


def weather(data):
    t = requests.get(f'https://sinoptik.ua/{data}')
    html_t = BS(t.content, 'html.parser')

    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
        return (t_min, t_max)


# ============================================ADMIN=============================================================

@dp.message_handler(state="admin_func")
async def admin_function(msg=types.Message, state=FSMContext):
    if msg.text == reklama:
        await msg.answer("Reklama rasmini yuboring: ")
        await state.set_state("download_image")
    if msg.text == users:
        obj = Users().select("id").fetchall()
        await msg.answer(f"Barcha foydalanuvchilar soni: {len(obj)}")


@dp.message_handler(content_types=types.ContentType.PHOTO, state="download_image")
async def from_user_get_image(msg: types.Message, state: FSMContext):
    photo = msg.photo[-1]
    file_id = photo.file_id

    # Rasm faylini olish
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{os.getenv('Token')}/{file_path}"
    file_url = f"https://api.telegram.org/file/bot{os.getenv('Token')}/{file_path}"

    # Faylni yuklab olish
    file_name = f"photo_{file_id}.jpg"  # Fayl nomini o'zgartiring
    file_path_local = f"/home/diyorbek/PycharmProjects/Modul8/Universal_bot/image/{file_name}"  # Faylni saqlash joyini o'zgartiring

    # Faylni yuklab olish
    async with bot.session.get(file_url) as response:
        content = await response.read()
        with open(file_path_local, "wb") as f:
            f.write(content)

    async with state.proxy() as file:
        file["image"] = file_path_local

    await msg.answer("Reklama matnini kiriting: ")
    await state.set_state("image_text")


@dp.message_handler(state="image_text")
async def image_text_func(msg=types.Message, state=FSMContext):
    async with state.proxy() as file:
        file["image_text"] = msg.text

    with open(file['image'], 'rb') as photo:
        await bot.send_photo(chat_id=msg.chat.id, photo=photo, caption=f"{file['image_text']}",
                             reply_markup=send_button())
    await state.set_state("send_users")


@dp.callback_query_handler(state="send_users")
async def send_users_functions(call=types.CallbackQuery, state=FSMContext):
    obj = Users().select("userId").fetchall()
    async with state.proxy() as file:
        file["document"] = call.data

    if call.data == "send":
        await call.message.delete()
        for user in obj:
            with open(file['image'], 'rb') as photo:
                await bot.send_photo(chat_id=user[0], photo=photo, caption=f"{file['image_text']}")
    if call.data == "edit":
        await call.message.delete()
        await call.message.answer("Bo`limlardan birini tanlang: ",
                                  reply_markup=admin_menu_button())
        await state.set_state("admin_func")
