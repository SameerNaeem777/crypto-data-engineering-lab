def validate_coin(coin):

    required_fields = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
    ]

    for field in required_fields:

        if field not in coin:
            return False

        if coin[field] is None:
            return False

    return True