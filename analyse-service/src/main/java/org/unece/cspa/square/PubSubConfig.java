package org.unece.cspa.square;

import org.springframework.amqp.core.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Profile({"pub-sub"})
@Configuration
public class PubSubConfig {

    @Bean
    public FanoutExchange fanout() {
        return new FanoutExchange("cspa.square");
    }

    @Bean
    public FinalProductSender sender() {
        return new FinalProductSender();
    }

    @Bean
    public Queue autoDeleteQueue() {
        return new AnonymousQueue();
    }

    @Bean
    public Binding binding(FanoutExchange fanout, Queue autoDeleteQueue) {
        return BindingBuilder.bind(autoDeleteQueue).to(fanout);
    }
}
