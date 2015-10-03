FROM ubuntu:precise

RUN apt-get update && apt-get install git python-flask msgpack-python python-pip -y
RUN pip install git+git://github.com/cocaine/cocaine-framework-python

COPY . /app
