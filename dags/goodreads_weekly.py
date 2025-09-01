from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def fetch_and_land(**_):
    # Implement on Day 5
    return "ok"

with DAG(
    dag_id="goodreads_weekly",
    start_date=datetime(2024, 1, 1),
    schedule="0 6 * * 1",  # Mondays 06:00 UTC
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)},
    tags=["goodreads","ingest"],
    doc_md="""
    # Goodreads weekly ingest
    Day 1 skeleton; real work lands Day 5.
    """
):
    start = EmptyOperator(task_id="start")
    extract = PythonOperator(task_id="fetch_and_land", python_callable=fetch_and_land)
    end = EmptyOperator(task_id="end")
    start >> extract >> end
