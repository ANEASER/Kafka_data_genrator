from fastapi import FastAPI, Response,Request
import random
import time
import json
import requests
from pydantic import BaseModel

"""
nlb = normal value lower bound
nub = normal value upper bound

alb = anomaly value lower bound
aub = anomaly value upper bound

af = anomaly frequency
"""

class Values(BaseModel):
    nlb: int
    nub: int
    alb: int
    aub: int
    af: int



app = FastAPI()

def generate_random_value(nlb, nub):
    base_value = random.randint(nlb, nub)  # Generate a random integer between 1 and 100
    return base_value

def add_random_offset(value, alb, aub):
    return value + random.randint(alb, aub)

@app.post('/stream/')
def generate_data_from_request(values: Values):
    
    values = values.dict()
    nlb = values["nlb"]
    nub = values["nub"]
    alb = values["alb"]
    aub = values["aub"]
    af = values["af"]
    
    random_value = generate_random_value(nlb, nub)

    anomalybound = 1000 // af
    
    if random.randint(0, anomalybound) == 1:  # Generate an anomaly value
        random_value = add_random_offset(random_value, alb, aub)
    timestamp = int(time.time())  # Get the current timestamp
    data = {'timestamp': timestamp, 'random_value': random_value}
    return data



@app.get('/')
def hello():
    return "This is the data generator service."
