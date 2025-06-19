from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from keyboards.keyboards import *

class MainCommandHandlers:

    # ||Запускается при старте бота||
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Приветствие "user"
        user = update.effective_user
        await update.message.reply_html(
            rf"Привет, {user.mention_html()}!",
        )

        reply_markup = get_inline_start_menu()

        # Отправка сообщения с кнопками
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Выберите кнопку:",
            reply_markup=reply_markup
        )

    @staticmethod
    async def help(update: Update, context):

        """Обработчик команды /help с вложенным меню"""
        if update.message:  # Если команда вызвана через /help
            await update.message.reply_text(
                "Разделы помощи:",
                reply_markup=get_inline_help_menu()
            )
        else:  # Если вызвано из callback
            query = update.callback_query
            await query.answer()
            await query.edit_message_text(
                "Разделы помощи:",
                reply_markup=get_inline_help_menu()
            )

    @staticmethod
    async def sosi(update: Update, context):
        """Обработчик команды /sosi с вложенным меню"""
        if update.message:  # Если команда вызвана через /sosi
            await update.message.reply_text(
                "Разделы sosi:",
                reply_markup=get_inline_sosi_menu()
            )
        else:  # Если вызвано из callback
            query = update.callback_query
            await query.answer()
            await query.edit_message_text(
                "Разделы sosi:",
                reply_markup=get_inline_sosi_menu()
            )


def register(application):
    application.add_handler(CommandHandler("start", MainCommandHandlers.start))
    application.add_handler(CommandHandler("sosi", MainCommandHandlers.sosi))
    application.add_handler(CommandHandler("help", MainCommandHandlers.help))