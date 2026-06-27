from src.load.load_market_data import load_market_data
from src.utils.logger import logger

def run_pipeline():
    logger.info("========== CRYPTO ETL PIPELINE STARTED ==========")

    load_market_data()

    logger.info("========== CRYPTO ETL PIPELINE FINISHED ==========")

if __name__ == "__main__":
    run_pipeline()