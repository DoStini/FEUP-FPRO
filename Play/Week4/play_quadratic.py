# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:45:22 2019

@author: morei
"""
import math


def solver(a, b, c):
    in_ = b**2 -4*a*c
    if in_ < 0:
        return([])
    elif in_ == 0:
        return([(-b + math.sqrt(in_))/(2*a)])
    else:
        b1 = (-b - math.sqrt(in_))/(2*a)
        b2 = (-b + math.sqrt(in_))/(2*a)
        out = [b1, b2] if b1 < b2 else [b2, b1]
        return(out)