# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:08:48 2019

@author: Hawkeye
"""

from flask import Flask
from flask import request
from flask import jsonify
import json
from DBhandler import DatabaseHandler as db
from Items import Item as item
from User import User

app = Flask(__name__)




@app.route('/')
def index():
    return jsonify('This is index page')

@app.route('/items/create',methods=['POST'])
def create():
    try:
        testdb = db()
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        items = item()
        items.newItem(name,loc,desc)
        testdb.insert_item_db(items)
        
        resp = jsonify({"Action":'Item Added Successfully'})
        resp.status_code = 200
        return resp
        
    except Exception as e:
        print(e)
        
@app.route('/items/update',methods=['POST'])
def update():
    try:
        testdb = db()
        item_id =request.json['item_id'] 
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        items = item()
        items.newItem(name,loc,desc)
        result = testdb.update_item(items,item_id)
        if result:
            resp = jsonify({"Action":'Item Updated Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action":'Item with Item Id {} is not found'.format(item_id)})
            resp.status_code = 200
            return resp
        
    except Exception as e:
        print(e)
@app.route('/items/view',methods=['GET'])
def view():
    testdb = db()
    resultlist=testdb.view_items()
    json_string = json.dumps([ob.__dict__ for ob in resultlist])
    return json_string
@app.route('/items/delete/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    try:
        testdb = db()
        result=testdb.delete_item(item_id)
        if result:
            resp = jsonify({"Action":'Item Deleted Successfully {}'.format(item_id)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action":'Item Not Found with id {}'.format(item_id)})
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
@app.route('/item/search/<string:loc>',methods=['GET'])
def search_item(loc):
    try:
        testdb = db()
        resultlist = testdb.search_item_by_loc(loc)
        json_string = json.dumps([ob.__dict__ for ob in resultlist])
        return json_string
    except Exception as e:
        print(e)

@app.route('/item/search/<string:name>',methods=['PUT'])
def search_item_name(name):
    try:
        testdb = db()
        resultlist = testdb.search_item_by_name(name)
        json_string = json.dumps([ob.__dict__ for ob in resultlist])
        return json_string
    except Exception as e:
        print(e)
    
@app.route('/user/register',methods=['POST'])
def register_user():
    try:
        testdb = db()
        username =request.json['username'] 
        email = request.json['email']
        password = request.json['password']
        user = User()
        user.User(username,email,password)
        
        excep=testdb.register_user(user)
        
        if excep:
            resp = jsonify({"Action":'Error occured {}'.format(excep)})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action":'User Registered Successfully'})
            resp.status_code = 200
            return resp        
        
        
    except Exception as e:
        print(e)


@app.route('/user/login',methods=['POST'])
def login_user():
    try:
        testdb = db() 
        email = request.json['email']
        password = request.json['password']
        
        if testdb.login_user(email,password):
            resp = jsonify({"Action":'User Logged In Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"Action":'User Login Failure',"reason":"Email or Password Incorrect"})
            resp.status_code = 200
            return resp
        
        
    except Exception as e:
        print(e)



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
