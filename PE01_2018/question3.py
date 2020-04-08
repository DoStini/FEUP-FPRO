# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:05:49 2019

@author: morei
"""

names = ["bart", "marie", "jo"]
ages = [23, 75, 19]
    
n = 0
a = 0
for name in names:
    for age in ages:
        if n == a:
            print(name + "-" + str(age))
            break
        a += 1 
    n += 1