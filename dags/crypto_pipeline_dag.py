from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def run_pipeline():
    from src.load import load_data
    load_data()


with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    catchup=False
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_crypto_pipeline",
        python_callable=run_pipeline
    )