# Containers demo

The idea is to illustrate the power of containers in the context of CSPA services.

# Components

A RabbitMQ broker, providing a communication for the services.

A collection service, providing the questionnnaire.

A process service, that implements the validation logic.

An analyse service, aggregating data and pushing it to the disseminate service.

The disseminate service is displaying the final product. It exists in two version.

# Demo central

All in one

```bash
docker-compose -f docker-compose.yml up -d
docker-compose stop
docker stop $(docker ps -a -q)
docker-compose -f docker-compose-new.yml up -d
```

Starting the first system:

```bash
docker-compose -f docker-compose.yml up -d
```

Stopping:

```bash
docker-compose stop
```

Then, check if all containers are **stopped** and if not act:

```bash
docker ps
docker stop $(docker ps -a -q)
```

Starting the second system:

```bash
docker-compose -f docker-compose-new.yml up -d
```

# Starting the containers

To start the main system, via the docker-compose.yml:

```bash
docker-compose up
```

To rebuild images using compose:

```bash
docker-compose build
```

Or in one go:

```bash
docker-compose build && docker-compose up
```

## Network

Service are reachable on the docker compose network by their compose id.

For example, the broker is declare as:

```yaml
services:
  broker:
```

in the compose file, and so is reached via the Python API like:

```python
connection = pika.BlockingConnection(pika.ConnectionParameters(host="broker"))
```
