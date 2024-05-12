
# Stream Data Generator

dockerized time series data generator  with random anomaly values and directly connected to kafka confluent broker
data capture part is airflow dag capture the kafka stream and write to txt file


## Features

- able to adjust normal value range
- able to adjust anomaly value range
- able to adjust anomaly frequency
- able to adjust kafka loading time




## Installation

To run genarator alone

```bash
  cd data_stream
  docker compose up -d
  python3 kafka_stream.py
```

To run data capture script

either can use airflow dag 
```bash
  cd data_capture
  docker compose up -d
```
or 
```bash
 python3 python_stream.py
```



## Customization

you can change the generator_parameters in kafka_stream.py please note to use integer value.
values json.

- nlb = normal value lower bound
- nub = normal value upper bound
- alb = anomaly value lower bound
- aub = anomaly value upper bound
- af = anomaly frequency max value is 1000

```python

genarator_parameters = {"nlb": 1, "nub": 100, "alb": 1, "aub": 10, "af": 25}

def get_data():
    res = requests.post("http://localhost:5000/stream/", json=genarator_parameters)
    res = res.json()
    return res
```

And also you can change the interval of value by customizing the sleep interval 

```python

if __name__ == "__main__":
    stream_data(2)

```
