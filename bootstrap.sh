#!/bin/bash
apt update
apt install python-pip -y

pip install docker-compose

curl -fsSL https://get.docker.com/ | sh
service docker start || systemctl start docker

git clone git clone https://github.com/scalr-tutorials/scalr-snow-webhook.git /opt/snow-webhook
