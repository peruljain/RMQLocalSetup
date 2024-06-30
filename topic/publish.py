#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic', exchange_type='topic')


for i in range(1,10):

    message = "Hello World!" + str(i)
    for j in range(1,i):
        message = message + "."
    routing_key = ''

    if i%2 == 0:
       routing_key = 'two.' + 'abc'
    elif i%3 == 0:
       routing_key = 'three.' + 'def'
    else:
       routing_key = 'all.'  + 'qwe'
    
    channel.basic_publish(exchange='topic', routing_key=routing_key, body=message)
    print(f" [x] Sent {message}")

connection.close()