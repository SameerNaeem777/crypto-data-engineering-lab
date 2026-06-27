SELECT
    name,
    symbol,
    current_price,
    price_change_percentage_24h
FROM market_data
ORDER BY price_change_percentage_24h DESC
LIMIT 10;