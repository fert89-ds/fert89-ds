from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_MACBOOK, URL_IPHONE12

keyboard = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton ( text='button1' ),
            KeyboardButton ( text='button2' )
        ],
        [
            KeyboardButton ( text='button3' )
        ]
    ],
    resize_keyboard=True
)

cb = CallbackData ( 'buy', 'id', 'name', 'price' )

keyboard1 = InlineKeyboardMarkup (
    inline_keyboard=[
        {
            InlineKeyboardButton ( text='Iphone 12',
                                   callback_data='buy:0:phone:1000' ),
            InlineKeyboardButton ( text='macBook',
                                   callback_data='buy:1:mac:8888' )
        },
        [
            InlineKeyboardButton ( text='Cancel',
                                   callback_data='cancel' )
        ]
    ]
)

phone_key = InlineKeyboardMarkup (
    inline_keyboard=[
        InlineKeyboardButton ( 'Купить', url=URL_IPHONE12 )
    ]
)

mac_key = InlineKeyboardMarkup (
    inline_keyboard=[
        InlineKeyboardButton ( 'Купить', url=URL_MACBOOK )
    ]
)
