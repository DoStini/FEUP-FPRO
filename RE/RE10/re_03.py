# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:56:28 2019

@author: morei
"""

def brute_force(f, l):
    return [str(x) + str(y) + str(z) for x in l for y in l for z in l if f(str(x) + str(y) + str(z))]