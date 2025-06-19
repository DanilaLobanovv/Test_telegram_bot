from telegram.ext import CommandHandler
from telegram import Update

class SosiCommandHandlers:

    @staticmethod
    async def sosi1(update: Update, context):
        await update.message.reply_text("sosi1")

    @staticmethod
    async def sosi2(update: Update, context):
        await update.message.reply_text("sosi2")

def register(application):

    application.add_handler(CommandHandler("sosi1", SosiCommandHandlers.sosi1))
    application.add_handler(CommandHandler("sosi2", SosiCommandHandlers.sosi2))