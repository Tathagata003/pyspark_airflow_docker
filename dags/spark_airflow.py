from airflow import DAG
import airflow
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id="spark_airflow_integration",
    default_args={
        "owner": "tathagata das",
        "start_date": airflow.utils.dates.days_ago(1),
    },
    schedule_interval="@daily"
)


start = PythonOperator(
    task_id="start",
    python_callable=lambda: print("DAG started"),
    dag=dag
)

# python_job = SparkSubmitOperator(
#     task_id="spark_submit",
#     application="jobs/wordcountjob.py",  # Path to your Spark application
#     conn_id="spark_conn",
#     dag=dag
# )
run_spark = BashOperator(
    task_id='spark-submit',
    bash_command='spark-submit --master spark://spark-master:7077 /opt/airflow/jobs/wordcountjob.py',
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable=lambda: print("DAG ended"),
    dag=dag
)

start>> run_spark >> end