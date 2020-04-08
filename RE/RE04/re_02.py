# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:51:11 2019

@author: morei
"""

def is_perfect(n):
    sum = 0
    if(n < 1):
        return(False)
    for x in range(1, n):
        if (n % x == 0):
            sum += x
    return(sum == n)
print(is_perfect(0))