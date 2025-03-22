import os

import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Obtém os valores das variáveis de ambiente
USER_NAME = os.getenv("USER_NAME")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_GROUP_CHAT_ID = os.getenv("BOT_GROUP_CHAT_ID")


def send_telegram_message(token, chat_id, message_text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message_text
    }
    requests.post(url, data=payload, timeout=10)


MSG = f"Olá Mundo!!!\n\nEnviado por {USER_NAME}."

send_telegram_message(
    token=BOT_TOKEN, chat_id=BOT_GROUP_CHAT_ID, message_text=MSG)
