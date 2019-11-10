# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:09:17 2019

@author: Hawkeye
"""

import pymysql as connector
from app.Items import Item
from datetime import datetime


def map_to_object(rows):
    item_list = []
    item_id = 0
    category = "lost/found"
    name = "watch"
    location = "Park"
    desc = ""
    date = ""
    for row in rows:
        count = 0
        for ele in row:
            if count == 0:
                item_id = ele
            elif count == 1:
                category = ele
            elif count == 2:
                name = ele
            elif count == 3:
                location = ele
            elif count == 4:
                desc = ele
            elif count == 5:
                date = ele
            count += 1
        new_item = Item()
        new_item.item(item_id, category, name, location, desc, date)
        item_list.append(new_item)
    return item_list


class DatabaseHandler(object):

    def __init__(self):
        self.my_db = connector.connect(host="db", port=3306, user="root", password="xzcv", db="lostandfound")

    def insert_item_db(self, items):
        date = datetime.now()
        items.date = date.strftime('%m/%d/%Y')
        my_cursor = self.my_db.cursor()
        sql = "INSERT INTO `items` (`item_category`,`item_name`,`location`,`description`,`date`)" \
              " VALUES (%s,%s,%s,%s,%s);"
        val = (items.category, items.name, items.location, items.desc, items.date)
        my_cursor.execute(sql, val)
        self.my_db.commit()
        print(my_cursor.rowcount, "record inserted.")
        my_cursor.close()
        self.my_db.close()

    def update_item(self, items, item_id):
        my_cursor = self.my_db.cursor()
        sql = "UPDATE `items` "\
              " SET `item_category` =%s,`item_name` =%s,`location` =%s,`description` =%s,`date` =%s WHERE `itemid` =%s;"
        val = (items.category, items.name, items.location, items.desc, items.date, item_id)
        res = my_cursor.execute(sql, val)
        self.my_db.commit()
        my_cursor.close()
        self.my_db.close()
        if res == 0:
            return False
        else:
            return True

    def view_items(self):
        my_cursor = self.my_db.cursor()
        sql = "SELECT * FROM `items`"
        my_cursor.execute(sql)
        rows = my_cursor.fetchall()
        item_list = map_to_object(rows)
        my_cursor.close()
        self.my_db.close()
        return item_list

    def delete_item(self, item_id):
        my_cursor = self.my_db.cursor()
        sql = "DELETE FROM `items` WHERE `itemid`={};".format(item_id)
        res = my_cursor.execute(sql)
        self.my_db.commit()
        my_cursor.close()
        self.my_db.close()
        if res == 1:
            return True
        else:
            return False

    def search_item_by_loc(self, loc):
        my_cursor = self.my_db.cursor()
        sql = "SELECT * FROM `items` WHERE `location` = '{}';".format(loc)
        my_cursor.execute(sql)
        rows = my_cursor.fetchall()
        item_list = map_to_object(rows)
        my_cursor.close()
        self.my_db.close()
        return item_list

    def search_item_by_name(self, name):
        my_cursor = self.my_db.cursor()
        sql = "SELECT * FROM `items` WHERE `item_name`='{}';".format(name)
        my_cursor.execute(sql)
        rows = my_cursor.fetchall()
        item_list = map_to_object(rows)
        my_cursor.close()
        self.my_db.close()
        return item_list

    def register_user(self, user):
        try:
            my_cursor = self.my_db.cursor()
            sql = "INSERT INTO `users`(`username`,`email`,`password`) VALUES(%s,%s,%s);"
            val = (user.username, user.email, user.password)
            my_cursor.execute(sql, val)
            self.my_db.commit()
            my_cursor.close()
            self.my_db.close()

        except Exception as e:
            return e.__str__()

    def login_user(self, email, password):
        my_cursor = self.my_db.cursor()
        sql = "SELECT * FROM `users` WHERE `email`='{}' and `password`='{}';".format(email, password)
        my_cursor.execute(sql)
        rows = my_cursor.fetchall()
        print(rows.__len__())
        my_cursor.close()
        self.my_db.close()

        if rows.__len__() == 1:
            return True
        else:
            return False
