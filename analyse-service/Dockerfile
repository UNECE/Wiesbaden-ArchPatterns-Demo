FROM maven:3

WORKDIR /app

COPY ./src /app/src
COPY ./pom.xml /app

RUN mvn clean package

CMD ["java", "-jar", "/app/target/analyse-service-0.0.1.jar"]
