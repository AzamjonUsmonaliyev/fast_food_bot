from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from database import get_foods
from aiogram.utils.keyboard import InlineKeyboardBuilder



admin_menu = ReplyKeyboardMarkup(
    keyboard=[
       
         [
            KeyboardButton(text="🧾 Buyurtmalar"),
            KeyboardButton(text="🍱 Menu")
        ],
        [
            KeyboardButton(text="👥 Foydalanuvchilar"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    
    ], 
    resize_keyboard= True,
    one_time_keyboard=True
)


order_button= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🆕 New")],
        [KeyboardButton(text="⏳ In Progress")],
        [KeyboardButton(text="✅ Finished")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)

admin_munu_text = """
✅ Siz muvaffaqiyatli Admin panelga kirdingiz!
Bu bo‘lim orqali siz quyidagi amallarni bajarishingiz mumkin:

🍔 Yangi taom qo‘shish

✏️ Taomlarni tahrirlash yoki o‘chirish

📊 Buyurtmalarni ko‘rish va boshqarish

👥 Foydalanuvchilarni kuzatish

⚙️ Iltimos, kerakli bo‘limni tanlang:"""
