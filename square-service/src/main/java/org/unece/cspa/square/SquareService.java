package org.unece.cspa.square;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class SquareService {
    public static void main(final String... args) {
        System.out.println("[START]");
        SpringApplication.run(SquareService.class, args);
    }
}