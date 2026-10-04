from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def hello_world():
    print("Hello World")

with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(seconds=5),
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="print_hello_world",
        python_callable=hello_world
    )