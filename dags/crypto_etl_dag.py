from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "sameer",
}

with DAG(
    dag_id="crypto_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 6, 27),
    schedule="@hourly",
    catchup=False,
) as dag:

    run_pipeline = BashOperator(
        task_id="run_crypto_pipeline",
        bash_command="cd /opt/airflow/project && python run_pipeline.py",
    )