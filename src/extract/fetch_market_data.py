import time
import requests

from src.utils.config import SETTINGS
from src.utils.logger import logger


def fetch_markets(vs="usd", per_page=250, page=1):
    url = f"{SETTINGS['api_base_url']}/coins/markets"

    params = {
        "vs_currency": vs,
        "per_page": per_page,
        "page": page,
    }

    retries = 3

    for attempt in range(retries):

        try:
            response = requests.get(
                url,
                params=params,
                timeout=20,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError:

            if response.status_code == 429:
                logger.warning(
                    f"Rate limit reached. Waiting 2 seconds... ({attempt + 1}/{retries})"
                )
                time.sleep(2)
                continue

            raise

        except requests.exceptions.RequestException:
            logger.warning(
                f"Network error. Retrying... ({attempt + 1}/{retries})"
            )
            time.sleep(2)

    raise Exception("Failed to fetch data after 3 retries.")


def fetch_all_markets(vs="usd", max_pages=1):

    all_coins = []

    for page in range(1, max_pages + 1):

        logger.info(f"Fetching page {page}")

        coins = fetch_markets(
            vs=vs,
            per_page=250,
            page=page,
        )

        if not coins:
            logger.warning(f"No data returned on page {page}")
            break

        all_coins.extend(coins)

        logger.info(f"Fetched {len(coins)} coins from page {page}")

        # CoinGecko free API ko spam na karein
        time.sleep(1)

    logger.info(f"Total coins fetched: {len(all_coins)}")

    return all_coins


if __name__ == "__main__":

    data = fetch_all_markets()

    print(f"\n✅ Total Coins Fetched: {len(data)}")

    if data:
        first = data[0]

        print("\nFirst Coin")
        print("=" * 40)
        print(f"Name          : {first['name']}")
        print(f"Symbol        : {first['symbol'].upper()}")
        print(f"Price         : ${first['current_price']:,}")
        print(f"Market Cap    : ${first['market_cap']:,}")
        print(f"Rank          : {first['market_cap_rank']}")
        print(f"24h Change    : {first['price_change_percentage_24h']}%")
        print("=" * 40)