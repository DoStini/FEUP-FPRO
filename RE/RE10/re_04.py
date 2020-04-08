# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:12:26 2019

@author: morei
"""

def multiples_of7(n):
    x = 0
    while x < n:
        if x % 7 == 0: yield x
        x += 1