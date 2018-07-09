FROM ubuntu:latest
MAINTAINER Anton Khromov 'jetneitrino@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY requirements.txt /requirements.txt
ADD . /app
RUN pip3 install -r requirements.txt
RUN rm /requirements.txt
WORKDIR /app
ENV DATABASE_URL=postgresql://admin:12345678@db/otus_db
ENV HOME /app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=/app/flask_app.py