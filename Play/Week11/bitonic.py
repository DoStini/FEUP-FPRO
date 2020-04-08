# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:33:41 2019

@author: morei
"""

def bitonic_point(f):
    alist = f()

    while len(alist) != 1:
        mid = len(alist)//2
        if alist[mid] > alist[mid-1]:
            alist = alist[mid:]
        else:
            alist = alist[:mid]
    return alist[0]