CREATE TABLE market_data (

    id BIGSERIAL PRIMARY KEY,

    coin_id VARCHAR(50) NOT NULL,

    symbol VARCHAR(20) NOT NULL,

    name VARCHAR(100) NOT NULL,

    current_price NUMERIC(18,8),

    market_cap BIGINT,

    market_cap_rank INTEGER,

    total_volume BIGINT,

    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);