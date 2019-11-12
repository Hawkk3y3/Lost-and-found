# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:08:48 2019

@author: Hawkeye
"""

from flask import Flask
from flask import request
from flask import jsonify
from app.User import User, UserBase
from app.Item import Item, ItemBase
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database = 'lost_and_found'
user = 'root'
password = 'xzcv'
host = 'localhost'
port = '3306'

"""-----------------------------------------------------------------------------"""
"""This Section is to create database if it doesn't already exists"""
connection_string = 'mysql://{0}:{1}@{2}:{3}'.format(user, password, host, port)
# This engine just used to query for list of databases
mysql_engine = create_engine(connection_string)

# Query for existing databases
existing_databases = mysql_engine.execute("SHOW DATABASES;")
# Results are a list of single item tuples, so unpack each tuple
existing_databases = [d[0] for d in existing_databases]

# Create database if not exists
if database not in existing_databases:
    mysql_engine.execute("CREATE DATABASE {0}".format(database))
"""--------------------------------------------------------------------------------"""

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string + '/{}'.format(database)

db = SQLAlchemy(app)


@app.before_first_request
def setup():
    """Check Database if it exists with the Tables of our model"""
    mysql_engine.execute("use {};".format(database))
    existing_tables = mysql_engine.execute("Show Tables;")
    existing_tables = [d[0] for d in existing_tables]
    table = User.__tablename__
    if table not in existing_tables:
        UserBase.metadata.drop_all(bind=db.engine)
        ItemBase.metadata.drop_all(bind=db.engine)
        UserBase.metadata.create_all(bind=db.engine)
        ItemBase.metadata.create_all(bind=db.engine)


@app.route("/")
def index():
    return "Hello World"


@app.route('/items/create', methods=['POST'])
def create():
    try:
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        item = Item(name, loc, desc)
        db.session.add(item)
        db.session.commit()
        db.session.close()

        resp = jsonify({"Action": 'Item Added Successfully'})
        resp.status_code = 200
        return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/items/update', methods=['POST'])
def update():
    try:
        item_id = request.json['item_id']
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        item = db.session.query(Item).filter(Item.id == item_id).one()
        item.item_name = name
        item.location = loc
        item.description = desc
        db.session.commit()
        db.session.close()

        if item:
            resp = jsonify({"Action": 'Item Updated Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'Item with Item Id {} is not found'.format(item_id)})
            resp.status_code = 200
            return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/items/view', methods=['GET'])
def view():
    items = db.session.query(Item).all()
    db.session.close()
    return jsonify(data=[item.serialize() for item in items])


@app.route('/items/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:

        result = db.session.query(Item).filter(Item.id == item_id).delete()
        db.session.commit()
        db.session.close()
        if result:
            resp = jsonify({"Action": 'Item Deleted Successfully {}'.format(item_id)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'Item Not Found with id {}'.format(item_id)})
            resp.status_code = 200
            return resp
    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/item/search/<string:loc>', methods=['GET'])
def search_item(loc):
    try:
        items = db.session.query(Item).filter(Item.location == loc).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/item/search/<string:name>', methods=['PUT'])
def search_item_name(name):
    try:
        items = db.session.query(Item).filter(Item.item_name == name).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/user/register', methods=['POST'])
def register_user():
    try:
        username = request.json['username']
        email = request.json['email']
        passw = request.json['password']

        new_user = User(username, email, passw)

        db.session.add(new_user)
        db.session.commit()
        db.session.close()

        resp = jsonify({"Action": 'User Registered Successfully'})
        resp.status_code = 200
        return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/user/login', methods=['POST'])
def login_user():
    try:
        email = request.json['email']
        passw = request.json['password']
        check = db.session.query(User).filter(User.email == email).filter(User.password == passw).all()

        if check.__len__ == 1:
            resp = jsonify({"Action": 'User Logged In Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'User Login Failure', "reason": "Email or Password Incorrect"})
            resp.status_code = 200
            return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


if __name__ == "__main__":
    app.run('127.0.0.1', 5000)

