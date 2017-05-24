FROM frolvlad/alpine-python3

MAINTAINER romaintailhurat

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app.py /app/
COPY ./templates/index.html /app/templates/index.html

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
