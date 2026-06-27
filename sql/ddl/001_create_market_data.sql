DROP TABLE IF EXISTS market_data;

CREATE TABLE market_data (

    id BIGSERIAL PRIMARY KEY,

    coin_id VARCHAR(255) UNIQUE NOT NULL,

    symbol VARCHAR(50) NOT NULL,

    name VARCHAR(255) NOT NULL,

    current_price NUMERIC(18,8),

    market_cap BIGINT,

    market_cap_rank INTEGER,

    total_volume BIGINT,

    price_change_percentage_24h NUMERIC,

    last_updated TIMESTAMP,

    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);