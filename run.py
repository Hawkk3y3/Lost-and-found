from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_celery import make_celery
app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

celery = make_celery(app)
celery.conf.update(app.config)
from item.api import *
from user.api import *

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
