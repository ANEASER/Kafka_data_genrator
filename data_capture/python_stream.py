from confluent_kafka import Consumer, KafkaError
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests
import time
from datetime import datetime

bootstrap_servers = 'localhost:9092'
group_id = 'test_group'
topic = 'time_values'

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'  
}

default_args = {
    'owner': 'anuda',
    'start_date': datetime(2023, 5, 5),
}


def push_to_db():
    consumer = Consumer(conf)
    consumer.subscribe([topic])
    file_path = './time_values.txt'

    with open(file_path, 'a') as file:
                file.write('Starting to capture data\n')

    while True:
        msg = consumer.poll(timeout=1.0)  
        
        
        if msg is not None:
            print(msg.value().decode('utf-8'))
            with open(file_path, 'a') as file:
                file.write(msg.value().decode('utf-8') + '\n')
        else:
            print('No message')

    consumer.close()


push_to_db()