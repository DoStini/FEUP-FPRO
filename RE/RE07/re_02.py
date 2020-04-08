# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:02:56 2019

@author: morei
"""

def collisions(alist):
    dic = {}
    for x in alist:
        num = hash_(x)
        dic[num] = dic.get(num, 0) + 1
    return dic

def hash_(num):
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num //= 10
    return sum_%8