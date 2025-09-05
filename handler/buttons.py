from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup


register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Register")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "📞 Phone",request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "📍 Location",request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


reg_text = """
    🍔 FastFood Botga xush kelibsiz! 🚀  

    Buyurtma berishdan oldin ro‘yxatdan o‘tishingiz kerak.  
    Iltimos, quyidagi ma’lumotlarni yuboring:  

👤 Ismingiz  
📞 Telefon raqamingiz (+998 formatda)  
📍 Yetkazib berish manzilingiz  

❗ Ma’lumotlaringiz faqat buyurtmalar uchun ishlatiladi.

                
"""

