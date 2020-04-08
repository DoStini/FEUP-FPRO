# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:34:07 2019

@author: morei
"""

ints = [1, 2, 2, 3, 5, 9, 13, 21, 34]
num = int(input())
smaller = "Less:"
greater = "Greater:"
for x in ints:
    if x > num:
        greater += " " + str(x)
    elif x < num:
        smaller += " " + str(x)
print(smaller)
print(greater)