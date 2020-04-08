# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:13:55 2019

@author: morei
"""

abc = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
def count_chars(astring):
    c0 = 0
    c1 = 0
    c2 = 0
    for char in astring:
        if char.lower() in list(abc):
            c0 += 1
        elif char in num:
            c1 += 1
        else:
            c2 += 1
    out = (c0, c1, c2)
    return out