# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:25:55 2019

@author: morei
"""

def longest(s):
    s = s.split()
    len_ = []
    for a in s:
        len_.append(len(a))
    return max(len_)