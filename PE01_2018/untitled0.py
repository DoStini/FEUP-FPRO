# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:37:20 2019

@author: morei
"""

number = int(input("Input a non negative integer: "))
sum_ = 0
while number > 0:
    digit1 = number % 10
    number //= 10
    digit2 = number % 10
    sum_ += 1 if digit1==digit2 else 0
print(sum_)