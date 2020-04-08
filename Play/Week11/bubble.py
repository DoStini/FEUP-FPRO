# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:56:10 2019

@author: morei
"""

def bubble_sort(alist):
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(alist)-1):
            if alist[x+1] < alist[x]:
                alist[x], alist[x+1] = alist[x+1], alist[x]
                swapped = True
    return alist    