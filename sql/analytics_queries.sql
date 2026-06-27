-- ==========================================
-- Analytics Queries
-- ==========================================

-- 1. View all market data
SELECT *
FROM market_data;

------------------------------------------------

-- 2. Top 10 most expensive coins

SELECT
    name,
    symbol,
    current_price
FROM market_data
ORDER BY current_price DESC
LIMIT 10;

------------------------------------------------

-- 3. Top 10 by Market Cap

SELECT
    name,
    market_cap
FROM market_data
ORDER BY market_cap DESC
LIMIT 10;

------------------------------------------------

-- 4. Highest Trading Volume

SELECT
    name,
    total_volume
FROM market_data
ORDER BY total_volume DESC
LIMIT 10;

------------------------------------------------

-- 5. Biggest Gainers (24 Hours)

SELECT
    name,
    price_change_percentage_24h
FROM market_data
ORDER BY price_change_percentage_24h DESC
LIMIT 10;

------------------------------------------------

-- 6. Biggest Losers (24 Hours)

SELECT
    name,
    price_change_percentage_24h
FROM market_data
ORDER BY price_change_percentage_24h ASC
LIMIT 10;

------------------------------------------------

-- 7. Coins Above $1000

SELECT
    name,
    current_price
FROM market_data
WHERE current_price > 1000
ORDER BY current_price DESC;

------------------------------------------------

-- 8. Total Crypto Market Cap

SELECT
    SUM(market_cap) AS total_market_cap
FROM market_data;

------------------------------------------------

-- 9. Average Coin Price

SELECT
    ROUND(AVG(current_price),2) AS average_price
FROM market_data;

------------------------------------------------

-- 10. Total Number of Coins

SELECT
    COUNT(*) AS total_coins
FROM market_data;