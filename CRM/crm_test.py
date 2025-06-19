from telegram import Update
from telegram.ext import ContextTypes
import requests

BITRIX_WEBHOOK = "https://yourdomain.bitrix24.ru/rest/1/yourwebhook/"


async def create_bitrix_deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    deal_data = {
        "TITLE": f"Заказ от {update.effective_user.full_name}",
        "STAGE_ID": "NEW",
        "CONTACT_ID": await get_or_create_bitrix_contact(update),
        "ASSIGNED_BY_ID": 1,  # ID ответственного
        "UF_CRM_TELEGRAM_ID": str(update.effective_user.id)
    }

    response = requests.post(
        f"{BITRIX_WEBHOOK}crm.deal.add",
        json={"fields": deal_data}
    ).json()

    if 'result' in response:
        await update.message.reply_text("Заявка создана!")
    else:
        await update.message.reply_text("Ошибка при создании заявки")


async def get_or_create_bitrix_contact(update: Update):
    user = update.effective_user
    phone = context.user_data.get('phone')

    # Поиск существующего контакта
    search_response = requests.post(
        f"{BITRIX_WEBHOOK}crm.contact.list",
        json={"filter": {"PHONE": phone}}
    ).json()

    if search_response.get('result'):
        return search_response['result'][0]['ID']

    # Создание нового контакта
    create_response = requests.post(
        f"{BITRIX_WEBHOOK}crm.contact.add",
        json={
            "fields": {
                "NAME": user.first_name,
                "LAST_NAME": user.last_name,
                "PHONE": [{"VALUE": phone}],
                "UF_CRM_TELEGRAM_ID": str(user.id)
            }
        }
    ).json()

    return create_response.get('result')