from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State

from database import is_admin
from .buttons import register_kb
from .admin_button import admin_munu_text,admin_menu,order_button


admin_router = Router()


@admin_router.message(Command("admin"))
async def start_admin(message:Message):
    chat_id = message.from_user.id

    user = is_admin(chat_id)

    if user:
        if user[-1]:
           
           await message.answer(text=admin_munu_text,reply_markup=admin_menu)
        else:
            await message.answer("Siz admin emassiz!!! 🙃")
    else:

        await message.answer("Siz Ro'yhatdan o'tmagansiz, Ro'yhatdan o'ting: ",reply_markup=register_kb)


@admin_router.message(F.text =="🧾 Buyurtmalar")
async def show_order(message: Message):
    text="""📦 Buyurtmalar bo‘limi:\nKerakli turini tanlang 👇"""

    await message.answer(text=text,reply_markup=order_button)





