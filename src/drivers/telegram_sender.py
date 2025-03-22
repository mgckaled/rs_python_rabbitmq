import os

import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Obtém os valores das variáveis de ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_GROUP_CHAT_ID = os.getenv("BOT_GROUP_CHAT_ID")


def send_telegram_message(message: str) -> None:

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": {BOT_GROUP_CHAT_ID},
        "text": message
    }
    requests.post(url, data=payload, timeout=10)
