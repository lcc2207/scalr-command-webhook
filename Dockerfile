FROM debian:jessie-slim
MAINTAINER Scalr <@scalr.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends python python-dev python-pip uwsgi uwsgi-plugin-python && \
    groupadd uwsgi && \
    useradd -g uwsgi uwsgi

COPY ./requirements.txt /opt/webhook/

RUN pip install -r /opt/webhook/requirements.txt

COPY . /opt/webhook

CMD ["/usr/bin/uwsgi", "--ini", "/opt/webhook/uwsgi.ini", "--logto2", "/var/log/webhook/webhook.log"]
