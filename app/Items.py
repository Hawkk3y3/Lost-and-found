# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:06:01 2019

@author: Hawkeye
"""


class Item(object):

    def __init__(self):
        self.item_id = 0
        self.category = "lost/found"
        self.name = "watch"
        self.location = "Park"
        self.desc = "Mens Watch with steel bracelet"
        self.date = "13/09/2019"

    def new_item(self, name, location, desc):
        self.name = name
        self.location = location
        self.desc = desc

    def item(self, item_id, category, name, location, desc, date):
        self.item_id = item_id
        self.category = category
        self.name = name
        self.location = location
        self.desc = desc
        self.date = date

    def __str__(self):
        return """Item Id: {}\nItem Category: {}\nItem Name: {}\nLocation:{}\nDescription:{},found on:{}
                """.format(self.item_id, self.category, self.name, self.location, self.desc, self.date)
