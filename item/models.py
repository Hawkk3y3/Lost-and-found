from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from run import db


class Item(db.Model):
    __tablename__ = 'Items'
    id = db.Column('item_id', db.Integer, primary_key=True)
    category = db.Column('category', db.String(50), default='lost/found')
    item_name = db.Column('item_name', db.String(100))
    location = db.Column('location', db.String(100))
    description = db.Column('description', db.String(500))
    date_created = db.Column('date_created', db.DateTime, default=datetime.now)

    def __init__(self, item_name, location, description):
        self.item_name = item_name
        self.location = location
        self.description = description

    def serialize(self):
        return {'item_id': self.id, 'category': self.category, 'item_name': self.item_name, 'location': self.location,
                'description': self.description, 'date_created': self.date_created}

    def update_item(self, db, item_id):
        try:
            item = db.session.query(Item).filter(Item.id == item_id).one()
            item.item_name = self.item_name
            item.location = self.loc
            item.description = self.description
            db.session.commit()
            db.session.close()

        except SQLAlchemyError as er:
            raise er
