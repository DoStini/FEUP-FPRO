# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:14:36 2019

@author: morei
"""

n1 = int(input())
n2 = int(input())
n_ = n2
len_ = 0
while True:
    n_ = n_/10
    if (n_ > 0.1):
        len_ += 1
    else:
        break
result = n1*10**len_ +n2
print(result)