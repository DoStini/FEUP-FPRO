# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:21:08 2019

@author: morei
"""

def comprehensions(i, j):
    a = [x for x in range(i, j+1) if str(x)[-1] == "3" or str(x)[-1] == "8"]
    b = tuple([round(x**1/2) for x in range(i, j+1)])
    c = {x: chr(x) for x in range(i, j+1)}
    return (a, b, c)