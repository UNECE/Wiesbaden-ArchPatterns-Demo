import amqp from "amqplib/callback_api";
import express from "express";
import process from "./process";
import send from "./send";

const port = 4000;
const listenerTimeout = 7000;
const app = express();

/* Handling connection to the broker, both for sending and receiving messages */
const connectToBroker = () => {
  //FIXME connection URL should be given by the environnement
  amqp.connect("amqp://broker:5672", (err, conn) => {
    console.log("Connecting to broker");
    conn.createChannel(function(err, ch) {
      let ex = "process-channel";
      ch.assertExchange(ex, "fanout", { durable: false });
      ch.assertQueue("", { exclusive: true }, (err, q) => {
        console.log(
          " [*] Waiting for messages in %s.",
          q.queue
        );
        ch.bindQueue(q.queue, ex, "");
        ch.consume(
          q.queue,
          (msg) => {
            let rawMessageJSON = JSON.parse(msg.content.toString());
            console.log(" [x] Message to analyse: %s", rawMessageJSON.toString());
            let finalProduct = process(rawMessageJSON.questionnaire);
            send(conn, finalProduct);
          },
          { noAck: true }
        );
      });
    });
  });
};

app.get("/", (req, res) => {
  res.send("hello from analyse service");
});

app.listen(port, () => {
  console.log(`Analyse service running on ${port}`);
  // We need to wait for the broker to accept connection
  setTimeout(() => {
    connectToBroker();
  }, listenerTimeout);
});
