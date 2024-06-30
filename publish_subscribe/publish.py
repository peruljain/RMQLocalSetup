#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')


for i in range(1,10):
    message = "Hello World!" + str(i)
    for j in range(1,i):
        message = message + "."
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(f" [x] Sent {message}")
connection.close()