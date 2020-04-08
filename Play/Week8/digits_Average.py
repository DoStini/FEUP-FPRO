# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:06:26 2019

@author: morei
"""
import math


def average(a, b):
    return math.ceil((a + b) / 2)

def digits_average(n):
    if n < 10:
        return n
    else:
        avg = 0
        power = 0
        
        n = recursive_part(avg, n, power)
        val = digits_average(n)
        if val is not None:
            return val
    
    
def recursive_part(avg, n, power):
    if n < 10:
        return avg
    else:
        avg = avg * 10 + average(n%10, (n//10)%10)
        n //= 10
        power += 1
        val = recursive_part(avg, n, power)
        if val is not None:
            return val