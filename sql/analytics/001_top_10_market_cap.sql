SELECT
    name,
    symbol,
    current_price,
    market_cap,
    market_cap_rank
FROM market_data
ORDER BY market_cap DESC
LIMIT 10;