from flask import Flask, Response
import random
import time
import json

app = Flask(__name__)

def generate_random_value():
    base_value = random.randint(1, 100)  # Generate a random integer between 1 and 100
    return base_value

def add_random_offset(value):
    return value + random.randint(500, 1000)


@app.route('/')
def generate_data():
    random_value = generate_random_value()
    if random.randint(0, 100) == 1:  # Add random offset with 50% probability
        random_value = add_random_offset(random_value)
    timestamp = int(time.time())  # Get the current timestamp
    data = {'timestamp': timestamp, 'random_value': random_value}
    json_data = json.dumps(data)
    return json_data
