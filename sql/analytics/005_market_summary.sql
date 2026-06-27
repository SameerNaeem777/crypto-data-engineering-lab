SELECT
    COUNT(*) AS total_coins,
    MAX(current_price) AS highest_price,
    MIN(current_price) AS lowest_price,
    SUM(market_cap) AS total_market_cap
FROM market_data;