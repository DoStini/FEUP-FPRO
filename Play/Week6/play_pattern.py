# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:07:33 2019

@author: morei
"""

def pattern_hunting(l1, l2, p):
    out = []
    for x in range(len(l1)):
        if p in l1[x]:
            out.append(l2[x])
        elif p in l2[x]:
            out.append(l1[x])
    return sorted(out, reverse=True)