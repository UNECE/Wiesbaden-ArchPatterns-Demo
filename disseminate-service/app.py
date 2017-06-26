from flask import Flask, render_template
import os
import pika
import time

app = Flask(__name__)

# ----- DATA
class FinalProduct():
    """
    Use to handle aggregate data from the analyse service
    """
    def __init__(self):
        self.data = { "some": "data structure" }

finalProduct = FinalProduct()



# ----- Routes definition
@app.route("/")
def home():
    return render_template("index.html", product=finalProduct)

if __name__ == "__main__":
    print("Broker URL is:" + os.environ["broker.url"])
    print("Waiting a few seconds for broker to be ready")
    time.sleep(7)
    print("Finish waiting, connecting to broker")
    # ----- Broker connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(os.environ["broker.url"])))
    channel = connection.channel()
    channel.exchange_declare(exchange='analyse-channel', type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='analyse-channel', queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()
    app.run(debug=False, host="0.0.0.0", port=2000)
