# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:38:39 2019

@author: Hawkeye
"""

from app.DBhandler import DatabaseHandler
from app.User import User
from app.Items import Item
import time


time.sleep(5)

test_db = DatabaseHandler()
# user = User()
# user.username="hawkeye"
# user.email="hawkeye@gmail.com"
# user.password="xzcv"

# items = item()
# name = 'name'
# loc = 'location'
# desc = 'description'
test_db.delete_item(1)

# items.newItem(name,loc,desc)
# testdb.insert_item_db(items)


