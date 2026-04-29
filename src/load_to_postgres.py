import pandas as pd
from sqlalchemy import create_engine
import os

DB_URL = "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
engine = create_engine(DB_URL)

BASE_PATH = "/opt/airflow/project"

tables = {
    "standings_clean": f"{BASE_PATH}/data/clean/standings_clean.csv",
    "scorers_clean": f"{BASE_PATH}/data/clean/scorers_clean.csv",
    "fixtures_clean": f"{BASE_PATH}/data/clean/fixtures_clean.csv",
}

for table_name, file_path in tables.items():
    print(f"Loading {file_path}")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{table_name} loaded")

print("All clean data loaded successfully.")