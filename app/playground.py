# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:38:39 2019

@author: Hawkeye
"""

from DBhandler import DatabaseHandler as db
from User import User
from Items import Item as item
import time


time.sleep(5)

testdb = db()
# user = User()
# user.username="hawkeye"
# user.email="hawkeye@gmail.com"
# user.password="xzcv"

# items = item()
# name = 'name'
# loc = 'location'
# desc = 'description'
testdb.delete_item(1)

# items.newItem(name,loc,desc)
# testdb.insert_item_db(items)


