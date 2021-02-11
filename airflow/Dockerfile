FROM ubuntu:20.04

ENV AIRFLOW_VERSION=1.10.10

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install apache-airflow==${AIRFLOW_VERSION} typing_extensions

RUN airflow initdb

CMD ["airflow", "webserver", "--hostname", "0.0.0.0", "--port", "8080"]