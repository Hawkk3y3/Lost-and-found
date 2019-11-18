from flask import request, jsonify

from run import app, db
from item.models import Item


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
        new_item = Item(name, loc, desc)
        result = new_item.update_item(db, item_id)
        if result:
            resp = jsonify({"Action": 'Item Updated Successfully'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"error": 'Some error occurred {}'.format(result)})
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


@app.route('/items/search/<string:loc>', methods=['GET'])
def search_item(loc):
    try:
        items = db.session.query(Item).filter(Item.location == loc).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/items/search/<string:name>', methods=['PUT'])
def search_item_name(name):
    try:
        items = db.session.query(Item).filter(Item.item_name == name).all()
        db.session.close()
        return jsonify(data=[item.serialize() for item in items])
    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp
