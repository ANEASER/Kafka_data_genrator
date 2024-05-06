#!/bin/bash

set -e

if [ -e "/opt/airflow/requirements.txt" ]; then
    pip install --user -r /opt/airflow/requirements.txt
fi

if [ ! -f "/opt/airflow/airflow.db" ]; then
    airflow db init && \
    airflow users create \
        --username admin \
        --firstname admin \
        --lastname admin \
        --role Admin \
        --email admin@abc.com \
        --password admin
fi

airflow db migrate

exec airflow webserver
