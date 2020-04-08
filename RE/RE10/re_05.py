# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:25:08 2019

@author: morei
"""

def odd_range(start, stop, step):
    lista = [x for x in range(start, stop) if x % 2 == 1]
    n = 0
    while n < len(lista):
        yield lista[n]
        n += step
        