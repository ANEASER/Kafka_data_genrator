from confluent_kafka import Consumer, KafkaError

bootstrap_servers = 'localhost:9092'
group_id = 'test_group'
topic = 'time_values'

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'  # Start consuming from the earliest message
}


def push_to_db():

    while True:
        consumer = Consumer(conf)
        consumer.subscribe([topic])
        msg = consumer.poll(timeout=1.0)  # Timeout in seconds
        
        file_path = './time_values.txt'

        if msg is not None:
            with open(file_path, 'a') as file:
                file.write(msg.value().decode('utf-8') + '\n')
        consumer.close()


push_to_db()