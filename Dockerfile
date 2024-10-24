FROM python:3.11-alpine

RUN apk add --no-cache shadow

RUN useradd -ms /bin/bash admin

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


RUN chown -R admin /code/app/*

USER admin