# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:57:13 2019

@author: morei
"""

num = int(input())
value = True
for x in range(2, num):
    if (num % x == 0) or (num == 1):
        value = False
        break
print (value)