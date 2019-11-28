from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError

from run import app, db
from item.models import Item


@app.route("/")
def index():
    return "Index Page"


@app.route('/items', methods=['POST'])
def create():
    try:
        name = request.json['name']
        loc = request.json['location']
        category = request.json['category']
        desc = request.json['description']
        item = Item(name, loc, category, desc)
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

    except SQLAlchemyError as e:
        resp = jsonify({"error": 'Something went wrong'})
        resp.status_code = 500
        return resp


@app.route('/items/<int:item_id>', methods=['PATCH'])
def update(item_id):
    try:
        name = request.json['name']
        loc = request.json['location']
        category = request.json['category']
        desc = request.json['description']
        new_item = Item(name, loc, category, desc)
        item = db.session.query(Item).filter(Item.id == item_id).one()
        new_item.update_item(item)
        db.session.commit()
        db.session.close()
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


@app.route('/items/<int:item_id>', methods=['DELETE'])
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


@app.route('/items', methods=['GET'])
def search_item():
    try:
        args = request.args
        if args.__len__() == 0:
            items = db.session.query(Item).all()
            db.session.close()
            return jsonify(data=[item.serialize() for item in items])
        elif 'name' in args and 'location' in args:
            loc = request.args.get('location', '')
            name = request.args.get('name', '')
            items = db.session.query(Item).filter_by(location=loc, item_name=name).all()
            db.session.close()
            return jsonify(data=[item.serialize() for item in items])

        elif 'name' in args:
            name = request.args.get('name', '')
            items = db.session.query(Item).filter_by(item_name=name).all()
            db.session.close()
            return jsonify(data=[item.serialize() for item in items])
        elif 'location' in args:
            loc = request.args.get('location', '')
            items = db.session.query(Item).filter_by(location=loc).all()
            db.session.close()
            return jsonify(data=[item.serialize() for item in items])
        else:
            resp = jsonify({"error": 'Query Parameters not defined correctly'})
            resp.status_code = 400
            return resp

    except SQLAlchemyError as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp
    except Exception as e:
        resp = jsonify({"error": 'something went wrong'})
        resp.status_code = 500
        return resp
