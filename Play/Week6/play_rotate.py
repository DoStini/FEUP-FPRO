# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:08:07 2019

@author: morei
"""

def rotate_list(l):
    result = l.copy()
    for x in range(len(l)):
        result[x-3] = l[x]
    return result