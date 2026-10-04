from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def detect_duplicates():
    numbers = [10, 20, 30, 20, 40, 10, 50]

    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    print("Doublons détectés :", duplicates)


with DAG(
    dag_id="detect_duplicates_dag",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
) as dag:

    detect_task = PythonOperator(
        task_id="detect_duplicates",
        python_callable=detect_duplicates
    )