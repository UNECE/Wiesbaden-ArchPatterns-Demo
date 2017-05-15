#!/usr/bin/env python
from flask import Flask, render_template
import pika
import sys
from datetime import datetime

FLAGS = { "BROKER_ON": False }

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", timestamp=datetime.now())

if FLAGS["BROKER_ON"]:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='triangles', type='fanout')
    message = "shape: Triangle!"
    channel.basic_publish(exchange='triangles', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()
