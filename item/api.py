from flask import request, jsonify
import sqlalchemy

from run import app, db
from item.models import Item
from item.models import ItemBase
from user.models import UserBase
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.exc import SQLAlchemyError


@app.before_first_request
def setup():
    engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
    ItemBase.metadata.drop_all(engine)
    UserBase.metadata.drop_all(engine)

    ItemBase.metadata.create_all(engine)
    UserBase.metadata.create_all(engine)


@app.route("/")
def index():
    return "Index Page"


@app.route("/items")
def item_index():
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
        resp.status_code = 201
        return resp

    except KeyError as k:
        resp = jsonify({"error": k.args[0] + ' Value is missing'})
        # Status Code 400 is used when the request made by the client is not understandable by the server
        resp.status_code = 400
        return resp

    except Exception as e:
        resp = jsonify({"error": 'Something went wrong'})
        resp.status_code = 500
        return resp


@app.route('/items/update', methods=['POST'])
def update():
    try:
        item_id = request.json['item_id']
        name = request.json['name']
        loc = request.json['location']
        desc = request.json['description']
        new_item = Item(name, loc, desc)
        new_item.update_item(db, item_id)
        resp = jsonify({"Action": 'Item Updated Successfully'})
        resp.status_code = 200
        return resp

    except KeyError as k:
        resp = jsonify({"error": k.args[0] + ' Value is missing'})
        # Status Code 400 is used when the request made by the client is not understandable by the server
        resp.status_code = 400
        return resp

    except SQLAlchemyError:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp


@app.route('/items/view', methods=['GET'])
def view():
    try:
        items = db.session.query(Item).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except SQLAlchemyError:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp


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
            resp.status_code = 400
            return resp

    except SQLAlchemyError as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp


@app.route('/items/search/<string:loc>', methods=['GET'])
def search_item(loc):
    try:
        items = db.session.query(Item).filter(Item.location == loc).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except SQLAlchemyError as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp


@app.route('/items/search/<string:name>', methods=['GET'])
def search_item_name(name):
    try:
        items = db.session.query(Item).filter(Item.item_name == name).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])

    except SQLAlchemyError as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp
