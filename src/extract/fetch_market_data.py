import requests

from src.utils.config import SETTINGS


def fetch_markets(vs="usd", per_page=250, page=1):
    url = f"{SETTINGS['api_base_url']}/coins/markets"

    params = {
        "vs_currency": vs,
        "per_page": per_page,
        "page": page,
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json()


def fetch_all_markets(vs="usd", max_pages=1):

    all_coins = []

    for page in range(1, max_pages + 1):

        print(f"Fetching page {page}...")

        coins = fetch_markets(
            vs=vs,
            per_page=250,
            page=page,
        )

        if not coins:
            break

        all_coins.extend(coins)

    return all_coins


if __name__ == "__main__":

    data = fetch_all_markets()

    print(f"\n✅ Total Coins Fetched: {len(data)}")

    first = data[0]

    print("\nFirst Coin:")
    print(first["name"], "-", first["symbol"].upper())