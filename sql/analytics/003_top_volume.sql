SELECT
    name,
    symbol,
    total_volume
FROM market_data
ORDER BY total_volume DESC
LIMIT 10;