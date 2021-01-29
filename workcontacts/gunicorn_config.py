command = '/home/alex/code/workcontacts/env/bin/gunicorn'
pythonpath = '/home/alex/code/workcontacts/workcontacts'
bind = '127.0.0.1:7000'
workers = 3
user = 'alex'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=workcontacts.settings'
