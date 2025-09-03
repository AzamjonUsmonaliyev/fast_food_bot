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
        [KeyboardButton(text = "Phone",request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)