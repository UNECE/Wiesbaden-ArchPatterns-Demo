# Containers demo

The idea is to illustrate the power of containers in the context of CSPA services.

# Components

A RabbitMQ broker, the dump pipes

A Python UI/rest, the triangles services

A Java service, consuming triangles and producing squares

A Javascript service, a CSPA service we want to integrate

All of them are Docker containers

# Questions

Should we stay on an abstract level or should we use more "statistical" services ?

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
