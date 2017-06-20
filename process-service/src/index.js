import amqp from "amqplib/callback_api"
import express from "express"

const port = 3000;
const app = express()

app.get("/", (req, res) => {
  res.send("hello from process service");
});

app.listen(port, () => {
  console.log(`Service running on ${port}`);
});
