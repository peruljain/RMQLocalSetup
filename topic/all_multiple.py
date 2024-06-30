#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic', exchange_type='topic')

result = channel.queue_declare(queue='all_queue', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='topic', queue=queue_name, routing_key = '#')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()