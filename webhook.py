#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import abort

import pytz
import string
import random
import json
import logging
import binascii
import dateutil.parser
import hmac
import os
import requests
import subprocess

from requests.exceptions import ConnectionError
from hashlib import sha1
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Configuration variables
SCALR_SIGNING_KEY = os.getenv('SCALR_SIGNING_KEY', '')
SCALR_URL = os.getenv('SCALR_URL', '')
SCALR_WEBHOOK = os.getenv('SCALR_WEBHOOK', '')
SCALR_COMMAND_GV = os.getenv('SCALR_COMMAND_GV', '')

for var in ['SCALR_SIGNING_KEY', 'SCALR_URL', 'SCALR_WEBHOOK', 'SCALR_COMMAND_GV']:
    logging.info('Config: %s = %s', var, globals()[var] if 'PASS' not in var else '*' * len(globals()[var]))

@app.route('/' + SCALR_WEBHOOK + '/', methods=['POST'])
def webhook_listener():
    if not validate_request(request):
        abort(403)
    data = json.loads(request.data)
    event = data['eventName']
    hostname = data['data']['SCALR_SERVER_HOSTNAME']
    ipaddress = data['data']['SCALR_INTERNAL_IP']
    command = data['data'][SCALR_COMMAND_GV]
    variables = json.dumps(data['data'])
    # return_code = subprocess.call(args=[ command, hostname, ipaddress, event, variables ])
    return_code = subprocess.check_output(args=[command, hostname, ipaddress, event, variables])
    logging.info(return_code)
    return(return_code)

def validate_request(request):
    if 'X-Signature' not in request.headers or 'Date' not in request.headers:
        logging.debug('Missing signature headers')
        return False
    date = request.headers['Date']
    body = request.data
    expected_signature = binascii.hexlify(hmac.new(SCALR_SIGNING_KEY, body + date, sha1).digest())
    if expected_signature != request.headers['X-Signature']:
        logging.debug('Signature does not match')
        return False
    date = dateutil.parser.parse(date)
    now = datetime.now(pytz.utc)
    delta = abs((now - date).total_seconds())
    return delta < 300


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
