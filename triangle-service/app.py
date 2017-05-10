#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='triangles',
                         type='fanout')

message = "shape: Triangle!"
channel.basic_publish(exchange='triangles',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
