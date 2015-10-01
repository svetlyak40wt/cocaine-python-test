FROM ubuntu:precise

RUN apt-get update && apt-get install -y python-pip
RUN pip install https://github.com/cocaine/cocaine-framework-python/archive/v0.12.zip?rnd=2

ADD . /app
