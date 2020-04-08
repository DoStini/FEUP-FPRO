# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:51:55 2019

@author: morei
"""

def days_until_empty(c, l):
    curr = c
    day = l - 1
    while curr > 0:
        day += 1
        curr += l
        if curr > c:
            curr = c
        curr -= day  
    return day