# bind = "0.0.0.0:80"
# chdir = "/www"
# loglevel = "error"
# workers = "1"
# worker_class = "gevent"
# threads = "1"
#
# errorlog = "-"
# accesslog = "-"

# gunicorn config.py

bind = "0.0.0.0:80"
chdir = "/www"
loglevel = "error"
workers = 1  # Ensure this is an integer, not a string
worker_class = "gevent"
threads = 1  # Ensure this is an integer, not a string

errorlog = "-"
accesslog = "-"

# Allow Gunicorn to trust `X-Forwarded-For` from any proxy
forwarded_allow_ips = "*"
