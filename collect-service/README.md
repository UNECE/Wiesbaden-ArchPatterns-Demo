# Collect service

This simple service collect information.

## Run

### With pipenv:

```bash
FLASK_APP=app.py pipenv run flask run
```

or

```bash
pipenv run python3 app.py
```

### With Docker:

Before the build, generate the `requirements.txt` with:

```bash
pipenv install --requirements > requirements.txt
```

Then, build the Docker image:

```bash
docker build -t romaintailhurat/cspa-triangle-service .
```

And run it:

```bash
docker run -d -p 5000:5000 romaintailhurat/cspa-triangle-service
```
