from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


if __name__ == "__main__":
    from item.api import *
    from user.api import *
    app.run('127.0.0.1', 5000)
