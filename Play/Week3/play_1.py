# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:50:37 2019

@author: morei
"""

num = int(input())
sum = 0
for x in range(1, num + 1):
    if(num % x == 0):
        sum += x
        
print(sum)