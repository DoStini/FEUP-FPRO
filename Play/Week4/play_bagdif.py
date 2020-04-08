# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:30:42 2019

@author: morei
"""

def bagdiff(xs, ys):
    for s2 in ys:
        if s2 in xs:
            xs.pop(xs.index(s2))
    return xs