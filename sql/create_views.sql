-- ==========================================
-- Create Dashboard View
-- ==========================================

CREATE OR REPLACE VIEW vw_market_dashboard AS

SELECT
    id,
    name,
    symbol,
    current_price,
    market_cap,
    market_cap_rank,
    total_volume,
    price_change_percentage_24h,
    extracted_at,
    last_updated

FROM market_data;