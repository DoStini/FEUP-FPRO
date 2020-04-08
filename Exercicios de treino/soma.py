# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:21:36 2019

@author: morei
"""

def sum(x):
    if x == 1:
        return 1
    else:
        return x + sum(x-1)