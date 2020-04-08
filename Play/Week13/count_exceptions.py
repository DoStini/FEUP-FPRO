# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:07:48 2020

@author: morei
"""

def count_exceptions(f, n1, n2):
    counter = 0
    for x in range(n1, n2+1):
        try:
            f(x)
        except Exception:
            counter += 1
    return counter