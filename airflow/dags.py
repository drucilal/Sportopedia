from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Constructing default arguments:

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'end_date': datetime(2020,07,01),
    'depends_on_past': False,
    'email': ['lefevre.drucila@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}