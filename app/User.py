# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:24:12 2019

@author: Hawkeye
"""

class User(object):
    
    def __init__(self):
        self.username = 'jhondoe'
        self.email = 'jhondoe@gmail.com'
        self.password = 'encrypted'
        

    def User(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password