# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:16:27 2019

@author: morei
"""

def last_man_standing(alist, step, index=0):
    if len(alist) == 1:
        return alist[0]
    else:
        index += step - 1
        if index >= len(alist):
            index = index % len(alist)
        alist.pop(index)
        val = last_man_standing(alist, step, index)
        if val is not None:
            return val
        