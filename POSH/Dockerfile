FROM debian:jessie-slim
MAINTAINER Scalr <@scalr.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends python python-dev python-pip uwsgi uwsgi-plugin-python wget apt-transport-https apt-utils curl && \
    groupadd uwsgi && \
    useradd -g uwsgi uwsgi

# Import the public repository GPG keys for Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Register the Microsoft .deb repository.
RUN curl https://packages.microsoft.com/config/ubuntu/14.04/prod.list | tee /etc/apt/sources.list.d/microsoft.list

# Update package list again and install PowerShell.
RUN apt-get update && apt-get install -y powershell

COPY ./requirements.txt /opt/command-webhook/

RUN pip install -r /opt/command-webhook/requirements.txt

COPY . /opt/command-webhook

EXPOSE 5018

CMD ["/usr/bin/uwsgi", "--ini", "/opt/command-webhook/uwsgi.ini", "--logto2", "/var/log/webhook/webhook.log"]
