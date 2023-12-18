from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from DB.model import Admin, Product
from bot.button.reply_button import admin_menu, admin_back, update_menu
from bot.button.text import add_product, back_menu, update_product, update_name,delete_product
from bot.dispatcher import dp

# ========================Admin_menu====================
@dp.message_handler(state = "admin_panel")
async def check_password_handler(msg:types.Message,state:FSMContext):
    id_ = Admin().select("chatid").fetchone()
    id = str(*id_)
    print("db",id)
    print(msg.from_user.id)
    if id == str(msg.from_user.id):
        await msg.answer(f"Xush kelibsiz {msg.from_user.full_name} bugun qanday o`zgarishlar qilamiz",reply_markup=admin_menu())
        await state.set_state("product_menu")
    else:
        await msg.answer("Kechirasiz siz admin emassiz: ")


# =======================Product_add===========================================
@dp.message_handler(Text(add_product),state = "product_menu")
async def product_add_handler(msg:types.Message,state:FSMContext):
    await msg.answer("Product nomini kiriting: ")
    await state.set_state("name_add")

@dp.message_handler(state = "name_add")
async def product_add_handler(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["product_name"] = msg.text
    await msg.answer("Product narxini kiriting: ")
    await state.set_state("price_add")

@dp.message_handler(state = "price_add")
async def product_add_handler(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["product_price"] = msg.text
    await msg.answer("Product sonini kiriting: ")
    await state.set_state("count_add")

@dp.message_handler(state = "count_add")
async def product_add_handler(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["product_count"] = msg.text
        data["admin_name"] = Admin(password=data.get("key")).select("name")
    data = dict(data)
    Product().insert_into(**data)
    await msg.answer("Muvaffaqiyatli saqlandi",reply_markup=admin_menu())
    await state.finish()
# =========================================================================================

@dp.message_handler(Text(update_product),state = "product_menu")
async def product_add_handler(msg:types.Message,state:FSMContext):
    await msg.answer("Tanlang: ",reply_markup=update_menu())
    await state.set_state("update_menu")

@dp.message_handler(Text(update_name),state = "update_menu")
async def update_handler(msg:types.Message,state:FSMContext):
    await msg.answer("Product hozirgi nomini kiriting: ")
    await state.set_state("update_name")


@dp.message_handler(state = "update_name")
async def update_name_handler(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["old_name"] = msg.text
    await msg.answer("O`zgartiriladigan nomini kiriting: ")
    await state.set_state("new_name")

@dp.message_handler(state ="new_name")
async def new_name_handler(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["new_name"] = msg.text
    data = dict(data)
    Product(name = data["old_name"]).update(name = data["new_name"])
    await msg.answer("Success")
# =========================================================================================

@dp.message_handler(Text(delete_product),state = "product_menu")
async def product_add_handler(msg:types.Message,state:FSMContext):
    await msg.answer("O`chiriladigan product nomini kiriting: ")
    await state.set_state("delete_menu")


@dp.message_handler(state = "delete_menu")
async def update_name_handler(msg:types.Message,state:FSMContext):
    Product().delete(product_name=msg.text)
    await msg.answer("Muvaffaqiyatli o`chirildi")
    await state.finish()

