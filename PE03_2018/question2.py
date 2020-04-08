# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:36:01 2019

@author: morei
"""

def evaluate(a, x):
    return sum([a[idx] * x ** idx for idx in range(len(a))])