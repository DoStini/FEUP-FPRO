# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:45:27 2019

@author: morei
"""
from math import factorial as fac
def pascal(n):
    final = ""
    for i in range(n):
        for j in range(i + 1):
            num = int(fac(i) / (fac(j) * fac(i - j)))
            final += str(num)
            if j != i:
                final += " "
            elif i != n-1:
                final += "\n"
    return final