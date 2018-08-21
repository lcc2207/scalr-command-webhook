#!/bin/bash
apt update
apt install python-pip -y

pip install docker-compose

curl -fsSL https://get.docker.com/ | sh
service docker start || systemctl start docker

git clone git clone https://github.com/lcc2207/scalr-command-webhook.git /opt/command-webhook
