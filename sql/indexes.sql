-- ==========================================
-- Performance Indexes
-- ==========================================

CREATE INDEX IF NOT EXISTS idx_market_symbol
ON market_data(symbol);

CREATE INDEX IF NOT EXISTS idx_market_cap
ON market_data(market_cap);

CREATE INDEX IF NOT EXISTS idx_current_price
ON market_data(current_price);

CREATE INDEX IF NOT EXISTS idx_market_rank
ON market_data(market_cap_rank);

CREATE INDEX IF NOT EXISTS idx_last_updated
ON market_data(last_updated);