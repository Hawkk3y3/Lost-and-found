# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:09:17 2019

@author: Hawkeye
"""

import pymysql as connector
from app.Items import Item
from datetime import datetime as date_time


class DatabaseHandler(object):

    def __init__(self):
        self.conn = connector.connect(host="db", port=3306, user="root", password="xzcv", db="lostandfound")

    def insert_item_db(self, items):
        date = date_time.now()
        items.date = date.strftime('%m/%d/%Y')
        cursor = self.conn.cursor()
        sql = "INSERT INTO `items` (`item_category`,`item_name`,`location`,`description`,`date`)" \
              " VALUES (%s,%s,%s,%s,%s);"
        val = (items.category, items.name, items.location, items.desc, items.date)
        cursor.execute(sql, val)
        self.conn.commit()
        print(cursor.rowcount, "record inserted.")
        cursor.close()
        self.conn.close()

    def update_item(self, items, item_id):
        cursor = self.conn.cursor()
        sql = "UPDATE `items`" \
              " SET `item_category` =%s,`item_name` =%s,`location` =%s,`description` =%s,`date` =%s WHERE `itemid` =%s;"
        val = (items.category, items.name, items.location, items.desc, items.date, item_id)
        res = cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        if res == 0:
            return False
        else:
            return True

    def view_items(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM `items`"
        cursor.execute(sql)
        rows = cursor.fetchall()
        item_list = self.map_to_object(rows)
        cursor.close()
        self.conn.close()
        return item_list

    def delete_item(self, item_id):
        cursor = self.conn.cursor()
        sql = "DELETE FROM `items` WHERE `itemid`={};".format(item_id)
        res = cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        if res == 1:
            return True
        else:
            return False

    def search_item_by_loc(self, loc):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM `items` WHERE `location` = '{}';".format(loc)
        cursor.execute(sql)
        rows = cursor.fetchall()
        item_list = self.map_to_object(rows)
        cursor.close()
        self.conn.close()
        return item_list

    def search_item_by_name(self, name):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM `items` WHERE `item_name`='{}';".format(name)
        cursor.execute(sql)
        rows = cursor.fetchall()
        item_list = self.map_to_object(rows)
        cursor.close()
        self.conn.close()
        return item_list

    def register_user(self, user):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO `users`(`username`,`email`,`password`) VALUES(%s,%s,%s);"
            val = (user.username, user.email, user.password)
            cursor.execute(sql, val)
            self.conn.commit()
            cursor.close()
            self.conn.close()

        except Exception as e:
            return e.__str__()

    def login_user(self, email, password):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM `users` WHERE `email`='{}' and `password`='{}';".format(email, password)
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows.__len__())
        cursor.close()
        self.conn.close()

        if rows.__len__() == 1:
            return True
        else:
            return False

    @staticmethod
    def map_to_object(rows):
        item_list = []
        new_item = Item()
        for row in rows:
            count = 0
            for ele in row:
                if count == 0:
                    new_item.item_id = ele
                elif count == 1:
                    new_item.category = ele
                elif count == 2:
                    new_item.name = ele
                elif count == 3:
                    new_item.location = ele
                elif count == 4:
                    new_item.desc = ele
                elif count == 5:
                    new_item.date = ele
                count += 1

            item_list.append(new_item)

        return item_list
