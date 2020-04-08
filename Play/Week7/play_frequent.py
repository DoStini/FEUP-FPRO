# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:08:28 2019

@author: morei
"""

def most_frequent(alist):
    dic = {}
    for x in alist:
        dic[x] = dic.get(x, 0) + 1
    max_ = 0
    counter = 0
    for x in dic:
        if dic[x] > counter:
            max_ = x
            counter = dic[x]
        elif dic[x] == counter:
            max_ = max([x, max_])
    return max_