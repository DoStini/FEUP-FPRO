# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:58:31 2019

@author: morei
"""

def get_composites(n):
    x = 4
    while x <= n:
        if "np" in ["np" if x % y == 0 else "p" for y in range(2, x)]: # prime checker
            yield x
        x += 1
