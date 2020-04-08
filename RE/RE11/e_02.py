# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:23:46 2019

@author: morei
"""

def find_me(f, limits):
    counter = 0
    
    while True:
        mid = (limits[1] + limits[0]) // 2
        val = f(mid)
        print(limits, mid)
        if val == 0:
            return counter
        elif val == -1:
            limits = (limits[0], mid)
        else:
            limits = (mid, limits[1])
        counter += 1