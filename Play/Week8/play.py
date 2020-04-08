# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:45:09 2019

@author: morei
"""

import math


def average(a, b):
    return math.ceil((a + b) / 2)

def mywhile1(n):
    if n >= 10:
        avg = 0
        power = 0
        n = mywhile2(n, power, avg)
        n = mywhile1(n)
    return n
    
def mywhile2(n, power, avg):
    if n >= 10:
        avg = avg + average(n % 10, (n//10) % 10) * 10**power
        n //= 10
        avg = mywhile2(n-1, power+1, avg)
    return avg

def digits_average(n):
    return mywhile1(n)

#import math
#
#
#def average(a, b):
#    return math.ceil((a + b) / 2)
#
#def digits_average(n):
#    if n < 10:
#        return n
#    else:
#        avg = 0
#        power = 0
#        
#        n = recursive_part(avg, n, power)
#        val = digits_average(n)
#        if val is not None:
#            return val
#    
#    
#def recursive_part(avg, n, power):
#    if n < 10:
#        return avg
#    else:
#        avg = avg * 10 + average(n%10, (n//10)%10)
#        n //= 10
#        power += 1
#        val = recursive_part(avg, n, power)
#        if val is not None:
#            return val