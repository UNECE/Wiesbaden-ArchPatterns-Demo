import amqp from "amqplib/callback_api";

// PORT :5672

const send = (connection, questionnaire) => {
  connection.createChannel((err, channel) => {
    if (err) {
      console.error("Error when creating a channel", err);
    }
    let exchange = "analyse-channel";
    channel.assertExchange(exchange, "fanout", { durable: false });
    channel.publish(exchange, "", new Buffer(JSON.stringify(questionnaire)));
    console.log(
      "New questionnaire send to analyse channel",
      JSON.stringify(questionnaire)
    );
  });
};

export default send;
