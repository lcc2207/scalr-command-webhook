#!/usr/bin/env python

import binascii
import hmac
import yaml

from hashlib import sha1
from datetime import datetime

import requests

signing_key = '123456789'

payload = """{
    "eventName": "HostUp",
    "eventId": "a4eda072-7deb-40e4-b32c-fd0edecea23f",
    "userData": "",
    "data": {
        "SCALR_EVENT_FARM_ROLE_ID": "67460",
        "SCALR_EVENT_CLOUD_LOCATION_ZONE": "us-east-1d",
        "SCALR_EVENT_NAME": "HostUp",
        "SCALR_FARM_ROLE_ID": "67460",
        "SCALR_EVENT_ROLE_NAME": "base64-ubuntu1204",
        "SCALR_ENV_ID": "10494",
        "SCALR_AMI_ID": "ami-df0c38b6",
        "SCALR_CLOUD_LOCATION": "us-east-1",
        "SCALR_EVENT_ENV_ID": "10494",
        "SCALR_EVENT_FARM_HASH": "38330f6e827837",
        "SCALR_FARM_HASH": "38330f6e827837",
        "SCALR_EVENT_ENV_NAME": "Tutorial",
        "SCALR_EVENT_EXTERNAL_IP": "10.193.13.125",
        "SCALR_CLOUD_SERVER_ID": "i-072ccf26",
        "SCALR_EVENT_CLOUD_SERVER_ID": "i-072ccf26",
        "SCALR_EVENT_AMI_ID": "ami-df0c38b6",
        "SCALR_FARM_ID": "18609",
        "SCALR_AVAIL_ZONE": "us-east-1d",
        "SCALR_EVENT_SERVER_ID": "f2bf96c0-028d-4b9a-9f43-391fd03bf18c",
        "SCALR_CLOUD_LOCATION_ZONE": "us-east-1d",
        "SCALR_IMAGE_ID": "ami-df0c38b6",
        "SCALR_EVENT_CLOUD_LOCATION": "us-east-1",
        "SCALR_EVENT_FARM_ID": "18609",
        "SCALR_INSTANCE_INDEX": "1",
        "SCALR_SERVER_TYPE": "m1.small",
        "SCALR_EVENT_FARM_ROLE_ALIAS": "app",
        "SCALR_EXTERNAL_IP": "54.81.159.120",
        "SCALR_BEHAVIORS": "base,chef",
        "SCALR_EVENT_AVAIL_ZONE": "us-east-1d",
        "SCALR_FARM_NAME": "Tutorial :: Continuous Integration",
        "SCALR_FARM_ROLE_ALIAS": "app",
        "SCALR_EVENT_SERVER_HOSTNAME": "ec2-54-81-159-120.compute-1.amazonaws.com",
        "SCALR_EVENT_FARM_NAME": "Tutorial :: Continuous Integration",
        "SCALR_REGION": "us-east-1",
        "SCALR_EVENT_BEHAVIORS": "base,chef",
        "SCALR_SERVER_ID": "f2bf96c0-028d-4b9a-9f43-391fd03bf18c",
        "SCALR_ENV_NAME": "Tutorial",
        "SCALR_SERVER_HOSTNAME": "example.com",
        "SCALR_EVENT_INTERNAL_IP": "10.193.13.125",
        "SCALR_ROLE_NAME": "base64-ubuntu1204",
        "SCALR_INTERNAL_IP": "10.193.13.125",
        "SCALR_EVENT_SERVER_TYPE": "m1.small",
        "SCALR_EVENT_INSTANCE_INDEX": "1",
        "SCALR_EVENT_IMAGE_ID": "ami-df0c38b6",
        "SCALR_EVENT_REGION": "us-east-1",
        "SCALR_ISDBMASTER": "",
        "SCALR_EVENT_ISDBMASTER": "",
        "SCALR_INSTANCE_ID": "i-072ccf26",
        "SCALR_EVENT_INSTANCE_ID": "i-072ccf26"
    },
    "timestamp": "Wed 22 Feb 2019 14:28:05 UTC"
}"""

def httpdate(dt):
    """Return a string representation of a date according to RFC 1123
    (HTTP/1.1).

    The supplied date must be in UTC.

    """
    weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
             "Oct", "Nov", "Dec"][dt.month - 1]
    return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
        dt.year, dt.hour, dt.minute, dt.second)

def signature(date, body):
    return binascii.hexlify(hmac.new(signing_key, body + date, sha1).digest())

date = httpdate(datetime.utcnow())
sig = signature(date, payload)

headers = {
    'Date': date,
    'X-Signature': sig
}

info=yaml.load(open('.kitchen/default-ubuntu-1604'))
host=info['hostname']
r = requests.post('http://'+ host + ':5018/reporting/', headers=headers, data=payload)
print r.status_code
print r.text
