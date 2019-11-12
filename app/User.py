# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:24:12 2019

@author: Hawkeye
"""
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

UserBase = declarative_base()


class User(UserBase):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    username = Column('username', String(50))
    email = Column('email', String(100))
    password = Column('password', String(100))
    verified = Column('verified', Boolean)
    date_created = Column('date_created', DateTime, default=datetime.now)

    def __init__(self, username, email, password, verified=False):
        self.username = username
        self.email = email
        self.password = password
        self.verified = verified

    @property
    def serialize(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password,
                'verified': self.verified, 'date_created': self.date_created}
