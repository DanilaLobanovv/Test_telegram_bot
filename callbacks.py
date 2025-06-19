from telegram.ext import ContextTypes, CommandHandler
from telegram import Update


async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Основной обработчик callback-запросов"""
    query = update.callback_query
    await query.answer()  # подтверждаем получение callback

    # Обрабатываем кнопки с командами
    if query.data.startswith('/'):
        await handle_command_callback(query, context)

    # Здесь можно добавить обработку других типов callback_data
    # elif query.data.startswith('other_prefix_'):
    #     await handle_other_callback(query, context)


async def handle_command_callback(query, context):
    """Обработчик callback-кнопок с командами"""
    # Получаем обработчики из первой группы (обычно MessageHandler)
    handlers = context.application.handlers[0]

    for handler in handlers:
        # Проверяем, что это CommandHandler и команда есть в его списке
        if isinstance(handler, CommandHandler) and query.data[1:] in handler.commands:
            # Создаем фейковый update
            fake_update = Update(
                query.message.message_id + 1,  # новый ID для update
                message=query.message.reply_to_message or query.message,
                callback_query=None
            )
            # Запускаем обработчик команды
            await handler.handle_update(fake_update, context.application, None, None)
