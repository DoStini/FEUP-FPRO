# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:40:33 2019

@author: morei
"""

num = str(input())
counter = 0
for x in range(0, len(num) - 1):
    if (num[x] == num[x+1]):
        counter += 1
print(counter)