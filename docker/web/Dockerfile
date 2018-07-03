FROM ubuntu:latest
MAINTAINER Anton Khromov 'jetneitrino@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
RUN rm /requirements.txt
