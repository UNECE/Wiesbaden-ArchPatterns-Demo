package org.unece.cspa.square;

import org.springframework.amqp.core.FanoutExchange;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;

public class FinalProductSender {

    private static final String MESSAGE = "This is a square";

    @Autowired
    private RabbitTemplate template;

    @Autowired
    private FanoutExchange fanout;

    @Scheduled(fixedDelay = 1000, initialDelay = 500)
    public void send() {
        System.out.println("Sending a message to " + fanout.getName());
        template.convertAndSend(fanout.getName(), "", MESSAGE);
    }
}
