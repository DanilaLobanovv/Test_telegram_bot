from telegram.ext import CommandHandler
from telegram import Update

class HelpCommandHandlers:

    @staticmethod
    async def help1(update: Update, context):
        await update.message.reply_text("help1")

    @staticmethod
    async def help2(update: Update, context):
        await update.message.reply_text("help2")

def register(application):

    application.add_handler(CommandHandler("help1", HelpCommandHandlers.help1))
    application.add_handler(CommandHandler("help2", HelpCommandHandlers.help2))