# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:41:48 2019

@author: morei
"""

def last_man_standing(alist, step):
    counter = 0
    while len(alist) > 1:
        len_ = len(alist)
        counter += step -1
        if counter >= len_:
            counter %= len_
        print(counter, alist)

        alist.pop(counter)
    return alist[0]