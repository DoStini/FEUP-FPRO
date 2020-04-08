# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:02:00 2019

@author: morei
"""

def logic(s, operations):
    for x in operations:
        if x == "and":
            s = s & operations[x]
        if x == "or":
            s = s | operations[x]
        if x == "not":
            s = operations[x] - s
        if x == "xor":
            s1 = s - (s & operations[x])
            s2 = operations[x] - (s & operations[x])
            s = s1 | s2
    return s