from telegram import Update
from telegram.ext import CallbackQueryHandler

from handlers.__init__ import *
from callbacks import handle_callback_query

# Основная функция||
def main() -> None:

    # Создание бота и ввод токена
    application = Application.builder().token("7722825455:AAGQvJrLgZGBmn9tZpTuAiE8t_PcemTaK6w").build()
    # Регистрируем все наши кнопки через __init__.py
    register_handlers(application)
    # Обработчик кнопок
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Обновляет сам бот когда ты сохраняешь файл
    application.run_polling(allowed_updates=Update.ALL_TYPES)


# Если функция основная, а не импортированная, то стартуем
if __name__ == "__main__":
    main()