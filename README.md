# command demo webhook

This webhook to kick off scripts you write


# Instance setup.
Execute "bootstrap.sh" on the target install

This will install docker and pull down the comand-webhook repo.

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
env = SCALR_URL=https://demo.scalr.com
env = SCALR_WEBHOOK=command  # name of the webhook endpiont ex) http:/xxx:5018/command
env = SCALR_COMMAND_GV=WEBHOOK_COMMAND # the path to the .sh/exe/etc you need to execute
```

# Launch
execute 'relaunch.sh'
