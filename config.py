DEBUG = False

database = 'lost_and_found'
user = 'root'
password = 'xzcv'
host = 'db'
port = '3306'
connection_string = 'mysql://{0}:{1}@{2}:{3}'.format(user, password, host, port)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = '{}/{}'.format(connection_string, database)

SECRET_KEY = "ThisisaSecret"

"""---------------------------------------------------"""
"""Setting up configurations for the mail Server"""
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'usmanmani781@gmail.com'
MAIL_PASSWORD = 'Us766866163'
MAIL_DEBUG = False
MAIL_DEFAULT_SENDER = ('Muhammad Usman', 'usmanmani781@gmail.com')
MAIL_MAX_EMAIL = None
MAIL_ASCII_ATTACHMENT = False

"""-------------------------------------------------"""
"""Celery Configurations"""
celery_host = 'redis'
celery_port = '6379'
CELERY_BROKER_URL = 'redis://{0}:{1}/0'.format(celery_host, celery_port)
CELERY_RESULT_BACKEND = 'redis://{0}:{1}/0'.format(celery_host, celery_port)
