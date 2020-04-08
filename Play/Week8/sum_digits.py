# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:16:05 2019

@author: morei
"""

def sum_digits_rec(n):
    sum_ = n % 10
    if n//10 == 0:
        return sum_
    else:
        next_ = n//10
        sum_ += sum_digits_rec(next_)
    return sum_