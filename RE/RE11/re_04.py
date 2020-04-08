# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:15:35 2019

@author: morei
"""

def bisect(f, n):
    lower, upper = 0, 1
    for x in range(n):
        mid = (lower + upper) / 2
        v = f(mid)
        print((lower, upper), v)
        if v == 0:
            return round(mid, 5)
        elif v * f(lower) > 0:
            lower = mid
        else:
            upper = mid
    return round(mid, 5)