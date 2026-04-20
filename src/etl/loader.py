import duckdb
import pandas as pd
from schemas import validate_schema
from loguru import logger
from pydantic import ValidationError
from tqdm import tqdm

class Loader: 
    def __init__(self, root_dir: str):
        db_path = f"{root_dir}/data/fraud_detection.duckdb"
        try:
            self.conn = duckdb.connect(database=db_path, read_only=False)
            logger.info("Connected to DuckDB")
        except Exception as e:
            logger.error(f"Error connecting to DuckDB: {e}")
        self.sql_path = f"{root_dir}/sql/build_warehouse.sql"
        
    def load_to_duckdb(self):
        try: 
            with open(self.sql_path, 'r') as f:
                sql_script = f.read()
            self.conn.execute(sql_script)
            logger.info("Successfully built the warehouse")
        except Exception as e:
            logger.error(f"Error building the warehouse: {e}")

    def load_transactions(self) -> pd.DataFrame:
        try:
            query = "Select * from fraud_transactions"
            fraud_df = self.conn.execute(query).fetchdf()
            records = fraud_df.to_dict(orient='records')

            logger.info(f"Loaded {len(records)} transactions")
        except Exception as e:
            logger.error(f"Error loading transactions: {e}")
            return pd.DataFrame()

        for i, record in enumerate(tqdm(records)):
            try:
                validate_schema(record)
            except ValidationError as e:
                logger.error(f"Validation Error at index {i}: {e}")

        return fraud_df