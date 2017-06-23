import amqp from "amqplib/callback_api";
import express from "express";
import process from "./process";
import send from "./send";

const port = 3000;
const app = express();

/* Handling connection to the broker, both for sending and receiving messages */
const connectToBroker = () => {
  //FIXME connection URL should be given by the environnement
  amqp.connect("amqp://broker:5672", (err, conn) => {
    console.log("Connecting to broker");
    conn.createChannel(function(err, ch) {
      let ex = "collect-channel";
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
            console.log(" [x] Message to process: %s", msg.content.toString());
            let modifiedQuestionnaire = process(msg.content);
            send(conn, modifiedQuestionnaire);
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

app.listen(port, () => {
  console.log(`Service running on ${port}`);
  // We need to wait for the broker to accept connection
  setTimeout(() => {
    connectToBroker();
  }, 10000);
});
