package org.unece.cspa.square;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class AnalyseService {

    public static void main(final String... args) {
        System.out.println("[START]");
        String brokerURL = System.getenv("broker.url");
        System.out.println(String.format("Broker URL is %s / %s", brokerURL));
        SpringApplication.run(AnalyseService.class, args);
    }
}