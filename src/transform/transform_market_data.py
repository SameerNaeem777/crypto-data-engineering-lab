import os
import pandas as pd

from src.extract.fetch_market_data import fetch_all_markets
from src.utils.logger import logger


def transform_market_data():

    logger.info("Starting Data Transformation")

    data = fetch_all_markets()

    df = pd.DataFrame(data)

    columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
        "price_change_percentage_24h",
        "last_updated",
    ]

    df = df[columns]

    os.makedirs("data/raw", exist_ok=True)

    output_file = "data/raw/market_data.csv"

    df.to_csv(output_file, index=False)

    logger.info(f"CSV saved to {output_file}")

    print(df.head())

    print(f"\n✅ CSV saved successfully: {output_file}")

    return df


if __name__ == "__main__":
    transform_market_data()