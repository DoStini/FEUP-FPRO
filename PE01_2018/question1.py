# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:35:38 2019

@author: morei
"""

num = int(input())
num_ = num
sum_ = 0
for x in range(3):
    sum_ += ((num_ % 10)**3)
    num_ //= 10
if sum_ == num:
    print(True)
else:
    print(False)