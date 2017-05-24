#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import pika
import sys
import json
from datetime import datetime

FLAGS = { "BROKER_ON": False }

app = Flask(__name__)

# Simple stupid memory storage
tempStore = []

@app.route("/")
def home():
    return render_template("index.html", timestamp=datetime.now())

@app.route("/events", methods=["GET"])
def getEvents():
    return jsonify(tempStore)

@app.route("/events", methods=["POST"])
def pushEvents():
    payload = request.data
    tempStore.append(json.loads(payload))
    return jsonify({"status":"message received"})

if FLAGS["BROKER_ON"]:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='triangles', type='fanout')
    message = "shape: Triangle!"
    channel.basic_publish(exchange='triangles', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()
