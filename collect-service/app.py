#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import pika
import sys
import json
from datetime import datetime
import os

app = Flask(__name__)

# Simple stupid memory storage
tempStore = []

def sendMessageToBroker(message):
    # Broker connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(os.environ["broker.url"])))
    channel = connection.channel()
    channel.exchange_declare(exchange='collect-channel', type='fanout')
    channel.basic_publish(exchange='collect-channel', routing_key='', body=message)
    connection.close()

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
    questionnaire = json.loads(payload)
    tempStore.append(questionnaire)
    sendMessageToBroker(json.dumps(questionnaire))
    return jsonify({"status":"message received"})

if __name__ == "__main__":
    print("Broker URL is:" + os.environ["broker.url"])
    app.run(debug=False, host="0.0.0.0", port=2000)
