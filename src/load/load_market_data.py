from src.extract.fetch_market_data import fetch_all_markets
from src.load.db_connection import get_connection
from src.validate.validate_market_data import validate_coin
from src.utils.logger import logger


def load_market_data():

    logger.info("Starting ETL Pipeline...")

    data = fetch_all_markets()

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
    ON CONFLICT (coin_id)
    DO NOTHING;
    """

    rows = []

    for coin in data:

        if not validate_coin(coin):
            logger.warning(f"Invalid record skipped: {coin.get('id', 'Unknown')}")
            continue

        rows.append(
            (
                coin["id"],
                coin["symbol"],
                coin["name"],
                coin["current_price"],
                coin["market_cap"],
                coin["market_cap_rank"],
                coin["total_volume"],
            )
        )

    cursor.executemany(query, rows)

    conn.commit()

    logger.info(f"Processed {len(data)} coins")
    logger.info(f"Inserted/Checked {len(rows)} records")
    logger.info("ETL Pipeline Completed Successfully")

    print(f"\n✅ Processed {len(data)} coins")
    print(f"✅ Inserted/Checked {len(rows)} records")
    print("✅ ETL Pipeline Completed Successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_market_data()