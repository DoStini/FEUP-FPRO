# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:50:32 2019

@author: morei
"""

from functools import reduce


def map_reduce(n1, n2):
    lista = [x**2 for x in range(n1, n2) if x % 2 == 1]
    val = reduce(lambda x, y: x * y if x + y < 50 else x + y, lista)
    return lista