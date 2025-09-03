from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import Command,CommandStart
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State

from database.query import is_register
from .buttons import register_kb,phone_kb

user_router = Router()


class Register(StatesGroup):
    fullname = State()
    phone = State()
    location = State()


@user_router.message(CommandStart())
async def start(message:Message):
    if is_register(message.from_user.id) is None:
        text = """
        🍔 FastFood Botga xush kelibsiz! 🚀  

            Buyurtma berishdan oldin ro‘yxatdan o‘tishingiz kerak.  
         Iltimos, quyidagi ma’lumotlarni yuboring:  

        👤 Ismingiz  
        📞 Telefon raqamingiz (+998 formatda)  
        📍 Yetkazib berish manzilingiz  

        ❗ Ma’lumotlaringiz faqat buyurtmalar uchun ishlatiladi.

                
"""
        await message.answer(text=text,reply_markup=register_kb)

    else:

        
        await message.answer("Siz avval ro'yhatdan o'tgansiz, menuga o'ting")


@user_router.message(F.text == "Register")
async def register_handler(message:Message,state:FSMContext):
    await state.set_state(Register.fullname)

    await message.answer("F.I.SH kiriting: ",reply_markup=ReplyKeyboardRemove())


@user_router.message(Register.fullname)
async def get_fullname(message:Message,state:FSMContext):
    await state.update_data(fullname = message.text)
    await state.set_state(Register.phone)

    await message.answer("Telfon raqam yiuboring: ",reply_markup=phone_kb,)



