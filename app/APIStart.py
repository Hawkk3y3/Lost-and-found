# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:08:48 2019

@author: Hawkeye
"""

from flask import Flask
from flask import request
from flask import jsonify
import json
from app.DBhandler import DatabaseHandler
from app.Items import Item
from app.User import User

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify('This is index page')


@app.route('/items/create', methods=['POST'])
def create():
    try:
        database_helper = DatabaseHandler()
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        items = Item()
        items.new_item(name, loc, desc)
        database_helper.insert_item_db(items)

        resp = jsonify({"Action": 'Item Added Successfully'})
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/items/update', methods=['POST'])
def update():
    try:
        database_helper = DatabaseHandler()
        item_id = request.json['item_id']
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        items = Item()
        items.new_item(name, loc, desc)
        result = database_helper.update_item(items, item_id)
        if result:
            resp = jsonify({"Action": 'Item Updated Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'Item with Item Id {} is not found'.format(item_id)})
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)


@app.route('/items/view', methods=['GET'])
def view():
    database_helper = DatabaseHandler()
    result_list = database_helper.view_items()
    json_string = json.dumps([ob.__dict__ for ob in result_list])
    return json_string


@app.route('/items/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        database_helper = DatabaseHandler()
        result = database_helper.delete_item(item_id)
        if result:
            resp = jsonify({"Action": 'Item Deleted Successfully {}'.format(item_id)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'Item Not Found with id {}'.format(item_id)})
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)


@app.route('/item/search/<string:loc>', methods=['GET'])
def search_item(loc):
    try:
        database_helper = DatabaseHandler()
        result_list = database_helper.search_item_by_loc(loc)
        json_string = json.dumps([ob.__dict__ for ob in result_list])
        return json_string
    except Exception as e:
        print(e)


@app.route('/item/search/<string:name>', methods=['PUT'])
def search_item_name(name):
    try:
        database_helper = DatabaseHandler()
        result_list = database_helper.search_item_by_name(name)
        json_string = json.dumps([ob.__dict__ for ob in result_list])
        return json_string
    except Exception as e:
        print(e)


@app.route('/user/register', methods=['POST'])
def register_user():
    try:
        database_helper = DatabaseHandler()
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        user = User()
        user.user(username, email, password)

        exception = database_helper.register_user(user)

        if exception:
            resp = jsonify({"Action": 'Error occured {}'.format(exception)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'User Registered Successfully'})
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)


@app.route('/user/login', methods=['POST'])
def login_user():
    try:
        database_helper = DatabaseHandler()
        email = request.json['email']
        password = request.json['password']

        if database_helper.login_user(email, password):
            resp = jsonify({"Action": 'User Logged In Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action": 'User Login Failure', "reason": "Email or Password Incorrect"})
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
