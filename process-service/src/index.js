import amqp from "amqplib/callback_api";
import express from "express";
import process from "./process";

const port = 3000;
const app = express();

/* Handling connection to the broker, both for sending and receiving messages */
const connectToBroker = () => {
  amqp.connect("amqp://broker:5672", (err, conn) => {
    console.log("Connecting to broker");
    conn.createChannel(function(err, ch) {
      var ex = "collect-channel";
      ch.assertExchange(ex, "fanout", { durable: false });
      ch.assertQueue("", { exclusive: true }, function(err, q) {
        console.log(
          " [*] Waiting for messages in %s.",
          q.queue
        );
        ch.bindQueue(q.queue, ex, "");
        ch.consume(
          q.queue,
          function(msg) {
            console.log(" [x] Message to process: %s", msg.content.toString());
            //process(msg.content);
          },
          { noAck: true }
        );
      });
    });
  });
};

app.get("/", (req, res) => {
  res.send("hello from process service");
});

app.get("/activate", (req, res) => {
  res.send("Trying to grab messages");
});

app.listen(port, () => {
  console.log(`Service running on ${port}`);
  setTimeout(() => {
    connectToBroker();
  }, 10000);
});
