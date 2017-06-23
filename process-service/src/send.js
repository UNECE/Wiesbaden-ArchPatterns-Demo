import amqp from "amqplib/callback_api";

// PORT :5672

const send = (connection, questionnaire) => {
    console.log(connection);
    connection.createChannel((err, channel) => {
      if (err) {
        console.error("Error when creating a channel", err);
      }
      let exchange = "process-channel";
      channel.assertExchange(exchange, "fanout", { durable: false });
      channel.publish(exchange, "", new Buffer(questionnaire));
      console.log("New questionnaire send to process channel", questionnaire);
    });
};

export default send;
