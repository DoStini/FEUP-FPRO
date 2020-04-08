# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:36:14 2019

@author: morei
"""

def biggest_member(atuple):
    biggest = tuple()
    for val in atuple:
        if type(val) == tuple:
            if len(val) > len(biggest):
                biggest = val
            out = biggest_member(val)
            if out is not None and len(out) > len(biggest):
                biggest = out
            
    return biggest