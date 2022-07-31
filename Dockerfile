FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY supersecretkeywithsalt)

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev musl-dev
RUN apk update && apk add libpq jpeg-dev zlib-dev libjpeg

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir /school
WORKDIR /school
COPY school /school

RUN adduser -D user

USER user