FROM debian:jessie-slim
MAINTAINER Scalr <@scalr.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends python python-dev python-pip uwsgi uwsgi-plugin-python && \
    groupadd uwsgi && \
    useradd -g uwsgi uwsgi

COPY ./requirements.txt /opt/command-webhook/

RUN pip install -r /opt/command-webhook/requirements.txt

COPY . /opt/command-webhook

EXPOSE 5018

CMD ["/usr/bin/uwsgi", "--ini", "/opt/command-webhook/uwsgi.ini", "--logto2", "/var/log/webhook/webhook.log"]
