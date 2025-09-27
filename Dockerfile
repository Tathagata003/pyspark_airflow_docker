FROM apache/airflow:3.1.0-python3.11

USER root
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository 'deb http://deb.debian.org/debian bullseye main' && \
    apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON=/opt/bitnami/python/bin/python3.11
ENV PYSPARK_DRIVER_PYTHON=/opt/bitnami/python/bin/python3.11
ENV SPARK_HOME=/opt/bitnami/spark
# ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

USER airflow

RUN pip install --no-cache-dir apache-airflow apache-airflow-providers-apache-spark pyspark==3.5.1