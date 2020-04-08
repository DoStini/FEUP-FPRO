# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:20:43 2019

@author: morei
"""

def rec(number):
    print(number)
    try:
        rec(number+1)
    except:
        rec(number+1)