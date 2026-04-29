from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "khadija",
    "retries": 1,
}

with DAG(
    dag_id="botola_data_pipeline",
    default_args=default_args,
    description="Football data engineering pipeline for Botola Pro",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["data-engineering", "football", "botola"],
) as dag:

    extract_data = BashOperator(
        task_id="extract_data_from_api",
        bash_command="cd /opt/airflow/project && python src/fetch_data.py",
    )

    clean_data = BashOperator(
        task_id="clean_and_transform_data",
        bash_command="cd /opt/airflow/project && python src/clean_data.py",
    )

    load_postgres = BashOperator(
        task_id="load_clean_data_to_postgres",
        bash_command="cd /opt/airflow/project && python src/load_to_postgres.py",
    )

    extract_data >> clean_data >> load_postgres