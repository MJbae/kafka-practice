import json
from kafka import KafkaProducer

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('quickstart-events', value={'foo': 'bar'})
producer.flush()
