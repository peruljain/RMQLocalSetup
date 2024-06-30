#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

for i in range(1,10):
    message = 'Hello World!-' + str(i)
    channel.basic_publish(exchange='',
                        routing_key='perul-test',
                        body=message)
    print(" [x] Sent " + message)

connection.close()