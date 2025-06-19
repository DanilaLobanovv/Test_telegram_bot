from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Создание клавиатуры с inline-кнопками
def get_inline_start_menu():
    keyboard = [
        [InlineKeyboardButton("help", callback_data='/help')],
        [InlineKeyboardButton("sosi", callback_data='/sosi')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_inline_help_menu():
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='/help1'),
         InlineKeyboardButton("Кнопка 2", callback_data='/help2')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_inline_sosi_menu():
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='/sosi1'),
         InlineKeyboardButton("Кнопка 2", callback_data='/sosi2')]
    ]
    return InlineKeyboardMarkup(keyboard)