# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:26:51 2019

@author: morei
"""

def evaluate(a, x):
    a = list(map(lambda f: f * x ** a.index(f), a))
    return sum(a)

evaluate = lambda a, x: sum(list(map(lambda f: f * x ** a.index(f), a)))