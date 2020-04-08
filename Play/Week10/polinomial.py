# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:18:26 2019

@author: morei
"""

def evaluate(a, x):
    return sum([a[y] * x ** y for y in range(len(a))])
    