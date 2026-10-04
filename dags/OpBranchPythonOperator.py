from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

def task_a():
    print("Tâche A exécutée")

def choisir_chemin():
    valeur = 5  # condition simple pour l'exemple

    if valeur > 10:
        return "task_b"
    else:
        return "task_c"

def task_b():
    print("Tâche B exécutée")

def task_c():
    print("Tâche C exécutée")

with DAG(
    dag_id="condition_a_b_c_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    A = PythonOperator(
        task_id="task_a",
        python_callable=task_a
    )

    branche = BranchPythonOperator(
        task_id="choix_condition",
        python_callable=choisir_chemin
    )

    B = PythonOperator(
        task_id="task_b",
        python_callable=task_b
    )

    C = PythonOperator(
        task_id="task_c",
        python_callable=task_c
    )

    A >> branche
    branche >> [B, C]