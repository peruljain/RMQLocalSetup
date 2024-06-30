#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type='direct')


for i in range(1,10):
    message = "Hello World!" + str(i)
    for j in range(1,i):
        message = message + "."
    routing_key = ''
    if i%2 == 0:
       routing_key = 'even'
    else:
       routing_key = 'odd'  
    
    channel.basic_publish(exchange='routing', routing_key=routing_key, body=message)
    print(f" [x] Sent {message}")

connection.close()