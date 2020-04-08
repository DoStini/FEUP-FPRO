# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:04:45 2019

@author: morei
"""

def count_zeros(f):
    alist = f()
    low, up= 0, len(alist)
    end = up
    while low < up:
        mid = (low+up)//2
        if alist[mid] == 1:
            low = mid + 1
        else:
            up = mid - 1
    return end - low
        
        
        
        
        
        
        
        
#        if alist[0] == 0 and alist[-1] == 0:
#            return len(alist)
#        else:
#            mid = len(alist)//2
#            if alist[mid] == 0 and alist[mid-1] > 0:
#                alist = alist[mid+1:]
#            elif alist[mid] < 0:
#                alist = alist[:mid-1]
#                