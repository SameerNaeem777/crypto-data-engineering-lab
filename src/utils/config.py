import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

SETTINGS = {
    "api_base_url": os.getenv("API_BASE_URL"),
    "pg_password": os.getenv("POSTGRES_PASSWORD"),
    "tg_token": os.getenv("TELEGRAM_BOT_TOKEN"),
    "tg_chat_id": os.getenv("TELEGRAM_CHAT_ID"),
}


def require(key):
    value = SETTINGS.get(key)

    if not value:
        raise RuntimeError(f"Missing config: {key}")

    return value