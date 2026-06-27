import requests

from src.utils.config import SETTINGS


def fetch_markets(vs="usd", per_page=10):
    url = f"{SETTINGS['api_base_url']}/coins/markets"

    params = {
        "vs_currency": vs,
        "per_page": per_page,
        "page": 1,
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    data = fetch_markets()

    print(f"\n✅ Fetched {len(data)} coins\n")

    first = data[0]

    print("=" * 50)
    print("FIRST COIN DETAILS")
    print("=" * 50)

    print(f"Coin Name     : {first['name']}")
    print(f"Symbol        : {first['symbol'].upper()}")
    print(f"Price         : ${first['current_price']:,}")
    print(f"Market Cap    : ${first['market_cap']:,}")
    print(f"24h Change    : {first['price_change_percentage_24h']}%")
    print(f"Rank          : {first['market_cap_rank']}")
    print(f"ATH           : ${first['ath']:,}")
    print(f"ATL           : ${first['atl']}")
    print(f"Last Updated  : {first['last_updated']}")