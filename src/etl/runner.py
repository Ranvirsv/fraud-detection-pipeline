from loader import Loader
from loguru import logger
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    root_dir = os.getenv("PROJECT_ROOT")
    
    logger.info("Starting ETL pipeline")
    loader = Loader(root_dir)
    loader.load_to_duckdb()
    df = loader.load_transactions()
    logger.info("ETL pipeline completed")

    df.to_parquet(f"{root_dir}/data/processed/analytical.parquet", index=False)