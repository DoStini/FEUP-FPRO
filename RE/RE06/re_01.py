# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:55:15 2019

@author: morei
"""

def jump(l):
    idx = 0
    jumps = 0
    idx = l[idx]
    while idx != -1:
        idx = l[idx]
        jumps += 1
    return jumps
