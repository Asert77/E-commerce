import time

import requests
from django.conf import settings
from celery import shared_task


@shared_task
def send_telegram_notification(order_id, product_name, quantity, customer_username, phone_number):
    time.sleep(5)

    token = settings.TELEGRAM_BOT_TOKEN
    method = 'sendMessage'
    message_text = (
        f"📦 Yangi buyurtma: #{order_id}\n"
        f"🛒 Mahsulot: {product_name}\n"
        f"🔢 Miqdor: {quantity}\n"
        f"👤 Mijoz: {customer_username}\n"
        f"📞 Telefon: {phone_number}"
    )



    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 392330197, 'text': message_text}
    ).json()
