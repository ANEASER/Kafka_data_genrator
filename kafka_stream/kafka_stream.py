from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests
import time
from kafka import KafkaProducer
import logging


def get_data():
    res = requests.get("http://localhost:5000/")
    res = res.json()
    return res

def format_data(res):
    data = {}
    data["timestamp"] = res["timestamp"]
    data["value"] = res["random_value"]
    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)
    curr_time = time.time()
    
    while True:
        if time.time() > curr_time + 180: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)
            time.sleep(5)
            producer.send('time_values', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue



stream_data()