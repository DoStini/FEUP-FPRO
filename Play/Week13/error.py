# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:58:30 2020

@author: morei
"""

def m(n1, n2):
    if n2 == 1:
        return n1
    else:
        return n1 + m(n1, n2-1)