
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

To run data captur script

either can use airflow dag 
```bash
  cd data_capture
  docker compose up -d
```
or 
```bash
 python3 python_stream.py
```
