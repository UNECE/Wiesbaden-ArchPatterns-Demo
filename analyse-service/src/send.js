import amqp from "amqplib/callback_api";
import request from "request";

// PORT :5672

const send = (connection, product) => {
  let url = process.env["disseminate.url"];
  // Send message to disseminate service
  request(
    {
      url: "http://"+ url +":5000/product",
      method: "PUT",
      json: product
    },
    (error, request, body) => {
      if (error) {
        console.log("Error", error);
      }
      console.log("OK");
    }
  );
  // Send message to broker
  connection.createChannel((err, channel) => {
    if (err) {
      console.error("Error when creating a channel", err);
    }
    let exchange = "analyse-channel";
    channel.assertExchange(exchange, "fanout", { durable: false });
    channel.publish(exchange, "", new Buffer(JSON.stringify(product)));
    console.log(
      "New questionnaire send to analyse channel",
      JSON.stringify(product)
    );
  });
};

export default send;
