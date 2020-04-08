# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:57:39 2019

@author: morei
"""

d, num = int(input()), int(input())

aux = num
sum_ = 0
while (aux > 0):
    digit = aux % 10
    if digit > d:
        sum_ += (2   * digit)
    aux //= 10
print(sum_)