#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import pika
import sys
import json
from datetime import datetime
import os

FLAGS = { "BROKER_ON": False }

app = Flask(__name__)

# Simple stupid memory storage
tempStore = []

@app.route("/")
def home():
    return render_template("index.html", timestamp=datetime.now())

@app.route("/info")
def info():
    infos = {
        "brokerUrl": os.environ["broker.url"]
    }
    return jsonify(infos)

@app.route("/events", methods=["GET"])
def getEvents():
    return jsonify(tempStore)

@app.route("/events", methods=["POST"])
def pushEvents():
    payload = request.data.decode("UTF-8")
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

if __name__ == "__main__":
    print("Broker URL is:" + os.environ["broker.url"])
    app.run(debug=False, host="0.0.0.0")
