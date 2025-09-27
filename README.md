## ABOUT

This project orchestrates Spark jobs written in `PYTHON` using Apache Airflow, all within a Dockerized environment. The DAG `spark_airflow_integration` is designed to submit Spark jobs written in Python ensuring that data processing is handled efficiently and reliably on a daily schedule.

#

**RUN**

Start the docker desktop and run the following in the parent directory of the project:
```bash
docker-compose up -d --build
```

## Airflow UI
Log in to the airflow UI using the password from the docker terminal. 

## Techstack
- Postgres: 14 
- Pyspark: 3.5.1
- Airflow: 3.1.0
- Python: 3.11

## Note

You must add the spark cluster url to the spark connection in the configuration on Airflow UI. 

Go to the Admin -> Connections in the Airflow UI and select the connection type `Spark` and the connection_id `spark_conn` as in the ./dags/spark_airflow.py
