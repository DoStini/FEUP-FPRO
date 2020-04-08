# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:47:23 2019

@author: morei
"""
def c(n, r):
    n_ = 1
    for x in range(2, n + 1):
        n_ *= x
    r_ = 1
    for x in range(2, r + 1):
        r_ *= x
    n_r = 1
    for x in range(2, n - r + 1):
        n_r *= x
        
    result = int(n_ / (r_ * n_r))
    return(result)