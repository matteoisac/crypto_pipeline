from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def run_pipeline():
    from src.load import load_data
    load_data()


def export_pipeline():
    from src.export import export_to_csv, upload_to_s3

    export_to_csv()
    upload_to_s3()


def redshift_pipeline():
    from src.redshift import load_to_redshift
    load_to_redshift()


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

    export_to_s3_task = PythonOperator(
        task_id="export_to_s3",
        python_callable=export_pipeline
    )

    load_to_redshift_task = PythonOperator(
        task_id="load_to_redshift",
        python_callable=redshift_pipeline
    )

    run_pipeline_task >> export_to_s3_task >> load_to_redshift_task