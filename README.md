# command demo webhook

This webhook keeps Farm and Server records updated in ServiceNow.


# Instance setup.
Execute "bootstrap.sh" on the target install

This will install docker and pull down the SNOW webhook repo.

# Update the uwsgi.ini file with your settings

```ini
[uwsgi]
chdir = /opt/command-webhook
http-socket = 0.0.0.0:5018
wsgi-file = webhook.py
callable = app
workers = 1
master = true
plugin = python
env = SCALR_SIGNING_KEY=scalr_signing_key
env = SNOW_URL=https://xxx.service-now.com/
env = SNOW_USER=admin
env = SNOW_PASS=password
env = SCALR_URL=https://demo.scalr.com
```

# Launch
execute 'relaunch.sh'
