# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:50:35 2019

@author: morei
"""

def  sparse_dot_product(dict1, dict2):
    set_f = set(dict1.keys()) & set(dict2.keys())
    output = 0
    for x in set_f:
        output += dict1[x] * dict2[x]
    return output