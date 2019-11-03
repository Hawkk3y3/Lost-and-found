# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:09:17 2019

@author: Hawkeye
"""



import pymysql as connector
from Items import Item as item
from datetime import datetime as datetimee

class DatabaseHandler(object):
    
    def __init__(self):
        self.mydb = connector.connect(host="db",port=3306,user="root",password="xzcv",db="lostandfound")
    
    def insert_item_db(self,items):
        date = datetimee.now()
        items.date = date.strftime('%m/%d/%Y')
        mycursor=self.mydb.cursor()
        sql = "INSERT INTO `items` (`item_category`,`item_name`,`location`,`description`,`date`) VALUES (%s,%s,%s,%s,%s);"
        val= (items.category,items.name,items.location,items.desc,items.date)
        mycursor.execute(sql,val)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        self.mydb.close()
        
    def update_item(self,items,item_id):
        mycursor=self.mydb.cursor()
        sql = "UPDATE `items` SET `item_category` =%s,`item_name` =%s,`location` =%s,`description` =%s,`date` =%s WHERE `itemid` =%s;"
        val= (items.category,items.name,items.location,items.desc,items.date,item_id)
        mycursor.execute(sql,val)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        self.mydb.close()
        
    def view_items(self):
        mycursor=self.mydb.cursor()
        sql = "SELECT * FROM `items`"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        itemlist = self.map_to_object(rows)
        mycursor.close()
        self.mydb.close()
        return itemlist
    
    def delete_item(self,item_id):
        mycursor=self.mydb.cursor()
        sql = "DELETE FROM `items` WHERE `itemid`={};".format(item_id)
        mycursor.execute(sql)
        self.mydb.commit()
        mycursor.close()
        self.mydb.close()
        
    def search_item_by_loc(self,loc):
        mycursor=self.mydb.cursor()
        sql = "SELECT * FROM `items` WHERE `location` = '{}';".format(loc)
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        itemlist = self.map_to_object(rows)
        mycursor.close()
        self.mydb.close()
        return itemlist
    
    def search_item_by_name(self,name):
        mycursor=self.mydb.cursor()
        sql = "SELECT * FROM `items` WHERE `item_name`='{}';".format(name)
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        itemlist = self.map_to_object(rows)
        mycursor.close()
        self.mydb.close()
        return itemlist
    
    def register_user(self,user):
        try:
            mycursor = self.mydb.cursor()
            sql = "INSERT INTO `users`(`username`,`email`,`password`) VALUES(%s,%s,%s);"
            val = (user.username,user.email,user.password)
            mycursor.execute(sql,val)
            self.mydb.commit()
            mycursor.close()
            self.mydb.close()
            
        except Exception as e:
            return e.__str__()
    
    
    def login_user(self,email,password):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `users` WHERE `email`='{}' and `password`='{}';".format(email,password)
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        print(rows.__len__())
        mycursor.close()
        self.mydb.close()
        
        if rows.__len__() == 1:
            return True
        else:
            return False
        
    def map_to_object(self,rows):
        itemlist = []
        item_id=0
        category = "lost/found"
        name = "watch"
        location = "Park"
        desc=""
        date=""
        for row in rows:
            count = 0
            for ele in row:
                if count == 0:
                    item_id=ele
                elif count==1:
                    category=ele
                elif count==2:
                    name=ele
                elif count==3:
                    location=ele
                elif count==4:
                    desc=ele
                elif count==5:
                    date=ele
                count+=1
            newItem=item()
            newItem.Item(item_id,category,name,location,desc,date)
            itemlist.append(newItem)
        return itemlist
        
    
