#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

for i in range(1,10):
    message = "Hello World!" + str(i)
    for j in range(1,i):
        message = message + "."
    channel.basic_publish(exchange='',
                      routing_key='work_queue',
                      body=message)
    print(f" [x] Sent {message}")

connection.close()

