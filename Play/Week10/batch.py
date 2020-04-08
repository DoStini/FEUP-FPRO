# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:17:55 2019

@author: morei
"""

def batch_norm(alist, batch_size):
    batches = []
    x = 0
    while x < len(alist):
        batches.append(alist[x: x+batch_size])
        x += batch_size
    for y in batches:
        list_copy = y.copy()
        list_copy = sorted(list_copy)
        print(list_copy)
        yield [x - list_copy[int(len(y)/2)] if len(y) % 2 == 1 else x - (list_copy[int(len(y)/2)] + list_copy[int(len(y)/2)-1])/2 for x in y] 