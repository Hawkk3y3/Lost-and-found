# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:06:01 2019

@author: Hawkeye
"""
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

ItemBase = declarative_base()


class Item(ItemBase):
    __tablename__ = 'Items'
    id = Column('item_id', Integer, primary_key=True)
    category = Column('category', String(50), default='lost/found')
    item_name = Column('item_name', String(100))
    location = Column('location', String(100))
    description = Column('description', String(500))
    date_created = Column('date_created', DateTime, default=datetime.now)

    def __init__(self, item_name, location, description):
        self.item_name = item_name
        self.location = location
        self.description = description

    def serialize(self):
        return {'item_id': self.id, 'category': self.category, 'item_name': self.item_name, 'location': self.location,
                'description': self.description, 'date_created': self.date_created}
