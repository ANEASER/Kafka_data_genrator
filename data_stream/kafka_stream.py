from datetime import datetime, timedelta
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
    
    while True:
        try:
            res = get_data()
            res = format_data(res)
            time.sleep(5)
            producer.send('time_values', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue



if __name__ == "__main__":
    stream_data()