from confluent_kafka import Consumer


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup3',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['statewise-earning'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()