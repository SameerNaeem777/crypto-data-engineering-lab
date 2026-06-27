from src.extract.fetch_market_data import fetch_markets
from src.load.db_connection import get_connection


def load_market_data():

    data = fetch_markets()

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO market_data (
        coin_id,
        symbol,
        name,
        current_price,
        market_cap,
        market_cap_rank,
        total_volume
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for coin in data:

        cursor.execute(
            query,
            (
                coin["id"],
                coin["symbol"],
                coin["name"],
                coin["current_price"],
                coin["market_cap"],
                coin["market_cap_rank"],
                coin["total_volume"],
            ),
        )

    conn.commit()

    print(f"✅ Inserted {len(data)} records into PostgreSQL")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_market_data()