DEBUG = True

database = 'lost_and_found'
user = 'root'
password = 'xzcv'
host = 'localhost'
port = '3306'
connection_string = 'mysql://{0}:{1}@{2}:{3}'.format(user, password, host, port)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = connection_string + '/{}'.format(database)

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
