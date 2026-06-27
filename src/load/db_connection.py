import psycopg2
from src.utils.config import SETTINGS


def get_connection():
    return psycopg2.connect(
        host="postgres",
        port=5432,
        database="crypto_lab",
        user="postgres",
        password=SETTINGS["pg_password"]
    )


if __name__ == "__main__":
    conn = get_connection()
    print("✅ Database Connected Successfully!")
    conn.close()