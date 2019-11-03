# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:38:39 2019

@author: Hawkeye
"""

from DBhandler import DatabaseHandler as db
from User import User

testdb = db()
user = User()
user.username="hawkeye"
user.email="hawkeye@gmail.com"
user.password="xzcv"

excep = testdb.register_user(user)
exc = testdb.login_user(user.email,user.password)

