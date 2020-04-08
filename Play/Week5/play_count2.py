# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:21:42 2019

@author: morei
"""

def count_until(tup):
    x = 0
    for a in tup:
        if type(a).__name__ == "tuple":
            return x
        x += 1
    return -1