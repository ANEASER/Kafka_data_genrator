from datetime import datetime, timedelta
import json
import requests
import time
from kafka import KafkaProducer
import logging


"""
nlb = normal value lower bound
nub = normal value upper bound

alb = anomaly value lower bound
aub = anomaly value upper bound

af = anomaly frequency max value is 1000
"""

genarator_parameters = {"nlb": 1, "nub": 100, "alb": 1, "aub": 10, "af": 25}

def get_data():
    res = requests.post("http://localhost:5000/stream/", json=genarator_parameters)
    res = res.json()
    return res

def format_data(res):
    data = {}
    data["timestamp"] = res["timestamp"]
    data["value"] = res["random_value"]
    return data

def stream_data(sleeptime=5):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)
    
    while True:
        try:
            res = get_data()
            res = format_data(res)


            time.sleep(sleeptime) # Request data every 5 seconds


            producer.send('time_values', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue



if __name__ == "__main__":
    stream_data(2)