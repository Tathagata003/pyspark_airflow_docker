from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "tathagata das",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="spark_airflow_integration",
    default_args=default_args,
    description="A DAG to run PySpark jobs",
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 27),
    catchup=False,
    tags=["spark", "example"]
) as dag:

    start = PythonOperator(
        task_id="start",
        python_callable=lambda: print("DAG started")
    )

    run_spark = SparkSubmitOperator(
        task_id="spark_submit",
        application="/jobs/wordcountjob.py", 
        conn_id="spark_conn",
        verbose=True
    )

    end = PythonOperator(
        task_id="end",
        python_callable=lambda: print("DAG ended")
    )

    # Set task dependencies
    start >> run_spark >> end
